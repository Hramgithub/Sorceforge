import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_010_text_extraction.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_010_text_extraction_G1_VIRAL_001"
PACKET = OUT_ROOT / "page_010_text_extraction_packet.json"
REPORT = OUT_ROOT / "page_010_text_extraction_report.json"
SUMMARY = OUT_ROOT / "page_010_text_extraction_summary.md"
TEXT_MAP = OUT_ROOT / "page_010_text_map.md"
AUTH = "BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_010_text_extraction_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-010-TRIAGE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_010_text_extraction_records_triage_decision_without_acceptance():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["package_id"] == "P010TXT-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTH
    assert packet["human_review_decision"]["decision"] == "p010_triage_ok"
    assert packet["human_review_decision"]["accepted_package_id"] == "P010TR-G1-VIRAL-001"
    assert packet["ocr_execution_created"] is False
    assert packet["ocr_output_created"] is False
    assert packet["ocr_acceptance_created"] is False
    assert packet["source_acceptance_created"] is False
    assert packet["semantic_map_created"] is False
    assert packet["pcrp_created"] is False
    assert packet["page_complete_acceptance_created"] is False
    assert packet["whole_gate_1_acceptance_created"] is False
    assert report["text_unit_count"] == 4
    assert report["crop_order_validation_status"] == "passed"
    assert report["text_extraction_contract_status"] == "passed"
    assert packet["text_extraction_contract_validation"]["status"] == "passed"
    assert packet["text_extraction_contract_validation"]["schema_version"] == "sourcefold_text_extraction_contract.v1"


def test_page_010_text_map_contains_all_four_text_evidence_crops_and_continuations():
    packet = read_json(PACKET)
    text_map = TEXT_MAP.read_text(encoding="utf-8-sig")

    assert packet["logical_reading_order"] == ["P010-B001-TES", "P010-B005-TES", "P010-B002-TES", "P010-B006-TES"]
    assert packet["crop_order_validation"]["status"] == "passed"
    assert packet["crop_order_validation"]["schema_version"] == "sourcefold_crop_order_validation.v1"
    assert packet["crop_order_validation"]["findings"] == []
    assert packet["crop_order_validation"]["logical_order_is_not_asset_order"] is True
    assert packet["crop_order_validation"]["physical_crop_asset_order"] == [
        "P010-B001-TES",
        "P010-B002-TES",
        "P010-B005-TES",
        "P010-B006-TES",
    ]
    assert packet["crop_order_validation"]["required_before"] == ["semantic_map", "pcrp"]
    assert packet["crop_order_validation"]["continuation_edges"] == [
        {
            "from": "P010-B005-TES",
            "to": "P010-B002-TES",
            "reason": "Hyeon body continues from lower-left block into upper-right block",
        }
    ]
    assert "P010-B001-TES -> P010-B005-TES -> P010-B002-TES -> P010-B006-TES" in text_map
    assert "Crop order validation: `passed`" in text_map
    assert "boots and green burberry waterproof jacket" in text_map
    assert "Voice Recorder (with moans and screams recorded to it)" in text_map
    assert "Ku Hyeon (Investigator)" in text_map
    assert "They constantly threaten to send someone over to the" in text_map
    assert "US to bring him back" in text_map
    assert "Electronic Tool Kit, Headcams (5)" in text_map
    assert "Maya Adeduwon (NPC)" in text_map
    assert "She has hours of Video Tape (VT) footage that she can slot into" in text_map
    assert "```text" in text_map


def test_page_010_text_summary_exposes_review_boundary():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "draft_text_ready_for_bogdan_review_no_ocr_acceptance" in summary
    assert "Logical reading order: `B001 -> B005 -> B002 -> B006`" in summary
    assert "Creates no OCR run/output acceptance" in summary
    assert "p010 text ok" in summary
