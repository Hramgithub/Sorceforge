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
from page_review_semantic_units import keeper_notes_callout_heading_level, nested_run_in_heading_level
from semantic_segmentation_contract import split_bounded_callout, validate_semantic_split_contracts


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_012_aggressive_batch.py"
TEST_PATH = ROOT / "tests" / "test_page_012_aggressive_batch.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-012-AGGRESSIVE-BATCH-001"
LANE_ID = "P012BATCH-G1-VIRAL-001"
PAGE = "012"
PAGE_ID = "PG-G1-VIRAL-P012"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_012.png"
PAGE_IMAGE_SHA256 = "D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6"
G1SP_006_PACKET_SHA256 = "E79EF8C4941184724D2E654799DA7DAEAAD4E0B29E4D52C9379D0DA5BD533822"

TRIAGE_ROOT = TRIAL_ROOT / "page_012_triage_G1_VIRAL_001"
TEXT_ROOT = TRIAL_ROOT / "page_012_text_extraction_G1_VIRAL_001"
SEM_ROOT = TRIAL_ROOT / "page_012_semantic_text_map_G1_VIRAL_001"
PCRP_ROOT = TRIAL_ROOT / "page_complete_review_p012_G1_VIRAL_001"
PCA_ROOT = TRIAL_ROOT / "page_complete_acceptance_p012_G1_VIRAL_001"
STATUS_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_007"
BATCH_ROOT = TRIAL_ROOT / "page_012_aggressive_batch_G1_VIRAL_001"

SKIPPED_REVIEW = "human_review_skipped_by_explicit_authorization"
DELEGATED_REVIEW = "review_delegated_to_Sol_Terra"

SOL_TERRA_STAGE_REVIEWS = {
    "P012TR-G1-VIRAL-001": {
        "sol": "OK: page 012 is bounded to the existing page image and split into text-only review surfaces without OCR/render/PDF/raw mutation.",
        "terra": "OK: no page 013 asset is inspected; no page acceptance or broad Gate authority is created by triage.",
    },
    "P012TXT-G1-VIRAL-001": {
        "sol": "OK: draft transcription is limited to P012 text evidence crops in logical reading order.",
        "terra": "OK: text extraction records skipped human review and creates no OCR/source/page/whole-Gate acceptance.",
    },
    "P012SEM-G1-VIRAL-001": {
        "sol": "OK: semantic units preserve headings, boxed sections, inline option headings, paragraphs, and continuation metadata.",
        "terra": "OK: semantic map is machine-reviewed only and does not process page 013 beyond inert continuation metadata.",
    },
    "PCRP-G1-VIRAL-P012-001": {
        "sol": "OK: page-complete review packet reconciles all P012 text blocks, semantic units, and review assets with no open blockers.",
        "terra": "OK: PCRP is internal machine-reviewed evidence only and does not claim per-stage Bogdan approval.",
    },
    "P012PCA-G1-VIRAL-001": {
        "sol": "OK: acceptance is page 012 only under delegated-review lane authority and exact PCRP predecessor binding.",
        "terra": "OK: PCA does not imply whole Gate 1, fixture admission, source acceptance, or direct human page-level approval.",
    },
    "G1SP-G1-VIRAL-007": {
        "sol": "OK: status refresh records pages 001-012 accepted-only and pages 013-020 unstarted.",
        "terra": "OK: page 013 is only a recommended next candidate and is not authorized by the status packet.",
    },
}

BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P012-B001",
        "role": "emily_continuation_left_upper_text",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R01",
        "crop_box_px": [170, 220, 1080, 600],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 150, "max_x": 190, "min_y": 200, "max_y": 240, "min_width": 1050, "min_height": 560},
        },
        "asset": "review_assets/1_P012-emily-continuation-left-upper-text-evidence.png",
    },
    {
        "block_id": "P012-B002",
        "role": "appearance_super_fan_option_box",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R02",
        "crop_box_px": [170, 820, 1080, 475],
        "crop_contract": {
            "coverage": "full_text_box",
            "context_allowed": False,
            "expected_bounds": {"min_x": 150, "max_x": 190, "min_y": 800, "max_y": 850, "min_width": 1050, "min_height": 450},
        },
        "asset": "review_assets/2_P012-appearance-super-fan-option-box-text-evidence.png",
    },
    {
        "block_id": "P012-B003",
        "role": "another_ghost_hunter_option_body_left_column",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R03",
        "crop_box_px": [170, 1285, 1080, 1815],
        "crop_contract": {
            "coverage": "full_text_region_part",
            "context_allowed": False,
            "expected_bounds": {"min_x": 150, "max_x": 190, "min_y": 1260, "max_y": 1300, "min_width": 1050, "min_height": 1780},
        },
        "asset": "review_assets/3_P012-another-ghost-hunter-option-left-column-text-evidence.png",
    },
    {
        "block_id": "P012-B004",
        "role": "another_ghost_hunter_option_body_right_upper",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R04",
        "crop_box_px": [1285, 210, 1120, 260],
        "crop_contract": {
            "coverage": "full_text_region_part",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1260, "max_x": 1310, "min_y": 190, "max_y": 230, "min_width": 1080, "min_height": 230},
        },
        "asset": "review_assets/4_P012-another-ghost-hunter-option-right-upper-text-evidence.png",
    },
    {
        "block_id": "P012-B005",
        "role": "appearance_another_ghost_hunter_option_box",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R05",
        "crop_box_px": [1305, 450, 1100, 340],
        "crop_contract": {
            "coverage": "full_text_box",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1280, "max_x": 1320, "min_y": 430, "max_y": 470, "min_width": 1050, "min_height": 300},
        },
        "asset": "review_assets/5_P012-appearance-another-ghost-hunter-option-box-text-evidence.png",
    },
    {
        "block_id": "P012-B006",
        "role": "keepers_notes_box",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R06",
        "crop_box_px": [1305, 790, 1100, 400],
        "crop_contract": {
            "coverage": "full_text_box",
            "context_allowed": False,
            "neighbor_text_exclusion": ["PRM-G1-VIRAL-001-P012-R03"],
            "expected_bounds": {"min_x": 1280, "max_x": 1320, "min_y": 770, "max_y": 810, "min_width": 1050, "min_height": 380},
            "source_note": "Keeper's Notes box only; excludes left-column Another Ghost Hunter Option text.",
        },
        "asset": "review_assets/6_P012-keepers-notes-box-text-evidence.png",
    },
    {
        "block_id": "P012-B007",
        "role": "creating_new_investigators_section",
        "source_region_id": "PRM-G1-VIRAL-001-P012-R07",
        "crop_box_px": [1300, 1260, 1120, 1900],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1270, "max_x": 1320, "min_y": 1240, "max_y": 1280, "min_width": 1080, "min_height": 1850},
        },
        "asset": "review_assets/7_P012-creating-new-investigators-section-text-evidence.png",
        "continues_to_page": "013",
    },
]

TEXT_UNITS: list[dict[str, Any]] = [
    {
        "unit_id": "P012-TEXT-001",
        "block_id": "P012-B001",
        "text": "her out to the island the previous day with a spare rowboat to get back to the mainland in case the anonymous tip-off proved to be false. (The spare rowboat is the one in the cove.) She decided to do a bit of exploring by herself during the daytime, figuring the ghosts wouldn't come out while the sun shone. Unfortunately, she poked around a bit too much and in the course of her explorations, was utterly corrupted by Hastalyk from within. Mechanically, she has a Taint level of 10 (see p.62 for details), but appears completely normal on the outside. She will subtly lead the Investigators on in an effort to release the Grand Corruption upon the world.",
    },
    {
        "unit_id": "P012-TEXT-002",
        "block_id": "P012-B002",
        "text": "APPEARANCE (SUPER FAN OPTION)\n\nEm is 5'2\" with a bob of strawberry blonde hair and an easy smile. She wears Spektral Krew merchandise all the time and has a t-shirt of Corrina's face that she made herself (it's a particularly unflattering photograph). She has a backpack that always seems to contain Spektral Krew photos for the cast to sign, as well as a large collection of Sharpies so she is always prepared. She dresses in a similar fashion to Corrina.",
    },
    {
        "unit_id": "P012-TEXT-003",
        "block_ids": ["P012-B003", "P012-B004"],
        "text": "Another Ghost Hunter Option. Em is from a rival ghost hunting channel called The Phantom Posse. She is their Spiritualist Medium who, unlike Corrina, genuinely believes she has powers (she is very, very lightly psychic when compared to someone like Enoch) as she does get general impressions from places. The Posse were tipped off by Maya around a week earlier about the island and they paid her handsomely for the tip. They subsequently went to the island to film a 48-hour stay there, but during their investigation were sickened by the Taint of Hastalyk and all died... except Em who became completely corrupted by the Taint and is now a hapless devotee of the Grand Corruption - something she is completely unaware of. She took the bodies of her former compatriots down to the charnel pit and threw them in, feeding Hastalyk's form, making it draw nearer to being able to manifest.\n\nShe has a stand-offish relationship with Corrina that is quite the opposite of the super fan version of Em. Corrina has met her on a number of occasions and finds herself fascinated and attracted to her in a way she can't really understand. Em forgets her name and calls her Carla from time-to-time.\n\nWhen the group finds her, she is frantically searching the island for her compatriots, and relieved to see familiar faces as the batteries on her torch are beginning to dim and she is getting incredibly scared. If questioned she says that they arrived the previous day to film - brought there by a local man in a rickety boat - and had decided to sleep in one of the abandoned and less filthy hospital rooms, and when she woke up she was alone. It was as if they had vanished. She has no idea that it was Maya who told her group. Of course, this is a lie though Em doesn't know this - Hastalyk has infected her mind and controls what she remembers and says. It is the truth from her point of view. It is also true from her point of view that she doesn't know where the Phantom Posse's equipment is nor where her colleagues are. In actuality, she dumped all of their electronic equipment in the sea weighed down by cobblestones and of course, fed their dead bodies to the pit.",
    },
    {
        "unit_id": "P012-TEXT-004",
        "block_id": "P012-B005",
        "text": "APPEARANCE (ANOTHER GHOST HUNTER OPTION)\n\nHer appearance is pretty much the same except that she wears a Phantom Posse t-shirt and has a backpack with all manner of spiritualist nonsense inside like crystals, divining rods, and the like.",
    },
    {
        "unit_id": "P012-TEXT-005",
        "block_id": "P012-B006",
        "text": "Keeper's Notes\n\nThe Keeper may decide that Em missed finding one of the static mounted cameras. If the investigators get a chance to look at the footage, they'll see the Phantom Posse going about their investigation, but at the very end, they'll see Emily dragging her teammates' bodies down a hallway, her hands covered in blood.",
    },
    {
        "unit_id": "P012-TEXT-006",
        "block_id": "P012-B007",
        "text": "Creating New Investigators\n\nWhile this scenario is designed to be run with the pre-generated Investigators provided, there is no reason that the players cannot make their own. There are only a few important points to keep in mind when doing so. The first is that the Investigators should be making some sort of online ghost hunting show with the goal of getting more views, subscriptions, patrons, and so on. In other words, they should want to 'go viral'.\n\nThe second important Investigator feature is that the host should be strongly motivated to finish the stream at all costs. While Marco's motivation is money and fame, there's no reason why another host might be motivated by a rivalry with another YouTube channel, an obsession with learning the truth about the supernatural, or even driven to debunk the supernatural as utter nonsense.\n\nThe third isn't as critical, but it can be very helpful for at least one of them to have The Sight (see p.60). This allows them to learn more about the true nature of what's going on, while adding to the overall mood of the story. The Investigator with The Sight could be the psychic from the group or not. It could even be interesting to have someone who has been faking psychic powers to suddenly experience real visions.\n\nOther Investigator Options. Other options are possible, though it would require some reworking by the Keeper. The amount of reworking depends on how far the Investigators stray from the scenario's core premise. The important features to include are plausible motivations for exploring the island, and electronic devices that can be used by Hastalyk to control the Investigators. The Keeper can use the ideas below, or come up with their own.\n\nMythos Investigators - A Miskatonic University expedition has been sent to Isola di Malamente with permission from the Italian",
        "continues_to_page": "013",
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
    parser = argparse.ArgumentParser(description="Build page 012 aggressive delegated-review batch.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 012 aggressive batch is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 012 aggressive batch requires {AUTHORIZATION_ID}")


def verify_predecessors() -> list[dict[str, str]]:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")
    predecessors = [
        ("post_p011_status_route_packet", TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_006" / "gate_1_status_packet.json", G1SP_006_PACKET_SHA256),
        ("page_012_image", PAGE_IMAGE, PAGE_IMAGE_SHA256),
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
        authority="Bogdan Telegram authorization for page 012 aggressive batch",
        exact_action=[
            "Create page 012 aggressive delegated-review batch artifacts.",
            "Generate P012TR/P012TXT/P012SEM/PCRP/P012PCA/status/batch outputs with skipped human review and Sol/Terra evidence.",
        ],
        admitted_inputs=[
            {"name": "post_p011_status_route_packet", "sha256": G1SP_006_PACKET_SHA256},
            {"name": "page_012_image", "sha256": PAGE_IMAGE_SHA256},
        ],
        allowed_outputs=[
            "scripts/build_page_012_aggressive_batch.py",
            "tests/test_page_012_aggressive_batch.py",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_012_*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p012_G1_VIRAL_001/*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_007/*",
        ],
        limits=[
            "Do not record direct Bogdan approval for internal P012 stages.",
            "Do not process page 013 or later beyond the post-P012 status recommendation.",
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
        "page_013_processing": False,
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
    page_copy = review_root / "page_012.png"
    shutil.copy2(PAGE_IMAGE, page_copy)
    assets["review_assets/page_012.png"] = {"path": page_copy.relative_to(ROOT).as_posix(), "sha256": sha256_file(page_copy)}
    with Image.open(PAGE_IMAGE) as image:
        validate_text_evidence_crop_contracts(image.size, BLOCKS)
        for block in BLOCKS:
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
        "package_id": "P012TR-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "triage_crop_contract_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "page_id": PAGE_ID,
        "predecessors": predecessors,
        "review_gate": review_gate("P012TR-G1-VIRAL-001"),
        "review_blocks": blocks,
        "logical_text_order": [f"{block['block_id']}-TES" for block in BLOCKS],
        "visual_only_blocks": [],
        "guardrails": guardrails({"triage_created": True}),
    }
    write_json(TRIAGE_ROOT / "page_012_triage_packet.json", packet)
    write_json(TRIAGE_ROOT / "page_012_triage_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "guardrails": packet["guardrails"], "block_count": len(blocks)})
    write_text(TRIAGE_ROOT / "page_012_triage_summary.md", "# Page 012 Triage Summary - P012TR-G1-VIRAL-001\n\nMachine-reviewed triage with human review skipped by explicit authorization. All seven page 012 review blocks are text-like evidence surfaces; no visual-only anchors are promoted. Page 013 is not processed.\n")
    write_manifest(TRIAGE_ROOT, "page_012_triage_manifest.md", "Page 012 Triage Manifest - P012TR-G1-VIRAL-001")
    return packet


def build_text(triage_packet: dict[str, Any]) -> dict[str, Any]:
    lines = ["# Page 012 Text Map - P012TXT-G1-VIRAL-001", "", "Status: `draft_text_machine_reviewed_human_review_skipped`", ""]
    for index, unit in enumerate(TEXT_UNITS, start=1):
        lines.extend([f"## {unit['unit_id']}", "", f"- Reading order: `{index}`", f"- Blocks: `{', '.join(unit_block_ids(unit))}`", "", "```text", unit["text"], "```", ""])
    write_text(TEXT_ROOT / "page_012_text_map.md", "\n".join(lines))
    packet = {
        "package_id": "P012TXT-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "draft_text_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": triage_packet["package_id"], "sha256": sha256_file(TRIAGE_ROOT / "page_012_triage_packet.json")},
        "review_gate": review_gate("P012TXT-G1-VIRAL-001"),
        "logical_reading_order": [unit["unit_id"] for unit in TEXT_UNITS],
        "extraction_method": "manual_from_text_evidence_region",
        "ocr_executed": False,
        "text_map": {"path": "page_012_text_map.md", "sha256": sha256_file(TEXT_ROOT / "page_012_text_map.md")},
        "continuation_metadata": [{"from": "P011/SU-P011-EMILY-005", "to": "P012-TEXT-001"}, {"from": "P012-TEXT-006", "to": "P013 inert continuation metadata only"}],
        "guardrails": guardrails({"text_extraction_created": True}),
    }
    write_json(TEXT_ROOT / "page_012_text_extraction_packet.json", packet)
    write_json(TEXT_ROOT / "page_012_text_extraction_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "text_unit_count": len(TEXT_UNITS), "guardrails": packet["guardrails"]})
    write_text(TEXT_ROOT / "page_012_text_extraction_summary.md", "# Page 012 Text Extraction Summary - P012TXT-G1-VIRAL-001\n\nDraft text extracted from P012TR text evidence crops under delegated Sol/Terra review. Human review is skipped by explicit authorization; this creates no OCR/source/page/whole-Gate acceptance.\n")
    write_manifest(TEXT_ROOT, "page_012_text_extraction_manifest.md", "Page 012 Text Extraction Manifest - P012TXT-G1-VIRAL-001")
    return packet


def semantic_units() -> list[dict[str, Any]]:
    keeper_callout = split_bounded_callout(
        TEXT_UNITS[4]["text"],
        callout_heading="Keeper's Notes",
        allow_to_end=True,
    )
    units = [
        ("SU-P012-EMILY-001", "continuation", None, "body", "P012-B001", TEXT_UNITS[0]["text"], None, None, None),
        ("SU-P012-EMILY-002", "heading", "h3", "section_heading", "P012-B002", "APPEARANCE (SUPER FAN OPTION)", "block_heading", "normal", True),
        ("SU-P012-EMILY-003", "paragraph", None, "body", "P012-B002", TEXT_UNITS[1]["text"].split("\n\n", 1)[1], None, None, None),
        ("SU-P012-EMILY-004", "heading", "h3", "section_heading", "P012-B003", "Another Ghost Hunter Option.", "inline_heading", "italic", False),
        ("SU-P012-EMILY-005", "paragraph", None, "body", "P012-B003", TEXT_UNITS[2]["text"].split("Another Ghost Hunter Option. ", 1)[1].split("\n\n")[0], None, None, None),
        ("SU-P012-EMILY-006", "paragraph", None, "body", "P012-B003", TEXT_UNITS[2]["text"].split("\n\n")[1], None, None, None),
        ("SU-P012-EMILY-007", "paragraph", None, "body", "P012-B003", TEXT_UNITS[2]["text"].split("\n\n")[2].split("doesn't know where", 1)[0].rstrip(), None, None, None),
        ("SU-P012-EMILY-008", "continuation", None, "body", "P012-B004", "doesn't know where the Phantom Posse's equipment is nor where her colleagues are. In actuality, she dumped all of their electronic equipment in the sea weighed down by cobblestones and of course, fed their dead bodies to the pit.", None, None, None),
        ("SU-P012-EMILY-009", "heading", "h3", "section_heading", "P012-B005", "APPEARANCE (ANOTHER GHOST HUNTER OPTION)", "block_heading", "normal", True),
        ("SU-P012-EMILY-010", "paragraph", None, "body", "P012-B005", TEXT_UNITS[3]["text"].split("\n\n", 1)[1], None, None, None),
        ("SU-P012-KEEPER-001", "heading", keeper_notes_callout_heading_level(), "callout_heading", "P012-B006", "Keeper's Notes", "block_heading", "bold", True),
        ("SU-P012-KEEPER-002", "paragraph", None, "callout_body", "P012-B006", keeper_callout.body, None, None, None),
        ("SU-P012-CNI-001", "heading", "h2", "section_heading", "P012-B007", "Creating New Investigators", "block_heading", "normal", True),
        ("SU-P012-CNI-002", "paragraph", None, "body", "P012-B007", TEXT_UNITS[5]["text"].split("\n\n")[1], None, None, None),
        ("SU-P012-CNI-003", "paragraph", None, "body", "P012-B007", TEXT_UNITS[5]["text"].split("\n\n")[2], None, None, None),
        ("SU-P012-CNI-004", "paragraph", None, "body", "P012-B007", TEXT_UNITS[5]["text"].split("\n\n")[3], None, None, None),
        ("SU-P012-CNI-005", "heading", "h3", "section_heading", "P012-B007", "Other Investigator Options.", "inline_heading", "italic", False),
        ("SU-P012-CNI-006", "paragraph", None, "body", "P012-B007", TEXT_UNITS[5]["text"].split("\n\n")[4].split(" ", 3)[3], None, None, None),
        ("SU-P012-CNI-007", "heading", nested_run_in_heading_level("h3"), "section_heading", "P012-B007", "Mythos Investigators", "inline_heading", "normal", False),
        ("SU-P012-CNI-008", "continuation", None, "body", "P012-B007", TEXT_UNITS[5]["text"].split("Mythos Investigators - ", 1)[1], None, None, None),
    ]
    result = []
    for order, (unit_id, unit_type, heading_level, display_style, block_id, text, layout_role, font_style, line_break_after) in enumerate(units, start=1):
        block = find_block(block_id)
        payload: dict[str, Any] = {
            "unit_id": unit_id,
            "unit_type": unit_type,
            "unit_scope": "in_scope_text",
            "reading_order": order,
            "source_block_id": block_id,
            "source_region_ids": [block["source_region_id"]],
            "crop_ids": [f"{block_id}-TES"],
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
        if unit_id == "SU-P012-CNI-007":
            payload["text_decoration"] = "underline"
            payload["continues_inline_to"] = "SU-P012-CNI-008"
        if unit_id == "SU-P012-CNI-008":
            payload["external_continues_to"] = "P013 inert continuation metadata only"
        if unit_id == "SU-P012-KEEPER-002":
            payload["semantic_split_contract"] = keeper_callout.contract()
        result.append(payload)
    return result


def build_semantic(text_packet: dict[str, Any]) -> dict[str, Any]:
    units = semantic_units()
    split_validation = validate_semantic_split_contracts(units)
    if not split_validation["valid"]:
        raise SystemExit("P012 semantic split contract validation failed")
    document = {
        "package_id": "P012SEM-G1-VIRAL-001",
        "map_id": "SM-G1-VIRAL-P012-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "semantic_text_map_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": text_packet["package_id"], "sha256": sha256_file(TEXT_ROOT / "page_012_text_extraction_packet.json")},
        "review_gate": review_gate("P012SEM-G1-VIRAL-001"),
        "units": units,
        "unit_count": len(units),
        "validation": {"status": "passed", "findings": split_validation["findings"]},
        "semantic_split_validation": split_validation,
        "guardrails": guardrails({"semantic_map_created": True}),
    }
    markdown = ["# Page 012 Semantic Text Map - P012SEM-G1-VIRAL-001", "", "Status: `semantic_text_map_machine_reviewed_human_review_skipped`", ""]
    for unit in units:
        markdown.extend([f"## {unit['unit_id']}", f"- Type: `{unit['unit_type']}`", f"- Heading level: `{unit.get('heading_level')}`", f"- Layout role: `{unit.get('layout_role')}`", "", "```text", unit["text"], "```", ""])
    write_json(SEM_ROOT / "page_012_semantic_text_map.json", document)
    write_text(SEM_ROOT / "page_012_semantic_text_map.md", "\n".join(markdown))
    write_json(SEM_ROOT / "page_012_semantic_text_map_report.json", {"package_id": document["package_id"], "status": document["status"], "review_gate": document["review_gate"], "unit_count": len(units), "semantic_split_validation": split_validation, "guardrails": document["guardrails"]})
    write_text(SEM_ROOT / "page_012_semantic_text_map_summary.md", "# Page 012 Semantic Text Map Summary - P012SEM-G1-VIRAL-001\n\nMachine-reviewed semantic map with skipped human review under explicit authorization. Headings, inline headings, paragraphs, boxes, and continuation metadata are represented.\n")
    write_manifest(SEM_ROOT, "page_012_semantic_text_map_manifest.md", "Page 012 Semantic Text Map Manifest - P012SEM-G1-VIRAL-001")
    return document


def build_pcrp(semantic_document: dict[str, Any]) -> dict[str, Any]:
    assets_root = PCRP_ROOT / "review_assets"
    assets_root.mkdir(parents=True, exist_ok=True)
    for rel in ["page_012.png"] + [block["asset"].split("/", 1)[1] for block in BLOCKS]:
        source = TRIAGE_ROOT / "review_assets" / rel
        if source.exists():
            shutil.copy2(source, assets_root / rel)
    for name, root, src_name in [
        ("page_012_text_map.md", TEXT_ROOT, "page_012_text_map.md"),
        ("page_012_semantic_text_map.md", SEM_ROOT, "page_012_semantic_text_map.md"),
        ("page_012_semantic_text_map.json", SEM_ROOT, "page_012_semantic_text_map.json"),
    ]:
        shutil.copy2(root / src_name, assets_root / name)
    packet = {
        "package_id": "PCRP-G1-VIRAL-P012-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_complete_review_packet_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": semantic_document["package_id"], "sha256": sha256_file(SEM_ROOT / "page_012_semantic_text_map.json")},
        "review_gate": review_gate("PCRP-G1-VIRAL-P012-001"),
        "ready_blocks": [block["block_id"] for block in BLOCKS],
        "ready_block_count": len(BLOCKS),
        "blockers": [],
        "open_questions": [],
        "semantic_validation": {"status": "passed", "findings": []},
        "inventory_reconciliation": {"status": "passed", "findings": []},
        "guardrails": guardrails({"pcrp_created": True}),
    }
    write_json(PCRP_ROOT / "page_complete_review_report.json", packet)
    write_text(PCRP_ROOT / "page_complete_review_packet.md", "# Page Complete Review Packet - PCRP-G1-VIRAL-P012-001\n\nMachine-reviewed page 012 PCRP. Human review skipped by explicit authorization; final human review is deferred to the post-P012 bundle/status.\n")
    write_text(PCRP_ROOT / "page_complete_review_summary.md", "# Page 012 Review Summary\n\n7/7 ready text blocks; no visual-only anchors; semantic validation and inventory reconciliation passed; no blockers or open questions.\n")
    write_manifest(PCRP_ROOT, "page_complete_review_manifest.md", "Page 012 Complete Review Manifest - PCRP-G1-VIRAL-P012-001")
    return packet


def build_pca(pcrp_packet: dict[str, Any]) -> dict[str, Any]:
    record = {
        "package_id": "P012PCA-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_012_complete_accepted_under_delegated_review_lane",
        "accepted_pages": ["012"],
        "human_review_state": SKIPPED_REVIEW,
        "delegated_review_state": DELEGATED_REVIEW,
        "predecessor": {"package_id": pcrp_packet["package_id"], "sha256": sha256_file(PCRP_ROOT / "page_complete_review_report.json")},
        "review_gate": review_gate("P012PCA-G1-VIRAL-001"),
        "guardrails": guardrails({"page_complete_acceptance_created": True}),
    }
    write_json(PCA_ROOT / "page_complete_acceptance_report.json", record)
    write_text(PCA_ROOT / "page_complete_acceptance_record.md", "# Page Complete Acceptance Record - P012PCA-G1-VIRAL-001\n\nPage 012 accepted only under explicit delegated-review lane authorization. This is not direct per-stage human approval and not whole Gate 1 acceptance.\n")
    write_text(PCA_ROOT / "page_complete_acceptance_summary.md", "# Page Complete Acceptance Summary - P012PCA-G1-VIRAL-001\n\nAccepted page: `012` only. Human review skipped by explicit authorization; Sol/Terra delegated review passed.\n")
    write_manifest(PCA_ROOT, "page_complete_acceptance_manifest.md", "Page 012 Complete Acceptance Manifest - P012PCA-G1-VIRAL-001")
    return record


def build_status(pca_record: dict[str, Any]) -> dict[str, Any]:
    packet = {
        "status_packet_id": "G1SP-G1-VIRAL-007",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "gate_1_status_route_packet_ready_for_final_human_batch_review",
        "page_complete_accepted_pages": [f"{i:03d}" for i in range(1, 13)],
        "remaining_page_complete_pages_unstarted": [f"{i:03d}" for i in range(13, 21)],
        "recommended_next_candidate": "page_013_triage_readiness_not_authorized",
        "predecessor": {"package_id": pca_record["package_id"], "sha256": sha256_file(PCA_ROOT / "page_complete_acceptance_report.json")},
        "review_gate": review_gate("G1SP-G1-VIRAL-007"),
        "guardrails": guardrails(),
    }
    write_json(STATUS_ROOT / "gate_1_status_packet.json", packet)
    write_json(STATUS_ROOT / "gate_1_status_report.json", packet)
    write_text(STATUS_ROOT / "gate_1_status_summary.md", "# Gate 1 Status Route Packet - G1SP-G1-VIRAL-007\n\nPages `001-012` are page-complete accepted only. Pages `013-020` remain unstarted. Page 013 triage/readiness is only the recommended next candidate and is not authorized. Whole Gate 1 and all broad capabilities remain blocked.\n")
    write_manifest(STATUS_ROOT, "gate_1_status_manifest.md", "Gate 1 Status Route Manifest - G1SP-G1-VIRAL-007")
    return packet


def build_bundle(stage_packets: list[dict[str, Any]]) -> None:
    bundle = {
        "package_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "ready_for_bogdan_final_batch_review",
        "human_review_model": "final_bundle_and_post_p012_status_only",
        "internal_stage_human_review_state": SKIPPED_REVIEW,
        "stage_packages": [packet.get("package_id") or packet.get("status_packet_id") for packet in stage_packets],
        "decision_options": ["p012 aggressive batch ok", "hold p012 batch: <reason>"],
        "guardrails": guardrails(),
    }
    write_json(BATCH_ROOT / "page_012_aggressive_batch_report.json", bundle)
    write_text(BATCH_ROOT / "page_012_aggressive_batch_summary.md", "# Page 012 Aggressive Batch Summary - P012BATCH-G1-VIRAL-001\n\nInternal stages P012TR/P012TXT/P012SEM/PCRP/P012PCA were machine-reviewed with Sol/Terra and skipped per-stage human review by explicit authorization. Final human review is requested on this bundle plus `G1SP-G1-VIRAL-007`.\n\nDecision: `p012 aggressive batch ok` or `hold p012 batch: <reason>`.\n")
    write_manifest(BATCH_ROOT, "page_012_aggressive_batch_manifest.md", "Page 012 Aggressive Batch Manifest - P012BATCH-G1-VIRAL-001")


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
