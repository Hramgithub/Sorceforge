from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image

from crop_role_contract import iter_text_surfaces, validate_crop_role_contract


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_011_triage.py"
TEST_PATH = ROOT / "tests" / "test_page_011_triage.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUTPUT_ROOT = TRIAL_ROOT / "page_011_triage_G1_VIRAL_001"
ASSET_ROOT = OUTPUT_ROOT / "review_assets"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-011-TRIAGE-001"
PACKAGE_ID = "P011TR-G1-VIRAL-001"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_011.png"

PAGE_IMAGE_SHA256 = "697DE9B2B13A2E48B11D60DA0A5D4D4183A0FFFA89509EE813D19D1390D77BE6"
G1SP_005_PACKET_SHA256 = "E696DE1651E43539A07ECA958B948678DE7FFAAE61EB426F2CE46C478C5310E2"
PRM_REPORT_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
CONTENT_MAP_SHA256 = "335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79"
ART_MAP_SHA256 = "77BD88C0522E17DF98603364677BC248450EC3E57996389881629E581197C544"

REVIEW_BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P011-B001",
        "role": "left_maya_continuation_secret_appearance_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P011-R01",
        "source_region_box_px": [150, 280, 820, 1750],
        "human_review_crop_box_px": [170, 210, 1080, 1900],
        "ocr_candidate_crop_box_px": [170, 210, 1080, 1900],
        "text_evidence_crop_box_px": [170, 210, 1080, 1900],
        "human_review_asset": "review_assets/1_P011-left-maya-continuation-secret-appearance-human-context.png",
        "ocr_candidate_asset": "review_assets/1a_P011-left-maya-continuation-secret-appearance-ocr-candidate.png",
        "text_evidence_asset": "review_assets/1b_P011-left-maya-continuation-secret-appearance-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_text_extraction_after_human_review",
        "not_ocr_verified_text": True,
        "external_continues_from": "P010/Maya continuation",
    },
    {
        "block_id": "P011-B002",
        "role": "emily_em_lavigne_portrait_image_area",
        "content_kind": "art_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P011-R02",
        "source_region_box_px": [1040, 470, 1050, 1250],
        "visual_pollution_guard_box_px": [1260, 220, 850, 1320],
        "human_review_crop_box_px": [1110, 220, 1000, 1320],
        "human_review_asset": "review_assets/2_P011-emily-em-lavigne-portrait-image-area-human-context.png",
        "routing": "defer_visual_anchor_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P011-B003",
        "role": "lower_left_screen_image_area",
        "content_kind": "art_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P011-R03",
        "source_region_box_px": [150, 2220, 820, 650],
        "visual_pollution_guard_box_px": [170, 2190, 1080, 900],
        "human_review_crop_box_px": [170, 2190, 1080, 900],
        "human_review_asset": "review_assets/3_P011-lower-left-screen-image-area-human-context.png",
        "routing": "defer_visual_anchor_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P011-B004",
        "role": "right_emily_profile_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P011-R04",
        "source_region_box_px": [1040, 1780, 1200, 1150],
        "human_review_crop_box_px": [1260, 1560, 1080, 1530],
        "ocr_candidate_crop_box_px": [1260, 1560, 1080, 1530],
        "text_evidence_crop_box_px": [1260, 1560, 1080, 1530],
        "human_review_asset": "review_assets/4_P011-right-emily-profile-text-human-context.png",
        "ocr_candidate_asset": "review_assets/4a_P011-right-emily-profile-text-ocr-candidate.png",
        "text_evidence_asset": "review_assets/4b_P011-right-emily-profile-text-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_text_extraction_after_human_review",
        "not_ocr_verified_text": True,
        "external_continues_to": "P012/Emily continuation",
    },
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build page 011 triage/readiness crop-contract packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 011 triage is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 011 triage requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "post_p010_gate_1_status_route_packet": {
            "path": TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_005" / "gate_1_status_packet.json",
            "sha256": G1SP_005_PACKET_SHA256,
        },
        "provisional_region_map_report": {"path": TRIAL_ROOT / "provisional_region_map_report.md", "sha256": PRM_REPORT_SHA256},
        "content_map_trial_report": {"path": TRIAL_ROOT / "content_map_trial_report.md", "sha256": CONTENT_MAP_SHA256},
        "art_map_trial_report": {"path": TRIAL_ROOT / "art_map_trial_report.md", "sha256": ART_MAP_SHA256},
        "page_011_image": {"path": PAGE_IMAGE, "sha256": PAGE_IMAGE_SHA256},
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        expected = item["sha256"]
        if expected == "PENDING":
            raise SystemExit(f"predecessor hash for {name} has not been locked")
        if actual != expected:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": item["path"].relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def crop_asset(image: Image.Image, box: list[int], asset_path: str) -> dict[str, str]:
    x, y, width, height = box
    target = OUTPUT_ROOT / asset_path
    target.parent.mkdir(parents=True, exist_ok=True)
    image.crop((x, y, x + width, y + height)).save(target)
    return {"path": target.relative_to(ROOT).as_posix(), "sha256": sha256_file(target)}


def build_crop_qa(blocks: list[dict[str, Any]], image_assets: dict[str, dict[str, str]]) -> dict[str, Any]:
    return validate_crop_role_contract(
        blocks=blocks,
        output_root=OUTPUT_ROOT,
        image_assets=image_assets,
        max_edge_ink_ratio=0.18,
        extra_fields={
            "layout_disposition": {
                "page_type": "mixed_profile_continuation_page",
                "text_like_region_count": 2,
                "art_count": 2,
                "shared_mixed_text_art_crop_allowed": False,
            },
            "recommended_later_text_order": ["P011-B001-TES", "P011-B004-TES"],
        },
    )


def build_packet(predecessors: list[dict[str, str]], image_assets: dict[str, dict[str, str]]) -> dict[str, Any]:
    blocks = []
    for block in REVIEW_BLOCKS:
        item = dict(block)
        item["human_review_asset_sha256"] = image_assets[block["human_review_asset"]]["sha256"]
        if block["content_kind"] == "text_like_region":
            for surface in iter_text_surfaces(item):
                surface["ocr_candidate_asset_sha256"] = image_assets[surface["ocr_candidate_asset"]]["sha256"]
                surface["text_evidence_asset_sha256"] = image_assets[surface["text_evidence_asset"]]["sha256"]
            if "text_evidence_surfaces" not in item:
                item["ocr_candidate_asset_sha256"] = image_assets[item["ocr_candidate_asset"]]["sha256"]
                item["text_evidence_asset_sha256"] = image_assets[item["text_evidence_asset"]]["sha256"]
        blocks.append(item)
    crop_qa = build_crop_qa(blocks, image_assets)
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp",
        "scope": "page_011_triage_and_crop_role_contract_only_no_text_extraction_no_pcrp_no_acceptance",
        "predecessors": predecessors,
        "page": "011",
        "page_identity": {
            "page_id": "PG-G1-VIRAL-P011",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P011",
            "image_sha256": PAGE_IMAGE_SHA256,
            "plain_label": "mixed_profile_continuation_page",
        },
        "triage_result": {
            "current_cursor": "page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp",
            "recommended_next_candidate": "bogdan_review_of_p011tr_001_before_any_text_extraction_or_pcrp_authorization",
            "review_crop_disposition": "role_separated_human_review_and_text_evidence_crops_from_start",
            "requires_new_ocr": False,
            "requires_new_render": False,
            "requires_pdf_or_raw_mutation": False,
            "text_extraction_created": False,
            "semantic_map_created": False,
            "pcrp_readiness_created": False,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
        },
        "review_blocks": blocks,
        "crop_qa": crop_qa,
        "sol_terra_reviews": [
            {"layer": "G1SP-005", "sol": "OK pages 001-010 are bound as accepted-only predecessors and route now points to P011", "terra": "OK status-only packet creates no P011 authority or Gate acceptance"},
            {"layer": "P011TR-001", "sol": "OK P011 PRM/content/art-map inputs reconcile to two text-like regions and two art anchors", "terra": "OK no OCR/text output/PCRP/page acceptance is created"},
            {"layer": "P011TR-001-crops", "sol": "OK text surfaces are role-separated and art anchors are kept visual-only", "terra": "OK no mixed text/art crop is promoted as OCR evidence"},
        ],
        "decision_options": ["p011 triage ok", "hold p011 triage: <reason>"],
        "capabilities_created": {
            "ocr_crop_contract_created": True,
            "text_extraction_created": False,
            "semantic_map_created": False,
            "ocr_execution_created": False,
            "ocr_output_created": False,
            "pcrp_readiness_created": False,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
            "fixture_admission_created": False,
            "source_acceptance_mutation_created": False,
            "pages_012_020_processing_created": False,
        },
        "blocked_capabilities": {
            "page_complete_acceptance": False,
            "whole_gate_1_acceptance": False,
            "fixture_admission": False,
            "source_acceptance_mutation": False,
            "ocr_execution": False,
            "render_execution": False,
            "pdf_parsing_or_text_layer_extraction": False,
            "raw_mutation": False,
            "translation": False,
            "proofreading": False,
            "renderer_profile_acceptance": False,
            "implementation": False,
            "push": False,
            "pages_012_020_processing": False,
        },
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 011 Triage Crop Contract Packet - P011TR-G1-VIRAL-001",
            "",
            "Status: `page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp`",
            "",
            "Purpose: review whether page 011 has a clean role-separated triage/crop contract before any text extraction, semantic map, PCRP, or page-complete acceptance.",
            "",
            "Boundary: this packet creates no OCR run, no OCR output/evidence, no text extraction, no semantic map, no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no render/PDF/raw mutation, and no pages 012-020 processing.",
            "",
            "## Observed Page 011",
            "",
            "- Page type: mixed profile continuation page.",
            "- Source map: `PRM-G1-VIRAL-001-P011-R01`..`R04`.",
            "- Text-like source regions: `R01`, `R04`.",
            "- Art anchors: `R02`, `R03`.",
            "- Later text order candidate: `P011-B001-TES` then `P011-B004-TES`.",
            "",
            "## Review Blocks",
            "",
            "- `P011-B001`: left Maya continuation/secret/appearance text with source, human, OCR-candidate, and text-evidence boxes.",
            "- `P011-B002`: Emily 'Em' Lavigne portrait/image area, human context only.",
            "- `P011-B003`: lower-left screen image area, human context only.",
            "- `P011-B004`: right Emily profile text with source, human, OCR-candidate, and text-evidence boxes.",
            "",
            "## Routing Recommendation",
            "",
            "- Recommended next candidate: Bogdan review of `P011TR-G1-VIRAL-001`.",
            "- If accepted, the next separate bounded layer should be page 011 text extraction from the text evidence crops.",
            "",
            "Decision after review: `p011 triage ok` or `hold p011 triage: <reason>`.",
            "",
        ]
    )


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PAGE_IMAGE, ASSET_ROOT / "page_011.png")
    image_assets: dict[str, dict[str, str]] = {
        "review_assets/page_011.png": {"path": (ASSET_ROOT / "page_011.png").relative_to(ROOT).as_posix(), "sha256": sha256_file(ASSET_ROOT / "page_011.png")}
    }
    with Image.open(PAGE_IMAGE) as image:
        for block in REVIEW_BLOCKS:
            image_assets[block["human_review_asset"]] = crop_asset(image, block["human_review_crop_box_px"], block["human_review_asset"])
            if block["content_kind"] != "text_like_region":
                continue
            for surface in iter_text_surfaces(block):
                image_assets[surface["ocr_candidate_asset"]] = crop_asset(image, surface["ocr_candidate_crop_box_px"], surface["ocr_candidate_asset"])
                image_assets[surface["text_evidence_asset"]] = crop_asset(image, surface["text_evidence_crop_box_px"], surface["text_evidence_asset"])
    packet = build_packet(predecessors, image_assets)

    write_json(OUTPUT_ROOT / "page_011_triage_packet.json", packet)
    (OUTPUT_ROOT / "page_011_triage_summary.md").write_text(build_summary(packet), encoding="utf-8", newline="\n")
    write_json(
        OUTPUT_ROOT / "page_011_triage_report.json",
        {
            "package_id": PACKAGE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
            "fixture_admission": False,
            "ocr_execution": False,
            "text_extraction_created": False,
            "semantic_map_created": False,
            "render_execution": False,
            "pdf_parsing_or_text_layer_extraction": False,
            "raw_mutation": False,
            "translation": False,
            "proofreading": False,
            "implementation": False,
            "push": False,
            "recommended_next_candidate": packet["triage_result"]["recommended_next_candidate"],
            "crop_qa_status": packet["crop_qa"]["status"],
            "pcrp_readiness_created": False,
            "ocr_crop_contract_created": True,
        },
    )
    lines = [
        "# Page 011 Triage Crop Contract Manifest - P011TR-G1-VIRAL-001",
        "",
        "Status: `page_011_triage_crop_contract_ready_for_bogdan_review_no_text_extraction_no_pcrp`",
        "",
        "Boundary: no text extraction, no semantic map, no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no OCR/render/PDF/raw mutation, no pages 012-020 processing.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_011_triage_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    (OUTPUT_ROOT / "page_011_triage_manifest.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    check_authorization()
    write_outputs()
