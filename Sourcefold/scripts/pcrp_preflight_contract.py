from __future__ import annotations

from typing import Any


PCRP_PREFLIGHT_SCHEMA_VERSION = "sourcefold_pcrp_preflight.v1"
PCRP_BLOCKED_OUTPUT_FLAGS = [
    "page_complete_acceptance_created",
    "whole_gate_1_acceptance_created",
    "fixture_admission_created",
    "source_acceptance_created",
    "ocr_acceptance_created",
]


def validate_pcrp_preflight(
    *,
    page: str,
    required_contracts: dict[str, dict[str, Any] | None],
    output_capabilities: dict[str, bool],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for contract_name, contract in required_contracts.items():
        if not isinstance(contract, dict):
            findings.append({"finding_id": "pcrp_preflight_missing_contract", "contract": contract_name})
            continue
        if contract.get("status") != "passed":
            findings.append(
                {
                    "finding_id": "pcrp_preflight_blocked_contract",
                    "contract": contract_name,
                    "status": contract.get("status"),
                    "findings": contract.get("findings"),
                }
            )
    leaked = [flag for flag in PCRP_BLOCKED_OUTPUT_FLAGS if output_capabilities.get(flag) is True]
    if leaked:
        findings.append({"finding_id": "pcrp_preflight_acceptance_leakage", "flags": leaked})
    return {
        "schema_version": PCRP_PREFLIGHT_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "page": page,
        "required_contracts": sorted(required_contracts),
        "output_capabilities": output_capabilities,
        "findings": findings,
    }
