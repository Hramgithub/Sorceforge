import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.deferred_review_contract import (  # noqa: E402
    DEFERRED_REVIEW_CONTRACT_SCHEMA_VERSION,
    validate_deferred_review_contract,
)


def test_deferred_review_contract_accepts_visual_anchor_and_action_backlog():
    result = validate_deferred_review_contract(
        attachments=[
            {
                "attachment_id": "P008-ART",
                "role": "human_review_crop",
                "covered_review_blocks": ["P008-B007"],
                "include_in_text_map": False,
                "skip_edge_ink_check": True,
            }
        ],
        action_backlog={"attachment_id": "P008-ACTION", "role": "action_backlog_markdown", "steps": [{"order": 1}]},
        creates_page_acceptance=False,
        creates_whole_gate_acceptance=False,
    )

    assert result["schema_version"] == DEFERRED_REVIEW_CONTRACT_SCHEMA_VERSION
    assert result["status"] == "passed"
    assert result["deferred_anchor_ids"] == ["P008-ART"]
    assert result["action_backlog_present"] is True


def test_deferred_review_contract_blocks_anchor_text_map_leakage():
    result = validate_deferred_review_contract(
        attachments=[
            {
                "attachment_id": "P008-ART",
                "role": "human_review_crop",
                "covered_review_blocks": ["P008-B007"],
                "include_in_text_map": True,
                "skip_edge_ink_check": True,
            }
        ],
        action_backlog=None,
        creates_page_acceptance=False,
        creates_whole_gate_acceptance=False,
    )

    assert result["status"] == "blocked"
    assert any(finding["finding_id"] == "deferred_anchor_leaks_into_text_map" for finding in result["findings"])


def test_deferred_review_contract_blocks_acceptance_leakage():
    result = validate_deferred_review_contract(
        attachments=[],
        action_backlog={"attachment_id": "P008-ACTION", "role": "action_backlog_markdown", "steps": [{"order": 1}]},
        creates_page_acceptance=True,
        creates_whole_gate_acceptance=True,
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "deferred_review_creates_page_acceptance" in finding_ids
    assert "deferred_review_creates_whole_gate_acceptance" in finding_ids
