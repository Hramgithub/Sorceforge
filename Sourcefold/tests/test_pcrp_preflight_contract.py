import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.pcrp_preflight_contract import (  # noqa: E402
    PCRP_PREFLIGHT_SCHEMA_VERSION,
    validate_pcrp_preflight,
)


def test_pcrp_preflight_accepts_passed_predecessor_contracts():
    result = validate_pcrp_preflight(
        page="010",
        required_contracts={
            "bounded_authorization": {"status": "passed"},
            "crop_role_contract": {"status": "passed"},
            "text_extraction_contract": {"status": "passed"},
            "human_review_gate": {"status": "passed"},
        },
        output_capabilities={
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
            "fixture_admission_created": False,
            "source_acceptance_created": False,
            "ocr_acceptance_created": False,
        },
    )

    assert result["schema_version"] == PCRP_PREFLIGHT_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_pcrp_preflight_blocks_missing_or_blocked_contract_and_acceptance_leakage():
    result = validate_pcrp_preflight(
        page="010",
        required_contracts={
            "bounded_authorization": {"status": "passed"},
            "crop_role_contract": {"status": "blocked", "findings": [{"finding_id": "bad_crop"}]},
            "human_review_gate": None,
        },
        output_capabilities={"page_complete_acceptance_created": True},
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "pcrp_preflight_blocked_contract" in finding_ids
    assert "pcrp_preflight_missing_contract" in finding_ids
    assert "pcrp_preflight_acceptance_leakage" in finding_ids
