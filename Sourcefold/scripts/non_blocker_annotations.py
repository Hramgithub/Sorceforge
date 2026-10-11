from __future__ import annotations

from typing import Any


NON_BLOCKER_ANNOTATION_SCHEMA_VERSION = "sourcefold_non_blocker_annotations.v1"
REQUIRED_FIELDS = {"annotation_id", "decision", "reviewer", "evidence_ref", "affected_ids", "downstream_limits"}


def validate_non_blocker_annotations(
    annotations: list[dict[str, Any]],
    *,
    known_ids: set[str],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for annotation in annotations:
        annotation_id = annotation.get("annotation_id", "<missing>")
        missing = sorted(REQUIRED_FIELDS - set(annotation))
        if missing:
            findings.append({"finding_id": "non_blocker_annotation_missing_required_field", "annotation_id": annotation_id, "fields": missing})
        if annotation.get("decision") != "complete_non_blocker":
            findings.append({"finding_id": "non_blocker_annotation_wrong_decision", "annotation_id": annotation_id, "decision": annotation.get("decision")})
        affected_ids = annotation.get("affected_ids")
        if not isinstance(affected_ids, list) or not affected_ids:
            findings.append({"finding_id": "non_blocker_annotation_missing_affected_ids", "annotation_id": annotation_id})
        else:
            unknown = sorted(set(affected_ids) - known_ids)
            if unknown:
                findings.append({"finding_id": "non_blocker_annotation_unknown_affected_id", "annotation_id": annotation_id, "unknown_ids": unknown})
        downstream_limits = annotation.get("downstream_limits")
        if not isinstance(downstream_limits, list) or not downstream_limits:
            findings.append({"finding_id": "non_blocker_annotation_missing_downstream_limits", "annotation_id": annotation_id})
    return {
        "schema_version": NON_BLOCKER_ANNOTATION_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "annotation_count": len(annotations),
        "findings": findings,
    }
