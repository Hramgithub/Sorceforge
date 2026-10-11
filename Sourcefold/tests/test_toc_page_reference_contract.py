import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.toc_page_reference_contract import (  # noqa: E402
    TOC_PAGE_REFERENCE_SCHEMA_VERSION,
    require_toc_page_reference_contract,
    validate_toc_page_reference_contract,
)


def rows():
    return [
        {
            "row_id": "TOC-R001",
            "entry_text": "Introduction",
            "page_ref": "6",
            "page_ref_region_id": "PRM-G1-VIRAL-001-P005-R02",
            "unit_type": "list_item",
            "page_ref_unit_type": "page_ref",
        },
        {
            "row_id": "TOC-R002",
            "entry_text": "Summary",
            "page_ref": "6",
            "page_ref_region_id": "PRM-G1-VIRAL-001-P005-R02",
            "unit_type": "list_item",
            "page_ref_unit_type": "page_ref",
        },
    ]


def test_toc_page_reference_contract_accepts_rows_and_page_refs():
    result = validate_toc_page_reference_contract(
        rows=rows(),
        page_marker_regions=["PRM-G1-VIRAL-001-P005-R03"],
        projection={"row_count": 2, "row_ids": ["TOC-R001", "TOC-R002"], "page_ref_count": 2},
    )

    assert result["schema_version"] == TOC_PAGE_REFERENCE_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_toc_page_reference_contract_blocks_missing_refs_and_marker_confusion():
    bad_rows = rows()
    bad_rows[0]["page_ref"] = ""
    bad_rows[1]["page_ref_region_id"] = "PRM-G1-VIRAL-001-P005-R03"
    result = validate_toc_page_reference_contract(
        rows=bad_rows,
        page_marker_regions=["PRM-G1-VIRAL-001-P005-R03"],
        projection={"row_count": 1, "row_ids": ["TOC-R001"], "page_ref_count": 1},
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "toc_row_missing_page_ref" in finding_ids
    assert "toc_page_ref_uses_margin_page_marker" in finding_ids
    assert "toc_projection_row_count_mismatch" in finding_ids
    assert "toc_projection_page_ref_count_mismatch" in finding_ids


def test_toc_page_reference_consumer_fails_closed():
    with pytest.raises(ValueError, match="TOC page-reference contract"):
        require_toc_page_reference_contract(
            rows=[],
            page_marker_regions=[],
            projection={"row_count": 1, "row_ids": ["missing"], "page_ref_count": 1},
            consumer="semantic_projection",
        )
