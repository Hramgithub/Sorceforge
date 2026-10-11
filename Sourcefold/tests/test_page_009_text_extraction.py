import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_009_text_extraction.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_009_text_extraction_G1_VIRAL_001"
PACKET = OUT_ROOT / "page_009_text_extraction_packet.json"
REPORT = OUT_ROOT / "page_009_text_extraction_report.json"
SUMMARY = OUT_ROOT / "page_009_text_extraction_summary.md"
TEXT_MAP = OUT_ROOT / "page_009_text_map.md"
AUTH = "BA-G1-VIRAL-PAGE-009-TEXT-EXTRACTION-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_009_text_extraction_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-003"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_009_text_extraction_records_crop_contract_decision_without_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["package_id"] == "P009TXT-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTH
    assert packet["human_review_decision"]["decision"] == "p009_crop_contract_ok"
    assert packet["human_review_decision"]["accepted_package_id"] == "P009TR-G1-VIRAL-003"
    assert packet["ocr_execution_created"] is False
    assert packet["ocr_output_created"] is False
    assert packet["ocr_acceptance_created"] is False
    assert packet["source_acceptance_created"] is False
    assert packet["pcrp_created"] is False
    assert packet["page_complete_acceptance_created"] is False
    assert packet["whole_gate_1_acceptance_created"] is False
    assert report["text_unit_count"] == 7


def test_page_009_text_map_contains_left_and_right_profile_text():
    text_map = TEXT_MAP.read_text(encoding="utf-8-sig")

    assert "Enoch Jeremiah Eakins (Investigator)" in text_map
    assert "Peter Wharton (Investigator)" in text_map
    assert "aangeraakt door duivels" in text_map
    assert "The Sight (see Appendix)" in text_map
    assert "Spektral Krew(TM) Satchel" in text_map
    assert "secretly sets up fake evidence" in text_map
    assert "Wears a pair of Doc Martens" in text_map
    assert "```text" in text_map
    assert "P009-B003-TEXT-EVIDENCE" in text_map
    assert "P009-B004-TEXT-EVIDENCE" in text_map


def test_page_009_text_summary_exposes_review_boundary():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "draft_text_ready_for_bogdan_review_no_ocr_acceptance" in summary
    assert "Creates no OCR run/output acceptance" in summary
    assert "p009 text ok" in summary
