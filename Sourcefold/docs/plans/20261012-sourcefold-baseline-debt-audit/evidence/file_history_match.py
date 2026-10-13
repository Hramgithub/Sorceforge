"""Read-only: list NRI history versions of a path and mark which (LF/CRLF) hash equals a recorded value.

Usage: python -I file_history_match.py <nri_repo> <repo_relative_path> <recorded_sha256> [<current_file>]
"""
import hashlib
import subprocess
import sys
from pathlib import Path

NRI, REL, RECORDED = sys.argv[1], sys.argv[2], sys.argv[3].upper()


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


def ids(b: bytes) -> dict:
    lf = b.replace(b"\r\n", b"\n")
    return {"lf": sha(lf), "crlf": sha(lf.replace(b"\n", b"\r\n"))}


if len(sys.argv) > 4:
    cur = ids(Path(sys.argv[4]).read_bytes())
    print("current", cur["lf"][:12], cur["crlf"][:12], [k for k, h in cur.items() if h == RECORDED])
log = subprocess.run(["git", "-C", NRI, "log", "--format=%H %cs %s", "--", REL], capture_output=True, text=True).stdout
for line in log.splitlines():
    rev, date, subject = line.split(" ", 2)
    blob = subprocess.run(["git", "-C", NRI, "show", f"{rev}:{REL}"], capture_output=True).stdout
    v = ids(blob)
    print(rev[:10], date, v["lf"][:12], [k for k, h in v.items() if h == RECORDED], subject[:80])
