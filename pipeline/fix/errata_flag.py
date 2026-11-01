"""The flag `parse_uncertain` («опечатка книги») stands exactly on records that have `errata` (Р-141).

Any kind of record: the flag is added where `errata` is not empty and removed where it is empty or missing.

Usage: python pipeline/fix/errata_flag.py (<files|dirs> | --changed | --all) [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import read, scope, scope_args, write  # noqa: E402


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    scope_args(ap)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    added = removed = 0
    for p in scope(ap, a):
        rec = read(p)
        if not isinstance(rec, dict) or "kind" not in rec:
            continue
        has = bool(rec.get("errata"))
        q = rec.get("quality")
        flags = (q or {}).get("flags") or []
        if has == ("parse_uncertain" in flags):
            continue
        if has:
            q = rec.setdefault("quality", {"needs_review": False, "flags": [], "notes": None})
            q.setdefault("flags", []).append("parse_uncertain")
            added += 1
        else:
            q["flags"] = [f for f in flags if f != "parse_uncertain"]
            removed += 1
        if not a.dry_run:
            write(p, rec)
    print(f"flag added {added}, removed {removed}" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
