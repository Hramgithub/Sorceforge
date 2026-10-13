"""Read-only full-scope scan of sealed byte identities at a Git revision.

For every tracked text blob (no NUL byte, contains LF, no CR), compute SHA-256 of the
blob (LF identity) and of its LF->CRLF transform (CRLF identity), then find every
64-hex token in all other tracked text blobs that equals either identity.

Usage: python -I identity_scan.py <repo> <rev> <out_json>
"""
import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO, REV, OUT = sys.argv[1], sys.argv[2], Path(sys.argv[3])
HEX = re.compile(rb"(?<![0-9A-Fa-f])[0-9A-Fa-f]{64}(?![0-9A-Fa-f])")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


listing = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "-z", REV], capture_output=True, check=True).stdout
entries = []
for item in listing.split(b"\0"):
    if not item:
        continue
    meta, path = item.split(b"\t", 1)
    _mode, kind, oid = meta.split()
    if kind == b"blob":
        entries.append((path.decode("utf-8"), oid.decode()))

proc = subprocess.Popen(["git", "-C", REPO, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
blobs = {}
for path, oid in entries:
    proc.stdin.write(oid.encode() + b"\n")
    proc.stdin.flush()
    header = proc.stdout.readline().split()
    size = int(header[2])
    data = proc.stdout.read(size)
    proc.stdout.read(1)
    blobs[path] = (oid, data)
proc.stdin.close()

# token index: hash -> list of (file, line)
refs = defaultdict(list)
for path, (_oid, data) in blobs.items():
    if b"\0" in data:
        continue
    for m in HEX.finditer(data):
        line = data.count(b"\n", 0, m.start()) + 1
        refs[m.group().decode().upper()].append(f"{path}:{line}")

rows = []
counts = defaultdict(int)
for path, (oid, data) in sorted(blobs.items()):
    if b"\0" in data or b"\n" not in data:
        counts["binary_or_single_line"] += 1
        continue
    if b"\r" in data:
        counts["blob_contains_cr"] += 1
        continue
    lf = sha(data)
    crlf = sha(data.replace(b"\n", b"\r\n"))
    lf_refs = [r for r in refs.get(lf, []) if not r.startswith(path + ":")]
    crlf_refs = [r for r in refs.get(crlf, []) if not r.startswith(path + ":")]
    if not lf_refs and not crlf_refs:
        cls = "unreferenced"
    elif crlf_refs and not lf_refs:
        cls = "crlf_only"
    elif lf_refs and not crlf_refs:
        cls = "lf_only"
    else:
        cls = "both"
    counts[cls] += 1
    if cls in ("crlf_only", "both"):
        rows.append({"path": path, "blob": oid, "class": cls, "lf_sha256": lf, "crlf_sha256": crlf,
                     "lf_refs": lf_refs, "crlf_refs": crlf_refs})

OUT.write_text(json.dumps({"rev": REV, "tracked_blobs": len(blobs), "counts": counts, "rows": rows}, indent=2), encoding="utf-8")
print("tracked blobs:", len(blobs))
print(json.dumps(counts, indent=1))
