"""Fix half and fifth values of percentages that do not follow from the percent (owner decision R-35).

In Call of Cthulhu 7e half = value // 2 and fifth = value // 5. For every percent object
({raw, value, half, fifth}) in creature and character stat blocks (attacks, dodge, skills) whose half
or fifth is wrong, the numbers and the "(half/fifth)" part of raw are set to the computed values, and
the record gets an `errata` item with `fixed: true` keeping what the book printed. Existing errata
items about the same percent are marked fixed instead of adding a duplicate.

Usage: python pipeline/fix/percent_parts.py [--kb kb] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PARTS = re.compile(r"\(\s*\d+\s*[/,]\s*\d+\s*\)")


def percents(sb: dict):
    for a in sb.get("attacks") or []:
        if isinstance(a.get("chance"), dict):
            yield (a.get("name") or {}).get("ru") or "атака", a["chance"]
    if isinstance(sb.get("dodge"), dict):
        yield "Уклонение", sb["dodge"]
    for s in sb.get("skills") or []:
        if isinstance(s.get("value"), dict):
            yield s.get("name") or "навык", s["value"]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=Path(__file__).resolve().parents[2] / "kb")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    fixed = files = 0
    ambiguous: list[str] = []
    for p in sorted(a.kb.rglob("*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        if r.get("kind") not in ("creature", "character") or not r.get("statblock"):
            continue
        changed = False
        for field, v in percents(r["statblock"]):
            val, half, fifth = v.get("value"), v.get("half"), v.get("fifth")
            if not isinstance(val, int) or half is None or fifth is None:
                continue
            h, f = val // 2, val // 5
            if (half, fifth) == (h, f) and not re.search(r"\(\s*\d+\s*,", v.get("raw", "")):
                continue
            printed = v.get("raw", "")
            other = [q for q in range(1, 201) if abs(q - val) >= 5 and q // 2 == half and q // 5 == fifth]
            if (half, fifth) != (h, f) and other:
                # half and fifth both fit a clearly different percent: the percent itself may be the misprint
                ambiguous.append(f"{p.stem}: {field} {printed} (половина и пятая подходят к {other[0]}%)")
                continue
            v["half"], v["fifth"] = h, f
            if PARTS.search(printed):
                v["raw"] = PARTS.sub(f"({h}/{f})", printed, count=1)
            expected = f"{val}% ({h}/{f})"
            errata = r.setdefault("errata", [])
            match = next((e for e in errata if field.lower() in (e.get("field") or "").lower()
                          and re.search(rf"\b{val}\b", (e.get("printed") or "") + (e.get("expected") or ""))), None)
            if match:
                match["fixed"] = True
                match["expected"] = match.get("expected") or expected
            else:
                errata.append({"field": field, "printed": printed, "expected": expected,
                               "note": "половина и пятая не следуют из процента; исправлено по правилу 7-й редакции (Р-35)",
                               "fixed": True})
            fixed += 1
            changed = True
            print(f"{p.stem}: {field} {printed} -> {v['raw']}")
        if changed:
            fl = r.setdefault("quality", {"needs_review": False, "flags": [], "notes": None}).setdefault("flags", [])
            if "parse_uncertain" not in fl:
                fl.append("parse_uncertain")
            files += 1
            if not a.dry_run:
                p.write_bytes((json.dumps(r, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(f"{fixed} percentages fixed in {files} records" + (" (dry run)" if a.dry_run else ""))
    print(f"left as printed, the percent itself may be wrong ({len(ambiguous)}):")
    for line in ambiguous:
        print("  " + line)


if __name__ == "__main__":
    main()
