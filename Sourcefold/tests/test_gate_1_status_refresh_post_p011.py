import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_status_refresh_post_p011.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_006"
PACKET = OUT_ROOT / "gate_1_status_packet.json"
REPORT = OUT_ROOT / "gate_1_status_report.json"
SUMMARY = OUT_ROOT / "gate_1_status_summary.md"
AUTH = "BA-G1-VIRAL-GATE-1-STATUS-REFRESH-006"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_post_p011_status_refresh_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-GATE-1-STATUS-REFRESH-005"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_post_p011_status_refresh_records_pages_001_011_without_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["status_packet_id"] == "G1SP-G1-VIRAL-006"
    assert packet["authorization_id"] == AUTH
    assert packet["creates_acceptance"] is False
    assert packet["baseline"]["page_complete_accepted_pages"] == [
        "001",
        "002",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
        "009",
        "010",
        "011",
    ]
    assert packet["baseline"]["g1sp_005_state"] == "stale_only_for_page_011_not_yet_accepted_after_P011PCA"
    assert report["creates_acceptance"] is False
    assert report["new_source_acceptance_rollup_created"] is False
    assert report["whole_gate_1_acceptance"] is False


def test_post_p011_status_refresh_blockers_and_routes():
    packet = read_json(PACKET)
    flags = packet["blocker_flags"]
    options = {item["option"]: item["status"] for item in packet["routing_matrix"]}

    assert flags["pages_001_011_complete"] is True
    assert flags["pages_012_020_unstarted"] is True
    assert flags["whole_gate_1_acceptance"] is False
    assert flags["source_profile_parameters_unaccepted_or_unparked"] is True
    assert flags["ocr_benchmark_remediation_unresolved"] is True
    assert packet["recommended_next_candidate"] == "page_012_triage_readiness"
    assert options["page_012_triage_readiness"] == "recommended_next_candidate_not_authorized_by_this_packet"
    assert options["whole_gate_1_acceptance"] == "not_ready"

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    assert packet["negative_capability_matrix"]["page_012_processing_authorized"] is False


def test_post_p011_status_refresh_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Gate 1 Status Route Packet - G1SP-G1-VIRAL-006" in summary
    assert "Page-complete accepted only: `001`, `002`, `003`, `004`, `005`, `006`, `007`, `008`, `009`, `010`, `011`." in summary
    assert "`pages_001_011_complete=true`" in summary
    assert "`pages_012_020_unstarted=true`" in summary
    assert "Recommended next candidate: `page_012_triage_readiness`." in summary
