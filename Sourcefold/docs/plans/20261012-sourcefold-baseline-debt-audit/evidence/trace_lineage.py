"""Read-only lineage trace for the 12 failing hash assertions.

Usage: python -I trace_lineage.py <sourcefold_root> <nri_repo> <out_json>
"""
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

SF = Path(sys.argv[1])
NRI = Path(sys.argv[2])
OUT = Path(sys.argv[3])

# (test file, failing test, consumer report const, recorded field, predecessor const)
CASES = [
    ("test_gate_1_review_decision.py", "test_gate_1_review_decision_preserves_brief_lineage", "REPORT", "input_brief_report_sha256", "BRIEF_REPORT"),
    ("test_gate_1_review_decision_brief.py", "test_gate_1_review_decision_brief_preserves_packet_lineage_and_boundaries", "REPORT", "input_packet_report_sha256", "G1RP_REPORT"),
    ("test_gate_1_review_packet.py", "test_gate_1_review_packet_preserves_lineage_and_boundaries", "REPORT", "input_fixture_admission_report_sha256", "SRFA_REPORT"),
    ("test_gate_1_source_recon_evidence_rollup.py", "test_gate_1_source_recon_rollup_preserves_decision_lineage", "REPORT", "input_decision_report_sha256", "DECISION_REPORT"),
    ("test_gate_1_status_packet.py", "test_gate_1_status_packet_preserves_rollup_lineage", "REPORT", "input_rollup_report_sha256", "ROLLUP_REPORT"),
    ("test_source_reconstruction_fixture_admission.py", "test_fixture_admission_preserves_lineage_and_boundaries", "REPORT", "input_qa_report_sha256", "SRQA_REPORT"),
    ("test_source_reconstruction_human_package.py", "test_human_package_preserves_boundary_and_lineage", "REPORT", "input_report_sha256", "SRVO_REPORT"),
    ("test_source_reconstruction_human_review.py", "test_human_review_preserves_lineage_and_boundaries", "REPORT", "input_package_sha256", "SRHP_REPORT"),
    ("test_source_reconstruction_next_slice.py", "test_next_slice_preserves_status_packet_and_region_lineage", "REPORT", "input_status_packet_report_sha256", "STATUS_REPORT"),
    ("test_source_reconstruction_next_slice_004.py", "test_page_004_next_slice_consumes_p003a_and_region_lineage", "REPORT", "input_region_map_sha256", "PRM_REPORT"),
    ("test_source_reconstruction_qa.py", "test_source_reconstruction_qa_preserves_lineage_and_boundaries", "REPORT", "input_review_sha256", "SRHR_REPORT"),
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def variants(data: bytes) -> dict:
    lf = data.replace(b"\r\n", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    nobom = data[3:] if data.startswith(b"\xef\xbb\xbf") else data
    return {"raw": sha(data), "lf": sha(lf), "crlf": sha(crlf), "no_bom": sha(nobom)}


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(NRI), *args], capture_output=True, check=False).stdout


def history(rel: str, recorded: str) -> dict:
    """Search NRI history of rel for a blob whose bytes (raw/LF/CRLF) hash to recorded."""
    revs = git("log", "--format=%H %cs %s", "--", rel).decode("utf-8", "replace").splitlines()
    found = None
    versions = []
    for line in revs:
        rev, date, subject = line.split(" ", 2)
        blob = subprocess.run(["git", "-C", str(NRI), "show", f"{rev}:{rel}"], capture_output=True).stdout
        if not blob:
            versions.append({"rev": rev[:10], "date": date, "subject": subject, "present": False})
            continue
        v = variants(blob)
        hit = [k for k, h in v.items() if h == recorded]
        versions.append({"rev": rev[:10], "date": date, "subject": subject[:90], "blob_raw": v["raw"][:16], "matches_recorded_as": hit})
        if hit and found is None:
            found = {"rev": rev[:10], "date": date, "subject": subject[:120], "as": hit}
    return {"commit_count": len(revs), "newest_matching_version": found, "versions": versions}


def load(test_file: str):
    spec = importlib.util.spec_from_file_location("t_" + test_file[:-3], SF / "tests" / test_file)
    mod = importlib.util.module_from_spec(spec)
    sys.path[:0] = [str(SF.parent), str(SF), str(SF / "scripts")]
    spec.loader.exec_module(mod)
    return mod


results = []
for test_file, test_name, rep_const, field, pred_const in CASES:
    mod = load(test_file)
    consumer = Path(getattr(mod, rep_const))
    pred = Path(getattr(mod, pred_const))
    report = json.loads(consumer.read_text(encoding="utf-8-sig"))
    recorded = report[field]
    data = pred.read_bytes()
    v = variants(data)
    rel_pred = "Sourcefold/" + pred.relative_to(SF).as_posix()
    rel_cons = "Sourcefold/" + consumer.relative_to(SF).as_posix()
    results.append({
        "test": f"tests/{test_file}::{test_name}",
        "consumer": rel_cons,
        "field": field,
        "predecessor": rel_pred,
        "recorded": recorded,
        "actual": v["raw"],
        "line_ending_or_bom_match": [k for k, h in v.items() if h == recorded],
        "predecessor_history": history(rel_pred, recorded),
        "consumer_history_commits": len(git("log", "--format=%H", "--", rel_cons).splitlines()),
    })

# ocr_remediation_review_package: four bound predecessor files
mod_root = SF / "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001"
review_path = mod_root / "ocr_remediation_review_G1_VIRAL_001" / "ocr_remediation_review_report.json"
review = json.loads(review_path.read_text(encoding="utf-8-sig"))["predecessor"]
for path_key, hash_key in {
    "matrix_report_path": "matrix_report_sha256",
    "matrix_rows_path": "matrix_rows_sha256",
    "output_manifest_path": "output_manifest_sha256",
    "remediation_plan_path": "remediation_plan_sha256",
}.items():
    pred = SF / review[path_key]
    recorded = review[hash_key]
    v = variants(pred.read_bytes())
    rel_pred = "Sourcefold/" + pred.relative_to(SF).as_posix()
    results.append({
        "test": "tests/test_ocr_remediation_review_package.py::test_review_package_binds_exact_predecessors_and_hashes",
        "consumer": "Sourcefold/" + review_path.relative_to(SF).as_posix(),
        "field": f"predecessor.{hash_key}",
        "predecessor": rel_pred,
        "recorded": recorded,
        "actual": v["raw"],
        "ok": v["raw"] == recorded,
        "line_ending_or_bom_match": [k for k, h in v.items() if h == recorded],
        "predecessor_history": history(rel_pred, recorded) if v["raw"] != recorded else None,
        "predecessor_commit_recorded": review.get("commit"),
    })

OUT.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {len(results)} rows")
