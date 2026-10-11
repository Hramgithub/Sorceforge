from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_page_001_complete.py"
TEST_PATH = ROOT / "tests" / "test_page_001_complete_acceptance.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P001-001"
PACKAGE_ID = "P001PCA-G1-VIRAL-001"
PAGE = "001"
OUT_ROOT = TRIAL_ROOT / "page_complete_acceptance_p001_G1_VIRAL_001"
REVIEW_ROOT = TRIAL_ROOT / "page_complete_review_p001_G1_VIRAL_001"
REVIEW_REPORT = REVIEW_ROOT / "page_complete_review_report.json"
REVIEW_PACKET = REVIEW_ROOT / "page_complete_review_packet.md"
REVIEW_SUMMARY = REVIEW_ROOT / "page_complete_review_summary.md"
REVIEW_MANIFEST = REVIEW_ROOT / "page_complete_review_manifest.md"

REVIEW_REPORT_SHA256 = "7ECD5487CA3CA8F5931C70C536BD7BCB774163A970930226A71453DB35F763FE"
REVIEW_PACKET_SHA256 = "D430A2A3DF4A7600991974D7A46A948411576E7E4532784B894E27800E3F2D81"
REVIEW_SUMMARY_SHA256 = "34BDABDAB67C6BC8FC3A9D2E7CEA7C4C6591B58433B6D10C8555E850187E9DC6"
REVIEW_MANIFEST_SHA256 = "517E18CED782C0B1C71E14C872E5A5EF6F202407D6C10932120EB34907224831"


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
    parser = argparse.ArgumentParser(description="Accept page 001 as complete under exact bounded authorization.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--page", required=True)
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 001 complete acceptance is fail-closed; pass --execute with exact authorization id")
    if args.page != PAGE:
        raise SystemExit(f"page-complete acceptance profile exists only for page {PAGE}")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 001 complete acceptance requires {AUTHORIZATION_ID}")
    return args


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_review_packet() -> dict[str, Any]:
    verify_authorization_ledger()
    expected = {
        REVIEW_REPORT: REVIEW_REPORT_SHA256,
        REVIEW_PACKET: REVIEW_PACKET_SHA256,
        REVIEW_SUMMARY: REVIEW_SUMMARY_SHA256,
        REVIEW_MANIFEST: REVIEW_MANIFEST_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256_file(path) != expected_hash:
            raise SystemExit(f"page-complete review predecessor hash mismatch: {path.relative_to(ROOT).as_posix()}")

    report = read_json(REVIEW_REPORT)
    if report["package_id"] != "PCRP-G1-VIRAL-P001-001":
        raise SystemExit("unexpected page-complete review package")
    if report["status"] != "ready_for_bogdan_page_complete_decision":
        raise SystemExit("page-complete review packet is not ready for Bogdan decision")
    if report["review_decision"]["page_complete_acceptance_created"] is not False:
        raise SystemExit("review packet must not already create page-complete acceptance")
    if report["page_complete_review"]["blockers"]:
        raise SystemExit("review packet contains blockers")
    if report["page_complete_review"]["open_questions"]:
        raise SystemExit("review packet contains open questions")
    if report["page_complete_review"]["reviewed_blocks"] != 3 or report["page_complete_review"]["ready_blocks"] != 3:
        raise SystemExit("page 001 review packet must have 3/3 ready visual anchors")
    if report["page_complete_review"]["structural_findings"]:
        raise SystemExit("review packet contains structural findings")
    if report["guardrails"]["ocr_executed"] is not False or report["guardrails"]["render_executed"] is not False:
        raise SystemExit("review packet breached OCR/render guardrail")
    return report


def build_report(review: dict[str, Any]) -> dict[str, Any]:
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_001_complete_accepted",
        "scope": "page_001_complete_acceptance_only",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        },
        "page": PAGE,
        "page_id": review["page_id"],
        "image_id": review["image_id"],
        "input_packages": [review["package_id"]],
        "review_input": {
            "package_id": review["package_id"],
            "authorization_id": review["authorization_id"],
            "report_sha256": REVIEW_REPORT_SHA256,
            "packet_sha256": REVIEW_PACKET_SHA256,
            "summary_sha256": REVIEW_SUMMARY_SHA256,
            "manifest_sha256": REVIEW_MANIFEST_SHA256,
        },
        "human_decision": {
            "telegram_message_id": "1257",
            "decision": "page 001 complete ok",
            "raw_text": "ok",
        },
        "page_complete_acceptance": {
            "acceptance_id": "P001-PAGE-COMPLETE-ACCEPTANCE-001",
            "accepted": True,
            "accepted_page": PAGE,
            "accepted_pages_as_complete": [PAGE],
            "basis": "PCRP-G1-VIRAL-P001-001 with 3/3 ready visual/title anchors, no blockers, no open questions, and Bogdan explicit ok",
            "reviewed_blocks": review["page_complete_review"]["reviewed_blocks"],
            "ready_blocks": review["page_complete_review"]["ready_blocks"],
            "reading_order": review["page_complete_review"]["reading_order"],
            "declared_none_categories": review["page_complete_review"]["declared_none_categories"],
            "blockers": [],
            "open_questions": [],
        },
        "guardrails": {
            "only_page_001_accepted_as_complete": True,
            "accepted_pages_as_complete": [PAGE],
            "whole_gate_1_acceptance_created": False,
            "fixture_admission": False,
            "source_acceptance_created_or_mutated": False,
            "ocr_executed": False,
            "pdf_opened_or_parsed": False,
            "pdf_text_layer_used": False,
            "render_executed": False,
            "raw_artifacts_modified": False,
            "translation_authorized": False,
            "proofreading_authorized": False,
            "renderer_profile_acceptance": False,
            "implementation_authorized": False,
            "push_authorized": False,
        },
    }


def build_record(report: dict[str, Any]) -> str:
    acceptance = report["page_complete_acceptance"]
    return "\n".join(
        [
            "# Page Complete Acceptance Record - Page 001",
            "",
            f"Package: `{report['package_id']}`",
            "",
            "Status: `page_001_complete_accepted`",
            "",
            "Decision: page 001 is accepted as complete.",
            "",
            "Basis:",
            "",
            "- Review input: `PCRP-G1-VIRAL-P001-001`.",
            f"- Reviewed blocks: {acceptance['reviewed_blocks']}.",
            f"- Ready blocks: {acceptance['ready_blocks']} / {acceptance['reviewed_blocks']}.",
            f"- Reading order: {' -> '.join(acceptance['reading_order'])}.",
            "- Blockers: none.",
            "- Open questions: none.",
            "- Bogdan decision: `page 001 complete ok`.",
            "",
            "Limits:",
            "",
            "- Only page 001 is accepted as complete.",
            "- Whole Gate 1 is not accepted.",
            "- No fixture admission is created.",
            "- No source acceptance is created or mutated.",
            "- No OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, or push is created.",
            "",
        ]
    )


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# Page Complete Acceptance Summary - Page 001",
            "",
            f"Package: `{report['package_id']}`",
            "",
            "- Page 001 is accepted as complete under Bogdan's explicit `page 001 complete ok` decision.",
            "- Basis: `PCRP-G1-VIRAL-P001-001` page-complete review packet.",
            "- Accepted pages as complete: page 001 only.",
            "- Whole Gate 1 is not accepted.",
            "- No fixture admission, source acceptance mutation, OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, or push was created.",
            "",
        ]
    )


def build_manifest(package_id: str, out_root: Path) -> str:
    lines = [
        "# Page Complete Acceptance Manifest",
        "",
        f"Package: `{package_id}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(out_root.rglob("*")):
        if path.is_file() and path.name != "page_complete_acceptance_manifest.md":
            lines.append(f"| `{path.relative_to(out_root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def build() -> None:
    review = verify_review_packet()
    report = build_report(review)
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    write_json(OUT_ROOT / "page_complete_acceptance_report.json", report)
    (OUT_ROOT / "page_complete_acceptance_record.md").write_text(build_record(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "page_complete_acceptance_summary.md").write_text(build_summary(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "page_complete_acceptance_manifest.md").write_text(
        build_manifest(report["package_id"], OUT_ROOT), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    parsed = check_authorization()
    build()
