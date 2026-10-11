from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_001_triage.py"
TEST_PATH = ROOT / "tests" / "test_page_001_triage.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUTPUT_ROOT = TRIAL_ROOT / "page_001_triage_G1_VIRAL_001"
ASSET_ROOT = OUTPUT_ROOT / "review_assets"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-001-TRIAGE-001"
PACKAGE_ID = "P001TR-G1-VIRAL-001"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_001.png"

PAGE_IMAGE_SHA256 = "672801EA676F0E8D7A4CAD7E960249BF6F5B049E2BF45533AAA02A87E537B692"
G1SP_002_PACKET_SHA256 = "9EC5331E2E67CA2F8103559B5D0EDBC51E86C80E5F36A075863861889AA8AAD3"
G1SP_002_REPORT_SHA256 = "226E57ED1C9288897054FD546BD79D646284A887922E3287383844F4B96FC076"
PGCT_REPORT_SHA256 = "EFDEBCC6ABBE916086887572D400DA9AAF41257F910D55AAF4D337BE386F550F"
PRM_REPORT_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"
PMR_REPORT_SHA256 = "72F9DA627C91E97CFDF68ED18D2472EE2978F97CF93383F25C1ED2BED2FE215F"
PIR_REPORT_SHA256 = "2F26E24D558B31384EDCFA022FFA5B72B48D11E7DA876AEED7CE9E26CE6E98BA"

PREDECESSORS = {
    "post_p008_gate_1_status_route_packet": {
        "path": TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_002" / "gate_1_status_packet.json",
        "sha256": G1SP_002_PACKET_SHA256,
    },
    "post_p008_gate_1_status_route_report": {
        "path": TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_002" / "gate_1_status_report.json",
        "sha256": G1SP_002_REPORT_SHA256,
    },
    "page_completeness_triage_report": {
        "path": TRIAL_ROOT / "page_completeness_triage_G1_VIRAL_001" / "page_completeness_triage_report.json",
        "sha256": PGCT_REPORT_SHA256,
    },
    "provisional_region_map_report": {
        "path": TRIAL_ROOT / "provisional_region_map_report.md",
        "sha256": PRM_REPORT_SHA256,
    },
    "page_map_model_report": {
        "path": TRIAL_ROOT / "page_map_model_report.md",
        "sha256": PMR_REPORT_SHA256,
    },
    "page_inventory_report": {
        "path": TRIAL_ROOT / "page_inventory_report.md",
        "sha256": PIR_REPORT_SHA256,
    },
    "page_001_image": {
        "path": PAGE_IMAGE,
        "sha256": PAGE_IMAGE_SHA256,
    },
}

REVIEW_BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P001-B001",
        "role": "cover_full_page_visual_anchor",
        "content_kind": "visual_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P001-R01",
        "box_px": [0, 0, 2550, 3300],
        "review_asset": "review_assets/1_P001-full-page-cover-anchor.png",
        "routing": "defer_visual_composition_to_page_complete_review",
        "not_source_text": True,
    },
    {
        "block_id": "P001-B002",
        "role": "cover_title_logo_area",
        "content_kind": "title_visual_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P001-R02",
        "source_region_box_px": [760, 260, 1050, 760],
        "review_crop_box_px": [500, 80, 1550, 1030],
        "review_asset": "review_assets/2_P001-title-logo-area.png",
        "routing": "needs_human_visual_title_routing_decision",
        "visible_text_hint": "VIRAL / UNREDACTED",
        "not_ocr_verified_text": True,
    },
    {
        "block_id": "P001-B003",
        "role": "cover_footer_rating_tagline_logos",
        "content_kind": "mixed_footer_visual_anchor",
        "source_region_id": "PRM-G1-VIRAL-001-P001-R03",
        "source_region_box_px": [380, 2750, 1750, 360],
        "review_crop_box_px": [40, 2740, 2460, 520],
        "review_asset": "review_assets/3_P001-footer-title-credit-like-block.png",
        "routing": "needs_human_footer_visual_routing_decision",
        "visible_text_hint": "rating badge, modern Call of Cthulhu scenario tagline, repository logo area",
        "not_ocr_verified_text": True,
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
    parser = argparse.ArgumentParser(description="Build page 001 triage/readiness routing packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 001 triage is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 001 triage requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    verified = []
    for name, item in PREDECESSORS.items():
        path = item["path"]
        expected = item["sha256"]
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": path.relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def crop_asset(image: Image.Image, block: dict[str, Any]) -> dict[str, str]:
    crop_box = block["review_crop_box_px"] if "review_crop_box_px" in block else block["box_px"]
    x, y, width, height = crop_box
    crop = image.crop((x, y, x + width, y + height))
    target = OUTPUT_ROOT / block["review_asset"]
    target.parent.mkdir(parents=True, exist_ok=True)
    crop.save(target)
    return {
        "path": target.relative_to(ROOT).as_posix(),
        "sha256": sha256_file(target),
    }


def build_packet(predecessors: list[dict[str, str]], assets: list[dict[str, str]]) -> dict[str, Any]:
    blocks = []
    for block, asset in zip(REVIEW_BLOCKS, assets, strict=True):
        item = dict(block)
        item["review_asset_sha256"] = asset["sha256"]
        blocks.append(item)

    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_001_triage_ready_for_bogdan_routing_decision",
        "scope": "page_001_triage_only_no_acceptance",
        "predecessors": predecessors,
        "page": "001",
        "page_identity": {
            "page_id": "PG-G1-VIRAL-P001",
            "image_id": "IMG-G1-VIRAL-RENDER-001-P001",
            "image_sha256": PAGE_IMAGE_SHA256,
            "plain_label": "cover/title composition",
        },
        "triage_result": {
            "page_001_incomplete_blocker_addressed_by_this_packet": "routed_for_human_decision_not_accepted",
            "recommended_next_candidate": "page_001_visual_title_page_complete_review_without_ocr",
            "requires_new_ocr": False,
            "requires_new_render": False,
            "requires_pdf_or_raw_mutation": False,
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
        },
        "review_blocks": blocks,
        "decision_options": [
            "page_001_route_ok_visual_title_review",
            "hold_page_001_triage: <reason>",
        ],
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
            "page_009_plus_processing": False,
        },
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 001 Triage Packet - P001TR-G1-VIRAL-001",
            "",
            "Status: `page_001_triage_ready_for_bogdan_routing_decision`",
            "",
            "Purpose: decide whether page 001 can proceed to a visual/title page-complete review without OCR/remediation.",
            "",
            "Boundary: this packet creates no page-complete acceptance, no whole Gate 1 acceptance, no OCR/render/PDF/raw mutation, and no page 009+ processing.",
            "",
            "## Observed Page 001",
            "",
            "- Page type: cover/title composition.",
            "- Existing evidence: rendered page image plus provisional region-map/page-map/page-inventory hints.",
            "- Prior status: incomplete in `PGCT-G1-VIRAL-001`.",
            "- Current result: routed for human decision, not accepted.",
            "",
            "## Review Blocks",
            "",
            "- `P001-B001`: full-page cover visual anchor.",
            "- `P001-B002`: title/logo area, visible text hint `VIRAL / UNREDACTED`.",
            "- `P001-B003`: footer/rating/tagline/logo mixed visual area.",
            "",
            "## Routing Recommendation",
            "",
            "- Recommended next candidate: `page_001_visual_title_page_complete_review_without_ocr`.",
            "- OCR benchmark remediation remains a separate later branch.",
            "",
            "Decision after review: `page 001 route ok` or `hold page 001 triage: <reason>`.",
            "",
        ]
    )


def build_report(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": packet["status"],
        "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
        "generator_script_sha256": sha256_file(SCRIPT_PATH),
        "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
        "test_contract_sha256": sha256_file(TEST_PATH),
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
    }


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    ASSET_ROOT.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PAGE_IMAGE, ASSET_ROOT / "page_001.png")
    image = Image.open(PAGE_IMAGE)
    assets = [crop_asset(image, block) for block in REVIEW_BLOCKS]
    packet = build_packet(predecessors, assets)
    summary = build_summary(packet)
    report = build_report(packet)

    packet_path = OUTPUT_ROOT / "page_001_triage_packet.json"
    summary_path = OUTPUT_ROOT / "page_001_triage_summary.md"
    report_path = OUTPUT_ROOT / "page_001_triage_report.json"
    manifest_path = OUTPUT_ROOT / "page_001_triage_manifest.md"

    write_json(packet_path, packet)
    summary_path.write_text(summary, encoding="utf-8", newline="\n")
    write_json(report_path, report)

    manifest = "\n".join(
        [
            "# Page 001 Triage Manifest - P001TR-G1-VIRAL-001",
            "",
            "Status: `page_001_triage_ready_for_bogdan_routing_decision`",
            "",
            "Boundary: no page-complete acceptance, no whole Gate 1 acceptance, no OCR/render/PDF/raw mutation, no page 009+ processing.",
            "",
            "## Output Hashes",
            "",
            "| Output | SHA-256 |",
            "|---|---|",
            f"| `page_001_triage_packet.json` | `{sha256_file(packet_path)}` |",
            f"| `page_001_triage_report.json` | `{sha256_file(report_path)}` |",
            f"| `page_001_triage_summary.md` | `{sha256_file(summary_path)}` |",
            "",
        ]
    )
    manifest_path.write_text(manifest, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> None:
    check_authorization(argv)
    write_outputs()


if __name__ == "__main__":
    main()
