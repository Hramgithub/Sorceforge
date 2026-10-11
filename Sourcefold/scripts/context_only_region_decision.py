from __future__ import annotations

from typing import Any


CONTEXT_ONLY_REGION_DECISION_SCHEMA_VERSION = "sourcefold_context_only_region_decision.v1"
FORBIDDEN_CAPABILITIES = {
    "page_complete_acceptance_created": False,
    "source_acceptance_created": False,
    "ocr_acceptance_created": False,
    "fixture_admission_created": False,
    "whole_gate_acceptance_created": False,
    "predecessor_mutated": False,
}


def validate_context_only_region_decision(
    *,
    decision: dict[str, Any],
    known_region_ids: set[str],
    forbidden_capabilities: dict[str, Any],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    region_id = decision.get("context_region_id")
    if not region_id:
        findings.append({"finding_id": "context_only_missing_region_id"})
    elif region_id not in known_region_ids:
        findings.append({"finding_id": "context_only_unknown_region_id", "region_id": region_id})

    if decision.get("confirmed_status") not in {"context_only", "context_only_not_peer_crop_record"}:
        findings.append({"finding_id": "context_only_wrong_status", "status": decision.get("confirmed_status")})
    if decision.get("reviewer") != "Bogdan":
        findings.append({"finding_id": "context_only_missing_bogdan_decision", "reviewer": decision.get("reviewer")})
    if not decision.get("human_decision_ref"):
        findings.append({"finding_id": "context_only_missing_human_decision_ref"})
    if not decision.get("overlap_rationale"):
        findings.append({"finding_id": "context_only_missing_overlap_rationale"})

    peer_region_ids = decision.get("peer_region_ids")
    if not isinstance(peer_region_ids, list) or not peer_region_ids:
        findings.append({"finding_id": "context_only_missing_peer_regions"})
    else:
        unknown_peers = sorted(set(peer_region_ids) - known_region_ids)
        if unknown_peers:
            findings.append({"finding_id": "context_only_unknown_peer_region", "region_ids": unknown_peers})
        if region_id in peer_region_ids:
            findings.append({"finding_id": "context_only_region_lists_itself_as_peer", "region_id": region_id})

    downstream_limits = decision.get("downstream_limits")
    if not isinstance(downstream_limits, list) or "not_page_complete_acceptance" not in downstream_limits:
        findings.append({"finding_id": "context_only_missing_downstream_limits"})

    leaked = {key: forbidden_capabilities.get(key) for key, expected in FORBIDDEN_CAPABILITIES.items() if forbidden_capabilities.get(key) is not expected}
    if leaked:
        findings.append({"finding_id": "context_only_authority_leakage", "flags": leaked})

    return {
        "schema_version": CONTEXT_ONLY_REGION_DECISION_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "context_region_id": region_id,
        "peer_region_ids": peer_region_ids if isinstance(peer_region_ids, list) else [],
        "forbidden_capability_requirements": FORBIDDEN_CAPABILITIES,
        "findings": findings,
    }


def require_context_only_region_decision(
    *,
    decision: dict[str, Any],
    known_region_ids: set[str],
    forbidden_capabilities: dict[str, Any],
    consumer: str,
) -> dict[str, Any]:
    validation = validate_context_only_region_decision(
        decision=decision,
        known_region_ids=known_region_ids,
        forbidden_capabilities=forbidden_capabilities,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by context-only region decision: {validation['findings']}")
    return validation
