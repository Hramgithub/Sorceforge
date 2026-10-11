import pytest
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.crop_order_validation import (
    CROP_ORDER_VALIDATION_SCHEMA_VERSION,
    require_passed_crop_order_validation,
    validate_crop_order,
)


def unit(crop_id: str, order: int, **extra):
    payload = {"crop_id": crop_id, "reading_order_index": order}
    payload.update(extra)
    return payload


def test_crop_order_validation_accepts_continuation_aware_order():
    result = validate_crop_order(
        units=[
            unit("B001", 1),
            unit("B005", 2, continues_to_crop_id="B002"),
            unit("B002", 3, continues_from_crop_id="B005"),
            unit("B006", 4),
        ],
        expected_logical_order=["B001", "B005", "B002", "B006"],
        physical_crop_asset_order=["B001", "B002", "B005", "B006"],
        continuation_edges=[{"from": "B005", "to": "B002", "reason": "column continuation"}],
    )

    assert result["schema_version"] == CROP_ORDER_VALIDATION_SCHEMA_VERSION
    assert result["status"] == "passed"
    assert result["findings"] == []
    assert result["logical_order_is_not_asset_order"] is True
    assert result["required_before"] == ["semantic_map", "pcrp"]


def test_crop_order_validation_blocks_asset_order_collapse():
    result = validate_crop_order(
        units=[
            unit("B001", 1),
            unit("B002", 2, continues_from_crop_id="B005"),
            unit("B005", 3, continues_to_crop_id="B002"),
            unit("B006", 4),
        ],
        expected_logical_order=["B001", "B005", "B002", "B006"],
        physical_crop_asset_order=["B001", "B002", "B005", "B006"],
        continuation_edges=[{"from": "B005", "to": "B002", "reason": "column continuation"}],
    )

    assert result["status"] == "blocked"
    assert {finding["finding_id"] for finding in result["findings"]} == {
        "logical_reading_order_mismatch",
        "logical_order_collapsed_to_asset_order",
    }


def test_crop_order_validation_blocks_missing_continuation_link():
    result = validate_crop_order(
        units=[
            unit("B001", 1),
            unit("B005", 2),
            unit("B002", 3),
            unit("B006", 4),
        ],
        expected_logical_order=["B001", "B005", "B002", "B006"],
        physical_crop_asset_order=["B001", "B002", "B005", "B006"],
        continuation_edges=[{"from": "B005", "to": "B002", "reason": "column continuation"}],
    )

    assert result["status"] == "blocked"
    assert any(finding["finding_id"] == "continuation_link_mismatch" for finding in result["findings"])


def test_semantic_or_pcrp_consumers_require_passed_crop_order_validation():
    packet = {
        "crop_order_validation": validate_crop_order(
            units=[unit("B001", 1)],
            expected_logical_order=["B001"],
            physical_crop_asset_order=["B001"],
            continuation_edges=[],
        )
    }

    assert require_passed_crop_order_validation(packet, consumer="semantic_map")["status"] == "passed"
    with pytest.raises(ValueError, match="requires crop_order_validation"):
        require_passed_crop_order_validation({}, consumer="semantic_map")
    with pytest.raises(ValueError, match="not covered"):
        require_passed_crop_order_validation(packet, consumer="page_acceptance")
