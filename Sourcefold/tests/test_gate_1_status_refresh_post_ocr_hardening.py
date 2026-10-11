import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_status_refresh_post_ocr_hardening.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017"
PACKET = OUT_ROOT / "gate_1_status_packet.json"
REPORT = OUT_ROOT / "gate_1_status_report.json"
SUMMARY = OUT_ROOT / "gate_1_status_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-POST-OCR-HARDENING-STATUS-READINESS-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_post_ocr_hardening_status_refresh_is_fail_closed():
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


def test_post_ocr_hardening_status_refresh_records_ready_evidence_and_blockers():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["status_packet_id"] == "G1SP-G1-VIRAL-017"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["status"] == "gate_1_status_post_ocr_hardening_ready_for_route_decision"
    assert packet["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert packet["page_021_plus_state"] == "unprocessed_not_authorized"
    assert packet["whole_gate_1_acceptance"] is False
    assert packet["consumed_route_review"] == "G1SPRMREV-G1-VIRAL-001"
    assert packet["consumed_ocr_hardening"] == "OCRHM-G1-VIRAL-001"

    assert packet["creates_acceptance"] is False
    assert packet["creates_parking_decision"] is False
    assert packet["executes_ocr"] is False
    assert report["creates_acceptance"] is False
    assert report["creates_parking_decision"] is False
    assert report["executes_ocr"] is False


def test_post_ocr_hardening_status_refresh_flags_are_precise():
    flags = read_json(PACKET)["readiness_flags"]

    assert flags["pages_001_020_page_complete_accepted_only"] is True
    assert flags["source_profile_readiness_matrix_review_accepted"] is True
    assert flags["ocr_benchmark_methodology_hardened_for_gate_review"] is True
    assert flags["ocr_benchmark_remediation_unresolved"] is False
    assert flags["source_profile_accepted"] is False
    assert flags["parking_decisions_recorded"] is False
    assert flags["unsupported_profiles_negative_fixtures_decided"] is False
    assert flags["page_021_plus_authorized"] is False
    assert flags["whole_gate_1_accepted"] is False


def test_post_ocr_hardening_status_refresh_keeps_broad_guardrails_false():
    packet = read_json(PACKET)

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    assert "source_profile_acceptance_or_parking_decisions_not_recorded" in packet["remaining_blockers"]
    assert "unsupported_profiles_and_negative_fixtures_need_decision" in packet["remaining_blockers"]
    assert "whole_gate_1_acceptance_not_recorded" in packet["remaining_blockers"]
    assert packet["recommended_next_candidates"][0]["candidate"] == "gate_1_source_profile_review_or_parking_decision"
    assert packet["recommended_next_candidates"][0]["requires_new_bounded_authorization"] is True


def test_post_ocr_hardening_status_refresh_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Gate 1 Status Packet - G1SP-G1-VIRAL-017" in summary
    assert "Pages `001-020`: page-complete accepted only." in summary
    assert "OCRHM-G1-VIRAL-001" in summary
    assert "No whole Gate 1 acceptance." in summary
