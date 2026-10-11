from __future__ import annotations

from typing import Any


REVIEW_DISPLAY_LABEL_SCHEMA_VERSION = "sourcefold_review_display_label.v1"


def validate_review_display_labels(
    *,
    blocks: list[dict[str, Any]],
    predecessor_mutated: bool,
    normalization_scope: str,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    if predecessor_mutated:
        findings.append({"finding_id": "review_display_label_mutates_predecessor"})
    if normalization_scope != "review_asset_only":
        findings.append({"finding_id": "review_display_label_wrong_scope", "scope": normalization_scope})

    for block in blocks:
        block_id = block.get("block_id", "<missing>")
        text_kind = block.get("text_kind")
        display_label = block.get("display_label")
        semantic_label = block.get("semantic_label")
        if text_kind == "body_only" and display_label in {None, "", "none"}:
            findings.append({"finding_id": "review_display_body_text_hidden_as_none", "block_id": block_id})
        if text_kind == "body_only" and semantic_label in {None, "", "none"}:
            findings.append({"finding_id": "review_display_body_semantic_hidden_as_none", "block_id": block_id})
        if display_label == block.get("block_role"):
            findings.append({"finding_id": "review_display_label_leaks_block_role", "block_id": block_id})

    return {
        "schema_version": REVIEW_DISPLAY_LABEL_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "normalization_scope": normalization_scope,
        "predecessor_mutated": predecessor_mutated,
        "block_count": len(blocks),
        "findings": findings,
    }


def require_review_display_labels(
    *,
    blocks: list[dict[str, Any]],
    predecessor_mutated: bool,
    normalization_scope: str,
    consumer: str,
) -> dict[str, Any]:
    validation = validate_review_display_labels(
        blocks=blocks,
        predecessor_mutated=predecessor_mutated,
        normalization_scope=normalization_scope,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by review display label contract: {validation['findings']}")
    return validation
