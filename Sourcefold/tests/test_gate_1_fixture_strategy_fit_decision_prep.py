import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_fixture_strategy_fit_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_strategy_fit_decision_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_fixture_strategy_fit_decision_prep.json"
REPORT = OUT_ROOT / "gate_1_fixture_strategy_fit_decision_prep_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_strategy_fit_decision_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-DECISION-PREP-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_strategy_fit_decision_prep_is_fail_closed():
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


def test_fixture_strategy_fit_decision_prep_consumes_policy_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1FSFDP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_policy_acceptance"] == "G1UNFPAR-G1-VIRAL-001"
    assert packet["fixture_strategy_reference"] == (
        "docs/plans/20260715-sourcefold-phase-0-release-charter/fixture_strategy.md"
    )
    assert report["decision_question_count"] == 5


def test_fixture_strategy_fit_decision_prep_questions_and_sequence():
    packet = read_json(PACKET)
    question_ids = [row["question_id"] for row in packet["decision_questions"]]
    assert question_ids == [
        "strategy_scope_fit",
        "positive_fixture_seed_fit",
        "negative_fixture_coverage_fit",
        "invalidation_dependency_fit",
        "admission_dependency",
    ]
    assert packet["remaining_blockers"] == [
        "fixture_strategy_fit_decision",
        "fixture_admission_readiness_refresh",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert packet["next_possible_packets"][0] == "fixture_strategy_fit_acceptance_record"


def test_fixture_strategy_fit_decision_prep_boundaries():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    for payload in (packet, report):
        assert payload["creates_fixture_strategy_fit_decision"] is False
        assert payload["admits_fixture"] is False
        assert payload["creates_fixture_manifest"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No fixture strategy fit decision is created." in summary
    assert "No fixture admission." in summary
    assert "No whole Gate 1 acceptance." in summary
    assert "No page 021+ processing." in summary
