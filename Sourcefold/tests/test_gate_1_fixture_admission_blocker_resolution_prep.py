import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_fixture_admission_blocker_resolution_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_G1_VIRAL_001"
PACKET = OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep.json"
REPORT = OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_report.json"
SUMMARY = OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-BLOCKER-RESOLUTION-PREP-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_fixture_admission_blocker_resolution_prep_is_fail_closed():
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


def test_fixture_admission_blocker_resolution_prep_consumes_review():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["packet_id"] == "G1FABRP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_readiness_packet"] == "G1FARP-G1-VIRAL-001"
    assert packet["source_review"] == "G1FARPREV-G1-VIRAL-001"
    assert report["blocker_count"] == 4


def test_fixture_admission_blocker_resolution_prep_is_prep_only():
    packet = read_json(PACKET)
    report = read_json(REPORT)
    for payload in (packet, report):
        assert payload["admits_fixture"] is False
        assert payload["accepts_whole_gate_1"] is False
        assert payload["processes_page_021_plus"] is False
    assert packet["creates_blocker_resolution"] is False
    assert packet["creates_fixture_manifest"] is False
    assert packet["accepts_source_profile"] is False
    assert packet["executes_ocr"] is False
    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key


def test_fixture_admission_blocker_resolution_prep_lists_blockers_and_sequence():
    packet = read_json(PACKET)
    blocker_ids = {row["blocker_id"] for row in packet["blockers"]}
    assert blocker_ids == {
        "unsupported_negative_fixture_policy",
        "fixture_strategy_fit_check",
        "whole_gate_1_dependency",
        "page_021_plus_boundary",
    }
    assert packet["recommended_sequence"][0] == "unsupported_negative_fixture_policy_decision_prep"
    assert packet["inherited_context"]["page_021_plus_requires_separate_ba"] is True

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "No fixture admission." in summary
    assert "No whole Gate 1 acceptance." in summary
    assert "No page 021+ processing." in summary
