"""Scratch-clone only: apply the union of discovered CRLF-identity paths, verify that each
working file's bytes now equal its CRLF identity and that blob ids are unchanged, and write
the final registry candidate.

Usage: python -I eol_apply_final.py <scratch_clone_root> <eol_iterate_json> <lineage_json> <out_json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

CLONE = Path(sys.argv[1])
assert "scratchpad" in str(CLONE)
iterated = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
lineage = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
OUT = Path(sys.argv[4])
MARK = "# EXPERIMENT (scratch only): sealed CRLF working-byte identity"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(CLONE), *args], capture_output=True, text=True, check=True).stdout


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


paths = sorted(set(iterated["crlf_identity_paths"]) | {row["predecessor"] for row in lineage})
attrs = CLONE / "Sourcefold" / ".gitattributes"
git("checkout", "--", "Sourcefold/.gitattributes")
blob_before = {p: git("ls-files", "-s", "--", p).split()[1] for p in paths}
lf_bytes = {p: subprocess.run(["git", "-C", str(CLONE), "show", f"HEAD:{p}"], capture_output=True, check=True).stdout for p in paths}
with attrs.open("a", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(["", MARK] + [p.removeprefix("Sourcefold/") + " text eol=crlf" for p in paths]) + "\n")
git("rm", "-q", "--cached", "--", *paths)
git("checkout", "HEAD", "--", *paths)

registry = []
for p in paths:
    work = (CLONE / p).read_bytes()
    lf = lf_bytes[p]
    expected_crlf = lf.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    nri_rev = subprocess.run(["git", "-C", "C:/_Hobby/_work/NRI", "log", "--format=%h %cs", "--", p], capture_output=True, text=True).stdout.split("\n")[0]
    registry.append({
        "path": p,
        "git_blob": blob_before[p],
        "git_lf_sha256": sha(lf),
        "sealed_crlf_sha256": sha(expected_crlf),
        "working_bytes_equal_crlf": work == expected_crlf,
        "lf_input_had_no_cr": b"\r" not in lf,
        "nri_first_commit": nri_rev,
    })
blob_after = {p: git("ls-files", "-s", "--", p).split()[1] for p in paths}
OUT.write_text(json.dumps(registry, indent=2), encoding="utf-8")
print("paths:", len(paths))
print("working bytes == crlf identity:", sum(r["working_bytes_equal_crlf"] for r in registry))
print("lf blobs contain no CR:", all(r["lf_input_had_no_cr"] for r in registry))
print("blob ids unchanged:", blob_before == blob_after)
print("status:", git("status", "--short").strip().splitlines())
