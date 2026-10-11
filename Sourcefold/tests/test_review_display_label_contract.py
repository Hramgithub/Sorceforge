import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.review_display_label_contract import (  # noqa: E402
    REVIEW_DISPLAY_LABEL_SCHEMA_VERSION,
    require_review_display_labels,
    validate_review_display_labels,
)


def test_review_display_label_contract_accepts_display_only_body_text_label():
    result = validate_review_display_labels(
        blocks=[
            {
                "block_id": "P004-B001",
                "text_kind": "body_only",
                "display_label": "text_body",
                "semantic_label": "text_body",
                "block_role": "body_block",
            }
        ],
        predecessor_mutated=False,
        normalization_scope="review_asset_only",
    )

    assert result["schema_version"] == REVIEW_DISPLAY_LABEL_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_review_display_label_contract_blocks_hidden_body_text_and_mutation():
    result = validate_review_display_labels(
        blocks=[
            {
                "block_id": "P004-B001",
                "text_kind": "body_only",
                "display_label": "none",
                "semantic_label": "none",
                "block_role": "body_block",
            }
        ],
        predecessor_mutated=True,
        normalization_scope="predecessor_mutation",
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "review_display_body_text_hidden_as_none" in finding_ids
    assert "review_display_body_semantic_hidden_as_none" in finding_ids
    assert "review_display_label_mutates_predecessor" in finding_ids
    assert "review_display_label_wrong_scope" in finding_ids


def test_review_display_label_consumer_fails_closed():
    with pytest.raises(ValueError, match="review display label contract"):
        require_review_display_labels(
            blocks=[{"block_id": "bad", "text_kind": "body_only", "display_label": "", "semantic_label": ""}],
            predecessor_mutated=False,
            normalization_scope="review_asset_only",
            consumer="review_packet",
        )
