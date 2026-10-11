import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_status_readiness_post_p020.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_016"
PACKET = OUT_ROOT / "gate_1_status_packet.json"
REPORT = OUT_ROOT / "gate_1_status_report.json"
SUMMARY = OUT_ROOT / "gate_1_status_summary.md"
AUTH = "BA-G1-VIRAL-POST-P020-STATUS-READINESS-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_post_p020_status_readiness_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-020-AGGRESSIVE-BATCH-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_post_p020_status_readiness_records_pages_001_020_without_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["status_packet_id"] == "G1SP-G1-VIRAL-016"
    assert packet["authorization_id"] == AUTH
    assert packet["creates_acceptance"] is False
    assert packet["baseline"]["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert packet["baseline"]["page_complete_acceptance_scope"] == "individual_pages_only"
    assert packet["baseline"]["p016_p020_final_review_state"] == "accepted"
    assert packet["baseline"]["page_021_plus_state"] == "unprocessed_not_authorized"
    assert packet["baseline"]["whole_gate_1_acceptance"] is False
    assert report["creates_acceptance"] is False
    assert report["page_021_plus_processing_authorized"] is False
    assert report["whole_gate_1_acceptance"] is False


def test_post_p020_status_readiness_binds_status_and_final_review_predecessors():
    packet = read_json(PACKET)
    bindings = packet["predecessor_bindings"]

    assert bindings["status_predecessor"]["package_id"] == "G1SP-G1-VIRAL-015"
    assert bindings["status_predecessor"]["packet_sha256"] == "B016D09B91A5C1DA9B3E6026C9E5CF777CE290773864C786A51903FA1FCD62F8"

    final_reviews = bindings["final_human_reviews"]
    assert list(final_reviews) == ["016", "017", "018", "019", "020"]
    assert final_reviews["016"]["package_id"] == "P016BATCHREV-G1-VIRAL-001"
    assert final_reviews["020"]["package_id"] == "P020BATCHREV-G1-VIRAL-001"
    assert final_reviews["016"]["report_sha256"] == "A99DFF6580DB07F3F66303B856EA5FB7A94E215864B4112F59C71B964682FD70"
    assert final_reviews["020"]["report_sha256"] == "B7E024DC1C30FED09539C048182E9369354D0081C9ECA5F4A47A210D957178FB"


def test_post_p020_status_readiness_blockers_and_routes():
    packet = read_json(PACKET)
    flags = packet["blocker_flags"]
    options = {item["option"]: item["status"] for item in packet["routing_matrix"]}

    assert flags["pages_001_020_complete"] is True
    assert flags["page_021_plus_unauthorized"] is True
    assert flags["whole_gate_1_acceptance"] is False
    assert flags["fixture_admission"] is False
    assert flags["source_profile_parameters_unaccepted_or_unparked"] is True
    assert flags["ocr_benchmark_remediation_unresolved"] is True
    assert flags["gate_1_status_only_no_acceptance"] is True
    assert packet["recommended_next_candidate"] == "gate_1_source_profile_readiness_or_parking_matrix"

    assert options["gate_1_source_profile_readiness_or_parking_matrix"] == "recommended_next_candidate_not_authorized_by_this_packet"
    assert options["page_021_or_p021_p025_aggressive"] == "separate_exact_authorization_required"
    assert options["whole_gate_1_acceptance"] == "not_ready"

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    assert packet["negative_capability_matrix"]["page_021_plus_processing_authorized"] is False


def test_post_p020_status_readiness_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Gate 1 Status Readiness Packet - G1SP-G1-VIRAL-016" in summary
    assert "Page-complete accepted only: `001`, `002`, `003`, `004`, `005`" in summary
    assert "- Page `021+`: `unprocessed_not_authorized`." in summary
    assert "`pages_001_020_complete=true`" in summary
    assert "`page_021_plus_unauthorized=true`" in summary
    assert "Recommended next candidate: `gate_1_source_profile_readiness_or_parking_matrix`." in summary
