from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
BRIEF_ROOT = TRIAL_ROOT / "gate_1_review_decision_brief_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_review_decision_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001"
DECISION_ID = "G1RD-G1-VIRAL-001"
BRIEF_REPORT_SHA256 = "E577B18D7E8945C39FA5286D83FD9D8607B45636ABD82243ED4A9F002B306FE8"
BRIEF_JSON_SHA256 = "3D262623ACB6111F7D50D9B2D22594AABEF06128737D4FC8445FF55B90D71E53"
BRIEF_MARKDOWN_SHA256 = "16C776322C46E969C4D63383CAE546CC5C4E12A79F1992AF5E07763D1B56C15E"
BOGDAN_DECISION_MESSAGE_ID = 303
BOGDAN_DECISION_TEXT = "1 принято"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Record Bogdan's Gate 1 review decision for exact G1RP slice.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 review decision record is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 review decision record requires {AUTHORIZATION_ID}")


def verify_brief(brief: dict[str, object]) -> None:
    if brief["brief_id"] != "G1RDB-G1-VIRAL-001":
        raise SystemExit("unexpected Gate 1 decision brief id")
    if brief["status"] != "gate_1_review_decision_brief_ready_requires_bogdan":
        raise SystemExit("unexpected Gate 1 decision brief status")
    if brief["gate_1_decision_recorded"] is not False or brief["gate_1_advancement"] is not False:
        raise SystemExit("brief already records or advances Gate 1")
    if brief["summary"] != {
        "decision_questions": 1,
        "packet_items": 7,
        "positive_source_text_items": 4,
        "negative_visual_exclusion_items": 3,
        "blocking_items": 0,
        "requires_bogdan_review": True,
    }:
        raise SystemExit("unexpected brief summary")
    for key in [
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
        "translation_authorized",
        "proofreading_authorized",
        "renderer_profile_acceptance",
        "implementation_authorized",
    ]:
        if brief[key] is not False:
            raise SystemExit(f"unsafe brief boundary flag: {key}")


def build() -> None:
    brief_report_path = BRIEF_ROOT / "gate_1_review_decision_brief_report.json"
    brief_json_path = BRIEF_ROOT / "gate_1_review_decision_brief.json"
    brief_markdown_path = BRIEF_ROOT / "gate_1_review_decision_brief.md"
    if sha256_file(brief_report_path) != BRIEF_REPORT_SHA256:
        raise SystemExit("decision brief report hash mismatch")
    if sha256_file(brief_json_path) != BRIEF_JSON_SHA256:
        raise SystemExit("decision brief JSON hash mismatch")
    if sha256_file(brief_markdown_path) != BRIEF_MARKDOWN_SHA256:
        raise SystemExit("decision brief Markdown hash mismatch")

    brief = read_json(brief_json_path)
    verify_brief(brief)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    decision = {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_source_reconstruction_evidence_slice_accepted",
        "input_brief_id": "G1RDB-G1-VIRAL-001",
        "input_packet_id": "G1RP-G1-VIRAL-001",
        "input_brief_report_sha256": BRIEF_REPORT_SHA256,
        "input_brief_json_sha256": BRIEF_JSON_SHA256,
        "input_brief_markdown_sha256": BRIEF_MARKDOWN_SHA256,
        "direct_packet_lineage": {
            "packet_id": "G1RP-G1-VIRAL-001",
            "packet_report_sha256": brief["input_packet_report_sha256"],
            "packet_manifest_sha256": brief["input_packet_manifest_sha256"],
            "packet_payload_sha256": brief["input_packet_sha256"],
            "packet_summary_sha256": brief["input_packet_summary_sha256"],
        },
        "user_decision": {
            "actor": "Bogdan",
            "telegram_message_id": BOGDAN_DECISION_MESSAGE_ID,
            "raw_text": BOGDAN_DECISION_TEXT,
            "normalized_decision": "accept",
            "accepted_answer": "1 - принять",
            "decision_timestamp": "2026-07-18T15:28:14Z",
        },
        "accepted_scope": "exact_G1RP_G1_VIRAL_001_source_reconstruction_evidence_slice_only",
        "accepted_records": 7,
        "accepted_source_text_records": 4,
        "accepted_visual_exclusion_records": 3,
        "accepted_pages_as_complete": False,
        "whole_gate_1_acceptance": False,
        "gate_1_source_reconstruction_evidence_slice_accepted": True,
        "gate_1_decision_recorded": True,
        "gate_1_advancement": True,
        "gate_1_advancement_scope": "seven_reviewed_records_only_pages_not_complete",
        "source_acceptance": "inherited_from_SRHR_for_exact_records",
        "qa_acceptance": "inherited_from_SRQA_for_exact_records",
        "fixture_admission": "inherited_from_SRFA_for_exact_records",
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "non_waivable_result": {
            "blocking_items": 0,
            "missing_qa_coverage": False,
            "stale_lineage": False,
            "waiver_or_parking_bypass": False,
            "pdf_text_layer_leakage": False,
            "unauthorized_ocr_pdf_render_raw_mutation": False,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001",
    }
    write_json(OUT_ROOT / "gate_1_review_decision_record.json", decision)

    markdown_lines = [
        "# Gate 1 Review Decision Record - G1RD-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_reconstruction_evidence_slice_accepted`",
        "",
        "Decision: Bogdan accepted exact `G1RP-G1-VIRAL-001` as a narrow Gate 1 source-reconstruction evidence slice.",
        "",
        "## Accepted Scope",
        "",
        "- Accepted records: `7`",
        "- Accepted source-text records: `4`",
        "- Accepted visual-exclusion records: `3`",
        "- Pages accepted as complete: `false`",
        "- Whole Gate 1 accepted: `false`",
        "- Translation authorized: `false`",
        "- Proofreading authorized: `false`",
        "- Renderer/profile acceptance: `false`",
        "- Implementation authorized: `false`",
        "",
        "## User Decision",
        "",
        "- Telegram message id: `303`",
        "- Raw text: `1 принято`",
        "- Normalized decision: `1 - принять`",
        "",
    ]
    (OUT_ROOT / "gate_1_review_decision_record.md").write_text("\n".join(markdown_lines), encoding="utf-8")

    report = {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_source_reconstruction_evidence_slice_accepted",
        "input_brief_id": "G1RDB-G1-VIRAL-001",
        "input_brief_report_sha256": BRIEF_REPORT_SHA256,
        "input_brief_json_sha256": BRIEF_JSON_SHA256,
        "input_brief_markdown_sha256": BRIEF_MARKDOWN_SHA256,
        "direct_packet_lineage": {
            "packet_id": "G1RP-G1-VIRAL-001",
            "packet_report_sha256": brief["input_packet_report_sha256"],
            "packet_manifest_sha256": brief["input_packet_manifest_sha256"],
            "packet_payload_sha256": brief["input_packet_sha256"],
            "packet_summary_sha256": brief["input_packet_summary_sha256"],
        },
        "generator_script": "scripts/record_gate_1_review_decision.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_gate_1_review_decision.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_gate_1_review_decision.py")
        if (ROOT / "tests" / "test_gate_1_review_decision.py").exists()
        else None,
        "accepted_records": 7,
        "accepted_pages_as_complete": False,
        "whole_gate_1_acceptance": False,
        "gate_1_decision_recorded": True,
        "gate_1_advancement": True,
        "gate_1_advancement_scope": "seven_reviewed_records_only_pages_not_complete",
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "requires_rollup_before_broader_gate_use": True,
    }
    write_json(OUT_ROOT / "gate_1_review_decision_report.json", report)

    summary_lines = [
        "# Gate 1 Review Decision Summary - G1RD-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_reconstruction_evidence_slice_accepted`",
        "",
        "- Accepted records: `7`",
        "- Pages accepted as complete: `false`",
        "- Whole Gate 1 accepted: `false`",
        "- Gate 1 advancement scope: `seven_reviewed_records_only_pages_not_complete`",
        "- Translation/proofreading/renderer-profile/implementation: `false`",
        "",
    ]
    (OUT_ROOT / "gate_1_review_decision_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    manifest_lines = [
        "# Gate 1 Review Decision Manifest - G1RD-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_reconstruction_evidence_slice_accepted`",
        "",
        "Boundary: accepted records are limited to seven reviewed records; pages are not accepted as complete.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_review_decision_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "gate_1_review_decision_manifest.md").write_text("\n".join(manifest_lines), encoding="utf-8")


if __name__ == "__main__":
    check_authorization()
    build()
