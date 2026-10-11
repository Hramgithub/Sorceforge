from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from page_review_semantic_units import (
    SEMANTIC_UNIT_SCHEMA_VERSION,
    SEMANTIC_UNIT_TAXONOMY_VERSION,
    build_semantic_map_markdown,
    reconcile_page_inventory,
    semantic_map_document,
    validate_semantic_map_markdown,
    validate_text_evidence_crop_links,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_009_semantic_text_map.py"
TEST_PATH = ROOT / "tests" / "test_page_009_semantic_text_map.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "page_009_text_extraction_G1_VIRAL_001"
OUTPUT_ROOT = TRIAL_ROOT / "page_009_semantic_text_map_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-009-SEMANTIC-TEXT-MAP-001"
PACKAGE_ID = "P009SEM-G1-VIRAL-001"
MAP_ID = "SM-G1-VIRAL-P009-001"

P009TXT_PACKET_SHA256 = "8980F0BD978A8B6F8D74F8F297A702B51BC040321BEE5E819EC5F40277F5402B"
P009TXT_REPORT_SHA256 = "E33F042A6CCF50A3F25B5A8F13051021A64084B827F557667D8086DC034251A1"
P009TXT_SUMMARY_SHA256 = "5C3B1A264555FA246FDFC68F4C8B1C1365EBE471EB22C02815538ECF7C724B97"
P009TXT_TEXT_MAP_SHA256 = "0F5DB5291A8F5DAE70F3EAF4757AFF0F164DB6D1D89745134A7440994841B968"
P009TXT_MANIFEST_SHA256 = "FFD29FAFCF61AA5D17ED8F865F5DB4D2E351DE9B7D6BC090F2EFC2DBA2AF96A5"


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
) -> dict[str, Any]:
    return {
        "unit_id": unit_id,
        "schema_version": SEMANTIC_UNIT_SCHEMA_VERSION,
        "taxonomy_version": SEMANTIC_UNIT_TAXONOMY_VERSION,
        "unit_type": unit_type,
        "unit_scope": "in_scope_text",
        "reading_order": reading_order,
        "source_region_ids": [source_region_id],
        "crop_ids": [crop_id],
        "evidence_predecessors": ["P009TXT-G1-VIRAL-001", "P009TR-G1-VIRAL-003"],
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


SEMANTIC_UNITS = [
    unit(
        unit_id="SU-P009-L-001",
        unit_type="heading",
        reading_order=1,
        text="Enoch Jeremiah Eakins (Investigator)",
        heading_level="h2",
        display_style="section_heading",
        block_role="title_region",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_name_heading",
    ),
    unit(
        unit_id="SU-P009-L-002",
        unit_type="paragraph",
        reading_order=2,
        text='Enoch is a former Wenger Mennonite Amish lad from Ohio who went on the Rumspringa and never returned. His community thought he was "aangeraakt door duivels" (touched by the devils), so never went looking for him (not that they do anyway).',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P009-L-003",
        unit_type="paragraph",
        reading_order=3,
        text="He is an absolute bear of a man who was hired by Marco as a bodyguard and investigator, just in case they ever get into danger with people as opposed to the supernatural, as despite being quite a kind soul, he is physically very intimidating. Enoch has a broad smile and an infectious laugh. He's actually a lot smarter than he looks and a competent investigator who picks up on things the others don't. Enoch doesn't fully understand it, but he actually has The Sight (see Appendix), though he puts a lot of what he sees down to just indulging in too much drink and drugs.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P009-L-004",
        unit_type="paragraph",
        reading_order=4,
        text="He has not told any of the Krew that he has The Sight, nor will he do so. It is his cross to bear.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P009-L-005",
        unit_type="heading",
        reading_order=5,
        text="APPEARANCE",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_box_heading",
    ),
    unit(
        unit_id="SU-P009-L-006",
        unit_type="paragraph",
        reading_order=6,
        text='Enoch (26) is a 6\'6" mountain of a man. Always wears a plain white button up shirt and blue jeans along with open-toed sandals (even in the snow) and a Spektral Krew branded baseball cap. He has a full beard and kind blue eyes. Has a fairly awful scar down one side of his face due to a farming implement accident when he was younger. Courteous to a tee and genuinely well liked by all of the Krew.',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_box_body",
    ),
    unit(
        unit_id="SU-P009-L-007",
        unit_type="heading",
        reading_order=7,
        text="GEAR CARRIED",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_box_heading",
    ),
    unit(
        unit_id="SU-P009-L-008",
        unit_type="paragraph",
        reading_order=8,
        text="Spektral Krew(TM) Satchel, Glowsticks (20), Wi-Fi Repeaters (2), Static Night Vision Cameras (6)",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R03",
        crop_id="P009-B003-TEXT-EVIDENCE",
        source_block_id="P009-B003",
        role="left_profile_box_body",
    ),
    unit(
        unit_id="SU-P009-R-001",
        unit_type="heading",
        reading_order=9,
        text="Peter Wharton (Investigator)",
        heading_level="h2",
        display_style="section_heading",
        block_role="title_region",
        source_region_id="PRM-G1-VIRAL-001-P009-R04",
        crop_id="P009-B004-TEXT-EVIDENCE",
        source_block_id="P009-B004",
        role="right_profile_name_heading",
    ),
    unit(
        unit_id="SU-P009-R-002",
        unit_type="paragraph",
        reading_order=10,
        text="Peter is a career criminal and former heroin addict who fell into his current job as cameraman for Spektral Krew when he went to sell a stolen laptop and digital camera to Marco.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R04",
        crop_id="P009-B004-TEXT-EVIDENCE",
        source_block_id="P009-B004",
        role="right_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P009-R-003",
        unit_type="paragraph",
        reading_order=11,
        text="He had bought and sold so many of these over the years that when asked by Marco to demonstrate how it worked, he easily understood what to do, and Marco offered him a job on the spot which he accepted as nobody had ever done that for him before. In order to keep the cash flowing, for Spektral Krew and thus himself, he secretly sets up fake evidence and triggers it at opportune moments during the investigations - using things like fishing line to move things off camera, palming small objects and leaving them in other places, then spotting them with shock on his face, leaving superchat messages on the stream pointing out his 'activity' using a false account, and the like. Peter's player should be encouraged to be inventive with his fake evidence, as well as making sure he doesn't get caught.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R04",
        crop_id="P009-B004-TEXT-EVIDENCE",
        source_block_id="P009-B004",
        role="right_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P009-R-004",
        unit_type="paragraph",
        reading_order=12,
        text="Peter is a man of few words and although appreciative of his job, he is always looking for the next thing to steal as it is a habit for him (he is a borderline kleptomaniac). Not easily phased. Likes Enoch as he sees him as a bit of a kindred spirit.",
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R04",
        crop_id="P009-B004-TEXT-EVIDENCE",
        source_block_id="P009-B004",
        role="right_profile_body_paragraph",
    ),
    unit(
        unit_id="SU-P009-R-005",
        unit_type="heading",
        reading_order=13,
        text="APPEARANCE",
        heading_level="h3",
        display_style="section_heading",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R04",
        crop_id="P009-B004-TEXT-EVIDENCE",
        source_block_id="P009-B004",
        role="right_profile_box_heading",
    ),
    unit(
        unit_id="SU-P009-R-006",
        unit_type="paragraph",
        reading_order=14,
        text='Peter (39) is 5\'9" and rakishly thin with slightly unkempt hair. Has a stubble covered face, with darting eyes and a hand-rolled cigarette always hanging off his lip. Wears a pair of Doc Martens',
        heading_level=None,
        display_style="body",
        block_role="text_column",
        source_region_id="PRM-G1-VIRAL-001-P009-R04",
        crop_id="P009-B004-TEXT-EVIDENCE",
        source_block_id="P009-B004",
        role="right_profile_box_body",
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
    parser = argparse.ArgumentParser(description="Build page 009 semantic text map review artifact.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 009 semantic text map is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 009 semantic text map requires {AUTHORIZATION_ID}")


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_predecessors() -> list[dict[str, str]]:
    verify_authorization_ledger()
    predecessors = {
        "p009txt_packet": {"path": INPUT_ROOT / "page_009_text_extraction_packet.json", "sha256": P009TXT_PACKET_SHA256},
        "p009txt_report": {"path": INPUT_ROOT / "page_009_text_extraction_report.json", "sha256": P009TXT_REPORT_SHA256},
        "p009txt_summary": {"path": INPUT_ROOT / "page_009_text_extraction_summary.md", "sha256": P009TXT_SUMMARY_SHA256},
        "p009txt_text_map": {"path": INPUT_ROOT / "page_009_text_map.md", "sha256": P009TXT_TEXT_MAP_SHA256},
        "p009txt_manifest": {"path": INPUT_ROOT / "page_009_text_extraction_manifest.md", "sha256": P009TXT_MANIFEST_SHA256},
    }
    verified = []
    for name, item in predecessors.items():
        actual = sha256_file(item["path"])
        if actual != item["sha256"]:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": item["path"].relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


def page_inventory() -> list[dict[str, Any]]:
    return [
        {
            "region_id": "PRM-G1-VIRAL-001-P009-R03",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph"],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P009-R04",
            "decision": "represented",
            "expected_unit_types": ["heading", "paragraph"],
        },
    ]


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page 009 Semantic Text Map Summary - P009SEM-G1-VIRAL-001",
            "",
            f"Status: `{report['status']}`",
            "",
            "- Builds a semantic text map from `P009TXT-G1-VIRAL-001`.",
            "- Splits headings, body paragraphs, APPEARANCE, and GEAR CARRIED into ordered semantic units.",
            "- Records heading levels and links every unit to a `text_evidence` crop id.",
            "- Creates no PCRP, no page-complete acceptance, no OCR/source acceptance, and no whole Gate 1 acceptance.",
            "- Next human decision: `p009 semantic map ok` or `hold p009 semantic map: <reason>`.",
            "",
        ]
    )


def build_manifest() -> str:
    lines = [
        "# Page 009 Semantic Text Map Manifest - P009SEM-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUTPUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "page_009_semantic_text_map_manifest.md":
            lines.append(f"| `{path.relative_to(OUTPUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs() -> None:
    predecessors = verify_predecessors()
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    document = semantic_map_document(
        page="009",
        package_id=PACKAGE_ID,
        map_id=MAP_ID,
        units=SEMANTIC_UNITS,
        source="P009TXT-G1-VIRAL-001",
    )
    markdown = build_semantic_map_markdown(document)
    projection = validate_semantic_map_markdown(markdown, expected_unit_count=len(SEMANTIC_UNITS))
    crop_linkage = validate_text_evidence_crop_links(
        SEMANTIC_UNITS,
        {"P009-B003-TEXT-EVIDENCE": "text_evidence_crop", "P009-B004-TEXT-EVIDENCE": "text_evidence_crop"},
    )
    inventory = reconcile_page_inventory(page_inventory(), SEMANTIC_UNITS)
    document["markdown_projection_validation"] = projection
    document["crop_linkage_validation"] = crop_linkage
    document["inventory_reconciliation"] = inventory
    document["structural_findings"] = (
        document["semantic_validation"]["findings"] + projection["findings"] + crop_linkage["findings"] + inventory["findings"]
    )
    json_path = OUTPUT_ROOT / "page_009_semantic_text_map.json"
    markdown_path = OUTPUT_ROOT / "page_009_semantic_text_map.md"
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
        "pcrp_created": False,
        "page_complete_acceptance_created": False,
        "source_acceptance_created": False,
        "ocr_acceptance_created": False,
        "whole_gate_1_acceptance_created": False,
    }
    write_json(OUTPUT_ROOT / "page_009_semantic_text_map_report.json", report)
    (OUTPUT_ROOT / "page_009_semantic_text_map_summary.md").write_text(
        build_summary(report), encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "page_009_semantic_text_map_manifest.md").write_text(
        build_manifest(), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    write_outputs()
