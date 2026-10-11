from __future__ import annotations

from typing import Any


OCR_INPUT_SURFACE_POLICY_SCHEMA_VERSION = "sourcefold_ocr_input_surface_policy.v1"

OK_SEQUENCE_SIMILARITY = 0.997
OK_TOKEN_RECALL = 0.993
GEOMETRY_DIAGNOSTIC_MIN_TOKEN_RECALL = 0.97

SURFACE_CLASSES = {
    "review_crop",
    "text_evidence_crop",
    "ocr_candidate_crop",
    "full_page_region",
}
TEXT_REVIEW_SURFACES = {"review_crop", "text_evidence_crop"}
ALLOWED_PURPOSES = {
    "smoke_non_promotable",
    "remediation",
    "candidate_policy",
    "candidate_scoring_evidence",
}
IMPLEMENTATION_BOUNDARY_FLAGS = {
    "tesseract_invoked",
    "render_invoked",
    "pdf_parsed",
    "pdf_text_layer_read",
    "non_temp_artifact_write",
}

P018_OBSERVED_CONTROL_MEASUREMENT = {
    "page_id": "P018",
    "candidate_family": "full_page_expanded_overlap_psm4",
    "sequence_similarity_ratio": 0.999466,
    "token_recall": 0.996067,
    "lane_id": "C01TEFG017018-G1-VIRAL-001",
    "manifest_sha256": "A754D100659FA7900677C7BBAF49ACC06F991A8E8C2A02DECE59506EF8C6DAC0",
    "acceptance_effect": "none",
}


def _finding(finding_id: str, **extra: Any) -> dict[str, Any]:
    finding = {"finding_id": finding_id}
    finding.update(extra)
    return finding


def _page_number(page_id: Any) -> int | None:
    text = str(page_id or "").upper().removeprefix("P")
    if not text.isdigit():
        return None
    return int(text)


def _source_artifact_findings(surface: dict[str, Any]) -> list[dict[str, Any]]:
    artifact = surface.get("source_artifact")
    if not isinstance(artifact, dict):
        return [_finding("missing_source_artifact")]
    findings: list[dict[str, Any]] = []
    if not artifact.get("path"):
        findings.append(_finding("missing_source_artifact_path"))
    if not artifact.get("sha256"):
        findings.append(_finding("missing_source_artifact_hash"))
    if artifact.get("hash_status") not in {None, "matched"}:
        findings.append(_finding("source_artifact_hash_mismatch", hash_status=artifact.get("hash_status")))
    return findings


def validate_ocr_input_surface(surface: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    surface_class = surface.get("surface_class")
    purpose = surface.get("allowed_purpose")

    if surface_class not in SURFACE_CLASSES:
        findings.append(_finding("unknown_surface_class", surface_class=surface_class))
    if purpose == "acceptance_evidence":
        findings.append(_finding("acceptance_evidence_rejected_in_c01teisp"))
    elif purpose not in ALLOWED_PURPOSES:
        findings.append(_finding("unknown_allowed_purpose", allowed_purpose=purpose))

    page_number = _page_number(surface.get("page_id"))
    if page_number is None:
        findings.append(_finding("missing_or_invalid_page_id", page_id=surface.get("page_id")))
    elif page_number >= 21:
        findings.append(_finding("page_021_plus_blocked", page_id=surface.get("page_id")))

    findings.extend(_source_artifact_findings(surface))

    if surface_class in TEXT_REVIEW_SURFACES:
        if surface.get("ocr_allowed") is not False:
            findings.append(_finding("review_surface_ocr_allowed_must_default_false", surface_class=surface_class))
        if purpose != "smoke_non_promotable":
            findings.append(_finding("review_surface_not_promotable", surface_class=surface_class, allowed_purpose=purpose))

    if surface_class == "ocr_candidate_crop" and surface.get("ocr_allowed") is not True:
        findings.append(_finding("ocr_candidate_crop_requires_ocr_allowed_true"))

    if surface_class == "full_page_region":
        authorization = surface.get("authorization")
        required = {"full_page_region_authorization_id", "page_family", "region_policy", "negative_reason_not_baseline"}
        missing = sorted(key for key in required if not isinstance(authorization, dict) or not authorization.get(key))
        if missing:
            findings.append(_finding("full_page_region_missing_authorization", missing=missing))
        if surface.get("ocr_allowed") is not True:
            findings.append(_finding("full_page_region_requires_ocr_allowed_true"))

    for flag in sorted(IMPLEMENTATION_BOUNDARY_FLAGS):
        if surface.get(flag) is True:
            findings.append(_finding("implementation_boundary_violation", flag=flag))

    if surface.get("reference_loaded_before_candidate_hash") is True:
        findings.append(_finding("reference_loaded_before_candidate_hash"))

    return {
        "schema_version": OCR_INPUT_SURFACE_POLICY_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "surface_class": surface_class,
        "allowed_purpose": purpose,
        "findings": findings,
    }


def evaluate_against_observed_control_measurement(metrics: dict[str, float]) -> dict[str, Any]:
    similarity = float(metrics["sequence_similarity_ratio"])
    recall = float(metrics["token_recall"])
    similarity_delta = round(similarity - P018_OBSERVED_CONTROL_MEASUREMENT["sequence_similarity_ratio"], 6)
    recall_delta = round(recall - P018_OBSERVED_CONTROL_MEASUREMENT["token_recall"], 6)
    return {
        "observed_control_measurement": P018_OBSERVED_CONTROL_MEASUREMENT,
        "sequence_similarity_delta": similarity_delta,
        "token_recall_delta": recall_delta,
        "structure_order_assessment": "diagnostic_only",
        "completeness_assessment": "diagnostic_only",
        "auto_pass": False,
        "auto_fail": False,
        "auto_promote": False,
        "auto_accept": False,
    }


def route_ocr_input_surface(
    *,
    surface: dict[str, Any],
    metrics: dict[str, float] | None = None,
    diagnostic_flags: list[str] | None = None,
    candidate_text_hash_sealed: bool = True,
    scoring_report_complete: bool = True,
) -> dict[str, Any]:
    validation = validate_ocr_input_surface(surface)
    findings = list(validation["findings"])

    if not candidate_text_hash_sealed:
        findings.append(_finding("candidate_hash_not_sealed"))
    if not scoring_report_complete:
        findings.append(_finding("partial_artifacts_quarantined"))

    finding_ids = {finding["finding_id"] for finding in findings}
    if "partial_artifacts_quarantined" in finding_ids:
        decision = "blocked_incomplete_artifacts"
    elif findings:
        decision = "blocked_unsafe_surface"
    elif surface["surface_class"] in TEXT_REVIEW_SURFACES:
        decision = "smoke_non_promotable"
    elif not metrics:
        decision = "geometry_probe_required" if surface["surface_class"] == "full_page_region" else "blocked_incomplete_artifacts"
    else:
        similarity = float(metrics["sequence_similarity_ratio"])
        recall = float(metrics["token_recall"])
        flags = set(diagnostic_flags or [])
        geometry_like = bool(flags & {"edge_artifacts", "column_order_drift", "text_near_crop_boundary", "clipped_review_crop"})
        if surface["surface_class"] == "ocr_candidate_crop" and similarity >= OK_SEQUENCE_SIMILARITY and recall >= OK_TOKEN_RECALL:
            decision = "baseline_ok"
        elif recall >= GEOMETRY_DIAGNOSTIC_MIN_TOKEN_RECALL and similarity < OK_SEQUENCE_SIMILARITY and geometry_like:
            decision = "geometry_probe_required"
        elif surface["surface_class"] == "full_page_region" and similarity >= OK_SEQUENCE_SIMILARITY and recall >= OK_TOKEN_RECALL:
            decision = "candidate_policy_ready_for_review"
        else:
            decision = "park_candidate_policy"

    result: dict[str, Any] = {
        "schema_version": OCR_INPUT_SURFACE_POLICY_SCHEMA_VERSION,
        "status": "passed" if decision in {"baseline_ok", "candidate_policy_ready_for_review", "smoke_non_promotable"} else "blocked",
        "route_decision": decision,
        "findings": findings,
        "acceptance_effect": "none",
        "policy_promotion_effect": "none",
        "ocr_execution_effect": "none",
    }
    if metrics:
        result["observed_control_measurement_evaluation"] = evaluate_against_observed_control_measurement(metrics)
    return result
