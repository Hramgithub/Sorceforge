from __future__ import annotations

from pathlib import Path
from typing import Any


REQUIRED_COVERAGE = {"full_text_box", "full_text_region", "full_text_region_part"}
AGGRESSIVE_PAGE_BUILDER_PATTERN = "build_page_*_aggressive_batch.py"


def validate_text_evidence_crop_contracts(page_size: tuple[int, int], blocks: list[dict[str, Any]]) -> None:
    page_width, page_height = page_size
    for block in blocks:
        block_id = block.get("block_id", "<unknown>")
        crop_box = block.get("crop_box_px")
        if not isinstance(crop_box, list) or len(crop_box) != 4:
            raise ValueError(f"{block_id} must define crop_box_px as [x, y, width, height]")
        x, y, width, height = crop_box
        if any(not isinstance(value, int) for value in crop_box):
            raise ValueError(f"{block_id} crop_box_px must contain integers")
        if min(x, y, width, height) < 0 or width == 0 or height == 0:
            raise ValueError(f"{block_id} has invalid crop dimensions: {crop_box}")
        if x + width > page_width or y + height > page_height:
            raise ValueError(f"{block_id} crop exceeds page bounds: {crop_box}")

        contract = block.get("crop_contract")
        if not isinstance(contract, dict):
            raise ValueError(f"{block_id} must define crop_contract")
        if contract.get("coverage") not in REQUIRED_COVERAGE:
            raise ValueError(f"{block_id} must declare full text coverage")
        if contract.get("context_allowed", False):
            raise ValueError(f"{block_id} text evidence crop may not allow implicit context text")

        expected = contract.get("expected_bounds", {})
        if not isinstance(expected, dict):
            raise ValueError(f"{block_id} expected_bounds must be an object when present")
        if x < expected.get("min_x", 0):
            raise ValueError(f"{block_id} crop starts before allowed min_x")
        if y < expected.get("min_y", 0):
            raise ValueError(f"{block_id} crop starts before allowed min_y")
        if x > expected.get("max_x", page_width):
            raise ValueError(f"{block_id} crop starts after allowed max_x")
        if y > expected.get("max_y", page_height):
            raise ValueError(f"{block_id} crop starts after allowed max_y")
        if width < expected.get("min_width", 1):
            raise ValueError(f"{block_id} crop width is too small for its text region")
        if height < expected.get("min_height", 1):
            raise ValueError(f"{block_id} crop height is too small for its text region")

        if block.get("asset") is None:
            raise ValueError(f"{block_id} must define a review asset")


def discover_aggressive_page_builders(scripts_root: Path) -> list[Path]:
    return sorted(scripts_root.glob(AGGRESSIVE_PAGE_BUILDER_PATTERN))


def assert_aggressive_page_builder_uses_crop_contracts(script_path: Path) -> None:
    source = script_path.read_text(encoding="utf-8")
    script_name = script_path.name

    if "page_review_crop_contracts" not in source:
        raise ValueError(f"{script_name} must import the shared crop contract validator")
    if "validate_text_evidence_crop_contracts(" not in source:
        raise ValueError(f"{script_name} must call validate_text_evidence_crop_contracts")
    if "crop_contract" not in source:
        raise ValueError(f"{script_name} must define crop_contract for text evidence blocks")
    if "context_allowed" not in source:
        raise ValueError(f"{script_name} must define context_allowed for text evidence blocks")
    if '"context_allowed": True' in source or "'context_allowed': True" in source:
        raise ValueError(f"{script_name} must not allow implicit context text in text evidence crops")
