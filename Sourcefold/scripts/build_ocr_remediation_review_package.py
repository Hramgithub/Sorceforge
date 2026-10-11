from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MATRIX_ROOT = TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "ocr_remediation_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-REMEDIATION-REVIEW-001"
REVIEW_ID = "ORR-G1-VIRAL-001"
ADMISSION_CANDIDATE_ID = "OAC-G1-VIRAL-001"
ROLLUP_ID = "GER-G1-VIRAL-001"
NEGATIVE_CHECK_ID = "ONC-G1-VIRAL-001"
PREDECESSOR_COMMIT = "f90d170b"

EXPECTED_SAMPLES = {
    "GS-G1-VIRAL-001",
    "GS-G1-VIRAL-002",
    "GS-G1-VIRAL-003",
    "GS-G1-VIRAL-004",
    "GS-G1-VIRAL-005",
}
EXPECTED_PSM = {1, 4, 8, 11}
DISABLED_DEFAULT_PSM = {3, 6}
EXPECTED_VARIANTS = {"original", "enhanced_x2", "binary_x3", "white_mask_x4"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def require(condition: bool, message: str, checks: list[dict[str, object]]) -> None:
    checks.append({"name": message, "passed": bool(condition)})
    if not condition:
        raise AssertionError(message)


def build() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    report_path = MATRIX_ROOT / "ocr_remediation_matrix_report.json"
    rows_path = MATRIX_ROOT / "ocr_remediation_matrix_rows.json"
    manifest_path = MATRIX_ROOT / "ocr_remediation_output_manifest.md"
    plan_path = MATRIX_ROOT / "ocr_remediation_plan.json"

    matrix_report = read_json(report_path)
    matrix_rows = read_json(rows_path)
    checks: list[dict[str, object]] = []

    aggregate = matrix_report["aggregate"]
    samples = matrix_report["samples"]
    row_samples = {row["sample_id"] for row in matrix_rows}
    row_psm = {row["psm"] for row in matrix_rows}
    row_variants = {row["variant"] for row in matrix_rows}

    require(matrix_report["run_id"] == "ORM-G1-VIRAL-001", "predecessor ORM id is exact", checks)
    require(matrix_report["status"] == "remediation_evidence_only", "predecessor status remains remediation evidence only", checks)
    require(set(sample["sample_id"] for sample in samples) == EXPECTED_SAMPLES, "exact five sample set is present", checks)
    require(row_samples == EXPECTED_SAMPLES, "matrix rows cover exact five sample set", checks)
    require(aggregate["samples"] == 5, "aggregate sample count is five", checks)
    require(aggregate["remediation_route_pass"] == 5, "all five samples have remediation-route pass", checks)
    require(aggregate["ocr_normalized_exact_zones"] == 5, "five OCR zones have normalized exact evidence", checks)
    require(aggregate["visual_qc_route_zones"] == 2, "two zones are routed to visual QC", checks)
    require(aggregate["source_acceptance"] is False, "source acceptance flag is false", checks)
    require(aggregate["gate_1_advancement"] is False, "Gate 1 advancement flag is false", checks)
    require(aggregate["approved_by_score"] is False, "approved-by-score flag is false", checks)
    require(len(matrix_rows) == 80, "matrix row count is 80", checks)
    require(row_psm == EXPECTED_PSM, "default matrix PSM set is 1/4/8/11", checks)
    require(row_psm.isdisjoint(DISABLED_DEFAULT_PSM), "disabled PSM 3/6 are absent from default rows", checks)
    require(row_variants == EXPECTED_VARIANTS, "all four Sourcefold-native variants are represented", checks)
    require(all(row["exit_code"] == 0 for row in matrix_rows), "all matrix OCR rows exited zero", checks)
    require(all(row.get("text_sha256") and row.get("tsv_sha256") for row in matrix_rows), "all rows bind text and TSV hashes", checks)
    require(all(row.get("stderr_sha256") and row.get("log_sha256") for row in matrix_rows), "all rows bind stderr and command log hashes", checks)

    selected_ocr_zones: list[dict[str, object]] = []
    visual_qc_zones: list[dict[str, object]] = []
    for sample in samples:
        for zone in sample["zones"]:
            item = {
                "sample_id": sample["sample_id"],
                "sample_type": sample["sample_type"],
                "zone_id": zone["zone_id"],
                "route": zone["route"],
                "finding": zone["finding"],
                "expected_label": zone["expected_label"],
                "crop_sha256": zone["crop_sha256"],
            }
            if zone["route"] == "ocr":
                item.update(
                    {
                        "selected_config": zone["selected_config"],
                        "selected_text_sha256": zone["selected_text_sha256"],
                        "selected_tsv_sha256": zone["selected_tsv_sha256"],
                        "normalized_exact": zone["normalized_exact"],
                        "token_recall": zone["token_recall"],
                        "char_error_rate": zone["char_error_rate"],
                        "overlay_qc_status": zone["overlay_qc"]["status"],
                        "order_qc_status": zone["order_qc"]["status"],
                    }
                )
                selected_ocr_zones.append(item)
            else:
                visual_qc_zones.append(item)

    require(len(selected_ocr_zones) == 5, "selected OCR zone count is five", checks)
    require(len(visual_qc_zones) == 2, "visual-QC route count is two", checks)
    require(all(zone["normalized_exact"] is True for zone in selected_ocr_zones), "selected OCR zones are normalized exact", checks)
    require(all(zone["token_recall"] == 1.0 for zone in selected_ocr_zones), "selected OCR zones have full token recall", checks)

    review = {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "remediation_evidence_only",
        "review_state": "valid_for_review",
        "predecessor": {
            "run_id": "ORM-G1-VIRAL-001",
            "authorization_id": "BA-G1-VIRAL-REMEDIATE-001",
            "authorization_status": "expired",
            "authorization_scope_consumed_by": "ORM-G1-VIRAL-001",
            "matrix_report_path": rel(report_path),
            "matrix_report_sha256": sha256_file(report_path),
            "matrix_rows_path": rel(rows_path),
            "matrix_rows_sha256": sha256_file(rows_path),
            "output_manifest_path": rel(manifest_path),
            "output_manifest_sha256": sha256_file(manifest_path),
            "remediation_plan_path": rel(plan_path),
            "remediation_plan_sha256": sha256_file(plan_path),
            "commit": PREDECESSOR_COMMIT,
        },
        "finding": "remediation_review_ready_for_gate_rollup",
        "aggregate": aggregate,
        "selected_ocr_zones": selected_ocr_zones,
        "visual_qc_zones": visual_qc_zones,
        "boundaries": {
            "new_ocr_executed": False,
            "pdf_opened_or_parsed": False,
            "raw_text_promoted": False,
            "source_acceptance": False,
            "gate_1_advancement": False,
            "translation_or_proofreading": False,
            "human_review_required_now": False,
            "human_review_required_when": "source_reconstruction_review_package_contains_readable_text",
        },
    }

    admission_candidate = {
        "candidate_id": ADMISSION_CANDIDATE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "remediation_evidence_only",
        "candidate_state": "candidate_for_future_gate_review",
        "basis": REVIEW_ID,
        "recommended_profile_scope": "five-sample-remediation-evidence-only",
        "recommended_default_psm_modes": [1, 4, 8, 11],
        "disabled_default_psm_modes": [3, 6],
        "recommended_variants": sorted(EXPECTED_VARIANTS),
        "route_rules": {
            "ocr": "Use only where route and sample evidence support normalized-exact OCR inspection.",
            "visual_qc": "Route decorative, ambiguous, or page-number-like components to visual QC without text acceptance.",
        },
        "selected_ocr_configs": selected_ocr_zones,
        "not_authorized": [
            "source_acceptance",
            "gate_1_advancement",
            "accepted_source_text",
            "translation",
            "proofreading",
            "renderer_profile_acceptance",
            "implementation",
            "new_ocr_execution",
        ],
        "approved_by_score": False,
    }

    rollup = {
        "rollup_id": ROLLUP_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "remediation_evidence_only",
        "rollup_state": "evidence_rollup_for_review",
        "predecessor_commit": PREDECESSOR_COMMIT,
        "inputs": {
            "pre_ocr_map_bundle": matrix_report["inputs"]["pre_ocr_map_bundle"],
            "gold_sample_manifest": matrix_report["inputs"]["gold_sample_manifest"],
            "ocr_candidate_manifest": matrix_report["inputs"]["ocr_candidate_manifest"],
            "baseline_benchmark_result": matrix_report["inputs"]["baseline_benchmark_result"],
            "remediation_matrix": "ORM-G1-VIRAL-001",
        },
        "outputs": {
            "remediation_review": REVIEW_ID,
            "ocr_admission_candidate": ADMISSION_CANDIDATE_ID,
            "negative_check_report": NEGATIVE_CHECK_ID,
        },
        "gate_boundary": {
            "ready_for_gate_rollup": True,
            "ready_for_human_source_review": False,
            "source_acceptance": False,
            "gate_1_advancement": False,
            "requires_separate_source_reconstruction_package": True,
        },
        "artifact_hashes": review["predecessor"],
    }

    negative_checks = {
        "check_id": NEGATIVE_CHECK_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "remediation_evidence_only",
        "check_state": "passed",
        "basis": REVIEW_ID,
        "checks": checks
        + [
            {"name": "no PDF opened, parsed, rendered, recounted, or rehashed by this script", "passed": True},
            {"name": "no OCR executed by this script", "passed": True},
            {"name": "no raw OCR text payload is copied into review rollups", "passed": True},
            {"name": "human review remains deferred until readable source reconstruction package", "passed": True},
        ],
    }

    write_json(OUT_ROOT / "ocr_remediation_review_report.json", review)
    write_json(OUT_ROOT / "ocr_admission_candidate.json", admission_candidate)
    write_json(OUT_ROOT / "evidence_rollup.json", rollup)
    write_json(OUT_ROOT / "negative_check_report.json", negative_checks)

    review_lines = [
        "# OCR Remediation Review Report - ORR-G1-VIRAL-001",
        "",
        "Status: `remediation_evidence_only`; review state: `valid_for_review`",
        "",
        f"Authorization: `{AUTHORIZATION_ID}`",
        "",
        "Boundary: this report reviews `ORM-G1-VIRAL-001` remediation evidence only. It is not source acceptance, Gate 1 advancement, QA completion, fixture acceptance, translation, proofreading, renderer/profile acceptance, implementation, or a human source review.",
        "",
        "`BA-G1-VIRAL-REMEDIATE-001` is `expired`; its scope was consumed by `ORM-G1-VIRAL-001` and does not authorize new OCR, PDF parsing, QA, fixtures, source acceptance, translation, proofreading, or Gate 1 advancement.",
        "",
        "## Aggregate",
        "",
        f"- Samples: `{aggregate['samples']}`",
        f"- Remediation-route pass: `{aggregate['remediation_route_pass']}/5`",
        f"- OCR normalized-exact zones: `{aggregate['ocr_normalized_exact_zones']}`",
        f"- Visual-QC route zones: `{aggregate['visual_qc_route_zones']}`",
        "- Source acceptance: `false`",
        "- Gate 1 advancement: `false`",
        "- Approved by score: `false`",
        "",
        "## OCR Route Findings",
        "",
        "| Sample | Zone | Finding | Selected config | Token recall | CER | Overlay QC | Order QC |",
        "|---|---|---|---|---:|---:|---|---|",
    ]
    for zone in selected_ocr_zones:
        review_lines.append(
            f"| `{zone['sample_id']}` | `{zone['zone_id']}` | `{zone['finding']}` | "
            f"`{zone['selected_config']}` | `{zone['token_recall']}` | `{zone['char_error_rate']}` | "
            f"`{zone['overlay_qc_status']}` | `{zone['order_qc_status']}` |"
        )

    review_lines.extend(
        [
            "",
            "## Visual-QC Route Findings",
            "",
            "| Sample | Zone | Finding | Label |",
            "|---|---|---|---|",
        ]
    )
    for zone in visual_qc_zones:
        review_lines.append(
            f"| `{zone['sample_id']}` | `{zone['zone_id']}` | `{zone['finding']}` | `{zone['expected_label']}` |"
        )

    review_lines.extend(
        [
            "",
            "## Review Decision",
            "",
            "- `ORM-G1-VIRAL-001` is suitable as remediation evidence for a later Gate 1 rollup.",
        "- The matrix does not authorize source reconstruction approval or human proofreading.",
        "- Visual-QC route findings are routing evidence only; they are not transcription or text acceptance.",
        "- Overlay/QC caveats remain part of the review package and must be carried into any later human-readable reconstruction review.",
            "- Bogdan should be asked to review only after a separate source reconstruction package contains readable text aligned to page images/regions.",
            "",
            "## Invalidation",
            "",
            "This review stales if ORM output hashes, crop hashes, gold samples, OCR candidate identity, POMB/GSM/OCM/OBR predecessors, scoring rules, route rules, script revision, reviewer authority, or any upstream evidence changes.",
        ]
    )
    (OUT_ROOT / "ocr_remediation_review_report.md").write_text("\n".join(review_lines) + "\n", encoding="utf-8")

    orchestration_lines = [
        "# OCR Remediation Review Orchestration - ORR-G1-VIRAL-001",
        "",
        f"- Script: `scripts/build_ocr_remediation_review_package.py`",
        f"- Authorization: `{AUTHORIZATION_ID}`",
        f"- Generated review: `{REVIEW_ID}`",
        f"- Generated admission candidate: `{ADMISSION_CANDIDATE_ID}`",
        f"- Generated evidence rollup: `{ROLLUP_ID}`",
        f"- Generated negative checks: `{NEGATIVE_CHECK_ID}`",
        "- OCR executed by this script: `false`",
        "- PDF opened/parsed/rendered by this script: `false`",
        "- Raw OCR text promoted: `false`",
        "- Human review requested now: `false`",
        "",
        "Reproduce with:",
        "",
        "```powershell",
        "python scripts\\build_ocr_remediation_review_package.py",
        "python -m pytest tests\\test_ocr_remediation_review_package.py",
        "scripts\\validate_roadmap.ps1",
        "```",
    ]
    (OUT_ROOT / "orchestration_record.md").write_text("\n".join(orchestration_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
