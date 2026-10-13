"""Read-only: path-aware attribution of sealed hash references, and a working-tree
consistency check.

A reference (file:line holding a 64-hex token equal to the LF or CRLF identity of a tracked
path P) is *attributed* to P when P's basename occurs within +-WINDOW lines of that token in
the referencing file. Unattributed references are content collisions (identical bytes in
another file) and are reported separately.

Usage:
  python -I identity_attribute.py <repo_at_rev> <scan_json> <out_json> [<worktree_root>]
If <worktree_root> is given, also count attributed references whose hash differs from the
current working bytes of P under that root.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath

REPO, SCAN, OUT = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
WORK = Path(sys.argv[4]) if len(sys.argv) > 4 else None
WINDOW = 6
scan = json.loads(SCAN.read_text(encoding="utf-8"))
rev = scan["rev"]
cache: dict[str, list[str]] = {}


def lines_of(path: str) -> list[str]:
    if path not in cache:
        data = subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"], capture_output=True, check=True).stdout
        cache[path] = data.decode("utf-8", "replace").splitlines()
    return cache[path]


blob_paths: dict[str, list[str]] = {}
for item in subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "-z", rev], capture_output=True, check=True).stdout.split(b"\0"):
    if item:
        meta, path = item.split(b"\t", 1)
        blob_paths.setdefault(meta.split()[2].decode(), []).append(path.decode("utf-8"))


def attributed(ref: str, target: str, blob: str) -> bool:
    # Unique content: the hash identifies exactly one tracked path.
    if len(blob_paths.get(blob, [])) == 1:
        return True
    # Duplicated content: require the target basename near the token.
    file, line = ref.rsplit(":", 1)
    n = int(line)
    lines = lines_of(file)
    window = "\n".join(lines[max(0, n - 1 - WINDOW): n + WINDOW])
    return PurePosixPath(target).name in window


rows = []
summary = {"crlf_attributed": 0, "lf_attributed": 0, "both_attributed": 0, "collision_only": 0}
for row in scan["rows"]:
    p = row["path"]
    crlf_attr = [r for r in row["crlf_refs"] if attributed(r, p, row["blob"])]
    lf_attr = [r for r in row["lf_refs"] if attributed(r, p, row["blob"])]
    if crlf_attr and lf_attr:
        cls = "both_attributed"
    elif crlf_attr:
        cls = "crlf_attributed"
    elif lf_attr:
        cls = "lf_attributed"
    else:
        cls = "collision_only"
    summary[cls] += 1
    rows.append({**{k: row[k] for k in ("path", "blob", "lf_sha256", "crlf_sha256")}, "class": cls,
                 "crlf_attributed_refs": crlf_attr, "lf_attributed_refs": lf_attr,
                 "unattributed_refs": [r for r in row["crlf_refs"] + row["lf_refs"] if r not in crlf_attr + lf_attr]})

result = {"rev": rev, "window_lines": WINDOW, "summary": summary, "rows": rows}

if WORK is not None:
    mismatched = 0
    checked = 0
    for r in rows:
        work = hashlib.sha256((WORK / r["path"]).read_bytes()).hexdigest().upper()
        for ref in r["crlf_attributed_refs"]:
            checked += 1
            mismatched += work != r["crlf_sha256"]
        for ref in r["lf_attributed_refs"]:
            checked += 1
            mismatched += work != r["lf_sha256"]
    result["worktree_check"] = {"root": str(WORK), "attributed_refs_checked": checked, "mismatched": mismatched}
    print("worktree attributed refs checked:", checked, "mismatched:", mismatched)

OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(summary))
