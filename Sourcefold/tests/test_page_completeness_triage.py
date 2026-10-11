import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_completeness_triage.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_completeness_triage_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_completeness_triage_report.json"
PACKET = OUT_ROOT / "page_completeness_triage_packet.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_triage_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-PAGE-COMPLETENESS-TRIAGE-001" in wrong_auth.stderr


def test_triage_keeps_all_acceptance_boundaries_false():
    report = read_json(REPORT)

    assert report["status"] == "page_completeness_triage_ready_for_bogdan_decision"
    assert report["page_complete_acceptance"] is False
    assert report["accepted_pages_as_complete"] is False
    assert report["whole_gate_1_acceptance"] is False
    assert report["fixture_admission"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["push_authorized"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False


def test_triage_covers_pages_002_003_and_holds_004_context_inset():
    report = read_json(REPORT)
    pages = {page["page"]: page for page in report["pages"]}

    assert set(pages) == {f"{page:03d}" for page in range(1, 21)}
    assert pages["001"]["classification"] == "incomplete"
    assert pages["002"]["recommendation"] == "ready_for_separate_page_complete_review"
    assert pages["003"]["recommendation"] == "ready_for_separate_page_complete_review"
    assert pages["004"]["recommendation"] == "hold_until_context_only_decision"
    assert pages["005"]["classification"] == "incomplete"
    assert pages["006"]["classification"] == "incomplete"
    assert pages["007"]["recommendation"] == "needs_next_bounded_source_slice"
    assert pages["020"]["recommendation"] == "needs_next_bounded_source_slice"
    assert pages["002"]["missing_source_regions"] == []
    assert pages["003"]["missing_source_regions"] == []
    assert pages["004"]["missing_source_regions"] == []
    assert len(pages["004"]["context_only_plain"]) == 1


def test_human_packet_excludes_internal_qa_details():
    packet = PACKET.read_text(encoding="utf-8-sig")

    forbidden = [
        "SHA",
        "sha",
        "pytest",
        "test key",
        "diff-check",
        "stale scan",
        "fixtures/candidate_inputs",
        "PRM-G1",
        "SRSA-G1",
        "P004A-G1",
    ]
    assert all(item not in packet for item in forbidden)
    assert "selected pages 1-20" in packet
    assert "Nothing in those decisions accepts the pages as complete by itself" in packet
