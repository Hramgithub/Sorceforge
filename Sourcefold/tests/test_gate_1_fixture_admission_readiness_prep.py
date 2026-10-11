import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_fixture_admission_readiness_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_fixture_admission_readiness_prep.json"
REPORT = OUT_ROOT / "gate_1_fixture_admission_readiness_prep_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_readiness_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-GATE-1-READINESS-PREP-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_admission_readiness_prep_is_fail_closed():
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


def test_fixture_admission_readiness_prep_consumes_decision_record():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1FARP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_decision_record"] == "G1SPDR-G1-VIRAL-001"
    assert packet["source_status_packet"] == "G1SP-G1-VIRAL-017"

    for payload in (packet, report):
        assert payload["admits_fixture"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False


def test_fixture_admission_readiness_prep_preserves_decision_counts():
    packet = read_json(PACKET)

    assert len(packet["accepted_gate_review_candidate_rows"]) == 5
    assert len(packet["parked_ocr_methodology_rows"]) == 2
    assert len(packet["evidence_only_rows"]) == 2
    assert len(packet["blocked_rows"]) == 2
    assert packet["page_021_plus_boundary"]["requires_separate_bounded_authorization"] is True
    assert packet["page_021_plus_boundary"]["included_in_this_packet"] is False
    for row in packet["parked_ocr_methodology_rows"]:
        assert row["parking_scope"] == "core_0_1_only"
        assert row["invalidation_conditions"]


def test_fixture_admission_readiness_prep_keeps_remaining_decisions_visible():
    packet = read_json(PACKET)
    assert "fixture_admission" in packet["remaining_actual_decisions"]
    assert "whole_gate_1_acceptance" in packet["remaining_actual_decisions"]
    assert "page_021_plus_disposition" in packet["remaining_actual_decisions"]

    readiness = {row["row_id"]: row for row in packet["readiness_rows"]}
    assert readiness["fixture_admission_readiness"]["status"] == "not_ready_requires_future_decision"
    assert readiness["whole_gate_1_acceptance_readiness"]["status"] == "not_ready_requires_future_decision"
    assert readiness["unsupported_negative_fixture_policy"]["status"] == "blocked_needs_future_decision"

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No fixture admission." in summary
    assert "No whole Gate 1 acceptance." in summary
    assert "No page 021+ processing or authorization." in summary


def test_fixture_admission_readiness_prep_negative_capabilities_are_false():
    packet = read_json(PACKET)
    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
