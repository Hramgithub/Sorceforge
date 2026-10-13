"""Read-only: for the 12 failing lineage tests, check which consumer reports pin the
hash of their own test file or generator script, and whether that pin is LF or CRLF.

Usage: python -I self_pins.py <lineage_json> <repo_root>
"""
import hashlib
import json
import sys
from pathlib import Path

rows = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
REPO = Path(sys.argv[2])


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


def ident(path: Path) -> dict:
    b = path.read_bytes()
    lf = b.replace(b"\r\n", b"\n")
    return {"lf": sha(lf), "crlf": sha(lf.replace(b"\n", b"\r\n"))}


seen = set()
for row in rows:
    consumer = REPO / row["consumer"]
    if consumer in seen:
        continue
    seen.add(consumer)
    report = json.loads(consumer.read_text(encoding="utf-8-sig"))
    test_file = REPO / "Sourcefold" / row["test"].split("::")[0]
    out = []
    for key, value in report.items():
        if not (isinstance(value, str) and len(value) == 64 and key.endswith("sha256")):
            continue
        if "test" in key:
            target = ident(test_file)
        elif "script" in key or "generator" in key:
            continue
        else:
            continue
        kind = [k for k, h in target.items() if h == value]
        out.append(f"{key}={'/'.join(kind) or 'NO MATCH'}")
    print(Path(row["test"].split("::")[0]).name, "|", ", ".join(out) or "no test self-pin")
