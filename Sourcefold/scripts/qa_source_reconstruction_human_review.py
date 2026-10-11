from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRHR_ROOT = TRIAL_ROOT / "source_reconstruction_human_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_qa_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-QA-001"
QA_ID = "SRQA-G1-VIRAL-001"
SRHR_REPORT_SHA256 = "FF7C9778E711D67964584CD00870762FD7ADE47E4368EA71DD3C373AB5EB4980"
SRHR_ACCEPTED_TEXT_SHA256 = "E623AD3DD9246B4DB30BB43A7A929CB13686E57ED02C44756FA365B65AB2D3E2"


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
    parser = argparse.ArgumentParser(description="QA Bogdan human source reconstruction review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction QA is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction QA requires {AUTHORIZATION_ID}")


def verify_boundary(srhr: dict[str, object]) -> None:
    if srhr["review_id"] != "SRHR-G1-VIRAL-001":
        raise SystemExit("unexpected SRHR review id")
    if srhr["status"] != "source_review_accepted_not_qa_accepted":
        raise SystemExit("unexpected SRHR status")
    if srhr["source_acceptance"] is not True:
        raise SystemExit("SRHR source acceptance is missing")
    if srhr["qa_acceptance"] is not False:
        raise SystemExit("SRHR is already QA accepted")
    if srhr["gate_1_advancement"] is not False:
        raise SystemExit("SRHR advanced Gate 1 unexpectedly")
    for key in [
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
        "fixture_creation",
        "translation_authorized",
        "proofreading_authorized",
    ]:
        if srhr[key] is not False:
            raise SystemExit(f"unsafe SRHR boundary flag: {key}")


def qa_records(srhr: dict[str, object], accepted_text: str) -> list[dict[str, object]]:
    records = srhr["human_review_records"]
    if len(records) != 7:
        raise SystemExit("SRHR does not contain exactly seven records")

    output = []
    text_records = 0
    visual_exclusion_records = 0
    for record in records:
        region_id = str(record["region_admission_id"])
        source_text_accepted = bool(record["source_text_accepted"])
        visual_exclusion_accepted = bool(record["visual_exclusion_accepted"])
        if source_text_accepted == visual_exclusion_accepted:
            raise SystemExit(f"ambiguous QA input acceptance: {region_id}")
        if record["qa_acceptance"] is not False or record["gate_1_advancement"] is not False:
            raise SystemExit(f"unexpected record boundary flag: {region_id}")

        visual_reference = ROOT / str(record["visual_reference"])
        if not visual_reference.exists() or sha256_file(visual_reference) != record["visual_reference_sha256"]:
            raise SystemExit(f"visual reference hash mismatch: {region_id}")
        source_crop = ROOT / str(record["source_input_crop"])
        if not source_crop.exists() or sha256_file(source_crop) != record["source_input_crop_sha256"]:
            raise SystemExit(f"source crop hash mismatch: {region_id}")

        candidate_text = record["candidate_text"]
        if source_text_accepted:
            text_records += 1
            if not candidate_text or str(candidate_text) not in accepted_text:
                raise SystemExit(f"accepted text output missing candidate text: {region_id}")
            qa_result = "source_text_qa_passed"
        else:
            visual_exclusion_records += 1
            if candidate_text is not None:
                raise SystemExit(f"visual exclusion carried candidate text: {region_id}")
            qa_result = "visual_exclusion_qa_passed"

        output_record = {
            "region_admission_id": region_id,
            "question_number": record["question_number"],
            "page_id": record["page_id"],
            "region_id": record["region_id"],
            "review_class": record["review_class"],
            "qa_result": qa_result,
            "source_text_accepted": source_text_accepted,
            "visual_exclusion_accepted": visual_exclusion_accepted,
            "qa_acceptance": True,
            "gate_1_advancement": False,
        }
        if "packet_correction_note" in record:
            output_record["packet_correction_note"] = record["packet_correction_note"]
        if "semantic_heading_hint" in record:
            output_record["semantic_heading_hint"] = record["semantic_heading_hint"]
        output.append(output_record)

    if text_records != 4 or visual_exclusion_records != 3:
        raise SystemExit("unexpected accepted text / visual exclusion split")

    r003 = next(record for record in output if record["region_admission_id"] == "SRA-G1-VIRAL-001-R003")
    if "full source crop was resent in message 259" not in r003.get("packet_correction_note", ""):
        raise SystemExit("R003 corrected-full-crop note missing")
    if r003.get("semantic_heading_hint") != [
        {"text": "Introduction", "level": "H1"},
        {"text": "Summary", "level": "H3"},
        {"text": "Overview", "level": "H3"},
        {"text": "The Spektral Krew", "level": "H2"},
    ]:
        raise SystemExit("R003 semantic heading hint mismatch")

    return sorted(output, key=lambda record: int(record["question_number"]))


def build() -> None:
    srhr_report_path = SRHR_ROOT / "source_reconstruction_human_review_report.json"
    accepted_text_path = SRHR_ROOT / "source_review_accepted_text.md"
    if sha256_file(srhr_report_path) != SRHR_REPORT_SHA256:
        raise SystemExit("SRHR report hash mismatch")
    if sha256_file(accepted_text_path) != SRHR_ACCEPTED_TEXT_SHA256:
        raise SystemExit("SRHR accepted text hash mismatch")

    srhr = read_json(srhr_report_path)
    accepted_text = accepted_text_path.read_text(encoding="utf-8")
    verify_boundary(srhr)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    records = qa_records(srhr, accepted_text)
    report = {
        "qa_id": QA_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "source_reconstruction_qa_passed_not_fixture_or_gate",
        "input_review_id": "SRHR-G1-VIRAL-001",
        "input_review_sha256": SRHR_REPORT_SHA256,
        "input_accepted_text_sha256": SRHR_ACCEPTED_TEXT_SHA256,
        "generator_script": "scripts/qa_source_reconstruction_human_review.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_source_reconstruction_qa.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_source_reconstruction_qa.py")
        if (ROOT / "tests" / "test_source_reconstruction_qa.py").exists()
        else None,
        "source_acceptance": True,
        "qa_acceptance": True,
        "gate_1_advancement": False,
        "fixture_creation": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "qa_records": records,
        "summary": {
            "records": len(records),
            "source_text_qa_passed_records": sum(1 for record in records if record["source_text_accepted"]),
            "visual_exclusion_qa_passed_records": sum(1 for record in records if record["visual_exclusion_accepted"]),
            "blocked_records": 0,
            "gate_1_advanced_records": 0,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_qa_report.json", report)

    summary_lines = [
        "# Source Reconstruction QA Summary - SRQA-G1-VIRAL-001",
        "",
        "Status: `source_reconstruction_qa_passed_not_fixture_or_gate`",
        "",
        "Boundary: SRHR source review passed QA. This is not fixture creation, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## QA Results",
        "",
        "- Source text QA passed records: `4`",
        "- Visual exclusion QA passed records: `3`",
        "- Blocked records: `0`",
        "- Gate 1 advanced: `false`",
        "",
        "## R003 Metadata",
        "",
        "- Corrected full-crop packet: `true`",
        "- Semantic heading hint preserved as metadata: `true`",
        "",
    ]
    (OUT_ROOT / "source_reconstruction_qa_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    manifest_lines = [
        "# Source Reconstruction QA Manifest - SRQA-G1-VIRAL-001",
        "",
        "Status: `source_reconstruction_qa_passed_not_fixture_or_gate`",
        "",
        "Boundary: no OCR, PDF parsing, rendering, raw OCR edits, fixture creation, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_qa_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_qa_manifest.md").write_text("\n".join(manifest_lines), encoding="utf-8")


if __name__ == "__main__":
    check_authorization()
    build()
