from __future__ import annotations

from typing import Any


DEFERRED_REVIEW_CONTRACT_SCHEMA_VERSION = "sourcefold_deferred_review_contract.v1"


def validate_deferred_review_contract(
    *,
    attachments: list[dict[str, Any]],
    action_backlog: dict[str, Any] | None,
    creates_page_acceptance: bool,
    creates_whole_gate_acceptance: bool,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    deferred_anchor_ids: list[str] = []
    for attachment in attachments:
        is_visual_anchor = attachment.get("include_in_text_map") is False or attachment.get("skip_edge_ink_check") is True
        if not is_visual_anchor:
            continue
        deferred_anchor_ids.append(attachment.get("attachment_id", "<missing>"))
        if attachment.get("role") != "human_review_crop":
            findings.append({"finding_id": "deferred_anchor_wrong_attachment_role", "attachment_id": attachment.get("attachment_id")})
        if attachment.get("include_in_text_map") is not False:
            findings.append({"finding_id": "deferred_anchor_leaks_into_text_map", "attachment_id": attachment.get("attachment_id")})
        if not attachment.get("covered_review_blocks"):
            findings.append({"finding_id": "deferred_anchor_missing_review_block_link", "attachment_id": attachment.get("attachment_id")})
    if action_backlog is not None:
        if action_backlog.get("role") != "action_backlog_markdown":
            findings.append({"finding_id": "action_backlog_wrong_role", "attachment_id": action_backlog.get("attachment_id")})
        if not action_backlog.get("steps"):
            findings.append({"finding_id": "action_backlog_missing_steps", "attachment_id": action_backlog.get("attachment_id")})
    if creates_page_acceptance:
        findings.append({"finding_id": "deferred_review_creates_page_acceptance"})
    if creates_whole_gate_acceptance:
        findings.append({"finding_id": "deferred_review_creates_whole_gate_acceptance"})
    return {
        "schema_version": DEFERRED_REVIEW_CONTRACT_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "deferred_anchor_ids": deferred_anchor_ids,
        "action_backlog_present": action_backlog is not None,
        "creates_page_acceptance": creates_page_acceptance,
        "creates_whole_gate_acceptance": creates_whole_gate_acceptance,
        "findings": findings,
    }
