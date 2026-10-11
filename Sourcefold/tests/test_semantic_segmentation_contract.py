import pytest

from scripts.semantic_segmentation_contract import (
    SemanticSegmentationError,
    callout_body_contract,
    split_bounded_callout,
    validate_semantic_split_contracts,
)


def test_bounded_callout_requires_declared_boundary():
    with pytest.raises(SemanticSegmentationError, match="boundary is not declared"):
        split_bounded_callout("Before\n\nKeeper's Notes\n\nBody\n\nAfter", callout_heading="Keeper's Notes")


def test_bounded_callout_splits_by_explicit_body_end_marker():
    result = split_bounded_callout(
        "Before\n\nKeeper's Notes\n\nKeeper body.\n\nAfter body.",
        callout_heading="Keeper's Notes",
        body_end_marker="Keeper body.",
    )

    assert result.before == "Before"
    assert result.body == "Keeper body."
    assert result.after == "After body."
    assert result.contract()["boundary_kind"] == "explicit_body_end_marker"


def test_bounded_callout_splits_by_next_segment_start_marker():
    result = split_bounded_callout(
        "Before\n\nKeeper's Notes\n\nKeeper body.\n\nNext Section. Body.",
        callout_heading="Keeper's Notes",
        next_segment_start_marker="Next Section.",
    )

    assert result.body == "Keeper body."
    assert result.after == "Next Section. Body."
    assert result.contract()["boundary_kind"] == "next_segment_start_marker"


def test_semantic_split_validation_requires_contract_for_keeper_body():
    result = validate_semantic_split_contracts(
        [{"unit_id": "SU-P999-KEEPER-002", "unit_type": "paragraph", "display_style": "body", "text": "Keeper body"}]
    )

    assert result["readiness_blocked"] is True
    assert result["findings"][0]["finding_id"] == "missing_semantic_split_contract"


def test_semantic_split_validation_accepts_registered_contract():
    result = validate_semantic_split_contracts(
        [
            {
                "unit_id": "SU-P999-KEEPER-002",
                "unit_type": "paragraph",
                "display_style": "body",
                "text": "Keeper body",
                "semantic_split_contract": callout_body_contract(callout_heading="Keeper's Notes"),
            }
        ]
    )

    assert result["valid"] is True
    assert result["findings"] == []
