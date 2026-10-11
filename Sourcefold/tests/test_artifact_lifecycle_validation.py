import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.artifact_lifecycle_validation import (  # noqa: E402
    ARTIFACT_LIFECYCLE_SCHEMA_VERSION,
    require_current_artifact,
    validate_artifact_lifecycle,
)


def test_artifact_lifecycle_accepts_current_superseding_packet():
    packet = {
        "package_id": "P009TR-G1-VIRAL-003",
        "status": "page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked",
        "scope": "page_009_crop_role_contract_only_no_pcrp_no_ocr_no_acceptance",
        "supersedes": {"package_id": "P009TR-G1-VIRAL-002"},
    }

    result = validate_artifact_lifecycle(
        packet=packet,
        required_current_package_id="P009TR-G1-VIRAL-003",
        stale_package_ids=["P009TR-G1-VIRAL-002"],
        required_supersedes_package_id="P009TR-G1-VIRAL-002",
        consumer="pcrp",
    )

    assert result["schema_version"] == ARTIFACT_LIFECYCLE_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_artifact_lifecycle_rejects_stale_packet_for_consumer():
    packet = {
        "package_id": "P009TR-G1-VIRAL-002",
        "status": "historical_readability_only_stale_for_pcrp",
        "scope": "readability_only",
    }

    result = validate_artifact_lifecycle(
        packet=packet,
        required_current_package_id="P009TR-G1-VIRAL-003",
        stale_package_ids=["P009TR-G1-VIRAL-002"],
        required_supersedes_package_id="P009TR-G1-VIRAL-002",
        consumer="pcrp",
    )

    assert result["status"] == "blocked"
    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert "non_current_artifact_for_consumer" in finding_ids
    assert "stale_artifact_for_consumer" in finding_ids


def test_artifact_lifecycle_consumer_fails_closed_on_missing_supersession():
    packet = {
        "package_id": "P009TR-G1-VIRAL-003",
        "status": "page_009_crop_contract_ready_for_bogdan_review_pcrp_still_blocked",
        "scope": "page_009_crop_role_contract_only_no_pcrp_no_ocr_no_acceptance",
    }

    with pytest.raises(ValueError, match="artifact lifecycle validation"):
        require_current_artifact(
            packet=packet,
            required_current_package_id="P009TR-G1-VIRAL-003",
            stale_package_ids=["P009TR-G1-VIRAL-002"],
            required_supersedes_package_id="P009TR-G1-VIRAL-002",
            consumer="pcrp",
        )
