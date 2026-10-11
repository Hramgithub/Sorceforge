import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACCEPT_SCRIPT = ROOT / "scripts" / "accept_gate_1_unsupported_negative_fixture_policy_decision_prep_review.py"
BUILD_SCRIPT = ROOT / "scripts" / "build_gate_1_unsupported_negative_fixture_policy_record.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
REVIEW_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_unsupported_negative_fixture_policy_record_G1_VIRAL_001"
REVIEW = REVIEW_ROOT / "gate_1_unsupported_negative_fixture_policy_decision_prep_review.json"
RECORD = OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_record.json"
REPORT = OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_record_report.json"
SUMMARY = OUT_ROOT / "gate_1_unsupported_negative_fixture_policy_record_summary.md"
REVIEW_AUTHORIZATION_ID = "BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-DECISION-PREP-REVIEW-001"
RECORD_AUTHORIZATION_ID = "BA-G1-VIRAL-UNSUPPORTED-NEGATIVE-FIXTURE-POLICY-RECORD-001"
HUMAN_DECISION = (
    "g1unfpdp packet ok; proceed to prepare unsupported/negative fixture policy record over "
    "unsupported_profiles_scope, negative_fixture_obligations, invalidation_conditions, and "
    "fixture_admission_dependency; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_unsupported_negative_fixture_policy_review_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(ACCEPT_SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(ACCEPT_SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-WRONG",
            "--decision",
            HUMAN_DECISION,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert REVIEW_AUTHORIZATION_ID in wrong_auth.stderr


def test_unsupported_negative_fixture_policy_record_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(BUILD_SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT), "--execute", "--authorization-id", "BA-WRONG"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert RECORD_AUTHORIZATION_ID in wrong_auth.stderr


def test_unsupported_negative_fixture_policy_review_scope_and_boundaries():
    review = read_json(REVIEW)

    assert review["review_id"] == "G1UNFPDPREV-G1-VIRAL-001"
    assert review["authorization_id"] == REVIEW_AUTHORIZATION_ID
    assert review["reviewed_packet_id"] == "G1UNFPDP-G1-VIRAL-001"
    assert review["human_decision"] == HUMAN_DECISION
    assert review["policy_record_scope"] == [
        "unsupported_profiles_scope",
        "negative_fixture_obligations",
        "invalidation_conditions",
        "fixture_admission_dependency",
    ]
    assert review["accepts_decision_prep_packet"] is True
    assert review["authorizes_policy_record_prep"] is True
    assert review["creates_policy_decision"] is False
    assert review["admits_fixture"] is False
    assert review["accepts_whole_gate_1"] is False
    assert review["processes_page_021_plus"] is False


def test_unsupported_negative_fixture_policy_record_decisions_and_boundaries():
    record = read_json(RECORD)
    report = read_json(REPORT)

    assert record["record_id"] == "G1UNFPR-G1-VIRAL-001"
    assert record["authorization_id"] == RECORD_AUTHORIZATION_ID
    assert record["source_decision_prep_packet"] == "G1UNFPDP-G1-VIRAL-001"
    assert record["source_review"] == "G1UNFPDPREV-G1-VIRAL-001"
    assert record["creates_policy_decision"] is False
    assert record["resolves_unsupported_negative_fixture_policy_blocker"] is False
    assert report["candidate_policy_decision_count"] == 4

    question_ids = {row["question_id"] for row in record["candidate_policy_decisions"]}
    assert question_ids == {
        "unsupported_profiles_scope",
        "negative_fixture_obligations",
        "invalidation_conditions",
        "fixture_admission_dependency",
    }

    for payload in (record, report):
        assert payload["creates_blocker_resolution"] is False
        assert payload["admits_fixture"] is False
        assert payload["creates_fixture_manifest"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False


def test_unsupported_negative_fixture_policy_record_remaining_sequence_and_summary():
    record = read_json(RECORD)
    assert record["remaining_blockers"] == [
        "fixture_strategy_fit_decision",
        "fixture_admission_readiness_refresh",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert record["next_possible_packets"][0] == "unsupported_negative_fixture_policy_record_acceptance"
    for key, value in record["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No fixture admission." in summary
    assert "No fixture manifest creation." in summary
    assert "No whole Gate 1 acceptance." in summary
    assert "No page 021+ processing." in summary
