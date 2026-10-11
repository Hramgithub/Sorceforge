from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
DECISION_ROOT = TRIAL_ROOT / "gate_1_review_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_recon_evidence_rollup_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001"
ROLLUP_ID = "G1SRER-G1-VIRAL-001"
DECISION_REPORT_SHA256 = "8F1FD747C95B758B2227C6483B09D34DB37A786B7988DA68EEB721A7942547C3"
DECISION_RECORD_SHA256 = "1300B2E068B514493596156BC4A57D476491915D76EA6A0A7779FC2C14A5D271"
DECISION_MARKDOWN_SHA256 = "F896C6375C44AF002B883A8441BE3FB504D8DE5CD01962B6C04322065BEFAC9E"
DECISION_SUMMARY_SHA256 = "5F6B819DBE127847951E84CB50571FD1838278A7707E26FE0765E4C2A725A4A5"


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
    parser = argparse.ArgumentParser(description="Roll up the narrow Viral Gate 1 source reconstruction decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 source reconstruction evidence rollup is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 source reconstruction evidence rollup requires {AUTHORIZATION_ID}")


def verify_decision(decision: dict[str, object], report: dict[str, object]) -> None:
    if decision["decision_id"] != "G1RD-G1-VIRAL-001" or report["decision_id"] != "G1RD-G1-VIRAL-001":
        raise SystemExit("unexpected Gate 1 review decision id")
    if decision["status"] != "gate_1_source_reconstruction_evidence_slice_accepted":
        raise SystemExit("unexpected Gate 1 review decision status")
    if decision["accepted_records"] != 7 or decision["accepted_source_text_records"] != 4:
        raise SystemExit("unexpected accepted source reconstruction record count")
    if decision["accepted_visual_exclusion_records"] != 3:
        raise SystemExit("unexpected accepted visual exclusion count")
    if decision["accepted_pages_as_complete"] is not False or decision["whole_gate_1_acceptance"] is not False:
        raise SystemExit("decision scope is broader than the rollup can carry")
    if decision["gate_1_advancement"] is not True:
        raise SystemExit("decision did not accept the narrow Gate 1 evidence slice")
    if decision["gate_1_advancement_scope"] != "seven_reviewed_records_only_pages_not_complete":
        raise SystemExit("unexpected Gate 1 advancement scope")
    if report["requires_rollup_before_broader_gate_use"] is not True:
        raise SystemExit("decision report does not require rollup before broader use")
    for key in [
        "translation_authorized",
        "proofreading_authorized",
        "renderer_profile_acceptance",
        "implementation_authorized",
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
    ]:
        if decision[key] is not False:
            raise SystemExit(f"unsafe decision boundary flag: {key}")


def build() -> None:
    decision_report_path = DECISION_ROOT / "gate_1_review_decision_report.json"
    decision_record_path = DECISION_ROOT / "gate_1_review_decision_record.json"
    decision_markdown_path = DECISION_ROOT / "gate_1_review_decision_record.md"
    decision_summary_path = DECISION_ROOT / "gate_1_review_decision_summary.md"
    if sha256_file(decision_report_path) != DECISION_REPORT_SHA256:
        raise SystemExit("Gate 1 decision report hash mismatch")
    if sha256_file(decision_record_path) != DECISION_RECORD_SHA256:
        raise SystemExit("Gate 1 decision record hash mismatch")
    if sha256_file(decision_markdown_path) != DECISION_MARKDOWN_SHA256:
        raise SystemExit("Gate 1 decision Markdown hash mismatch")
    if sha256_file(decision_summary_path) != DECISION_SUMMARY_SHA256:
        raise SystemExit("Gate 1 decision summary hash mismatch")

    decision = read_json(decision_record_path)
    report = read_json(decision_report_path)
    verify_decision(decision, report)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    rollup = {
        "rollup_id": ROLLUP_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "narrow_source_reconstruction_evidence_rollup_ready",
        "input_decision_id": "G1RD-G1-VIRAL-001",
        "input_decision_report_sha256": DECISION_REPORT_SHA256,
        "input_decision_record_sha256": DECISION_RECORD_SHA256,
        "input_decision_markdown_sha256": DECISION_MARKDOWN_SHA256,
        "input_decision_summary_sha256": DECISION_SUMMARY_SHA256,
        "input_packet_lineage": decision["direct_packet_lineage"],
        "accepted_scope": "seven_reviewed_records_only_pages_not_complete",
        "accepted_records": 7,
        "accepted_source_text_records": 4,
        "accepted_visual_exclusion_records": 3,
        "accepted_pages": ["001", "005", "006"],
        "accepted_pages_as_complete": False,
        "whole_gate_1_acceptance": False,
        "page_complete_acceptance": False,
        "gate_1_source_reconstruction_evidence_slice_accepted": True,
        "gate_1_advancement": True,
        "gate_1_advancement_scope": "seven_reviewed_records_only_pages_not_complete",
        "usable_as_higher_level_gate_1_status_input": True,
        "requires_explicit_scope_label_when_reused": True,
        "not_accepted": [
            "page_001_complete",
            "page_005_complete",
            "page_006_complete",
            "whole_viral_pdf",
            "whole_gate_1",
            "translation",
            "proofreading",
            "renderer_profile",
            "implementation",
            "push",
        ],
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "recommended_next_actions": [
            "BA-G1-VIRAL-GATE-1-STATUS-PACKET-001",
            "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001",
        ],
    }
    write_json(OUT_ROOT / "gate_1_source_recon_evidence_rollup.json", rollup)

    summary_lines = [
        "# Gate 1 Source Reconstruction Evidence Rollup - G1SRER-G1-VIRAL-001",
        "",
        "Status: `narrow_source_reconstruction_evidence_rollup_ready`",
        "",
        "This rollup carries `G1RD-G1-VIRAL-001` forward without broadening it.",
        "",
        "## Accepted",
        "",
        "- Accepted records: `7`",
        "- Accepted source-text records: `4`",
        "- Accepted visual-exclusion records: `3`",
        "- Gate 1 advancement scope: `seven_reviewed_records_only_pages_not_complete`",
        "",
        "## Not Accepted",
        "",
        "- Pages 001/005/006 as complete: `false`",
        "- Whole Viral PDF: `false`",
        "- Whole Gate 1: `false`",
        "- Translation/proofreading/renderer-profile/implementation/push: `false`",
        "",
        "## Next Safe Actions",
        "",
        "- Build a higher-level Gate 1 status packet that preserves this narrow scope.",
        "- Or continue source reconstruction with a separately authorized next slice.",
        "",
    ]
    (OUT_ROOT / "gate_1_source_recon_evidence_rollup_summary.md").write_text(
        "\n".join(summary_lines),
        encoding="utf-8",
    )

    rollup_report = {
        "rollup_id": ROLLUP_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "narrow_source_reconstruction_evidence_rollup_ready",
        "input_decision_id": "G1RD-G1-VIRAL-001",
        "input_decision_report_sha256": DECISION_REPORT_SHA256,
        "input_decision_record_sha256": DECISION_RECORD_SHA256,
        "input_decision_markdown_sha256": DECISION_MARKDOWN_SHA256,
        "input_decision_summary_sha256": DECISION_SUMMARY_SHA256,
        "generator_script": "scripts/rollup_gate_1_source_reconstruction_evidence.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_gate_1_source_recon_evidence_rollup.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_gate_1_source_recon_evidence_rollup.py")
        if (ROOT / "tests" / "test_gate_1_source_recon_evidence_rollup.py").exists()
        else None,
        "accepted_records": 7,
        "accepted_pages_as_complete": False,
        "whole_gate_1_acceptance": False,
        "gate_1_advancement": True,
        "gate_1_advancement_scope": "seven_reviewed_records_only_pages_not_complete",
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
    }
    write_json(OUT_ROOT / "gate_1_source_recon_evidence_rollup_report.json", rollup_report)

    manifest_lines = [
        "# Gate 1 Source Reconstruction Evidence Rollup Manifest - G1SRER-G1-VIRAL-001",
        "",
        "Status: `narrow_source_reconstruction_evidence_rollup_ready`",
        "",
        "Boundary: this rollup carries only seven reviewed records; pages and whole Gate 1 are not accepted.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_source_recon_evidence_rollup_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "gate_1_source_recon_evidence_rollup_manifest.md").write_text(
        "\n".join(manifest_lines),
        encoding="utf-8",
    )


if __name__ == "__main__":
    check_authorization()
    build()
