from __future__ import annotations

from typing import Any


HUMAN_REVIEW_GATE_SCHEMA_VERSION = "sourcefold_human_review_gate.v1"


def validate_human_review_gate(
    *,
    sol_review: dict[str, Any],
    terra_review: dict[str, Any],
    human_decision: dict[str, Any],
    expected_package_id: str,
    allowed_decisions: list[str],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    if sol_review.get("status") != "OK":
        findings.append({"finding_id": "human_review_gate_sol_not_ok", "status": sol_review.get("status")})
    if terra_review.get("status") != "OK":
        findings.append({"finding_id": "human_review_gate_terra_not_ok", "status": terra_review.get("status")})
    if human_decision.get("package_id") != expected_package_id:
        findings.append(
            {
                "finding_id": "human_review_gate_wrong_package",
                "expected": expected_package_id,
                "actual": human_decision.get("package_id"),
            }
        )
    decision = human_decision.get("decision")
    if decision not in allowed_decisions:
        findings.append({"finding_id": "human_review_gate_decision_not_allowed", "decision": decision, "allowed": allowed_decisions})
    if not human_decision.get("source_message_id"):
        findings.append({"finding_id": "human_review_gate_missing_source_message"})
    if human_decision.get("creates_page_complete_acceptance") is True:
        findings.append({"finding_id": "human_review_gate_leaks_page_acceptance"})
    return {
        "schema_version": HUMAN_REVIEW_GATE_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "expected_package_id": expected_package_id,
        "allowed_decisions": allowed_decisions,
        "findings": findings,
    }
