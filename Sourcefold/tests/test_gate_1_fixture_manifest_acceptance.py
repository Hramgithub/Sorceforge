import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_fixture_manifest_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_manifest_acceptance_G1_VIRAL_001"
ACCEPTANCE = OUT_ROOT / "gate_1_fixture_manifest_acceptance.json"
REPORT = OUT_ROOT / "gate_1_fixture_manifest_acceptance_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_manifest_acceptance_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-MANIFEST-ACCEPTANCE-001"
HUMAN_DECISION = (
    "g1fmp packet ok; proceed to prepare fixture manifest acceptance record; "
    "no fixture admission, no whole Gate 1 acceptance, no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_manifest_acceptance_is_fail_closed():
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
            "g1fmp packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_fixture_manifest_acceptance_scope():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    assert acceptance["acceptance_id"] == "G1FMR-G1-VIRAL-001"
    assert acceptance["authorization_id"] == AUTHORIZATION_ID
    assert acceptance["source_manifest_prep_packet"] == "G1FMP-G1-VIRAL-001"
    assert acceptance["source_readiness_refresh"] == "G1FARR-G1-VIRAL-001"
    assert acceptance["human_decision"] == HUMAN_DECISION
    assert acceptance["creates_fixture_manifest"] is True
    assert acceptance["fixture_manifest_status"] == "candidate_fixture_manifest_recorded_no_admission"
    assert acceptance["accepted_manifest_shape"]["manifest_status"] == "candidate_fixture_manifest_recorded_no_admission"
    assert "manifest_status_if_" + "later_accepted" not in acceptance["accepted_manifest_shape"]
    assert acceptance["resolves_fixture_manifest_review_blocker"] is True
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["accepted_review_question_count"] == 4
    assert {row["question_id"] for row in acceptance["accepted_review_questions"]} == {
        "positive_fixture_seed_manifest_shape",
        "negative_fixture_group_manifest_shape",
        "manifest_invalidation_shape",
        "manifest_admission_dependency",
    }
    assert all(row["accepted_as_fixture_manifest_shape"] is True for row in acceptance["accepted_review_questions"])
    stale_prompt = "later " + "manifest"
    assert all(stale_prompt not in row["source_prompt"] for row in acceptance["accepted_review_questions"])


def test_fixture_manifest_acceptance_boundaries():
    acceptance = read_json(ACCEPTANCE)
    report = read_json(REPORT)

    for payload in (acceptance, report):
        assert payload["admits_fixture"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    assert acceptance["remaining_blockers"] == [
        "fixture_admission_decision",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert acceptance["next_possible_packets"][0] == "fixture_admission_decision_prep"
    for key, value in acceptance["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Fixture manifest record created: `true`." in summary
    assert "Fixture admission: `false`." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing: `false`." in summary
