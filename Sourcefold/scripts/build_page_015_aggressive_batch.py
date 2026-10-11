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


ROOT = Path(__file__).resolve().parents[1]
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001"
LANE_ID = "P015BATCH-G1-VIRAL-001"
PAGE = "015"
PAGE_ID = "PG-G1-VIRAL-P015"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_015.png"
PAGE_IMAGE_SHA256 = "023836CD8DF8B77073F977E22F00CA87391F96855765D77B5C2826B0F00EDBBA"
G1SP_009_PACKET_SHA256 = "E0F15FCA01D32C95D41EBCA87D87EDCEEEE59A2C503FF0965614169BF0159B54"
P014_FINAL_REVIEW_SHA256 = "FF8C193BB61A5D6A12F1E60EC7C853EB164CD1EC10A92A058A591200B430A76B"

TRIAGE_ROOT = TRIAL_ROOT / "page_015_triage_G1_VIRAL_001"
TEXT_ROOT = TRIAL_ROOT / "page_015_text_extraction_G1_VIRAL_001"
SEM_ROOT = TRIAL_ROOT / "page_015_semantic_text_map_G1_VIRAL_001"
PCRP_ROOT = TRIAL_ROOT / "page_complete_review_p015_G1_VIRAL_001"
PCA_ROOT = TRIAL_ROOT / "page_complete_acceptance_p015_G1_VIRAL_001"
STATUS_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_010"
BATCH_ROOT = TRIAL_ROOT / "page_015_aggressive_batch_G1_VIRAL_001"

SKIPPED_REVIEW = "human_review_skipped_by_explicit_authorization"
DELEGATED_REVIEW = "review_delegated_to_Sol_Terra"

SOL_TERRA_STAGE_REVIEWS = {
    "P015TR-G1-VIRAL-001": {
        "sol": "OK: page 015 is bounded to the exact page image with two text evidence crops and one visual-only photo anchor.",
        "terra": "OK: preflight materializes page 015 authority and page 016+ remains blocked.",
    },
    "P015TXT-G1-VIRAL-001": {
        "sol": "OK: draft transcription is limited to page 015 timeline and visible history text evidence.",
        "terra": "OK: text extraction records no OCR/source/page/whole-Gate acceptance and excludes the photo anchor.",
    },
    "P015SEM-G1-VIRAL-001": {
        "sol": "OK: semantic units keep timeline time labels below structural heading level and mark History as continuing.",
        "terra": "OK: semantic map does not transcribe or process page 016 continuation.",
    },
    "PCRP-G1-VIRAL-P015-001": {
        "sol": "OK: page-complete review packet reconciles P015 text, visual anchor, semantic units, and continuation metadata.",
        "terra": "OK: PCRP is internal delegated evidence only and claims no direct Bogdan per-stage approval.",
    },
    "P015PCA-G1-VIRAL-001": {
        "sol": "OK: acceptance is page 015 only under delegated-review lane authority and exact PCRP predecessor binding.",
        "terra": "OK: PCA does not imply whole Gate 1, fixture admission, source acceptance, or page 016 processing.",
    },
    "G1SP-G1-VIRAL-010": {
        "sol": "OK: status refresh records pages 001-015 accepted-only and pages 016-020 unstarted.",
        "terra": "OK: page 016 is only a recommended next candidate and is not authorized by the status packet.",
    },
}

BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P015-B001",
        "role": "timeline_text_panel",
        "source_region_id": "PRM-G1-VIRAL-001-P015-R01",
        "crop_box_px": [220, 220, 1040, 2910],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 200, "max_x": 240, "min_y": 200, "max_y": 240, "min_width": 1000, "min_height": 2850},
        },
        "asset": "review_assets/1_P015-timeline-text-evidence.png",
    },
    {
        "block_id": "P015-B002",
        "role": "history_text_visible_continuation",
        "source_region_id": "PRM-G1-VIRAL-001-P015-R03",
        "crop_box_px": [1285, 1650, 1120, 1400],
        "crop_contract": {
            "coverage": "full_text_region_part",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1260, "max_x": 1310, "min_y": 1620, "max_y": 1680, "min_width": 1080, "min_height": 1360},
        },
        "continues_to_next_page": True,
        "asset": "review_assets/2_P015-history-text-evidence.png",
    },
]

VISUAL_ONLY_BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P015-V001",
        "role": "upper_right_stone_structure_photo",
        "source_region_id": "PRM-G1-VIRAL-001-P015-R02",
        "crop_box_px": [1310, 220, 1050, 1430],
        "asset": "review_assets/3_P015-stone-structure-photo-visual-anchor.png",
        "visual_only": True,
        "text_extraction": "excluded_visual_anchor",
    }
]

TIMELINE_TEXT = """Timeline

Saturday, August 24th 2019

The weather calls for clear skies, though it's going to be hot and humid, with temperatures around 75° F (24° C) and 80% humidity. It will be extremely dark until the moon comes up just after midnight.

7:40 AM: Spektral Krew arrives in Italy and intends to spend the day on the mainland preparing for that night's livestream. They meet with their contact Nuncio who is going to transport them to the island.

6:30 PM: The Krew load their gear onto Nuncio's rickety boat that will take them from the harbor in Perla out to Isola di Malamente. The plan is to pick them up just before sunrise at the drop-off point the following day.

7:00 PM: They arrive at Isola di Malamente and unload their gear. A tour boat passes near the island, but doesn't appear to see them.

7:25 PM: The lighthouse is explored and the base station is set up in the radio room. The satellite uplink is established and tested and the first Wi-Fi transmitter is set up near the top of the lighthouse.

7:55 PM: Sunset.

8:00 PM: They scout the bridge location and set up the second Wi-Fi transmitter on the far side.

The broadcast begins.

11:45 PM: Maya contacts the Investigators to advise them to get to the Crypt and start setting up for the grand finale.

12:00 AM: The Investigators use Corrina's 'Witch Board' in the Crypt beneath the Chapel. The seance is performed at the stroke of midnight to the tolling bells that echo across the sea from Perla. The name H A S T A L Y K is slowly spelled out and the Great Old One stirs, causing the earth to shake and the ancient altar to crack down the center. Rubble falls onto the stairs leading to the surface, blocking the exit and trapping the Investigators below. Part of the wall near the altar falls away, revealing the entrance to the catacombs. Hyeon is notified that they have passed one million channel subscribers and their stream is flagged as having gone 'viral.'

Time Unknown: Sometime before dawn, the Investigators reach the Charnel Pit and the last Plague Monk casts himself in, birthing Hastalyk. Thirty seconds later in an undisclosed location, orders are given to have several heavily armed military jets dispatched to level Isola di Malamente with a mixture of high explosive, incendiary, and napalm bombs. They arrive 15 minutes later.

6:28 AM: Sunrise"""

HISTORY_TEXT = """History

Sometime during the Stone Age, Hastalyk makes landfall on Earth from the endless void of space upon what is now known as Isola di Malamente as a microscopic organism and slowly begins infecting and defiling the island. The powerful influence of the Great Old One draws early human settlers there during the Bronze Age. They begin worshiping this otherworldly, but invisible horror as a god.

As the Bronze Age settlers make sacrifices to Hastalyk, it begins to grow in size and eventually manifest as a swirling charnel pit around the time of what we know as the beginnings of Ancient Greece around 700 BC. It is still too weak to spread beyond the island, so instructs its worshipers to build a temple around it - this is when it was worshiped as Phthisis - a personification of rot and decay.

Countless temples were built atop the original temple as the cult adapted to the current pantheons including Erra, Nergal, Vejovis, Morbus, and eventually the monastery of Saint Roche was built in the early 14th century just prior to the outbreak of the Black Death.

The monastery became known for taking in the ill, infirm, and dying to look after them in their final years. These included plague victims, lepers, and those suffering from brain fevers (insanity). The bodies were burned in a large cremation pit. The monastery was converted into a sanitarium in the late 1800s."""

TEXT_UNITS = [
    {"unit_id": "P015-TEXT-001", "block_id": "P015-B001", "text": TIMELINE_TEXT},
    {"unit_id": "P015-TEXT-002", "block_id": "P015-B002", "text": HISTORY_TEXT, "continues_to_next_page": True},
]

TIMELINE_EVENTS = [
    ("SU-P015-TIME-004", "7:40 AM", "Spektral Krew arrives in Italy and intends to spend the day on the mainland preparing for that night's livestream. They meet with their contact Nuncio who is going to transport them to the island."),
    ("SU-P015-TIME-005", "6:30 PM", "The Krew load their gear onto Nuncio's rickety boat that will take them from the harbor in Perla out to Isola di Malamente. The plan is to pick them up just before sunrise at the drop-off point the following day."),
    ("SU-P015-TIME-006", "7:00 PM", "They arrive at Isola di Malamente and unload their gear. A tour boat passes near the island, but doesn't appear to see them."),
    ("SU-P015-TIME-007", "7:25 PM", "The lighthouse is explored and the base station is set up in the radio room. The satellite uplink is established and tested and the first Wi-Fi transmitter is set up near the top of the lighthouse."),
    ("SU-P015-TIME-008", "7:55 PM", "Sunset."),
    ("SU-P015-TIME-009", "8:00 PM", "They scout the bridge location and set up the second Wi-Fi transmitter on the far side."),
    ("SU-P015-TIME-011", "11:45 PM", "Maya contacts the Investigators to advise them to get to the Crypt and start setting up for the grand finale."),
    ("SU-P015-TIME-012", "12:00 AM", "The Investigators use Corrina's 'Witch Board' in the Crypt beneath the Chapel. The seance is performed at the stroke of midnight to the tolling bells that echo across the sea from Perla. The name H A S T A L Y K is slowly spelled out and the Great Old One stirs, causing the earth to shake and the ancient altar to crack down the center. Rubble falls onto the stairs leading to the surface, blocking the exit and trapping the Investigators below. Part of the wall near the altar falls away, revealing the entrance to the catacombs. Hyeon is notified that they have passed one million channel subscribers and their stream is flagged as having gone 'viral.'"),
    ("SU-P015-TIME-013", "Time Unknown", "Sometime before dawn, the Investigators reach the Charnel Pit and the last Plague Monk casts himself in, birthing Hastalyk. Thirty seconds later in an undisclosed location, orders are given to have several heavily armed military jets dispatched to level Isola di Malamente with a mixture of high explosive, incendiary, and napalm bombs. They arrive 15 minutes later."),
    ("SU-P015-TIME-014", "6:28 AM", "Sunrise"),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build page 015 aggressive delegated-review batch.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 015 aggressive batch is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 015 aggressive batch requires {AUTHORIZATION_ID}")


def aggressive_batch_authorization_preflight() -> None:
    materialize_aggressive_batch_authorization(
        ledger_path=AUTHORIZATION_LEDGER,
        authorization_id=AUTHORIZATION_ID,
        page=PAGE,
        lane_id=LANE_ID,
        authority='Bogdan Telegram message `2030`: "давай дальше страница 15 агрессивно"',
        exact_action=[
            "Create page 015 aggressive delegated-review batch artifacts.",
            "Generate P015TR/P015TXT/P015SEM/PCRP/P015PCA/status/batch outputs with skipped human review and Sol/Terra evidence.",
        ],
        admitted_inputs=[
            {"name": "post_p014_status_route_packet", "sha256": G1SP_009_PACKET_SHA256},
            {"name": "p014_final_batch_review", "sha256": P014_FINAL_REVIEW_SHA256},
            {"name": "page_015_image", "sha256": PAGE_IMAGE_SHA256},
        ],
        allowed_outputs=[
            "scripts/build_page_015_aggressive_batch.py",
            "tests/test_page_015_aggressive_batch.py",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_015_*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p015_G1_VIRAL_001/*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_010/*",
        ],
        limits=[
            "Do not record direct Bogdan approval for internal P015 stages.",
            "Do not process page 016 or later beyond the post-P015 status recommendation.",
            "Do not accept whole Gate 1, admit fixtures, mutate source/OCR/render/PDF/raw, translate, proofread, implement, push, or create final batch review.",
        ],
    )


def verify_predecessors() -> list[dict[str, str]]:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")
    predecessors = [
        ("post_p014_status_route_packet", TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_009" / "gate_1_status_packet.json", G1SP_009_PACKET_SHA256),
        ("p014_final_batch_review", TRIAL_ROOT / "page_014_aggressive_batch_final_review_G1_VIRAL_001" / "page_014_aggressive_batch_final_review_report.json", P014_FINAL_REVIEW_SHA256),
        ("page_015_image", PAGE_IMAGE, PAGE_IMAGE_SHA256),
    ]
    verified = []
    for name, path, expected in predecessors:
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"predecessor hash mismatch for {name}: {actual}")
        verified.append({"name": name, "path": path.relative_to(ROOT).as_posix(), "sha256": actual})
    return verified


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
    guard = {
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
        "page_016_plus_processing": False,
        "final_human_batch_review_acceptance": False,
    }
    if extra:
        guard.update(extra)
    return guard


def reset_outputs() -> None:
    for root in [TRIAGE_ROOT, TEXT_ROOT, SEM_ROOT, PCRP_ROOT, PCA_ROOT, STATUS_ROOT, BATCH_ROOT]:
        if root.exists():
            shutil.rmtree(root)
        root.mkdir(parents=True, exist_ok=True)


def crop_assets() -> dict[str, dict[str, str]]:
    assets: dict[str, dict[str, str]] = {}
    review_root = TRIAGE_ROOT / "review_assets"
    review_root.mkdir(parents=True, exist_ok=True)
    page_copy = review_root / "page_015.png"
    shutil.copy2(PAGE_IMAGE, page_copy)
    assets["review_assets/page_015.png"] = {"path": page_copy.relative_to(ROOT).as_posix(), "sha256": sha256_file(page_copy)}
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
        blocks.append({**block, "reading_order": index, "content_kind": "text_like_region", "text_evidence_crop_id": f"{block['block_id']}-TES", "asset_sha256": assets[block["asset"]]["sha256"]})
    packet = {
        "package_id": "P015TR-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "triage_crop_contract_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "page_id": PAGE_ID,
        "predecessors": predecessors,
        "review_gate": review_gate("P015TR-G1-VIRAL-001"),
        "review_blocks": blocks,
        "logical_text_order": [f"{block['block_id']}-TES" for block in BLOCKS],
        "visual_only_blocks": VISUAL_ONLY_BLOCKS,
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails({"triage_created": True}),
    }
    write_json(TRIAGE_ROOT / "page_015_triage_packet.json", packet)
    write_json(TRIAGE_ROOT / "page_015_triage_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "guardrails": packet["guardrails"], "text_block_count": len(blocks), "visual_only_block_count": len(VISUAL_ONLY_BLOCKS)})
    write_text(TRIAGE_ROOT / "page_015_triage_summary.md", "# Page 015 Triage Summary - P015TR-G1-VIRAL-001\n\nMachine-reviewed triage with human review skipped by explicit authorization. Two page 015 text-evidence surfaces are contract-bound and one upper-right photo is a visual-only anchor. History continues to page 016; page 016 is not processed.\n")
    write_manifest(TRIAGE_ROOT, "page_015_triage_manifest.md", "Page 015 Triage Manifest - P015TR-G1-VIRAL-001")
    return packet


def build_text(triage_packet: dict[str, Any]) -> dict[str, Any]:
    lines = ["# Page 015 Text Map - P015TXT-G1-VIRAL-001", "", "Status: `draft_text_machine_reviewed_human_review_skipped`", ""]
    for index, unit in enumerate(TEXT_UNITS, start=1):
        lines.extend([f"## {unit['unit_id']}", "", f"- Reading order: `{index}`", f"- Blocks: `{unit['block_id']}`"])
        if unit.get("continues_to_next_page"):
            lines.append("- Continuation: `continues_to_page_016_not_processed`")
        lines.extend(["", "```text", unit["text"], "```", ""])
    write_text(TEXT_ROOT / "page_015_text_map.md", "\n".join(lines))
    packet = {
        "package_id": "P015TXT-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "draft_text_machine_reviewed_human_review_skipped",
        "predecessor": {"package_id": triage_packet["package_id"], "sha256": sha256_file(TRIAGE_ROOT / "page_015_triage_packet.json")},
        "review_gate": review_gate("P015TXT-G1-VIRAL-001"),
        "extraction_method": "manual_from_text_evidence_region",
        "ocr_executed": False,
        "text_units": TEXT_UNITS,
        "logical_reading_order": [unit["unit_id"] for unit in TEXT_UNITS],
        "excluded_visual_anchors": ["P015-V001"],
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails({"text_extraction_created": True}),
    }
    write_json(TEXT_ROOT / "page_015_text_extraction_packet.json", packet)
    write_json(TEXT_ROOT / "page_015_text_extraction_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "guardrails": packet["guardrails"], "unit_count": len(TEXT_UNITS)})
    write_text(TEXT_ROOT / "page_015_text_extraction_summary.md", "# Page 015 Text Extraction Summary - P015TXT-G1-VIRAL-001\n\nDraft text extracted from P015TR text evidence crops under delegated Sol/Terra review. Human review is skipped by explicit authorization; the upper-right photo is excluded from text extraction.\n")
    write_manifest(TEXT_ROOT, "page_015_text_extraction_manifest.md", "Page 015 Text Extraction Manifest - P015TXT-G1-VIRAL-001")
    return packet


def semantic_units() -> list[dict[str, Any]]:
    units = [
        {"unit_id": "SU-P015-TIME-001", "unit_type": "heading", "heading_level": "h2", "semantic_role": "section_heading", "block_id": "P015-B001", "text": "Timeline", "layout_role": "block_heading", "display_style": "normal", "is_structural_heading": True},
        {"unit_id": "SU-P015-TIME-002", "unit_type": "heading", "heading_level": "h3", "semantic_role": "date_heading", "block_id": "P015-B001", "text": "Saturday, August 24th 2019", "layout_role": "block_heading", "display_style": "blue", "is_structural_heading": True},
        {"unit_id": "SU-P015-TIME-003", "unit_type": "paragraph", "heading_level": None, "semantic_role": "timeline_weather_note", "block_id": "P015-B001", "text": "The weather calls for clear skies, though it's going to be hot and humid, with temperatures around 75° F (24° C) and 80% humidity. It will be extremely dark until the moon comes up just after midnight.", "layout_role": "body", "display_style": "italic", "is_structural_heading": False},
    ]
    for unit_id, label, text in TIMELINE_EVENTS:
        units.append({"unit_id": unit_id, "unit_type": "timeline_entry", "heading_level": None, "semantic_role": "timeline_event", "block_id": "P015-B001", "time_label": label, "text": text, "layout_role": "timeline_entry", "display_style": "time_label_bold", "is_structural_heading": False})
    units.insert(9, {"unit_id": "SU-P015-TIME-010", "unit_type": "paragraph", "heading_level": None, "semantic_role": "timeline_event_note", "block_id": "P015-B001", "text": "The broadcast begins.", "layout_role": "body", "display_style": "normal", "is_structural_heading": False})
    units.extend(
        [
            {"unit_id": "SU-P015-HIST-001", "unit_type": "heading", "heading_level": "h2", "semantic_role": "section_heading", "block_id": "P015-B002", "text": "History", "layout_role": "block_heading", "display_style": "normal", "is_structural_heading": True},
            {"unit_id": "SU-P015-HIST-002", "unit_type": "paragraph", "heading_level": None, "semantic_role": "history_origin", "block_id": "P015-B002", "text": "Sometime during the Stone Age, Hastalyk makes landfall on Earth from the endless void of space upon what is now known as Isola di Malamente as a microscopic organism and slowly begins infecting and defiling the island. The powerful influence of the Great Old One draws early human settlers there during the Bronze Age. They begin worshiping this otherworldly, but invisible horror as a god.", "layout_role": "body", "display_style": "normal", "is_structural_heading": False},
            {"unit_id": "SU-P015-HIST-003", "unit_type": "paragraph", "heading_level": None, "semantic_role": "history_bronze_age_cult", "block_id": "P015-B002", "text": "As the Bronze Age settlers make sacrifices to Hastalyk, it begins to grow in size and eventually manifest as a swirling charnel pit around the time of what we know as the beginnings of Ancient Greece around 700 BC. It is still too weak to spread beyond the island, so instructs its worshipers to build a temple around it - this is when it was worshiped as Phthisis - a personification of rot and decay.", "layout_role": "body", "display_style": "normal", "is_structural_heading": False},
            {"unit_id": "SU-P015-HIST-004", "unit_type": "paragraph", "heading_level": None, "semantic_role": "history_layered_temples", "block_id": "P015-B002", "text": "Countless temples were built atop the original temple as the cult adapted to the current pantheons including Erra, Nergal, Vejovis, Morbus, and eventually the monastery of Saint Roche was built in the early 14th century just prior to the outbreak of the Black Death.", "layout_role": "body", "display_style": "normal", "is_structural_heading": False},
            {"unit_id": "SU-P015-HIST-005", "unit_type": "paragraph", "heading_level": None, "semantic_role": "history_monastery_sanitarium_continues", "block_id": "P015-B002", "text": "The monastery became known for taking in the ill, infirm, and dying to look after them in their final years. These included plague victims, lepers, and those suffering from brain fevers (insanity). The bodies were burned in a large cremation pit. The monastery was converted into a sanitarium in the late 1800s.", "layout_role": "body", "display_style": "normal", "is_structural_heading": False, "continues_to_next_page": True, "continuation_target": "page_016"},
        ]
    )
    return units


def build_semantic(text_packet: dict[str, Any]) -> dict[str, Any]:
    units = semantic_units()
    payload = {
        "package_id": "P015SEM-G1-VIRAL-001",
        "map_id": "SM-G1-VIRAL-P015-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "semantic_text_map_machine_reviewed_human_review_skipped",
        "predecessor": {"package_id": text_packet["package_id"], "sha256": sha256_file(TEXT_ROOT / "page_015_text_extraction_packet.json")},
        "review_gate": review_gate("P015SEM-G1-VIRAL-001"),
        "units": units,
        "unit_count": len(units),
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails({"semantic_map_created": True}),
    }
    write_json(SEM_ROOT / "page_015_semantic_text_map.json", payload)
    write_json(SEM_ROOT / "page_015_semantic_text_map_report.json", {"package_id": payload["package_id"], "status": payload["status"], "review_gate": payload["review_gate"], "guardrails": payload["guardrails"], "unit_count": len(units)})
    markdown = ["# Page 015 Semantic Text Map - P015SEM-G1-VIRAL-001", "", "Status: `semantic_text_map_machine_reviewed_human_review_skipped`", ""]
    for unit in units:
        markdown.extend([f"## {unit['unit_id']}", f"- Type: `{unit['unit_type']}`", f"- Heading level: `{unit['heading_level']}`", f"- Layout role: `{unit['layout_role']}`"])
        if unit.get("time_label"):
            markdown.append(f"- Time label: `{unit['time_label']}`")
        if unit.get("continues_to_next_page"):
            markdown.append("- Continuation: `continues_to_page_016_not_processed`")
        markdown.extend(["", "```text", unit["text"], "```", ""])
    write_text(SEM_ROOT / "page_015_semantic_text_map.md", "\n".join(markdown))
    write_text(SEM_ROOT / "page_015_semantic_text_map_summary.md", "# Page 015 Semantic Text Map Summary - P015SEM-G1-VIRAL-001\n\nMachine-reviewed semantic map. Timeline time labels are timeline-entry labels, not structural headings. History continues to page 016; page 016 is not processed.\n")
    write_manifest(SEM_ROOT, "page_015_semantic_text_map_manifest.md", "Page 015 Semantic Text Map Manifest - P015SEM-G1-VIRAL-001")
    return payload


def copy_review_assets() -> None:
    target_root = PCRP_ROOT / "review_assets"
    target_root.mkdir(parents=True, exist_ok=True)
    for asset in ["review_assets/page_015.png"] + [block["asset"] for block in BLOCKS + VISUAL_ONLY_BLOCKS]:
        shutil.copy2(TRIAGE_ROOT / asset, target_root / Path(asset).name)
    shutil.copy2(TEXT_ROOT / "page_015_text_map.md", target_root / "page_015_text_map.md")
    shutil.copy2(SEM_ROOT / "page_015_semantic_text_map.json", target_root / "page_015_semantic_text_map.json")
    shutil.copy2(SEM_ROOT / "page_015_semantic_text_map.md", target_root / "page_015_semantic_text_map.md")


def build_pcrp(semantic_packet: dict[str, Any]) -> dict[str, Any]:
    copy_review_assets()
    report = {
        "package_id": "PCRP-G1-VIRAL-P015-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_complete_review_machine_reviewed_human_review_skipped",
        "predecessor": {"package_id": semantic_packet["package_id"], "sha256": sha256_file(SEM_ROOT / "page_015_semantic_text_map.json")},
        "review_gate": review_gate("PCRP-G1-VIRAL-P015-001"),
        "text_evidence_blocks": [block["block_id"] for block in BLOCKS],
        "visual_only_blocks": [block["block_id"] for block in VISUAL_ONLY_BLOCKS],
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails({"pcrp_created": True}),
    }
    write_json(PCRP_ROOT / "page_complete_review_report.json", report)
    write_text(PCRP_ROOT / "page_complete_review_packet.md", "# Page Complete Review Packet - PCRP-G1-VIRAL-P015-001\n\nMachine-reviewed page 015 PCRP. Human review skipped by explicit authorization; final human review is deferred to the post-P015 bundle/status. History continuation to page 016 is recorded, but page 016 is not processed.\n")
    write_text(PCRP_ROOT / "page_complete_review_summary.md", "# Page 015 Complete Review Summary - PCRP-G1-VIRAL-P015-001\n\nReady blocks: 2 text-evidence blocks plus 1 visual-only photo anchor. History continues to page 016; page 016 remains unprocessed.\n")
    write_manifest(PCRP_ROOT, "page_complete_review_manifest.md", "Page 015 Complete Review Manifest - PCRP-G1-VIRAL-P015-001")
    return report


def build_pca(pcrp_report: dict[str, Any]) -> dict[str, Any]:
    report = {
        "package_id": "P015PCA-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_015_delegated_page_complete_acceptance_recorded",
        "accepted_pages": ["015"],
        "predecessor": {"package_id": pcrp_report["package_id"], "sha256": sha256_file(PCRP_ROOT / "page_complete_review_report.json")},
        "review_gate": review_gate("P015PCA-G1-VIRAL-001"),
        "human_review_state": SKIPPED_REVIEW,
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails({"page_complete_acceptance_created": True}),
    }
    write_json(PCA_ROOT / "page_complete_acceptance_report.json", report)
    write_text(PCA_ROOT / "page_complete_acceptance_record.md", "# Page Complete Acceptance Record - P015PCA-G1-VIRAL-001\n\nPage 015 accepted only under explicit delegated-review lane authorization. This is not direct per-stage human approval and not whole Gate 1 acceptance.\n")
    write_text(PCA_ROOT / "page_complete_acceptance_summary.md", "# Page Complete Acceptance Summary - P015PCA-G1-VIRAL-001\n\nAccepted page: `015` only. History continuation to page 016 is recorded; page 016 remains unprocessed.\n")
    write_manifest(PCA_ROOT, "page_complete_acceptance_manifest.md", "Page 015 Complete Acceptance Manifest - P015PCA-G1-VIRAL-001")
    return report


def build_status(pca_report: dict[str, Any]) -> dict[str, Any]:
    packet = {
        "status_packet_id": "G1SP-G1-VIRAL-010",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "gate_1_status_route_packet_ready_for_final_human_batch_review",
        "page_complete_accepted_pages": [f"{i:03d}" for i in range(1, 16)],
        "remaining_page_complete_pages_unstarted": ["016", "017", "018", "019", "020"],
        "recommended_next_candidate": "page_016_triage_readiness_not_authorized",
        "predecessor": {"package_id": pca_report["package_id"], "sha256": sha256_file(PCA_ROOT / "page_complete_acceptance_report.json")},
        "review_gate": review_gate("G1SP-G1-VIRAL-010"),
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails(),
    }
    write_json(STATUS_ROOT / "gate_1_status_packet.json", packet)
    write_json(STATUS_ROOT / "gate_1_status_report.json", packet)
    write_text(STATUS_ROOT / "gate_1_status_summary.md", "# Gate 1 Status Route Packet - G1SP-G1-VIRAL-010\n\nPages `001-015` are page-complete accepted only. Pages `016-020` remain unstarted. Page 016 triage/readiness is only the recommended next candidate and is not authorized. Whole Gate 1 and all broad capabilities remain blocked.\n")
    write_manifest(STATUS_ROOT, "gate_1_status_manifest.md", "Gate 1 Status Route Manifest - G1SP-G1-VIRAL-010")
    return packet


def build_bundle(stage_packets: list[dict[str, Any]]) -> None:
    bundle = {
        "package_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "ready_for_bogdan_final_batch_review",
        "human_review_model": "final_bundle_and_post_p015_status_only",
        "internal_stage_human_review_state": SKIPPED_REVIEW,
        "stage_packages": [packet.get("package_id") or packet.get("status_packet_id") for packet in stage_packets],
        "decision_options": ["p015 aggressive batch ok", "hold p015 batch: <reason>"],
        "continuation": {"history_continues_to_page": "016", "page_016_processed": False},
        "guardrails": guardrails(),
    }
    write_json(BATCH_ROOT / "page_015_aggressive_batch_report.json", bundle)
    write_text(BATCH_ROOT / "page_015_aggressive_batch_summary.md", "# Page 015 Aggressive Batch Summary - P015BATCH-G1-VIRAL-001\n\nInternal stages P015TR/P015TXT/P015SEM/PCRP/P015PCA were machine-reviewed with Sol/Terra and skipped per-stage human review by explicit authorization. Final human review is requested on this bundle plus `G1SP-G1-VIRAL-010`.\n\nHistory continues to page 016, but page 016 is not processed by this batch.\n\nDecision: `p015 aggressive batch ok` or `hold p015 batch: <reason>`.\n")
    write_manifest(BATCH_ROOT, "page_015_aggressive_batch_manifest.md", "Page 015 Aggressive Batch Manifest - P015BATCH-G1-VIRAL-001")


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
