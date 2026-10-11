import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_011_triage.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_011_triage_G1_VIRAL_001"
PACKET = OUT_ROOT / "page_011_triage_packet.json"
REPORT = OUT_ROOT / "page_011_triage_report.json"
SUMMARY = OUT_ROOT / "page_011_triage_summary.md"
AUTH = "BA-G1-VIRAL-PAGE-011-TRIAGE-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_011_triage_is_fail_closed():
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


def test_page_011_triage_is_bounded_crop_contract_only():
    report = read_json(REPORT)

    assert report["package_id"] == "P011TR-G1-VIRAL-001"
    assert report["status"] == "page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp"
    assert report["ocr_crop_contract_created"] is True
    assert report["text_extraction_created"] is False
    assert report["semantic_map_created"] is False
    assert report["pcrp_readiness_created"] is False
    assert report["crop_qa_status"] == "passed"
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


def test_page_011_triage_routes_mixed_profile_page_without_text_extraction_or_pcrp():
    packet = read_json(PACKET)

    assert packet["page"] == "011"
    assert packet["page_identity"]["plain_label"] == "mixed_profile_continuation_page"
    assert packet["triage_result"]["current_cursor"] == "page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp"
    assert packet["triage_result"]["recommended_next_candidate"] == "bogdan_review_of_p011tr_001_before_any_text_extraction_or_pcrp_authorization"
    assert packet["triage_result"]["review_crop_disposition"] == "role_separated_human_review_and_text_evidence_crops_from_start"
    assert packet["triage_result"]["requires_new_ocr"] is False
    assert packet["triage_result"]["requires_new_render"] is False
    assert packet["triage_result"]["requires_pdf_or_raw_mutation"] is False
    assert packet["triage_result"]["text_extraction_created"] is False
    assert packet["triage_result"]["semantic_map_created"] is False
    assert packet["triage_result"]["page_complete_acceptance_created"] is False
    assert packet["blocked_capabilities"]["pages_012_020_processing"] is False


def test_page_011_triage_has_prm_aligned_blocks_and_role_separated_assets():
    packet = read_json(PACKET)
    blocks = {block["block_id"]: block for block in packet["review_blocks"]}

    assert set(blocks) == {"P011-B001", "P011-B002", "P011-B003", "P011-B004"}
    assert [blocks[f"P011-B00{i}"]["source_region_id"] for i in range(1, 5)] == [
        "PRM-G1-VIRAL-001-P011-R01",
        "PRM-G1-VIRAL-001-P011-R02",
        "PRM-G1-VIRAL-001-P011-R03",
        "PRM-G1-VIRAL-001-P011-R04",
    ]
    assert blocks["P011-B001"]["content_kind"] == "text_like_region"
    assert blocks["P011-B002"]["content_kind"] == "art_anchor"
    assert blocks["P011-B003"]["content_kind"] == "art_anchor"
    assert blocks["P011-B004"]["content_kind"] == "text_like_region"
    assert "ocr_candidate_crop_box_px" not in blocks["P011-B002"]
    assert "ocr_candidate_crop_box_px" not in blocks["P011-B003"]
    assert blocks["P011-B001"]["external_continues_from"] == "P010/Maya continuation"
    assert blocks["P011-B004"]["external_continues_to"] == "P012/Emily continuation"
    for block in blocks.values():
        assert (OUT_ROOT / block["human_review_asset"]).exists()
        assert block["human_review_asset_sha256"]
        if block["content_kind"] == "text_like_region":
            assert (OUT_ROOT / block["ocr_candidate_asset"]).exists()
            assert (OUT_ROOT / block["text_evidence_asset"]).exists()
            assert block["ocr_candidate_asset_sha256"]
            assert block["text_evidence_asset_sha256"]


def test_page_011_crop_contract_qa_blocks_art_as_text_evidence():
    packet = read_json(PACKET)
    qa = packet["crop_qa"]

    assert qa["status"] == "passed"
    assert qa["findings"] == []
    assert qa["semantic_text_map_linkage"]["human_review_crop_satisfies_text_evidence"] is False
    assert qa["page_map_reconciliation"]["represented_text_like_regions"] == [
        "PRM-G1-VIRAL-001-P011-R01",
        "PRM-G1-VIRAL-001-P011-R04",
    ]
    assert qa["page_map_reconciliation"]["text_evidence_surface_ids"] == [
        "P011-B001-TES",
        "P011-B004-TES",
    ]
    assert qa["layout_disposition"]["shared_mixed_text_art_crop_allowed"] is False
    assert qa["recommended_later_text_order"] == ["P011-B001-TES", "P011-B004-TES"]
    assert all(check["status"] == "passed" for check in qa["checks"])
    assert all(check["overlaps_art_or_portrait_source_region"] is False for check in qa["checks"])
    assert all(check["source_region_box_is_lineage_not_ocr_boundary"] is True for check in qa["checks"])


def test_page_011_triage_records_sol_terra_reviews():
    packet = read_json(PACKET)
    reviews = packet["sol_terra_reviews"]

    assert [item["layer"] for item in reviews] == ["G1SP-005", "P011TR-001", "P011TR-001-crops"]
    assert all(item["sol"].startswith("OK") for item in reviews)
    assert all(item["terra"].startswith("OK") for item in reviews)
    assert packet["capabilities_created"]["ocr_crop_contract_created"] is True
    assert packet["capabilities_created"]["text_extraction_created"] is False
    assert packet["capabilities_created"]["semantic_map_created"] is False
    assert packet["capabilities_created"]["pcrp_readiness_created"] is False


def test_page_011_triage_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Page 011 Triage Crop Contract Packet - P011TR-G1-VIRAL-001" in summary
    assert "mixed profile continuation page" in summary
    assert "Text-like source regions: `R01`, `R04`." in summary
    assert "Art anchors: `R02`, `R03`." in summary
    assert "Decision after review: `p011 triage ok` or `hold p011 triage: <reason>`." in summary
