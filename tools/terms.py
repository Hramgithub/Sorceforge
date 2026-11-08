"""The glossary (Р-184): look a word up, list what needs the owner's word, export for other projects.

The Russian term is chosen by priority: official localization > the owner's registry > trusted fan translation > ours.
Lookup searches the glossary (kb/terms) and the names of all records, so a translator finds both «Pushing the Roll»
(rule) and «Hardened» (talent).

Usage:
  python tools/terms.py <word>            English or Russian, any part of the word
  python tools/terms.py --review          terms that wait for the owner (status review), by domain
  python tools/terms.py --export <file>   CSV in the columns of CoC_Terminology_Decisions.csv (for other projects)
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter

from kblib import records

BY = {"official": "офиц.", "owner": "реестр", "trusted": "фан.", "ours": "наш", "rejected": "отвергнут"}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("word", nargs="?")
    ap.add_argument("--review", action="store_true")
    ap.add_argument("--export")
    a = ap.parse_args()
    recs = [r for _, r in records()]
    terms = [r for r in recs if r.get("kind") == "term"]
    if a.export:
        with open(a.export, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["source_term", "accepted_ru", "aliases", "bad_ru", "domain", "status", "source_scope", "decision_rule", "notes"])
            for t in sorted(terms, key=lambda t: (t["name"]["en"] or t["name"]["ru"]).lower()):
                w.writerow([t["name"]["en"] or "", t["name"]["ru"], ";".join(t.get("aliases") or []), ";".join(t.get("avoid") or []),
                            t.get("domain") or "", "accepted" if t["status"] == "accepted" else "review_required", t.get("scope") or "",
                            f"sourcefold_{t['chosen_by']}", ((t.get("definition") or {}).get("ru") or "")])
        print(f"{len(terms)} терминов → {a.export}")
        return 0
    if a.review:
        rv = [t for t in terms if t["status"] == "review"]
        print(f"ждут владельца: {len(rv)} из {len(terms)}; по областям: {dict(Counter(t.get('domain') for t in rv).most_common())}")
        return 0
    if not a.word:
        ap.print_help()
        return 1
    q = a.word.lower()
    for t in terms:
        names = [t["name"]["en"], t["name"]["ru"], *(t.get("aliases") or []), *(v["ru"] for v in t.get("variants") or [])]
        if any(q in (n or "").lower() for n in names):
            vs = "; ".join(f"{v['ru']} ({BY.get(v['by'], v['by'])})" for v in t.get("variants") or [])
            print(f"[термин] {t['name']['en'] or '—'} → {t['name']['ru']}  ({BY[t['chosen_by']]}, {t['status']}{', ' + t['scope'] if t.get('scope') else ''})")
            if vs:
                print(f"         варианты: {vs}")
            if t.get("avoid"):
                print(f"         не писать: {', '.join(t['avoid'])}")
    for r in recs:
        if r.get("kind") == "term":
            continue
        n = r.get("name") or {}
        if any(q in (x or "").lower() for x in (n.get("en"), n.get("ru"))):
            tr = "наш перевод" if "translated" in ((r.get("quality") or {}).get("flags") or []) else "по книге"
            print(f"[{r.get('kind')}] {n.get('en') or '—'} → {n.get('ru')}  ({tr}; {r['id']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
