from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image

from crop_role_contract import validate_crop_role_contract
from non_blocker_annotations import validate_non_blocker_annotations


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_009_triage.py"
TEST_PATH = ROOT / "tests" / "test_page_009_triage.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUTPUT_ROOT = TRIAL_ROOT / "page_009_triage_G1_VIRAL_003"
ASSET_ROOT = OUTPUT_ROOT / "review_assets"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-009-CROP-CONTRACT-003"
PACKAGE_ID = "P009TR-G1-VIRAL-003"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_009.png"

PAGE_IMAGE_SHA256 = "3EC853C61DED9F5009F3FD567A03D499408C25EE385169DFE0EC82A2C47FC456"
G1SP_003_PACKET_SHA256 = "769A9E7B53FE37876C7B883455FA6BF8C222E2118462923A5ABAF78BE090B1F6"
PRM_REPORT_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
PMR_REPORT_SHA256 = "72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F"
PIR_REPORT_SHA256 = "2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA"
P009TR_002_REPORT_SHA256 = "B58E943A8A37B5478E7976C8EF1B1BB20D0BF6F5451C5073497FE1A5CE9EB5D1"
P009TR_002_PACKET_SHA256 = "9560C86398642A466D5559608DACD59753723D88CF898D54091300117413F8DA"
P009TR_002_SUMMARY_SHA256 = "F435E104044F1E5E4B11E1547CA41ED072E3E2C0DA4323D9F59F97C52B2E6749"
P009TR_002_MANIFEST_SHA256 = "D347CB3075D63A6AAC5E515CA078055B6765A97104E729FF0EA6B73944C45C0B"

REVIEW_BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P009-B001",
        "role": "left_portrait_image_area",
        "content_kind": "art_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R01",
        "source_region_box_px": [180, 260, 1030, 920],
        "human_review_crop_box_px": [160, 225, 1085, 1005],
        "human_review_asset": "review_assets/1_P009-left-portrait-image-area-readable.png",
        "routing": "defer_visual_anchor_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P009-B002",
        "role": "right_portrait_image_area",
        "content_kind": "art_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R02",
        "source_region_box_px": [1320, 260, 1030, 920],
        "human_review_crop_box_px": [1300, 225, 1085, 1005],
        "human_review_asset": "review_assets/2_P009-right-portrait-image-area-readable.png",
        "routing": "defer_visual_anchor_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P009-B003",
        "role": "left_profile_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R03",
        "source_region_box_px": [180, 1200, 1030, 1650],
        "human_review_crop_box_px": [140, 1090, 1115, 1960],
        "ocr_candidate_crop_box_px": [55, 1540, 1215, 1500],
        "text_evidence_crop_box_px": [50, 1540, 1225, 1500],
        "human_review_asset": "review_assets/3_P009-left-profile-text-column-human-context.png",
        "ocr_candidate_asset": "review_assets/3a_P009-left-profile-text-column-ocr-candidate.png",
        "text_evidence_asset": "review_assets/3b_P009-left-profile-text-column-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_pcrp_after_human_review",
        "not_ocr_verified_text": True,
        "right_lower_grey_block_disposition": "not_applicable_left_column",
    },
    {
        "block_id": "P009-B004",
        "role": "right_profile_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R04",
        "source_region_box_px": [1320, 1200, 1030, 1650],
        "human_review_crop_box_px": [1280, 1090, 1115, 1960],
        "ocr_candidate_crop_box_px": [1280, 1540, 1215, 1500],
        "text_evidence_crop_box_px": [1275, 1540, 1225, 1500],
        "human_review_asset": "review_assets/4_P009-right-profile-text-column-human-context.png",
        "ocr_candidate_asset": "review_assets/4a_P009-right-profile-text-column-ocr-candidate.png",
        "text_evidence_asset": "review_assets/4b_P009-right-profile-text-column-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_pcrp_after_human_review",
        "not_ocr_verified_text": True,
        "right_lower_grey_block_disposition": "complete_non_blocker",
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
    parser = argparse.ArgumentParser(description="Build superseding page 009 triage/readiness routing packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 009 triage refresh is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 009 triage refresh requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "post_p001_gate_1_status_route_packet": {
            "path": TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_003" / "gate_1_status_packet.json",
            "sha256": G1SP_003_PACKET_SHA256,
        },
        "provisional_region_map_report": {"path": TRIAL_ROOT / "provisional_region_map_report.md", "sha256": PRM_REPORT_SHA256},
        "page_map_model_report": {"path": TRIAL_ROOT / "page_map_model_report.md", "sha256": PMR_REPORT_SHA256},
        "page_inventory_report": {"path": TRIAL_ROOT / "page_inventory_report.md", "sha256": PIR_REPORT_SHA256},
        "page_009_image": {"path": PAGE_IMAGE, "sha256": PAGE_IMAGE_SHA256},
        "p009tr_002_report": {
            "path": TRIAL_ROOT / "page_009_triage_G1_VIRAL_002" / "page_009_triage_report.json",
            "sha256": P009TR_002_REPORT_SHA256,
        },
        "p009tr_002_packet": {
            "path": TRIAL_ROOT / "page_009_triage_G1_VIRAL_002" / "page_009_triage_packet.json",
            "sha256": P009TR_002_PACKET_SHA256,
        },
        "p009tr_002_summary": {
            "path": TRIAL_ROOT / "page_009_triage_G1_VIRAL_002" / "page_009_triage_summary.md",
            "sha256": P009TR_002_SUMMARY_SHA256,
        },
        "p009tr_002_manifest": {
            "path": TRIAL_ROOT / "page_009_triage_G1_VIRAL_002" / "page_009_triage_manifest.md",
            "sha256": P009TR_002_MANIFEST_SHA256,
        },
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        expected = item["sha256"]
        if actual != expected:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": item["path"].relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def crop_asset(image: Image.Image, block: dict[str, Any], box_key: str, asset_key: str) -> dict[str, str]:
    x, y, width, height = block[box_key]
    target = OUTPUT_ROOT / block[asset_key]
    target.parent.mkdir(parents=True, exist_ok=True)
    image.crop((x, y, x + width, y + height)).save(target)
    return {"path": target.relative_to(ROOT).as_posix(), "sha256": sha256_file(target)}


def rects_overlap(a: list[int], b: list[int]) -> bool:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def edge_ink_ratios(path: Path) -> dict[str, float]:
    with Image.open(path).convert("RGB") as image:
        width, height = image.size
        margin = min(24, width // 8, height // 8)
        pixels = image.load()

        def is_ink(x: int, y: int) -> bool:
            r, g, b = pixels[x, y]
            black_text = r < 110 and g < 110 and b < 110
            red_text = r > 120 and g < 90 and b < 90
            green_text = r > 120 and g > 150 and b < 140
            return black_text or red_text or green_text

        bands = {
            "left": [(x, y) for x in range(margin) for y in range(height)],
            "right": [(x, y) for x in range(width - margin, width) for y in range(height)],
            "top": [(x, y) for x in range(width) for y in range(margin)],
            "bottom": [(x, y) for x in range(width) for y in range(height - margin, height)],
        }
        return {edge: round(sum(1 for x, y in coords if is_ink(x, y)) / len(coords), 4) for edge, coords in bands.items()}


def build_crop_qa(blocks: list[dict[str, Any]], image_assets: dict[str, dict[str, str]]) -> dict[str, Any]:
    def p009_is_ink(rgb: tuple[int, int, int]) -> bool:
        r, g, b = rgb
        black_text = r < 110 and g < 110 and b < 110
        red_text = r > 120 and g < 90 and b < 90
        green_text = r > 120 and g > 150 and b < 140
        return black_text or red_text or green_text

    non_blocker_annotations = [
        {
            "annotation_id": "NBA-P009-RIGHT-LOWER-GREY-BLOCK-001",
            "decision": "complete_non_blocker",
            "reviewer": "Bogdan",
            "evidence_ref": "P009-B004-TEXT-EVIDENCE",
            "affected_ids": ["P009-B004", "PRM-G1-VIRAL-001-P009-R04", "P009-B004-TEXT-EVIDENCE"],
            "downstream_limits": ["not_page_acceptance", "not_ocr_acceptance", "not_source_acceptance"],
        }
    ]
    known_ids = {block["block_id"] for block in blocks} | {block["source_region_id"] for block in blocks}
    known_ids.add("P009-B004-TEXT-EVIDENCE")
    return validate_crop_role_contract(
        blocks=blocks,
        output_root=OUTPUT_ROOT,
        image_assets=image_assets,
        max_edge_ink_ratio=0.02,
        is_ink=p009_is_ink,
        extra_fields={
            "right_lower_grey_block": {"status": "complete_non_blocker", "block_id": "P009-B004"},
            "non_blocker_annotations": non_blocker_annotations,
            "non_blocker_annotation_validation": validate_non_blocker_annotations(
                non_blocker_annotations,
                known_ids=known_ids,
            ),
        },
    )


def build_packet(predecessors: list[dict[str, str]], image_assets: dict[str, dict[str, str]]) -> dict[str, Any]:
    blocks = []
    for block in REVIEW_BLOCKS:
        item = dict(block)
        item["human_review_asset_sha256"] = image_assets[block["human_review_asset"]]["sha256"]
        if block["content_kind"] == "text_like_region":
            item["ocr_candidate_asset_sha256"] = image_assets[block["ocr_candidate_asset"]]["sha256"]
            item["text_evidence_asset_sha256"] = image_assets[block["text_evidence_asset"]]["sha256"]
        blocks.append(item)
    crop_qa = build_crop_qa(blocks, image_assets)
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked",
        "scope": "page_009_crop_role_contract_only_no_pcrp_no_ocr_no_acceptance",
        "supersedes": {
            "package_id": "P009TR-G1-VIRAL-002",
            "reason": "historical_readability_only_stale_for_pcrp_routing",
        },
        "predecessors": predecessors,
        "page": "009",
        "page_identity": {
            "page_id": "PG-G1-VIRAL-P009",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P009",
            "image_sha256": PAGE_IMAGE_SHA256,
            "plain_label": "two-profile visual/text composition",
        },
        "triage_result": {
            "current_cursor": "page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked",
            "previous_recommended_next_candidate": "page_009_page_complete_review_profile_candidate_without_new_ocr_or_render",
            "previous_recommendation_disposition": "superseded_for_pcrp_purposes",
            "recommended_next_candidate": "bogdan_review_of_p009tr_003_crop_contract_before_any_pcrp_authorization",
            "review_crop_disposition": "role_separated_human_review_and_text_evidence_crops",
            "requires_new_ocr": False,
            "requires_new_render": False,
            "requires_pdf_or_raw_mutation": False,
            "pcrp_readiness_created": False,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
        },
        "review_blocks": blocks,
        "crop_qa": crop_qa,
        "sol_terra_step_reviews": [
            {"step": 1, "sol": "OK cursor corrected to crop-contract state", "terra": "OK PCRP remains blocked"},
            {"step": 2, "sol": "OK P009TR-002 preserved as historical readability evidence", "terra": "OK stale for PCRP"},
            {"step": 3, "sol": "OK old route recommendation superseded", "terra": "OK no retro-mutation of 002"},
            {"step": 4, "sol": "OK bounded authorization is 003 only", "terra": "OK no OCR/PCRP/acceptance authority"},
            {"step": 5, "sol": "OK four crop roles present", "terra": "OK human crops cannot satisfy text evidence"},
            {"step": 6, "sol": "OK QA checks cover edges, pollution, page map, linkage", "terra": "OK right lower grey block non-blocker"},
            {"step": 7, "sol": "OK PCRP guard requires 003", "terra": "OK 002 rejected as PCRP predecessor"},
            {"step": 8, "sol": "OK ready for Bogdan crop-contract review", "terra": "OK do not open PCRP before review"},
        ],
        "decision_options": ["p009 crop contract ok", "hold p009 crop contract: <reason>"],
        "capabilities_created": {
            "ocr_crop_contract_created": True,
            "ocr_execution_created": False,
            "ocr_evidence_created": False,
            "ocr_output_created": False,
            "page_map_completeness_proof_created": False,
            "pcrp_readiness_created": False,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
            "fixture_admission_created": False,
            "source_acceptance_mutation_created": False,
            "pages_010_020_processing_created": False,
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
            "pages_010_020_processing": False,
        },
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 009 Crop Contract Packet - P009TR-G1-VIRAL-003",
            "",
            "Status: `page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked`",
            "",
            "Purpose: review whether page 009 now has a role-separated crop contract suitable as the bounded input contract for a later PCRP authorization.",
            "",
            "Boundary: this packet creates no OCR run, no OCR output/evidence, no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no render/PDF/raw mutation, and no pages 010-020 processing.",
            "",
            "## Observed Page 009",
            "",
            "- Page type: two-profile visual/text composition.",
            "- Existing evidence: rendered page image plus provisional region-map/page-map/page-inventory hints.",
            "- Current result: page 009 crop-role contract ready for human review, not accepted.",
            "- Supersedes: `P009TR-G1-VIRAL-002` for PCRP routing only; `_002` remains historical/readability-only evidence.",
            "- Right lower grey block: complete/non-blocker.",
            "",
            "## Review Blocks",
            "",
            "- `P009-B001`: left portrait/image area, `source_region_box_px` plus `human_review_crop_box_px` only.",
            "- `P009-B002`: right portrait/image area, `source_region_box_px` plus `human_review_crop_box_px` only.",
            "- `P009-B003`: left profile text block with `source_region_box_px`, `human_review_crop_box_px`, `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.",
            "- `P009-B004`: right profile text block with `source_region_box_px`, `human_review_crop_box_px`, `ocr_candidate_crop_box_px`, and `text_evidence_crop_box_px`.",
            "",
            "## Routing Recommendation",
            "",
            "- Previous `_002` route recommendation is superseded for PCRP purposes.",
            "- Recommended next candidate: Bogdan review of `P009TR-G1-VIRAL-003`; only after that may a separate PCRP authorization be created.",
            "- OCR benchmark remediation remains a separate later branch; no OCR is executed here.",
            "",
            "Decision after review: `p009 crop contract ok` or `hold p009 crop contract: <reason>`.",
            "",
        ]
    )


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PAGE_IMAGE, ASSET_ROOT / "page_009.png")
    image = Image.open(PAGE_IMAGE)
    image_assets: dict[str, dict[str, str]] = {}
    for block in REVIEW_BLOCKS:
        for box_key, asset_key in (
            ("human_review_crop_box_px", "human_review_asset"),
            ("ocr_candidate_crop_box_px", "ocr_candidate_asset"),
            ("text_evidence_crop_box_px", "text_evidence_asset"),
        ):
            if box_key not in block:
                continue
            image_assets[block[asset_key]] = crop_asset(image, block, box_key, asset_key)
    packet = build_packet(predecessors, image_assets)

    packet_path = OUTPUT_ROOT / "page_009_triage_packet.json"
    summary_path = OUTPUT_ROOT / "page_009_triage_summary.md"
    report_path = OUTPUT_ROOT / "page_009_triage_report.json"
    manifest_path = OUTPUT_ROOT / "page_009_triage_manifest.md"
    write_json(packet_path, packet)
    summary_path.write_text(build_summary(packet), encoding="utf-8", newline="\n")
    write_json(
        report_path,
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
        "# Page 009 Crop Contract Manifest - P009TR-G1-VIRAL-003",
        "",
        "Status: `page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked`",
        "",
        "Boundary: no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no OCR/render/PDF/raw mutation, no pages 010-020 processing.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_009_triage_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    manifest_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    check_authorization()
    write_outputs()
