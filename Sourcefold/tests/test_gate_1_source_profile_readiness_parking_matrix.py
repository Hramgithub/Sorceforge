import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_source_profile_readiness_parking_matrix.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_readiness_parking_matrix_G1_VIRAL_001"
MATRIX = OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix.json"
REPORT = OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_report.json"
SUMMARY = OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_summary.md"
AUTH = "BA-G1-VIRAL-SOURCE-PROFILE-READINESS-PARKING-MATRIX-001"

ALLOWED_DISPOSITIONS = {
    "ready_for_gate_review",
    "parked_for_0.1",
    "parked_pending_ocr_hardening",
    "blocked_needs_decision",
    "evidence_only_not_accepting",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_source_profile_readiness_matrix_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-POST-P020-STATUS-READINESS-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_source_profile_readiness_matrix_records_scope_without_acceptance():
    matrix = read_json(MATRIX)
    report = read_json(REPORT)

    assert matrix["matrix_id"] == "G1SPRM-G1-VIRAL-001"
    assert matrix["authorization_id"] == AUTH
    assert matrix["creates_acceptance"] is False
    assert matrix["creates_parking_decision"] is False
    assert matrix["starts_ocr_remediation"] is False
    assert matrix["baseline"]["status_packet"] == "G1SP-G1-VIRAL-016"
    assert matrix["baseline"]["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert matrix["baseline"]["page_021_plus_state"] == "unprocessed_not_authorized"
    assert matrix["baseline"]["whole_gate_1_acceptance"] is False
    assert report["creates_acceptance"] is False
    assert report["creates_parking_decision"] is False
    assert report["starts_ocr_remediation"] is False


def test_source_profile_readiness_matrix_rows_have_single_allowed_disposition():
    matrix = read_json(MATRIX)
    row_ids = {row["id"] for row in matrix["rows"]}

    assert len(matrix["rows"]) == 12
    assert "ocr_benchmark_remediation_debt" in row_ids
    assert "page_021_plus_disposition" in row_ids
    assert "whole_gate_1_acceptance" in row_ids
    for row in matrix["rows"]:
        assert row["disposition"] in ALLOWED_DISPOSITIONS
        assert row["requires_human_decision_before_acceptance"] is True


def test_source_profile_readiness_matrix_preserves_negative_capabilities():
    matrix = read_json(MATRIX)
    negative = matrix["negative_capability_matrix"]

    for key, value in negative.items():
        assert value is False, key
    assert negative["page_021_plus_processing"] is False
    assert negative["whole_gate_1_acceptance"] is False
    assert negative["ocr_execution"] is False
    assert negative["ocr_remediation_execution"] is False
    assert negative["source_profile_acceptance"] is False
    assert matrix["next_branch_after_this_matrix"]["status"] == "selected_next_branch_not_started_not_authorized_by_this_matrix"


def test_source_profile_readiness_matrix_verifies_key_inputs():
    matrix = read_json(MATRIX)
    inputs = matrix["verified_inputs"]

    assert inputs["G1SP-G1-VIRAL-016.packet"]["sha256"] == "C69701A098CC33486B89C6F0D7F8D1A890B05C288DC8F814A430D44ABF47F88F"
    assert inputs["G1SP-G1-VIRAL-016.report"]["sha256"] == "3C051D65A15CB4DE0FA5649D6FE6C5C81AC75B3A752EC80E126EA81E50713F05"
    assert inputs["G1SP-G1-VIRAL-015.packet"]["sha256"] == "B016D09B91A5C1DA9B3E6026C9E5CF777CE290773864C786A51903FA1FCD62F8"
    assert inputs["ORM-G1-VIRAL-001.report"]["sha256"] == "3A454433ABA46E237D091F5BB4DA6EB8B73FCEE400935AF10BB0DC5731F212F5"
    assert inputs["ONC-G1-VIRAL-001.report"]["sha256"] == "2205564DB2BCD9EEF73D8EB02034EA28D7292D1A6970E3056F3BD9F5887E8F61"


def test_source_profile_readiness_matrix_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Gate 1 Source Profile Readiness Parking Matrix - G1SPRM-G1-VIRAL-001" in summary
    assert "Pages `001` through `020`: page-complete accepted only." in summary
    assert "Page `021+`: `unprocessed_not_authorized`." in summary
    assert "starts no OCR remediation" in summary
    assert "`ocr_benchmark_remediation_methodology_hardening`" in summary
