import re, random, itertools
from language_definition.phones.vowels import Vowel
from language_definition.phones.pulmonic_consonants import PulmonicConsonant


class RuleChange:
    def __init__(self, orig, target, ctxt):
        self.target = self.sub_target(
            ctxt, target if isinstance(target, str) else random.choice(target)
        )
        context = self.sub_context(ctxt, orig)

        ctr_v = 0
        while "V" in context:
            context = re.sub(
                "V",
                f"(?P<v{str(ctr_v)}>[{''.join([v.ipa for v in Vowel if not v.is_long])}:])",
                context,
                count=1,
            )
            self.target = self.target.replace("V", f"\g<v{str(ctr_v)}>", 1)
            ctr_v += 1

        ctr_c = 0
        while "C" in context:
            context = re.sub(
                "C",
                f"(?P<c{str(ctr_c)}>[{''.join([c.ipa for c in PulmonicConsonant])}:])",
                context,
                count=1,
            )
            self.target = self.target.replace("C", f"\g<c{str(ctr_c)}>", 1)
            ctr_c += 1

        self.context = re.compile(context)

    @classmethod
    def from_data(cls, ctx, target):
        cls.target = target
        cls.context = ctx
        return cls

    def sub_context(self, ctxt, to_sub):
        if ctxt == "_":  # replace all
            context = to_sub
        else:
            if ctxt[0] == "#":
                context = "^" + re.sub("_", to_sub, ctxt[1:])
            elif ctxt[-1] == "#":
                context = re.sub("_", to_sub, ctxt[:-1]) + "$"
            else:
                context = re.sub("_", to_sub, ctxt)
        return context

    def sub_target(self, ctxt, to_sub):
        if ctxt == "_":  # replace all
            context = to_sub
        else:
            if ctxt[0] == "#":
                context = re.sub("_", to_sub, ctxt[1:])
            elif ctxt[-1] == "#":
                context = re.sub("_", to_sub, ctxt[:-1])
            else:
                context = re.sub("_", to_sub, ctxt)
        return context

    def __str__(self):
        return str(self.context) + " => " + self.target

    def __repr__(self):
        return "RuleChange: " + self.__str__()


class RuleChangeApplier:
    def __init__(self, file_path, num_rules):
        possible_changes = []
        with open(file_path) as f:
            for line in f:
                cur_change = []
                if line[0] == "!":
                    continue
                try:
                    line, comment = line.split("!!")
                except ValueError:
                    line = line.strip("\n")
                    comment = ""
                rules = line.split("&&")
                for rule in rules:
                    src, trg, ctx = rule.split("/")
                    src = src.split(",")
                    for s in src:
                        cur_change.append(RuleChange(s, trg.split(","), ctx))
                possible_changes.append(cur_change)

        self.changes = list(
            itertools.chain(*random.sample(possible_changes, num_rules))
        )

    def apply_changes(self, word_list):
        result = []
        for word in word_list:
            for rule in self.changes:
                word = re.sub(rule.context, rule.target, word)
            result.append(word)
        return result

    @classmethod
    def from_file(cls, path):
        cls.changes = []
        with open(path) as f:
            for line in f:
                context, target = line.split(";")
                cls.changes.append(RuleChange.from_data(context, target))
        return cls

    def save_change(self, path):

        with open(path, "w") as f:
            for rule in self.changes:
                f.write(str(rule.context) + ";" + str(rule.target) + "\n")
