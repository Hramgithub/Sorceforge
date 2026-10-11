from __future__ import annotations

from typing import Any


ROUTE_CURSOR_TRANSITION_SCHEMA_VERSION = "sourcefold_route_cursor_transition.v1"
BLOCKED_AUTHORITY_FLAGS = [
    "page_complete_acceptance_created",
    "whole_gate_1_acceptance_created",
    "fixture_admission_created",
    "source_acceptance_created",
    "pcrp_created",
]


def validate_route_cursor_transition(
    *,
    from_cursor: str,
    to_cursor: str,
    allowed_transitions: dict[str, list[str]],
    created_capabilities: dict[str, bool],
    required_next: str | None = None,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    allowed_next = allowed_transitions.get(from_cursor, [])
    if to_cursor not in allowed_next:
        findings.append(
            {
                "finding_id": "route_cursor_transition_not_allowed",
                "from_cursor": from_cursor,
                "to_cursor": to_cursor,
                "allowed_next": allowed_next,
            }
        )
    if required_next and to_cursor != required_next:
        findings.append(
            {
                "finding_id": "route_cursor_required_next_mismatch",
                "required_next": required_next,
                "actual_next": to_cursor,
            }
        )
    leaked = [flag for flag in BLOCKED_AUTHORITY_FLAGS if created_capabilities.get(flag) is True]
    if leaked:
        findings.append({"finding_id": "route_cursor_transition_created_unauthorized_capability", "flags": leaked})
    return {
        "schema_version": ROUTE_CURSOR_TRANSITION_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "from_cursor": from_cursor,
        "to_cursor": to_cursor,
        "required_next": required_next,
        "created_capabilities": created_capabilities,
        "findings": findings,
    }
