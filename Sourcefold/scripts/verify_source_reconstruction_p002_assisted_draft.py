from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "verify_source_reconstruction_p002_assisted_draft.py"
TEST_PATH = ROOT / "tests" / "test_source_reconstruction_p002_assisted_draft_verify.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRAD_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-HUMAN-VERIFY-001"
VERIFY_ID = "SRADV-G1-VIRAL-002"
SRAD_REPORT_SHA256 = "296763B5942B937B66822E4988C30FF5B96FBFBFF08952987FA5E8D22CE07F05"
SRAD_MANIFEST_SHA256 = "D6E50079093DEDA2F178D744E19DA29650CF3B2667B1F5418D4CB02F018E4280"
SRAD_DRAFT_SHA256 = "256568A3889A1BA9417662F8E897D818416A7FCBA664E0A896CB7F931F2C769B"

USER_DECISION = {
    "telegram_message_id": "377",
    "raw_text": "1 ок; 2 ок; Заголовки игнорирую. По тексту все ок.",
    "record_decisions": [
        {
            "question_id": "1",
            "decision": "ok",
            "verified_text_matches_crop": True,
            "heading_handling": "ignore_headings_for_this_decision",
        },
        {
            "question_id": "2",
            "decision": "ok",
            "verified_text_matches_crop": True,
            "heading_handling": "ignore_headings_for_this_decision",
        },
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
    parser = argparse.ArgumentParser(description="Verify Viral page 002 assisted source reconstruction draft.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page 002 assisted draft verification is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"page 002 assisted draft verification requires {AUTHORIZATION_ID}")


def verify_predecessor() -> dict[str, object]:
    report_path = SRAD_ROOT / "source_reconstruction_p002_assisted_draft_report.json"
    manifest_path = SRAD_ROOT / "source_reconstruction_p002_assisted_draft_manifest.md"
    draft_path = SRAD_ROOT / "assisted_text_draft_for_bogdan.md"
    if sha256_file(report_path) != SRAD_REPORT_SHA256:
        raise SystemExit("SRAD report hash mismatch")
    if sha256_file(manifest_path) != SRAD_MANIFEST_SHA256:
        raise SystemExit("SRAD manifest hash mismatch")
    if sha256_file(draft_path) != SRAD_DRAFT_SHA256:
        raise SystemExit("SRAD assisted draft hash mismatch")

    report = read_json(report_path)
    if report["draft_id"] != "SRAD-G1-VIRAL-002":
        raise SystemExit("unexpected SRAD draft id")
    if report["draft_text_is_source_accepted"] is not False:
        raise SystemExit("SRAD predecessor was unexpectedly source accepted")
    if report["page_complete_acceptance"] is not False or report["whole_gate_1_acceptance"] is not False:
        raise SystemExit("SRAD predecessor unexpectedly expanded scope")
    if len(report["records"]) != 2:
        raise SystemExit("SRAD predecessor did not contain exactly two records")
    return report


def build() -> None:
    srad_report = verify_predecessor()

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    decisions = {item["question_id"]: item for item in USER_DECISION["record_decisions"]}
    verified_records = []
    for record in srad_report["records"]:
        decision = decisions[record["question_id"]]
        verified_records.append(
            {
                "question_id": record["question_id"],
                "verified_record_id": f"{VERIFY_ID}-R{int(record['question_id']):02d}",
                "input_assisted_record_id": record["assisted_record_id"],
                "source_region_id": record["source_region_id"],
                "corrected_crop_reference": record["corrected_crop_reference"],
                "corrected_crop_reference_sha256": record["corrected_crop_reference_sha256"],
                "verified_text": record["draft_text"],
                "verified_text_sha256": sha256_text(record["draft_text"]),
                "bogdan_decision": decision["decision"],
                "verified_text_matches_crop": decision["verified_text_matches_crop"],
                "heading_handling": decision["heading_handling"],
                "source_acceptance": False,
                "qa_acceptance": False,
                "fixture_admission": False,
                "gate_1_advancement": False,
            }
        )

    report = {
        "verification_id": VERIFY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "assisted_draft_human_verified_not_source_accepted",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_sha256": sha256_file(TEST_PATH),
        },
        "input_assisted_draft_id": "SRAD-G1-VIRAL-002",
        "input_assisted_draft_report_sha256": SRAD_REPORT_SHA256,
        "input_assisted_draft_manifest_sha256": SRAD_MANIFEST_SHA256,
        "input_assisted_draft_markdown_sha256": SRAD_DRAFT_SHA256,
        "user_decision": USER_DECISION,
        "selected_page": "002",
        "selected_scope": "page_002_two_record_assisted_draft_human_verification_only",
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
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-QA-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_p002_assisted_draft_verify_report.json", report)

    summary_lines = [
        "# Page 002 Assisted Draft Human Verification - SRADV-G1-VIRAL-002",
        "",
        "Status: `assisted_draft_human_verified_not_source_accepted`",
        "",
        "Boundary: Bogdan verified that the draft text matches the two corrected page 002 crops. This is not source acceptance, QA, fixture admission, page-complete acceptance, Gate 1 advancement, translation, proofreading, renderer/profile acceptance, implementation, or push.",
        "",
        "## Bogdan Decision",
        "",
        f"- Telegram message: `{USER_DECISION['telegram_message_id']}`",
        f"- Raw text: `{USER_DECISION['raw_text']}`",
        "- Heading/title handling: ignored for this decision.",
        "",
        "## Verified Records",
        "",
    ]
    for record in verified_records:
        summary_lines.append(f"### {record['question_id']} - {record['source_region_id']}")
        summary_lines.append("")
        summary_lines.append(f"- Decision: `{record['bogdan_decision']}`")
        summary_lines.append(f"- Corrected crop: `{record['corrected_crop_reference']}`")
        summary_lines.append(f"- Verified text SHA-256: `{record['verified_text_sha256']}`")
        summary_lines.append("")
        summary_lines.append("```text")
        summary_lines.append(record["verified_text"])
        summary_lines.append("```")
        summary_lines.append("")
    (OUT_ROOT / "assisted_draft_human_verification_summary.md").write_text(
        "\n".join(summary_lines), encoding="utf-8", newline="\n"
    )

    manifest_lines = [
        "# Page 002 Assisted Draft Human Verification Manifest - SRADV-G1-VIRAL-002",
        "",
        "Status: `assisted_draft_human_verified_not_source_accepted`",
        "",
        "Boundary: no source acceptance, QA, fixtures, Gate 1 advancement, OCR execution, PDF parsing/rendering, raw OCR mutation, translation, proofreading, implementation, or push.",
        "",
        "## Generator Hashes",
        "",
        f"- Script `{SCRIPT_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(SCRIPT_PATH)}`",
        f"- Test `{TEST_PATH.relative_to(ROOT).as_posix()}` SHA-256: `{sha256_file(TEST_PATH)}`",
        "",
        "## Input Hashes",
        "",
        f"- SRAD report SHA-256: `{SRAD_REPORT_SHA256}`",
        f"- SRAD manifest SHA-256: `{SRAD_MANIFEST_SHA256}`",
        f"- SRAD assisted draft Markdown SHA-256: `{SRAD_DRAFT_SHA256}`",
        "",
        "## Records",
        "",
        "| Question | Source region | Crop SHA-256 | Verified text SHA-256 | Decision |",
        "|---:|---|---|---|---|",
    ]
    for record in verified_records:
        manifest_lines.append(
            f"| {record['question_id']} | `{record['source_region_id']}` | `{record['corrected_crop_reference_sha256']}` | `{record['verified_text_sha256']}` | `{record['bogdan_decision']}` |"
        )
    manifest_lines.extend(["", "## Output Hashes", "", "| Output | SHA-256 |", "|---|---|"])
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_p002_assisted_draft_verify_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_p002_assisted_draft_verify_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    check_authorization()
    build()
