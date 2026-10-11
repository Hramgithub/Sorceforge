import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_fixture_strategy_fit_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_strategy_fit_acceptance_G1_VIRAL_001"
ACCEPTANCE = OUT_ROOT / "gate_1_fixture_strategy_fit_acceptance.json"
REPORT = OUT_ROOT / "gate_1_fixture_strategy_fit_acceptance_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_strategy_fit_acceptance_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-STRATEGY-FIT-ACCEPTANCE-001"
HUMAN_DECISION = (
    "g1fsfdp packet ok; proceed to prepare fixture strategy fit acceptance record over "
    "strategy_scope_fit, positive_fixture_seed_fit, negative_fixture_coverage_fit, "
    "invalidation_dependency_fit, and admission_dependency; no fixture admission, "
    "no fixture manifest, no whole Gate 1 acceptance, no page 021+, no push"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_strategy_fit_acceptance_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
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
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            AUTHORIZATION_ID,
            "--decision",
            "g1fsfdp packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_fixture_strategy_fit_acceptance_scope():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    assert acceptance["acceptance_id"] == "G1FSFAR-G1-VIRAL-001"
    assert acceptance["authorization_id"] == AUTHORIZATION_ID
    assert acceptance["source_decision_prep_packet"] == "G1FSFDP-G1-VIRAL-001"
    assert acceptance["source_policy_acceptance"] == "G1UNFPAR-G1-VIRAL-001"
    assert acceptance["human_decision"] == HUMAN_DECISION
    assert acceptance["creates_fixture_strategy_fit_decision"] is True
    assert acceptance["resolves_fixture_strategy_fit_blocker"] is True
    assert report["accepted_strategy_fit_decision_count"] == 5
    assert acceptance["accepted_strategy_fit_scope"] == [
        "strategy_scope_fit",
        "positive_fixture_seed_fit",
        "negative_fixture_coverage_fit",
        "invalidation_dependency_fit",
        "admission_dependency",
    ]
    assert {row["question_id"] for row in acceptance["accepted_strategy_fit_decisions"]} == set(
        acceptance["accepted_strategy_fit_scope"]
    )
    assert all(row["accepted_as_strategy_fit_decision"] is True for row in acceptance["accepted_strategy_fit_decisions"])


def test_fixture_strategy_fit_acceptance_boundaries():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    for payload in (acceptance, report):
        assert payload["admits_fixture"] is False
        assert payload["creates_fixture_manifest"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    assert acceptance["remaining_blockers"] == [
        "fixture_admission_readiness_refresh",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert acceptance["next_possible_packets"][0] == "fixture_admission_readiness_refresh"
    for key, value in acceptance["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Fixture strategy fit decision accepted: `true`." in summary
    assert "Fixture admission: `false`." in summary
    assert "Fixture manifest creation: `false`." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing: `false`." in summary
