from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "source_reconstruction_remediation_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_crop_overlay_G1_VIRAL_001"
CROP_ROOT = OUT_ROOT / "crop_overlay_refs"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001"
REPORT_ID = "SRCO-G1-VIRAL-001"


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def repo_path(path: Path) -> str:
    return str(path.relative_to(ROOT))


def copy_ref(record: dict[str, object], suffix: str) -> dict[str, object]:
    source = ROOT / str(record["input_crop"])
    target = CROP_ROOT / f"{record['region_admission_id']}__{suffix}.png"
    shutil.copyfile(source, target)
    with Image.open(target) as image:
        size = {"width": image.width, "height": image.height}
    return {
        "path": repo_path(target),
        "sha256": sha256_file(target),
        "basis": "existing_input_crop_exact_copy",
        "source_input_crop": record["input_crop"],
        "source_input_crop_sha256": sha256_file(source),
        "size_px": size,
    }


def narrow_ref(record: dict[str, object], suffix: str, box: tuple[int, int, int, int]) -> dict[str, object]:
    source = ROOT / str(record["input_crop"])
    target = CROP_ROOT / f"{record['region_admission_id']}__{suffix}.png"
    with Image.open(source) as image:
        cropped = image.crop(box)
        cropped.save(target)
        source_size = {"width": image.width, "height": image.height}
        target_size = {"width": cropped.width, "height": cropped.height}
    return {
        "path": repo_path(target),
        "sha256": sha256_file(target),
        "basis": "existing_input_crop_derived_subcrop",
        "source_input_crop": record["input_crop"],
        "source_input_crop_sha256": sha256_file(source),
        "source_size_px": source_size,
        "subcrop_box_px": {"left": box[0], "top": box[1], "right": box[2], "bottom": box[3]},
        "size_px": target_size,
    }


def route_anchor(record: dict[str, object]) -> dict[str, object]:
    return {
        "region_admission_id": record["region_admission_id"],
        "sample_id": record["sample_id"],
        "page_id": record["page_id"],
        "region_id": record["region_id"],
        "predecessor_zone_id": record["predecessor_zone_id"],
        "predecessor_crop_sha256": record["predecessor_crop_sha256"],
        "page_image": record["page_image"],
        "input_crop": record["input_crop"],
        "route_class": record["route_class"],
        "review_class": record["review_class"],
        "selected_config": record.get("selected_config"),
        "candidate_text_sha256": record.get("candidate_text_sha256"),
        "candidate_tsv_sha256": record.get("candidate_tsv_sha256"),
        "overlay_qc_status": record.get("overlay_qc_status"),
        "order_qc_status": record.get("order_qc_status"),
    }


def remediate_candidate(record: dict[str, object]) -> dict[str, object]:
    region_id = str(record["region_admission_id"])
    base = route_anchor(record)

    if region_id == "SRA-G1-VIRAL-001-R001":
        return base | {
            "remediation_status": "visual_component_demoted_from_text_review",
            "human_review_ready": False,
            "new_ocr_required": False,
            "source_acceptance": False,
            "cleaned_candidate_text": None,
            "crop_overlay_artifact": copy_ref(record, "visual_reference"),
            "next_action": "keep_visual_qc_only_until_manual_visual_decision",
        }
    if region_id == "SRA-G1-VIRAL-001-R002":
        return base | {
            "remediation_status": "noise_stripped_overlay_reference_ready",
            "human_review_ready": False,
            "new_ocr_required": False,
            "source_acceptance": False,
            "cleaned_candidate_text": record["cleaned_candidate_text"],
            "crop_overlay_artifact": copy_ref(record, "overlay_reference"),
            "next_action": "include_in_later_human_package_after_overlay_review",
        }
    if region_id == "SRA-G1-VIRAL-001-R003":
        return base | {
            "remediation_status": "narrow_subcrop_prepared_for_later_ocr_rerun",
            "human_review_ready": False,
            "new_ocr_required": True,
            "source_acceptance": False,
            "cleaned_candidate_text": None,
            "crop_overlay_artifact": narrow_ref(record, "narrow_contents_candidate", (0, 0, 560, 235)),
            "next_action": "run_bounded_ocr_on_refined_crop_after_separate_authorization",
        }
    if region_id == "SRA-G1-VIRAL-001-R004":
        return base | {
            "remediation_status": "clean_text_overlay_reference_ready",
            "human_review_ready": False,
            "new_ocr_required": False,
            "source_acceptance": False,
            "cleaned_candidate_text": record["cleaned_candidate_text"],
            "crop_overlay_artifact": copy_ref(record, "overlay_reference"),
            "next_action": "include_in_later_human_package_after_overlay_review",
        }
    if region_id == "SRA-G1-VIRAL-001-R005":
        return base | {
            "remediation_status": "carried_forward_candidate",
            "human_review_ready": True,
            "new_ocr_required": False,
            "source_acceptance": False,
            "cleaned_candidate_text": record["cleaned_candidate_text"],
            "crop_overlay_artifact": copy_ref(record, "carry_forward_reference"),
            "next_action": "carry_forward_to_later_human_package",
        }
    raise AssertionError(f"unexpected region id {region_id}")


def remediate_visual(record: dict[str, object]) -> dict[str, object]:
    base = route_anchor(record)
    return base | {
        "remediation_status": "visual_qc_reference_ready",
        "human_review_ready": False,
        "new_ocr_required": False,
        "source_acceptance": False,
        "candidate_text_created": False,
        "crop_overlay_artifact": copy_ref(record, "visual_qc_reference"),
        "next_action": "keep_visual_qc_only_until_manual_visual_decision",
    }


def build() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    CROP_ROOT.mkdir(parents=True, exist_ok=True)
    triage = read_json(INPUT_ROOT / "source_reconstruction_remediation_report.json")
    candidates = [remediate_candidate(record) for record in triage["candidate_records"]]
    visual = [remediate_visual(record) for record in triage["visual_qc_records"]]
    all_records = candidates + visual

    report = {
        "report_id": REPORT_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "crop_overlay_remediation_evidence_only",
        "input_report_id": triage["report_id"],
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "ocr_executed": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "candidate_records": candidates,
        "visual_qc_records": visual,
        "summary": {
            "records": len(all_records),
            "candidate_records": len(candidates),
            "visual_qc_records": len(visual),
            "ready_for_later_human_review": sum(1 for record in candidates if record["human_review_ready"]),
            "overlay_reference_ready": sum(1 for record in candidates if "overlay_reference" in record["crop_overlay_artifact"]["path"]),
            "visual_qc_reference_ready": len(visual),
            "new_ocr_required": sum(1 for record in candidates if record["new_ocr_required"]),
        },
        "human_review_ready": False,
        "human_review_blocked": True,
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_crop_overlay_report.json", report)

    lines = [
        "# Source Reconstruction Crop/Overlay Remediation - SRCO-G1-VIRAL-001",
        "",
        "Status: `crop_overlay_remediation_evidence_only`",
        "",
        "Boundary: no OCR, PDF parsing, raw OCR output edits, source acceptance, QA acceptance, fixtures, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "Human review remains blocked. This package prepares exact crop/overlay references and one refined crop for a later bounded OCR run.",
        "",
        "## Summary",
        "",
        f"- Candidate records: `{report['summary']['candidate_records']}`",
        f"- Visual-QC records: `{report['summary']['visual_qc_records']}`",
        f"- Ready for later human review: `{report['summary']['ready_for_later_human_review']}`",
        f"- Overlay references ready: `{report['summary']['overlay_reference_ready']}`",
        f"- Refined OCR rerun required: `{report['summary']['new_ocr_required']}`",
        "",
        "## Record Remediation",
        "",
        "| Region admission | Status | Next action | Artifact |",
        "|---|---|---|---|",
    ]
    for record in candidates:
        artifact = record["crop_overlay_artifact"]["path"]
        lines.append(
            f"| `{record['region_admission_id']}` | `{record['remediation_status']}` | `{record['next_action']}` | `{artifact}` |"
        )
    for record in visual:
        artifact = record["crop_overlay_artifact"]["path"]
        lines.append(
            f"| `{record['region_admission_id']}` | `{record['remediation_status']}` | `{record['next_action']}` | `{artifact}` |"
        )
    lines.extend(
        [
            "",
            "## Next",
            "",
            "Create a separate bounded refined OCR authorization for only the prepared refined crop(s), then rebuild the human review candidate package if evidence improves.",
        ]
    )
    (OUT_ROOT / "source_reconstruction_crop_overlay_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
