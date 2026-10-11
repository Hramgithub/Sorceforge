import pytest

from scripts.source_reconstruction_crop_guardrails import validate_crop_layout


def test_crop_guardrail_accepts_padded_non_overlapping_boxes():
    report = validate_crop_layout(
        [
            {"source_region_id": "r1", "box_px": [100, 100, 500, 400]},
            {"source_region_id": "r2", "box_px": [100, 540, 500, 400]},
        ],
        image_size=(1000, 1200),
        min_gutter_px=24,
        validated_at_stage="unit",
    )

    assert report["guardrail_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert report["status"] == "passed"


def test_crop_guardrail_rejects_overlapping_boxes():
    with pytest.raises(ValueError, match="overlaps"):
        validate_crop_layout(
            [
                {"source_region_id": "r1", "box_px": [100, 100, 500, 400]},
                {"source_region_id": "r2", "box_px": [100, 450, 500, 400]},
            ],
            image_size=(1000, 1200),
            validated_at_stage="unit",
        )


def test_crop_guardrail_rejects_too_small_gutter():
    with pytest.raises(ValueError, match="too close"):
        validate_crop_layout(
            [
                {"source_region_id": "r1", "box_px": [100, 100, 500, 400]},
                {"source_region_id": "r2", "box_px": [100, 515, 500, 400]},
            ],
            image_size=(1000, 1200),
            min_gutter_px=24,
            validated_at_stage="unit",
        )


def test_crop_guardrail_rejects_blocked_tight_boxes():
    with pytest.raises(ValueError, match="blocked tight"):
        validate_crop_layout(
            [{"source_region_id": "r1", "box_px": [460, 860, 1650, 2050]}],
            image_size=(2550, 3300),
            blocked_boxes=([460, 860, 1650, 2050],),
            validated_at_stage="unit",
        )


def test_crop_guardrail_rejects_non_integer_coordinates():
    with pytest.raises(ValueError, match="integers"):
        validate_crop_layout(
            [{"source_region_id": "r1", "box_px": [100, 100.5, 500, 400]}],
            image_size=(1000, 1200),
            validated_at_stage="unit",
        )


def test_crop_guardrail_rejects_out_of_bounds_boxes():
    with pytest.raises(ValueError, match="exceeds page bounds"):
        validate_crop_layout(
            [{"source_region_id": "r1", "box_px": [100, 100, 1000, 400]}],
            image_size=(1000, 1200),
            validated_at_stage="unit",
        )


def test_crop_guardrail_rejects_unapproved_non_exact_boxes():
    with pytest.raises(ValueError, match="not the approved"):
        validate_crop_layout(
            [{"source_region_id": "r1", "box_px": [101, 100, 500, 400]}],
            image_size=(1000, 1200),
            approved_boxes_by_region={"r1": [100, 100, 500, 400]},
            validated_at_stage="unit",
        )


def test_crop_guardrail_rejects_diagonal_near_collisions():
    with pytest.raises(ValueError, match="too close"):
        validate_crop_layout(
            [
                {"source_region_id": "r1", "box_px": [100, 100, 500, 400]},
                {"source_region_id": "r2", "box_px": [610, 510, 300, 300]},
            ],
            image_size=(1000, 1200),
            min_gutter_px=24,
            validated_at_stage="unit",
        )
