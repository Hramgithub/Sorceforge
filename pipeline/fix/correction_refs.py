"""`corrections[].ref` holds only a decision number (Р-140).

`ref` is the decision a correction was made by («Р-22») or null. A book and page («malleus-monstrorum-2-en p.24»),
a file path or other text found in `ref` moves to the end of `reason` in brackets («…, (malleus-monstrorum-2-en,
с. 24)»), and `ref` becomes the first decision number named in the reason, or null. `from` and `to` never change.

Usage: python pipeline/fix/correction_refs.py (<files|dirs> | --changed | --all) [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import read, scope, scope_args, write  # noqa: E402

DECISION = re.compile(r"^Р-\d+$")
NAMED = re.compile(r"[РR]-(\d+)")
PAGE = re.compile(r"^(?P<book>[a-z0-9-]+)\s+pp?\.\s*(?P<page>\d+(?:\s*[–-]\s*\d+)?)$")


def fix(c: dict) -> bool:
    ref = c.get("ref")
    if ref is not None and DECISION.match(ref):
        return False
    if ref is None:
        named = NAMED.search(c.get("reason") or "")
        if not named:
            return False
        c["ref"] = f"Р-{named.group(1)}"
        return True
    text = (ref or "").strip()
    reason = c.get("reason") or ""
    if text:
        m = PAGE.match(text)
        src = f"{m['book']}, с. {m['page'].replace('-', '–').replace(' ', '')}" if m else text
        if src not in reason and text not in reason:
            reason = f"{reason.rstrip()} ({src})" if reason else src
    named = NAMED.search(reason)
    c["reason"] = reason
    c["ref"] = f"Р-{named.group(1)}" if named else None
    return True


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    scope_args(ap)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = items = 0
    for p in scope(ap, a):
        rec = read(p)
        n = sum(fix(c) for c in rec.get("corrections") or [] if isinstance(c, dict))
        if n:
            files += 1
            items += n
            if not a.dry_run:
                write(p, rec)
    print(f"{items} corrections in {files} files" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
