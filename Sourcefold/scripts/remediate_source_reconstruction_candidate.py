from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
REVIEW_ROOT = TRIAL_ROOT / "source_reconstruction_review_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_remediation_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-REMEDIATE-001"
REPORT_ID = "SRCR-G1-VIRAL-001"


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def normalize_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def classify(record: dict[str, object]) -> dict[str, object]:
    lines = normalize_lines(str(record["candidate_text"]))
    region_id = record["region_admission_id"]
    overlay = record["overlay_qc_status"]
    route_anchor = {
        "region_admission_id": region_id,
        "sample_id": record["sample_id"],
        "page_id": record["page_id"],
        "region_id": record["region_id"],
        "predecessor_zone_id": record["predecessor_zone_id"],
        "predecessor_crop_sha256": record["predecessor_crop_sha256"],
        "page_image": record["page_image"],
        "input_crop": record["input_crop"],
        "route_class": record["route_class"],
        "review_class": record["review_class"],
        "selected_config": record["selected_config"],
        "candidate_text_sha256": record["candidate_text_sha256"],
        "candidate_tsv_sha256": record["candidate_tsv_sha256"],
        "overlay_qc_status": record["overlay_qc_status"],
        "order_qc_status": record["order_qc_status"],
    }

    if region_id == "SRA-G1-VIRAL-001-R001":
        return route_anchor | {
            "status": "blocked_visual_component",
            "reason": "cover title split still has visual-only title component and bad geometry",
            "recommended_next_action": "visual_crop_remediation",
            "cleaned_candidate_text": None,
            "human_review_ready": False,
        }
    if region_id == "SRA-G1-VIRAL-001-R002":
        cleaned = [line for line in lines if not (len(line) <= 2 and line.islower())]
        return route_anchor | {
            "status": "cleanup_candidate_needs_overlay_verify",
            "reason": "low-confidence short noise can be stripped, but overlay still needs visual verification",
            "recommended_next_action": "overlay_verify_after_cleanup",
            "cleaned_candidate_text": "\n".join(cleaned),
            "human_review_ready": False,
        }
    if region_id == "SRA-G1-VIRAL-001-R003":
        return route_anchor | {
            "status": "blocked_overbroad_crop",
            "reason": "candidate includes extra contents-adjacent heading text from an overbroad crop",
            "recommended_next_action": "narrow_contents_crop_remediation",
            "cleaned_candidate_text": None,
            "human_review_ready": False,
        }
    if region_id == "SRA-G1-VIRAL-001-R004":
        return route_anchor | {
            "status": "text_clean_needs_overlay_verify",
            "reason": f"text is clean but overlay status is {overlay}",
            "recommended_next_action": "overlay_verify",
            "cleaned_candidate_text": "\n".join(lines),
            "human_review_ready": False,
        }
    if region_id == "SRA-G1-VIRAL-001-R005":
        return route_anchor | {
            "status": "candidate_ready_for_later_human_review",
            "reason": "candidate text and overlay/order checks are suitable for a later package",
            "recommended_next_action": "carry_forward",
            "cleaned_candidate_text": "\n".join(lines),
            "human_review_ready": True,
        }
    raise AssertionError(f"unexpected region id {region_id}")


def build() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    run_manifest = read_json(REVIEW_ROOT / "source_reconstruction_run_manifest.json")
    records = [classify(record) for record in run_manifest["candidate_records"]]
    visual_queue = run_manifest["visual_qc_queue"]

    report = {
        "report_id": REPORT_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "remediation_triage_only",
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "input_run_manifest": "SRM-G1-VIRAL-001",
        "candidate_records": records,
        "visual_qc_records": visual_queue,
        "summary": {
            "candidate_records": len(records),
            "ready_for_later_human_review": sum(1 for record in records if record["human_review_ready"]),
            "needs_overlay_verify": sum(1 for record in records if "overlay" in record["recommended_next_action"]),
            "needs_crop_remediation": sum(1 for record in records if "crop" in record["recommended_next_action"]),
            "visual_qc_only_records": len(visual_queue),
        },
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_remediation_report.json", report)

    lines = [
        "# Source Reconstruction Candidate Remediation - SRCR-G1-VIRAL-001",
        "",
        "Status: `remediation_triage_only`",
        "",
        "Boundary: no OCR, PDF parsing, raw-output edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Summary",
        "",
        f"- Candidate records: `{report['summary']['candidate_records']}`",
        f"- Ready for later human review: `{report['summary']['ready_for_later_human_review']}`",
        f"- Needs overlay verify: `{report['summary']['needs_overlay_verify']}`",
        f"- Needs crop remediation: `{report['summary']['needs_crop_remediation']}`",
        f"- Visual-QC-only records: `{report['summary']['visual_qc_only_records']}`",
        "",
        "## Record Triage",
        "",
        "| Region admission | Status | Next action |",
        "|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| `{record['region_admission_id']}` | `{record['status']}` | `{record['recommended_next_action']}` |"
        )
    lines.extend(
        [
            "",
            "## Next",
            "",
            "Create a separate bounded crop/overlay remediation authorization before any new OCR or human source review.",
        ]
    )
    (OUT_ROOT / "source_reconstruction_remediation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
