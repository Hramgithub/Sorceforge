from __future__ import annotations

from typing import Any


LEGACY_PCRP_REFRESH_SCHEMA_VERSION = "sourcefold_legacy_pcrp_refresh.v1"
REQUIRED_CURRENT_CONTRACTS = {
    "semantic_validation",
    "inventory_reconciliation",
    "artifact_lifecycle",
    "bounded_authorization",
    "human_review_gate",
    "pcrp_preflight",
}


def validate_legacy_pcrp_refresh_contract(
    *,
    legacy_packet: dict[str, Any],
    refresh_packet: dict[str, Any],
    consumer: str,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    legacy_id = legacy_packet.get("package_id")
    refresh_id = refresh_packet.get("package_id")

    if legacy_packet.get("state") not in {"held", "stale", "superseded", "legacy_compatibility_only"}:
        findings.append({"finding_id": "legacy_pcrp_wrong_legacy_state", "package_id": legacy_id, "state": legacy_packet.get("state")})
    if legacy_packet.get("used_directly_for_page_acceptance") is True:
        findings.append({"finding_id": "legacy_pcrp_used_directly_for_acceptance", "package_id": legacy_id})
    if refresh_packet.get("refreshes_package_id") != legacy_id:
        findings.append(
            {
                "finding_id": "legacy_pcrp_missing_refresh_link",
                "legacy_package_id": legacy_id,
                "refreshes_package_id": refresh_packet.get("refreshes_package_id"),
            }
        )
    if refresh_packet.get("state") != "current":
        findings.append({"finding_id": "legacy_pcrp_refresh_not_current", "package_id": refresh_id, "state": refresh_packet.get("state")})

    passed_contracts = set(refresh_packet.get("passed_contracts", []))
    missing_contracts = sorted(REQUIRED_CURRENT_CONTRACTS - passed_contracts)
    if missing_contracts:
        findings.append({"finding_id": "legacy_pcrp_refresh_missing_current_contracts", "contracts": missing_contracts})
    if legacy_packet.get("known_structural_defects") and refresh_packet.get("negative_regression_input_recorded") is not True:
        findings.append({"finding_id": "legacy_pcrp_missing_negative_regression_record", "package_id": legacy_id})

    if consumer == "page_acceptance" and refresh_packet.get("creates_page_acceptance") is True:
        findings.append({"finding_id": "legacy_pcrp_refresh_leaks_page_acceptance", "package_id": refresh_id})

    return {
        "schema_version": LEGACY_PCRP_REFRESH_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "legacy_package_id": legacy_id,
        "refresh_package_id": refresh_id,
        "consumer": consumer,
        "required_current_contracts": sorted(REQUIRED_CURRENT_CONTRACTS),
        "findings": findings,
    }


def require_legacy_pcrp_refresh_contract(
    *,
    legacy_packet: dict[str, Any],
    refresh_packet: dict[str, Any],
    consumer: str,
) -> dict[str, Any]:
    validation = validate_legacy_pcrp_refresh_contract(
        legacy_packet=legacy_packet,
        refresh_packet=refresh_packet,
        consumer=consumer,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by legacy PCRP refresh contract: {validation['findings']}")
    return validation
