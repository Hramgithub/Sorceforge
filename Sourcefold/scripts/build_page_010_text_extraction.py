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
SCRIPT_PATH = ROOT / "scripts" / "build_page_010_text_extraction.py"
TEST_PATH = ROOT / "tests" / "test_page_010_text_extraction.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "page_010_triage_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "page_010_text_extraction_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001"
PACKAGE_ID = "P010TXT-G1-VIRAL-001"
EXPECTED_LOGICAL_READING_ORDER = ["P010-B001-TES", "P010-B005-TES", "P010-B002-TES", "P010-B006-TES"]
PHYSICAL_CROP_ASSET_ORDER = ["P010-B001-TES", "P010-B002-TES", "P010-B005-TES", "P010-B006-TES"]

P010TR_001_PACKET_SHA256 = "210D0801AC1287AD18CCCD87DC8776C1DD85C203BFE555B041E76EDADDE645A0"
P010TR_001_REPORT_SHA256 = "8CB26C4E3CB1BD710195DDF29E438BE8ECA02F6E378572017138463550BC3BC1"
P010TR_001_SUMMARY_SHA256 = "A9AFF4566DF805F16B4D9B26C80220751DC80D5E5A6BD7712076CE87C476283F"
P010TR_001_MANIFEST_SHA256 = "5300F05902050F6D4C4EEFF90B8D4A9F64CEB8965BF773E0FFBDE1116E9AEF28"

TEXT_UNITS: list[dict[str, Any]] = [
    {
        "unit_id": "P010-TEXT-001",
        "block_id": "P010-B001",
        "crop_id": "P010-B001-TES",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R01",
        "role": "peter_profile_continuation_gear",
        "unit_type": "boxed_text",
        "reading_order_index": 1,
        "continues_from_page": "009",
        "continues_to_page": None,
        "text": "\n\n".join(
            [
                "boots and green burberry waterproof jacket under which he always seems to have the same lumberjack shirt and torn blue jeans on.",
                "GEAR CARRIED\n\nSpektral Krew(TM) Satchel, Glowsticks (20), Handheld Night Vision Camera, EMF Meter, EVP Recorder, Smartphone with FLIR Camera, Smartphone, Burner Phone, Saboteur Items, Voice Recorder (with moans and screams recorded to it).",
            ]
        ),
    },
    {
        "unit_id": "P010-TEXT-002",
        "block_id": "P010-B005",
        "crop_id": "P010-B005-TES",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R05",
        "source_region_split": "left_derived_from_R05",
        "role": "hyeon_profile_heading_and_body_start",
        "unit_type": "paragraph_group",
        "reading_order_index": 2,
        "continues_from_page": None,
        "continues_to_crop_id": "P010-B002-TES",
        "text": "\n\n".join(
            [
                "Ku Hyeon (Investigator)",
                "Hyeon (pronounced like HYUN) is a South Korean exchange student who studied in the US. He prefers to go by his family name Hyeon. He is the Producer and go-to 'tech guy' for Spektral Krew and generally sets up and directs the shots. He has completed his degree in film studies, production, and development and is a dab hand at video editing and sound engineering - though the bulk of this is left to Maya.",
                "He is Marco's sound engineer for the channel and often appears on screen as he is honest to a tee and always speaks his mind from a logical standpoint, almost to the point of coming across as argumentative. He has yet to see or experience anything that he would 100% call paranormal and is almost belligerently disagreeable, especially when Corrina does her usual shtick. He knows his parents would not approve of this career path, though he is making good money in the US from his video editing/sound engineering and the Spektral Krew channel. They constantly threaten to send someone over to the",
            ]
        ),
    },
    {
        "unit_id": "P010-TEXT-003",
        "block_id": "P010-B002",
        "crop_id": "P010-B002-TES",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R02",
        "role": "hyeon_profile_body_continuation_appearance_gear",
        "unit_type": "paragraph_group",
        "reading_order_index": 3,
        "continues_from_crop_id": "P010-B005-TES",
        "continues_to_page": None,
        "text": "\n\n".join(
            [
                "US to bring him back. He is always looking at his phone and rejecting calls from them.",
                "APPEARANCE\n\nHyeon (22) is 6'2\" with an average build. His fashion is westernized and includes a bomber jacket, jeans, a pair of fashionable black framed spectacle, and black hair. He always has his backpack and utility belt on when on an investigation. He also wears his own custom tech rig which consists of three iPads that feed him information. They can be folded down to read, flipped around for everyone to see or closed up against his chest for ease of movement.",
                "GEAR CARRIED\n\nSpektral Krew(TM) Satchel, Glowsticks (20), iPad Rig, Electronic Tool Kit, Headcams (5), Misc. Batteries and Electronic Parts",
            ]
        ),
    },
    {
        "unit_id": "P010-TEXT-004",
        "block_id": "P010-B006",
        "crop_id": "P010-B006-TES",
        "source_region_id": "PRM-G1-VIRAL-001-P010-R05",
        "source_region_split": "right_derived_from_R05",
        "role": "maya_profile_heading_and_body_start",
        "unit_type": "paragraph_group",
        "reading_order_index": 4,
        "continues_from_page": None,
        "continues_to_page": "011",
        "text": "\n\n".join(
            [
                "Maya Adeduwon (NPC)",
                "Maya is the English/Nigerian editor and producer for Marco. She was in a car accident when she was younger which left her wheelchair-bound. She is as sharp as a tack, incredibly smart, and quite sassy when she needs to be. She has a habit of calling everyone 'babez' (for example, \"Marco babez, what do you want me to say?\"). She found out about Isola di Malamente from an online contact.",
                "From a technical standpoint, Maya watches, directs, and edits the camera feeds from the Spektral Krew when the team is on a ghost hunt from the safety of her home in London. She has hours of Video Tape (VT) footage that she can slot into",
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
    parser = argparse.ArgumentParser(description="Build page 010 text extraction review artifact.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 010 text extraction is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 010 text extraction requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "p010tr_001_packet": {"path": INPUT_ROOT / "page_010_triage_packet.json", "sha256": P010TR_001_PACKET_SHA256},
        "p010tr_001_report": {"path": INPUT_ROOT / "page_010_triage_report.json", "sha256": P010TR_001_REPORT_SHA256},
        "p010tr_001_summary": {"path": INPUT_ROOT / "page_010_triage_summary.md", "sha256": P010TR_001_SUMMARY_SHA256},
        "p010tr_001_manifest": {"path": INPUT_ROOT / "page_010_triage_manifest.md", "sha256": P010TR_001_MANIFEST_SHA256},
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
        "# Page 010 Text Extraction - P010TXT-G1-VIRAL-001",
        "",
        "Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`",
        "",
        "Boundary: draft transcription from `P010TR-G1-VIRAL-001` text evidence crops only. This is not OCR acceptance, source acceptance, page-complete acceptance, semantic mapping, or PCRP.",
        "",
        "Logical reading order: `P010-B001-TES -> P010-B005-TES -> P010-B002-TES -> P010-B006-TES`.",
        "",
        "Crop order validation: `passed`; logical reading order is continuation-aware and is intentionally not file/asset order.",
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
        continuation_edges=[
            {
                "from": "P010-B005-TES",
                "to": "P010-B002-TES",
                "reason": "Hyeon body continues from lower-left block into upper-right block",
            },
        ],
    )


def build_packet(predecessors: list[dict[str, str]], text_map_sha256: str) -> dict[str, Any]:
    crop_order_validation = build_crop_order_validation()
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "draft_text_ready_for_bogdan_review_no_ocr_acceptance",
        "scope": "page_010_text_extraction_review_only_no_semantic_map_no_pcrp_no_acceptance",
        "predecessors": predecessors,
        "human_review_decision": {
            "decision": "p010_triage_ok",
            "source_message_id": "1476",
            "source_text": "Все , теперь вижу, принято. Коммит",
            "accepted_package_id": "P010TR-G1-VIRAL-001",
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
        "pages_011_020_processing_created": False,
        "text_map": {
            "path": "page_010_text_map.md",
            "sha256": text_map_sha256,
            "unit_count": len(TEXT_UNITS),
            "crop_ids": [unit["crop_id"] for unit in TEXT_UNITS],
        },
        "continuation_notes": [
            "P010-B001 continues Peter Wharton from page 009.",
            "P010-B005 starts Ku Hyeon and continues into P010-B002.",
            "P010-B006 starts Maya Adeduwon and continues to page 011.",
        ],
        "sol_terra_review": {
            "sol": "OK: draft text is bound to the four accepted P010 text-evidence crops and crop_order_validation confirms continuation-aware logical order before semantic/PCRP movement.",
            "terra": "OK: logical order is not file/asset order, Hyeon B005->B002 continuation is explicit, and output is not OCR/source/semantic/PCRP/page acceptance.",
        },
        "decision_options": ["p010 text ok", "hold p010 text: <reason>"],
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 010 Text Extraction Summary - P010TXT-G1-VIRAL-001",
            "",
            "Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`",
            "",
            "- Records Bogdan's `p010 triage ok` decision for `P010TR-G1-VIRAL-001`.",
            "- Provides a draft text file from four page 010 text evidence crops.",
            "- Logical reading order: `B001 -> B005 -> B002 -> B006`.",
            "- Creates no OCR run/output acceptance, no source acceptance, no semantic map, no PCRP, no page-complete acceptance, and no whole Gate 1 acceptance.",
            "- Next human decision: `p010 text ok` or `hold p010 text: <reason>`.",
            "",
        ]
    )


def build_manifest() -> str:
    lines = [
        "# Page 010 Text Extraction Manifest - P010TXT-G1-VIRAL-001",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_010_text_extraction_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    text_map_path = OUTPUT_ROOT / "page_010_text_map.md"
    text_map_path.write_text(build_text_map(), encoding="utf-8", newline="\n")
    packet = build_packet(predecessors, sha256_file(text_map_path))
    if packet["crop_order_validation"]["status"] != "passed":
        raise SystemExit(f"crop order validation blocked: {packet['crop_order_validation']['findings']}")
    packet["text_extraction_contract_validation"] = require_valid_text_extraction_contract(
        packet=packet,
        expected_predecessor_package_id="P010TR-G1-VIRAL-001",
        requires_crop_order_validation=True,
        requires_continuation_notes=True,
    )
    write_json(OUTPUT_ROOT / "page_010_text_extraction_packet.json", packet)
    write_json(
        OUTPUT_ROOT / "page_010_text_extraction_report.json",
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
            "crop_order_validation_status": packet["crop_order_validation"]["status"],
            "text_extraction_contract_status": packet["text_extraction_contract_validation"]["status"],
            "logical_order_is_not_asset_order": packet["crop_order_validation"]["logical_order_is_not_asset_order"],
            "ocr_execution_created": False,
            "ocr_output_created": False,
            "source_acceptance_created": False,
            "semantic_map_created": False,
            "pcrp_created": False,
            "page_complete_acceptance_created": False,
        },
    )
    (OUTPUT_ROOT / "page_010_text_extraction_summary.md").write_text(
        build_summary(packet), encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "page_010_text_extraction_manifest.md").write_text(
        build_manifest(), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    write_outputs()
