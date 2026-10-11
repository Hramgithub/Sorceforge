from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from display_structure_labels import normalize_draft_structure_lines

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_004_context_decision.py"
TEST_PATH = ROOT / "tests" / "test_page_004_context_decision.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-004-CONTEXT-DECISION-001"
PACKAGE_ID = "P004CDP-G1-VIRAL-001"
PAGE = "004"
OUT_ROOT = TRIAL_ROOT / "page_004_context_decision_G1_VIRAL_001"
ASSETS_ROOT = OUT_ROOT / "review_assets"

PAGE_IMAGE = TRIAL_ROOT / "images" / "page_004.png"
SOURCE_REVIEW_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_004"
SOURCE_REVIEW_REPORT = SOURCE_REVIEW_ROOT / "source_reconstruction_next_slice_report.json"
SOURCE_REVIEW_PACKET = SOURCE_REVIEW_ROOT / "human_review_packet.md"
BLOCK_R02 = SOURCE_REVIEW_ROOT / "region_refs" / "1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png"
BLOCK_R03 = SOURCE_REVIEW_ROOT / "region_refs" / "2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png"
SOURCE_ACCEPTANCE_ROOT = TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001"
SOURCE_ACCEPTANCE_REPORT = SOURCE_ACCEPTANCE_ROOT / "p004_verified_review_acceptance_report.json"
SOURCE_ACCEPTANCE_MANIFEST = SOURCE_ACCEPTANCE_ROOT / "p004_verified_review_acceptance_manifest.md"
SOURCE_ACCEPTANCE_SUMMARY = SOURCE_ACCEPTANCE_ROOT / "p004_verified_review_acceptance_summary.md"

SOURCE_REVIEW_REPORT_SHA256 = "C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A"
SOURCE_REVIEW_PACKET_SHA256 = "1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446"
SOURCE_ACCEPTANCE_REPORT_SHA256 = "0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E"
SOURCE_ACCEPTANCE_MANIFEST_SHA256 = "75C0C0BD96FF77E64D2F7C827D7D21B12F7EF15964E8EC9734F9428CCC064C06"
SOURCE_ACCEPTANCE_SUMMARY_SHA256 = "BF664162A899765C3B614F87002792D213D70DB82A7ED4142686AA439D50C64C"
PAGE_IMAGE_SHA256 = "45A61639C922FD6CCD085BA259BA114DD92FBCB96E86A17D216F5387DCCA9B88"
BLOCK_R02_SHA256 = "ADD3C344100356249BF38C85A7C89D2A2DB9FF23B48141509A47F86C6A32C219"
BLOCK_R03_SHA256 = "EFB82E2F8ECE14585CFD83F71C301B7024C437680703B18765A259A7E3B234C8"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build page 004 context-only decision packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--page", required=True)
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 004 context decision is fail-closed; pass --execute with exact authorization id")
    if args.page != PAGE:
        raise SystemExit(f"context decision profile exists only for page {PAGE}")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 004 context decision requires {AUTHORIZATION_ID}")
    return args


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_inputs() -> tuple[dict[str, Any], dict[str, Any]]:
    verify_authorization_ledger()
    expected = {
        SOURCE_REVIEW_REPORT: SOURCE_REVIEW_REPORT_SHA256,
        SOURCE_REVIEW_PACKET: SOURCE_REVIEW_PACKET_SHA256,
        SOURCE_ACCEPTANCE_REPORT: SOURCE_ACCEPTANCE_REPORT_SHA256,
        SOURCE_ACCEPTANCE_MANIFEST: SOURCE_ACCEPTANCE_MANIFEST_SHA256,
        SOURCE_ACCEPTANCE_SUMMARY: SOURCE_ACCEPTANCE_SUMMARY_SHA256,
        PAGE_IMAGE: PAGE_IMAGE_SHA256,
        BLOCK_R02: BLOCK_R02_SHA256,
        BLOCK_R03: BLOCK_R03_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256_file(path) != expected_hash:
            raise SystemExit(f"page 004 context decision predecessor hash mismatch: {path.relative_to(ROOT).as_posix()}")

    review = read_json(SOURCE_REVIEW_REPORT)
    acceptance = read_json(SOURCE_ACCEPTANCE_REPORT)
    context_region = acceptance["crop_guardrail"]["context_region_policy"]
    if review["package_id"] != "SRCR-G1-VIRAL-004":
        raise SystemExit("unexpected page 004 source review package")
    if acceptance["package_id"] != "P004A-G1-VIRAL-004":
        raise SystemExit("unexpected page 004 source acceptance package")
    if context_region["source_region_id"] != "PRM-G1-VIRAL-001-P004-R01":
        raise SystemExit("unexpected context-only region")
    if context_region["status"] != "context_only_not_peer_crop_record":
        raise SystemExit("page 004 full tilted inset is not marked context-only")
    if acceptance["page_complete_acceptance"] is not False:
        raise SystemExit("predecessor must not already accept page 004 as complete")
    if acceptance["fixture_admission"] is not False or acceptance["whole_gate_1_acceptance"] is not False:
        raise SystemExit("predecessor breached fixture/Gate boundary")
    return review, acceptance


def build_block_text_md(review_packet_text: str) -> str:
    return normalize_draft_structure_lines(review_packet_text)


def copy_review_assets() -> list[dict[str, str]]:
    ASSETS_ROOT.mkdir(parents=True, exist_ok=True)
    assets = [
        ("P004-ATT-PAGE", "source_page_image", PAGE_IMAGE, ASSETS_ROOT / "page_004.png"),
        ("P004-ATT-BLOCK-R02", "block_crop", BLOCK_R02, ASSETS_ROOT / BLOCK_R02.name),
        ("P004-ATT-BLOCK-R03", "block_crop", BLOCK_R03, ASSETS_ROOT / BLOCK_R03.name),
    ]
    result: list[dict[str, str]] = []
    for attachment_id, role, source, dest in assets:
        shutil.copy2(source, dest)
        result.append(
            {
                "attachment_id": attachment_id,
                "role": role,
                "source_path": source.relative_to(ROOT).as_posix(),
                "package_path": dest.relative_to(OUT_ROOT).as_posix(),
                "sha256": sha256_file(dest),
            }
        )

    block_text = ASSETS_ROOT / "page_004_ocr_block_text.md"
    block_text.write_text(build_block_text_md(SOURCE_REVIEW_PACKET.read_text(encoding="utf-8-sig")), encoding="utf-8", newline="\n")
    result.append(
        {
            "attachment_id": "P004-ATT-BLOCK-TEXT",
            "role": "ocr_block_text_markdown",
            "source_path": SOURCE_REVIEW_PACKET.relative_to(ROOT).as_posix(),
            "package_path": block_text.relative_to(OUT_ROOT).as_posix(),
            "sha256": sha256_file(block_text),
        }
    )
    return result


def build_report(review: dict[str, Any], acceptance: dict[str, Any], attachments: list[dict[str, str]]) -> dict[str, Any]:
    accepted_records = acceptance["source_acceptance"]["accepted_records"]
    context_region = acceptance["crop_guardrail"]["context_region_policy"]
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "ready_for_bogdan_page_004_context_only_decision",
        "scope": "page_004_context_only_decision_packet_no_acceptance",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        },
        "page": PAGE,
        "page_id": "PG-G1-VIRAL-P004",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P004",
        "input_packages": [review["package_id"], acceptance["package_id"]],
        "review_attachments": attachments,
        "context_decision": {
            "requires_bogdan_decision": True,
            "context_region_id": context_region["source_region_id"],
            "proposed_status": context_region["status"],
            "reason": context_region["reason"],
            "full_tilted_inset": True,
            "display_normalization": {
                "scope": "review_asset_only",
                "rule": "body-only text blocks use text_body instead of none in human-facing structure labels",
                "predecessor_source_review_packet_mutated": False,
            },
            "accepted_peer_records": [
                {
                    "source_region_id": record["source_region_id"],
                    "role": record["accepted_structure"][0]["semantic_role"],
                    "review_id": record["review_id"],
                    "crop_reference": record["crop_reference"],
                    "crop_reference_sha256": record["crop_reference_sha256"],
                    "accepted_text_sha256": record["accepted_text_sha256"],
                }
                for record in accepted_records
            ],
            "recommendation": "confirm_PRM-G1-VIRAL-001-P004-R01_as_context_only_before_page_map_readiness",
            "decision_options": [
                "confirm_page_004_full_tilted_inset_context_only",
                "hold_page_004_context_decision_for_additional_review",
            ],
        },
        "predecessors": {
            "source_review": {
                "package_id": review["package_id"],
                "report_sha256": SOURCE_REVIEW_REPORT_SHA256,
                "packet_sha256": SOURCE_REVIEW_PACKET_SHA256,
            },
            "source_acceptance": {
                "package_id": acceptance["package_id"],
                "report_sha256": SOURCE_ACCEPTANCE_REPORT_SHA256,
                "manifest_sha256": SOURCE_ACCEPTANCE_MANIFEST_SHA256,
                "summary_sha256": SOURCE_ACCEPTANCE_SUMMARY_SHA256,
            },
        },
        "guardrails": {
            "ocr_executed": False,
            "pdf_opened_or_parsed": False,
            "pdf_text_layer_used": False,
            "render_executed": False,
            "raw_artifacts_modified": False,
            "source_acceptance_created_or_mutated": False,
            "page_complete_acceptance_created": False,
            "accepted_pages_as_complete": [],
            "whole_gate_1_acceptance_created": False,
            "fixture_admission": False,
            "translation_authorized": False,
            "proofreading_authorized": False,
            "renderer_profile_acceptance": False,
            "implementation_authorized": False,
            "push_authorized": False,
        },
    }


def build_packet(report: dict[str, Any]) -> str:
    decision = report["context_decision"]
    peer_lines = []
    for record in decision["accepted_peer_records"]:
        peer_lines.extend(
            [
                f"### {record['source_region_id']} - {record['role']}",
                "",
                f"- Review id: `{record['review_id']}`",
                f"- Crop: `{record['crop_reference']}`",
                f"- Crop SHA-256: `{record['crop_reference_sha256']}`",
                f"- Accepted text SHA-256: `{record['accepted_text_sha256']}`",
                "",
            ]
        )
    attachment_lines = [
        f"- `{asset['package_path']}` - {asset['role']}, SHA-256 `{asset['sha256']}`"
        for asset in report["review_attachments"]
    ]
    lines = [
        "# Page 004 Context-Only Decision Packet",
        "",
        f"Package: `{report['package_id']}`",
        "",
        "Status: `ready_for_bogdan_page_004_context_only_decision`",
        "",
        "Boundary: this is a context-only decision packet. It does not accept page 004 as complete, does not advance Gate 1, and does not admit fixtures.",
        "",
        "## Proposed Context Decision",
        "",
        f"- Region: `{decision['context_region_id']}`",
        f"- Proposed status: `{decision['proposed_status']}`",
        f"- Reason: {decision['reason']}",
        "- Full tilted inset: yes.",
        "- Accepted peer text records remain the title/body records below.",
        "",
        "## Accepted Peer Records",
        "",
        *peer_lines,
        "## Review Attachments",
        "",
        *attachment_lines,
        "",
        "## Decision Needed",
        "",
        "Bogdan can now decide whether the full tilted inset should remain context-only before page-map readiness for page 004.",
        "",
        "Reply shape:",
        "",
        "```text",
        "page 004 context-only ok",
        "```",
        "",
        "or:",
        "",
        "```text",
        "hold page 004 context-only: <reason>",
        "```",
        "",
        "This packet itself creates no page-complete acceptance.",
        "",
    ]
    return "\n".join(lines)


def build_summary(report: dict[str, Any]) -> str:
    decision = report["context_decision"]
    return "\n".join(
        [
            "# Page 004 Context-Only Decision Summary",
            "",
            f"Package: `{report['package_id']}`",
            "",
            f"- Proposed decision: `{decision['context_region_id']}` remains `context_only_not_peer_crop_record`.",
            "- Reason: full tilted inset contains the title/body regions and would overlap peer crops under the global crop layout guardrail.",
            "- Accepted peer records: 2.",
            "- Review attachments: source page shot, 2 block shots, OCR/block text markdown.",
            "- No page-complete acceptance, whole Gate 1 acceptance, fixture admission, OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, or push was created.",
            "- Result: ready for Bogdan's explicit context-only decision.",
            "",
        ]
    )


def build_manifest(package_id: str, out_root: Path) -> str:
    lines = [
        "# Page 004 Context-Only Decision Manifest",
        "",
        f"Package: `{package_id}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(out_root.rglob("*")):
        if path.is_file() and path.name != "page_004_context_decision_manifest.md":
            lines.append(f"| `{path.relative_to(out_root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def build() -> None:
    review, acceptance = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    attachments = copy_review_assets()
    report = build_report(review, acceptance, attachments)
    write_json(OUT_ROOT / "page_004_context_decision_report.json", report)
    (OUT_ROOT / "page_004_context_decision_packet.md").write_text(build_packet(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "page_004_context_decision_summary.md").write_text(build_summary(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "page_004_context_decision_manifest.md").write_text(
        build_manifest(report["package_id"], OUT_ROOT), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    parsed = check_authorization()
    build()
