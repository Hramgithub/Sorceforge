import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.human_review_gate_contract import (  # noqa: E402
    HUMAN_REVIEW_GATE_SCHEMA_VERSION,
    validate_human_review_gate,
)


def test_human_review_gate_accepts_sol_terra_and_bogdan_decision():
    result = validate_human_review_gate(
        sol_review={"status": "OK"},
        terra_review={"status": "OK"},
        human_decision={
            "package_id": "P010TXT-G1-VIRAL-001",
            "decision": "p010 text ok",
            "source_message_id": "1494",
            "creates_page_complete_acceptance": False,
        },
        expected_package_id="P010TXT-G1-VIRAL-001",
        allowed_decisions=["p010 text ok", "hold p010 text"],
    )

    assert result["schema_version"] == HUMAN_REVIEW_GATE_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_human_review_gate_blocks_missing_or_wrong_review_state():
    result = validate_human_review_gate(
        sol_review={"status": "OK"},
        terra_review={"status": "BLOCKED"},
        human_decision={
            "package_id": "P010TR-G1-VIRAL-001",
            "decision": "page complete ok",
            "creates_page_complete_acceptance": True,
        },
        expected_package_id="P010TXT-G1-VIRAL-001",
        allowed_decisions=["p010 text ok", "hold p010 text"],
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "human_review_gate_terra_not_ok" in finding_ids
    assert "human_review_gate_wrong_package" in finding_ids
    assert "human_review_gate_decision_not_allowed" in finding_ids
    assert "human_review_gate_missing_source_message" in finding_ids
    assert "human_review_gate_leaks_page_acceptance" in finding_ids
