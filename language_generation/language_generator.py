import random, json
from language_definition.phones.vowels import Vowel
from language_definition.phones.pulmonic_consonants import (
    PulmonicConsonant,
    Manner,
    OBSTRUENTS,
    SONORANTS,
)


class Generator:
    def __init__(self, lang_json, vocab_size):
        consonants = lang_json["phones"]["mandatory"]["consonants"]
        vowels = lang_json["phones"]["mandatory"]["vowels"]

        consonants += self.sub_sample(
            lang_json["phones"]["possible"]["consonants"],
            len(consonants) + len(vowels),
            vocab_size,
        )
        self.consonants = [PulmonicConsonant[c] for c in consonants]

        vowels += self.sub_sample(
            lang_json["phones"]["possible"]["vowels"], 
            len(consonants) + len(vowels), vocab_size
        )
        self.vowels = [Vowel[v] for v in vowels]

        self.syllable_num = lang_json["phonotactics"]["syllables_number"]
        self.clusters_ini = lang_json["phonotactics"]["clusters"]["initial"]
        self.clusters_mid = lang_json["phonotactics"]["clusters"]["middle"]
        self.clusters_fin = lang_json["phonotactics"]["clusters"]["final"]

    def sub_sample(self, samp_list, cur_num_letters, vocab_size):
        upper_range = min(
            int((vocab_size - cur_num_letters) * 2 / 3), len(samp_list)
        )
        return random.sample(samp_list, random.randint(0, upper_range))

    def generate_phonetic_list(self, num_items):
        result = []
        while len(result) < num_items:
            word = ""
            cur_syllab_num = random.choice(self.syllable_num)
            word += self.generate_phonetic_syllable(
                random.choice(random.choice(self.clusters_ini))
            )
            if cur_syllab_num > 1:
                for _ in range(cur_syllab_num - 2):
                    word += self.generate_phonetic_syllable(
                        random.choice(random.choice(self.clusters_mid))
                    )
                word += self.generate_phonetic_syllable(
                    random.choice(random.choice(self.clusters_fin))
                )
            if word not in result:
                result.append(word)
        return result

    def generate_phonetic_syllable(self, shape):
        result = ""
        for symbol in shape:
            if symbol == "V":
                result += random.choice(self.vowels).ipa
            elif symbol == "C":
                result += random.choice(self.consonants).ipa
            elif symbol == "P":  # plosives/stops
                result += random.choice(
                    [c for c in self.consonants if c.manner == Manner.STOP]
                ).ipa
            elif symbol == "S":  # sonorant
                result += random.choice(
                    [c for c in self.consonants if c.manner in SONORANTS]
                ).ipa
            elif symbol == "O":  # obstruents: plosive, fricative and affricates
                result += random.choice(
                    [c for c in self.consonants if c.manner in OBSTRUENTS]
                ).ipa
            elif symbol.islower():
                result += symbol
            else:
                print("Unidentified symbol:", symbol)
        return result

    def save_conf(self, path):
        json_res = {
            "phones": {
                "mandatory": {
                    "consonants": [c.ipa for c in self.consonants],
                    "vowels": [v.ipa for v in self.vowels],
                },
                "optional": {"consonants": [], "vowels": []},
            },
            "phonotactics": {
                "syllabe_number": self.syllable_num,
                "clusters": {
                    "initial": self.clusters_ini,
                    "middle": self.clusters_mid,
                    "final": self.clusters_fin,
                },
            },
        }

        with open(path, "w") as outfile:
            json.dump(json_res, outfile)
