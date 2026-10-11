from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "accept_page_004_context_only.py"
TEST_PATH = ROOT / "tests" / "test_page_004_context_only_acceptance.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"

AUTHORIZATION_ID = "BA-G1-VIRAL-PAGE-004-CONTEXT-ONLY-CONFIRM-001"
PACKAGE_ID = "P004COD-G1-VIRAL-001"
PAGE = "004"
OUT_ROOT = TRIAL_ROOT / "page_004_context_only_confirmation_G1_VIRAL_001"
DECISION_ROOT = TRIAL_ROOT / "page_004_context_decision_G1_VIRAL_001"
DECISION_REPORT = DECISION_ROOT / "page_004_context_decision_report.json"
DECISION_PACKET = DECISION_ROOT / "page_004_context_decision_packet.md"
DECISION_SUMMARY = DECISION_ROOT / "page_004_context_decision_summary.md"
DECISION_MANIFEST = DECISION_ROOT / "page_004_context_decision_manifest.md"

DECISION_REPORT_SHA256 = "B790887E0002F132D5CB27B6F2E7E5894183C73924C3181EAAB46374D2AF3C81"
DECISION_PACKET_SHA256 = "A638817C20AA39243A4C4FC2AC61499BF75EFAA86AF6DE2A2361781A9D622EA2"
DECISION_SUMMARY_SHA256 = "C133C0BCAE7C0322761A2B093D630D47EC67FC41E0768CF4EA5BE3A65073CAA5"
DECISION_MANIFEST_SHA256 = "FC55B5368B88B59292226D4E6A64923870ECC6A55526851C456FB43EB65D662F"


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
    parser = argparse.ArgumentParser(description="Confirm Page 004 full tilted inset as context-only.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--page", required=True)
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Page 004 context-only confirmation is fail-closed; pass --execute with exact authorization id")
    if args.page != PAGE:
        raise SystemExit(f"context-only confirmation profile exists only for page {PAGE}")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Page 004 context-only confirmation requires {AUTHORIZATION_ID}")
    return args


def verify_authorization_ledger() -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} is missing from bounded trial authorization ledger")


def verify_decision_packet() -> dict[str, Any]:
    verify_authorization_ledger()
    expected = {
        DECISION_REPORT: DECISION_REPORT_SHA256,
        DECISION_PACKET: DECISION_PACKET_SHA256,
        DECISION_SUMMARY: DECISION_SUMMARY_SHA256,
        DECISION_MANIFEST: DECISION_MANIFEST_SHA256,
    }
    for path, expected_hash in expected.items():
        if sha256_file(path) != expected_hash:
            raise SystemExit(f"page 004 context decision predecessor hash mismatch: {path.relative_to(ROOT).as_posix()}")

    report = read_json(DECISION_REPORT)
    decision = report["context_decision"]
    if report["package_id"] != "P004CDP-G1-VIRAL-001":
        raise SystemExit("unexpected page 004 context decision package")
    if report["status"] != "ready_for_bogdan_page_004_context_only_decision":
        raise SystemExit("context decision packet is not ready for Bogdan decision")
    if decision["context_region_id"] != "PRM-G1-VIRAL-001-P004-R01":
        raise SystemExit("unexpected page 004 context region")
    if decision["proposed_status"] != "context_only_not_peer_crop_record":
        raise SystemExit("unexpected proposed context-only status")
    if report["guardrails"]["page_complete_acceptance_created"] is not False:
        raise SystemExit("decision packet must not create page-complete acceptance")
    return report


def build_report(decision_report: dict[str, Any]) -> dict[str, Any]:
    decision = decision_report["context_decision"]
    return {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_004_context_only_confirmed",
        "scope": "page_004_context_region_decision_only_no_page_complete_acceptance",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        },
        "page": PAGE,
        "page_id": decision_report["page_id"],
        "image_id": decision_report["image_id"],
        "input_packages": [decision_report["package_id"]],
        "decision_input": {
            "package_id": decision_report["package_id"],
            "authorization_id": decision_report["authorization_id"],
            "report_sha256": DECISION_REPORT_SHA256,
            "packet_sha256": DECISION_PACKET_SHA256,
            "summary_sha256": DECISION_SUMMARY_SHA256,
            "manifest_sha256": DECISION_MANIFEST_SHA256,
        },
        "human_decision": {
            "telegram_message_id": "758",
            "decision": "page 004 context-only ok",
            "raw_text": "насколько вижу все правильно кропнулось, весь текст снят. всего два кропа на страницу тоже правильно. ... второй кроп - принят, `page 004 context-only ok`",
        },
        "context_only_confirmation": {
            "confirmation_id": "P004-CONTEXT-ONLY-CONFIRMATION-001",
            "accepted": True,
            "context_region_id": decision["context_region_id"],
            "confirmed_status": decision["proposed_status"],
            "reason": decision["reason"],
            "full_tilted_inset": decision["full_tilted_inset"],
            "accepted_peer_records": decision["accepted_peer_records"],
            "body_only_structure_label": "text_body",
            "predecessor_source_review_packet_mutated": False,
        },
        "guardrails": {
            "page_complete_acceptance_created": False,
            "accepted_pages_as_complete": [],
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
    confirmation = report["context_only_confirmation"]
    return "\n".join(
        [
            "# Page 004 Context-Only Confirmation Record",
            "",
            f"Package: `{report['package_id']}`",
            "",
            "Status: `page_004_context_only_confirmed`",
            "",
            f"Decision: `{confirmation['context_region_id']}` is confirmed as `context_only_not_peer_crop_record`.",
            "",
            "Basis:",
            "",
            "- Decision input: `P004CDP-G1-VIRAL-001`.",
            "- Bogdan decision: `page 004 context-only ok`.",
            "- Accepted peer records remain the two page 004 text crops.",
            "- Body-only human-facing structure label is `text_body`, not `none`.",
            "",
            "Limits:",
            "",
            "- Page 004 is not accepted as complete.",
            "- Whole Gate 1 is not accepted.",
            "- No fixture admission is created.",
            "- No source acceptance is created or mutated.",
            "- No OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, or push is created.",
            "",
        ]
    )


def build_summary(report: dict[str, Any]) -> str:
    confirmation = report["context_only_confirmation"]
    return "\n".join(
        [
            "# Page 004 Context-Only Confirmation Summary",
            "",
            f"Package: `{report['package_id']}`",
            "",
            f"- `{confirmation['context_region_id']}` is confirmed as `context_only_not_peer_crop_record` under Bogdan's explicit `page 004 context-only ok` decision.",
            "- The two page 004 peer text crops remain accepted as the title/body records.",
            "- Human-facing body-only structure label is now `text_body`, avoiding ambiguous `none` wording in review assets.",
            "- Page 004 is not accepted as complete.",
            "- Whole Gate 1, fixture admission, source acceptance mutation, OCR, render, PDF parsing/text-layer extraction, raw mutation, translation, proofreading, implementation, and push remain false.",
            "",
        ]
    )


def build_manifest(package_id: str, out_root: Path) -> str:
    lines = [
        "# Page 004 Context-Only Confirmation Manifest",
        "",
        f"Package: `{package_id}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(out_root.rglob("*")):
        if path.is_file() and path.name != "page_004_context_only_confirmation_manifest.md":
            lines.append(f"| `{path.relative_to(out_root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def build() -> None:
    decision_report = verify_decision_packet()
    report = build_report(decision_report)
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    write_json(OUT_ROOT / "page_004_context_only_confirmation_report.json", report)
    (OUT_ROOT / "page_004_context_only_confirmation_record.md").write_text(build_record(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "page_004_context_only_confirmation_summary.md").write_text(build_summary(report), encoding="utf-8", newline="\n")
    (OUT_ROOT / "page_004_context_only_confirmation_manifest.md").write_text(
        build_manifest(report["package_id"], OUT_ROOT), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    parsed = check_authorization()
    build()
