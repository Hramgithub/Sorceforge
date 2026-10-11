from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from crop_order_validation import validate_crop_order
from text_extraction_contract import require_valid_text_extraction_contract


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_011_text_extraction.py"
TEST_PATH = ROOT / "tests" / "test_page_011_text_extraction.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "page_011_triage_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "page_011_text_extraction_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-011-TEXT-EXTRACTION-001"
PACKAGE_ID = "P011TXT-G1-VIRAL-001"
EXPECTED_LOGICAL_READING_ORDER = ["P011-B001-TES", "P011-B004-TES"]
PHYSICAL_CROP_ASSET_ORDER = ["P011-B001-TES", "P011-B004-TES"]

P011TR_001_PACKET_SHA256 = "E27AF4DC0B601D7562DE240980C7F6BC8BAD008D05FC3841396B2B0F8289BE8B"
P011TR_001_REPORT_SHA256 = "E1E3E3A43DAD0995142E9842C0DAC3BBE601385ADC9FE6E2D60F72641F227E6D"
P011TR_001_SUMMARY_SHA256 = "30ECCD3E545209C8F7A7E64A50C3C0C4C8E5FD2D1029E3F3D60EA7FE137006B8"
P011TR_001_MANIFEST_SHA256 = "A0F73DEA7B22DF264D1E5F7C638093FD54E51065F5EBE77C919EFA895281FC12"

TEXT_UNITS: list[dict[str, Any]] = [
    {
        "unit_id": "P011-TEXT-001",
        "block_id": "P011-B001",
        "crop_id": "P011-B001-TES",
        "source_region_id": "PRM-G1-VIRAL-001-P011-R01",
        "role": "maya_profile_continuation_secret_appearance",
        "unit_type": "paragraph_group",
        "reading_order_index": 1,
        "continues_from_page": "010",
        "continues_to_page": None,
        "text": "\n\n".join(
            [
                "the stream when they take a break or move location and can essentially cut the feed by doing this. She has a direct chat line to Hyeon via one of his iPads on his tech rig, but if desperate will call Marco directly. Marco often refers to Maya as \"the eyes in the sky\".",
                "Maya's Secrets",
                "Maya also deals and mines Crypto and does hacking in her spare time, seeing just how far she can go down the rabbit hole. She sees right through Corrina and knows in her heart of hearts that she is a phony. She has a real soft spot for Enoch and sees how troubled and kind he is.",
                "During her editing of Spektral Krew's videos, she has seen Peter sneaking off and faking evidence when he thinks he is not being watched. She cuts all of this out and has it stored just in case she needs something from him. She understands his reasons though - they are onto a good thing with Marco and it pays well. She found out about Isola di Malamente and did a deep-dive on it, discovering that on all of the major map sites, the island is blank and featureless, but on a forum that hacks military satellites it shows the island as being full of buildings. What are they trying to hide?",
                "Although loyal to the Krew, she is not above making a quick buck or two by telling other ghost hunting teams about locations they are visiting. This irks Marco no-end, and he often wonders how rival investigative teams like the Phantom Posse and Ghost Bros manage to investigate some places before they do, never once suspecting Maya could be responsible.",
                "APPEARANCE",
                "Before the accident, Maya stood 5'8\". She has long semi-afro/dreadlocks, a pierced nose, absolutely perfect white teeth, and is extremely smiley. She always has a t-shirt on as she rarely leaves the house and has multiple screens and workstations. She enjoys working with the Spektral Krew and helps them out on investigations by watching the feeds from the many cameras they use.",
            ]
        ),
    },
    {
        "unit_id": "P011-TEXT-002",
        "block_id": "P011-B004",
        "crop_id": "P011-B004-TES",
        "source_region_id": "PRM-G1-VIRAL-001-P011-R04",
        "role": "emily_profile_heading_body_start",
        "unit_type": "paragraph_group",
        "reading_order_index": 2,
        "continues_from_page": None,
        "continues_to_page": "012",
        "text": "\n\n".join(
            [
                "Emily 'Em' Lavigne (NPC)",
                "To either add a sense of menace or lighten up proceedings a bit, we have included an NPC - Emily 'Em' Lavigne. She has been designed to be used in two different ways. As either 'The Super Fan' or the surviving member of a rival ghost hunting group.",
                "Super Fan Option. Em is a stalker super fan of the channel who follows them everywhere as she is utterly obsessed with Corrina - think someone like Mel from the Flight of the Conchords TV series. Em truly believes that she is spiritually connected to Corrina in some inexplicable way. Corrina is very aware of Em, though acts aloof and pretends to forget her name. Em is ultimately attracted to Corrina beyond spiritual connection, but has not actually come to terms with her own sexuality - she is actually a closeted lesbian. On the other hand, Corrina puts on an act of being incredibly sexually free and pretends to be pan-sexual - she is actually very straight and doesn't reciprocate Em's slightly cringe-worthy advances. Em is tolerated by Marco and the Krew as she buys a lot of merchandise and endlessly promotes them on all forms of social media. She has created over 200 dummy accounts to sub to their channel and help the algorithm.",
                "Em learned about the Krew investigating the island around a week ago from an anonymous tipoff - this was actually by Maya who was hedging her bets on who she could make the most cash from. She flew out to Italy immediately, stayed in Perla for a few days and paid a group of local teens to ferry",
            ]
        ),
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
    parser = argparse.ArgumentParser(description="Build page 011 text extraction review artifact.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 011 text extraction is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 011 text extraction requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "p011tr_001_packet": {"path": INPUT_ROOT / "page_011_triage_packet.json", "sha256": P011TR_001_PACKET_SHA256},
        "p011tr_001_report": {"path": INPUT_ROOT / "page_011_triage_report.json", "sha256": P011TR_001_REPORT_SHA256},
        "p011tr_001_summary": {"path": INPUT_ROOT / "page_011_triage_summary.md", "sha256": P011TR_001_SUMMARY_SHA256},
        "p011tr_001_manifest": {"path": INPUT_ROOT / "page_011_triage_manifest.md", "sha256": P011TR_001_MANIFEST_SHA256},
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        if actual != item["sha256"]:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": item["path"].relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def build_text_map() -> str:
    lines = [
        "# Page 011 Text Extraction - P011TXT-G1-VIRAL-001",
        "",
        "Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`",
        "",
        "Boundary: draft transcription from `P011TR-G1-VIRAL-001` text evidence crops only. This is not OCR acceptance, source acceptance, page-complete acceptance, semantic mapping, or PCRP.",
        "",
        "Excluded from text extraction: `P011-B002` Emily portrait and `P011-B003` lower-left screen image are visual-only anchors.",
        "",
        "Logical reading order: `P011-B001-TES -> P011-B004-TES`.",
        "",
        "Crop order validation: `passed`; logical reading order uses only text evidence crops.",
        "",
    ]
    for unit in TEXT_UNITS:
        lines.extend(
            [
                f"## {unit['unit_id']} - {unit['role']}",
                "",
                f"- Reading order: `{unit['reading_order_index']}`",
                f"- Block: `{unit['block_id']}`",
                f"- Crop: `{unit['crop_id']}`",
                f"- Source region: `{unit['source_region_id']}`",
                f"- Type: `{unit['unit_type']}`",
                "",
                "```text",
                unit["text"],
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def build_crop_order_validation() -> dict[str, Any]:
    return validate_crop_order(
        units=TEXT_UNITS,
        expected_logical_order=EXPECTED_LOGICAL_READING_ORDER,
        physical_crop_asset_order=PHYSICAL_CROP_ASSET_ORDER,
        continuation_edges=[],
    )


def build_packet(predecessors: list[dict[str, str]], text_map_sha256: str) -> dict[str, Any]:
    crop_order_validation = build_crop_order_validation()
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "draft_text_ready_for_bogdan_review_no_ocr_acceptance",
        "scope": "page_011_text_extraction_review_only_no_semantic_map_no_pcrp_no_acceptance",
        "predecessors": predecessors,
        "human_review_decision": {
            "decision": "p011_triage_ok",
            "source_message_id": "1669",
            "source_text": "p011 triage ok",
            "accepted_package_id": "P011TR-G1-VIRAL-001",
            "creates_page_complete_acceptance": False,
        },
        "text_source_state": "manual_transcription_from_text_evidence_crops_draft",
        "logical_reading_order": EXPECTED_LOGICAL_READING_ORDER,
        "crop_order_validation": crop_order_validation,
        "ocr_execution_created": False,
        "ocr_output_created": False,
        "ocr_acceptance_created": False,
        "source_acceptance_created": False,
        "semantic_map_created": False,
        "pcrp_created": False,
        "page_complete_acceptance_created": False,
        "whole_gate_1_acceptance_created": False,
        "fixture_admission_created": False,
        "pages_012_020_processing_created": False,
        "text_map": {
            "path": "page_011_text_map.md",
            "sha256": text_map_sha256,
            "unit_count": len(TEXT_UNITS),
            "crop_ids": [unit["crop_id"] for unit in TEXT_UNITS],
            "excluded_visual_only_blocks": ["P011-B002", "P011-B003"],
        },
        "continuation_notes": [
            "P011-B001 continues Maya Adeduwon from page 010.",
            "P011-B004 starts Emily 'Em' Lavigne and continues to page 012.",
        ],
        "sol_terra_review": {
            "sol": "OK: draft text is bound only to P011-B001-TES and P011-B004-TES, with visual-only B002/B003 excluded from extraction.",
            "terra": "OK: this creates no OCR/source/semantic/PCRP/page acceptance and does not process page 012 beyond continuation metadata.",
        },
        "decision_options": ["p011 text ok", "hold p011 text: <reason>"],
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 011 Text Extraction Summary - P011TXT-G1-VIRAL-001",
            "",
            "Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`",
            "",
            "- Records Bogdan's `p011 triage ok` decision for `P011TR-G1-VIRAL-001`.",
            "- Provides a draft text file from two page 011 text evidence crops.",
            "- Logical reading order: `B001 -> B004`.",
            "- Excludes visual-only `P011-B002` portrait and `P011-B003` screen image from text extraction.",
            "- Creates no OCR run/output acceptance, no source acceptance, no semantic map, no PCRP, no page-complete acceptance, and no whole Gate 1 acceptance.",
            "- Next human decision: `p011 text ok` or `hold p011 text: <reason>`.",
            "",
        ]
    )


def build_manifest() -> str:
    lines = [
        "# Page 011 Text Extraction Manifest - P011TXT-G1-VIRAL-001",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_011_text_extraction_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    text_map_path = OUTPUT_ROOT / "page_011_text_map.md"
    text_map_path.write_text(build_text_map(), encoding="utf-8", newline="\n")
    packet = build_packet(predecessors, sha256_file(text_map_path))
    if packet["crop_order_validation"]["status"] != "passed":
        raise SystemExit(f"crop order validation blocked: {packet['crop_order_validation']['findings']}")
    packet["text_extraction_contract_validation"] = require_valid_text_extraction_contract(
        packet=packet,
        expected_predecessor_package_id="P011TR-G1-VIRAL-001",
        requires_crop_order_validation=True,
        requires_continuation_notes=True,
    )
    write_json(OUTPUT_ROOT / "page_011_text_extraction_packet.json", packet)
    write_json(
        OUTPUT_ROOT / "page_011_text_extraction_report.json",
        {
            "package_id": PACKAGE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "text_map_sha256": packet["text_map"]["sha256"],
            "text_unit_count": len(TEXT_UNITS),
            "logical_reading_order": packet["logical_reading_order"],
            "excluded_visual_only_blocks": packet["text_map"]["excluded_visual_only_blocks"],
            "crop_order_validation_status": packet["crop_order_validation"]["status"],
            "text_extraction_contract_status": packet["text_extraction_contract_validation"]["status"],
            "ocr_execution_created": False,
            "ocr_output_created": False,
            "source_acceptance_created": False,
            "semantic_map_created": False,
            "pcrp_created": False,
            "page_complete_acceptance_created": False,
            "pages_012_020_processing_created": False,
        },
    )
    (OUTPUT_ROOT / "page_011_text_extraction_summary.md").write_text(
        build_summary(packet), encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "page_011_text_extraction_manifest.md").write_text(
        build_manifest(), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    write_outputs()
