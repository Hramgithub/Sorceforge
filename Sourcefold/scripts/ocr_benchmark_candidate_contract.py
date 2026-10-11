from __future__ import annotations

from typing import Any


OCR_BENCHMARK_CANDIDATE_SCHEMA_VERSION = "sourcefold_ocr_benchmark_candidate.v1"
REQUIRED_RAW_OUTPUTS = {"txt_sha256", "tsv_sha256", "log_sha256", "stderr_sha256"}


def validate_ocr_benchmark_candidate_contract(
    *,
    run: dict[str, Any],
    admitted_zone_ids: set[str],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    zones = run.get("zones")
    if not isinstance(zones, list) or not zones:
        findings.append({"finding_id": "ocr_benchmark_missing_zones"})
        zones = []

    zone_ids = {zone.get("zone_id") for zone in zones if zone.get("zone_id")}
    missing = sorted(admitted_zone_ids - zone_ids)
    extra = sorted(zone_ids - admitted_zone_ids)
    if missing:
        findings.append({"finding_id": "ocr_benchmark_missing_admitted_zone", "zone_ids": missing})
    if extra:
        findings.append({"finding_id": "ocr_benchmark_unadmitted_zone", "zone_ids": extra})

    if not run.get("ocr_profile_id"):
        findings.append({"finding_id": "ocr_benchmark_missing_profile"})
    if run.get("threshold_changed_after_results") is True:
        findings.append({"finding_id": "ocr_benchmark_threshold_changed_after_results"})
    if run.get("pdf_text_layer_used") is True:
        findings.append({"finding_id": "ocr_benchmark_pdf_text_layer_leakage"})
    if run.get("raw_outputs_mutated") is True:
        findings.append({"finding_id": "ocr_benchmark_raw_output_mutation"})
    if run.get("ocr_acceptance_created") is True:
        findings.append({"finding_id": "ocr_benchmark_acceptance_leakage"})
    if run.get("unauthorized_rerun") is True:
        findings.append({"finding_id": "ocr_benchmark_unauthorized_rerun"})

    for zone in zones:
        zone_id = zone.get("zone_id", "<missing>")
        if not zone.get("page_id") or not zone.get("crop_sha256"):
            findings.append({"finding_id": "ocr_benchmark_zone_missing_lineage", "zone_id": zone_id})
        zone_role = zone.get("zone_role")
        if zone_role not in {"ocr_candidate", "visual_qc_only"}:
            findings.append({"finding_id": "ocr_benchmark_unknown_zone_role", "zone_id": zone_id, "zone_role": zone_role})
        raw_outputs = zone.get("raw_outputs", {})
        if zone_role == "ocr_candidate":
            missing_outputs = sorted(REQUIRED_RAW_OUTPUTS - set(raw_outputs))
            if missing_outputs:
                findings.append({"finding_id": "ocr_benchmark_missing_raw_output_hashes", "zone_id": zone_id, "fields": missing_outputs})
        if zone_role == "visual_qc_only" and raw_outputs:
            findings.append({"finding_id": "ocr_benchmark_visual_qc_has_ocr_output", "zone_id": zone_id})

    return {
        "schema_version": OCR_BENCHMARK_CANDIDATE_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "zone_count": len(zones),
        "admitted_zone_ids": sorted(admitted_zone_ids),
        "findings": findings,
    }


def require_ocr_benchmark_candidate_contract(
    *,
    run: dict[str, Any],
    admitted_zone_ids: set[str],
    consumer: str,
) -> dict[str, Any]:
    validation = validate_ocr_benchmark_candidate_contract(run=run, admitted_zone_ids=admitted_zone_ids)
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by OCR benchmark candidate contract: {validation['findings']}")
    return validation
