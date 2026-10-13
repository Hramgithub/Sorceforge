"""Scratch-clone experiment only: add `text eol=crlf` for the line-ending identity
paths to Sourcefold/.gitattributes, re-materialize them from HEAD, and verify that
working bytes equal the sealed hashes while blob ids stay unchanged.

Usage: python -I eol_experiment.py <scratch_clone_root> <lineage_json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

CLONE = Path(sys.argv[1])
rows = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
assert "scratchpad" in str(CLONE), "refusing to run outside the scratch clone"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(CLONE), *args], capture_output=True, text=True, check=True).stdout


git("checkout", "--", ".gitattributes", "Sourcefold/.gitattributes")
paths = sorted({row["predecessor"] for row in rows})
blobs_before = {p: git("ls-files", "-s", "--", p).split()[1] for p in paths}

attrs = CLONE / "Sourcefold" / ".gitattributes"
lines = ["", "# EXPERIMENT (scratch only): sealed CRLF working-byte identity"]
lines += [p.removeprefix("Sourcefold/") + " text eol=crlf" for p in paths]
with attrs.open("a", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")

git("rm", "-q", "--cached", "--", *paths)
git("checkout", "HEAD", "--", *paths)

ok = 0
for row in rows:
    data = (CLONE / row["predecessor"]).read_bytes()
    if hashlib.sha256(data).hexdigest().upper() == row["recorded"]:
        ok += 1
    else:
        print("still mismatched:", row["predecessor"])
blobs_after = {p: git("ls-files", "-s", "--", p).split()[1] for p in paths}
print(f"rows matching sealed hash: {ok}/{len(rows)}")
print("blob ids unchanged:", blobs_before == blobs_after)
print("git status:", git("status", "--short").strip().splitlines())
