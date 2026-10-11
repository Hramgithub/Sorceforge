from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
G1RP_ROOT = TRIAL_ROOT / "gate_1_review_packet_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_review_decision_brief_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001"
BRIEF_ID = "G1RDB-G1-VIRAL-001"
G1RP_REPORT_SHA256 = "AE3695954BE26DB60EB541CD9819532CE5CA98F961D0F0B21F06C0BE5F96D990"
G1RP_MANIFEST_SHA256 = "E21D57630A3AB235AE901D3A27375F16527A81F0DE584D80EEA5527AA382DE86"
G1RP_PACKET_SHA256 = "8197860F5176CB25423D6CE6EDB30B831E603D369C100A3F79105620894EDCF9"
G1RP_SUMMARY_SHA256 = "93424483B2C870028A2330F79C81F0A3C270A2E5A9085314D4687C89D2F628EC"
ACCEPTED_PROTOCOL_REVISION = "5ee1760f"


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
    parser = argparse.ArgumentParser(description="Prepare Gate 1 review decision brief without deciding Gate 1.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 review decision brief is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 review decision brief requires {AUTHORIZATION_ID}")


def verify_packet(report: dict[str, object], packet: dict[str, object]) -> None:
    if report["packet_id"] != "G1RP-G1-VIRAL-001" or packet["packet_id"] != "G1RP-G1-VIRAL-001":
        raise SystemExit("unexpected Gate 1 review packet id")
    if report["status"] != "gate_1_review_packet_ready_not_advanced":
        raise SystemExit("unexpected Gate 1 review packet status")
    if report["gate_1_review_packet_ready"] is not True or report["gate_1_advancement"] is not False:
        raise SystemExit("Gate 1 review packet flags are unsafe")
    for key in [
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
        "translation_authorized",
        "proofreading_authorized",
        "renderer_profile_acceptance",
        "implementation_authorized",
    ]:
        if report[key] is not False:
            raise SystemExit(f"unsafe packet boundary flag: {key}")
    if report["summary"] != {
        "packet_items": 7,
        "positive_source_text_items": 4,
        "negative_visual_exclusion_items": 3,
        "blocked_items": 0,
        "gate_1_advanced_items": 0,
    }:
        raise SystemExit("unexpected packet summary")
    if len(packet["packet_items"]) != 7:
        raise SystemExit("unexpected packet item count")


def decision_question() -> dict[str, object]:
    return {
        "question_number": 1,
        "subject": "G1RP-G1-VIRAL-001",
        "question": "Accept this exact Gate 1 review packet as the Gate 1 source-reconstruction evidence slice for Viral?",
        "accepted_answer_format": [
            "1 - принять",
            "1 - hold: <blocker>",
            "1 - reject: <reason>",
            "1 - park: <exact scope/rationale>",
        ],
        "acceptance_scope": "exact_G1RP_G1_VIRAL_001_source_reconstruction_evidence_slice_only",
        "not_authorized_by_acceptance": [
            "whole_gate_1_acceptance",
            "translation",
            "proofreading",
            "renderer_profile_acceptance",
            "implementation",
            "push",
        ],
    }


def non_waivable_checklist() -> list[dict[str, object]]:
    return [
        {"check": "exact_scope_only", "status": "ready", "detail": "Decision brief is limited to G1RP-G1-VIRAL-001."},
        {"check": "no_stale_lineage", "status": "ready", "detail": "G1RP hashes match committed packet artifacts."},
        {"check": "no_unresolved_blocking_items", "status": "ready", "detail": "Packet blocked_items is 0."},
        {"check": "no_missing_qa_coverage", "status": "ready", "detail": "All seven SRFA fixtures are included in the packet."},
        {"check": "no_waiver_or_parking_bypass", "status": "ready", "detail": "No waiver or parking is applied by this brief."},
        {"check": "no_pdf_text_layer_leakage", "status": "ready", "detail": "Packet consumes only committed SRFA/G1RP JSON and Markdown hashes."},
        {"check": "no_unauthorized_ocr_pdf_render_raw_mutation", "status": "ready", "detail": "All boundary flags remain false."},
        {"check": "r003_metadata_not_source_mutation", "status": "ready", "detail": "R003 crop correction and heading hint remain metadata."},
    ]


def build() -> None:
    report_path = G1RP_ROOT / "gate_1_review_packet_report.json"
    manifest_path = G1RP_ROOT / "gate_1_review_packet_manifest.md"
    packet_path = G1RP_ROOT / "gate_1_review_packet.json"
    summary_path = G1RP_ROOT / "gate_1_review_packet_summary.md"
    if sha256_file(report_path) != G1RP_REPORT_SHA256:
        raise SystemExit("G1RP report hash mismatch")
    if sha256_file(manifest_path) != G1RP_MANIFEST_SHA256:
        raise SystemExit("G1RP manifest hash mismatch")
    if sha256_file(packet_path) != G1RP_PACKET_SHA256:
        raise SystemExit("G1RP packet hash mismatch")
    if sha256_file(summary_path) != G1RP_SUMMARY_SHA256:
        raise SystemExit("G1RP summary hash mismatch")

    report = read_json(report_path)
    packet = read_json(packet_path)
    verify_packet(report, packet)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    brief = {
        "brief_id": BRIEF_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_review_decision_brief_ready_requires_bogdan",
        "input_packet_id": "G1RP-G1-VIRAL-001",
        "accepted_protocol_revision": ACCEPTED_PROTOCOL_REVISION,
        "input_packet_report_sha256": G1RP_REPORT_SHA256,
        "input_packet_manifest_sha256": G1RP_MANIFEST_SHA256,
        "input_packet_sha256": G1RP_PACKET_SHA256,
        "input_packet_summary_sha256": G1RP_SUMMARY_SHA256,
        "upstream_fixture_admission_report_sha256": report["input_fixture_admission_report_sha256"],
        "upstream_admitted_fixtures_sha256": report["input_admitted_fixtures_sha256"],
        "upstream_fixture_admission_summary_sha256": report["input_fixture_admission_summary_sha256"],
        "upstream_qa_report_sha256": packet["upstream_qa_report_sha256"],
        "upstream_qa_summary_sha256": packet["upstream_qa_summary_sha256"],
        "review_scope": "Viral source reconstruction evidence slice from seven admitted fixtures",
        "decision_questions": [decision_question()],
        "non_waivable_checklist": non_waivable_checklist(),
        "if_accepted_requires": [
            "user_visible_gate_1_decision_record",
            "actor_authority_and_timestamp",
            "accepted_evidence_hashes",
            "unresolved_descendants_none",
            "permission_and_blocker_state_after_decision",
        ],
        "if_parked_requires": [
            "accepted_scope_revision",
            "exact_affected_units_anchors_predecessors",
            "descendant_exclusion_proof",
            "rerun_or_rollup_requirement",
            "authority_and_timestamp",
        ],
        "inherited_source_acceptance": True,
        "inherited_qa_acceptance": True,
        "fixture_admission": True,
        "gate_1_review_packet_ready": True,
        "gate_1_decision_recorded": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "summary": {
            "decision_questions": 1,
            "packet_items": report["summary"]["packet_items"],
            "positive_source_text_items": report["summary"]["positive_source_text_items"],
            "negative_visual_exclusion_items": report["summary"]["negative_visual_exclusion_items"],
            "blocking_items": report["summary"]["blocked_items"],
            "requires_bogdan_review": True,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001",
    }
    write_json(OUT_ROOT / "gate_1_review_decision_brief.json", brief)

    brief_lines = [
        "# Gate 1 Review Decision Brief - G1RDB-G1-VIRAL-001",
        "",
        "Status: `gate_1_review_decision_brief_ready_requires_bogdan`",
        "",
        "Scope: exact `G1RP-G1-VIRAL-001` source reconstruction evidence slice only.",
        "",
        "Boundary: accepting this brief must not authorize whole Gate 1 acceptance, translation, proofreading, renderer/profile acceptance, implementation, or push.",
        "",
        "## Packet Summary",
        "",
        "- Packet items: `7`",
        "- Positive source-text items: `4`",
        "- Negative visual-exclusion items: `3`",
        "- Blocking items: `0`",
        "- Gate 1 advanced: `false`",
        "",
        "## Lineage",
        "",
        "- Accepted protocol revision: `5ee1760f`",
        "- G1RP report SHA-256: `AE3695954BE26DB60EB541CD9819532CE5CA98F961D0F0B21F06C0BE5F96D990`",
        "- G1RP manifest SHA-256: `E21D57630A3AB235AE901D3A27375F16527A81F0DE584D80EEA5527AA382DE86`",
        "- G1RP payload SHA-256: `8197860F5176CB25423D6CE6EDB30B831E603D369C100A3F79105620894EDCF9`",
        "- G1RP summary SHA-256: `93424483B2C870028A2330F79C81F0A3C270A2E5A9085314D4687C89D2F628EC`",
        "- SRFA report SHA-256: `485ECEAAC7CC1CC3FBE95341ED7A0F5E68345EF59CCC8CEB7F8F57706A541A1C`",
        "- SRFA fixtures SHA-256: `1B9DA0A5BF9E219059065F3C1517B4C0E1265060F578F1C6007E9C2AA1611B9F`",
        "- SRFA summary SHA-256: `DC76D7677EE76EFBAF7BCBBF7ED7C0BED38727CC0E9EAB63C3F7F26DF2013949`",
        "- SRQA report SHA-256: `A98811F3368FD468618A111D9F7A85BFFBD72CE9387CCF11DA011875C80553E0`",
        "- SRQA summary SHA-256: `C7C32A1D4E9A74DC3F086D4D355151BF6C89DBDE576775AC0F67312E98981EC3`",
        "",
        "## Non-Waivable Checklist",
        "",
        "- no stale lineage",
        "- no unresolved/open blocking findings",
        "- no missing QA coverage",
        "- no waiver/parking bypass",
        "- no PDF text-layer leakage",
        "- no unauthorized OCR/PDF parsing/rendering/raw OCR mutation",
        "",
        "## Question For Bogdan",
        "",
        "1 - `G1RP-G1-VIRAL-001`: принять как Gate 1 source-reconstruction evidence slice?",
        "",
        "Valid short answers:",
        "",
        "- `1 - принять`",
        "- `1 - hold: <blocker>`",
        "- `1 - reject: <reason>`",
        "- `1 - park: <exact scope/rationale>`",
        "",
    ]
    (OUT_ROOT / "gate_1_review_decision_brief.md").write_text("\n".join(brief_lines), encoding="utf-8")

    report_out = {
        "brief_id": BRIEF_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_review_decision_brief_ready_requires_bogdan",
        "input_packet_id": "G1RP-G1-VIRAL-001",
        "accepted_protocol_revision": ACCEPTED_PROTOCOL_REVISION,
        "input_packet_report_sha256": G1RP_REPORT_SHA256,
        "input_packet_manifest_sha256": G1RP_MANIFEST_SHA256,
        "input_packet_sha256": G1RP_PACKET_SHA256,
        "input_packet_summary_sha256": G1RP_SUMMARY_SHA256,
        "generator_script": "scripts/prepare_gate_1_review_decision_brief.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_gate_1_review_decision_brief.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_gate_1_review_decision_brief.py")
        if (ROOT / "tests" / "test_gate_1_review_decision_brief.py").exists()
        else None,
        "requires_bogdan_review": True,
        "gate_1_decision_recorded": False,
        "gate_1_advancement": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "decision_question_count": 1,
    }
    write_json(OUT_ROOT / "gate_1_review_decision_brief_report.json", report_out)

    summary_lines = [
        "# Gate 1 Review Decision Brief Summary - G1RDB-G1-VIRAL-001",
        "",
        "Status: `gate_1_review_decision_brief_ready_requires_bogdan`",
        "",
        "- Decision questions: `1`",
        "- Requires Bogdan review: `true`",
        "- Gate 1 decision recorded: `false`",
        "- Gate 1 advanced: `false`",
        "",
    ]
    (OUT_ROOT / "gate_1_review_decision_brief_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    manifest_lines = [
        "# Gate 1 Review Decision Brief Manifest - G1RDB-G1-VIRAL-001",
        "",
        "Status: `gate_1_review_decision_brief_ready_requires_bogdan`",
        "",
        "Boundary: no OCR, PDF parsing, rendering, raw OCR edits, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_review_decision_brief_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "gate_1_review_decision_brief_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    check_authorization()
    build()
