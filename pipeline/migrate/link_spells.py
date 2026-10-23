"""Link spell names in statblocks to the spell reference (R-52).

Reads the mention map (jsonl: id, items[{name, slug}]) made when the spell
reference was built (`checks/20261023-spells/spell_mentions.jsonl`) and writes
`statblock.spells.items` — every printed spell name in order of appearance, with
`spell` = `coc:spell:<slug>` when the record exists, else null; commentary is
skipped. `raw` is not changed.

    python pipeline/migrate/link_spells.py [--write] [mentions.jsonl]
"""
import glob
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")


def main():
    write = "--write" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else "checks/20261023-spells/spell_mentions.jsonl"
    mentions = {}
    for line in open(path, encoding="utf-8"):
        if line.strip():
            m = json.loads(line)
            mentions[m["id"]] = m["items"]
    spells = {json.load(open(f, encoding="utf-8"))["id"] for f in glob.glob("kb/spells/*.json")}
    files = glob.glob("kb/creatures/*.json") + glob.glob("kb/characters/*.json") + glob.glob("kb/books/*/*/*.json")
    linked = unlinked = missing_name = changed = 0
    for f in sorted(files):
        d = json.load(open(f, encoding="utf-8"))
        sp = (d.get("statblock") or {}).get("spells")
        if not sp or d["id"] not in mentions:
            continue
        raw, pos, items = sp["raw"], 0, []
        found = []
        for it in mentions[d["id"]]:
            i = raw.find(it["name"])
            if i < 0:
                missing_name += 1
                print("name not in raw:", d["id"], it["name"])
                continue
            if not it.get("slug"):
                continue  # commentary («на усмотрение Хранителя», «знает 1d4 заклинаний»), not a spell name
            sid = "coc:spell:" + it["slug"]
            if sid not in spells:
                sid = None
            found.append((i, {"name": it["name"], "spell": sid}))
        # order of appearance; the viewer links names left to right
        for _, it in sorted(found, key=lambda x: x[0]):
            items.append(it)
            linked += it["spell"] is not None
            unlinked += it["spell"] is None
        if sp.get("items", []) != items:
            if items:
                sp["items"] = items
            else:
                sp.pop("items", None)
            changed += 1
            if write:
                with open(f, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"linked {linked}, without spell {unlinked}, names not found {missing_name}, "
          f"records {'written' if write else 'to change'}: {changed}")


if __name__ == "__main__":
    main()
