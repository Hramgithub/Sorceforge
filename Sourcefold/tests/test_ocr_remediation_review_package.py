import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MATRIX_ROOT = TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001"
REVIEW_ROOT = TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def test_review_package_preserves_evidence_only_boundary():
    review = read_json(REVIEW_ROOT / "ocr_remediation_review_report.json")
    admission = read_json(REVIEW_ROOT / "ocr_admission_candidate.json")
    rollup = read_json(REVIEW_ROOT / "evidence_rollup.json")
    negative = read_json(REVIEW_ROOT / "negative_check_report.json")

    for artifact in (review, admission, rollup, negative):
        assert artifact["status"] == "remediation_evidence_only"

    assert review["aggregate"]["source_acceptance"] is False
    assert review["aggregate"]["gate_1_advancement"] is False
    assert review["aggregate"]["approved_by_score"] is False
    assert admission["approved_by_score"] is False
    assert rollup["gate_boundary"]["source_acceptance"] is False
    assert rollup["gate_boundary"]["gate_1_advancement"] is False
    assert rollup["gate_boundary"]["ready_for_human_source_review"] is False


def test_review_package_binds_exact_predecessors_and_hashes():
    review = read_json(REVIEW_ROOT / "ocr_remediation_review_report.json")
    predecessor = review["predecessor"]

    assert predecessor["run_id"] == "ORM-G1-VIRAL-001"
    assert predecessor["authorization_id"] == "BA-G1-VIRAL-REMEDIATE-001"
    assert predecessor["authorization_status"] == "expired"
    assert predecessor["authorization_scope_consumed_by"] == "ORM-G1-VIRAL-001"
    assert predecessor["commit"] == "f90d170b"

    bound = {
        "matrix_report_path": "matrix_report_sha256",
        "matrix_rows_path": "matrix_rows_sha256",
        "output_manifest_path": "output_manifest_sha256",
        "remediation_plan_path": "remediation_plan_sha256",
    }
    for path_key, hash_key in bound.items():
        path = ROOT / predecessor[path_key]
        assert path.exists()
        assert sha256_file(path) == predecessor[hash_key]


def test_review_metrics_match_existing_orm_without_new_outputs():
    matrix = read_json(MATRIX_ROOT / "ocr_remediation_matrix_report.json")
    rows = read_json(MATRIX_ROOT / "ocr_remediation_matrix_rows.json")
    review = read_json(REVIEW_ROOT / "ocr_remediation_review_report.json")

    assert review["aggregate"] == matrix["aggregate"]
    assert review["aggregate"]["samples"] == 5
    assert review["aggregate"]["remediation_route_pass"] == 5
    assert review["aggregate"]["ocr_normalized_exact_zones"] == 5
    assert review["aggregate"]["visual_qc_route_zones"] == 2
    assert len(rows) == 80
    assert {row["psm"] for row in rows} == {1, 4, 8, 11}
    assert {3, 6}.isdisjoint({row["psm"] for row in rows})
    assert len(review["selected_ocr_zones"]) == 5
    assert len(review["visual_qc_zones"]) == 2


def test_negative_checks_and_payload_boundaries_are_explicit():
    negative = read_json(REVIEW_ROOT / "negative_check_report.json")
    assert negative["check_state"] == "passed"
    assert all(check["passed"] for check in negative["checks"])

    combined = "\n".join(
        path.read_text(encoding="utf-8-sig")
        for path in REVIEW_ROOT.glob("*")
        if path.suffix in {".json", ".md"}
    )
    forbidden_runtime_references = [
        "source_acceptance\": true",
        "gate_1_advancement\": true",
        "approved_by_score\": true",
    ]
    for token in forbidden_runtime_references:
        assert token not in combined


def test_no_review_step_regenerates_orm_raw_evidence():
    review_files = {path.name for path in REVIEW_ROOT.iterdir() if path.is_file()}
    assert review_files == {
        "ocr_remediation_review_report.json",
        "ocr_admission_candidate.json",
        "evidence_rollup.json",
        "negative_check_report.json",
        "ocr_remediation_review_report.md",
        "orchestration_record.md",
    }
    assert not (REVIEW_ROOT / "raw_outputs").exists()
    assert not (REVIEW_ROOT / "input_crops").exists()
    assert not (REVIEW_ROOT / "prepared_inputs").exists()
