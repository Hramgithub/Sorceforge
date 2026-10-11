from __future__ import annotations

from typing import Any


VISUAL_TITLE_PAGE_CONTRACT_SCHEMA_VERSION = "sourcefold_visual_title_page_contract.v1"
REQUIRED_NEGATIVE_CAPABILITIES = {
    "ocr_executed": False,
    "text_extraction_created": False,
    "source_acceptance_created": False,
    "fixture_admission_created": False,
    "whole_gate_acceptance_created": False,
    "raw_artifacts_modified": False,
}


def validate_visual_title_page_contract(
    *,
    profile: dict[str, Any],
    anchors: list[dict[str, Any]],
    negative_capabilities: dict[str, Any],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    page_type = profile.get("page_type")
    if page_type != "visual_title":
        findings.append({"finding_id": "visual_title_wrong_page_type", "page_type": page_type})
    if profile.get("requires_text_extraction") is not False:
        findings.append({"finding_id": "visual_title_text_extraction_not_explicitly_disabled"})
    if profile.get("allows_page_complete_without_text_map") is not True:
        findings.append({"finding_id": "visual_title_missing_without_text_map_authority"})

    required_anchor_ids = profile.get("required_anchor_ids")
    if not isinstance(required_anchor_ids, list) or not required_anchor_ids:
        findings.append({"finding_id": "visual_title_missing_required_anchor_ids"})
        required_anchor_ids = []

    anchor_by_id = {anchor.get("anchor_id"): anchor for anchor in anchors}
    missing_anchors = sorted(set(required_anchor_ids) - set(anchor_by_id))
    if missing_anchors:
        findings.append({"finding_id": "visual_title_missing_required_anchors", "anchor_ids": missing_anchors})

    for anchor_id in required_anchor_ids:
        anchor = anchor_by_id.get(anchor_id)
        if not anchor:
            continue
        if anchor.get("review_state") != "ready_for_review":
            findings.append({"finding_id": "visual_title_anchor_not_ready", "anchor_id": anchor_id})
        if anchor.get("not_source_text") is not True:
            findings.append({"finding_id": "visual_title_anchor_leaks_source_text", "anchor_id": anchor_id})
        if not anchor.get("evidence_ref"):
            findings.append({"finding_id": "visual_title_anchor_missing_evidence_ref", "anchor_id": anchor_id})

    leaked = {
        key: actual
        for key, expected in REQUIRED_NEGATIVE_CAPABILITIES.items()
        if (actual := negative_capabilities.get(key)) is not expected
    }
    if leaked:
        findings.append({"finding_id": "visual_title_negative_capability_leakage", "flags": leaked})

    return {
        "schema_version": VISUAL_TITLE_PAGE_CONTRACT_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "page_type": page_type,
        "anchor_count": len(anchors),
        "required_anchor_ids": required_anchor_ids,
        "negative_capability_requirements": REQUIRED_NEGATIVE_CAPABILITIES,
        "findings": findings,
    }


def require_visual_title_page_contract(
    *,
    profile: dict[str, Any],
    anchors: list[dict[str, Any]],
    negative_capabilities: dict[str, Any],
    consumer: str,
) -> dict[str, Any]:
    validation = validate_visual_title_page_contract(
        profile=profile,
        anchors=anchors,
        negative_capabilities=negative_capabilities,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by visual title page contract: {validation['findings']}")
    return validation
