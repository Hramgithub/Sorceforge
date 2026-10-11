import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_011_text_extraction.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_011_text_extraction_G1_VIRAL_001"
PACKET = OUT_ROOT / "page_011_text_extraction_packet.json"
REPORT = OUT_ROOT / "page_011_text_extraction_report.json"
SUMMARY = OUT_ROOT / "page_011_text_extraction_summary.md"
TEXT_MAP = OUT_ROOT / "page_011_text_map.md"
AUTH = "BA-G1-VIRAL-PAGE-011-TEXT-EXTRACTION-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_011_text_extraction_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-011-TRIAGE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_011_text_extraction_records_triage_decision_without_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["package_id"] == "P011TXT-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTH
    assert packet["human_review_decision"]["decision"] == "p011_triage_ok"
    assert packet["human_review_decision"]["accepted_package_id"] == "P011TR-G1-VIRAL-001"
    assert packet["ocr_execution_created"] is False
    assert packet["ocr_output_created"] is False
    assert packet["ocr_acceptance_created"] is False
    assert packet["source_acceptance_created"] is False
    assert packet["semantic_map_created"] is False
    assert packet["pcrp_created"] is False
    assert packet["page_complete_acceptance_created"] is False
    assert packet["whole_gate_1_acceptance_created"] is False
    assert packet["pages_012_020_processing_created"] is False
    assert report["text_unit_count"] == 2
    assert report["excluded_visual_only_blocks"] == ["P011-B002", "P011-B003"]
    assert report["crop_order_validation_status"] == "passed"
    assert report["text_extraction_contract_status"] == "passed"
    assert packet["text_extraction_contract_validation"]["status"] == "passed"
    assert packet["text_extraction_contract_validation"]["schema_version"] == "sourcefold_text_extraction_contract.v1"


def test_page_011_text_map_contains_only_two_text_evidence_crops_and_continuations():
    packet = read_json(PACKET)
    text_map = TEXT_MAP.read_text(encoding="utf-8-sig")

    assert packet["logical_reading_order"] == ["P011-B001-TES", "P011-B004-TES"]
    assert packet["crop_order_validation"]["status"] == "passed"
    assert packet["crop_order_validation"]["schema_version"] == "sourcefold_crop_order_validation.v1"
    assert packet["crop_order_validation"]["findings"] == []
    assert packet["crop_order_validation"]["logical_order_is_not_asset_order"] is False
    assert packet["crop_order_validation"]["physical_crop_asset_order"] == ["P011-B001-TES", "P011-B004-TES"]
    assert packet["crop_order_validation"]["required_before"] == ["semantic_map", "pcrp"]
    assert packet["text_map"]["excluded_visual_only_blocks"] == ["P011-B002", "P011-B003"]
    assert "P011-B001-TES -> P011-B004-TES" in text_map
    assert "P011-B002` Emily portrait and `P011-B003` lower-left screen image are visual-only anchors" in text_map
    assert "Maya's Secrets" in text_map
    assert "Marco often refers to Maya as \"the eyes in the sky\"" in text_map
    assert "APPEARANCE" in text_map
    assert "Emily 'Em' Lavigne (NPC)" in text_map
    assert "Super Fan Option" in text_map
    assert "paid a group of local teens to ferry" in text_map
    assert "```text" in text_map


def test_page_011_text_summary_exposes_review_boundary():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "draft_text_ready_for_bogdan_review_no_ocr_acceptance" in summary
    assert "Logical reading order: `B001 -> B004`" in summary
    assert "Excludes visual-only `P011-B002` portrait and `P011-B003` screen image" in summary
    assert "Creates no OCR run/output acceptance" in summary
    assert "p011 text ok" in summary
