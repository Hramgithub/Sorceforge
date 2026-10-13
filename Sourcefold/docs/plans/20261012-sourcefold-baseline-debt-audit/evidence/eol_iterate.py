"""Scratch-clone only: iterate failing lineage tests, discover every predecessor whose
sealed hash equals its LF->CRLF identity, add it to the scratch eol=crlf list, re-materialize,
and repeat until no new path is found. Writes the final classified list as JSON.

Usage: python -I eol_iterate.py <scratch_clone_root> <python_exe> <basetemp> <out_json> <node_id>...
"""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CLONE = Path(sys.argv[1])
PY = sys.argv[2]
BASETEMP = sys.argv[3]
OUT = Path(sys.argv[4])
NODES = sys.argv[5:]
SF = CLONE / "Sourcefold"
assert "scratchpad" in str(CLONE), "refusing to run outside the scratch clone"
MARK = "# EXPERIMENT (scratch only): sealed CRLF working-byte identity"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(CLONE), *args], capture_output=True, text=True, check=True).stdout


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


def crlf(b: bytes) -> bytes:
    return b.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")


def current_list() -> list[str]:
    text = (SF / ".gitattributes").read_text(encoding="utf-8")
    if MARK not in text:
        return []
    tail = text.split(MARK, 1)[1]
    return ["Sourcefold/" + line.split(" text eol=crlf")[0] for line in tail.splitlines() if line.endswith("text eol=crlf")]


def apply(paths: list[str]) -> None:
    git("checkout", "--", "Sourcefold/.gitattributes")
    lines = ["", MARK] + [p.removeprefix("Sourcefold/") + " text eol=crlf" for p in sorted(paths)]
    with (SF / ".gitattributes").open("a", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    git("rm", "-q", "--cached", "--", *paths)
    git("checkout", "HEAD", "--", *paths)


def module(test_file: str):
    spec = importlib.util.spec_from_file_location("m_" + Path(test_file).stem, SF / test_file)
    mod = importlib.util.module_from_spec(spec)
    sys.path[:0] = [str(CLONE), str(SF), str(SF / "scripts")]
    spec.loader.exec_module(mod)
    return mod


# Start from the committed baseline: drop any earlier experiment and restore LF bytes.
previous = current_list()
git("checkout", "--", "Sourcefold/.gitattributes")
if previous:
    git("rm", "-q", "--cached", "--", *previous)
    git("checkout", "HEAD", "--", *previous)
assert not git("status", "--short").strip(), "clone not clean after reset"

known: set[str] = set()
records = []
for round_no in range(1, 30):
    run = subprocess.run(
        [PY, "-B", "-m", "pytest", "-p", "no:cacheprovider", "-q", "--tb=long", "--basetemp", BASETEMP, *NODES],
        cwd=SF, capture_output=True, text=True, encoding="utf-8", errors="replace",
        env={**os.environ, "PYTHONPATH": str(CLONE), "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"},
    )
    found = []
    unexplained = []
    # Each failure block: "_____ test_name _____" ... "> assert <left> == sha256_file(CONST)" ... "tests\\x.py:NN: AssertionError"
    blocks = re.split(r"\n_{2,} (\S+) _{2,}\n", run.stdout)
    for i in range(1, len(blocks), 2):
        name, body = blocks[i], blocks[i + 1]
        m = re.search(r">\s+assert (.+?) == sha256_file\((\w+)\)", body)
        loc = re.search(r"\n(tests[\\/][^:]+\.py):\d+: ", body)
        if not (m and loc):
            unexplained.append(name)
            continue
        test_file = loc.group(1).replace("\\", "/")
        const = m.group(2)
        left = re.search(r"AssertionError: assert '([0-9A-F]{64})' ==", body) or re.search(r"\+ ([0-9A-F]{64})", body)
        path = Path(getattr(module(test_file), const))
        rel = "Sourcefold/" + path.relative_to(SF).as_posix()
        data = path.read_bytes()
        recorded = None
        for cand in re.findall(r"[0-9A-F]{64}", body):
            if cand == sha(crlf(data)):
                recorded = cand
        records.append({"round": round_no, "test": f"{test_file}::{name}", "constant": const, "predecessor": rel,
                        "lf_sha256": sha(data.replace(b'\r\n', b'\n')), "crlf_sha256": sha(crlf(data)),
                        "sealed_equals_crlf": recorded is not None})
        if recorded and rel not in known:
            found.append(rel)
        elif not recorded:
            unexplained.append(f"{name}:{const}")
    summary = run.stdout.strip().splitlines()[-1] if run.stdout.strip() else run.stderr[-300:]
    print(f"round {round_no}: {summary}; new={len(found)} unexplained={unexplained}")
    if not found:
        break
    known.update(found)
    apply(sorted(known))

OUT.write_text(json.dumps({"crlf_identity_paths": sorted(known), "observations": records}, indent=2), encoding="utf-8")
print("total crlf identity paths:", len(known))
