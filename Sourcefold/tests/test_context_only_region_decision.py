import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.context_only_region_decision import (  # noqa: E402
    CONTEXT_ONLY_REGION_DECISION_SCHEMA_VERSION,
    require_context_only_region_decision,
    validate_context_only_region_decision,
)


KNOWN = {"PRM-G1-VIRAL-001-P004-R01", "PRM-G1-VIRAL-001-P004-R02", "PRM-G1-VIRAL-001-P004-R03"}


def decision(**overrides):
    payload = {
        "context_region_id": "PRM-G1-VIRAL-001-P004-R01",
        "confirmed_status": "context_only_not_peer_crop_record",
        "reviewer": "Bogdan",
        "human_decision_ref": "page 004 context-only ok",
        "overlap_rationale": "full tilted inset would overlap peer text crops",
        "peer_region_ids": ["PRM-G1-VIRAL-001-P004-R02", "PRM-G1-VIRAL-001-P004-R03"],
        "downstream_limits": ["not_page_complete_acceptance", "not_source_acceptance"],
    }
    payload.update(overrides)
    return payload


def forbidden(**overrides):
    payload = {
        "page_complete_acceptance_created": False,
        "source_acceptance_created": False,
        "ocr_acceptance_created": False,
        "fixture_admission_created": False,
        "whole_gate_acceptance_created": False,
        "predecessor_mutated": False,
    }
    payload.update(overrides)
    return payload


def test_context_only_region_decision_accepts_p004_style_inset():
    result = validate_context_only_region_decision(
        decision=decision(),
        known_region_ids=KNOWN,
        forbidden_capabilities=forbidden(),
    )

    assert result["schema_version"] == CONTEXT_ONLY_REGION_DECISION_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_context_only_region_decision_blocks_missing_peer_unknown_region_and_acceptance_leakage():
    result = validate_context_only_region_decision(
        decision=decision(context_region_id="missing", peer_region_ids=[], downstream_limits=[]),
        known_region_ids=KNOWN,
        forbidden_capabilities=forbidden(page_complete_acceptance_created=True),
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "context_only_unknown_region_id" in finding_ids
    assert "context_only_missing_peer_regions" in finding_ids
    assert "context_only_missing_downstream_limits" in finding_ids
    assert "context_only_authority_leakage" in finding_ids


def test_context_only_region_decision_consumer_fails_closed():
    with pytest.raises(ValueError, match="context-only region decision"):
        require_context_only_region_decision(
            decision=decision(reviewer="Sol"),
            known_region_ids=KNOWN,
            forbidden_capabilities=forbidden(),
            consumer="page_map",
        )
