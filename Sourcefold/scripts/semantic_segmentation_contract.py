from __future__ import annotations

from dataclasses import dataclass


class SemanticSegmentationError(ValueError):
    pass


@dataclass(frozen=True)
class BoundedCalloutSplit:
    before: str
    heading: str
    body: str
    after: str
    boundary_kind: str
    boundary_marker: str

    def contract(self) -> dict[str, str]:
        return callout_body_contract(
            callout_heading=self.heading,
            boundary_kind=self.boundary_kind,
            boundary_marker=self.boundary_marker,
        )


BOUNDARY_KINDS = {
    "explicit_body_end_marker",
    "next_segment_start_marker",
    "callout_extends_to_text_block_end",
    "reviewed_source_region_boundary",
    "reviewed_continuation_boundary",
}

BOX_BODY_DISPLAY_STYLES = {"callout_body", "sidebar_body", "card_body"}


def callout_body_contract(
    *,
    callout_heading: str,
    boundary_kind: str = "callout_extends_to_text_block_end",
    boundary_marker: str = "<text_block_end>",
) -> dict[str, str]:
    if boundary_kind not in BOUNDARY_KINDS:
        raise SemanticSegmentationError(f"unsupported semantic split boundary kind: {boundary_kind}")
    return {
        "contract": "semantic_segmentation_contract.v1",
        "segment_type": "bounded_callout_body",
        "callout_heading": callout_heading,
        "boundary_kind": boundary_kind,
        "boundary_marker": boundary_marker,
    }


def _unit_id(unit: dict) -> str | None:
    value = unit.get("unit_id")
    return value if isinstance(value, str) else None


def _is_segment_body_unit(unit: dict) -> bool:
    unit_type = unit.get("unit_type")
    if unit_type not in {"paragraph", "quote", "list", "continuation"}:
        return False
    unit_id = _unit_id(unit) or ""
    semantic_role = unit.get("semantic_role") if isinstance(unit.get("semantic_role"), str) else ""
    return (
        unit.get("display_style") in BOX_BODY_DISPLAY_STYLES
        or "-KEEPER-" in unit_id
        or semantic_role.startswith("keeper_notes")
    )


def validate_semantic_split_contracts(units: list[dict]) -> dict:
    findings: list[dict] = []
    for unit in units:
        if not _is_segment_body_unit(unit):
            continue
        unit_id = _unit_id(unit)
        contract = unit.get("semantic_split_contract")
        if not isinstance(contract, dict):
            findings.append(
                {
                    "finding_id": "missing_semantic_split_contract",
                    "rule_id": "SU-SEG-001",
                    "severity": "blocker",
                    "waiver": "non_waivable",
                    "unit_id": unit_id,
                    "message": "Callout/sidebar/card/Keeper body units must declare a semantic_split_contract.",
                }
            )
            continue
        if contract.get("contract") != "semantic_segmentation_contract.v1":
            findings.append(
                {
                    "finding_id": "invalid_semantic_split_contract",
                    "rule_id": "SU-SEG-002",
                    "severity": "blocker",
                    "waiver": "non_waivable",
                    "unit_id": unit_id,
                    "message": "semantic_split_contract must use semantic_segmentation_contract.v1.",
                }
            )
        if contract.get("boundary_kind") not in BOUNDARY_KINDS:
            findings.append(
                {
                    "finding_id": "invalid_semantic_split_boundary",
                    "rule_id": "SU-SEG-003",
                    "severity": "blocker",
                    "waiver": "non_waivable",
                    "unit_id": unit_id,
                    "message": "semantic_split_contract boundary_kind is not registered.",
                }
            )
        if not isinstance(contract.get("boundary_marker"), str) or not contract.get("boundary_marker"):
            findings.append(
                {
                    "finding_id": "missing_semantic_split_boundary_marker",
                    "rule_id": "SU-SEG-004",
                    "severity": "blocker",
                    "waiver": "non_waivable",
                    "unit_id": unit_id,
                    "message": "semantic_split_contract must record the boundary marker.",
                }
            )
    blocker_count = sum(1 for item in findings if item["severity"] == "blocker" and item["waiver"] == "non_waivable")
    return {"valid": blocker_count == 0, "readiness_blocked": blocker_count > 0, "findings": findings}


def _normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _strip_leading_blank_lines(text: str) -> str:
    while text.startswith("\n"):
        text = text[1:]
    return text


def split_bounded_callout(
    text: str,
    *,
    callout_heading: str,
    body_end_marker: str | None = None,
    next_segment_start_marker: str | None = None,
    allow_to_end: bool = False,
) -> BoundedCalloutSplit:
    normalized = _normalize(text)
    heading_index = normalized.find(callout_heading)
    if heading_index < 0:
        raise SemanticSegmentationError(f"missing callout heading: {callout_heading}")

    after_heading = normalized[heading_index + len(callout_heading) :]
    tail = _strip_leading_blank_lines(after_heading)
    before = normalized[:heading_index].strip()

    if body_end_marker:
        marker_index = tail.find(body_end_marker)
        if marker_index < 0:
            raise SemanticSegmentationError(f"missing callout body end marker: {body_end_marker}")
        body_end = marker_index + len(body_end_marker)
        body = tail[:body_end].strip()
        after = tail[body_end:].strip()
        return BoundedCalloutSplit(
            before=before,
            heading=callout_heading,
            body=body,
            after=after,
            boundary_kind="explicit_body_end_marker",
            boundary_marker=body_end_marker,
        )

    if next_segment_start_marker:
        marker_index = tail.find(next_segment_start_marker)
        if marker_index < 0:
            raise SemanticSegmentationError(f"missing next segment start marker: {next_segment_start_marker}")
        body = tail[:marker_index].strip()
        after = tail[marker_index:].strip()
        return BoundedCalloutSplit(
            before=before,
            heading=callout_heading,
            body=body,
            after=after,
            boundary_kind="next_segment_start_marker",
            boundary_marker=next_segment_start_marker,
        )

    if allow_to_end:
        return BoundedCalloutSplit(
            before=before,
            heading=callout_heading,
            body=tail.strip(),
            after="",
            boundary_kind="callout_extends_to_text_block_end",
            boundary_marker="<text_block_end>",
        )

    raise SemanticSegmentationError(
        "callout body boundary is not declared; pass body_end_marker, "
        "next_segment_start_marker, or allow_to_end=True"
    )
