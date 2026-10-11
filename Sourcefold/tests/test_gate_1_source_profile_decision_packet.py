import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_source_profile_decision_packet.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_decision_packet_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_source_profile_decision_packet.json"
REPORT = OUT_ROOT / "gate_1_source_profile_decision_packet_report.json"
SUMMARY = OUT_ROOT / "gate_1_source_profile_decision_packet_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-DECISION-PACKET-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_source_profile_decision_packet_is_fail_closed():
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


def test_source_profile_decision_packet_consumes_review_and_creates_no_decision():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1SPDP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["purpose"] == "decision_packet_prep_no_acceptance_no_parking"
    assert packet["controlling_review"] == "G1SPRPDREV-G1-VIRAL-001"
    assert packet["source_prep_packet"] == "G1SPRPD-G1-VIRAL-001"
    for payload in (packet, report):
        assert payload["creates_acceptance"] is False
        assert payload["accepts_source_profile"] is False
        assert payload["creates_parking_decision"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["admits_fixture"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["executes_ocr"] is False


def test_source_profile_decision_packet_represents_rows_and_options():
    packet = read_json(PACKET)

    assert len(packet["decision_rows"]) == 12
    assert len({row["source_matrix_row_id"] for row in packet["decision_rows"]}) == 12
    assert len(packet["decision_options"]) == 5
    for option in packet["decision_options"]:
        assert option["requires_future_explicit_decision"] is True
        assert option["creates_acceptance"] is False
        assert option["creates_parking_decision"] is False
        assert option["source_rows"]


def test_source_profile_decision_packet_guardrails_and_summary():
    packet = read_json(PACKET)
    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    assert "fixture_admission" in packet["remaining_actual_decisions"]
    assert "page_021_plus_disposition" in packet["remaining_actual_decisions"]

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No source-profile acceptance." in summary
    assert "No parking decision." in summary
    assert "No whole Gate 1 acceptance." in summary
