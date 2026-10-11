import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.route_cursor_transition import (  # noqa: E402
    ROUTE_CURSOR_TRANSITION_SCHEMA_VERSION,
    validate_route_cursor_transition,
)


def test_route_cursor_transition_accepts_allowed_status_only_move():
    result = validate_route_cursor_transition(
        from_cursor="page_009_complete_pages_010_020_unstarted",
        to_cursor="page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp",
        required_next="page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp",
        allowed_transitions={
            "page_009_complete_pages_010_020_unstarted": [
                "page_010_triage_crop_contract_ready_for_bogdan_review_no_pcrp"
            ]
        },
        created_capabilities={
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
            "fixture_admission_created": False,
            "source_acceptance_created": False,
            "pcrp_created": False,
        },
    )

    assert result["schema_version"] == ROUTE_CURSOR_TRANSITION_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_route_cursor_transition_blocks_unlisted_move_and_acceptance_leak():
    result = validate_route_cursor_transition(
        from_cursor="page_010_text_ready",
        to_cursor="page_010_page_complete_accepted",
        required_next="page_010_semantic_map_ready",
        allowed_transitions={"page_010_text_ready": ["page_010_semantic_map_ready"]},
        created_capabilities={"page_complete_acceptance_created": True},
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "route_cursor_transition_not_allowed" in finding_ids
    assert "route_cursor_required_next_mismatch" in finding_ids
    assert "route_cursor_transition_created_unauthorized_capability" in finding_ids
