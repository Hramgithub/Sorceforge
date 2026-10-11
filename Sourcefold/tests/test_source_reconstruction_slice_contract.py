import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.source_reconstruction_slice_contract import (  # noqa: E402
    SOURCE_RECONSTRUCTION_SLICE_SCHEMA_VERSION,
    require_source_reconstruction_slice_contract,
    validate_source_reconstruction_slice_contract,
)


def packet(records=None, **overrides):
    payload = {
        "packet_id": "G1RP-G1-VIRAL-001",
        "accepted_scope": "exact_source_reconstruction_slice_only",
        "requires_rollup_before_broader_gate_use": True,
        "records": records
        if records is not None
        else [
            *[
                {"record_id": f"SRC-{index}", "record_type": "source_text", "predecessor_sha256": "A"}
                for index in range(4)
            ],
            *[
                {"record_id": f"VIS-{index}", "record_type": "visual_exclusion", "predecessor_sha256": "B"}
                for index in range(3)
            ],
        ],
    }
    payload.update(overrides)
    return payload


def forbidden(**overrides):
    payload = {
        "page_complete_acceptance_created": False,
        "whole_gate_acceptance_created": False,
        "translation_authorized": False,
        "proofreading_authorized": False,
        "implementation_authorized": False,
        "push_authorized": False,
    }
    payload.update(overrides)
    return payload


def test_source_reconstruction_slice_accepts_narrow_seven_record_slice():
    result = validate_source_reconstruction_slice_contract(
        packet=packet(),
        expected_record_count=7,
        expected_source_text_records=4,
        expected_visual_exclusion_records=3,
        forbidden_capabilities=forbidden(),
    )

    assert result["schema_version"] == SOURCE_RECONSTRUCTION_SLICE_SCHEMA_VERSION
    assert result["status"] == "passed"
    assert result["record_count"] == 7


def test_source_reconstruction_slice_blocks_count_scope_and_authority_leakage():
    result = validate_source_reconstruction_slice_contract(
        packet=packet(records=[{"record_id": "SRC-1", "record_type": "source_text"}], accepted_scope="whole_gate_1"),
        expected_record_count=7,
        expected_source_text_records=4,
        expected_visual_exclusion_records=3,
        forbidden_capabilities=forbidden(page_complete_acceptance_created=True),
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "source_slice_record_count_mismatch" in finding_ids
    assert "source_slice_scope_too_broad" in finding_ids
    assert "source_slice_authority_leakage" in finding_ids
    assert "source_slice_record_missing_lineage" in finding_ids


def test_source_reconstruction_slice_consumer_fails_closed():
    with pytest.raises(ValueError, match="source reconstruction slice contract"):
        require_source_reconstruction_slice_contract(
            packet=packet(records=[]),
            expected_record_count=7,
            expected_source_text_records=4,
            expected_visual_exclusion_records=3,
            forbidden_capabilities=forbidden(),
            consumer="gate_rollup",
        )
