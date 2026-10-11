import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_source_profile_review_parking_decision_prep_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_G1_VIRAL_001"
REVIEW = OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_review.json"
SUMMARY = OUT_ROOT / "gate_1_source_profile_review_parking_decision_prep_review_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-REVIEW-PARKING-DECISION-PREP-REVIEW-001"
DECISION = (
    "G1SPRPD accepted as decision-prep only; proceed to prepare Gate 1 source-profile decision packet; "
    "no source-profile acceptance or parking yet"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_g1sprpd_review_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-WRONG", "--decision", DECISION],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTHORIZATION_ID, "--decision", "accept source profile"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert DECISION in wrong_decision.stderr


def test_g1sprpd_review_accepts_prep_only_and_authorizes_next_packet_prep():
    review = read_json(REVIEW)

    assert review["review_id"] == "G1SPRPDREV-G1-VIRAL-001"
    assert review["authorization_id"] == AUTHORIZATION_ID
    assert review["reviewed_packet_id"] == "G1SPRPD-G1-VIRAL-001"
    assert review["human_decision"] == DECISION
    assert review["human_decision_source"]["message_id"] == "2227"
    assert review["accepts_decision_prep_packet"] is True
    assert review["authorizes_next_packet_prep"] is True
    assert review["accepts_source_profile"] is False
    assert review["creates_parking_decision"] is False
    assert review["accepts_whole_gate_1"] is False
    assert review["admits_fixture"] is False
    assert review["processes_page_021_plus"] is False


def test_g1sprpd_review_preserves_boundaries():
    review = read_json(REVIEW)

    assert review["decision_prep_counts"] == {
        "accept_for_gate_review_candidate": 5,
        "park_for_0_1_with_invalidation_conditions": 2,
        "remain_evidence_only_not_accepting": 2,
        "hold_blocked_needs_decision": 2,
        "requires_separate_bounded_authorization": 1,
        "not_accepted_not_parked": 0,
    }
    for key, value in review["negative_capability_matrix"].items():
        assert value is False, key


def test_g1sprpd_review_summary_is_clear():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "decision-prep only" in summary
    assert "No source-profile acceptance." in summary
    assert "No parking decision." in summary
    assert "No whole Gate 1 acceptance." in summary
