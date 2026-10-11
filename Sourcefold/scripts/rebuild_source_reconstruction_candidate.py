from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRCO_ROOT = TRIAL_ROOT / "source_reconstruction_crop_overlay_G1_VIRAL_001"
SRFO_ROOT = TRIAL_ROOT / "source_reconstruction_refined_ocr_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_rebuild_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-REBUILD-001"
PACKAGE_ID = "SRRB-G1-VIRAL-001"
SRCO_SHA256 = "08B77397484FF43C6E4E466632531B15829EA3C34A75F79C6DE84B70E433C78F"
SRFO_SHA256 = "531B61BE0C826E94427320C3CDEBEC1F2459043097ACF8FD9B456B0A0C4AA687"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, object] | list[dict[str, object]]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Rebuild source reconstruction candidate evidence package.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction rebuild is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction rebuild requires {AUTHORIZATION_ID}")


def selected_srfo_row(srfo_report: dict[str, object], srfo_rows: list[dict[str, object]]) -> dict[str, object]:
    selected = srfo_report["inputs"][0]
    matches = [
        row
        for row in srfo_rows
        if row["region_admission_id"] == selected["region_admission_id"]
        and row["config_id"] == selected["selected_config"]
    ]
    if len(matches) != 1:
        raise SystemExit("SRFO selected row mismatch")
    return matches[0]


def candidate_record(record: dict[str, object], srfo_report: dict[str, object], srfo_rows: list[dict[str, object]]) -> dict[str, object]:
    region_id = str(record["region_admission_id"])
    base = {
        "region_admission_id": region_id,
        "sample_id": record["sample_id"],
        "page_id": record["page_id"],
        "region_id": record["region_id"],
        "predecessor_zone_id": record["predecessor_zone_id"],
        "route_class": record["route_class"],
        "review_class": record["review_class"],
        "crop_reference": record["crop_overlay_artifact"]["path"],
        "crop_reference_sha256": record["crop_overlay_artifact"]["sha256"],
        "source_acceptance": False,
        "qa_acceptance": False,
    }
    if region_id == "SRA-G1-VIRAL-001-R001":
        return base | {
            "candidate_text": None,
            "rebuild_status": "visual_component_blocked",
            "human_review_ready": False,
            "blockers": ["visual_component_requires_manual_decision"],
        }
    if region_id in {"SRA-G1-VIRAL-001-R002", "SRA-G1-VIRAL-001-R004"}:
        return base | {
            "candidate_text": record["cleaned_candidate_text"],
            "candidate_text_basis": "srco_cleaned_candidate_text",
            "rebuild_status": "candidate_text_with_overlay_review_required",
            "human_review_ready": False,
            "blockers": ["overlay_review_required"],
        }
    if region_id == "SRA-G1-VIRAL-001-R003":
        selected = srfo_report["inputs"][0]
        row = selected_srfo_row(srfo_report, srfo_rows)
        return base | {
            "candidate_text": None,
            "candidate_text_basis": "srfo_raw_text_hash_only",
            "selected_config": selected["selected_config"],
            "selected_text_sha256": selected["selected_text_sha256"],
            "selected_tsv_sha256": selected["selected_tsv_sha256"],
            "selected_raw_text_path": row["raw_text"],
            "metric_scope": selected["metric_scope"],
            "replaces_full_region_text": selected["replaces_full_region_text"],
            "normalized_exact": selected["normalized_exact"],
            "token_recall": selected["token_recall"],
            "overlay_qc": selected["overlay_qc"],
            "rebuild_status": "refined_ocr_evidence_ready_but_overlay_blocked",
            "human_review_ready": False,
            "blockers": ["overlay_review_required", "full_contents_region_not_replaced"],
        }
    if region_id == "SRA-G1-VIRAL-001-R005":
        return base | {
            "candidate_text": record["cleaned_candidate_text"],
            "candidate_text_basis": "srco_carried_forward_candidate_text",
            "rebuild_status": "candidate_text_ready_for_later_human_review",
            "human_review_ready": True,
            "blockers": [],
        }
    raise AssertionError(f"unexpected region {region_id}")


def build() -> None:
    srco_report_path = SRCO_ROOT / "source_reconstruction_crop_overlay_report.json"
    srfo_report_path = SRFO_ROOT / "source_reconstruction_refined_ocr_report.json"
    if sha256_file(srco_report_path) != SRCO_SHA256:
        raise SystemExit("SRCO report hash mismatch")
    if sha256_file(srfo_report_path) != SRFO_SHA256:
        raise SystemExit("SRFO report hash mismatch")

    srco = read_json(srco_report_path)
    srfo = read_json(srfo_report_path)
    srfo_rows = read_json(SRFO_ROOT / "source_reconstruction_refined_ocr_rows.json")
    if srco["report_id"] != "SRCO-G1-VIRAL-001":
        raise SystemExit("unexpected SRCO report id")
    if srfo["run_id"] != "SRFO-G1-VIRAL-001":
        raise SystemExit("unexpected SRFO run id")

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    candidates = [candidate_record(record, srfo, srfo_rows) for record in srco["candidate_records"]]
    visuals = [
        {
            "region_admission_id": record["region_admission_id"],
            "sample_id": record["sample_id"],
            "page_id": record["page_id"],
            "region_id": record["region_id"],
            "predecessor_zone_id": record["predecessor_zone_id"],
            "route_class": record["route_class"],
            "review_class": record["review_class"],
            "crop_reference": record["crop_overlay_artifact"]["path"],
            "crop_reference_sha256": record["crop_overlay_artifact"]["sha256"],
            "candidate_text_created": False,
            "source_acceptance": False,
            "qa_acceptance": False,
            "human_review_ready": False,
            "blockers": ["visual_qc_manual_decision_required"],
        }
        for record in srco["visual_qc_records"]
    ]
    blocking_records = [
        record["region_admission_id"]
        for record in candidates + visuals
        if record["human_review_ready"] is not True
    ]
    report = {
        "package_id": PACKAGE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "rebuilt_candidate_blocked_for_visual_overlay_review",
        "inputs": {
            "srco_report": "SRCO-G1-VIRAL-001",
            "srco_report_sha256": SRCO_SHA256,
            "srfo_report": "SRFO-G1-VIRAL-001",
            "srfo_report_sha256": SRFO_SHA256,
        },
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "human_review_ready": False,
        "human_review_blocked": True,
        "candidate_records": candidates,
        "visual_qc_records": visuals,
        "summary": {
            "candidate_records": len(candidates),
            "visual_qc_records": len(visuals),
            "candidate_text_records": sum(1 for record in candidates if record["candidate_text"] is not None),
            "later_human_ready_records": sum(1 for record in candidates if record["human_review_ready"] is True),
            "blocking_records": blocking_records,
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_rebuild_report.json", report)

    lines = [
        "# Source Reconstruction Rebuild - SRRB-G1-VIRAL-001",
        "",
        "Status: `rebuilt_candidate_blocked_for_visual_overlay_review`",
        "",
        "Boundary: no OCR, PDF parsing, raw OCR edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "This package is not human-ready. It consolidates SRCO/SRFO evidence and lists remaining visual/overlay blockers.",
        "",
        "## Summary",
        "",
        f"- Candidate records: `{report['summary']['candidate_records']}`",
        f"- Visual-QC records: `{report['summary']['visual_qc_records']}`",
        f"- Candidate text records: `{report['summary']['candidate_text_records']}`",
        f"- Later human-ready records: `{report['summary']['later_human_ready_records']}`",
        "- Human review ready: `false`",
        "",
        "## Rebuild Records",
        "",
        "| Region admission | Status | Human-ready | Blockers |",
        "|---|---|---:|---|",
    ]
    for record in candidates:
        blockers = ", ".join(record["blockers"]) if record["blockers"] else "none"
        lines.append(
            f"| `{record['region_admission_id']}` | `{record['rebuild_status']}` | `{str(record['human_review_ready']).lower()}` | {blockers} |"
        )
    for record in visuals:
        blockers = ", ".join(record["blockers"])
        lines.append(
            f"| `{record['region_admission_id']}` | `visual_qc_blocked` | `false` | {blockers} |"
        )
    lines.extend(
        [
            "",
            "## Output Hashes",
            "",
            "| Output | SHA-256 |",
            "|---|---|",
        ]
    )
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_rebuild_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    (OUT_ROOT / "source_reconstruction_rebuild_manifest.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    check_authorization()
    build()
