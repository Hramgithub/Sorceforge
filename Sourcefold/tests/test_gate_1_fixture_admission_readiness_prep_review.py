import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_fixture_admission_readiness_prep_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_review_G1_VIRAL_001"
REVIEW = OUT_ROOT / "gate_1_fixture_admission_readiness_prep_review.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_readiness_prep_review_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-READINESS-PREP-REVIEW-001"
DECISION = (
    "G1FARP accepted as readiness/blocker packet only; proceed to prepare fixture admission "
    "blocker resolution prep; no fixture admission, no whole Gate 1 acceptance, no page 021+, no push"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_g1farp_review_is_fail_closed():
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
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTHORIZATION_ID, "--decision", "admit fixture"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert DECISION in wrong_decision.stderr


def test_g1farp_review_accepts_readiness_only():
    review = read_json(REVIEW)

    assert review["review_id"] == "G1FARPREV-G1-VIRAL-001"
    assert review["authorization_id"] == AUTHORIZATION_ID
    assert review["reviewed_packet_id"] == "G1FARP-G1-VIRAL-001"
    assert review["human_decision"] == DECISION
    assert review["human_decision_source"]["message_id"] == "2255"
    assert review["accepts_readiness_blocker_packet"] is True
    assert review["authorizes_next_packet_prep"] is True
    assert review["admits_fixture"] is False
    assert review["accepts_whole_gate_1"] is False
    assert review["processes_page_021_plus"] is False


def test_g1farp_review_preserves_readiness_statuses_and_boundaries():
    review = read_json(REVIEW)
    assert review["readiness_statuses"]["fixture_admission_readiness"] == "not_ready_requires_future_decision"
    assert review["readiness_statuses"]["unsupported_negative_fixture_policy"] == "blocked_needs_future_decision"
    assert review["readiness_statuses"]["whole_gate_1_acceptance_readiness"] == "not_ready_requires_future_decision"
    for key, value in review["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No fixture admission." in summary
    assert "No whole Gate 1 acceptance." in summary
    assert "No page 021+ processing." in summary
