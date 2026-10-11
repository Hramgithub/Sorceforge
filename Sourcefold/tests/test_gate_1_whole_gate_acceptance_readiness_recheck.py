import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_whole_gate_acceptance_readiness_recheck.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck.json"
REPORT = OUT_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_report.json"
SUMMARY = OUT_ROOT / "gate_1_whole_gate_acceptance_readiness_recheck_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-WHOLE-GATE-1-ACCEPTANCE-READINESS-RECHECK-PREP-001"
HUMAN_DECISION = "Ок делай"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_whole_gate_acceptance_readiness_recheck_is_fail_closed():
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
            "proceed with whole Gate 1 acceptance readiness recheck prep",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_whole_gate_acceptance_readiness_recheck_consumes_g1fadar():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1WGARR-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert packet["human_decision"] == HUMAN_DECISION
    assert packet["creates_readiness_recheck_packet"] is True
    assert report["positive_fixture_group_count"] == 1
    assert report["negative_fixture_group_count"] == 4
    assert report["page_complete_accepted_page_count"] == 20
    assert report["review_question_count"] == 4


def test_whole_gate_acceptance_readiness_recheck_rows_and_questions():
    packet = read_json(PACKET)
    rows = {row["row_id"]: row for row in packet["readiness_rows"]}

    assert rows["pages_001_020_page_complete_scope"]["status"] == "ready_as_individual_page_complete_inputs_only"
    assert rows["fixture_admission_decision"]["status"] == "ready_from_g1fadar_admitted_fixture_manifest_groups"
    assert rows["page_021_plus_boundary"]["status"] == "blocked_separate_bounded_authorization_only"
    assert rows["whole_gate_1_acceptance_readiness"]["status"] == "ready_for_separate_human_gate_acceptance_decision"
    assert {row["question_id"] for row in packet["review_questions"]} == {
        "gate_1_scope_for_acceptance",
        "page_021_plus_boundary",
        "acceptance_record_boundary",
        "downstream_boundary",
    }


def test_whole_gate_acceptance_readiness_recheck_boundaries():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    for payload in (packet, report):
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["admits_new_or_broader_fixture"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False

    assert packet["remaining_blockers"] == [
        "whole_gate_1_acceptance_decision_review",
        "whole_gate_1_acceptance_record_if_bogdan_later_accepts",
        "page_021_plus_separate_bounded_authorization_if_selected",
    ]
    assert packet["next_possible_packets"][0] == "whole_gate_1_acceptance_decision_record"
    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "This packet does not accept whole Gate 1." in summary
    assert "Whole Gate 1 acceptance: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary
    assert "Translation/proofreading/implementation/push: `false`." in summary
