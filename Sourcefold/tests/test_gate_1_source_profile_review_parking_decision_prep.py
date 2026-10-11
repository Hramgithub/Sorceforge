import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_source_profile_review_parking_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep.json"
REPORT = OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_report.json"
SUMMARY = OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_source_profile_review_parking_decision_prep_is_fail_closed():
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


def test_source_profile_review_parking_decision_prep_has_exact_lineage_and_no_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1SPRPD-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["purpose"] == "decision_prep_no_acceptance_no_parking"
    assert packet["consumed_status_refresh"] == "G1SP-G1-VIRAL-017"
    assert packet["consumed_matrix"] == "G1SPRM-G1-VIRAL-001"
    assert packet["consumed_matrix_review"] == "G1SPRMREV-G1-VIRAL-001"
    assert packet["consumed_ocr_hardening"] == "OCRHM-G1-VIRAL-001"

    for payload in (packet, report):
        assert payload["creates_acceptance"] is False
        assert payload["creates_parking_decision"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["admits_fixture"] is False
        assert payload["executes_ocr"] is False
        assert payload["processes_page_021_plus"] is False


def test_source_profile_review_parking_decision_prep_represents_all_matrix_rows_once():
    packet = read_json(PACKET)
    rows = packet["decision_prep_rows"]

    assert len(rows) == 12
    row_ids = [row["source_matrix_row_id"] for row in rows]
    assert len(row_ids) == len(set(row_ids))
    assert packet["decision_prep_counts"] == {
        "accept_for_gate_review_candidate": 5,
        "park_for_0_1_with_invalidation_conditions": 2,
        "remain_evidence_only_not_accepting": 2,
        "hold_blocked_needs_decision": 2,
        "requires_separate_bounded_authorization": 1,
        "not_accepted_not_parked": 0,
    }


def test_blocked_rows_do_not_become_accepted_or_parked():
    rows = {row["source_matrix_row_id"]: row for row in read_json(PACKET)["decision_prep_rows"]}

    assert rows["page_021_plus_disposition"]["decision_prep_category"] == "requires_separate_bounded_authorization"
    assert rows["unsupported_profiles_and_negative_fixtures"]["decision_prep_category"] == "hold_blocked_needs_decision"
    assert rows["whole_gate_1_acceptance"]["decision_prep_category"] == "hold_blocked_needs_decision"
    for row in rows.values():
        assert row["creates_acceptance"] is False
        assert row["creates_parking_decision"] is False
        assert row["requires_future_explicit_decision"] is True


def test_negative_capabilities_remain_false_and_summary_is_human_readable():
    packet = read_json(PACKET)

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    assert packet["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert packet["page_021_plus_state"] == "unprocessed_not_authorized"
    assert "fixture_admission" in packet["remaining_actual_decisions"]

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "decision prep only" in summary
    assert "`accept_for_gate_review_candidate`: 5" in summary
    assert "`park_for_0_1_with_invalidation_conditions`: 2" in summary
    assert "No whole Gate 1 acceptance." in summary
