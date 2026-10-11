import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_fixture_admission_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_decision_acceptance_G1_VIRAL_001"
ACCEPTANCE = OUT_ROOT / "gate_1_fixture_admission_decision_acceptance.json"
REPORT = OUT_ROOT / "gate_1_fixture_admission_decision_acceptance_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_decision_acceptance_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-ACCEPTANCE-001"
HUMAN_DECISION = (
    "g1fadp packet ok; proceed to prepare fixture admission decision acceptance record; "
    "no whole Gate 1 acceptance, no page 021+, no push"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_admission_decision_acceptance_is_fail_closed():
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
            "g1fadp packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_fixture_admission_decision_acceptance_scope():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    assert acceptance["acceptance_id"] == "G1FADAR-G1-VIRAL-001"
    assert acceptance["authorization_id"] == AUTHORIZATION_ID
    assert acceptance["source_decision_prep_packet"] == "G1FADP-G1-VIRAL-001"
    assert acceptance["human_decision"] == HUMAN_DECISION
    assert acceptance["creates_fixture_admission_decision"] is True
    assert acceptance["admits_fixture"] is True
    assert acceptance["resolves_fixture_admission_decision_blocker"] is True
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["accepted_fixture_admission_decision_count"] == 5
    assert all(row["status"] == "admitted_by_fixture_admission_decision" for row in acceptance["admitted_positive_fixture_groups"])
    assert all(row["status"] == "admitted_by_fixture_admission_decision" for row in acceptance["admitted_negative_fixture_groups"])
    decisions = {row["question_id"]: row["decision"] for row in acceptance["accepted_fixture_admission_decisions"]}
    assert decisions["positive_fixture_group_admission_scope"] == "positive_seed_group_pages_001_020_admitted"
    assert decisions["admission_decision_boundary"] == "fixture_admission_acceptance_record_created"


def test_fixture_admission_decision_acceptance_boundaries():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    for payload in (acceptance, report):
        assert payload["creates_fixture_manifest"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    assert acceptance["remaining_blockers"] == [
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert acceptance["next_possible_packets"][0] == "whole_gate_1_acceptance_readiness_recheck"
    for key, value in acceptance["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Fixture admission decision accepted: `true`." in summary
    assert "Fixture admission: `true`." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing: `false`." in summary
