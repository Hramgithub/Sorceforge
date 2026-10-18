"""Step 3 of the creatures slice: check migrated kb/creatures records against the book.

For each record, takes the physical page from sources[0] and looks at pages p-1..p+2
(stat blocks often spill to the next page or sit in a neighbouring column). Checks:
- the creature name (first word of name.ru) occurs on those pages (validates the page offset);
- every number the record states (characteristics, HP, MP, build, move, armor, attack and
  dodge percents with half/fifth, skill percents, dice in damage and sanity loss) occurs
  in the page text (numbers and dice normalised as in the rules core check).

Writes a JSON report; no book text is stored.

Usage: python check_creatures.py --kb kb/creatures --pages <pdf_text dir> --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "20261017-rules-core" / "scripts"))
from check_entries import norm, numbers, tokens  # noqa: E402


def record_numbers(rec: dict) -> set[str]:
    sb = rec["statblock"]
    parts: list[str] = []
    for c in sb.get("characteristics", {}).values():
        parts.append(c.get("raw", ""))
    for key in ("hp", "mp", "build", "armor", "damage_bonus"):
        if isinstance(sb.get(key), dict):
            parts.append(sb[key].get("raw", ""))
    if isinstance(sb.get("move"), dict):
        parts.append(sb["move"].get("raw", ""))
    for a in sb.get("attacks", []):
        parts.append(a["chance"].get("raw", ""))
        if a.get("damage"):
            parts.append(a["damage"].get("raw", ""))
    if sb.get("dodge"):
        parts.append(sb["dodge"].get("raw", ""))
    for s in sb.get("skills", []):
        parts.append(s["value"].get("raw", ""))
    for s in sb.get("sanity_loss", []):
        parts.append(f"{s['success']} {s['fail']}".replace("d", "к"))
    out: set[str] = set()
    for p in parts:
        out |= numbers(p.replace("d", "к"))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, required=True)
    ap.add_argument("--pages", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--book-id", default=None, help="check against this source (default: first source of each record)")
    ap.add_argument("--window", default="-1,0,1,2", help="page offsets to look at")
    ap.add_argument("--name-lang", default="ru", choices=["ru", "en"])
    a = ap.parse_args()
    raw_pages = {int(f.stem[1:]): f.read_text(encoding="utf-8") for f in a.pages.glob("p*.txt")}
    offsets = [int(x) for x in a.window.split(",")]
    results = []
    for f in sorted(a.kb.glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        src = next((s for s in rec["sources"] if a.book_id in (None, s["book_id"])), None)
        if src is None:
            continue
        page = src.get("physical_page")
        window = [page + o for o in offsets if page and page + o in raw_pages] if page else []
        text = "\n".join(raw_pages[p] for p in window)
        page_nums = numbers(text)
        if a.name_lang == "en":
            words = [w for w in (rec["name"].get("en") or "").lower().split() if len(w) >= 4]
            name_found = bool(words) and all(w[:5] in text.lower() for w in words)
        else:
            name_tok = (tokens(rec["name"]["ru"]) or [""])[0]
            name_found = bool(name_tok) and name_tok[:6] in norm(text)
        want = record_numbers(rec)
        missing = sorted(want - page_nums)
        recall = round(1 - len(missing) / len(want), 3) if want else 1.0
        status = "ok" if name_found and not missing else ("page_not_confirmed" if not name_found else "numbers_missing")
        results.append({"id": rec["id"], "name": rec["name"]["ru"], "physical_page": page, "name_found": name_found,
                        "numbers": len(want), "recall": recall, "missing": missing, "status": status,
                        "flags": rec.get("quality", {}).get("flags", [])})
    summary: dict[str, int] = {}
    for r in results:
        summary[r["status"]] = summary.get(r["status"], 0) + 1
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps({"summary": summary, "results": results}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
