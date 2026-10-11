from __future__ import annotations

from typing import Any

try:
    from crop_order_validation import CROP_ORDER_VALIDATION_SCHEMA_VERSION, require_passed_crop_order_validation
except ModuleNotFoundError:
    from scripts.crop_order_validation import CROP_ORDER_VALIDATION_SCHEMA_VERSION, require_passed_crop_order_validation


TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION = "sourcefold_text_extraction_contract.v1"
NEGATIVE_CAPABILITY_FLAGS = [
    "ocr_execution_created",
    "ocr_output_created",
    "ocr_acceptance_created",
    "source_acceptance_created",
    "semantic_map_created",
    "pcrp_created",
    "page_complete_acceptance_created",
    "whole_gate_1_acceptance_created",
    "fixture_admission_created",
]


def validate_text_extraction_contract(
    *,
    packet: dict[str, Any],
    expected_predecessor_package_id: str,
    requires_crop_order_validation: bool,
    requires_continuation_notes: bool,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    decision = packet.get("human_review_decision", {})
    if decision.get("accepted_package_id") != expected_predecessor_package_id:
        findings.append(
            {
                "finding_id": "text_extraction_wrong_predecessor",
                "expected": expected_predecessor_package_id,
                "actual": decision.get("accepted_package_id"),
            }
        )
    crop_ids = packet.get("text_map", {}).get("crop_ids")
    if not isinstance(crop_ids, list) or not crop_ids:
        findings.append({"finding_id": "text_extraction_missing_text_evidence_crop_ids"})
    for flag in NEGATIVE_CAPABILITY_FLAGS:
        if packet.get(flag) is not False:
            findings.append({"finding_id": "text_extraction_negative_capability_violation", "flag": flag})
    if requires_continuation_notes and not packet.get("continuation_notes"):
        findings.append({"finding_id": "text_extraction_missing_continuation_notes"})
    if requires_crop_order_validation:
        validation = packet.get("crop_order_validation")
        if not isinstance(validation, dict):
            findings.append({"finding_id": "text_extraction_crop_order_validation_missing_or_blocked", "message": "missing crop_order_validation"})
        elif validation.get("schema_version") != CROP_ORDER_VALIDATION_SCHEMA_VERSION:
            findings.append({"finding_id": "text_extraction_crop_order_validation_missing_or_blocked", "message": "wrong crop_order_validation schema"})
        elif validation.get("status") != "passed":
            findings.append(
                {
                    "finding_id": "text_extraction_crop_order_validation_missing_or_blocked",
                    "message": f"blocked crop_order_validation: {validation.get('findings')}",
                }
            )
    return {
        "schema_version": TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "expected_predecessor_package_id": expected_predecessor_package_id,
        "requires_crop_order_validation": requires_crop_order_validation,
        "requires_continuation_notes": requires_continuation_notes,
        "findings": findings,
    }


def require_valid_text_extraction_contract(
    *,
    packet: dict[str, Any],
    expected_predecessor_package_id: str,
    requires_crop_order_validation: bool,
    requires_continuation_notes: bool,
) -> dict[str, Any]:
    validation = validate_text_extraction_contract(
        packet=packet,
        expected_predecessor_package_id=expected_predecessor_package_id,
        requires_crop_order_validation=requires_crop_order_validation,
        requires_continuation_notes=requires_continuation_notes,
    )
    if validation["status"] != "passed":
        raise ValueError(f"text extraction contract blocked: {validation['findings']}")
    return validation


def require_text_extraction_consumer_gate(packet: dict[str, Any], *, consumer: str) -> dict[str, Any]:
    contract = packet.get("text_extraction_contract_validation")
    if not isinstance(contract, dict):
        raise ValueError(f"{consumer} requires text_extraction_contract_validation before consuming text extraction.")
    if contract.get("schema_version") != TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION:
        raise ValueError(f"{consumer} requires {TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION}.")
    if contract.get("status") != "passed":
        raise ValueError(f"{consumer} blocked by text_extraction_contract_validation: {contract.get('findings')}")
    if "crop_order_validation" in packet:
        require_passed_crop_order_validation(packet, consumer=consumer)
    return {
        "schema_version": TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION,
        "status": "passed",
        "consumer": consumer,
        "text_extraction_contract_status": contract["status"],
        "crop_order_validation_required": "crop_order_validation" in packet,
    }
