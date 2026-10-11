from __future__ import annotations

from typing import Any


TOC_PAGE_REFERENCE_SCHEMA_VERSION = "sourcefold_toc_page_reference.v1"


def validate_toc_page_reference_contract(
    *,
    rows: list[dict[str, Any]],
    page_marker_regions: list[str],
    projection: dict[str, Any],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    row_ids: set[str] = set()
    for index, row in enumerate(rows):
        row_id = row.get("row_id")
        if not row_id:
            findings.append({"finding_id": "toc_row_missing_id", "index": index})
            continue
        if row_id in row_ids:
            findings.append({"finding_id": "toc_duplicate_row_id", "row_id": row_id})
        row_ids.add(row_id)
        if not row.get("entry_text"):
            findings.append({"finding_id": "toc_row_missing_entry_text", "row_id": row_id})
        page_ref = row.get("page_ref")
        if page_ref in {None, ""}:
            findings.append({"finding_id": "toc_row_missing_page_ref", "row_id": row_id})
        if row.get("page_ref_region_id") in page_marker_regions:
            findings.append({"finding_id": "toc_page_ref_uses_margin_page_marker", "row_id": row_id})
        if row.get("unit_type") not in {"table_row", "list_item"}:
            findings.append({"finding_id": "toc_row_wrong_unit_type", "row_id": row_id, "unit_type": row.get("unit_type")})
        if row.get("page_ref_unit_type") != "page_ref":
            findings.append({"finding_id": "toc_page_ref_wrong_unit_type", "row_id": row_id})

    if projection.get("row_count") != len(rows):
        findings.append({"finding_id": "toc_projection_row_count_mismatch", "expected": len(rows), "actual": projection.get("row_count")})
    if sorted(projection.get("row_ids", [])) != sorted(row_ids):
        findings.append({"finding_id": "toc_projection_row_ids_mismatch"})
    if projection.get("page_ref_count") != len(rows):
        findings.append({"finding_id": "toc_projection_page_ref_count_mismatch", "expected": len(rows), "actual": projection.get("page_ref_count")})

    return {
        "schema_version": TOC_PAGE_REFERENCE_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "row_count": len(rows),
        "page_marker_regions": page_marker_regions,
        "findings": findings,
    }


def require_toc_page_reference_contract(
    *,
    rows: list[dict[str, Any]],
    page_marker_regions: list[str],
    projection: dict[str, Any],
    consumer: str,
) -> dict[str, Any]:
    validation = validate_toc_page_reference_contract(
        rows=rows,
        page_marker_regions=page_marker_regions,
        projection=projection,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by TOC page-reference contract: {validation['findings']}")
    return validation
