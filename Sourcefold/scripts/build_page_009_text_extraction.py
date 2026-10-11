from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from text_extraction_contract import require_valid_text_extraction_contract


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_009_text_extraction.py"
TEST_PATH = ROOT / "tests" / "test_page_009_text_extraction.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "page_009_triage_G1_VIRAL_003"
OUTPUT_ROOT = TRIAL_ROOT / "page_009_text_extraction_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-009-TEXT-EXTRACTION-001"
PACKAGE_ID = "P009TXT-G1-VIRAL-001"

P009TR_003_PACKET_SHA256 = "51154E1B2007EF0204B6F40FB71E761C5B55FD350C9B6B5152D71A07C791F390"
P009TR_003_REPORT_SHA256 = "0F0A679344957DB67097A164466349A28A4A81C16C9B96D1565FFE4CBE42B9F8"
P009TR_003_SUMMARY_SHA256 = "B04C0D560FA4B82AC4219B2733E9E27B4D6D7A347E8B7DB5B1036E0A2A08EC27"
P009TR_003_MANIFEST_SHA256 = "27C10FEFA49D6B233C49B3620E23059BC87AF7D254AC1144CA54C1283098EF26"

TEXT_UNITS: list[dict[str, Any]] = [
    {
        "unit_id": "P009-TEXT-L-001",
        "block_id": "P009-B003",
        "crop_id": "P009-B003-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R03",
        "role": "left_profile_heading",
        "unit_type": "heading",
        "text": "Enoch Jeremiah Eakins (Investigator)",
    },
    {
        "unit_id": "P009-TEXT-L-002",
        "block_id": "P009-B003",
        "crop_id": "P009-B003-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R03",
        "role": "left_profile_body",
        "unit_type": "paragraph_group",
        "text": "\n\n".join(
            [
                "Enoch is a former Wenger Mennonite Amish lad from Ohio who went on the Rumspringa and never returned. His community thought he was \"aangeraakt door duivels\" (touched by the devils), so never went looking for him (not that they do anyway).",
                "He is an absolute bear of a man who was hired by Marco as a bodyguard and investigator, just in case they ever get into danger with people as opposed to the supernatural, as despite being quite a kind soul, he is physically very intimidating. Enoch has a broad smile and an infectious laugh. He's actually a lot smarter than he looks and a competent investigator who picks up on things the others don't. Enoch doesn't fully understand it, but he actually has The Sight (see Appendix), though he puts a lot of what he sees down to just indulging in too much drink and drugs.",
                "He has not told any of the Krew that he has The Sight, nor will he do so. It is his cross to bear.",
            ]
        ),
    },
    {
        "unit_id": "P009-TEXT-L-003",
        "block_id": "P009-B003",
        "crop_id": "P009-B003-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R03",
        "role": "left_profile_appearance",
        "unit_type": "boxed_text",
        "text": "APPEARANCE\n\nEnoch (26) is a 6'6\" mountain of a man. Always wears a plain white button up shirt and blue jeans along with open-toed sandals (even in the snow) and a Spektral Krew branded baseball cap. He has a full beard and kind blue eyes. Has a fairly awful scar down one side of his face due to a farming implement accident when he was younger. Courteous to a tee and genuinely well liked by all of the Krew.",
    },
    {
        "unit_id": "P009-TEXT-L-004",
        "block_id": "P009-B003",
        "crop_id": "P009-B003-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R03",
        "role": "left_profile_gear",
        "unit_type": "boxed_text",
        "text": "GEAR CARRIED\n\nSpektral Krew(TM) Satchel, Glowsticks (20), Wi-Fi Repeaters (2), Static Night Vision Cameras (6)",
    },
    {
        "unit_id": "P009-TEXT-R-001",
        "block_id": "P009-B004",
        "crop_id": "P009-B004-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R04",
        "role": "right_profile_heading",
        "unit_type": "heading",
        "text": "Peter Wharton (Investigator)",
    },
    {
        "unit_id": "P009-TEXT-R-002",
        "block_id": "P009-B004",
        "crop_id": "P009-B004-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R04",
        "role": "right_profile_body",
        "unit_type": "paragraph_group",
        "text": "\n\n".join(
            [
                "Peter is a career criminal and former heroin addict who fell into his current job as cameraman for Spektral Krew when he went to sell a stolen laptop and digital camera to Marco.",
                "He had bought and sold so many of these over the years that when asked by Marco to demonstrate how it worked, he easily understood what to do, and Marco offered him a job on the spot which he accepted as nobody had ever done that for him before. In order to keep the cash flowing, for Spektral Krew and thus himself, he secretly sets up fake evidence and triggers it at opportune moments during the investigations - using things like fishing line to move things off camera, palming small objects and leaving them in other places, then spotting them with shock on his face, leaving superchat messages on the stream pointing out his 'activity' using a false account, and the like. Peter's player should be encouraged to be inventive with his fake evidence, as well as making sure he doesn't get caught.",
                "Peter is a man of few words and although appreciative of his job, he is always looking for the next thing to steal as it is a habit for him (he is a borderline kleptomaniac). Not easily phased. Likes Enoch as he sees him as a bit of a kindred spirit.",
            ]
        ),
    },
    {
        "unit_id": "P009-TEXT-R-003",
        "block_id": "P009-B004",
        "crop_id": "P009-B004-TEXT-EVIDENCE",
        "source_region_id": "PRM-G1-VIRAL-001-P009-R04",
        "role": "right_profile_appearance",
        "unit_type": "boxed_text",
        "text": "APPEARANCE\n\nPeter (39) is 5'9\" and rakishly thin with slightly unkempt hair. Has a stubble covered face, with darting eyes and a hand-rolled cigarette always hanging off his lip. Wears a pair of Doc Martens",
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
    parser = argparse.ArgumentParser(description="Build page 009 text extraction review artifact.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 009 text extraction is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 009 text extraction requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "p009tr_003_packet": {"path": INPUT_ROOT / "page_009_triage_packet.json", "sha256": P009TR_003_PACKET_SHA256},
        "p009tr_003_report": {"path": INPUT_ROOT / "page_009_triage_report.json", "sha256": P009TR_003_REPORT_SHA256},
        "p009tr_003_summary": {"path": INPUT_ROOT / "page_009_triage_summary.md", "sha256": P009TR_003_SUMMARY_SHA256},
        "p009tr_003_manifest": {"path": INPUT_ROOT / "page_009_triage_manifest.md", "sha256": P009TR_003_MANIFEST_SHA256},
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
        "# Page 009 Text Extraction - P009TXT-G1-VIRAL-001",
        "",
        "Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`",
        "",
        "Boundary: draft transcription from `P009TR-G1-VIRAL-003` text evidence crops only. This is not OCR acceptance, source acceptance, page-complete acceptance, or PCRP.",
        "",
    ]
    for unit in TEXT_UNITS:
        lines.extend(
            [
                f"## {unit['unit_id']} - {unit['role']}",
                "",
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


def build_packet(predecessors: list[dict[str, str]], text_map_sha256: str) -> dict[str, Any]:
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "draft_text_ready_for_bogdan_review_no_ocr_acceptance",
        "scope": "page_009_text_extraction_review_only_no_pcrp_no_acceptance",
        "predecessors": predecessors,
        "human_review_decision": {
            "decision": "p009_crop_contract_ok",
            "source_message_id": "1351",
            "source_text": "Ок, тогда шаг ок.",
            "accepted_package_id": "P009TR-G1-VIRAL-003",
            "creates_page_complete_acceptance": False,
        },
        "text_source_state": "manual_transcription_from_text_evidence_crops_draft",
        "ocr_execution_created": False,
        "ocr_output_created": False,
        "ocr_acceptance_created": False,
        "source_acceptance_created": False,
        "semantic_map_created": False,
        "pcrp_created": False,
        "page_complete_acceptance_created": False,
        "whole_gate_1_acceptance_created": False,
        "fixture_admission_created": False,
        "pages_010_020_processing_created": False,
        "text_map": {
            "path": "page_009_text_map.md",
            "sha256": text_map_sha256,
            "unit_count": len(TEXT_UNITS),
            "crop_ids": sorted({unit["crop_id"] for unit in TEXT_UNITS}),
        },
        "sol_terra_review": {
            "sol": "OK: decision is recorded, text units are bounded to P009TR-003 text evidence crops, and no acceptance/PCRP capability is created.",
            "terra": "OK: draft transcription is not labeled OCR output or accepted source; PCRP remains separately authorized.",
        },
        "decision_options": ["p009 text ok", "hold p009 text: <reason>"],
    }


def build_summary(packet: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 009 Text Extraction Summary - P009TXT-G1-VIRAL-001",
            "",
            "Status: `draft_text_ready_for_bogdan_review_no_ocr_acceptance`",
            "",
            "- Records Bogdan's `p009 crop contract ok` decision for `P009TR-G1-VIRAL-003`.",
            "- Provides a draft text file from the two page 009 text evidence crops.",
            "- Creates no OCR run/output acceptance, no source acceptance, no PCRP, no page-complete acceptance, and no whole Gate 1 acceptance.",
            "- Next human decision: `p009 text ok` or `hold p009 text: <reason>`.",
            "",
        ]
    )


def build_manifest() -> str:
    lines = [
        "# Page 009 Text Extraction Manifest - P009TXT-G1-VIRAL-001",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_009_text_extraction_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    text_map = build_text_map()
    text_map_path = OUTPUT_ROOT / "page_009_text_map.md"
    text_map_path.write_text(text_map, encoding="utf-8", newline="\n")
    packet = build_packet(predecessors, sha256_file(text_map_path))
    packet["text_extraction_contract_validation"] = require_valid_text_extraction_contract(
        packet=packet,
        expected_predecessor_package_id="P009TR-G1-VIRAL-003",
        requires_crop_order_validation=False,
        requires_continuation_notes=False,
    )
    write_json(OUTPUT_ROOT / "page_009_text_extraction_packet.json", packet)
    write_json(
        OUTPUT_ROOT / "page_009_text_extraction_report.json",
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
            "ocr_execution_created": False,
            "ocr_output_created": False,
            "source_acceptance_created": False,
            "semantic_map_created": False,
            "pcrp_created": False,
            "page_complete_acceptance_created": False,
            "text_extraction_contract_status": packet["text_extraction_contract_validation"]["status"],
        },
    )
    (OUTPUT_ROOT / "page_009_text_extraction_summary.md").write_text(
        build_summary(packet), encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "page_009_text_extraction_manifest.md").write_text(
        build_manifest(), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    write_outputs()
