import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_009_triage.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_009_triage_G1_VIRAL_003"
PACKET = OUT_ROOT / "page_009_triage_packet.json"
REPORT = OUT_ROOT / "page_009_triage_report.json"
SUMMARY = OUT_ROOT / "page_009_triage_summary.md"
AUTH = "BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-003"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_009_triage_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-001-TRIAGE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_009_triage_is_status_only_and_bounded():
    report = read_json(REPORT)

    assert report["package_id"] == "P009TR-G1-VIRAL-003"
    assert report["status"] == "page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked"
    assert report["ocr_crop_contract_created"] is True
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


def test_page_009_triage_routes_profile_spread_without_ocr():
    packet = read_json(PACKET)

    assert packet["page"] == "009"
    assert packet["supersedes"]["package_id"] == "P009TR-G1-VIRAL-002"
    assert packet["supersedes"]["reason"] == "historical_readability_only_stale_for_pcrp_routing"
    assert packet["page_identity"]["plain_label"] == "two-profile visual/text composition"
    assert packet["triage_result"]["current_cursor"] == "page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked"
    assert packet["triage_result"]["previous_recommendation_disposition"] == "superseded_for_pcrp_purposes"
    assert packet["triage_result"]["recommended_next_candidate"] == "bogdan_review_of_p009tr_003_crop_contract_before_any_pcrp_authorization"
    assert packet["triage_result"]["review_crop_disposition"] == "role_separated_human_review_and_text_evidence_crops"
    assert packet["triage_result"]["requires_new_ocr"] is False
    assert packet["triage_result"]["requires_new_render"] is False
    assert packet["triage_result"]["requires_pdf_or_raw_mutation"] is False
    assert packet["triage_result"]["page_complete_acceptance_created"] is False
    assert packet["blocked_capabilities"]["pages_010_020_processing"] is False


def test_page_009_triage_has_four_role_separated_blocks_and_assets():
    packet = read_json(PACKET)
    blocks = {block["block_id"]: block for block in packet["review_blocks"]}

    assert set(blocks) == {"P009-B001", "P009-B002", "P009-B003", "P009-B004"}
    assert blocks["P009-B001"]["content_kind"] == "art_anchor"
    assert blocks["P009-B002"]["content_kind"] == "art_anchor"
    assert blocks["P009-B003"]["content_kind"] == "text_like_region"
    assert blocks["P009-B004"]["content_kind"] == "text_like_region"
    assert blocks["P009-B001"]["source_region_box_px"] == [180, 260, 1030, 920]
    assert blocks["P009-B001"]["human_review_crop_box_px"] == [160, 225, 1085, 1005]
    assert "ocr_candidate_crop_box_px" not in blocks["P009-B001"]
    assert blocks["P009-B003"]["human_review_crop_box_px"] == [140, 1090, 1115, 1960]
    assert blocks["P009-B003"]["ocr_candidate_crop_box_px"] == [55, 1540, 1215, 1500]
    assert blocks["P009-B003"]["text_evidence_crop_box_px"] == [50, 1540, 1225, 1500]
    assert blocks["P009-B004"]["source_region_box_px"] == [1320, 1200, 1030, 1650]
    assert blocks["P009-B004"]["human_review_crop_box_px"] == [1280, 1090, 1115, 1960]
    assert blocks["P009-B004"]["ocr_candidate_crop_box_px"] == [1280, 1540, 1215, 1500]
    assert blocks["P009-B004"]["text_evidence_crop_box_px"] == [1275, 1540, 1225, 1500]
    for block in blocks.values():
        assert (OUT_ROOT / block["human_review_asset"]).exists()
        assert block["human_review_asset_sha256"]
        if block["content_kind"] == "text_like_region":
            assert (OUT_ROOT / block["ocr_candidate_asset"]).exists()
            assert (OUT_ROOT / block["text_evidence_asset"]).exists()
            assert block["ocr_candidate_asset_sha256"]
            assert block["text_evidence_asset_sha256"]


def test_page_009_crop_contract_qa_blocks_human_crop_as_ocr_evidence():
    packet = read_json(PACKET)
    qa = packet["crop_qa"]

    assert qa["status"] == "passed"
    assert qa["findings"] == []
    assert qa["semantic_text_map_linkage"]["human_review_crop_satisfies_text_evidence"] is False
    assert qa["page_map_reconciliation"]["represented_text_like_regions"] == [
        "PRM-G1-VIRAL-001-P009-R03",
        "PRM-G1-VIRAL-001-P009-R04",
    ]
    assert qa["page_map_reconciliation"]["text_evidence_crop_block_ids"] == ["P009-B003", "P009-B004"]
    assert qa["right_lower_grey_block"] == {"status": "complete_non_blocker", "block_id": "P009-B004"}
    assert qa["non_blocker_annotation_validation"]["status"] == "passed"
    assert qa["non_blocker_annotations"][0]["decision"] == "complete_non_blocker"
    assert "P009-B004" in qa["non_blocker_annotations"][0]["affected_ids"]
    assert all(check["status"] == "passed" for check in qa["checks"])
    assert all(check["overlaps_art_or_portrait_source_region"] is False for check in qa["checks"])
    assert all(check["source_region_box_is_lineage_not_ocr_boundary"] is True for check in qa["checks"])


def test_page_009_crop_contract_records_sol_terra_per_step_reviews():
    packet = read_json(PACKET)
    reviews = packet["sol_terra_step_reviews"]

    assert [item["step"] for item in reviews] == list(range(1, 9))
    assert all(item["sol"].startswith("OK") for item in reviews)
    assert all(item["terra"].startswith("OK") for item in reviews)
    assert packet["capabilities_created"]["ocr_crop_contract_created"] is True
    assert packet["capabilities_created"]["ocr_execution_created"] is False
    assert packet["capabilities_created"]["ocr_evidence_created"] is False
    assert packet["capabilities_created"]["pcrp_readiness_created"] is False


def test_page_009_triage_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Page 009 Crop Contract Packet - P009TR-G1-VIRAL-003" in summary
    assert "two-profile visual/text composition" in summary
    assert "Supersedes: `P009TR-G1-VIRAL-002`" in summary
    assert "no page-complete acceptance" in summary
    assert "Decision after review: `p009 crop contract ok` or `hold p009 crop contract: <reason>`." in summary
