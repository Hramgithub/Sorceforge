from __future__ import annotations

from typing import Any


SOURCE_RECONSTRUCTION_SLICE_SCHEMA_VERSION = "sourcefold_source_reconstruction_slice.v1"
FORBIDDEN_CAPABILITIES = {
    "page_complete_acceptance_created": False,
    "whole_gate_acceptance_created": False,
    "translation_authorized": False,
    "proofreading_authorized": False,
    "implementation_authorized": False,
    "push_authorized": False,
}
ALLOWED_RECORD_TYPES = {"source_text", "visual_exclusion"}


def validate_source_reconstruction_slice_contract(
    *,
    packet: dict[str, Any],
    expected_record_count: int,
    expected_source_text_records: int,
    expected_visual_exclusion_records: int,
    forbidden_capabilities: dict[str, Any],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    records = packet.get("records", packet.get("packet_items", []))
    if not isinstance(records, list):
        findings.append({"finding_id": "source_slice_records_not_list"})
        records = []

    if len(records) != expected_record_count:
        findings.append(
            {
                "finding_id": "source_slice_record_count_mismatch",
                "expected": expected_record_count,
                "actual": len(records),
            }
        )

    source_text_records = [record for record in records if record.get("record_type") == "source_text" or record.get("fixture_kind") == "positive"]
    visual_exclusion_records = [
        record for record in records if record.get("record_type") == "visual_exclusion" or record.get("fixture_kind") == "negative_visual_exclusion"
    ]
    if len(source_text_records) != expected_source_text_records:
        findings.append(
            {
                "finding_id": "source_slice_source_text_count_mismatch",
                "expected": expected_source_text_records,
                "actual": len(source_text_records),
            }
        )
    if len(visual_exclusion_records) != expected_visual_exclusion_records:
        findings.append(
            {
                "finding_id": "source_slice_visual_exclusion_count_mismatch",
                "expected": expected_visual_exclusion_records,
                "actual": len(visual_exclusion_records),
            }
        )

    seen_ids: set[str] = set()
    for index, record in enumerate(records):
        record_id = record.get("record_id") or record.get("fixture_id")
        if not record_id:
            findings.append({"finding_id": "source_slice_record_missing_id", "index": index})
            continue
        if record_id in seen_ids:
            findings.append({"finding_id": "source_slice_duplicate_record_id", "record_id": record_id})
        seen_ids.add(record_id)
        record_type = record.get("record_type")
        fixture_kind = record.get("fixture_kind")
        if record_type not in ALLOWED_RECORD_TYPES and fixture_kind not in {"positive", "negative_visual_exclusion"}:
            findings.append({"finding_id": "source_slice_unknown_record_type", "record_id": record_id})
        if not (record.get("predecessor_sha256") or record.get("source_sha256") or record.get("qa_acceptance") is True):
            findings.append({"finding_id": "source_slice_record_missing_lineage", "record_id": record_id})

    if packet.get("accepted_scope") not in {None, "exact_source_reconstruction_slice_only", "exact_G1RP_G1_VIRAL_001_source_reconstruction_evidence_slice_only"}:
        findings.append({"finding_id": "source_slice_scope_too_broad", "accepted_scope": packet.get("accepted_scope")})
    if packet.get("requires_rollup_before_broader_gate_use") is False:
        findings.append({"finding_id": "source_slice_missing_broader_rollup_gate"})

    leaked = {key: forbidden_capabilities.get(key) for key, expected in FORBIDDEN_CAPABILITIES.items() if forbidden_capabilities.get(key) is not expected}
    if leaked:
        findings.append({"finding_id": "source_slice_authority_leakage", "flags": leaked})

    return {
        "schema_version": SOURCE_RECONSTRUCTION_SLICE_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "record_count": len(records),
        "source_text_records": len(source_text_records),
        "visual_exclusion_records": len(visual_exclusion_records),
        "forbidden_capability_requirements": FORBIDDEN_CAPABILITIES,
        "findings": findings,
    }


def require_source_reconstruction_slice_contract(
    *,
    packet: dict[str, Any],
    expected_record_count: int,
    expected_source_text_records: int,
    expected_visual_exclusion_records: int,
    forbidden_capabilities: dict[str, Any],
    consumer: str,
) -> dict[str, Any]:
    validation = validate_source_reconstruction_slice_contract(
        packet=packet,
        expected_record_count=expected_record_count,
        expected_source_text_records=expected_source_text_records,
        expected_visual_exclusion_records=expected_visual_exclusion_records,
        forbidden_capabilities=forbidden_capabilities,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by source reconstruction slice contract: {validation['findings']}")
    return validation
