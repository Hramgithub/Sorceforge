from __future__ import annotations

from typing import Any


ARTIFACT_LIFECYCLE_SCHEMA_VERSION = "sourcefold_artifact_lifecycle.v1"
STALE_STATES = {"held", "stale", "superseded", "readability_only"}


def validate_artifact_lifecycle(
    *,
    packet: dict[str, Any],
    required_current_package_id: str,
    stale_package_ids: list[str] | None = None,
    required_supersedes_package_id: str | None = None,
    consumer: str,
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    package_id = packet.get("package_id")
    if package_id != required_current_package_id:
        findings.append(
            {
                "finding_id": "non_current_artifact_for_consumer",
                "consumer": consumer,
                "expected": required_current_package_id,
                "actual": package_id,
            }
        )
    if package_id in set(stale_package_ids or []):
        findings.append(
            {
                "finding_id": "stale_artifact_for_consumer",
                "consumer": consumer,
                "package_id": package_id,
            }
        )
    supersedes = packet.get("supersedes", {})
    if required_supersedes_package_id and supersedes.get("package_id") != required_supersedes_package_id:
        findings.append(
            {
                "finding_id": "missing_required_supersession_link",
                "consumer": consumer,
                "expected_supersedes": required_supersedes_package_id,
                "actual_supersedes": supersedes.get("package_id"),
            }
        )
    status_text = " ".join(str(packet.get(key, "")) for key in ("status", "scope"))
    if any(state in status_text for state in STALE_STATES):
        findings.append(
            {
                "finding_id": "stale_state_text_for_current_consumer",
                "consumer": consumer,
                "package_id": package_id,
                "status": packet.get("status"),
                "scope": packet.get("scope"),
            }
        )
    return {
        "schema_version": ARTIFACT_LIFECYCLE_SCHEMA_VERSION,
        "status": "passed" if not findings else "blocked",
        "consumer": consumer,
        "required_current_package_id": required_current_package_id,
        "stale_package_ids": stale_package_ids or [],
        "required_supersedes_package_id": required_supersedes_package_id,
        "findings": findings,
    }


def require_current_artifact(
    *,
    packet: dict[str, Any],
    required_current_package_id: str,
    stale_package_ids: list[str] | None = None,
    required_supersedes_package_id: str | None = None,
    consumer: str,
) -> dict[str, Any]:
    validation = validate_artifact_lifecycle(
        packet=packet,
        required_current_package_id=required_current_package_id,
        stale_package_ids=stale_package_ids,
        required_supersedes_package_id=required_supersedes_package_id,
        consumer=consumer,
    )
    if validation["status"] != "passed":
        raise ValueError(f"{consumer} blocked by artifact lifecycle validation: {validation['findings']}")
    return validation
