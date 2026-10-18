"""Find where each Malleus-sourced creature appears in the Keeper Rulebook (chapter 14).

For every record with a malleus-keeper-deck-en source, scans physical pages 256-321 of the
rulebook text layer. A page qualifies if the Russian name stem occurs on it or the next page
and the page pair carries a stat block. Among qualifying pages, the one with the best recall
of the record's characteristic averages is chosen. Output: JSON with page, recall and verdict:
- "in_rulebook"   recall >= 0.6 — same creature with comparable numbers;
- "weak"          name found but numbers mostly differ (check by eye);
- "not_found"     no qualifying page — probably not in the Keeper Rulebook.

Usage: python locate_in_rulebook.py --kb kb/creatures --pages <pdf_text dir> --out <json>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "20261017-rules-core" / "scripts"))
from check_entries import norm, numbers, tokens  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, required=True)
    ap.add_argument("--pages", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    pages = {int(f.stem[1:]): f.read_text(encoding="utf-8") for f in a.pages.glob("p*.txt")}
    ch14 = [p for p in range(256, 322) if p in pages]
    results = []
    for f in sorted(a.kb.glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        if not any(s["book_id"] == "malleus-keeper-deck-en" for s in rec["sources"]):
            continue
        want = set()
        for c in rec["statblock"]["characteristics"].values():
            want |= numbers(c.get("raw", ""))
        stem = (tokens(rec["name"]["ru"]) or [""])[0][:6]
        best = None
        for p in ch14:
            pair = pages[p] + "\n" + pages.get(p + 1, "")
            if not stem or stem not in norm(pair) or not re.search(r"СИЛ\s+\d", pair):
                continue
            recall = len(want & numbers(pair)) / len(want) if want else 0
            if best is None or recall > best[1]:
                best = (p, recall)
        if best is None:
            verdict, page, recall = "not_found", None, 0.0
        else:
            page, recall = best
            verdict = "in_rulebook" if recall >= 0.6 else "weak"
        recorded = next(s.get("physical_page") for s in rec["sources"] if s["book_id"] == "keeper-rulebook-ru") \
            if any(s["book_id"] == "keeper-rulebook-ru" for s in rec["sources"]) else None
        results.append({"id": rec["id"], "name": rec["name"]["ru"], "verdict": verdict, "page": page,
                        "recall": round(recall, 2), "recorded_page": recorded})
    a.out.write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in results:
        print(f"{r['verdict']:12} {r['id'].split(':')[-1]:32} page {r['page']} (recorded {r['recorded_page']}) recall {r['recall']}")


if __name__ == "__main__":
    main()
