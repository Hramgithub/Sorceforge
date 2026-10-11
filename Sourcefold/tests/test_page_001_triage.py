import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_001_triage.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_001_triage_G1_VIRAL_001"
PACKET = OUT_ROOT / "page_001_triage_packet.json"
REPORT = OUT_ROOT / "page_001_triage_report.json"
SUMMARY = OUT_ROOT / "page_001_triage_summary.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_001_triage_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P002-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-PAGE-001-TRIAGE-001" in wrong_auth.stderr


def test_page_001_triage_is_status_only_and_bounded():
    report = read_json(REPORT)

    assert report["package_id"] == "P001TR-G1-VIRAL-001"
    assert report["status"] == "page_001_triage_ready_for_bogdan_routing_decision"
    assert report["page_complete_acceptance_created"] is False
    assert report["whole_gate_1_acceptance_created"] is False
    assert report["fixture_admission"] is False
    assert report["ocr_execution"] is False
    assert report["render_execution"] is False
    assert report["pdf_parsing_or_text_layer_extraction"] is False
    assert report["raw_mutation"] is False
    assert report["translation"] is False
    assert report["proofreading"] is False
    assert report["implementation"] is False
    assert report["push"] is False


def test_page_001_triage_routes_cover_title_without_ocr():
    packet = read_json(PACKET)

    assert packet["page"] == "001"
    assert packet["page_identity"]["plain_label"] == "cover/title composition"
    assert packet["triage_result"]["recommended_next_candidate"] == "page_001_visual_title_page_complete_review_without_ocr"
    assert packet["triage_result"]["requires_new_ocr"] is False
    assert packet["triage_result"]["requires_new_render"] is False
    assert packet["triage_result"]["requires_pdf_or_raw_mutation"] is False
    assert packet["triage_result"]["page_complete_acceptance_created"] is False


def test_page_001_triage_has_review_blocks_and_assets():
    packet = read_json(PACKET)
    blocks = {block["block_id"]: block for block in packet["review_blocks"]}

    assert set(blocks) == {"P001-B001", "P001-B002", "P001-B003"}
    assert blocks["P001-B001"]["content_kind"] == "visual_anchor"
    assert blocks["P001-B001"]["not_source_text"] is True
    assert blocks["P001-B002"]["content_kind"] == "title_visual_anchor"
    assert blocks["P001-B002"]["visible_text_hint"] == "VIRAL / UNREDACTED"
    assert blocks["P001-B002"]["review_crop_box_px"] == [500, 80, 1550, 1030]
    assert blocks["P001-B003"]["content_kind"] == "mixed_footer_visual_anchor"
    assert blocks["P001-B003"]["review_crop_box_px"] == [40, 2740, 2460, 520]
    for block in blocks.values():
        assert (OUT_ROOT / block["review_asset"]).exists()
        assert block["review_asset_sha256"]


def test_page_001_triage_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Page 001 Triage Packet - P001TR-G1-VIRAL-001" in summary
    assert "cover/title composition" in summary
    assert "VIRAL / UNREDACTED" in summary
    assert "no page-complete acceptance" in summary
    assert "Decision after review: `page 001 route ok` or `hold page 001 triage: <reason>`." in summary
