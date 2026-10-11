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
SCRIPT_PATH = ROOT / "scripts" / "build_page_010_triage.py"
TEST_PATH = ROOT / "tests" / "test_page_010_triage.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUTPUT_ROOT = TRIAL_ROOT / "page_010_triage_G1_VIRAL_001"
ASSET_ROOT = OUTPUT_ROOT / "review_assets"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-010-TRIAGE-001"
PACKAGE_ID = "P010TR-G1-VIRAL-001"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_010.png"

PAGE_IMAGE_SHA256 = "A7A30C4F60CE2CEB91F3939C4DBF1393AA0452EC290D5F927AE10F77CEE988D7"
G1SP_004_PACKET_SHA256 = "970AEEF0161A081AB3535057F311B0CA17F8F5AD56F3F35EA3E7350657E26761"
PRM_REPORT_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
PMR_REPORT_SHA256 = "72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F"
PIR_REPORT_SHA256 = "2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA"
CONTENT_MAP_SHA256 = "335699DB7AE60E87390D88D7A26AA22BA297F50F90B7868F7ED869C2F5AABE79"
ART_MAP_SHA256 = "77BD88C0522E17DF98603364677BC248450EC3E57996389881629E581197C544"

REVIEW_BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P010-B001",
        "role": "upper_left_continuation_gear_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R01",
        "source_region_box_px": [230, 220, 910, 460],
        "human_review_crop_box_px": [180, 170, 1080, 500],
        "ocr_candidate_crop_box_px": [180, 170, 1080, 500],
        "text_evidence_crop_box_px": [180, 170, 1080, 500],
        "human_review_asset": "review_assets/1_P010-upper-left-continuation-gear-human-context.png",
        "ocr_candidate_asset": "review_assets/1a_P010-upper-left-continuation-gear-ocr-candidate.png",
        "text_evidence_asset": "review_assets/1b_P010-upper-left-continuation-gear-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_text_extraction_after_human_review",
        "not_ocr_verified_text": True,
    },
    {
        "block_id": "P010-B002",
        "role": "upper_right_continuation_appearance_gear_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R02",
        "source_region_box_px": [1380, 220, 930, 460],
        "human_review_crop_box_px": [1280, 170, 1070, 875],
        "ocr_candidate_crop_box_px": [1280, 170, 1070, 875],
        "text_evidence_crop_box_px": [1280, 170, 1070, 875],
        "human_review_asset": "review_assets/2_P010-upper-right-continuation-appearance-gear-human-context.png",
        "ocr_candidate_asset": "review_assets/2a_P010-upper-right-continuation-appearance-gear-ocr-candidate.png",
        "text_evidence_asset": "review_assets/2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_text_extraction_after_human_review",
        "not_ocr_verified_text": True,
    },
    {
        "block_id": "P010-B003",
        "role": "left_hyeon_portrait_image_area",
        "content_kind": "art_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R03",
        "source_region_box_px": [230, 700, 920, 1450],
        "visual_pollution_guard_box_px": [160, 720, 1060, 1260],
        "human_review_crop_box_px": [160, 650, 1060, 1460],
        "human_review_asset": "review_assets/3_P010-left-hyeon-portrait-image-area-human-context.png",
        "routing": "defer_visual_anchor_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P010-B004",
        "role": "right_maya_portrait_image_area",
        "content_kind": "art_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R04",
        "source_region_box_px": [1390, 700, 920, 1450],
        "visual_pollution_guard_box_px": [1310, 1120, 1040, 1220],
        "human_review_crop_box_px": [1310, 650, 1040, 1460],
        "human_review_asset": "review_assets/4_P010-right-maya-portrait-image-area-human-context.png",
        "routing": "defer_visual_anchor_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P010-B005",
        "role": "lower_left_hyeon_profile_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R05",
        "source_region_split": "left_derived_from_R05",
        "source_region_box_px": [230, 2180, 2080, 650],
        "human_review_crop_box_px": [180, 2020, 1080, 1040],
        "ocr_candidate_crop_box_px": [180, 2020, 1080, 1040],
        "text_evidence_crop_box_px": [180, 2020, 1080, 1040],
        "human_review_asset": "review_assets/5_P010-lower-left-hyeon-profile-human-context.png",
        "ocr_candidate_asset": "review_assets/5a_P010-lower-left-hyeon-profile-ocr-candidate.png",
        "text_evidence_asset": "review_assets/5b_P010-lower-left-hyeon-profile-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_text_extraction_after_human_review",
        "not_ocr_verified_text": True,
        "lower_region_disposition": "left_text_block_derived_from_single_prm_region_R05_no_shared_lower_human_crop",
    },
    {
        "block_id": "P010-B006",
        "role": "lower_right_maya_profile_text_like_block",
        "content_kind": "text_like_region",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R05",
        "source_region_split": "right_derived_from_R05",
        "source_region_box_px": [230, 2180, 2080, 650],
        "human_review_crop_box_px": [1260, 2360, 1110, 740],
        "ocr_candidate_crop_box_px": [1260, 2360, 1110, 740],
        "text_evidence_crop_box_px": [1260, 2360, 1110, 740],
        "human_review_asset": "review_assets/6_P010-lower-right-maya-profile-human-context.png",
        "ocr_candidate_asset": "review_assets/6a_P010-lower-right-maya-profile-ocr-candidate.png",
        "text_evidence_asset": "review_assets/6b_P010-lower-right-maya-profile-text-evidence.png",
        "routing": "crop_contract_candidate_for_later_text_extraction_after_human_review",
        "not_ocr_verified_text": True,
        "lower_region_disposition": "right_text_block_derived_from_single_prm_region_R05_no_shared_lower_human_crop",
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
    parser = argparse.ArgumentParser(description="Build page 010 triage/readiness crop-contract packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 010 triage is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 010 triage requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "post_p009_gate_1_status_route_packet": {
            "path": TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_004" / "gate_1_status_packet.json",
            "sha256": G1SP_004_PACKET_SHA256,
        },
        "provisional_region_map_report": {"path": TRIAL_ROOT / "provisional_region_map_report.md", "sha256": PRM_REPORT_SHA256},
        "page_map_model_report": {"path": TRIAL_ROOT / "page_map_model_report.md", "sha256": PMR_REPORT_SHA256},
        "page_inventory_report": {"path": TRIAL_ROOT / "page_inventory_report.md", "sha256": PIR_REPORT_SHA256},
        "content_map_trial_report": {"path": TRIAL_ROOT / "content_map_trial_report.md", "sha256": CONTENT_MAP_SHA256},
        "art_map_trial_report": {"path": TRIAL_ROOT / "art_map_trial_report.md", "sha256": ART_MAP_SHA256},
        "page_010_image": {"path": PAGE_IMAGE, "sha256": PAGE_IMAGE_SHA256},
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        expected = item["sha256"]
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
            black_text = r < 120 and g < 120 and b < 120
            red_text = r > 120 and g < 100 and b < 100
            green_text = r > 110 and g > 140 and b < 150
            return black_text or red_text or green_text

        bands = {
            "left": [(x, y) for x in range(margin) for y in range(height)],
            "right": [(x, y) for x in range(width - margin, width) for y in range(height)],
            "top": [(x, y) for x in range(width) for y in range(margin)],
            "bottom": [(x, y) for x in range(width) for y in range(height - margin, height)],
        }
        return {edge: round(sum(1 for x, y in coords if is_ink(x, y)) / len(coords), 4) for edge, coords in bands.items()}


def build_crop_qa(blocks: list[dict[str, Any]], image_assets: dict[str, dict[str, str]]) -> dict[str, Any]:
    return validate_crop_role_contract(
        blocks=blocks,
        output_root=OUTPUT_ROOT,
        image_assets=image_assets,
        max_edge_ink_ratio=0.15,
        extra_fields={
            "layout_disposition": {
                "page_type": "dual_profile_mixed_page",
                "art_count": 2,
                "lower_prm_region_split_for_ocr": True,
                "shared_lower_human_review_crop_allowed": False,
            },
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
        "status": "page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp",
        "scope": "page_010_triage_and_crop_role_contract_only_no_text_extraction_no_pcrp_no_acceptance",
        "predecessors": predecessors,
        "page": "010",
        "page_identity": {
            "page_id": "PG-G1-VIRAL-P010",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P010",
            "image_sha256": PAGE_IMAGE_SHA256,
            "plain_label": "dual_profile_mixed_page",
        },
        "triage_result": {
            "current_cursor": "page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp",
            "recommended_next_candidate": "bogdan_review_of_p010tr_001_before_any_text_extraction_or_pcrp_authorization",
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
            {"layer": "G1SP-004", "sol": "OK pages 001-009 are bound as accepted-only predecessors and route now points to P010", "terra": "OK status-only packet creates no P010 authority or Gate acceptance"},
            {"layer": "P010TR-001", "sol": "OK P010 PRM/page/content/art-map inputs reconcile to three text-like regions and two art anchors", "terra": "OK no OCR/text output/PCRP/page acceptance is created"},
            {"layer": "P010TR-001-crops", "sol": "OK lower R05 is represented as two peer column text blocks with separate human/OCR/text crops", "terra": "OK there is no shared lower human crop and art regions are excluded from OCR surfaces"},
        ],
        "decision_options": ["p010 triage ok", "hold p010 triage: <reason>"],
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
            "pages_011_020_processing_created": False,
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
            "pages_011_020_processing": False,
        },
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 010 Triage Crop Contract Packet - P010TR-G1-VIRAL-001",
            "",
            "Status: `page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp`",
            "",
            "Purpose: review whether page 010 has a clean role-separated triage/crop contract before any text extraction, semantic map, PCRP, or page-complete acceptance.",
            "",
            "Boundary: this packet creates no OCR run, no OCR output/evidence, no text extraction, no semantic map, no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no render/PDF/raw mutation, and no pages 011-020 processing.",
            "",
            "## Observed Page 010",
            "",
            "- Page type: dual-profile mixed page with continuation/gear text, two portraits, and lower profile text.",
            "- Source map: `PRM-G1-VIRAL-001-P010-R01`..`R05`.",
            "- Text-like source regions: `R01`, `R02`, `R05`.",
            "- Art anchors: `R03`, `R04`.",
            "- Lower `R05` is one PRM region but is represented as two independent lower text blocks by visible column.",
            "- No shared lower human review crop is allowed in this packet.",
            "",
            "## Review Blocks",
            "",
            "- `P010-B001`: upper-left continuation/gear text with source, human, OCR-candidate, and text-evidence boxes.",
            "- `P010-B002`: upper-right continuation/appearance/gear text with source, human, OCR-candidate, and text-evidence boxes.",
            "- `P010-B003`: left Hyeon portrait/image area, human context only.",
            "- `P010-B004`: right Maya portrait/image area, human context only.",
            "- `P010-B005`: lower-left Hyeon profile text with source lineage, human, OCR-candidate, and text-evidence boxes.",
            "- `P010-B006`: lower-right Maya profile text with source lineage, human, OCR-candidate, and text-evidence boxes.",
            "",
            "## Routing Recommendation",
            "",
            "- Recommended next candidate: Bogdan review of `P010TR-G1-VIRAL-001`.",
            "- If accepted, the next separate bounded layer should be page 010 text extraction from the text evidence crops.",
            "",
            "Decision after review: `p010 triage ok` or `hold p010 triage: <reason>`.",
            "",
        ]
    )


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PAGE_IMAGE, ASSET_ROOT / "page_010.png")
    image_assets: dict[str, dict[str, str]] = {
        "review_assets/page_010.png": {"path": (ASSET_ROOT / "page_010.png").relative_to(ROOT).as_posix(), "sha256": sha256_file(ASSET_ROOT / "page_010.png")}
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

    write_json(OUTPUT_ROOT / "page_010_triage_packet.json", packet)
    (OUTPUT_ROOT / "page_010_triage_summary.md").write_text(build_summary(packet), encoding="utf-8", newline="\n")
    write_json(
        OUTPUT_ROOT / "page_010_triage_report.json",
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
        "# Page 010 Triage Crop Contract Manifest - P010TR-G1-VIRAL-001",
        "",
        "Status: `page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp`",
        "",
        "Boundary: no text extraction, no semantic map, no PCRP, no page-complete acceptance, no whole Gate 1 acceptance, no OCR/render/PDF/raw mutation, no pages 011-020 processing.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_010_triage_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    (OUTPUT_ROOT / "page_010_triage_manifest.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    check_authorization()
    write_outputs()
