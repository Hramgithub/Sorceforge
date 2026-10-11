from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRVO_ROOT = TRIAL_ROOT / "source_reconstruction_visual_overlay_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_human_package_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001"
PACKAGE_ID = "SRHP-G1-VIRAL-001"
SRVO_SHA256 = "54ABBA9FA01B8AFECB2C2B4FD12EE4FCFD2EDA5B0B2948FB4A2D4C17238E2BF8"


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
    parser = argparse.ArgumentParser(description="Assemble a source reconstruction package for later human review.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction human package assembly is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction human package assembly requires {AUTHORIZATION_ID}")


def review_records(srvo: dict[str, object]) -> list[dict[str, object]]:
    records = srvo["candidate_records"] + srvo["visual_qc_records"]
    ordered = sorted(records, key=lambda record: str(record["region_admission_id"]))
    package_records = []
    for index, record in enumerate(ordered, start=1):
        region_id = str(record["region_admission_id"])
        if record["human_review_ready"] is not True:
            raise SystemExit(f"record is not human-review-ready: {region_id}")
        if record["remaining_blockers"]:
            raise SystemExit(f"record still has blockers: {region_id}")

        visual_reference = ROOT / str(record["visual_reference"])
        if not visual_reference.exists():
            raise SystemExit(f"missing visual reference: {region_id}")
        if sha256_file(visual_reference) != record["visual_reference_sha256"]:
            raise SystemExit(f"visual reference hash mismatch: {region_id}")

        source_input_crop = record["source_input_crop"]
        source_input_crop_sha256 = record["source_input_crop_sha256"]
        if source_input_crop is not None:
            source_crop = ROOT / str(source_input_crop)
            if not source_crop.exists():
                raise SystemExit(f"missing source crop: {region_id}")
            if sha256_file(source_crop) != source_input_crop_sha256:
                raise SystemExit(f"source crop hash mismatch: {region_id}")

        package_records.append(
            {
                "review_order": index,
                "region_admission_id": region_id,
                "record_kind": record["record_kind"],
                "sample_id": record["sample_id"],
                "page_id": record["page_id"],
                "region_id": record["region_id"],
                "predecessor_zone_id": record["predecessor_zone_id"],
                "route_class": record["route_class"],
                "review_class": record["review_class"],
                "decision": record["decision"],
                "decision_note": record["decision_note"],
                "candidate_text": record["candidate_text"],
                "candidate_text_basis": record["candidate_text_basis"],
                "visual_reference": record["visual_reference"],
                "visual_reference_sha256": record["visual_reference_sha256"],
                "source_input_crop": source_input_crop,
                "source_input_crop_sha256": source_input_crop_sha256,
                "human_review_ready": True,
                "source_acceptance": False,
                "qa_acceptance": False,
                "review_instruction": "review_candidate_text_or_visual_exclusion_before_any_source_acceptance",
            }
        )
    return package_records


def build() -> None:
    srvo_report_path = SRVO_ROOT / "source_reconstruction_visual_overlay_review_report.json"
    if sha256_file(srvo_report_path) != SRVO_SHA256:
        raise SystemExit("SRVO report hash mismatch")

    srvo = read_json(srvo_report_path)
    if srvo["report_id"] != "SRVO-G1-VIRAL-001":
        raise SystemExit("unexpected SRVO report id")
    if srvo["human_review_ready"] is not True or srvo["human_review_blocked"] is not False:
        raise SystemExit("SRVO is not ready for human package assembly")
    if srvo["source_acceptance"] is not False or srvo["qa_acceptance"] is not False:
        raise SystemExit("SRVO boundary flags are not safe")

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    records = review_records(srvo)
    candidate_text_records = [record for record in records if record["candidate_text"] is not None]
    visual_only_records = [record for record in records if record["candidate_text"] is None]
    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "human_review_package_ready_not_source_accepted",
        "input_report_id": "SRVO-G1-VIRAL-001",
        "input_report_sha256": SRVO_SHA256,
        "generator_script": "scripts/assemble_source_reconstruction_human_package.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_source_reconstruction_human_package.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_source_reconstruction_human_package.py")
        if (ROOT / "tests" / "test_source_reconstruction_human_package.py").exists()
        else None,
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "candidate_text_is_source_accepted": False,
        "ready_for_bogdan_human_review": True,
        "human_review_records": records,
        "summary": {
            "records": len(records),
            "candidate_text_records": len(candidate_text_records),
            "visual_only_records": len(visual_only_records),
            "source_accepted_records": 0,
            "qa_accepted_records": 0,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-HUMAN-REVIEW-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_human_package_report.json", report)

    review_lines = [
        "# Source Reconstruction Human Review Package - SRHP-G1-VIRAL-001",
        "",
        "Status: `human_review_package_ready_not_source_accepted`",
        "",
        "Boundary: this package is for Bogdan human review only. It is not accepted source text, QA acceptance, fixture creation, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Review Items",
        "",
    ]
    for record in records:
        review_lines.append(f"### {record['review_order']}. {record['region_admission_id']}")
        review_lines.append("")
        review_lines.append(f"- Decision: `{record['decision']}`")
        review_lines.append(f"- Route: `{record['route_class']}` / `{record['review_class']}`")
        review_lines.append(f"- Visual reference: `{record['visual_reference']}`")
        review_lines.append(f"- Source crop SHA-256: `{record['source_input_crop_sha256'] or 'none'}`")
        review_lines.append("- Source accepted: `false`")
        review_lines.append("")
        if record["candidate_text"] is None:
            review_lines.append("No source-text candidate; review the visual-only exclusion.")
        else:
            review_lines.append("```text")
            review_lines.append(str(record["candidate_text"]))
            review_lines.append("```")
        review_lines.append("")
    (OUT_ROOT / "human_review_package.md").write_text("\n".join(review_lines), encoding="utf-8")

    manifest_lines = [
        "# Source Reconstruction Human Package Manifest - SRHP-G1-VIRAL-001",
        "",
        "Status: `human_review_package_ready_not_source_accepted`",
        "",
        "Boundary: no OCR, PDF parsing, rendering, raw OCR edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Summary",
        "",
        f"- Records: `{report['summary']['records']}`",
        f"- Candidate text records: `{report['summary']['candidate_text_records']}`",
        f"- Visual-only records: `{report['summary']['visual_only_records']}`",
        "- Ready for Bogdan human review: `true`",
        "- Source accepted: `false`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_human_package_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_human_package_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    check_authorization()
    build()
