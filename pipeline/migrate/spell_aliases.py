"""Add Russian spell names from the web helper to `aliases` of kb/spells (R-52).

For every spell record linked to helper ids (`helper_id`, `merged_helper_ids` in
checks/20261023-spells/spell_inventory.jsonl) the script adds, if missing:
the helper title, its Cyrillic aliases, and the names under which grimoires
list the spell («Вызвать крылатого» for Summon/Bind Byakhee). English
alternative names come from Grand Grimoire and are not taken from the helper.

    python pipeline/migrate/spell_aliases.py [--write]
"""
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HELPER = r"C:\_Hobby\_work\git_coc\web_helper_coc_gm\public\docs\magic\data"
CYR = re.compile(r"[А-Яа-яЁё]")


def main():
    write = "--write" in sys.argv
    owner = {}
    for line in open("checks/20261023-spells/spell_inventory.jsonl", encoding="utf-8"):
        r = json.loads(line)
        for h in [r.get("helper_id")] + (r.get("merged_helper_ids") or []):
            if h:
                owner[h] = r["slug"]
    names = {}  # slug -> list of names
    for f in glob.glob(HELPER + r"\spell-details\*.json"):
        d = json.load(open(f, encoding="utf-8"))
        slug = owner.get(d["id"])
        if not slug:
            continue
        for n in [d.get("title"), d.get("originalTitle")] + (d.get("aliases") or []) + (d.get("alternativeNames") or []):
            if n and CYR.search(n) and "alias of" not in n:
                names.setdefault(slug, []).append(n.strip())
    for f in glob.glob(HELPER + r"\grimoire-details\*.json"):
        g = json.load(open(f, encoding="utf-8"))
        for s in g.get("learnableSpells") or []:
            slug = owner.get(s.get("spellId"))
            n = s.get("nameInGrimoire")
            if slug and n and CYR.search(n):
                names.setdefault(slug, []).append(n.strip())
    added = files = 0
    for slug, ns in sorted(names.items()):
        p = f"kb/spells/{slug}.json"
        d = json.load(open(p, encoding="utf-8"))
        have = {d["name"]["ru"].lower(), (d["name"].get("en") or "").lower()} | {a.lower() for a in d.get("aliases") or []}
        new = []
        for n in ns:
            if n.lower() not in have:
                have.add(n.lower())
                new.append(n)
        if new:
            d["aliases"] = (d.get("aliases") or []) + new
            added += len(new)
            files += 1
            print(slug, "+", new)
            if write:
                with open(p, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"aliases added {added} in {files} records ({'written' if write else 'dry run'})")


if __name__ == "__main__":
    main()
