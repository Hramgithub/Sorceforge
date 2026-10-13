"""Read-only: for tracked blobs that contain CR, compare raw (as tracked) and CRLF->LF
identities against references elsewhere, and compare with the NRI blob at the export source.

Usage: python -I cr_blob_scan.py <repo> <rev> <nri_repo> <nri_rev> <identity_scan_json> <out_json>
"""
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path, PurePosixPath

REPO, REV, NRI, NRI_REV, SCAN, OUT = sys.argv[1:7]
refs_index: dict[str, list[str]] = {}
scan = json.loads(Path(SCAN).read_text(encoding="utf-8"))


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


def blobs(repo: str, rev: str) -> dict[str, tuple[str, bytes]]:
    listing = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "-z", rev], capture_output=True, check=True).stdout
    entries = []
    for item in listing.split(b"\0"):
        if item:
            meta, path = item.split(b"\t", 1)
            if meta.split()[1] == b"blob":
                entries.append((path.decode("utf-8"), meta.split()[2].decode()))
    proc = subprocess.Popen(["git", "-C", repo, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = {}
    for path, oid in entries:
        proc.stdin.write(oid.encode() + b"\n")
        proc.stdin.flush()
        size = int(proc.stdout.readline().split()[2])
        out[path] = (oid, proc.stdout.read(size))
        proc.stdout.read(1)
    proc.stdin.close()
    return out


import re
HEX = re.compile(rb"(?<![0-9A-Fa-f])[0-9A-Fa-f]{64}(?![0-9A-Fa-f])")
sf = blobs(REPO, REV)
for path, (_oid, data) in sf.items():
    if b"\0" in data:
        continue
    for m in HEX.finditer(data):
        refs_index.setdefault(m.group().decode().upper(), []).append(f"{path}:{data.count(b'\n', 0, m.start()) + 1}")

nri = blobs(NRI, NRI_REV)
rows = []
cls = Counter()
for path, (oid, data) in sorted(sf.items()):
    if b"\0" in data or b"\r" not in data:
        continue
    raw = sha(data)
    lf = sha(data.replace(b"\r\n", b"\n"))
    raw_refs = [r for r in refs_index.get(raw, []) if not r.startswith(path + ":")]
    lf_refs = [r for r in refs_index.get(lf, []) if not r.startswith(path + ":")]
    nri_entry = nri.get(path)
    nri_same = nri_entry is not None and nri_entry[0] == oid
    nri_has_cr = nri_entry is not None and b"\r" in nri_entry[1]
    key = ("raw_sealed" if raw_refs else "") + ("+" if raw_refs and lf_refs else "") + ("lf_sealed" if lf_refs else "") or "unreferenced"
    cls[(key, "nri_blob_same" if nri_same else ("nri_missing" if nri_entry is None else ("nri_blob_has_cr" if nri_has_cr else "nri_blob_lf")))] += 1
    rows.append({"path": path, "blob": oid, "raw_sha256": raw, "lf_sha256": lf, "class": key,
                 "nri_blob_same": nri_same, "nri_blob_has_cr": nri_has_cr, "raw_refs": raw_refs[:5], "lf_refs": lf_refs[:5]})

Path(OUT).write_text(json.dumps({"rev": REV, "nri_rev": NRI_REV, "rows": rows}, indent=2), encoding="utf-8")
print("CR-containing text blobs:", len(rows))
for (k, n), c in sorted(cls.items()):
    print(f"  {k:24s} {n:16s} {c}")
diff = sum(1 for p, (o, _d) in sf.items() if p in nri and nri[p][0] != o)
print("paths whose blob differs from NRI source:", diff, "| missing in NRI:", sum(1 for p in sf if p not in nri))
