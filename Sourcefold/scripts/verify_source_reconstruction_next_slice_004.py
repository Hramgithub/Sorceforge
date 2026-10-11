from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "verify_source_reconstruction_next_slice_004.py"
TEST_PATH = ROOT / "tests" / "test_source_reconstruction_next_slice_004_verify.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRCR_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_004"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_004_verify_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004-HUMAN-VERIFY-001"
VERIFY_ID = "SRCRV-G1-VIRAL-004"
SRCR_REPORT_SHA256 = "C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A"
SRCR_MANIFEST_SHA256 = "30120887FEECD7277D12B8BBC3892546DB71A908C27D06BC18256E22B7045EF4"
SRCR_PACKET_SHA256 = "1E084D1BEE01A02BC53E8E7D482F0ED216282DC5E9291BCA78382E730F30F446"

USER_DECISION = {
    "telegram_message_id": "523",
    "raw_text": "1 ок\n2 ок",
    "record_decisions": [
        {"question_id": "1", "decision": "ok", "verified_draft_matches_crop": True},
        {"question_id": "2", "decision": "ok", "verified_draft_matches_crop": True},
    ],
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Verify Viral page 004 source reconstruction review packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 004 review packet verification is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 004 review packet verification requires {AUTHORIZATION_ID}")


def verify_predecessor() -> dict[str, object]:
    report_path = SRCR_ROOT / "source_reconstruction_next_slice_report.json"
    manifest_path = SRCR_ROOT / "source_reconstruction_next_slice_manifest.md"
    packet_path = SRCR_ROOT / "human_review_packet.md"
    if sha256_file(report_path) != SRCR_REPORT_SHA256:
        raise SystemExit("SRCR-G1-VIRAL-004 report hash mismatch")
    if sha256_file(manifest_path) != SRCR_MANIFEST_SHA256:
        raise SystemExit("SRCR-G1-VIRAL-004 manifest hash mismatch")
    if sha256_file(packet_path) != SRCR_PACKET_SHA256:
        raise SystemExit("SRCR-G1-VIRAL-004 human review packet hash mismatch")

    report = read_json(report_path)
    if report["package_id"] != "SRCR-G1-VIRAL-004":
        raise SystemExit("unexpected page 004 review package id")
    if report["summary"]["records"] != 2:
        raise SystemExit("page 004 review packet does not contain exactly two records")
    if report["source_acceptance"] is not False or report["qa_acceptance"] is not False:
        raise SystemExit("page 004 review packet unexpectedly accepted source text or QA")
    if report["page_complete_acceptance"] is not False or report["whole_gate_1_acceptance"] is not False:
        raise SystemExit("page 004 review packet unexpectedly expanded page or Gate scope")
    guardrail = report.get("crop_layout_guardrail")
    if not guardrail or guardrail["guardrail_policy_id"] != "SRCG-GLOBAL-CROP-BOX-LAYOUT-001":
        raise SystemExit("page 004 review packet missing global crop guardrail evidence")
    if guardrail["status"] != "passed":
        raise SystemExit("page 004 crop guardrail did not pass")
    return report


def build() -> None:
    predecessor = verify_predecessor()

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    decisions = {item["question_id"]: item for item in USER_DECISION["record_decisions"]}
    verified_records = []
    for record in predecessor["records"]:
        decision = decisions[record["question_id"]]
        verified_records.append(
            {
                "question_id": record["question_id"],
                "verified_record_id": f"{VERIFY_ID}-R{int(record['question_id']):02d}",
                "input_review_id": record["review_id"],
                "source_region_id": record["source_region_id"],
                "crop_reference": record["crop_reference"],
                "crop_reference_sha256": record["crop_reference_sha256"],
                "verified_draft_text": record["draft_text"],
                "verified_draft_text_sha256": sha256_text(record["draft_text"]),
                "verified_structure": record["draft_structure"],
                "bogdan_decision": decision["decision"],
                "verified_draft_matches_crop": decision["verified_draft_matches_crop"],
                "source_acceptance": False,
                "qa_acceptance": False,
                "fixture_admission": False,
                "page_complete_acceptance": False,
                "whole_gate_1_acceptance": False,
                "gate_1_advancement": False,
            }
        )

    report = {
        "verification_id": VERIFY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "page_004_review_packet_human_verified_not_source_accepted",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_review_packet_id": "SRCR-G1-VIRAL-004",
        "input_report_sha256": SRCR_REPORT_SHA256,
        "input_manifest_sha256": SRCR_MANIFEST_SHA256,
        "input_human_review_packet_sha256": SRCR_PACKET_SHA256,
        "user_decision": USER_DECISION,
        "selected_page": "004",
        "selected_scope": "page_004_two_record_human_verification_only",
        "records": verified_records,
        "summary": {
            "records": len(verified_records),
            "human_verified_records": len(verified_records),
            "source_accepted_records": 0,
            "qa_accepted_records": 0,
            "accepted_pages_as_complete": False,
            "whole_gate_1_acceptance": False,
        },
        "human_verification_recorded": True,
        "source_acceptance": False,
        "qa_acceptance": False,
        "fixture_admission": False,
        "gate_1_advancement": False,
        "page_complete_acceptance": False,
        "whole_gate_1_acceptance": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "renderer_profile_acceptance": False,
        "implementation_authorized": False,
        "push_authorized": False,
        "next_authorization_recommendation": "BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_next_slice_004_verify_report.json", report)

    summary_lines = [
        "# Page 004 Review Packet Human Verification - SRCRV-G1-VIRAL-004",
        "",
        "Status: `page_004_review_packet_human_verified_not_source_accepted`",
        "",
        "Boundary: Bogdan verified the two page 004 draft review records. This is not source acceptance, QA acceptance, fixture admission, page-complete acceptance, Gate 1 advancement, translation, proofreading, renderer/profile acceptance, implementation, or push.",
        "",
        "## Bogdan Decision",
        "",
        f"- Telegram message: `{USER_DECISION['telegram_message_id']}`",
        f"- Raw text: `{USER_DECISION['raw_text']}`",
        "",
        "## Verified Records",
        "",
    ]
    for record in verified_records:
        summary_lines.append(f"### {record['question_id']} - {record['source_region_id']}")
        summary_lines.append("")
        summary_lines.append(f"- Decision: `{record['bogdan_decision']}`")
        summary_lines.append(f"- Crop: `{record['crop_reference']}`")
        summary_lines.append(f"- Verified draft text SHA-256: `{record['verified_draft_text_sha256']}`")
        summary_lines.append("")
    (OUT_ROOT / "page_004_human_verification_summary.md").write_text(
        "\n".join(summary_lines), encoding="utf-8", newline="\n"
    )

    manifest_lines = [
        "# Page 004 Review Packet Human Verification Manifest - SRCRV-G1-VIRAL-004",
        "",
        "Status: `page_004_review_packet_human_verified_not_source_accepted`",
        "",
        "Boundary: no source acceptance, QA acceptance, fixtures, Gate 1 advancement, OCR execution, PDF parsing/rendering, raw OCR mutation, translation, proofreading, implementation, or push.",
        "",
        "## Generator Hashes",
        "",
        f"- Script `{SCRIPT_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(SCRIPT_PATH)}`",
        f"- Test `{TEST_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(TEST_PATH)}`",
        "",
        "## Input Hashes",
        "",
        f"- SRCR report SHA-256: `{SRCR_REPORT_SHA256}`",
        f"- SRCR manifest SHA-256: `{SRCR_MANIFEST_SHA256}`",
        f"- SRCR human review packet SHA-256: `{SRCR_PACKET_SHA256}`",
        "",
        "## Records",
        "",
        "| Question | Source region | Crop SHA-256 | Verified draft text SHA-256 | Decision |",
        "|---:|---|---|---|---|",
    ]
    for record in verified_records:
        manifest_lines.append(
            f"| {record['question_id']} | `{record['source_region_id']}` | `{record['crop_reference_sha256']}` | `{record['verified_draft_text_sha256']}` | `{record['bogdan_decision']}` |"
        )
    manifest_lines.extend(["", "## Output Hashes", "", "| Output | SHA-256 |", "|---|---|"])
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_next_slice_004_verify_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_next_slice_004_verify_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
