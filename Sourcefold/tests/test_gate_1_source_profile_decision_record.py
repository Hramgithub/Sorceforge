import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_source_profile_decision_record.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_decision_record_G1_VIRAL_001"
RECORD = OUT_ROOT / "gate_1_source_profile_decision_record.json"
REPORT = OUT_ROOT / "gate_1_source_profile_decision_record_report.json"
SUMMARY = OUT_ROOT / "gate_1_source_profile_decision_record_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-DECISION-RECORD-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_source_profile_decision_record_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-WRONG"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_source_profile_decision_record_provenance_and_scope():
    record = read_json(RECORD)
    report = read_json(REPORT)

    assert record["record_id"] == "G1SPDR-G1-VIRAL-001"
    assert record["authorization_id"] == AUTHORIZATION_ID
    assert record["source_options_packet"] == "G1SPDP-G1-VIRAL-001"
    assert record["authority_provenance"]["bogdan_reply_raw"] == "ok"
    assert record["authority_provenance"]["bogdan_reply_display"] == "ок"
    assert record["authority_provenance"]["not_recorded_as_verbatim_long_phrase"] is True

    for payload in (record, report):
        assert payload["accepts_source_profile"] is False
        assert payload["creates_gate_review_candidate_status"] is True
        assert payload["creates_parking_decision"] is True
        assert payload["accepts_whole_gate_1"] is False
        assert payload["admits_fixture"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False


def test_source_profile_decision_record_counts_and_rows():
    record = read_json(RECORD)
    decisions = record["decisions"]

    assert len(decisions) == 12
    assert len({row["source_matrix_row_id"] for row in decisions}) == 12
    assert record["decision_counts"] == {
        "accepted_for_gate_review_candidate_status": 5,
        "parked_for_core_0_1_with_invalidation_conditions": 2,
        "kept_evidence_only_not_accepting": 2,
        "held_blocked_needs_future_decision": 2,
        "requires_separate_bounded_authorization": 1,
    }
    assert sum(1 for row in decisions if row["creates_parking_decision"]) == 2
    assert all(row["creates_source_profile_acceptance"] is False for row in decisions)


def test_source_profile_decision_record_guardrails_and_summary():
    record = read_json(RECORD)
    for key, value in record["negative_capability_matrix"].items():
        assert value is False, key

    assert "fixture_admission" in record["remaining_actual_decisions"]
    assert "page_021_plus_disposition" in record["remaining_actual_decisions"]
    assert "whole_gate_1_acceptance" in record["remaining_actual_decisions"]

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No whole source-profile acceptance." in summary
    assert "No fixture admission." in summary
    assert "No whole Gate 1 acceptance." in summary
    assert "No page 021+ processing or authorization." in summary
