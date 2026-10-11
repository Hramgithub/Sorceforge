from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from human_review_gate_contract import validate_human_review_gate
from page_review_semantic_units import (
    SEMANTIC_UNIT_SCHEMA_VERSION,
    SEMANTIC_UNIT_TAXONOMY_VERSION,
    build_semantic_map_markdown,
    reconcile_page_inventory,
    semantic_map_document,
    validate_semantic_map_markdown,
    validate_text_evidence_crop_links,
)
from text_extraction_contract import require_text_extraction_consumer_gate


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_010_semantic_text_map.py"
TEST_PATH = ROOT / "tests" / "test_page_010_semantic_text_map.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "page_010_text_extraction_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "page_010_semantic_text_map_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-010-SEMANTIC-TEXT-MAP-001"
PACKAGE_ID = "P010SEM-G1-VIRAL-001"
MAP_ID = "SM-G1-VIRAL-P010-001"

P010TXT_PACKET_SHA256 = "8153D685A82352030C38A6F3F58843AE0F05FDCD98C697BD652C4F6E04F9644A"
P010TXT_REPORT_SHA256 = "929E9B25BFED4FABA1DC131DF22E25F127B66EC8545D2B06A3A48C935FE68EE0"
P010TXT_SUMMARY_SHA256 = "2D2603FA96139CAB57965E0FD37B4EC283BDD7843A23F92C1126A27FB18B04A8"
P010TXT_TEXT_MAP_SHA256 = "EBF6D19ADA6DE436A19AC74C43CFF567F6C05F6D3A3F59991B12150027769D59"
P010TXT_MANIFEST_SHA256 = "FCAA9E9BFECFB14D3657934E79114D63AE448A8AEFEF7D3392137FB8C32015EC"


def unit(
    *,
    unit_id: str,
    unit_type: str,
    reading_order: int,
    text: str,
    heading_level: str | None,
    display_style: str,
    block_role: str,
    source_region_id: str,
    crop_id: str,
    source_block_id: str,
    role: str,
    continues_from: str | None = None,
    continues_to: str | None = None,
    external_continues_from: str | None = None,
    external_continues_to: str | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "unit_id": unit_id,
        "schema_version": SEMANTIC_UNIT_SCHEMA_VERSION,
        "taxonomy_version": SEMANTIC_UNIT_TAXONOMY_VERSION,
        "unit_type": unit_type,
        "unit_scope": "in_scope_text",
        "reading_order": reading_order,
        "source_region_ids": [source_region_id],
        "crop_ids": [crop_id],
        "evidence_predecessors": ["P010TXT-G1-VIRAL-001", "P010TR-G1-VIRAL-001"],
        "text_source_state": "human_verified",
        "text": text,
        "heading_level": heading_level,
        "display_style": display_style,
        "source_role": "human_verified_span",
        "block_role": block_role,
        "source_block_id": source_block_id,
        "span_ids": [unit_id.replace("SU-", "SPAN-")],
        "review_state": "ready_for_review",
        "source_text_role": role,
    }
    if continues_from is not None:
        payload["continues_from"] = continues_from
    if continues_to is not None:
        payload["continues_to"] = continues_to
    if external_continues_from is not None:
        payload["external_continues_from"] = external_continues_from
    if external_continues_to is not None:
        payload["external_continues_to"] = external_continues_to
    return payload


SEMANTIC_UNITS = [
    unit(
        unit_id="SU-P010-PETER-001",
        unit_type="continuation",
        reading_order=1,
        text="boots and green burberry waterproof jacket under which he always seems to have the same lumberjack shirt and torn blue jeans on.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R01",
        crop_id="P010-B001-TES",
        source_block_id="P010-B001",
        role="peter_appearance_continuation",
        external_continues_from="P009/SU-P009-R-006",
    ),
    unit(
        unit_id="SU-P010-PETER-002",
        unit_type="heading",
        reading_order=2,
        text="GEAR CARRIED",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R01",
        crop_id="P010-B001-TES",
        source_block_id="P010-B001",
        role="peter_box_heading",
    ),
    unit(
        unit_id="SU-P010-PETER-003",
        unit_type="paragraph",
        reading_order=3,
        text="Spektral Krew(TM) Satchel, Glowsticks (20), Handheld Night Vision Camera, EMF Meter, EVP Recorder, Smartphone with FLIR Camera, Smartphone, Burner Phone, Saboteur Items, Voice Recorder (with moans and screams recorded to it).",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R01",
        crop_id="P010-B001-TES",
        source_block_id="P010-B001",
        role="peter_box_body",
    ),
    unit(
        unit_id="SU-P010-HYEON-001",
        unit_type="heading",
        reading_order=4,
        text="Ku Hyeon (Investigator)",
        heading_level="h2",
        display_style="section_heading",
        block_role="title_region",
        source_region_id="PRM-G1-VIRAL-001-P010-R05",
        crop_id="P010-B005-TES",
        source_block_id="P010-B005",
        role="hyeon_profile_name_heading",
    ),
    unit(
        unit_id="SU-P010-HYEON-002",
        unit_type="paragraph",
        reading_order=5,
        text="Hyeon (pronounced like HYUN) is a South Korean exchange student who studied in the US. He prefers to go by his family name Hyeon. He is the Producer and go-to 'tech guy' for Spektral Krew and generally sets up and directs the shots. He has completed his degree in film studies, production, and development and is a dab hand at video editing and sound engineering - though the bulk of this is left to Maya.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R05",
        crop_id="P010-B005-TES",
        source_block_id="P010-B005",
        role="hyeon_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P010-HYEON-003",
        unit_type="continuation",
        reading_order=6,
        text="He is Marco's sound engineer for the channel and often appears on screen as he is honest to a tee and always speaks his mind from a logical standpoint, almost to the point of coming across as argumentative. He has yet to see or experience anything that he would 100% call paranormal and is almost belligerently disagreeable, especially when Corrina does her usual shtick. He knows his parents would not approve of this career path, though he is making good money in the US from his video editing/sound engineering and the Spektral Krew channel. They constantly threaten to send someone over to the",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R05",
        crop_id="P010-B005-TES",
        source_block_id="P010-B005",
        role="hyeon_profile_body_continuation_start",
        continues_to="SU-P010-HYEON-004",
    ),
    unit(
        unit_id="SU-P010-HYEON-004",
        unit_type="continuation",
        reading_order=7,
        text="US to bring him back. He is always looking at his phone and rejecting calls from them.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R02",
        crop_id="P010-B002-TES",
        source_block_id="P010-B002",
        role="hyeon_profile_body_continuation_finish",
        continues_from="SU-P010-HYEON-003",
    ),
    unit(
        unit_id="SU-P010-HYEON-005",
        unit_type="heading",
        reading_order=8,
        text="APPEARANCE",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R02",
        crop_id="P010-B002-TES",
        source_block_id="P010-B002",
        role="hyeon_box_heading",
    ),
    unit(
        unit_id="SU-P010-HYEON-006",
        unit_type="paragraph",
        reading_order=9,
        text='Hyeon (22) is 6\'2" with an average build. His fashion is westernized and includes a bomber jacket, jeans, a pair of fashionable black framed spectacle, and black hair. He always has his backpack and utility belt on when on an investigation. He also wears his own custom tech rig which consists of three iPads that feed him information. They can be folded down to read, flipped around for everyone to see or closed up against his chest for ease of movement.',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R02",
        crop_id="P010-B002-TES",
        source_block_id="P010-B002",
        role="hyeon_box_body",
    ),
    unit(
        unit_id="SU-P010-HYEON-007",
        unit_type="heading",
        reading_order=10,
        text="GEAR CARRIED",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R02",
        crop_id="P010-B002-TES",
        source_block_id="P010-B002",
        role="hyeon_box_heading",
    ),
    unit(
        unit_id="SU-P010-HYEON-008",
        unit_type="paragraph",
        reading_order=11,
        text="Spektral Krew(TM) Satchel, Glowsticks (20), iPad Rig, Electronic Tool Kit, Headcams (5), Misc. Batteries and Electronic Parts",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R02",
        crop_id="P010-B002-TES",
        source_block_id="P010-B002",
        role="hyeon_box_body",
    ),
    unit(
        unit_id="SU-P010-MAYA-001",
        unit_type="heading",
        reading_order=12,
        text="Maya Adeduwon (NPC)",
        heading_level="h2",
        display_style="section_heading",
        block_role="title_region",
        source_region_id="PRM-G1-VIRAL-001-P010-R05",
        crop_id="P010-B006-TES",
        source_block_id="P010-B006",
        role="maya_profile_name_heading",
    ),
    unit(
        unit_id="SU-P010-MAYA-002",
        unit_type="paragraph",
        reading_order=13,
        text='Maya is the English/Nigerian editor and producer for Marco. She was in a car accident when she was younger which left her wheelchair-bound. She is as sharp as a tack, incredibly smart, and quite sassy when she needs to be. She has a habit of calling everyone \'babez\' (for example, "Marco babez, what do you want me to say?"). She found out about Isola di Malamente from an online contact.',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R05",
        crop_id="P010-B006-TES",
        source_block_id="P010-B006",
        role="maya_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P010-MAYA-003",
        unit_type="continuation",
        reading_order=14,
        text="From a technical standpoint, Maya watches, directs, and edits the camera feeds from the Spektral Krew when the team is on a ghost hunt from the safety of her home in London. She has hours of Video Tape (VT) footage that she can slot into",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P010-R05",
        crop_id="P010-B006-TES",
        source_block_id="P010-B006",
        role="maya_profile_body_continuation_start",
        external_continues_to="P011/Maya continuation",
    ),
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
    parser = argparse.ArgumentParser(description="Build page 010 semantic text map review artifact.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 010 semantic text map is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 010 semantic text map requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> tuple[list[dict[str, str]], dict[str, Any]]:
    verify_authorization_ledger()
    predecessors = {
        "p010txt_packet": {"path": INPUT_ROOT / "page_010_text_extraction_packet.json", "sha256": P010TXT_PACKET_SHA256},
        "p010txt_report": {"path": INPUT_ROOT / "page_010_text_extraction_report.json", "sha256": P010TXT_REPORT_SHA256},
        "p010txt_summary": {"path": INPUT_ROOT / "page_010_text_extraction_summary.md", "sha256": P010TXT_SUMMARY_SHA256},
        "p010txt_text_map": {"path": INPUT_ROOT / "page_010_text_map.md", "sha256": P010TXT_TEXT_MAP_SHA256},
        "p010txt_manifest": {"path": INPUT_ROOT / "page_010_text_extraction_manifest.md", "sha256": P010TXT_MANIFEST_SHA256},
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        if actual != item["sha256"]:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": item["path"].relative_to(ROOT).as_posix(), "sha256": actual})
    packet = json.loads((INPUT_ROOT / "page_010_text_extraction_packet.json").read_text(encoding="utf-8-sig"))
    return verified, packet


def page_inventory() -> list[dict[str, Any]]:
    return [
        {
            "region_id": "PRM-G1-VIRAL-001-P010-R01",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph", "continuation"],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P010-R02",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph", "continuation"],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P010-R03",
            "decision": "visual_only",
            "expected_unit_types": [],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P010-R04",
            "decision": "visual_only",
            "expected_unit_types": [],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P010-R05",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph", "continuation"],
        },
    ]


def build_human_review_gate() -> dict[str, Any]:
    return validate_human_review_gate(
        sol_review={
            "reviewer": "Sol",
            "status": "OK",
            "finding": "P010TXT-G1-VIRAL-001 text was accepted for semantic projection; semantic units preserve logical order, headings, paragraph boundaries, and crop linkage.",
        },
        terra_review={
            "reviewer": "Terra",
            "status": "OK",
            "finding": "Semantic map remains review material only and creates no PCRP, page-complete acceptance, source acceptance, page 011 processing, whole Gate acceptance, or push.",
        },
        human_decision={
            "decision": "p010_text_ok",
            "package_id": "P010TXT-G1-VIRAL-001",
            "source_message_id": "telegram_message_before_1561",
            "source_text": "Р010 текст ок",
            "creates_page_complete_acceptance": False,
        },
        expected_package_id="P010TXT-G1-VIRAL-001",
        allowed_decisions=["p010_text_ok"],
    )


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 010 Semantic Text Map Summary - P010SEM-G1-VIRAL-001",
            "",
            f"Status: `{report['status']}`",
            "",
            "- Records Bogdan's `p010 text ok` decision for `P010TXT-G1-VIRAL-001`.",
            "- Projects draft text into semantic units with heading levels, paragraph boundaries, crop linkage, and continuation notes.",
            "- Logical order is preserved as `B001 -> B005 -> B002 -> B006` through unit reading order.",
            "- Hyeon continuation is linked inside page 010; Peter from page 009 and Maya to page 011 are recorded as external continuation metadata.",
            "- Creates no PCRP, no page-complete acceptance, no OCR/source acceptance, no page 011 processing, and no whole Gate 1 acceptance.",
            "- Next human decision: `p010 semantic map ok` or `hold p010 semantic map: <reason>`.",
            "",
        ]
    )


def build_manifest() -> str:
    lines = [
        "# Page 010 Semantic Text Map Manifest - P010SEM-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_010_semantic_text_map_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs() -> None:
    predecessors, text_packet = verify_predecessors()
    text_consumer_gate = require_text_extraction_consumer_gate(text_packet, consumer="semantic_map")
    human_review_gate = build_human_review_gate()
    if human_review_gate["status"] != "passed":
        raise SystemExit(f"human review gate blocked: {human_review_gate['findings']}")

    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    document = semantic_map_document(
        page="010",
        package_id=PACKAGE_ID,
        map_id=MAP_ID,
        units=SEMANTIC_UNITS,
        source="P010TXT-G1-VIRAL-001",
    )
    document["text_extraction_consumer_gate"] = text_consumer_gate
    document["human_review_gate"] = human_review_gate
    document["continuation_summary"] = {
        "logical_crop_order": ["P010-B001-TES", "P010-B005-TES", "P010-B002-TES", "P010-B006-TES"],
        "external_continuations": [
            {"from": "P009/SU-P009-R-006", "to": "SU-P010-PETER-001"},
            {"from": "SU-P010-MAYA-003", "to": "P011/Maya continuation"},
        ],
        "in_page_continuations": [{"from": "SU-P010-HYEON-003", "to": "SU-P010-HYEON-004"}],
    }
    markdown = build_semantic_map_markdown(document)
    projection = validate_semantic_map_markdown(markdown, expected_unit_count=len(SEMANTIC_UNITS))
    crop_linkage = validate_text_evidence_crop_links(
        SEMANTIC_UNITS,
        {
            "P010-B001-TES": "text_evidence_crop",
            "P010-B005-TES": "text_evidence_crop",
            "P010-B002-TES": "text_evidence_crop",
            "P010-B006-TES": "text_evidence_crop",
        },
    )
    inventory = reconcile_page_inventory(page_inventory(), SEMANTIC_UNITS)
    document["markdown_projection_validation"] = projection
    document["crop_linkage_validation"] = crop_linkage
    document["inventory_reconciliation"] = inventory
    document["structural_findings"] = (
        document["semantic_validation"]["findings"] + projection["findings"] + crop_linkage["findings"] + inventory["findings"]
    )
    json_path = OUTPUT_ROOT / "page_010_semantic_text_map.json"
    markdown_path = OUTPUT_ROOT / "page_010_semantic_text_map.md"
    write_json(json_path, document)
    markdown_path.write_text(markdown, encoding="utf-8", newline="\n")
    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance",
        "predecessors": predecessors,
        "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
        "generator_script_sha256": sha256_file(SCRIPT_PATH),
        "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
        "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        "semantic_map_json_sha256": sha256_file(json_path),
        "semantic_map_markdown_sha256": sha256_file(markdown_path),
        "unit_count": len(SEMANTIC_UNITS),
        "semantic_validation": document["semantic_validation"],
        "markdown_projection_validation": projection,
        "crop_linkage_validation": crop_linkage,
        "inventory_reconciliation": inventory,
        "text_extraction_consumer_gate": text_consumer_gate,
        "human_review_gate": human_review_gate,
        "pcrp_created": False,
        "page_complete_acceptance_created": False,
        "source_acceptance_created": False,
        "ocr_acceptance_created": False,
        "whole_gate_1_acceptance_created": False,
        "pages_011_020_processing_created": False,
    }
    write_json(OUTPUT_ROOT / "page_010_semantic_text_map_report.json", report)
    (OUTPUT_ROOT / "page_010_semantic_text_map_summary.md").write_text(
        build_summary(report), encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "page_010_semantic_text_map_manifest.md").write_text(
        build_manifest(), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    write_outputs()
