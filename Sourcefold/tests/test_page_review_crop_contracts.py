from __future__ import annotations

from pathlib import Path

import pytest

from Sourcefold.scripts.page_review_crop_contracts import (
    assert_aggressive_page_builder_uses_crop_contracts,
    discover_aggressive_page_builders,
    validate_text_evidence_crop_contracts,
)


def test_text_evidence_crop_contract_accepts_bound_full_text_region():
    validate_text_evidence_crop_contracts(
        (1000, 1000),
        [
            {
                "block_id": "B001",
                "crop_box_px": [100, 100, 400, 300],
                "asset": "review_assets/b001.png",
                "crop_contract": {
                    "coverage": "full_text_region",
                    "context_allowed": False,
                    "expected_bounds": {"min_x": 90, "max_x": 110, "min_width": 390, "min_height": 290},
                },
            }
        ],
    )


def test_text_evidence_crop_contract_rejects_missing_contract():
    with pytest.raises(ValueError, match="crop_contract"):
        validate_text_evidence_crop_contracts(
            (1000, 1000),
            [{"block_id": "B001", "crop_box_px": [100, 100, 400, 300], "asset": "review_assets/b001.png"}],
        )


def test_text_evidence_crop_contract_rejects_undercoverage():
    with pytest.raises(ValueError, match="width is too small"):
        validate_text_evidence_crop_contracts(
            (1000, 1000),
            [
                {
                    "block_id": "B001",
                    "crop_box_px": [100, 100, 200, 300],
                    "asset": "review_assets/b001.png",
                    "crop_contract": {
                        "coverage": "full_text_region",
                        "context_allowed": False,
                        "expected_bounds": {"min_width": 390, "min_height": 290},
                    },
                }
            ],
        )


def test_text_evidence_crop_contract_rejects_implicit_context():
    with pytest.raises(ValueError, match="implicit context"):
        validate_text_evidence_crop_contracts(
            (1000, 1000),
            [
                {
                    "block_id": "B001",
                    "crop_box_px": [100, 100, 400, 300],
                    "asset": "review_assets/b001.png",
                    "crop_contract": {
                        "coverage": "full_text_region",
                        "context_allowed": True,
                        "expected_bounds": {"min_width": 390, "min_height": 290},
                    },
                }
            ],
        )


def test_aggressive_page_builders_require_shared_crop_contract_validator():
    scripts_root = Path(__file__).resolve().parents[1] / "scripts"
    builders = discover_aggressive_page_builders(scripts_root)

    assert builders, "expected at least one aggressive page builder"
    for builder in builders:
        assert_aggressive_page_builder_uses_crop_contracts(builder)


def test_aggressive_page_builder_contract_scanner_rejects_legacy_builder(tmp_path):
    legacy_builder = tmp_path / "build_page_013_aggressive_batch.py"
    legacy_builder.write_text(
        """
BLOCKS = [
    {
        "block_id": "P013-B001",
        "role": "text_evidence",
        "crop_box_px": [100, 100, 400, 300],
        "asset": "review_assets/p013-b001.png",
    }
]
""".lstrip(),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="crop contract|crop_contract|validator"):
        assert_aggressive_page_builder_uses_crop_contracts(legacy_builder)


def test_aggressive_page_builder_contract_scanner_accepts_shared_contract(tmp_path):
    builder = tmp_path / "build_page_013_aggressive_batch.py"
    builder.write_text(
        """
from page_review_crop_contracts import validate_text_evidence_crop_contracts


BLOCKS = [
    {
        "block_id": "P013-B001",
        "role": "text_evidence",
        "crop_box_px": [100, 100, 400, 300],
        "asset": "review_assets/p013-b001.png",
        "crop_contract": {
            "coverage": "full_text_region",
            "context_allowed": False,
            "expected_bounds": {"min_width": 390, "min_height": 290},
        },
    }
]


def build(image):
    validate_text_evidence_crop_contracts(image.size, BLOCKS)
""".lstrip(),
        encoding="utf-8",
    )

    assert_aggressive_page_builder_uses_crop_contracts(builder)
