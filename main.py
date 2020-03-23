import json, os
from datetime import datetime
from language_generation.language_generator import Generator
from language_generation.rule_change_applier import RuleChangeApplier

# FYI - V vowel, C consonnant, S sonorant, O obstruent, P stop

# Daily folder creation
cur_date = datetime.today().strftime("%m_%d")
cur_time = datetime.today().strftime("%H:%M")
cur_date_time = cur_date + "_" + cur_time
for folder in ["output/"]:
    try:
        os.mkdir(folder + cur_date_time + "/")
        os.mkdir(folder + cur_date_time + "/config/")
    except:
        print("Folder already there", folder)

# Configuration
cur_language = json.load(open("data/sound_inventories/italic.json", "r"))
cur_language_change = "data/sound_changes/italic.txt"
num_children = 3
num_words = 200
child_lang_name = "ic"
protolang = []
protolang_children = {}

# Protolanguage generation
g = Generator(cur_language)
print(f"Current generator (proto-language): "
      f"\n  - Vowels = {[v.ipa for v in g.vowels]}"
      f"\n  - Consonnants = {[c.ipa for c in g.consonants]}")

g.save_conf("output/" + cur_date_time + "/config/conf.json")

# Language generation
protolang = g.generate_phonetic_list(num_words)
with open(f"output/{cur_date_time}/protolang", "w") as f:
    f.write("\n".join(protolang))
print("Proto-language generated")

# Successive evolutions
for i in range(num_children):
    a = RuleChangeApplier(cur_language_change, 0 if i == 0 else 15)
    a.save_change(f"output/{cur_date_time}/config/rule_change_{str(i)}.txt")

    protolang_children[child_lang_name + str(i)] = a.apply_changes(protolang)
    print(f"Children {i+1}/{num_children} generated")

# Save function for MOSES and MEDeA input format
keys = list(protolang_children.keys())
for k in keys:
    with open(f"output/{cur_date_time}/{'_'.join(keys)}.{k}", "w") as f:
        with open(f"output/{cur_date_time}/{'_'.join(keys)}.ipa.{k}", "w") as f_ipa:
            f.write("\n".join(protolang_children[k]))
            f_ipa.write("\n".join([str([k] + list(s) + ["EOW"]) for s in protolang_children[k]]))
print("All saved - run done")
