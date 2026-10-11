import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.crop_order_validation import validate_crop_order  # noqa: E402
from scripts.text_extraction_contract import (  # noqa: E402
    TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION,
    require_text_extraction_consumer_gate,
    require_valid_text_extraction_contract,
    validate_text_extraction_contract,
)


def packet(**overrides):
    base = {
        "human_review_decision": {"accepted_package_id": "P010TR-G1-VIRAL-001"},
        "text_map": {"crop_ids": ["P010-B001-TES"]},
        "continuation_notes": ["B005 continues into B002"],
        "crop_order_validation": validate_crop_order(
            units=[
                {"crop_id": "P010-B001-TES", "reading_order_index": 1},
                {"crop_id": "P010-B005-TES", "reading_order_index": 2, "continues_to_crop_id": "P010-B002-TES"},
                {"crop_id": "P010-B002-TES", "reading_order_index": 3, "continues_from_crop_id": "P010-B005-TES"},
            ],
            expected_logical_order=["P010-B001-TES", "P010-B005-TES", "P010-B002-TES"],
            physical_crop_asset_order=["P010-B001-TES", "P010-B002-TES", "P010-B005-TES"],
            continuation_edges=[{"from": "P010-B005-TES", "to": "P010-B002-TES"}],
        ),
        "ocr_execution_created": False,
        "ocr_output_created": False,
        "ocr_acceptance_created": False,
        "source_acceptance_created": False,
        "semantic_map_created": False,
        "pcrp_created": False,
        "page_complete_acceptance_created": False,
        "whole_gate_1_acceptance_created": False,
        "fixture_admission_created": False,
    }
    base.update(overrides)
    return base


def test_text_extraction_contract_accepts_bounded_packet_with_crop_order():
    result = validate_text_extraction_contract(
        packet=packet(),
        expected_predecessor_package_id="P010TR-G1-VIRAL-001",
        requires_crop_order_validation=True,
        requires_continuation_notes=True,
    )

    assert result["schema_version"] == TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_text_extraction_contract_blocks_missing_crop_ids_and_acceptance_leakage():
    bad_packet = packet(text_map={"crop_ids": []}, pcrp_created=True)

    result = validate_text_extraction_contract(
        packet=bad_packet,
        expected_predecessor_package_id="P010TR-G1-VIRAL-001",
        requires_crop_order_validation=True,
        requires_continuation_notes=True,
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "text_extraction_missing_text_evidence_crop_ids" in finding_ids
    assert "text_extraction_negative_capability_violation" in finding_ids


def test_text_extraction_contract_requires_crop_order_when_declared():
    bad_packet = packet(crop_order_validation={"schema_version": "wrong", "status": "passed"})

    with pytest.raises(ValueError, match="text extraction contract blocked"):
        require_valid_text_extraction_contract(
            packet=bad_packet,
            expected_predecessor_package_id="P010TR-G1-VIRAL-001",
            requires_crop_order_validation=True,
            requires_continuation_notes=True,
        )


def test_semantic_or_pcrp_consumer_requires_passed_text_extraction_contract():
    good_packet = packet()
    good_packet["text_extraction_contract_validation"] = validate_text_extraction_contract(
        packet=good_packet,
        expected_predecessor_package_id="P010TR-G1-VIRAL-001",
        requires_crop_order_validation=True,
        requires_continuation_notes=True,
    )

    assert require_text_extraction_consumer_gate(good_packet, consumer="semantic_map")["status"] == "passed"
    assert require_text_extraction_consumer_gate(good_packet, consumer="pcrp")["status"] == "passed"

    with pytest.raises(ValueError, match="requires text_extraction_contract_validation"):
        require_text_extraction_consumer_gate(packet(), consumer="semantic_map")


def test_semantic_or_pcrp_consumer_blocks_bad_text_contract():
    bad_packet = packet()
    bad_packet["text_extraction_contract_validation"] = {"schema_version": TEXT_EXTRACTION_CONTRACT_SCHEMA_VERSION, "status": "blocked", "findings": []}

    with pytest.raises(ValueError, match="blocked by text_extraction_contract_validation"):
        require_text_extraction_consumer_gate(bad_packet, consumer="pcrp")
