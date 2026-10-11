import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_fixture_admission_blocker_resolution_prep_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_G1_VIRAL_001"
REVIEW = OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-BLOCKER-RESOLUTION-PREP-REVIEW-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_g1fabrp_review_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-WRONG", "--decision", "ok"],
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
    assert "ok" in wrong_decision.stderr


def test_g1fabrp_review_accepts_prep_only():
    review = read_json(REVIEW)

    assert review["review_id"] == "G1FABRPREV-G1-VIRAL-001"
    assert review["authorization_id"] == AUTHORIZATION_ID
    assert review["reviewed_packet_id"] == "G1FABRP-G1-VIRAL-001"
    assert review["human_decision"] == "ok"
    assert review["human_decision_source"]["message_id"] == "2275"
    assert review["accepts_blocker_resolution_prep_packet"] is True
    assert review["creates_blocker_resolution"] is False
    assert review["admits_fixture"] is False
    assert review["accepts_whole_gate_1"] is False
    assert review["processes_page_021_plus"] is False


def test_g1fabrp_review_preserves_blockers_and_boundaries():
    review = read_json(REVIEW)

    assert review["reviewed_blockers"] == [
        "unsupported_negative_fixture_policy",
        "fixture_strategy_fit_check",
        "whole_gate_1_dependency",
        "page_021_plus_boundary",
    ]
    assert review["next_candidate"] == "unsupported_negative_fixture_policy_decision_prep"
    for key, value in review["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No blocker resolution." in summary
    assert "No fixture admission." in summary
    assert "No whole Gate 1 acceptance." in summary
