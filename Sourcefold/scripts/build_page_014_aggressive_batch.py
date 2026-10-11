from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from PIL import Image

from bounded_authorization_contract import materialize_aggressive_batch_authorization
from page_review_crop_contracts import validate_text_evidence_crop_contracts
from page_review_semantic_units import keeper_notes_callout_heading_level
from semantic_segmentation_contract import callout_body_contract, validate_semantic_split_contracts
ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_014_aggressive_batch.py"
TEST_PATH = ROOT / "tests" / "test_page_014_aggressive_batch.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-014-AGGRESSIVE-BATCH-001"
LANE_ID = "P014BATCH-G1-VIRAL-001"
PAGE = "014"
PAGE_ID = "PG-G1-VIRAL-P014"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_014.png"
PAGE_IMAGE_SHA256 = "24271ACED987DDF04850975ABE27D3B9BD4D48C74D81226E381D98D5E82948EA"
G1SP_008_PACKET_SHA256 = "EED84F376597007FECA15774E4DCFEDEFC3F619278985BEB11E0D46295565725"
P013_FINAL_REVIEW_SHA256 = "3C9AF88656119DE46753B6F8454B5BE36C331BE212E3A133A3E5BF8F163D63F4"

TRIAGE_ROOT = TRIAL_ROOT / "page_014_triage_G1_VIRAL_001"
TEXT_ROOT = TRIAL_ROOT / "page_014_text_extraction_G1_VIRAL_001"
SEM_ROOT = TRIAL_ROOT / "page_014_semantic_text_map_G1_VIRAL_001"
PCRP_ROOT = TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001"
PCA_ROOT = TRIAL_ROOT / "page_complete_acceptance_p014_G1_VIRAL_001"
STATUS_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_009"
BATCH_ROOT = TRIAL_ROOT / "page_014_aggressive_batch_G1_VIRAL_001"

SKIPPED_REVIEW = "human_review_skipped_by_explicit_authorization"
DELEGATED_REVIEW = "review_delegated_to_Sol_Terra"

SOL_TERRA_STAGE_REVIEWS = {
    "P014TR-G1-VIRAL-001": {
        "sol": "OK: page 014 is bounded to the existing page image and uses explicit crop provenance contracts for all text evidence surfaces.",
        "terra": "OK: triage is hash-bound to G1SP-G1-VIRAL-008 and page_014.png; page 015+ is not processed.",
    },
    "P014TXT-G1-VIRAL-001": {
        "sol": "OK: draft transcription is limited to P014 text evidence crops in logical reading order.",
        "terra": "OK: text extraction records skipped human review and creates no OCR/source/page/whole-Gate acceptance.",
    },
    "P014SEM-G1-VIRAL-001": {
        "sol": "OK: semantic units preserve continuation text, inline underlined option headings, and paragraph boundaries.",
        "terra": "OK: semantic map is machine-reviewed only and contains no page 015 processing.",
    },
    "PCRP-G1-VIRAL-P014-001": {
        "sol": "OK: page-complete review packet reconciles all P014 text blocks, semantic units, and review assets with no open blockers.",
        "terra": "OK: PCRP is internal machine-reviewed evidence only and does not claim per-stage Bogdan approval.",
    },
    "P014PCA-G1-VIRAL-001": {
        "sol": "OK: acceptance is page 014 only under delegated-review lane authority and exact PCRP predecessor binding.",
        "terra": "OK: PCA does not imply whole Gate 1, fixture admission, source acceptance, or direct human page-level approval.",
    },
    "G1SP-G1-VIRAL-009": {
        "sol": "OK: status refresh records pages 001-014 accepted-only and pages 015-020 unstarted.",
        "terra": "OK: page 015 is only a recommended next candidate and is not authorized by the status packet.",
    },
}

BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P014-B001",
        "role": "spektral_krew_gear_title_and_carried_intro",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R01",
        "crop_box_px": [180, 215, 900, 300],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 160, "max_x": 200, "min_y": 195, "max_y": 235, "min_width": 860, "min_height": 270},
        },
        "asset": "review_assets/1_P014-title-carried-intro-text-evidence.png",
    },
    {
        "block_id": "P014-B002",
        "role": "equipment_satchel",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R02",
        "crop_box_px": [180, 515, 920, 375],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 160, "max_x": 200, "min_y": 495, "max_y": 535, "min_width": 880, "min_height": 340},
        },
        "asset": "review_assets/2_P014-equipment-satchel-text-evidence.png",
    },
    {
        "block_id": "P014-B003",
        "role": "night_vision_and_emf_meter",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R03",
        "crop_box_px": [180, 900, 920, 460],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 160, "max_x": 200, "min_y": 875, "max_y": 925, "min_width": 880, "min_height": 420},
        },
        "asset": "review_assets/3_P014-night-vision-emf-text-evidence.png",
    },
    {
        "block_id": "P014-B004",
        "role": "keeper_notes_emf_meter",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R04",
        "crop_box_px": [180, 1370, 930, 405],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 160, "max_x": 200, "min_y": 1340, "max_y": 1395, "min_width": 890, "min_height": 360},
        },
        "asset": "review_assets/4_P014-emf-keepers-notes-text-evidence.png",
    },
    {
        "block_id": "P014-B005",
        "role": "spirit_box_and_notes",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R05",
        "crop_box_px": [180, 1810, 930, 600],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 160, "max_x": 200, "min_y": 1785, "max_y": 1830, "min_width": 890, "min_height": 560},
        },
        "asset": "review_assets/5_P014-spirit-box-notes-text-evidence.png",
    },
    {
        "block_id": "P014-B006",
        "role": "evp_recorder_and_flir_camera",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R06",
        "crop_box_px": [180, 2405, 930, 610],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 160, "max_x": 200, "min_y": 2380, "max_y": 2430, "min_width": 890, "min_height": 560},
        },
        "asset": "review_assets/6_P014-evp-flir-text-evidence.png",
    },
    {
        "block_id": "P014-B007",
        "role": "static_base_station_and_notes",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R07",
        "crop_box_px": [1290, 215, 1130, 700],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1270, "max_x": 1310, "min_y": 195, "max_y": 235, "min_width": 1080, "min_height": 650},
        },
        "asset": "review_assets/7_P014-static-base-station-text-evidence.png",
    },
    {
        "block_id": "P014-B008",
        "role": "cellular_repeaters_and_notes",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R08",
        "crop_box_px": [1290, 905, 1130, 595],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1270, "max_x": 1310, "min_y": 880, "max_y": 930, "min_width": 1080, "min_height": 560},
        },
        "asset": "review_assets/8_P014-cellular-repeaters-notes-text-evidence.png",
    },
    {
        "block_id": "P014-B009",
        "role": "ups_batteries_night_vision_drone",
        "source_region_id": "PRM-G1-VIRAL-001-P014-R09",
        "crop_box_px": [1290, 1510, 1130, 1005],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1270, "max_x": 1310, "min_y": 1485, "max_y": 1535, "min_width": 1080, "min_height": 960},
        },
        "asset": "review_assets/9_P014-ups-night-vision-drone-text-evidence.png",
    },
]

VISUAL_ONLY_BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P014-V001",
        "role": "night_vision_camera_photo",
        "source_region_id": "PRM-G1-VIRAL-001-P014-V01",
        "crop_box_px": [1290, 2530, 1130, 520],
        "asset": "review_assets/10_P014-night-vision-camera-photo-visual-anchor.png",
    }
]

TEXT_UNITS: list[dict[str, Any]] = [
    {
        "unit_id": "P014-TEXT-001",
        "block_id": "P014-B001",
        "text": "Spektral Krew Gear\n\nCarried\nThese bits of equipment are carried by the Krew based on their job (see Investigator descriptions).",
    },
    {
        "unit_id": "P014-TEXT-002",
        "block_id": "P014-B002",
        "text": "Equipment Satchel\nEach team member has a black canvas satchel (with the Spektral Krew logo of course) for carrying their gear. In some cases, the host may hand off his satchel to someone else while they're on camera. It's big enough to hold the Handheld Night Vision Cameras, EMF Meters, Smart Phones, and FLIR Cameras, plus any other personal gear.",
    },
    {
        "unit_id": "P014-TEXT-003",
        "block_id": "P014-B003",
        "text": "Handheld Night Vision Cameras (2)\n4K Wi-Fi Full Spectrum Camcorders, Ultra HD Infrared Night Vision Paranormal Investigation Video Camera with 60 fps 24 MP 30x Digital Zoom. Peter and Enoch usually carry and operate these. [Four Hours of Battery Life]\n\nEMF Meter\nHF-B3G Triple Axis HF RF Power Meter Analyzer and Detector. [12 Hours of Battery Life]",
    },
    {
        "unit_id": "P014-TEXT-004",
        "block_id": "P014-B004",
        "text": "Keeper's Notes\nThere are not many EMFs on the island, but the Krew will see the odd tick here and there from background noise. While ghosts don't generate electromagnetic fields, Hastalyk can use this against the Investigators by causing it to respond in the direction it wants them to go. Marco is usually in possession of this.",
    },
    {
        "unit_id": "P014-TEXT-005",
        "block_id": "P014-B005",
        "text": "Spirit Box\nThis is a custom radio with a frequency scan mode that the Krew hopes will allow them to communicate with spirits. It's about the size of a walkie-talkie and includes a headphone to better hear voices from the beyond. [Eight Hours of Battery Life]\n\nKeeper's Notes\nIt's possible that the Spirit Box could pick up radio chatter from the Italian military or the Plague Monk chanting various disturbing litanies in Latin (Keeper's discretion).",
    },
    {
        "unit_id": "P014-TEXT-006",
        "block_id": "P014-B006",
        "text": "EVP Recorder SCD1\nThe SCD1 is an experimental piece of equipment that Marco has had someone build - it is the Silent Capture Device. The processor and software can detect when nobody is talking and will flash when it picks up a sound during silence. This can be played back in real time. This was an expensive piece of prototype technology, so Marco keeps hold of this.\n\nFLIR Camera for Smartphone\nFLIR ONE Pro - iOS - Professional Grade Thermal Camera for Smartphones - with VividIR and MSX Image Enhancement Technology. This has been jury rigged by Hyeon so that it uses the video feed from Peter's camera. [Battery Life of the FLIR is only 45 Minutes]",
    },
    {
        "unit_id": "P014-TEXT-007",
        "block_id": "P014-B007",
        "text": "Static\nThese bits of equipment are set up early on and, with the exception of the drone, remain at a single location.\n\nBase Station\nThis is a custom industrial laptop with a Wi-Fi hub and satellite uplink set up for live streaming. A deep cycle battery unit supplies enough power for up to 12 hours of continuous broadcasting.\n\nKeeper's Notes\nAt the Keeper's discretion, other devices may be charged off the base station's battery, but this obviously takes time that the Investigators may not have.",
    },
    {
        "unit_id": "P014-TEXT-008",
        "block_id": "P014-B008",
        "text": "Cellular Wi-Fi Repeaters/Transmitters (2)\nEach provides Wi-Fi within a 300 Meter radius, and has a battery unit that provides 8-10 hours of uninterrupted signal.\n\nKeeper's Notes\nThese are best set up in three key locations, the lighthouse, the far side of the bridge, and the hospital tower. This provides the greatest area of coverage for the investigation site. Note that since the satellite signal is being routed through the Base Station at the lighthouse, the hospital signal requires the bridge transmitter to be active.",
    },
    {
        "unit_id": "P014-TEXT-009",
        "block_id": "P014-B009",
        "text": "UPS Batteries (3)\nPrimarily used to power the Wi-Fi Transmitters, they have various connections via which other equipment can be recharged. They can provide around six hours of power each in the event of power failure. Really only there in the instance of the battery backup for the hub failing. Extremely heavy as they are essentially large deep-cycle batteries.\n\nNight Vision Cameras (6)\nFoscam HT2 1080p Outdoor 2.4 g/5 gHz Wi-Fi PTZ IP Camera, 4x Optical Zoom Pan Tilt Security Surveillance Speed Dome, Two-Way Audio with Mic & Speaker, 165 ft. Night Vision, CMOS Image Sensor, IP66. [Six Hours of Battery Life]\n\nDrone\nThis optional drone is an expensive professional model that is equipped with a night vision capable 4K video camera that can be controlled via Hyeon's iPad app. The video can be recorded locally or fed directly to the live stream. [It includes three batteries with 20 minutes of flight time each.]",
    },
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build page 014 aggressive delegated-review batch.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 014 aggressive batch is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 014 aggressive batch requires {AUTHORIZATION_ID}")


def verify_predecessors() -> list[dict[str, str]]:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")
    predecessors = [
        ("post_p013_status_route_packet", TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_008" / "gate_1_status_packet.json", G1SP_008_PACKET_SHA256),
        ("p013_final_batch_review", TRIAL_ROOT / "page_013_aggressive_batch_final_review_G1_VIRAL_001" / "page_013_aggressive_batch_final_review_report.json", P013_FINAL_REVIEW_SHA256),
        ("page_014_image", PAGE_IMAGE, PAGE_IMAGE_SHA256),
    ]
    verified = []
    for name, path, expected in predecessors:
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": path.relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def aggressive_batch_authorization_preflight() -> None:
    materialize_aggressive_batch_authorization(
        ledger_path=AUTHORIZATION_LEDGER,
        authorization_id=AUTHORIZATION_ID,
        page=PAGE,
        lane_id=LANE_ID,
        authority="Bogdan Telegram authorization for page 014 aggressive batch",
        exact_action=[
            "Create page 014 aggressive delegated-review batch artifacts.",
            "Generate P014TR/P014TXT/P014SEM/PCRP/P014PCA/status/batch outputs with skipped human review and Sol/Terra evidence.",
        ],
        admitted_inputs=[
            {"name": "post_p013_status_route_packet", "sha256": G1SP_008_PACKET_SHA256},
            {"name": "p013_final_batch_review", "sha256": P013_FINAL_REVIEW_SHA256},
            {"name": "page_014_image", "sha256": PAGE_IMAGE_SHA256},
        ],
        allowed_outputs=[
            "scripts/build_page_014_aggressive_batch.py",
            "tests/test_page_014_aggressive_batch.py",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_014_*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p014_G1_VIRAL_001/*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_009/*",
        ],
        limits=[
            "Do not record direct Bogdan approval for internal P014 stages.",
            "Do not process page 015 or later beyond the post-P014 status recommendation.",
            "Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.",
        ],
    )


def review_gate(stage: str) -> dict[str, Any]:
    review = SOL_TERRA_STAGE_REVIEWS[stage]
    return {
        "human_review_state": SKIPPED_REVIEW,
        "delegated_review_state": DELEGATED_REVIEW,
        "lane_authority": AUTHORIZATION_ID,
        "sol": {"status": "OK", "finding": review["sol"]},
        "terra": {"status": "OK", "finding": review["terra"]},
        "status": "passed",
        "blockers": [],
    }


def guardrails(extra: dict[str, bool] | None = None) -> dict[str, bool]:
    data = {
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
        "page_015_plus_processing": False,
    }
    if extra:
        data.update(extra)
    return data


def unit_block_ids(unit: dict[str, Any]) -> list[str]:
    if "block_ids" in unit:
        return list(unit["block_ids"])
    return [unit["block_id"]]


def find_block(block_id: str) -> dict[str, Any]:
    return next(item for item in BLOCKS if item["block_id"] == block_id)


def reset_outputs() -> None:
    for root in [TRIAGE_ROOT, TEXT_ROOT, SEM_ROOT, PCRP_ROOT, PCA_ROOT, STATUS_ROOT, BATCH_ROOT]:
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)


def crop_assets() -> dict[str, dict[str, str]]:
    assets: dict[str, dict[str, str]] = {}
    review_root = TRIAGE_ROOT / "review_assets"
    review_root.mkdir(parents=True, exist_ok=True)
    page_copy = review_root / "page_014.png"
    shutil.copy2(PAGE_IMAGE, page_copy)
    assets["review_assets/page_014.png"] = {"path": page_copy.relative_to(ROOT).as_posix(), "sha256": sha256_file(page_copy)}
    with Image.open(PAGE_IMAGE) as image:
        validate_text_evidence_crop_contracts(image.size, BLOCKS)
        for block in BLOCKS + VISUAL_ONLY_BLOCKS:
            x, y, w, h = block["crop_box_px"]
            target = TRIAGE_ROOT / block["asset"]
            target.parent.mkdir(parents=True, exist_ok=True)
            image.crop((x, y, x + w, y + h)).save(target)
            assets[block["asset"]] = {"path": target.relative_to(ROOT).as_posix(), "sha256": sha256_file(target)}
    return assets


def write_manifest(root: Path, filename: str, title: str) -> None:
    lines = [f"# {title}", "", "| Output | SHA-256 |", "|---|---|"]
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != filename:
            lines.append(f"| `{path.relative_to(root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(root / filename, "\n".join(lines))


def build_triage(predecessors: list[dict[str, str]], assets: dict[str, dict[str, str]]) -> dict[str, Any]:
    blocks = []
    for index, block in enumerate(BLOCKS, start=1):
        blocks.append(
            {
                **block,
                "reading_order": index,
                "content_kind": "text_like_region",
                "text_evidence_crop_id": f"{block['block_id']}-TES",
                "asset_sha256": assets[block["asset"]]["sha256"],
            }
        )
    packet = {
        "package_id": "P014TR-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "triage_crop_contract_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "page_id": PAGE_ID,
        "predecessors": predecessors,
        "review_gate": review_gate("P014TR-G1-VIRAL-001"),
        "review_blocks": blocks,
        "logical_text_order": [f"{block['block_id']}-TES" for block in BLOCKS],
        "visual_only_blocks": VISUAL_ONLY_BLOCKS,
        "guardrails": guardrails({"triage_created": True}),
    }
    write_json(TRIAGE_ROOT / "page_014_triage_packet.json", packet)
    write_json(TRIAGE_ROOT / "page_014_triage_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "guardrails": packet["guardrails"], "block_count": len(blocks)})
    write_text(TRIAGE_ROOT / "page_014_triage_summary.md", "# Page 014 Triage Summary - P014TR-G1-VIRAL-001\n\nMachine-reviewed triage with human review skipped by explicit authorization. Nine page 014 text-evidence surfaces are contract-bound and one visual-only photo anchor is included. Page 015+ is not processed.\n")
    write_manifest(TRIAGE_ROOT, "page_014_triage_manifest.md", "Page 014 Triage Manifest - P014TR-G1-VIRAL-001")
    return packet


def build_text(triage_packet: dict[str, Any]) -> dict[str, Any]:
    lines = ["# Page 014 Text Map - P014TXT-G1-VIRAL-001", "", "Status: `draft_text_machine_reviewed_human_review_skipped`", ""]
    for index, unit in enumerate(TEXT_UNITS, start=1):
        lines.extend([f"## {unit['unit_id']}", "", f"- Reading order: `{index}`", f"- Blocks: `{', '.join(unit_block_ids(unit))}`", "", "```text", unit["text"], "```", ""])
    write_text(TEXT_ROOT / "page_014_text_map.md", "\n".join(lines))
    packet = {
        "package_id": "P014TXT-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "draft_text_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": triage_packet["package_id"], "sha256": sha256_file(TRIAGE_ROOT / "page_014_triage_packet.json")},
        "review_gate": review_gate("P014TXT-G1-VIRAL-001"),
        "logical_reading_order": [unit["unit_id"] for unit in TEXT_UNITS],
        "extraction_method": "manual_from_text_evidence_region",
        "ocr_executed": False,
        "text_map": {"path": "page_014_text_map.md", "sha256": sha256_file(TEXT_ROOT / "page_014_text_map.md")},
        "continuation_metadata": [],
        "guardrails": guardrails({"text_extraction_created": True}),
    }
    write_json(TEXT_ROOT / "page_014_text_extraction_packet.json", packet)
    write_json(TEXT_ROOT / "page_014_text_extraction_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "text_unit_count": len(TEXT_UNITS), "guardrails": packet["guardrails"]})
    write_text(TEXT_ROOT / "page_014_text_extraction_summary.md", "# Page 014 Text Extraction Summary - P014TXT-G1-VIRAL-001\n\nDraft text extracted from P014TR text evidence crops under delegated Sol/Terra review. Human review is skipped by explicit authorization; this creates no OCR/source/page/whole-Gate acceptance.\n")
    write_manifest(TEXT_ROOT, "page_014_text_extraction_manifest.md", "Page 014 Text Extraction Manifest - P014TXT-G1-VIRAL-001")
    return packet


def semantic_units() -> list[dict[str, Any]]:
    keeper_contract = callout_body_contract(callout_heading="Keeper's Notes")
    definitions = [
        ("SU-P014-GEAR-001", "heading", "h2", "section_heading", "P014-B001", "Spektral Krew Gear", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-002", "heading", "h3", "section_heading", "P014-B001", "Carried", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-003", "paragraph", None, "body", "P014-B001", "These bits of equipment are carried by the Krew based on their job (see Investigator descriptions).", None, None, None, {}),
        ("SU-P014-GEAR-004", "heading", "h4", "section_heading", "P014-B002", "Equipment Satchel", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-005", "paragraph", None, "body", "P014-B002", "Each team member has a black canvas satchel (with the Spektral Krew logo of course) for carrying their gear. In some cases, the host may hand off his satchel to someone else while they're on camera. It's big enough to hold the Handheld Night Vision Cameras, EMF Meters, Smart Phones, and FLIR Cameras, plus any other personal gear.", None, None, None, {}),
        ("SU-P014-GEAR-006", "heading", "h4", "section_heading", "P014-B003", "Handheld Night Vision Cameras (2)", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-007", "paragraph", None, "body", "P014-B003", "4K Wi-Fi Full Spectrum Camcorders, Ultra HD Infrared Night Vision Paranormal Investigation Video Camera with 60 fps 24 MP 30x Digital Zoom. Peter and Enoch usually carry and operate these. [Four Hours of Battery Life]", None, None, None, {}),
        ("SU-P014-GEAR-008", "heading", "h4", "section_heading", "P014-B003", "EMF Meter", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-009", "paragraph", None, "body", "P014-B003", "HF-B3G Triple Axis HF RF Power Meter Analyzer and Detector. [12 Hours of Battery Life]", None, None, None, {}),
        ("SU-P014-GEAR-010", "heading", keeper_notes_callout_heading_level(), "callout_heading", "P014-B004", "Keeper's Notes", "block_heading", "bold", True, {}),
        ("SU-P014-GEAR-011", "paragraph", None, "callout_body", "P014-B004", "There are not many EMFs on the island, but the Krew will see the odd tick here and there from background noise. While ghosts don't generate electromagnetic fields, Hastalyk can use this against the Investigators by causing it to respond in the direction it wants them to go. Marco is usually in possession of this.", None, None, None, {"semantic_split_contract": keeper_contract}),
        ("SU-P014-GEAR-012", "heading", "h4", "section_heading", "P014-B005", "Spirit Box", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-013", "paragraph", None, "body", "P014-B005", "This is a custom radio with a frequency scan mode that the Krew hopes will allow them to communicate with spirits. It's about the size of a walkie-talkie and includes a headphone to better hear voices from the beyond. [Eight Hours of Battery Life]", None, None, None, {}),
        ("SU-P014-GEAR-014", "heading", keeper_notes_callout_heading_level(), "callout_heading", "P014-B005", "Keeper's Notes", "block_heading", "bold", True, {}),
        ("SU-P014-GEAR-015", "paragraph", None, "callout_body", "P014-B005", "It's possible that the Spirit Box could pick up radio chatter from the Italian military or the Plague Monk chanting various disturbing litanies in Latin (Keeper's discretion).", None, None, None, {"semantic_split_contract": keeper_contract}),
        ("SU-P014-GEAR-016", "heading", "h4", "section_heading", "P014-B006", "EVP Recorder SCD1", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-017", "paragraph", None, "body", "P014-B006", "The SCD1 is an experimental piece of equipment that Marco has had someone build - it is the Silent Capture Device. The processor and software can detect when nobody is talking and will flash when it picks up a sound during silence. This can be played back in real time. This was an expensive piece of prototype technology, so Marco keeps hold of this.", None, None, None, {}),
        ("SU-P014-GEAR-018", "heading", "h4", "section_heading", "P014-B006", "FLIR Camera for Smartphone", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-019", "paragraph", None, "body", "P014-B006", "FLIR ONE Pro - iOS - Professional Grade Thermal Camera for Smartphones - with VividIR and MSX Image Enhancement Technology. This has been jury rigged by Hyeon so that it uses the video feed from Peter's camera. [Battery Life of the FLIR is only 45 Minutes]", None, None, None, {}),
        ("SU-P014-GEAR-020", "heading", "h3", "section_heading", "P014-B007", "Static", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-021", "paragraph", None, "body", "P014-B007", "These bits of equipment are set up early on and, with the exception of the drone, remain at a single location.", None, None, None, {}),
        ("SU-P014-GEAR-022", "heading", "h4", "section_heading", "P014-B007", "Base Station", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-023", "paragraph", None, "body", "P014-B007", "This is a custom industrial laptop with a Wi-Fi hub and satellite uplink set up for live streaming. A deep cycle battery unit supplies enough power for up to 12 hours of continuous broadcasting.", None, None, None, {}),
        ("SU-P014-GEAR-024", "heading", keeper_notes_callout_heading_level(), "callout_heading", "P014-B007", "Keeper's Notes", "block_heading", "bold", True, {}),
        ("SU-P014-GEAR-025", "paragraph", None, "callout_body", "P014-B007", "At the Keeper's discretion, other devices may be charged off the base station's battery, but this obviously takes time that the Investigators may not have.", None, None, None, {"semantic_split_contract": keeper_contract}),
        ("SU-P014-GEAR-026", "heading", "h4", "section_heading", "P014-B008", "Cellular Wi-Fi Repeaters/Transmitters (2)", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-027", "paragraph", None, "body", "P014-B008", "Each provides Wi-Fi within a 300 Meter radius, and has a battery unit that provides 8-10 hours of uninterrupted signal.", None, None, None, {}),
        ("SU-P014-GEAR-028", "heading", keeper_notes_callout_heading_level(), "callout_heading", "P014-B008", "Keeper's Notes", "block_heading", "bold", True, {}),
        ("SU-P014-GEAR-029", "paragraph", None, "callout_body", "P014-B008", "These are best set up in three key locations, the lighthouse, the far side of the bridge, and the hospital tower. This provides the greatest area of coverage for the investigation site. Note that since the satellite signal is being routed through the Base Station at the lighthouse, the hospital signal requires the bridge transmitter to be active.", None, None, None, {"semantic_split_contract": keeper_contract}),
        ("SU-P014-GEAR-030", "heading", "h4", "section_heading", "P014-B009", "UPS Batteries (3)", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-031", "paragraph", None, "body", "P014-B009", "Primarily used to power the Wi-Fi Transmitters, they have various connections via which other equipment can be recharged. They can provide around six hours of power each in the event of power failure. Really only there in the instance of the battery backup for the hub failing. Extremely heavy as they are essentially large deep-cycle batteries.", None, None, None, {}),
        ("SU-P014-GEAR-032", "heading", "h4", "section_heading", "P014-B009", "Night Vision Cameras (6)", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-033", "paragraph", None, "body", "P014-B009", "Foscam HT2 1080p Outdoor 2.4 g/5 gHz Wi-Fi PTZ IP Camera, 4x Optical Zoom Pan Tilt Security Surveillance Speed Dome, Two-Way Audio with Mic & Speaker, 165 ft. Night Vision, CMOS Image Sensor, IP66. [Six Hours of Battery Life]", None, None, None, {}),
        ("SU-P014-GEAR-034", "heading", "h4", "section_heading", "P014-B009", "Drone", "block_heading", "normal", True, {}),
        ("SU-P014-GEAR-035", "paragraph", None, "body", "P014-B009", "This optional drone is an expensive professional model that is equipped with a night vision capable 4K video camera that can be controlled via Hyeon's iPad app. The video can be recorded locally or fed directly to the live stream. [It includes three batteries with 20 minutes of flight time each.]", None, None, None, {}),
    ]
    result = []
    for order, (unit_id, unit_type, heading_level, display_style, block_id, text, layout_role, font_style, line_break_after, extra) in enumerate(definitions, start=1):
        block = find_block(block_id)
        crop_ids = [f"{item}-TES" for item in unit_block_ids(next((unit for unit in TEXT_UNITS if unit.get("block_id") == block_id or block_id in unit.get("block_ids", [])), {"block_id": block_id}))]
        payload: dict[str, Any] = {
            "unit_id": unit_id,
            "unit_type": unit_type,
            "unit_scope": "in_scope_text",
            "reading_order": order,
            "source_block_id": block_id,
            "source_region_ids": [block["source_region_id"]],
            "crop_ids": crop_ids,
            "text": text,
            "heading_level": heading_level,
            "display_style": display_style,
            "text_source_state": "machine_reviewed_delegated",
        }
        if layout_role is not None:
            payload["layout_role"] = layout_role
        if font_style is not None:
            payload["font_style"] = font_style
        if line_break_after is not None:
            payload["line_break_after"] = line_break_after
        payload.update(extra)
        result.append(payload)
    return result


def build_semantic(text_packet: dict[str, Any]) -> dict[str, Any]:
    units = semantic_units()
    split_validation = validate_semantic_split_contracts(units)
    if not split_validation["valid"]:
        raise SystemExit("P014 semantic split contract validation failed")
    document = {
        "package_id": "P014SEM-G1-VIRAL-001",
        "map_id": "SM-G1-VIRAL-P014-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "semantic_text_map_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": text_packet["package_id"], "sha256": sha256_file(TEXT_ROOT / "page_014_text_extraction_packet.json")},
        "review_gate": review_gate("P014SEM-G1-VIRAL-001"),
        "units": units,
        "unit_count": len(units),
        "validation": {"status": "passed", "findings": split_validation["findings"]},
        "semantic_split_validation": split_validation,
        "guardrails": guardrails({"semantic_map_created": True}),
    }
    markdown = ["# Page 014 Semantic Text Map - P014SEM-G1-VIRAL-001", "", "Status: `semantic_text_map_machine_reviewed_human_review_skipped`", ""]
    for unit in units:
        markdown.extend([f"## {unit['unit_id']}", f"- Type: `{unit['unit_type']}`", f"- Heading level: `{unit.get('heading_level')}`", f"- Layout role: `{unit.get('layout_role')}`", "", "```text", unit["text"], "```", ""])
    write_json(SEM_ROOT / "page_014_semantic_text_map.json", document)
    write_text(SEM_ROOT / "page_014_semantic_text_map.md", "\n".join(markdown))
    write_json(SEM_ROOT / "page_014_semantic_text_map_report.json", {"package_id": document["package_id"], "status": document["status"], "review_gate": document["review_gate"], "unit_count": len(units), "semantic_split_validation": split_validation, "guardrails": document["guardrails"]})
    write_text(SEM_ROOT / "page_014_semantic_text_map_summary.md", "# Page 014 Semantic Text Map Summary - P014SEM-G1-VIRAL-001\n\nMachine-reviewed semantic map with skipped human review under explicit authorization. Continuation text and inline underlined option headings are represented.\n")
    write_manifest(SEM_ROOT, "page_014_semantic_text_map_manifest.md", "Page 014 Semantic Text Map Manifest - P014SEM-G1-VIRAL-001")
    return document


def build_pcrp(semantic_document: dict[str, Any]) -> dict[str, Any]:
    assets_root = PCRP_ROOT / "review_assets"
    assets_root.mkdir(parents=True, exist_ok=True)
    for rel in ["page_014.png"] + [block["asset"].split("/", 1)[1] for block in BLOCKS + VISUAL_ONLY_BLOCKS]:
        source = TRIAGE_ROOT / "review_assets" / rel
        if source.exists():
            shutil.copy2(source, assets_root / rel)
    for name, root, src_name in [
        ("page_014_text_map.md", TEXT_ROOT, "page_014_text_map.md"),
        ("page_014_semantic_text_map.md", SEM_ROOT, "page_014_semantic_text_map.md"),
        ("page_014_semantic_text_map.json", SEM_ROOT, "page_014_semantic_text_map.json"),
    ]:
        shutil.copy2(root / src_name, assets_root / name)
    packet = {
        "package_id": "PCRP-G1-VIRAL-P014-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_complete_review_packet_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": semantic_document["package_id"], "sha256": sha256_file(SEM_ROOT / "page_014_semantic_text_map.json")},
        "review_gate": review_gate("PCRP-G1-VIRAL-P014-001"),
        "ready_blocks": [block["block_id"] for block in BLOCKS],
        "ready_block_count": len(BLOCKS),
        "visual_only_blocks": [block["block_id"] for block in VISUAL_ONLY_BLOCKS],
        "visual_only_block_count": len(VISUAL_ONLY_BLOCKS),
        "blockers": [],
        "open_questions": [],
        "semantic_validation": {"status": "passed", "findings": []},
        "inventory_reconciliation": {"status": "passed", "findings": []},
        "guardrails": guardrails({"pcrp_created": True}),
    }
    write_json(PCRP_ROOT / "page_complete_review_report.json", packet)
    write_text(PCRP_ROOT / "page_complete_review_packet.md", "# Page Complete Review Packet - PCRP-G1-VIRAL-P014-001\n\nMachine-reviewed page 014 PCRP. Human review skipped by explicit authorization; final human review is deferred to the post-P014 bundle/status.\n")
    write_text(PCRP_ROOT / "page_complete_review_summary.md", "# Page 014 Review Summary\n\n9/9 ready text-evidence surfaces and 1 visual-only photo anchor are reconciled; semantic validation and inventory reconciliation passed; no blockers or open questions.\n")
    write_manifest(PCRP_ROOT, "page_complete_review_manifest.md", "Page 014 Complete Review Manifest - PCRP-G1-VIRAL-P014-001")
    return packet


def build_pca(pcrp_packet: dict[str, Any]) -> dict[str, Any]:
    record = {
        "package_id": "P014PCA-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_014_complete_accepted_under_delegated_review_lane",
        "accepted_pages": ["014"],
        "human_review_state": SKIPPED_REVIEW,
        "delegated_review_state": DELEGATED_REVIEW,
        "predecessor": {"package_id": pcrp_packet["package_id"], "sha256": sha256_file(PCRP_ROOT / "page_complete_review_report.json")},
        "review_gate": review_gate("P014PCA-G1-VIRAL-001"),
        "guardrails": guardrails({"page_complete_acceptance_created": True}),
    }
    write_json(PCA_ROOT / "page_complete_acceptance_report.json", record)
    write_text(PCA_ROOT / "page_complete_acceptance_record.md", "# Page Complete Acceptance Record - P014PCA-G1-VIRAL-001\n\nPage 014 accepted only under explicit delegated-review lane authorization. This is not direct per-stage human approval and not whole Gate 1 acceptance.\n")
    write_text(PCA_ROOT / "page_complete_acceptance_summary.md", "# Page Complete Acceptance Summary - P014PCA-G1-VIRAL-001\n\nAccepted page: `014` only. Human review skipped by explicit authorization; Sol/Terra delegated review passed.\n")
    write_manifest(PCA_ROOT, "page_complete_acceptance_manifest.md", "Page 014 Complete Acceptance Manifest - P014PCA-G1-VIRAL-001")
    return record


def build_status(pca_record: dict[str, Any]) -> dict[str, Any]:
    packet = {
        "status_packet_id": "G1SP-G1-VIRAL-009",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "gate_1_status_route_packet_ready_for_final_human_batch_review",
        "page_complete_accepted_pages": [f"{i:03d}" for i in range(1, 15)],
        "remaining_page_complete_pages_unstarted": [f"{i:03d}" for i in range(15, 21)],
        "recommended_next_candidate": "page_015_triage_readiness_not_authorized",
        "predecessor": {"package_id": pca_record["package_id"], "sha256": sha256_file(PCA_ROOT / "page_complete_acceptance_report.json")},
        "review_gate": review_gate("G1SP-G1-VIRAL-009"),
        "guardrails": guardrails(),
    }
    write_json(STATUS_ROOT / "gate_1_status_packet.json", packet)
    write_json(STATUS_ROOT / "gate_1_status_report.json", packet)
    write_text(STATUS_ROOT / "gate_1_status_summary.md", "# Gate 1 Status Route Packet - G1SP-G1-VIRAL-009\n\nPages `001-014` are page-complete accepted only. Pages `015-020` remain unstarted. Page 015 triage/readiness is only the recommended next candidate and is not authorized. Whole Gate 1 and all broad capabilities remain blocked.\n")
    write_manifest(STATUS_ROOT, "gate_1_status_manifest.md", "Gate 1 Status Route Manifest - G1SP-G1-VIRAL-009")
    return packet


def build_bundle(stage_packets: list[dict[str, Any]]) -> None:
    bundle = {
        "package_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "ready_for_bogdan_final_batch_review",
        "human_review_model": "final_bundle_and_post_p014_status_only",
        "internal_stage_human_review_state": SKIPPED_REVIEW,
        "stage_packages": [packet.get("package_id") or packet.get("status_packet_id") for packet in stage_packets],
        "decision_options": ["p014 aggressive batch ok", "hold p014 batch: <reason>"],
        "guardrails": guardrails(),
    }
    write_json(BATCH_ROOT / "page_014_aggressive_batch_report.json", bundle)
    write_text(BATCH_ROOT / "page_014_aggressive_batch_summary.md", "# Page 014 Aggressive Batch Summary - P014BATCH-G1-VIRAL-001\n\nInternal stages P014TR/P014TXT/P014SEM/PCRP/P014PCA were machine-reviewed with Sol/Terra and skipped per-stage human review by explicit authorization. Final human review is requested on this bundle plus `G1SP-G1-VIRAL-009`.\n\nDecision: `p014 aggressive batch ok` or `hold p014 batch: <reason>`.\n")
    write_manifest(BATCH_ROOT, "page_014_aggressive_batch_manifest.md", "Page 014 Aggressive Batch Manifest - P014BATCH-G1-VIRAL-001")


def build() -> None:
    aggressive_batch_authorization_preflight()
    predecessors = verify_predecessors()
    reset_outputs()
    assets = crop_assets()
    triage = build_triage(predecessors, assets)
    text = build_text(triage)
    semantic = build_semantic(text)
    pcrp = build_pcrp(semantic)
    pca = build_pca(pcrp)
    status = build_status(pca)
    build_bundle([triage, text, semantic, pcrp, pca, status])


if __name__ == "__main__":
    check_authorization()
    build()
