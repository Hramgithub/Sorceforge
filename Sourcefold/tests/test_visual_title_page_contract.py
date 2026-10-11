import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.visual_title_page_contract import (  # noqa: E402
    VISUAL_TITLE_PAGE_CONTRACT_SCHEMA_VERSION,
    require_visual_title_page_contract,
    validate_visual_title_page_contract,
)


def profile(**overrides):
    payload = {
        "page_type": "visual_title",
        "required_anchor_ids": ["cover", "title", "footer"],
        "requires_text_extraction": False,
        "allows_page_complete_without_text_map": True,
    }
    payload.update(overrides)
    return payload


def anchors():
    return [
        {"anchor_id": "cover", "review_state": "ready_for_review", "not_source_text": True, "evidence_ref": "P001-B001"},
        {"anchor_id": "title", "review_state": "ready_for_review", "not_source_text": True, "evidence_ref": "P001-B002"},
        {"anchor_id": "footer", "review_state": "ready_for_review", "not_source_text": True, "evidence_ref": "P001-B003"},
    ]


def negative_capabilities(**overrides):
    payload = {
        "ocr_executed": False,
        "text_extraction_created": False,
        "source_acceptance_created": False,
        "fixture_admission_created": False,
        "whole_gate_acceptance_created": False,
        "raw_artifacts_modified": False,
    }
    payload.update(overrides)
    return payload


def test_visual_title_page_contract_accepts_p001_style_cover_page():
    result = validate_visual_title_page_contract(
        profile=profile(),
        anchors=anchors(),
        negative_capabilities=negative_capabilities(),
    )

    assert result["schema_version"] == VISUAL_TITLE_PAGE_CONTRACT_SCHEMA_VERSION
    assert result["status"] == "passed"
    assert result["required_anchor_ids"] == ["cover", "title", "footer"]


def test_visual_title_page_contract_blocks_missing_anchor_and_text_extraction():
    result = validate_visual_title_page_contract(
        profile=profile(requires_text_extraction=True),
        anchors=anchors()[:2],
        negative_capabilities=negative_capabilities(text_extraction_created=True),
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "visual_title_text_extraction_not_explicitly_disabled" in finding_ids
    assert "visual_title_missing_required_anchors" in finding_ids
    assert "visual_title_negative_capability_leakage" in finding_ids


def test_visual_title_page_contract_consumer_fails_closed():
    with pytest.raises(ValueError, match="visual title page contract"):
        require_visual_title_page_contract(
            profile=profile(page_type="text_page"),
            anchors=anchors(),
            negative_capabilities=negative_capabilities(),
            consumer="page_acceptance",
        )
