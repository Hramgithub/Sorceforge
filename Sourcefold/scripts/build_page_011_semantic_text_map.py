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
SCRIPT_PATH = ROOT / "scripts" / "build_page_011_semantic_text_map.py"
TEST_PATH = ROOT / "tests" / "test_page_011_semantic_text_map.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "page_011_text_extraction_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "page_011_semantic_text_map_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-011-SEMANTIC-TEXT-MAP-001"
PACKAGE_ID = "P011SEM-G1-VIRAL-001"
MAP_ID = "SM-G1-VIRAL-P011-001"

P011TXT_PACKET_SHA256 = "EE49200061446792CAC839FA541473614AB630D4D71993DB366BFD335EB23412"
P011TXT_REPORT_SHA256 = "4DB125FCBF72A5F0F703489966B8563103C0A642BBC0EE168EF98B928C1893EE"
P011TXT_SUMMARY_SHA256 = "9D873BC246A1A0D79C0AE00A9ED7AEC157B7FF1E88E94F22E09A693E1401893B"
P011TXT_TEXT_MAP_SHA256 = "0564ABB708AEE61F6602926B67427460DE6B96167F98A2FB5F97468CF9EBCAF8"
P011TXT_MANIFEST_SHA256 = "E236D50126AF1042834B8D1A5C5FE7B447C1D8293143FE9D0E110863113FD93F"


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
    layout_role: str | None = None,
    font_style: str | None = None,
    line_break_after: bool | str | None = None,
    continues_inline_to: str | None = None,
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
        "evidence_predecessors": ["P011TXT-G1-VIRAL-001", "P011TR-G1-VIRAL-001"],
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
    if external_continues_from is not None:
        payload["external_continues_from"] = external_continues_from
    if external_continues_to is not None:
        payload["external_continues_to"] = external_continues_to
    if layout_role is not None:
        payload["layout_role"] = layout_role
    if font_style is not None:
        payload["font_style"] = font_style
    if line_break_after is not None:
        payload["line_break_after"] = line_break_after
    if continues_inline_to is not None:
        payload["continues_inline_to"] = continues_inline_to
    return payload


SEMANTIC_UNITS = [
    unit(
        unit_id="SU-P011-MAYA-001",
        unit_type="continuation",
        reading_order=1,
        text='the stream when they take a break or move location and can essentially cut the feed by doing this. She has a direct chat line to Hyeon via one of his iPads on his tech rig, but if desperate will call Marco directly. Marco often refers to Maya as "the eyes in the sky".',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_profile_body_continuation_finish",
        external_continues_from="P010/SU-P010-MAYA-003",
    ),
    unit(
        unit_id="SU-P011-MAYA-002",
        unit_type="heading",
        reading_order=2,
        text="Maya's Secrets",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_secret_box_heading",
        layout_role="block_heading",
        font_style="normal",
        line_break_after=True,
    ),
    unit(
        unit_id="SU-P011-MAYA-003",
        unit_type="paragraph",
        reading_order=3,
        text="Maya also deals and mines Crypto and does hacking in her spare time, seeing just how far she can go down the rabbit hole. She sees right through Corrina and knows in her heart of hearts that she is a phony. She has a real soft spot for Enoch and sees how troubled and kind he is.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_secret_body_paragraph",
    ),
    unit(
        unit_id="SU-P011-MAYA-004",
        unit_type="paragraph",
        reading_order=4,
        text="During her editing of Spektral Krew's videos, she has seen Peter sneaking off and faking evidence when he thinks he is not being watched. She cuts all of this out and has it stored just in case she needs something from him. She understands his reasons though - they are onto a good thing with Marco and it pays well. She found out about Isola di Malamente and did a deep-dive on it, discovering that on all of the major map sites, the island is blank and featureless, but on a forum that hacks military satellites it shows the island as being full of buildings. What are they trying to hide?",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_secret_body_paragraph",
    ),
    unit(
        unit_id="SU-P011-MAYA-005",
        unit_type="paragraph",
        reading_order=5,
        text="Although loyal to the Krew, she is not above making a quick buck or two by telling other ghost hunting teams about locations they are visiting. This irks Marco no-end, and he often wonders how rival investigative teams like the Phantom Posse and Ghost Bros manage to investigate some places before they do, never once suspecting Maya could be responsible.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_secret_body_paragraph",
    ),
    unit(
        unit_id="SU-P011-MAYA-006",
        unit_type="heading",
        reading_order=6,
        text="APPEARANCE",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_box_heading",
        layout_role="block_heading",
        font_style="normal",
        line_break_after=True,
    ),
    unit(
        unit_id="SU-P011-MAYA-007",
        unit_type="paragraph",
        reading_order=7,
        text='Before the accident, Maya stood 5\'8". She has long semi-afro/dreadlocks, a pierced nose, absolutely perfect white teeth, and is extremely smiley. She always has a t-shirt on as she rarely leaves the house and has multiple screens and workstations. She enjoys working with the Spektral Krew and helps them out on investigations by watching the feeds from the many cameras they use.',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R01",
        crop_id="P011-B001-TES",
        source_block_id="P011-B001",
        role="maya_box_body",
    ),
    unit(
        unit_id="SU-P011-EMILY-001",
        unit_type="heading",
        reading_order=8,
        text="Emily 'Em' Lavigne (NPC)",
        heading_level="h2",
        display_style="section_heading",
        block_role="title_region",
        source_region_id="PRM-G1-VIRAL-001-P011-R04",
        crop_id="P011-B004-TES",
        source_block_id="P011-B004",
        role="emily_profile_name_heading",
        layout_role="block_heading",
        font_style="normal",
        line_break_after=True,
    ),
    unit(
        unit_id="SU-P011-EMILY-002",
        unit_type="paragraph",
        reading_order=9,
        text="To either add a sense of menace or lighten up proceedings a bit, we have included an NPC - Emily 'Em' Lavigne. She has been designed to be used in two different ways. As either 'The Super Fan' or the surviving member of a rival ghost hunting group.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R04",
        crop_id="P011-B004-TES",
        source_block_id="P011-B004",
        role="emily_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P011-EMILY-003",
        unit_type="heading",
        reading_order=10,
        text="Super Fan Option.",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R04",
        crop_id="P011-B004-TES",
        source_block_id="P011-B004",
        role="emily_inline_option_heading",
        layout_role="inline_heading",
        font_style="italic",
        line_break_after=False,
        continues_inline_to="SU-P011-EMILY-004",
    ),
    unit(
        unit_id="SU-P011-EMILY-004",
        unit_type="paragraph",
        reading_order=11,
        text="Em is a stalker super fan of the channel who follows them everywhere as she is utterly obsessed with Corrina - think someone like Mel from the Flight of the Conchords TV series. Em truly believes that she is spiritually connected to Corrina in some inexplicable way. Corrina is very aware of Em, though acts aloof and pretends to forget her name. Em is ultimately attracted to Corrina beyond spiritual connection, but has not actually come to terms with her own sexuality - she is actually a closeted lesbian. On the other hand, Corrina puts on an act of being incredibly sexually free and pretends to be pan-sexual - she is actually very straight and doesn't reciprocate Em's slightly cringe-worthy advances. Em is tolerated by Marco and the Krew as she buys a lot of merchandise and endlessly promotes them on all forms of social media. She has created over 200 dummy accounts to sub to their channel and help the algorithm.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R04",
        crop_id="P011-B004-TES",
        source_block_id="P011-B004",
        role="emily_super_fan_option_body",
    ),
    unit(
        unit_id="SU-P011-EMILY-005",
        unit_type="continuation",
        reading_order=12,
        text="Em learned about the Krew investigating the island around a week ago from an anonymous tipoff - this was actually by Maya who was hedging her bets on who she could make the most cash from. She flew out to Italy immediately, stayed in Perla for a few days and paid a group of local teens to ferry",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P011-R04",
        crop_id="P011-B004-TES",
        source_block_id="P011-B004",
        role="emily_profile_body_continuation_start",
        external_continues_to="P012/Emily continuation",
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
    parser = argparse.ArgumentParser(description="Build page 011 semantic text map review artifact.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 011 semantic text map is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 011 semantic text map requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> tuple[list[dict[str, str]], dict[str, Any]]:
    verify_authorization_ledger()
    predecessors = {
        "p011txt_packet": {"path": INPUT_ROOT / "page_011_text_extraction_packet.json", "sha256": P011TXT_PACKET_SHA256},
        "p011txt_report": {"path": INPUT_ROOT / "page_011_text_extraction_report.json", "sha256": P011TXT_REPORT_SHA256},
        "p011txt_summary": {"path": INPUT_ROOT / "page_011_text_extraction_summary.md", "sha256": P011TXT_SUMMARY_SHA256},
        "p011txt_text_map": {"path": INPUT_ROOT / "page_011_text_map.md", "sha256": P011TXT_TEXT_MAP_SHA256},
        "p011txt_manifest": {"path": INPUT_ROOT / "page_011_text_extraction_manifest.md", "sha256": P011TXT_MANIFEST_SHA256},
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        if actual != item["sha256"]:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": item["path"].relative_to(ROOT).as_posix(), "sha256": actual})
    packet = json.loads((INPUT_ROOT / "page_011_text_extraction_packet.json").read_text(encoding="utf-8-sig"))
    return verified, packet


def page_inventory() -> list[dict[str, Any]]:
    return [
        {
            "region_id": "PRM-G1-VIRAL-001-P011-R01",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph", "continuation"],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P011-R02",
            "decision": "visual_only",
            "expected_unit_types": [],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P011-R03",
            "decision": "visual_only",
            "expected_unit_types": [],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P011-R04",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph", "continuation"],
        },
    ]


def build_human_review_gate() -> dict[str, Any]:
    return validate_human_review_gate(
        sol_review={
            "reviewer": "Sol",
            "status": "OK",
            "finding": "P011TXT-G1-VIRAL-001 text was accepted for semantic projection; semantic units preserve logical order, heading levels, paragraph boundaries, crop linkage, and page-continuation metadata.",
        },
        terra_review={
            "reviewer": "Terra",
            "status": "OK",
            "finding": "Semantic map remains review material only and creates no PCRP, page-complete acceptance, source acceptance, page 012 processing, whole Gate acceptance, fixture admission, or push.",
        },
        human_decision={
            "decision": "p011_text_ok",
            "package_id": "P011TXT-G1-VIRAL-001",
            "source_message_id": "1691",
            "source_text": "p011 text ok",
            "creates_page_complete_acceptance": False,
        },
        expected_package_id="P011TXT-G1-VIRAL-001",
        allowed_decisions=["p011_text_ok"],
    )


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 011 Semantic Text Map Summary - P011SEM-G1-VIRAL-001",
            "",
            f"Status: `{report['status']}`",
            "",
            "- Records Bogdan's `p011 text ok` decision for `P011TXT-G1-VIRAL-001`.",
            "- Projects draft text into semantic units with heading levels, paragraph boundaries, crop linkage, and continuation notes.",
            "- Adds universal layout/style hints where needed: block headings carry line-break metadata and the inline Emily option heading carries italic/same-line continuation metadata.",
            "- Logical order is preserved as `B001 -> B004` through unit reading order.",
            "- Maya continuation from page 010 and Emily continuation to page 012 are recorded only as external continuation metadata.",
            "- Visual-only `P011-B002` portrait and `P011-B003` screen image remain excluded from in-scope text units.",
            "- Creates no PCRP, no page-complete acceptance, no OCR/source acceptance, no page 012 processing, and no whole Gate 1 acceptance.",
            "- Next human decision: `p011 semantic map ok` or `hold p011 semantic map: <reason>`.",
            "",
        ]
    )


def build_manifest() -> str:
    lines = [
        "# Page 011 Semantic Text Map Manifest - P011SEM-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_011_semantic_text_map_manifest.md":
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
        page="011",
        package_id=PACKAGE_ID,
        map_id=MAP_ID,
        units=SEMANTIC_UNITS,
        source="P011TXT-G1-VIRAL-001",
    )
    document["text_extraction_consumer_gate"] = text_consumer_gate
    document["human_review_gate"] = human_review_gate
    document["continuation_summary"] = {
        "logical_crop_order": ["P011-B001-TES", "P011-B004-TES"],
        "external_continuations": [
            {"from": "P010/SU-P010-MAYA-003", "to": "SU-P011-MAYA-001"},
            {"from": "SU-P011-EMILY-005", "to": "P012/Emily continuation"},
        ],
        "in_page_continuations": [],
    }
    markdown = build_semantic_map_markdown(document)
    projection = validate_semantic_map_markdown(markdown, expected_unit_count=len(SEMANTIC_UNITS))
    crop_linkage = validate_text_evidence_crop_links(
        SEMANTIC_UNITS,
        {
            "P011-B001-TES": "text_evidence_crop",
            "P011-B004-TES": "text_evidence_crop",
        },
    )
    inventory = reconcile_page_inventory(page_inventory(), SEMANTIC_UNITS)
    document["markdown_projection_validation"] = projection
    document["crop_linkage_validation"] = crop_linkage
    document["inventory_reconciliation"] = inventory
    document["structural_findings"] = (
        document["semantic_validation"]["findings"] + projection["findings"] + crop_linkage["findings"] + inventory["findings"]
    )
    json_path = OUTPUT_ROOT / "page_011_semantic_text_map.json"
    markdown_path = OUTPUT_ROOT / "page_011_semantic_text_map.md"
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
        "layout_hints_created": True,
        "layout_hints_scope": "universal_optional_semantic_unit_fields",
        "pcrp_created": False,
        "page_complete_acceptance_created": False,
        "source_acceptance_created": False,
        "ocr_acceptance_created": False,
        "whole_gate_1_acceptance_created": False,
        "pages_012_020_processing_created": False,
    }
    write_json(OUTPUT_ROOT / "page_011_semantic_text_map_report.json", report)
    (OUTPUT_ROOT / "page_011_semantic_text_map_summary.md").write_text(
        build_summary(report), encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "page_011_semantic_text_map_manifest.md").write_text(
        build_manifest(), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    write_outputs()
