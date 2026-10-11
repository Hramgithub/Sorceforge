import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.non_blocker_annotations import (  # noqa: E402
    NON_BLOCKER_ANNOTATION_SCHEMA_VERSION,
    validate_non_blocker_annotations,
)


def test_non_blocker_annotations_accept_reviewed_non_blocker():
    result = validate_non_blocker_annotations(
        [
            {
                "annotation_id": "NBA-P009-R-GREY",
                "decision": "complete_non_blocker",
                "reviewer": "Bogdan",
                "evidence_ref": "P009-B004-TEXT-EVIDENCE",
                "affected_ids": ["P009-B004", "PRM-G1-VIRAL-001-P009-R04"],
                "downstream_limits": ["not_page_acceptance", "not_ocr_acceptance"],
            }
        ],
        known_ids={"P009-B004", "PRM-G1-VIRAL-001-P009-R04", "P009-B004-TEXT-EVIDENCE"},
    )

    assert result["schema_version"] == NON_BLOCKER_ANNOTATION_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_non_blocker_annotations_block_silent_or_unknown_annotation():
    result = validate_non_blocker_annotations(
        [
            {
                "annotation_id": "NBA-P009-R-GREY",
                "decision": "complete_non_blocker",
                "reviewer": "Bogdan",
                "evidence_ref": "P009-B004-TEXT-EVIDENCE",
                "affected_ids": ["missing"],
                "downstream_limits": [],
            }
        ],
        known_ids={"P009-B004"},
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "non_blocker_annotation_unknown_affected_id" in finding_ids
    assert "non_blocker_annotation_missing_downstream_limits" in finding_ids
