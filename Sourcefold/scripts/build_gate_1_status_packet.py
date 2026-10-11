from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
ROLLUP_ROOT = TRIAL_ROOT / "gate_1_source_recon_evidence_rollup_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-STATUS-PACKET-001"
STATUS_PACKET_ID = "G1SP-G1-VIRAL-001"
ROLLUP_ID = "G1SRER-G1-VIRAL-001"
ROLLUP_REPORT_SHA256 = "CDF75D022DC29D0594CA441F02EDA2DC50CE9C0C4BA81F5C51523745318A4AEB"
ROLLUP_MANIFEST_SHA256 = "C5211A4F6607B6DEAE73EFA599C8F25F269833AAAACED9838FF2746AA4A1A265"
ROLLUP_PAYLOAD_SHA256 = "3674E136BAA0F1D62DC240FAD1C1E34FD919D56A4A7251D580106D9BEFB83380"
ROLLUP_SUMMARY_SHA256 = "5740BE4D8B7AAA7D8D05DFDFD3EBA4A67EF26538B9C95E653A3D8B09C498BC8B"


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
    parser = argparse.ArgumentParser(description="Build the Viral Gate 1 status packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 status packet build is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 status packet build requires {AUTHORIZATION_ID}")


def verify_rollup(rollup: dict[str, object], report: dict[str, object]) -> None:
    if rollup["rollup_id"] != ROLLUP_ID or report["rollup_id"] != ROLLUP_ID:
        raise SystemExit("unexpected Gate 1 source reconstruction evidence rollup id")
    if rollup["status"] != "narrow_source_reconstruction_evidence_rollup_ready":
        raise SystemExit("unexpected rollup status")
    if rollup["accepted_scope"] != "seven_reviewed_records_only_pages_not_complete":
        raise SystemExit("status packet can only consume the seven-record narrow scope")
    if rollup["accepted_records"] != 7:
        raise SystemExit("unexpected accepted record count")
    if rollup["accepted_source_text_records"] != 4 or rollup["accepted_visual_exclusion_records"] != 3:
        raise SystemExit("unexpected accepted record split")
    if rollup["accepted_pages_as_complete"] is not False:
        raise SystemExit("rollup accepted pages as complete")
    if rollup["page_complete_acceptance"] is not False:
        raise SystemExit("rollup has page-complete acceptance")
    if rollup["whole_gate_1_acceptance"] is not False:
        raise SystemExit("rollup accepted whole Gate 1")
    if rollup["requires_explicit_scope_label_when_reused"] is not True:
        raise SystemExit("rollup reuse does not require explicit scope labeling")
    for item in ["page_001_complete", "page_005_complete", "page_006_complete", "whole_viral_pdf", "whole_gate_1"]:
        if item not in rollup["not_accepted"]:
            raise SystemExit(f"missing not-accepted boundary: {item}")
    for key in [
        "translation_authorized",
        "proofreading_authorized",
        "renderer_profile_acceptance",
        "implementation_authorized",
        "push_authorized",
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
    ]:
        if rollup[key] is not False or report[key] is not False:
            raise SystemExit(f"unsafe rollup boundary flag: {key}")


def build() -> None:
    rollup_report_path = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup_report.json"
    rollup_manifest_path = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup_manifest.md"
    rollup_payload_path = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup.json"
    rollup_summary_path = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup_summary.md"
    if sha256_file(rollup_report_path) != ROLLUP_REPORT_SHA256:
        raise SystemExit("Gate 1 source reconstruction rollup report hash mismatch")
    if sha256_file(rollup_manifest_path) != ROLLUP_MANIFEST_SHA256:
        raise SystemExit("Gate 1 source reconstruction rollup manifest hash mismatch")
    if sha256_file(rollup_payload_path) != ROLLUP_PAYLOAD_SHA256:
        raise SystemExit("Gate 1 source reconstruction rollup payload hash mismatch")
    if sha256_file(rollup_summary_path) != ROLLUP_SUMMARY_SHA256:
        raise SystemExit("Gate 1 source reconstruction rollup summary hash mismatch")

    rollup = read_json(rollup_payload_path)
    report = read_json(rollup_report_path)
    verify_rollup(rollup, report)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    status_packet = {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_status_packet_ready_narrow_slice_only",
        "input_rollup_id": ROLLUP_ID,
        "input_rollup_report_sha256": ROLLUP_REPORT_SHA256,
        "input_rollup_manifest_sha256": ROLLUP_MANIFEST_SHA256,
        "input_rollup_payload_sha256": ROLLUP_PAYLOAD_SHA256,
        "input_rollup_summary_sha256": ROLLUP_SUMMARY_SHA256,
        "current_gate_1_state": "partial_narrow_source_reconstruction_evidence_accepted",
        "accepted_evidence": {
            "source_reconstruction_slice": {
                "rollup_id": ROLLUP_ID,
                "accepted_scope": "seven_reviewed_records_only_pages_not_complete",
                "accepted_records": 7,
                "accepted_source_text_records": 4,
                "accepted_visual_exclusion_records": 3,
                "accepted_pages": ["001", "005", "006"],
                "accepted_pages_as_complete": False,
                "page_complete_acceptance": False,
                "whole_gate_1_acceptance": False,
            }
        },
        "not_accepted": [
            "page_001_complete",
            "page_005_complete",
            "page_006_complete",
            "whole_viral_pdf",
            "whole_gate_1",
            "source_profile",
            "translation",
            "proofreading",
            "renderer_profile",
            "implementation",
            "push",
        ],
        "pending": [
            "additional_source_reconstruction_slices",
            "page_complete_review_if_needed",
            "whole_gate_1_review",
            "source_profile_parameter_acceptance",
            "translation_authorization",
            "proofreading_authorization",
            "renderer_profile_acceptance",
            "implementation_authorization",
            "push_authorization",
        ],
        "new_gate_1_advancement_created": False,
        "inherited_gate_1_advancement_scope": "seven_reviewed_records_only_pages_not_complete",
        "whole_gate_1_ready": False,
        "source_profile_accepted": False,
        "page_complete_acceptance": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "recommended_next_actions": [
            "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001",
            "BA-G1-VIRAL-GATE-1-STATUS-REVIEW-001",
        ],
    }
    write_json(OUT_ROOT / "gate_1_status_packet.json", status_packet)

    summary_lines = [
        "# Gate 1 Status Packet - G1SP-G1-VIRAL-001",
        "",
        "Status: `gate_1_status_packet_ready_narrow_slice_only`",
        "",
        "This packet summarizes the current Viral Gate 1 state without broadening `G1SRER-G1-VIRAL-001`.",
        "",
        "## Accepted / Rolled Up",
        "",
        "- Source reconstruction evidence slice: `G1SRER-G1-VIRAL-001`",
        "- Accepted records: `7`",
        "- Source-text records: `4`",
        "- Visual-exclusion records: `3`",
        "- Scope: `seven_reviewed_records_only_pages_not_complete`",
        "",
        "## Not Accepted",
        "",
        "- Page 001 complete: `false`",
        "- Page 005 complete: `false`",
        "- Page 006 complete: `false`",
        "- Whole Viral PDF: `false`",
        "- Whole Gate 1: `false`",
        "- Source profile: `false`",
        "- Translation/proofreading/renderer-profile/implementation/push: `false`",
        "",
        "## Pending",
        "",
        "- Additional source reconstruction slices.",
        "- Any page-complete or whole-Gate acceptance.",
        "- Source profile parameter acceptance.",
        "- Translation, proofreading, renderer/profile acceptance, implementation, and push.",
        "",
        "## Next Safe Actions",
        "",
        "- Continue source reconstruction with a separately authorized next slice.",
        "- Or review this status packet without treating it as new Gate 1 advancement.",
        "",
    ]
    (OUT_ROOT / "gate_1_status_packet_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    status_report = {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_status_packet_ready_narrow_slice_only",
        "input_rollup_id": ROLLUP_ID,
        "input_rollup_report_sha256": ROLLUP_REPORT_SHA256,
        "input_rollup_manifest_sha256": ROLLUP_MANIFEST_SHA256,
        "input_rollup_payload_sha256": ROLLUP_PAYLOAD_SHA256,
        "input_rollup_summary_sha256": ROLLUP_SUMMARY_SHA256,
        "generator_script": "scripts/build_gate_1_status_packet.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_gate_1_status_packet.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_gate_1_status_packet.py")
        if (ROOT / "tests" / "test_gate_1_status_packet.py").exists()
        else None,
        "accepted_records": 7,
        "accepted_pages_as_complete": False,
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "new_gate_1_advancement_created": False,
        "whole_gate_1_ready": False,
        "source_profile_accepted": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
    }
    write_json(OUT_ROOT / "gate_1_status_packet_report.json", status_report)

    manifest_lines = [
        "# Gate 1 Status Packet Manifest - G1SP-G1-VIRAL-001",
        "",
        "Status: `gate_1_status_packet_ready_narrow_slice_only`",
        "",
        "Boundary: this packet summarizes one seven-record source reconstruction rollup; it does not accept pages, the whole PDF, or whole Gate 1.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_status_packet_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "gate_1_status_packet_manifest.md").write_text("\n".join(manifest_lines), encoding="utf-8")


if __name__ == "__main__":
    check_authorization()
    build()
