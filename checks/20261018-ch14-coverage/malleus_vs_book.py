import json, re, sys, pathlib
helper = pathlib.Path(sys.argv[1]); pages = pathlib.Path(sys.argv[2])
txt = {int(p.stem[1:]): p.read_text(encoding="utf-8") for p in pages.glob("p*.txt") if 256 <= int(p.stem[1:]) <= 321}
def norm(s): return re.sub(r"[^а-я ]+", " ", (s or "").lower().replace("ё","е"))
rows = []
for p in sorted(helper.glob("*.json")):
    j = json.loads(p.read_text(encoding="utf-8"))
    if j.get("source_set") != "malleus_keeper_deck_65": continue
    name = j.get("name") or ""
    stems = [w[:6] for w in norm(name).split() if len(w) >= 4] or [norm(name).strip()[:6]]
    hits = [pg for pg, t in sorted(txt.items()) if all(s in norm(t) for s in stems)]
    stat = [pg for pg in hits if re.search(r"СИЛ\s+\d", txt[pg])]
    rows.append((p.stem, name, j.get("name_en"), stat[:3], hits[:3]))
inbook = [r for r in rows if r[3]]
out = [f"malleus cards: {len(rows)}; found with stat block in ch14: {len(inbook)}"]
out += [f"  {r[0]} | {r[1]} | {r[2]} | stat pages {r[3]}" for r in inbook]
out += ["not found in ch14:"] + [f"  {r[0]} | {r[1]} | mentions {r[4]}" for r in rows if not r[3]]
pathlib.Path(sys.argv[3]).write_text("\n".join(out), encoding="utf-8")
