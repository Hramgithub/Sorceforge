"""Apply the high-confidence findings of the logic audit (owner approved 2026-10-30).

1.1 form_of -> instance_of for named individuals; 1.2 Black Sphinx drops form_of;
1.3 Order informers: servitor_of Dagon and Hydra -> works_for Robert Marsh;
1.4 pets: servitor_of a person -> works_for; 2.1 Innsmouth hybrids get instance_of;
3.1 houses named after residents get «Дом …» names, person names leave house aliases;
4.2 people buried, depicted or mentioned at a place move from residents to refs.
(4.1 Y'ha-nthlei was fixed earlier by R-80.)
"""
import glob
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

records = {}
for f in glob.glob("kb/**/*.json", recursive=True):
    with open(f, encoding="utf-8") as fh:
        d = json.load(fh)
    if isinstance(d, dict) and "id" in d:
        records[d["id"]] = (f, d)
changed = set()


def rec(rid):
    return records[rid][1]


def touch(rid):
    changed.add(rid)


# 1.1
for short in ["brown-jenkin", "mr-shiny", "the-five-watchers", "ghadamon", "dho-spawn",
              "zoth-syra-and-yoth-kala", "dagon-i-gidra"]:
    d = rec("coc:creature:" + short)
    n = 0
    for r in d["relations"]:
        if r["type"] == "form_of":
            r["type"] = "instance_of"
            n += 1
    assert n == 1, short
    touch(d["id"])

# 1.2
d = rec("masks-of-nyarlathotep-en/creature/black-sphinx")
before = len(d["relations"])
d["relations"] = [r for r in d["relations"] if r["type"] != "form_of"]
assert len(d["relations"]) == before - 1
touch(d["id"])

# 1.3
ROBERT = "pobeg-iz-innsmuta-ru/character/robert-marsh"
assert ROBERT in records
for short in ["dzho-sardzhent", "kermit-allen-rouz", "moyra-pirs"]:
    d = rec("pobeg-iz-innsmuta-ru/character/" + short)
    n = 0
    for r in d["relations"]:
        if r["type"] == "servitor_of" and r["target"] == "coc:creature:dagon-i-gidra":
            r["type"], r["target"] = "works_for", ROBERT
            n += 1
    assert n == 1, short
    touch(d["id"])

# 1.4
for short in ["hetep", "fog-spawn"]:
    d = rec("masks-of-nyarlathotep-en/creature/" + short)
    n = 0
    for r in d["relations"]:
        if r["type"] == "servitor_of" and records[r["target"]][1]["kind"] == "character":
            r["type"] = "works_for"
            n += 1
    assert n == 1, short
    touch(d["id"])

# 2.1
for short in ["brittani-eliot", "charlz-gilman", "darold-eliot", "dzho-sardzhent", "ken-martin",
              "kermit-allen-rouz", "kharris-dzheyks", "margaret-bebson", "morgan-eliot", "moyra-pirs",
              "sendi-lane", "uorren-billingem", "vera-sautuik"]:
    d = rec("pobeg-iz-innsmuta-ru/character/" + short)
    rels = d.setdefault("relations", [])
    assert not any(r["type"] == "instance_of" for r in rels), short
    rels.insert(0, {"type": "instance_of", "target": "coc:creature:deep-one-hybrid",
                    "note": "гибрид глубоководных"})
    touch(d["id"])

# 3.1
L = "coc:location:innsmouth-"
NAMES = {
    "1004-enni-pernell": "Дом Энни Пернелл",
    "1005-chakhlyy-gibrid": "Заброшенная ферма",
    "1006-nik-kasper": "Хижина Ника Каспера",
    "102-zhilets-doma-na-fish-strit": "Заброшенный дом на Фиш-стрит",
    "607-deniel-mauri": "Дом Даниэла Моури",
    "610-otis-fuller": "Дом Отиса Фуллера",
    "713-moyra-pirs": "Дом Мойры Пирс",
    "801-abrakham-sautuik": "Дом Абрахама Саутуика",
    "803-dzho-sardzhent": "Дом Джо Сарджента",
}
for short, name in NAMES.items():
    rec(L + short)["name"]["ru"] = name
    touch(L + short)
for short in ["301-charlz-trokmorton", "302-barnabas-starik-marsh", "304-sebastyan-marsh",
              "305-tomas-ueyt", "306-uorren-billingem", "401-sintiya-dzhenks-gilman",
              "403-lester-devis", "405-uilyam-genri-parker-iii", "607-deniel-mauri"]:
    d = rec(L + short)
    assert d.get("aliases"), short
    del d["aliases"]
    touch(d["id"])

# 4.2
OBED = "pobeg-iz-innsmuta-ru/character/obed-marsh"
EFRAIM = "pobeg-iz-innsmuta-ru/character/efraim-ueyt"
for short, people in [("211-kladbishche-kraystcherch", [OBED, EFRAIM]),
                      ("609-memorial-obeda-marsha", [OBED]),
                      ("709-pervaya-unitarianskaya-tserkov-innsmuta", [OBED])]:
    d = rec(L + short)
    kept = [r for r in d["residents"] if r["id"] not in people]
    assert len(kept) == len(d["residents"]) - len(people), short
    if kept:
        d["residents"] = kept
    else:
        del d["residents"]
    refs = d.setdefault("refs", [])
    for p in people:
        if p not in refs:
            refs.insert(0, p)
    touch(d["id"])

for rid in sorted(changed):
    f, d = records[rid]
    with open(f, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f)
print(len(changed), "files")
