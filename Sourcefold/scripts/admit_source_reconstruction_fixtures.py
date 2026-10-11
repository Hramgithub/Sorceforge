from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRQA_ROOT = TRIAL_ROOT / "source_reconstruction_qa_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_fixture_admission_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-FIXTURE-ADMISSION-001"
ADMISSION_ID = "SRFA-G1-VIRAL-001"
SRQA_REPORT_SHA256 = "A98811F3368FD468618A111D9F7A85BFFBD72CE9387CCF11DA011875C80553E0"
SRQA_SUMMARY_SHA256 = "C7C32A1D4E9A74DC3F086D4D355151BF6C89DBDE576775AC0F67312E98981EC3"


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
    parser = argparse.ArgumentParser(description="Admit source reconstruction fixtures from SRQA.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction fixture admission is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction fixture admission requires {AUTHORIZATION_ID}")


def verify_qa(srqa: dict[str, object]) -> None:
    if srqa["qa_id"] != "SRQA-G1-VIRAL-001":
        raise SystemExit("unexpected SRQA id")
    if srqa["status"] != "source_reconstruction_qa_passed_not_fixture_or_gate":
        raise SystemExit("unexpected SRQA status")
    if srqa["source_acceptance"] is not True or srqa["qa_acceptance"] is not True:
        raise SystemExit("SRQA acceptance flags are not ready for fixture admission")
    if srqa["gate_1_advancement"] is not False or srqa["fixture_creation"] is not False:
        raise SystemExit("SRQA already created fixtures or advanced Gate 1")
    for key in [
        "ocr_executed",
        "pdf_opened_or_parsed",
        "raw_ocr_outputs_modified",
        "translation_authorized",
        "proofreading_authorized",
    ]:
        if srqa[key] is not False:
            raise SystemExit(f"unsafe SRQA boundary flag: {key}")
    if srqa["summary"] != {
        "records": 7,
        "source_text_qa_passed_records": 4,
        "visual_exclusion_qa_passed_records": 3,
        "blocked_records": 0,
        "gate_1_advanced_records": 0,
    }:
        raise SystemExit("unexpected SRQA summary")


def fixture_records(srqa: dict[str, object]) -> list[dict[str, object]]:
    records = srqa["qa_records"]
    output = []
    source_index = 1
    exclusion_index = 1
    for record in records:
        region_id = str(record["region_admission_id"])
        source_text = bool(record["source_text_accepted"])
        visual_exclusion = bool(record["visual_exclusion_accepted"])
        if source_text == visual_exclusion:
            raise SystemExit(f"ambiguous fixture input: {region_id}")
        if record["qa_acceptance"] is not True or record["gate_1_advancement"] is not False:
            raise SystemExit(f"unexpected QA record flags: {region_id}")

        if source_text:
            fixture_id = f"FX-G1-VIRAL-SOURCE-{source_index:03d}"
            fixture_kind = "positive_source_text"
            expected_behavior = "candidate_text_must_match_exact_source_review_text"
            source_index += 1
        else:
            fixture_id = f"FX-G1-VIRAL-VISUAL-EXCLUSION-{exclusion_index:03d}"
            fixture_kind = "negative_visual_exclusion"
            expected_behavior = "visual_only_region_must_not_create_source_text"
            exclusion_index += 1

        fixture = {
            "fixture_id": fixture_id,
            "fixture_kind": fixture_kind,
            "source_qa_id": "SRQA-G1-VIRAL-001",
            "region_admission_id": region_id,
            "question_number": record["question_number"],
            "page_id": record["page_id"],
            "region_id": record["region_id"],
            "review_class": record["review_class"],
            "expected_behavior": expected_behavior,
            "source_text_accepted": source_text,
            "visual_exclusion_accepted": visual_exclusion,
            "qa_acceptance": True,
            "fixture_admitted": True,
            "gate_1_advancement": False,
        }
        if "packet_correction_note" in record:
            fixture["packet_correction_note"] = record["packet_correction_note"]
        if "semantic_heading_hint" in record:
            fixture["semantic_heading_hint"] = record["semantic_heading_hint"]
        output.append(fixture)

    if source_index != 5 or exclusion_index != 4:
        raise SystemExit("unexpected fixture split")
    return output


def build() -> None:
    srqa_report_path = SRQA_ROOT / "source_reconstruction_qa_report.json"
    srqa_summary_path = SRQA_ROOT / "source_reconstruction_qa_summary.md"
    if sha256_file(srqa_report_path) != SRQA_REPORT_SHA256:
        raise SystemExit("SRQA report hash mismatch")
    if sha256_file(srqa_summary_path) != SRQA_SUMMARY_SHA256:
        raise SystemExit("SRQA summary hash mismatch")

    srqa = read_json(srqa_report_path)
    verify_qa(srqa)

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    fixtures = fixture_records(srqa)
    source_fixtures = [fixture for fixture in fixtures if fixture["fixture_kind"] == "positive_source_text"]
    exclusion_fixtures = [fixture for fixture in fixtures if fixture["fixture_kind"] == "negative_visual_exclusion"]

    write_json(OUT_ROOT / "source_reconstruction_admitted_fixtures.json", {"fixtures": fixtures})
    report = {
        "admission_id": ADMISSION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "source_reconstruction_fixtures_admitted_not_gate",
        "input_qa_id": "SRQA-G1-VIRAL-001",
        "input_qa_report_sha256": SRQA_REPORT_SHA256,
        "input_qa_summary_sha256": SRQA_SUMMARY_SHA256,
        "generator_script": "scripts/admit_source_reconstruction_fixtures.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_source_reconstruction_fixture_admission.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_source_reconstruction_fixture_admission.py")
        if (ROOT / "tests" / "test_source_reconstruction_fixture_admission.py").exists()
        else None,
        "source_acceptance": True,
        "qa_acceptance": True,
        "fixture_admission": True,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "summary": {
            "fixtures": len(fixtures),
            "positive_source_text_fixtures": len(source_fixtures),
            "negative_visual_exclusion_fixtures": len(exclusion_fixtures),
            "blocked_fixtures": 0,
            "gate_1_advanced_fixtures": 0,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-GATE-1-REVIEW-PACKET-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_fixture_admission_report.json", report)

    summary_lines = [
        "# Source Reconstruction Fixture Admission Summary - SRFA-G1-VIRAL-001",
        "",
        "Status: `source_reconstruction_fixtures_admitted_not_gate`",
        "",
        "Boundary: fixtures are admitted as stable downstream test inputs from SRQA. This is not translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Summary",
        "",
        "- Positive source-text fixtures: `4`",
        "- Negative visual-exclusion fixtures: `3`",
        "- Blocked fixtures: `0`",
        "- Gate 1 advanced: `false`",
        "",
    ]
    (OUT_ROOT / "source_reconstruction_fixture_admission_summary.md").write_text(
        "\n".join(summary_lines), encoding="utf-8"
    )

    manifest_lines = [
        "# Source Reconstruction Fixture Admission Manifest - SRFA-G1-VIRAL-001",
        "",
        "Status: `source_reconstruction_fixtures_admitted_not_gate`",
        "",
        "Boundary: no OCR, PDF parsing, rendering, raw OCR edits, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_fixture_admission_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_fixture_admission_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    check_authorization()
    build()
