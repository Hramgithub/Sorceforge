import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_010_triage.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_010_triage_G1_VIRAL_001"
PACKET = OUT_ROOT / "page_010_triage_packet.json"
REPORT = OUT_ROOT / "page_010_triage_report.json"
SUMMARY = OUT_ROOT / "page_010_triage_summary.md"
AUTH = "BA-G1-VIRAL-PAGE-010-TRIAGE-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_010_triage_is_fail_closed():
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


def test_page_010_triage_is_bounded_crop_contract_only():
    report = read_json(REPORT)

    assert report["package_id"] == "P010TR-G1-VIRAL-001"
    assert report["status"] == "page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp"
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


def test_page_010_triage_routes_profile_spread_without_text_extraction_or_pcrp():
    packet = read_json(PACKET)

    assert packet["page"] == "010"
    assert packet["page_identity"]["plain_label"] == "dual_profile_mixed_page"
    assert packet["triage_result"]["current_cursor"] == "page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp"
    assert packet["triage_result"]["recommended_next_candidate"] == "bogdan_review_of_p010tr_001_before_any_text_extraction_or_pcrp_authorization"
    assert packet["triage_result"]["review_crop_disposition"] == "role_separated_human_review_and_text_evidence_crops_from_start"
    assert packet["triage_result"]["requires_new_ocr"] is False
    assert packet["triage_result"]["requires_new_render"] is False
    assert packet["triage_result"]["requires_pdf_or_raw_mutation"] is False
    assert packet["triage_result"]["text_extraction_created"] is False
    assert packet["triage_result"]["semantic_map_created"] is False
    assert packet["triage_result"]["page_complete_acceptance_created"] is False
    assert packet["blocked_capabilities"]["pages_011_020_processing"] is False


def test_page_010_triage_has_prm_aligned_blocks_and_role_separated_assets():
    packet = read_json(PACKET)
    blocks = {block["block_id"]: block for block in packet["review_blocks"]}

    assert set(blocks) == {"P010-B001", "P010-B002", "P010-B003", "P010-B004", "P010-B005", "P010-B006"}
    assert [blocks[f"P010-B00{i}"]["source_region_id"] for i in range(1, 7)] == [
        "PRM-G1-VIRAL-001-P010-R01",
        "PRM-G1-VIRAL-001-P010-R02",
        "PRM-G1-VIRAL-001-P010-R03",
        "PRM-G1-VIRAL-001-P010-R04",
        "PRM-G1-VIRAL-001-P010-R05",
        "PRM-G1-VIRAL-001-P010-R05",
    ]
    assert blocks["P010-B001"]["source_region_box_px"] == [230, 220, 910, 460]
    assert blocks["P010-B002"]["source_region_box_px"] == [1380, 220, 930, 460]
    assert blocks["P010-B003"]["content_kind"] == "art_anchor"
    assert blocks["P010-B004"]["content_kind"] == "art_anchor"
    assert "ocr_candidate_crop_box_px" not in blocks["P010-B003"]
    assert blocks["P010-B005"]["source_region_split"] == "left_derived_from_R05"
    assert blocks["P010-B006"]["source_region_split"] == "right_derived_from_R05"
    assert "text_evidence_surfaces" not in blocks["P010-B005"]
    assert "text_evidence_surfaces" not in blocks["P010-B006"]
    assert blocks["P010-B005"]["human_review_crop_box_px"] == blocks["P010-B005"]["text_evidence_crop_box_px"]
    assert blocks["P010-B006"]["human_review_crop_box_px"] == blocks["P010-B006"]["text_evidence_crop_box_px"]
    assert "lower-profile-text-area-human-context" not in blocks["P010-B005"]["human_review_asset"]
    assert "lower-profile-text-area-human-context" not in blocks["P010-B006"]["human_review_asset"]
    for block in blocks.values():
        assert (OUT_ROOT / block["human_review_asset"]).exists()
        assert block["human_review_asset_sha256"]
        if block["content_kind"] == "text_like_region":
            surfaces = block.get("text_evidence_surfaces") or [
                {
                    "ocr_candidate_asset": block["ocr_candidate_asset"],
                    "text_evidence_asset": block["text_evidence_asset"],
                    "ocr_candidate_asset_sha256": block["ocr_candidate_asset_sha256"],
                    "text_evidence_asset_sha256": block["text_evidence_asset_sha256"],
                }
            ]
            for surface in surfaces:
                assert (OUT_ROOT / surface["ocr_candidate_asset"]).exists()
                assert (OUT_ROOT / surface["text_evidence_asset"]).exists()
                assert surface["ocr_candidate_asset_sha256"]
                assert surface["text_evidence_asset_sha256"]


def test_page_010_crop_contract_qa_blocks_human_crop_as_ocr_evidence():
    packet = read_json(PACKET)
    qa = packet["crop_qa"]

    assert qa["status"] == "passed"
    assert qa["findings"] == []
    assert qa["semantic_text_map_linkage"]["human_review_crop_satisfies_text_evidence"] is False
    assert qa["page_map_reconciliation"]["represented_text_like_regions"] == [
        "PRM-G1-VIRAL-001-P010-R01",
        "PRM-G1-VIRAL-001-P010-R02",
        "PRM-G1-VIRAL-001-P010-R05",
    ]
    assert qa["page_map_reconciliation"]["text_evidence_surface_ids"] == [
        "P010-B001-TES",
        "P010-B002-TES",
        "P010-B005-TES",
        "P010-B006-TES",
    ]
    assert qa["layout_disposition"]["lower_prm_region_split_for_ocr"] is True
    assert qa["layout_disposition"]["shared_lower_human_review_crop_allowed"] is False
    assert all(check["status"] == "passed" for check in qa["checks"])
    assert all(check["overlaps_art_or_portrait_source_region"] is False for check in qa["checks"])
    assert all(check["source_region_box_is_lineage_not_ocr_boundary"] is True for check in qa["checks"])


def test_page_010_triage_records_sol_terra_reviews():
    packet = read_json(PACKET)
    reviews = packet["sol_terra_reviews"]

    assert [item["layer"] for item in reviews] == ["G1SP-004", "P010TR-001", "P010TR-001-crops"]
    assert all(item["sol"].startswith("OK") for item in reviews)
    assert all(item["terra"].startswith("OK") for item in reviews)
    assert packet["capabilities_created"]["ocr_crop_contract_created"] is True
    assert packet["capabilities_created"]["text_extraction_created"] is False
    assert packet["capabilities_created"]["semantic_map_created"] is False
    assert packet["capabilities_created"]["pcrp_readiness_created"] is False


def test_page_010_triage_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "Page 010 Triage Crop Contract Packet - P010TR-G1-VIRAL-001" in summary
    assert "dual-profile mixed page" in summary
    assert "Lower `R05` is one PRM region but is represented as two independent lower text blocks" in summary
    assert "No shared lower human review crop is allowed" in summary
    assert "no text extraction" in summary
    assert "Decision after review: `p010 triage ok` or `hold p010 triage: <reason>`." in summary
