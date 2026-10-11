from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SRCO_ROOT = TRIAL_ROOT / "source_reconstruction_crop_overlay_G1_VIRAL_001"
SRRB_ROOT = TRIAL_ROOT / "source_reconstruction_rebuild_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_visual_overlay_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-VISUAL-OVERLAY-REVIEW-001"
REPORT_ID = "SRVO-G1-VIRAL-001"
SRCO_SHA256 = "08B77397484FF43C6E4E466632531B15829EA3C34A75F79C6DE84B70E433C78F"
SRRB_SHA256 = "E4E442446B1609E11E74F5EA0E970037BBA996284D090AF5E7873FBA0112E5E2"


MANUAL_DECISIONS: dict[str, dict[str, object]] = {
    "SRA-G1-VIRAL-001-R001": {
        "decision_status": "visual_component_review_closed",
        "decision": "visual_only_component_excluded_from_source_text_candidate",
        "candidate_text": None,
        "candidate_text_basis": None,
        "human_review_ready": True,
        "closed_blockers": ["visual_component_requires_manual_decision"],
        "remaining_blockers": [],
        "decision_note": "Decorative cover/title treatment is visual-only in this reconstruction slice; no source-text candidate is created.",
    },
    "SRA-G1-VIRAL-001-R002": {
        "decision_status": "overlay_review_closed",
        "decision": "overlay_readable_candidate_text_ready",
        "candidate_text": "Contents",
        "candidate_text_basis": "manual_visual_overlay_review",
        "human_review_ready": True,
        "closed_blockers": ["overlay_review_required"],
        "remaining_blockers": [],
        "decision_note": "Overlay reference visibly contains the heading Contents.",
    },
    "SRA-G1-VIRAL-001-R003": {
        "decision_status": "overlay_and_full_region_review_closed",
        "decision": "manual_full_region_candidate_text_ready",
        "candidate_text": "Introduction\nSummary\nOverview\nThe Spektral Krew",
        "candidate_text_basis": "manual_visual_review_of_full_source_crop",
        "human_review_ready": True,
        "closed_blockers": ["overlay_review_required", "full_contents_region_not_replaced"],
        "remaining_blockers": [],
        "decision_note": "Refined OCR remains evidence-only; full-region candidate text comes from visual review of the source crop and is not source acceptance.",
    },
    "SRA-G1-VIRAL-001-R004": {
        "decision_status": "overlay_review_closed",
        "decision": "overlay_readable_candidate_text_ready",
        "candidate_text": "Introduction",
        "candidate_text_basis": "manual_visual_overlay_review",
        "human_review_ready": True,
        "closed_blockers": ["overlay_review_required"],
        "remaining_blockers": [],
        "decision_note": "Overlay reference visibly contains the section heading Introduction.",
    },
    "SRA-G1-VIRAL-001-R005": {
        "decision_status": "carried_forward_ready",
        "decision": "candidate_text_carried_forward",
        "candidate_text": "\u201cWe are the Spektral Krew, and we go places and do things you\nwould never do.\u201d \u2014 Marco Proudfoot",
        "candidate_text_basis": "srrb_carried_forward_candidate_text",
        "human_review_ready": True,
        "closed_blockers": [],
        "remaining_blockers": [],
        "decision_note": "Already ready in SRRB; carried forward without source acceptance.",
    },
    "SRA-G1-VIRAL-001-R006": {
        "decision_status": "visual_qc_review_closed",
        "decision": "visual_only_component_excluded_from_source_text_candidate",
        "candidate_text": None,
        "candidate_text_basis": None,
        "human_review_ready": True,
        "closed_blockers": ["visual_qc_manual_decision_required"],
        "remaining_blockers": [],
        "decision_note": "Cover visual component is visual-only for this source reconstruction slice.",
    },
    "SRA-G1-VIRAL-001-R007": {
        "decision_status": "visual_qc_review_closed",
        "decision": "non_source_layout_background_excluded",
        "candidate_text": None,
        "candidate_text_basis": None,
        "human_review_ready": True,
        "closed_blockers": ["visual_qc_manual_decision_required"],
        "remaining_blockers": [],
        "decision_note": "Reference crop contains background/layout texture only; no source-text candidate is created.",
    },
}


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
    parser = argparse.ArgumentParser(description="Record visual/overlay source reconstruction review decisions.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("source reconstruction visual/overlay review is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"source reconstruction visual/overlay review requires {AUTHORIZATION_ID}")


def by_region(records: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    return {str(record["region_admission_id"]): record for record in records}


def normalize_path(path: object) -> str:
    return str(path)


def build_review_record(
    srrb_record: dict[str, object],
    srco_record: dict[str, object] | None,
    record_kind: str,
) -> dict[str, object]:
    region_id = str(srrb_record["region_admission_id"])
    decision = MANUAL_DECISIONS[region_id]
    reference_path = ROOT / normalize_path(srrb_record["crop_reference"])
    if not reference_path.exists():
        raise SystemExit(f"missing visual reference for {region_id}")
    if sha256_file(reference_path) != srrb_record["crop_reference_sha256"]:
        raise SystemExit(f"visual reference hash mismatch for {region_id}")

    source_crop = None
    source_crop_sha256 = None
    if srco_record is not None:
        artifact = srco_record["crop_overlay_artifact"]
        source_crop = normalize_path(artifact["source_input_crop"])
        source_crop_sha256 = artifact["source_input_crop_sha256"]
        source_path = ROOT / source_crop
        if not source_path.exists():
            raise SystemExit(f"missing source crop for {region_id}")
        if sha256_file(source_path) != source_crop_sha256:
            raise SystemExit(f"source crop hash mismatch for {region_id}")

    return {
        "region_admission_id": region_id,
        "record_kind": record_kind,
        "sample_id": srrb_record["sample_id"],
        "page_id": srrb_record["page_id"],
        "region_id": srrb_record["region_id"],
        "predecessor_zone_id": srrb_record["predecessor_zone_id"],
        "route_class": srrb_record["route_class"],
        "review_class": srrb_record["review_class"],
        "visual_reference": srrb_record["crop_reference"],
        "visual_reference_sha256": srrb_record["crop_reference_sha256"],
        "source_input_crop": source_crop,
        "source_input_crop_sha256": source_crop_sha256,
        "predecessor_blockers": srrb_record.get("blockers", []),
        "decision_status": decision["decision_status"],
        "decision": decision["decision"],
        "candidate_text": decision["candidate_text"],
        "candidate_text_basis": decision["candidate_text_basis"],
        "human_review_ready": decision["human_review_ready"],
        "closed_blockers": decision["closed_blockers"],
        "remaining_blockers": decision["remaining_blockers"],
        "decision_note": decision["decision_note"],
        "source_acceptance": False,
        "qa_acceptance": False,
    }


def build() -> None:
    srco_report_path = SRCO_ROOT / "source_reconstruction_crop_overlay_report.json"
    srrb_report_path = SRRB_ROOT / "source_reconstruction_rebuild_report.json"
    if sha256_file(srco_report_path) != SRCO_SHA256:
        raise SystemExit("SRCO report hash mismatch")
    if sha256_file(srrb_report_path) != SRRB_SHA256:
        raise SystemExit("SRRB report hash mismatch")

    srco = read_json(srco_report_path)
    srrb = read_json(srrb_report_path)
    if srco["report_id"] != "SRCO-G1-VIRAL-001":
        raise SystemExit("unexpected SRCO report id")
    if srrb["package_id"] != "SRRB-G1-VIRAL-001":
        raise SystemExit("unexpected SRRB package id")

    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    srco_candidates = by_region(srco["candidate_records"])
    srco_visuals = by_region(srco["visual_qc_records"])
    candidate_records = [
        build_review_record(record, srco_candidates.get(str(record["region_admission_id"])), "candidate")
        for record in srrb["candidate_records"]
    ]
    visual_qc_records = [
        build_review_record(record, srco_visuals.get(str(record["region_admission_id"])), "visual_qc")
        for record in srrb["visual_qc_records"]
    ]
    records = candidate_records + visual_qc_records
    if set(MANUAL_DECISIONS) != {str(record["region_admission_id"]) for record in records}:
        raise SystemExit("manual decision coverage mismatch")

    remaining_blockers = [
        {
            "region_admission_id": record["region_admission_id"],
            "remaining_blockers": record["remaining_blockers"],
        }
        for record in records
        if record["remaining_blockers"]
    ]
    candidate_text_records = [
        record for record in candidate_records if record["candidate_text"] is not None
    ]
    report = {
        "report_id": REPORT_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "visual_overlay_blockers_closed_for_later_human_review",
        "input_package_id": "SRRB-G1-VIRAL-001",
        "input_package_sha256": SRRB_SHA256,
        "input_crop_overlay_report_id": "SRCO-G1-VIRAL-001",
        "input_crop_overlay_report_sha256": SRCO_SHA256,
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "candidate_text_is_source_accepted": False,
        "human_review_ready": True,
        "human_review_blocked": False,
        "candidate_records": candidate_records,
        "visual_qc_records": visual_qc_records,
        "summary": {
            "candidate_records": len(candidate_records),
            "visual_qc_records": len(visual_qc_records),
            "candidate_text_records": len(candidate_text_records),
            "visual_only_records": sum(1 for record in records if record["candidate_text"] is None),
            "closed_blocker_records": sum(1 for record in records if record["closed_blockers"]),
            "remaining_blockers": remaining_blockers,
            "human_review_ready_records": sum(1 for record in records if record["human_review_ready"] is True),
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-HUMAN-PACKAGE-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_visual_overlay_review_report.json", report)

    candidate_lines = [
        "# Source Reconstruction Candidate Text - SRVO-G1-VIRAL-001",
        "",
        "Status: `ready_for_later_human_review_not_source_accepted`",
        "",
        "Boundary: candidate text below is not accepted source text, not QA acceptance, and not Gate 1 advancement.",
        "",
    ]
    for record in candidate_records:
        candidate_lines.append(f"## {record['region_admission_id']}")
        candidate_lines.append("")
        candidate_lines.append(f"- Decision: `{record['decision']}`")
        candidate_lines.append(f"- Basis: `{record['candidate_text_basis'] or 'none'}`")
        candidate_lines.append("")
        if record["candidate_text"] is None:
            candidate_lines.append("No source-text candidate created.")
        else:
            candidate_lines.append("```text")
            candidate_lines.append(str(record["candidate_text"]))
            candidate_lines.append("```")
        candidate_lines.append("")
    (OUT_ROOT / "candidate_text_for_later_human_review.md").write_text("\n".join(candidate_lines), encoding="utf-8")

    manifest_lines = [
        "# Source Reconstruction Visual/Overlay Review - SRVO-G1-VIRAL-001",
        "",
        "Status: `visual_overlay_blockers_closed_for_later_human_review`",
        "",
        "Boundary: no OCR, PDF parsing, rendering, raw OCR edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Summary",
        "",
        f"- Candidate records: `{report['summary']['candidate_records']}`",
        f"- Visual-QC records: `{report['summary']['visual_qc_records']}`",
        f"- Candidate text records: `{report['summary']['candidate_text_records']}`",
        f"- Visual-only records: `{report['summary']['visual_only_records']}`",
        f"- Remaining blockers: `{len(remaining_blockers)}`",
        "- Human review ready: `true`",
        "- Source accepted: `false`",
        "",
        "## Decisions",
        "",
        "| Region admission | Decision | Human-ready | Remaining blockers |",
        "|---|---|---:|---|",
    ]
    for record in records:
        remaining = ", ".join(record["remaining_blockers"]) if record["remaining_blockers"] else "none"
        manifest_lines.append(
            f"| `{record['region_admission_id']}` | `{record['decision']}` | `{str(record['human_review_ready']).lower()}` | {remaining} |"
        )
    manifest_lines.extend(
        [
            "",
            "## Output Hashes",
            "",
            "| Output | SHA-256 |",
            "|---|---|",
        ]
    )
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_visual_overlay_review_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    (OUT_ROOT / "source_reconstruction_visual_overlay_review_manifest.md").write_text(
        "\n".join(manifest_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    check_authorization()
    build()
