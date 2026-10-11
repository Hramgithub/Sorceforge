import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_fixture_admission_decision_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_decision_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_fixture_admission_decision_prep.json"
REPORT = OUT_ROOT / "gate_1_fixture_admission_decision_prep_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_decision_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-DECISION-PREP-001"
HUMAN_DECISION = (
    "proceed with fixture_admission_decision_prep; no fixture admission, "
    "no whole Gate 1 acceptance, no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_admission_decision_prep_is_fail_closed():
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
            "proceed with fixture_admission_decision_prep",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_fixture_admission_decision_prep_scope():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1FADP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_fixture_manifest_record"] == "G1FMR-G1-VIRAL-001"
    assert packet["human_decision"] == HUMAN_DECISION
    assert packet["status"] == "fixture_admission_decision_prep_ready_for_review"
    assert packet["creates_fixture_admission_decision"] is False
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["decision_question_count"] == 5
    assert {row["question_id"] for row in packet["decision_questions"]} == {
        "positive_fixture_group_admission_scope",
        "negative_fixture_group_admission_scope",
        "admission_invalidation_and_lineage_blockers",
        "admission_decision_boundary",
        "whole_gate_1_dependency",
    }


def test_fixture_admission_decision_prep_boundaries():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    for payload in (packet, report):
        assert payload["admits_fixture"] is False
        assert payload["creates_fixture_manifest"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    assert packet["remaining_blockers"] == [
        "fixture_admission_decision_review",
        "fixture_admission_decision_acceptance_record",
        "whole_gate_1_acceptance_readiness_recheck",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert packet["next_possible_packets"][0] == "fixture_admission_decision_acceptance_record"
    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Fixture admission decision created: `false`." in summary
    assert "Fixture admission: `false`." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing: `false`." in summary
