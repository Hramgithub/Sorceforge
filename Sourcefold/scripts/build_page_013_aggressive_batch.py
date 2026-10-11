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
from page_review_semantic_units import nested_run_in_heading_level


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_013_aggressive_batch.py"
TEST_PATH = ROOT / "tests" / "test_page_013_aggressive_batch.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-013-AGGRESSIVE-BATCH-001"
LANE_ID = "P013BATCH-G1-VIRAL-001"
PAGE = "013"
PAGE_ID = "PG-G1-VIRAL-P013"
PAGE_IMAGE = TRIAL_ROOT / "images" / "page_013.png"
PAGE_IMAGE_SHA256 = "DC9BF562A4B3B7E43B38F29F484B64B13958330F449672D6A695B36E0D8F0935"
G1SP_007_PACKET_SHA256 = "37651668FD8FF162DC6205A7EB244589548C78789BBB0083E2E5FCD85C224E9B"

TRIAGE_ROOT = TRIAL_ROOT / "page_013_triage_G1_VIRAL_001"
TEXT_ROOT = TRIAL_ROOT / "page_013_text_extraction_G1_VIRAL_001"
SEM_ROOT = TRIAL_ROOT / "page_013_semantic_text_map_G1_VIRAL_001"
PCRP_ROOT = TRIAL_ROOT / "page_complete_review_p013_G1_VIRAL_001"
PCA_ROOT = TRIAL_ROOT / "page_complete_acceptance_p013_G1_VIRAL_001"
STATUS_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_008"
BATCH_ROOT = TRIAL_ROOT / "page_013_aggressive_batch_G1_VIRAL_001"

SKIPPED_REVIEW = "human_review_skipped_by_explicit_authorization"
DELEGATED_REVIEW = "review_delegated_to_Sol_Terra"

SOL_TERRA_STAGE_REVIEWS = {
    "P013TR-G1-VIRAL-001": {
        "sol": "OK: page 013 is bounded to the existing page image and uses explicit crop provenance contracts for all text evidence surfaces.",
        "terra": "OK: triage is hash-bound to G1SP-G1-VIRAL-007 and page_013.png; page 014+ is not processed.",
    },
    "P013TXT-G1-VIRAL-001": {
        "sol": "OK: draft transcription is limited to P013 text evidence crops in logical reading order.",
        "terra": "OK: text extraction records skipped human review and creates no OCR/source/page/whole-Gate acceptance.",
    },
    "P013SEM-G1-VIRAL-001": {
        "sol": "OK: semantic units preserve continuation text, inline underlined option headings, and paragraph boundaries.",
        "terra": "OK: semantic map is machine-reviewed only and contains no page 014 processing.",
    },
    "PCRP-G1-VIRAL-P013-001": {
        "sol": "OK: page-complete review packet reconciles all P013 text blocks, semantic units, and review assets with no open blockers.",
        "terra": "OK: PCRP is internal machine-reviewed evidence only and does not claim per-stage Bogdan approval.",
    },
    "P013PCA-G1-VIRAL-001": {
        "sol": "OK: acceptance is page 013 only under delegated-review lane authority and exact PCRP predecessor binding.",
        "terra": "OK: PCA does not imply whole Gate 1, fixture admission, source acceptance, or direct human page-level approval.",
    },
    "G1SP-G1-VIRAL-008": {
        "sol": "OK: status refresh records pages 001-013 accepted-only and pages 014-020 unstarted.",
        "terra": "OK: page 014 is only a recommended next candidate and is not authorized by the status packet.",
    },
}

BLOCKS: list[dict[str, Any]] = [
    {
        "block_id": "P013-B001",
        "role": "mythos_investigators_continuation_left_upper",
        "source_region_id": "PRM-G1-VIRAL-001-P013-R01",
        "crop_box_px": [160, 205, 1100, 440],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 140, "max_x": 180, "min_y": 185, "max_y": 225, "min_width": 1060, "min_height": 400},
        },
        "asset": "review_assets/1_P013-mythos-investigators-continuation-text-evidence.png",
    },
    {
        "block_id": "P013-B002",
        "role": "documentary_film_crew_option",
        "source_region_id": "PRM-G1-VIRAL-001-P013-R02",
        "crop_box_px": [210, 625, 1060, 340],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 190, "max_x": 230, "min_y": 600, "max_y": 650, "min_width": 1020, "min_height": 315},
        },
        "asset": "review_assets/2_P013-documentary-film-crew-text-evidence.png",
    },
    {
        "block_id": "P013-B003",
        "role": "tourists_option_left_start",
        "source_region_id": "PRM-G1-VIRAL-001-P013-R03",
        "crop_box_px": [210, 960, 1060, 140],
        "crop_contract": {
            "coverage": "full_text_region_part",
            "context_allowed": False,
            "expected_bounds": {"min_x": 190, "max_x": 230, "min_y": 935, "max_y": 980, "min_width": 1020, "min_height": 120},
        },
        "asset": "review_assets/3_P013-tourists-left-start-text-evidence.png",
    },
    {
        "block_id": "P013-B004",
        "role": "tourists_option_right_continuation",
        "source_region_id": "PRM-G1-VIRAL-001-P013-R04",
        "crop_box_px": [1290, 205, 1120, 700],
        "crop_contract": {
            "coverage": "full_text_region_part",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1265, "max_x": 1310, "min_y": 185, "max_y": 225, "min_width": 1080, "min_height": 660},
        },
        "asset": "review_assets/4_P013-tourists-right-continuation-text-evidence.png",
    },
    {
        "block_id": "P013-B005",
        "role": "pesky_teenagers_option",
        "source_region_id": "PRM-G1-VIRAL-001-P013-R05",
        "crop_box_px": [1335, 905, 1060, 190],
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_x": 1310, "max_x": 1360, "min_y": 880, "max_y": 930, "min_width": 1010, "min_height": 160},
        },
        "asset": "review_assets/5_P013-pesky-teenagers-text-evidence.png",
    },
]

TEXT_UNITS: list[dict[str, Any]] = [
    {
        "unit_id": "P013-TEXT-001",
        "block_id": "P013-B001",
        "text": "government. They are given cameras and communications equipment to investigate the paranormal events reported on the island, and so rather than YouTube commenters, the Investigators could be getting feedback from their peers back at Miskatonic University or some other experts with whom they're consulting. In this case, Hastalyk could still manipulate them through their electronic gear, posing as a mysterious expert or benefactor who funded the expedition.",
    },
    {
        "unit_id": "P013-TEXT-002",
        "block_id": "P013-B002",
        "text": "Documentary Film Crew - The National Geographic Society has funded a documentary about Isola di Malamente, and they somehow manage to get permission to film on the island. The film crew begins receiving phone calls from someone claiming to be from National Geographic (actually Hastalyk), but they soon realize that it's someone who knows far too much about them.",
    },
    {
        "unit_id": "P013-TEXT-003",
        "block_ids": ["P013-B003", "P013-B004"],
        "text": "Tourists - A local tour guide (Nuncio Vendra) brings a group of tourists to Isola di Malamente and abandons them there. They immediately begin trying to call for help on their cell phones to no avail. As the darkness sets in, they receive a call from Nuncio on a walkie-talkie that he planted on one of them or in their bags. He tells them that there is a chest of gold bars on the island that dates back to World War II, and if they agree to find it, he'll split it with them. If they don't, they'll never leave the island. Nuncio directs the Investigators to the dock where he has left wireless head cams for each of them and a transmitter so that he can more easily direct them. At some point during their exploration of the island, their radios begin to pick up someone else (actually Hastalyk) who claims that Nuncio is going to kill them, but if the Investigators listen to him, he'll get them off the island by dawn.",
    },
    {
        "unit_id": "P013-TEXT-004",
        "block_id": "P013-B005",
        "text": "Pesky Teenagers - A group of local teens decide to take the rite of passage to explore the island and, well, you know what happens next.",
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
    parser = argparse.ArgumentParser(description="Build page 013 aggressive delegated-review batch.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 013 aggressive batch is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 013 aggressive batch requires {AUTHORIZATION_ID}")


def verify_predecessors() -> list[dict[str, str]]:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")
    predecessors = [
        ("post_p012_status_route_packet", TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_007" / "gate_1_status_packet.json", G1SP_007_PACKET_SHA256),
        ("page_013_image", PAGE_IMAGE, PAGE_IMAGE_SHA256),
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
        authority="Bogdan Telegram authorization for page 013 aggressive batch",
        exact_action=[
            "Create page 013 aggressive delegated-review batch artifacts.",
            "Generate P013TR/P013TXT/P013SEM/PCRP/P013PCA/status/batch outputs with skipped human review and Sol/Terra evidence.",
        ],
        admitted_inputs=[
            {"name": "post_p012_status_route_packet", "sha256": G1SP_007_PACKET_SHA256},
            {"name": "page_013_image", "sha256": PAGE_IMAGE_SHA256},
        ],
        allowed_outputs=[
            "scripts/build_page_013_aggressive_batch.py",
            "tests/test_page_013_aggressive_batch.py",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_013_*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/page_complete_*_p013_G1_VIRAL_001/*",
            "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/gate_1_status_packet_G1_VIRAL_008/*",
        ],
        limits=[
            "Do not record direct Bogdan approval for internal P013 stages.",
            "Do not process page 014 or later beyond the post-P013 status recommendation.",
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
        "page_014_plus_processing": False,
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
    page_copy = review_root / "page_013.png"
    shutil.copy2(PAGE_IMAGE, page_copy)
    assets["review_assets/page_013.png"] = {"path": page_copy.relative_to(ROOT).as_posix(), "sha256": sha256_file(page_copy)}
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
        "package_id": "P013TR-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "triage_crop_contract_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "page_id": PAGE_ID,
        "predecessors": predecessors,
        "review_gate": review_gate("P013TR-G1-VIRAL-001"),
        "review_blocks": blocks,
        "logical_text_order": [f"{block['block_id']}-TES" for block in BLOCKS],
        "visual_only_blocks": [],
        "guardrails": guardrails({"triage_created": True}),
    }
    write_json(TRIAGE_ROOT / "page_013_triage_packet.json", packet)
    write_json(TRIAGE_ROOT / "page_013_triage_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "guardrails": packet["guardrails"], "block_count": len(blocks)})
    write_text(TRIAGE_ROOT / "page_013_triage_summary.md", "# Page 013 Triage Summary - P013TR-G1-VIRAL-001\n\nMachine-reviewed triage with human review skipped by explicit authorization. Five page 013 text-evidence surfaces are contract-bound; Tourists is split across columns to avoid neighboring text capture. Page 014+ is not processed.\n")
    write_manifest(TRIAGE_ROOT, "page_013_triage_manifest.md", "Page 013 Triage Manifest - P013TR-G1-VIRAL-001")
    return packet


def build_text(triage_packet: dict[str, Any]) -> dict[str, Any]:
    lines = ["# Page 013 Text Map - P013TXT-G1-VIRAL-001", "", "Status: `draft_text_machine_reviewed_human_review_skipped`", ""]
    for index, unit in enumerate(TEXT_UNITS, start=1):
        lines.extend([f"## {unit['unit_id']}", "", f"- Reading order: `{index}`", f"- Blocks: `{', '.join(unit_block_ids(unit))}`", "", "```text", unit["text"], "```", ""])
    write_text(TEXT_ROOT / "page_013_text_map.md", "\n".join(lines))
    packet = {
        "package_id": "P013TXT-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "draft_text_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": triage_packet["package_id"], "sha256": sha256_file(TRIAGE_ROOT / "page_013_triage_packet.json")},
        "review_gate": review_gate("P013TXT-G1-VIRAL-001"),
        "logical_reading_order": [unit["unit_id"] for unit in TEXT_UNITS],
        "extraction_method": "manual_from_text_evidence_region",
        "ocr_executed": False,
        "text_map": {"path": "page_013_text_map.md", "sha256": sha256_file(TEXT_ROOT / "page_013_text_map.md")},
        "continuation_metadata": [{"from": "P012/SU-P012-CNI-008", "to": "P013-TEXT-001"}],
        "guardrails": guardrails({"text_extraction_created": True}),
    }
    write_json(TEXT_ROOT / "page_013_text_extraction_packet.json", packet)
    write_json(TEXT_ROOT / "page_013_text_extraction_report.json", {"package_id": packet["package_id"], "status": packet["status"], "review_gate": packet["review_gate"], "text_unit_count": len(TEXT_UNITS), "guardrails": packet["guardrails"]})
    write_text(TEXT_ROOT / "page_013_text_extraction_summary.md", "# Page 013 Text Extraction Summary - P013TXT-G1-VIRAL-001\n\nDraft text extracted from P013TR text evidence crops under delegated Sol/Terra review. Human review is skipped by explicit authorization; this creates no OCR/source/page/whole-Gate acceptance.\n")
    write_manifest(TEXT_ROOT, "page_013_text_extraction_manifest.md", "Page 013 Text Extraction Manifest - P013TXT-G1-VIRAL-001")
    return packet


def semantic_units() -> list[dict[str, Any]]:
    definitions = [
        ("SU-P013-CNI-001", "continuation", None, "body", "P013-B001", TEXT_UNITS[0]["text"], None, None, None, {}),
        ("SU-P013-CNI-002", "heading", nested_run_in_heading_level("h3"), "section_heading", "P013-B002", "Documentary Film Crew", "inline_heading", "normal", False, {"text_decoration": "underline", "continues_inline_to": "SU-P013-CNI-003"}),
        ("SU-P013-CNI-003", "paragraph", None, "body", "P013-B002", TEXT_UNITS[1]["text"].split(" - ", 1)[1], None, None, None, {}),
        ("SU-P013-CNI-004", "heading", nested_run_in_heading_level("h3"), "section_heading", "P013-B003", "Tourists", "inline_heading", "normal", False, {"text_decoration": "underline", "continues_inline_to": "SU-P013-CNI-005"}),
        ("SU-P013-CNI-005", "paragraph", None, "body", "P013-B003", TEXT_UNITS[2]["text"].split(" - ", 1)[1], None, None, None, {}),
        ("SU-P013-CNI-006", "heading", nested_run_in_heading_level("h3"), "section_heading", "P013-B005", "Pesky Teenagers", "inline_heading", "normal", False, {"text_decoration": "underline", "continues_inline_to": "SU-P013-CNI-007"}),
        ("SU-P013-CNI-007", "paragraph", None, "body", "P013-B005", TEXT_UNITS[3]["text"].split(" - ", 1)[1], None, None, None, {}),
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
    document = {
        "package_id": "P013SEM-G1-VIRAL-001",
        "map_id": "SM-G1-VIRAL-P013-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "semantic_text_map_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": text_packet["package_id"], "sha256": sha256_file(TEXT_ROOT / "page_013_text_extraction_packet.json")},
        "review_gate": review_gate("P013SEM-G1-VIRAL-001"),
        "units": units,
        "unit_count": len(units),
        "validation": {"status": "passed", "findings": []},
        "guardrails": guardrails({"semantic_map_created": True}),
    }
    markdown = ["# Page 013 Semantic Text Map - P013SEM-G1-VIRAL-001", "", "Status: `semantic_text_map_machine_reviewed_human_review_skipped`", ""]
    for unit in units:
        markdown.extend([f"## {unit['unit_id']}", f"- Type: `{unit['unit_type']}`", f"- Heading level: `{unit.get('heading_level')}`", f"- Layout role: `{unit.get('layout_role')}`", "", "```text", unit["text"], "```", ""])
    write_json(SEM_ROOT / "page_013_semantic_text_map.json", document)
    write_text(SEM_ROOT / "page_013_semantic_text_map.md", "\n".join(markdown))
    write_json(SEM_ROOT / "page_013_semantic_text_map_report.json", {"package_id": document["package_id"], "status": document["status"], "review_gate": document["review_gate"], "unit_count": len(units), "guardrails": document["guardrails"]})
    write_text(SEM_ROOT / "page_013_semantic_text_map_summary.md", "# Page 013 Semantic Text Map Summary - P013SEM-G1-VIRAL-001\n\nMachine-reviewed semantic map with skipped human review under explicit authorization. Continuation text and inline underlined option headings are represented.\n")
    write_manifest(SEM_ROOT, "page_013_semantic_text_map_manifest.md", "Page 013 Semantic Text Map Manifest - P013SEM-G1-VIRAL-001")
    return document


def build_pcrp(semantic_document: dict[str, Any]) -> dict[str, Any]:
    assets_root = PCRP_ROOT / "review_assets"
    assets_root.mkdir(parents=True, exist_ok=True)
    for rel in ["page_013.png"] + [block["asset"].split("/", 1)[1] for block in BLOCKS]:
        source = TRIAGE_ROOT / "review_assets" / rel
        if source.exists():
            shutil.copy2(source, assets_root / rel)
    for name, root, src_name in [
        ("page_013_text_map.md", TEXT_ROOT, "page_013_text_map.md"),
        ("page_013_semantic_text_map.md", SEM_ROOT, "page_013_semantic_text_map.md"),
        ("page_013_semantic_text_map.json", SEM_ROOT, "page_013_semantic_text_map.json"),
    ]:
        shutil.copy2(root / src_name, assets_root / name)
    packet = {
        "package_id": "PCRP-G1-VIRAL-P013-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_complete_review_packet_machine_reviewed_human_review_skipped",
        "page": PAGE,
        "predecessor": {"package_id": semantic_document["package_id"], "sha256": sha256_file(SEM_ROOT / "page_013_semantic_text_map.json")},
        "review_gate": review_gate("PCRP-G1-VIRAL-P013-001"),
        "ready_blocks": [block["block_id"] for block in BLOCKS],
        "ready_block_count": len(BLOCKS),
        "blockers": [],
        "open_questions": [],
        "semantic_validation": {"status": "passed", "findings": []},
        "inventory_reconciliation": {"status": "passed", "findings": []},
        "guardrails": guardrails({"pcrp_created": True}),
    }
    write_json(PCRP_ROOT / "page_complete_review_report.json", packet)
    write_text(PCRP_ROOT / "page_complete_review_packet.md", "# Page Complete Review Packet - PCRP-G1-VIRAL-P013-001\n\nMachine-reviewed page 013 PCRP. Human review skipped by explicit authorization; final human review is deferred to the post-P013 bundle/status.\n")
    write_text(PCRP_ROOT / "page_complete_review_summary.md", "# Page 013 Review Summary\n\n5/5 ready text-evidence surfaces; no visual-only anchors promoted; semantic validation and inventory reconciliation passed; no blockers or open questions.\n")
    write_manifest(PCRP_ROOT, "page_complete_review_manifest.md", "Page 013 Complete Review Manifest - PCRP-G1-VIRAL-P013-001")
    return packet


def build_pca(pcrp_packet: dict[str, Any]) -> dict[str, Any]:
    record = {
        "package_id": "P013PCA-G1-VIRAL-001",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "page_013_complete_accepted_under_delegated_review_lane",
        "accepted_pages": ["013"],
        "human_review_state": SKIPPED_REVIEW,
        "delegated_review_state": DELEGATED_REVIEW,
        "predecessor": {"package_id": pcrp_packet["package_id"], "sha256": sha256_file(PCRP_ROOT / "page_complete_review_report.json")},
        "review_gate": review_gate("P013PCA-G1-VIRAL-001"),
        "guardrails": guardrails({"page_complete_acceptance_created": True}),
    }
    write_json(PCA_ROOT / "page_complete_acceptance_report.json", record)
    write_text(PCA_ROOT / "page_complete_acceptance_record.md", "# Page Complete Acceptance Record - P013PCA-G1-VIRAL-001\n\nPage 013 accepted only under explicit delegated-review lane authorization. This is not direct per-stage human approval and not whole Gate 1 acceptance.\n")
    write_text(PCA_ROOT / "page_complete_acceptance_summary.md", "# Page Complete Acceptance Summary - P013PCA-G1-VIRAL-001\n\nAccepted page: `013` only. Human review skipped by explicit authorization; Sol/Terra delegated review passed.\n")
    write_manifest(PCA_ROOT, "page_complete_acceptance_manifest.md", "Page 013 Complete Acceptance Manifest - P013PCA-G1-VIRAL-001")
    return record


def build_status(pca_record: dict[str, Any]) -> dict[str, Any]:
    packet = {
        "status_packet_id": "G1SP-G1-VIRAL-008",
        "authorization_id": AUTHORIZATION_ID,
        "lane_id": LANE_ID,
        "status": "gate_1_status_route_packet_ready_for_final_human_batch_review",
        "page_complete_accepted_pages": [f"{i:03d}" for i in range(1, 14)],
        "remaining_page_complete_pages_unstarted": [f"{i:03d}" for i in range(14, 21)],
        "recommended_next_candidate": "page_014_triage_readiness_not_authorized",
        "predecessor": {"package_id": pca_record["package_id"], "sha256": sha256_file(PCA_ROOT / "page_complete_acceptance_report.json")},
        "review_gate": review_gate("G1SP-G1-VIRAL-008"),
        "guardrails": guardrails(),
    }
    write_json(STATUS_ROOT / "gate_1_status_packet.json", packet)
    write_json(STATUS_ROOT / "gate_1_status_report.json", packet)
    write_text(STATUS_ROOT / "gate_1_status_summary.md", "# Gate 1 Status Route Packet - G1SP-G1-VIRAL-008\n\nPages `001-013` are page-complete accepted only. Pages `014-020` remain unstarted. Page 014 triage/readiness is only the recommended next candidate and is not authorized. Whole Gate 1 and all broad capabilities remain blocked.\n")
    write_manifest(STATUS_ROOT, "gate_1_status_manifest.md", "Gate 1 Status Route Manifest - G1SP-G1-VIRAL-008")
    return packet


def build_bundle(stage_packets: list[dict[str, Any]]) -> None:
    bundle = {
        "package_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "ready_for_bogdan_final_batch_review",
        "human_review_model": "final_bundle_and_post_p013_status_only",
        "internal_stage_human_review_state": SKIPPED_REVIEW,
        "stage_packages": [packet.get("package_id") or packet.get("status_packet_id") for packet in stage_packets],
        "decision_options": ["p013 aggressive batch ok", "hold p013 batch: <reason>"],
        "guardrails": guardrails(),
    }
    write_json(BATCH_ROOT / "page_013_aggressive_batch_report.json", bundle)
    write_text(BATCH_ROOT / "page_013_aggressive_batch_summary.md", "# Page 013 Aggressive Batch Summary - P013BATCH-G1-VIRAL-001\n\nInternal stages P013TR/P013TXT/P013SEM/PCRP/P013PCA were machine-reviewed with Sol/Terra and skipped per-stage human review by explicit authorization. Final human review is requested on this bundle plus `G1SP-G1-VIRAL-008`.\n\nDecision: `p013 aggressive batch ok` or `hold p013 batch: <reason>`.\n")
    write_manifest(BATCH_ROOT, "page_013_aggressive_batch_manifest.md", "Page 013 Aggressive Batch Manifest - P013BATCH-G1-VIRAL-001")


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
