import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.legacy_pcrp_refresh_contract import (  # noqa: E402
    LEGACY_PCRP_REFRESH_SCHEMA_VERSION,
    REQUIRED_CURRENT_CONTRACTS,
    require_legacy_pcrp_refresh_contract,
    validate_legacy_pcrp_refresh_contract,
)


def legacy(**overrides):
    payload = {
        "package_id": "PCRP-G1-VIRAL-P006-001",
        "state": "held",
        "used_directly_for_page_acceptance": False,
        "known_structural_defects": ["collapsed_text_map"],
    }
    payload.update(overrides)
    return payload


def refresh(**overrides):
    payload = {
        "package_id": "PCRP-G1-VIRAL-P006-002",
        "state": "current",
        "refreshes_package_id": "PCRP-G1-VIRAL-P006-001",
        "passed_contracts": sorted(REQUIRED_CURRENT_CONTRACTS),
        "negative_regression_input_recorded": True,
        "creates_page_acceptance": False,
    }
    payload.update(overrides)
    return payload


def test_legacy_pcrp_refresh_contract_accepts_current_refresh_packet():
    result = validate_legacy_pcrp_refresh_contract(
        legacy_packet=legacy(),
        refresh_packet=refresh(),
        consumer="page_acceptance",
    )

    assert result["schema_version"] == LEGACY_PCRP_REFRESH_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_legacy_pcrp_refresh_contract_blocks_direct_legacy_and_missing_contracts():
    result = validate_legacy_pcrp_refresh_contract(
        legacy_packet=legacy(used_directly_for_page_acceptance=True),
        refresh_packet=refresh(passed_contracts=["semantic_validation"], negative_regression_input_recorded=False),
        consumer="page_acceptance",
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "legacy_pcrp_used_directly_for_acceptance" in finding_ids
    assert "legacy_pcrp_refresh_missing_current_contracts" in finding_ids
    assert "legacy_pcrp_missing_negative_regression_record" in finding_ids


def test_legacy_pcrp_refresh_consumer_fails_closed():
    with pytest.raises(ValueError, match="legacy PCRP refresh contract"):
        require_legacy_pcrp_refresh_contract(
            legacy_packet=legacy(state="current"),
            refresh_packet=refresh(refreshes_package_id="wrong"),
            consumer="page_acceptance",
        )
