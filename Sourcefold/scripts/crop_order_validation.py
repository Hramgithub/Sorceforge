from __future__ import annotations

from typing import Any


CROP_ORDER_VALIDATION_SCHEMA_VERSION = "sourcefold_crop_order_validation.v1"


def validate_crop_order(
    *,
    units: list[dict[str, Any]],
    expected_logical_order: list[str],
    physical_crop_asset_order: list[str],
    continuation_edges: list[dict[str, str]],
    required_before: list[str] | None = None,
) -> dict[str, Any]:
    ordered_units = sorted(units, key=lambda unit: unit["reading_order_index"])
    actual_order = [unit["crop_id"] for unit in ordered_units]
    findings: list[dict[str, Any]] = []
    if actual_order != expected_logical_order:
        findings.append(
            {
                "finding_id": "logical_reading_order_mismatch",
                "expected": expected_logical_order,
                "actual": actual_order,
            }
        )
    if actual_order == physical_crop_asset_order and expected_logical_order != physical_crop_asset_order:
        findings.append(
            {
                "finding_id": "logical_order_collapsed_to_asset_order",
                "asset_order": physical_crop_asset_order,
            }
        )

    by_crop_id = {unit["crop_id"]: unit for unit in units}
    for edge in continuation_edges:
        source = by_crop_id.get(edge["from"])
        target = by_crop_id.get(edge["to"])
        if source is None or target is None:
            findings.append({"finding_id": "missing_continuation_endpoint", **edge})
            continue
        if source.get("continues_to_crop_id") != edge["to"] or target.get("continues_from_crop_id") != edge["from"]:
            findings.append({"finding_id": "continuation_link_mismatch", **edge})

    return {
        "schema_version": CROP_ORDER_VALIDATION_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "findings": findings,
        "logical_reading_order": actual_order,
        "expected_logical_reading_order": expected_logical_order,
        "physical_crop_asset_order": physical_crop_asset_order,
        "logical_order_is_not_asset_order": actual_order != physical_crop_asset_order,
        "continuation_edges": continuation_edges,
        "required_before": required_before or ["semantic_map", "pcrp"],
    }


def require_passed_crop_order_validation(packet: dict[str, Any], *, consumer: str) -> dict[str, Any]:
    validation = packet.get("crop_order_validation")
    if not isinstance(validation, dict):
        raise ValueError(f"{consumer} requires crop_order_validation before consuming text extraction.")
    if validation.get("schema_version") != CROP_ORDER_VALIDATION_SCHEMA_VERSION:
        raise ValueError(f"{consumer} requires {CROP_ORDER_VALIDATION_SCHEMA_VERSION}.")
    if validation.get("status") != "passed":
        raise ValueError(f"{consumer} blocked by crop_order_validation findings: {validation.get('findings')}")
    required_before = validation.get("required_before")
    if not isinstance(required_before, list) or consumer not in required_before:
        raise ValueError(f"{consumer} is not covered by crop_order_validation.required_before.")
    return validation
