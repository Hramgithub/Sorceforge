"""Scratch-clone only: build the T1 candidate set from the attribution JSON plus explicit
reviewed decisions, apply `text eol=crlf` for that set in Sourcefold/.gitattributes,
re-materialize from HEAD, and verify bytes and blob ids.

Usage: python -I eol_apply_set.py <scratch_clone_root> <attr_json> <out_set_json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

CLONE = Path(sys.argv[1])
assert "scratchpad" in str(CLONE)
attr = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
OUT = Path(sys.argv[3])
MARK = "# EXPERIMENT (scratch only): sealed CRLF working-byte identity"

# Reviewed decisions for rows the automatic attribution cannot settle.
REVIEWED = {
    # LF reference is prose describing the mismatch (export R1 review), not a sealing record.
    "gate_1_review_decision_brief_report.json": ("crlf", "LF ref is R1-release-review.md:76 prose; sealing records use CRLF"),
    # OBR-002 manifest rows are keyed by sample id, not file name.
    **{f"GS-G1-VIRAL-00{i}.stderr.txt": ("crlf", f"sealed by ocr_benchmark_OBR-G1-VIRAL-002/ocr_output_manifest.md:{59 + i} (Stderr SHA-256, row keyed by sample id)") for i in range(1, 6)},
}


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(CLONE), *args], capture_output=True, text=True, check=True).stdout


selected, kept_lf, unresolved = [], [], []
for row in attr["rows"]:
    name = Path(row["path"]).name
    if row["class"] == "crlf_attributed":
        selected.append({"path": row["path"], "basis": "attributed", "sealing_refs": row["crlf_attributed_refs"]})
    elif row["class"] == "lf_attributed":
        kept_lf.append({"path": row["path"], "sealing_refs": row["lf_attributed_refs"]})
    elif name in REVIEWED and "OBR-G1-VIRAL-002" in row["path"] or name == "gate_1_review_decision_brief_report.json":
        decision, why = REVIEWED[name]
        selected.append({"path": row["path"], "basis": "reviewed: " + why,
                         "sealing_refs": row["crlf_attributed_refs"] or row["unattributed_refs"]})
    else:
        unresolved.append(row["path"])

paths = sorted(item["path"] for item in selected)
git("checkout", "--", ".gitattributes", "Sourcefold/.gitattributes")
blob_before = {p: git("ls-files", "-s", "--", p).split()[1] for p in paths}
with (CLONE / "Sourcefold" / ".gitattributes").open("a", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(["", MARK] + [p.removeprefix("Sourcefold/") + " text eol=crlf" for p in paths]) + "\n")
for i in range(0, len(paths), 50):
    git("rm", "-q", "--cached", "--", *paths[i:i + 50])
    git("checkout", "HEAD", "--", *paths[i:i + 50])
blob_after = {p: git("ls-files", "-s", "--", p).split()[1] for p in paths}
crlf_ok = 0
rows_by_path = {r["path"]: r for r in attr["rows"]}
for p in paths:
    if hashlib.sha256((CLONE / p).read_bytes()).hexdigest().upper() == rows_by_path[p]["crlf_sha256"]:
        crlf_ok += 1

OUT.write_text(json.dumps({"selected_crlf": selected, "kept_lf": kept_lf, "unresolved": unresolved}, indent=2), encoding="utf-8")
print("selected:", len(paths), "kept LF:", len(kept_lf), "unresolved:", unresolved)
print("working bytes == CRLF identity:", crlf_ok, "/", len(paths))
print("blob ids unchanged:", blob_before == blob_after)
print("status:", git("status", "--short").strip().splitlines())
