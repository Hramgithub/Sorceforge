"""Link statblock attacks to the weapon reference (R-59).

Reads the attack map (jsonl: id, index, name, weapon) made when the weapon
reference was built (`checks/20261024-weapons/attack_weapons.jsonl`) and sets
`statblock.attacks[index].weapon` = `coc:weapon:<slug>` when the printed attack
name matches and the weapon record exists. Names and numbers are not changed.

    python pipeline/migrate/link_weapons.py [--write] [map.jsonl]
"""
import glob
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")


def main():
    write = "--write" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else "checks/20261024-weapons/attack_weapons.jsonl"
    amap = {}
    for line in open(path, encoding="utf-8"):
        if line.strip():
            m = json.loads(line)
            if m.get("weapon"):
                amap[(m["id"], m["index"])] = (m["name"], "coc:weapon:" + m["weapon"])
    weapons = {json.load(open(f, encoding="utf-8"))["id"] for f in glob.glob("kb/weapons/*.json")}
    files = glob.glob("kb/creatures/*.json") + glob.glob("kb/characters/*.json") + glob.glob("kb/books/*/*/*.json")
    linked = skipped = changed = 0
    for f in sorted(files):
        d = json.load(open(f, encoding="utf-8"))
        attacks = (d.get("statblock") or {}).get("attacks") or []
        dirty = False
        for i, a in enumerate(attacks):
            hit = amap.get((d["id"], i))
            if not hit:
                continue
            name, wid = hit
            if a["name"]["ru"] != name or wid not in weapons:
                skipped += 1
                print("skip:", d["id"], i, a["name"]["ru"], "->", wid)
                continue
            linked += 1
            if a.get("weapon") != wid:
                # keep key order: weapon goes after damage
                attacks[i] = {k: v for k, v in a.items() if k != "notes"} | {"weapon": wid} | ({"notes": a["notes"]} if "notes" in a else {})
                dirty = True
        if dirty:
            changed += 1
            if write:
                with open(f, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"linked {linked}, skipped {skipped}, records {'written' if write else 'to change'}: {changed}")


if __name__ == "__main__":
    main()
