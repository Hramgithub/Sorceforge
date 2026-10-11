from __future__ import annotations

from typing import Any

try:
    from semantic_segmentation_contract import BOX_BODY_DISPLAY_STYLES, BOUNDARY_KINDS
except ModuleNotFoundError:
    from scripts.semantic_segmentation_contract import BOX_BODY_DISPLAY_STYLES, BOUNDARY_KINDS


SEMANTIC_UNIT_SCHEMA_VERSION = "page_review_semantic_units.v1"
SEMANTIC_UNIT_TAXONOMY_VERSION = "sourcefold_page_review_taxonomy.v1"

UNIT_TYPES = {
    "heading",
    "paragraph",
    "quote",
    "list",
    "list_item",
    "table",
    "table_row",
    "table_cell",
    "callout",
    "sidebar",
    "card",
    "stat_block",
    "stat_label",
    "stat_value",
    "art",
    "caption",
    "page_ref",
    "page_marker",
    "continuation",
    "unknown_unsupported",
    "unclassified_bounded_unit",
}
HEADING_LEVELS = {"h1", "h2", "h3", "h4", "h5", "h6"}
UNIT_SCOPES = {"in_scope_text", "context_only", "visual_only", "excluded", "unknown", "blocked"}
DISPLAY_STYLES = {
    "chapter_heading",
    "section_heading",
    "body",
    "pull_quote",
    "list_item",
    "table_header",
    "table_cell",
    "callout_title",
    "callout_body",
    "sidebar_title",
    "sidebar_body",
    "card_title",
    "card_body",
    "stat_label",
    "stat_value",
    "caption",
    "page_ref",
    "page_marker",
    "visual_art",
    "unknown",
}
SOURCE_ROLES = {
    "accepted_source_block",
    "human_verified_span",
    "draft_review_span",
    "existing_ocr_raw",
    "profile_override",
    "visual_context",
    "not_applicable",
    "unknown",
}
BLOCK_ROLES = {
    "title_region",
    "text_column",
    "body_block",
    "list_region",
    "table_region",
    "art_region",
    "caption_region",
    "callout_region",
    "sidebar_region",
    "card_region",
    "stat_block_region",
    "page_marker_region",
    "context_region",
    "excluded_region",
    "unknown_region",
}
TEXT_SOURCE_STATES = {
    "accepted_source",
    "human_verified",
    "draft_review_text",
    "ocr_raw_existing",
    "not_applicable",
}
REVIEW_STATES = {"ready_for_review", "blocked", "context_only", "visual_only", "excluded", "unknown"}
REGION_DECISIONS = {"represented", "absent", "context_only", "visual_only", "excluded", "unknown", "blocked"}
REGION_DECISIONS_WITHOUT_UNITS = {"absent", "context_only", "visual_only", "excluded"}
REPRESENTING_SCOPES = {"in_scope_text", "context_only", "visual_only"}
UNKNOWN_UNIT_TYPES = {"unknown_unsupported", "unclassified_bounded_unit"}
PARAGRAPH_BOUNDARY_UNIT_TYPES = {"paragraph", "continuation"}
NOT_EVIDENCE_FOR = [
    "source_acceptance",
    "ocr_acceptance",
    "pdf_text_extraction",
    "render_acceptance",
    "fixture_admission",
    "page_complete_acceptance",
    "whole_gate_acceptance",
]
TEXT_EVIDENCE_CROP_ROLES = {"ocr_candidate_crop", "text_evidence_crop"}
LAYOUT_ROLES = {"block_heading", "inline_heading", "body", "unknown"}
FONT_STYLES = {"normal", "italic", "bold", "bold_italic", "unknown"}

REQUIRED_FIELDS = {
    "unit_id",
    "schema_version",
    "taxonomy_version",
    "unit_type",
    "unit_scope",
    "display_style",
    "source_role",
    "block_role",
    "reading_order",
    "source_region_ids",
    "crop_ids",
    "evidence_predecessors",
    "text_source_state",
}


def finding(
    finding_id: str,
    rule_id: str,
    unit_id: str | None,
    message: str,
    severity: str = "blocker",
    waiver: str = "non_waivable",
) -> dict[str, Any]:
    return {
        "finding_id": finding_id,
        "rule_id": rule_id,
        "severity": severity,
        "waiver": waiver,
        "unit_id": unit_id,
        "message": message,
    }


def nested_run_in_heading_level(parent_heading_level: str) -> str:
    if parent_heading_level not in HEADING_LEVELS:
        raise ValueError("parent_heading_level must be h1 through h6")
    parent_depth = int(parent_heading_level[1:])
    return f"h{min(parent_depth + 1, 6)}"


def keeper_notes_callout_heading_level() -> str:
    return "h4"


def contains_embedded_paragraph_boundary(text: Any) -> bool:
    if not isinstance(text, str):
        return False
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.split("\n")
    return any(not line.strip() for line in lines[1:-1])


def is_segment_body_unit(unit: dict[str, Any]) -> bool:
    unit_type = unit.get("unit_type")
    if unit_type not in {"paragraph", "quote", "list", "continuation"}:
        return False
    unit_id = unit.get("unit_id") if isinstance(unit.get("unit_id"), str) else ""
    semantic_role = unit.get("semantic_role") if isinstance(unit.get("semantic_role"), str) else ""
    return (
        unit.get("display_style") in BOX_BODY_DISPLAY_STYLES
        or "-KEEPER-" in unit_id
        or semantic_role.startswith("keeper_notes")
    )


def validate_semantic_units(units: list[dict[str, Any]]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    seen_unit_ids: set[str] = set()
    unit_ids = {unit.get("unit_id") for unit in units if isinstance(unit.get("unit_id"), str)}
    unit_by_id = {unit.get("unit_id"): unit for unit in units if isinstance(unit.get("unit_id"), str)}
    reading_orders: list[int] = []

    for index, unit in enumerate(units):
        unit_id = unit.get("unit_id") if isinstance(unit.get("unit_id"), str) else f"<unit:{index}>"
        missing = sorted(REQUIRED_FIELDS - set(unit))
        for field in missing:
            findings.append(
                finding(
                    "semantic_unit_schema_missing_required_field",
                    "SU-SCHEMA-001",
                    unit_id,
                    f"Semantic unit is missing required field `{field}`.",
                )
            )

        if unit_id in seen_unit_ids:
            findings.append(
                finding(
                    "duplicate_semantic_unit_id",
                    "SU-ID-001",
                    unit_id,
                    "Semantic unit IDs must be unique within the page review map.",
                )
            )
        seen_unit_ids.add(unit_id)

        if unit.get("schema_version") != SEMANTIC_UNIT_SCHEMA_VERSION:
            findings.append(
                finding(
                    "stale_or_unknown_semantic_schema",
                    "SU-SCHEMA-002",
                    unit_id,
                    "Semantic unit schema version must match the active page-review schema.",
                )
            )
        if unit.get("taxonomy_version") != SEMANTIC_UNIT_TAXONOMY_VERSION:
            findings.append(
                finding(
                    "stale_semantic_taxonomy",
                    "SU-TAXONOMY-001",
                    unit_id,
                    "Semantic unit taxonomy version must match the active page-review taxonomy.",
                )
            )

        unit_type = unit.get("unit_type")
        if unit_type not in UNIT_TYPES:
            findings.append(
                finding("unknown_semantic_unit_type", "SU-TAXONOMY-002", unit_id, "Semantic unit type is not registered.")
            )

        heading_level = unit.get("heading_level")
        if unit_type == "heading":
            if heading_level not in HEADING_LEVELS:
                findings.append(
                    finding(
                        "invalid_heading_level",
                        "SU-HEADING-001",
                        unit_id,
                        "Heading units must use a registered h1-h6 heading level.",
                    )
                )
        elif heading_level is not None:
            findings.append(
                finding(
                    "invalid_heading_level",
                    "SU-HEADING-002",
                    unit_id,
                    "Only heading units may carry heading_level; quote/body/table/art units must keep it null.",
                )
            )

        if unit.get("unit_scope") not in UNIT_SCOPES:
            findings.append(finding("invalid_unit_scope", "SU-SCOPE-001", unit_id, "Semantic unit scope is not registered."))

        if (
            unit_type not in UNIT_TYPES or unit_type in {"unknown_unsupported", "unclassified_bounded_unit"}
        ) and unit.get("unit_scope") not in {
            "unknown",
            "blocked",
        }:
            findings.append(
                finding(
                    "unknown_unit_without_blocker",
                    "SU-SCOPE-002",
                    unit_id,
                    "Unknown or unclassified units must stay in unknown/blocked scope until classified.",
                )
            )

        if unit.get("display_style") not in DISPLAY_STYLES:
            findings.append(
                finding("invalid_display_style", "SU-STYLE-001", unit_id, "Display style is not registered.")
            )
        if unit.get("display_style") in BLOCK_ROLES:
            findings.append(
                finding(
                    "style_is_block_role",
                    "SU-STYLE-002",
                    unit_id,
                    "Display style must describe typography, not source/page block role.",
                )
            )
        if unit.get("source_role") not in SOURCE_ROLES:
            findings.append(
                finding("invalid_source_role", "SU-SOURCE-001", unit_id, "Source role is not registered.")
            )
        if unit.get("block_role") not in BLOCK_ROLES:
            findings.append(finding("invalid_block_role", "SU-BLOCK-001", unit_id, "Block role is not registered."))

        if unit.get("text_source_state") not in TEXT_SOURCE_STATES:
            findings.append(
                finding(
                    "unauthorized_text_source",
                    "SU-EVIDENCE-001",
                    unit_id,
                    "Text source state is not registered for bounded page-review evidence.",
                )
            )

        if (
            unit_type in PARAGRAPH_BOUNDARY_UNIT_TYPES
            and unit.get("unit_scope") == "in_scope_text"
            and contains_embedded_paragraph_boundary(unit.get("text"))
        ):
            findings.append(
                finding(
                    "paragraph_boundary_flattened",
                    "SU-PARA-001",
                    unit_id,
                    "Paragraph and continuation units must not embed multiple visible source paragraphs; split them into separate semantic units or record explicit paragraph-boundary metadata under a separately reviewed contract.",
                )
            )

        if is_segment_body_unit(unit):
            contract = unit.get("semantic_split_contract")
            if not isinstance(contract, dict):
                findings.append(
                    finding(
                        "missing_semantic_split_contract",
                        "SU-SEG-001",
                        unit_id,
                        "Callout/sidebar/card/Keeper body units must declare a semantic_split_contract.",
                    )
                )
            else:
                if contract.get("contract") != "semantic_segmentation_contract.v1":
                    findings.append(
                        finding(
                            "invalid_semantic_split_contract",
                            "SU-SEG-002",
                            unit_id,
                            "semantic_split_contract must use semantic_segmentation_contract.v1.",
                        )
                    )
                if contract.get("boundary_kind") not in BOUNDARY_KINDS:
                    findings.append(
                        finding(
                            "invalid_semantic_split_boundary",
                            "SU-SEG-003",
                            unit_id,
                            "semantic_split_contract boundary_kind is not registered.",
                        )
                    )
                if not isinstance(contract.get("boundary_marker"), str) or not contract.get("boundary_marker"):
                    findings.append(
                        finding(
                            "missing_semantic_split_boundary_marker",
                            "SU-SEG-004",
                            unit_id,
                            "semantic_split_contract must record the boundary marker.",
                        )
                    )

        review_state = unit.get("review_state")
        if review_state is not None and review_state not in REVIEW_STATES:
            findings.append(finding("invalid_review_state", "SU-STATE-001", unit_id, "Review state is not registered."))

        for field in ("source_region_ids", "crop_ids", "span_ids", "evidence_predecessors"):
            if field in unit:
                if not isinstance(unit[field], list):
                    findings.append(
                        finding("invalid_semantic_unit_cardinality", "SU-CARD-001", unit_id, f"`{field}` must be a list.")
                    )
                elif field in {"source_region_ids", "crop_ids", "evidence_predecessors"} and not unit[field]:
                    findings.append(
                        finding("invalid_semantic_unit_cardinality", "SU-CARD-002", unit_id, f"`{field}` must not be empty.")
                    )

        reading_order = unit.get("reading_order")
        if not isinstance(reading_order, int) or reading_order < 1:
            findings.append(
                finding(
                    "invalid_reading_order",
                    "SU-ORDER-001",
                    unit_id,
                    "Semantic unit reading_order must be a positive integer.",
                )
            )
        else:
            reading_orders.append(reading_order)

        layout_role = unit.get("layout_role")
        if layout_role is not None and layout_role not in LAYOUT_ROLES:
            findings.append(finding("invalid_layout_role", "SU-LAYOUT-001", unit_id, "Layout role is not registered."))

        font_style = unit.get("font_style")
        if font_style is not None and font_style not in FONT_STYLES:
            findings.append(finding("invalid_font_style", "SU-LAYOUT-002", unit_id, "Font style is not registered."))

        line_break_after = unit.get("line_break_after")
        if line_break_after is not None and not isinstance(line_break_after, bool) and line_break_after != "unknown":
            findings.append(
                finding(
                    "invalid_line_break_after",
                    "SU-LAYOUT-003",
                    unit_id,
                    "`line_break_after` must be true, false, or unknown.",
                )
            )

        for link_field in ("parent_unit_id", "container_unit_id", "continues_from", "continues_to", "continues_inline_to"):
            linked = unit.get(link_field)
            if linked is not None and not isinstance(linked, str):
                findings.append(
                    finding(
                        "invalid_semantic_unit_link_type",
                        "SU-LINK-002",
                        unit_id,
                        f"`{link_field}` must be a scalar semantic unit id.",
                    )
                )
            elif linked is not None and linked not in unit_ids:
                findings.append(
                    finding(
                        "missing_semantic_unit_link",
                        "SU-LINK-001",
                        unit_id,
                        f"`{link_field}` points to an unknown semantic unit.",
                    )
                )

        if unit_type == "table_row":
            parent = unit_by_id.get(unit.get("parent_unit_id"))
            if parent is None or parent.get("unit_type") != "table":
                findings.append(
                    finding(
                        "table_structure_flattened",
                        "SU-TOPO-001",
                        unit_id,
                        "Table rows must link to a table parent unit.",
                    )
                )
        if unit_type == "table_cell":
            parent = unit_by_id.get(unit.get("parent_unit_id"))
            container = unit_by_id.get(unit.get("container_unit_id"))
            if parent is None or parent.get("unit_type") != "table_row" or container is None or container.get("unit_type") != "table":
                findings.append(
                    finding(
                        "table_structure_flattened",
                        "SU-TOPO-002",
                        unit_id,
                        "Table cells must link to a table-row parent and table container.",
                    )
                )
        if unit_type in {"stat_label", "stat_value"}:
            parent = unit_by_id.get(unit.get("parent_unit_id"))
            if parent is None or parent.get("unit_type") != "stat_block":
                findings.append(
                    finding(
                        "stat_block_flattened",
                        "SU-TOPO-003",
                        unit_id,
                        "Stat labels and values must link to a stat-block parent.",
                    )
                )

    children_by_parent: dict[str, list[dict[str, Any]]] = {}
    for unit in units:
        parent_unit_id = unit.get("parent_unit_id")
        if isinstance(parent_unit_id, str):
            children_by_parent.setdefault(parent_unit_id, []).append(unit)
    for unit in units:
        unit_id = unit.get("unit_id") if isinstance(unit.get("unit_id"), str) else None
        unit_type = unit.get("unit_type")
        if unit_type in {"callout", "sidebar", "card"} and not children_by_parent.get(unit_id or ""):
            findings.append(
                finding(
                    "callout_container_unresolved",
                    "SU-TOPO-004",
                    unit_id,
                    "Callout, sidebar, and card containers must expose linked child content units.",
                )
            )

    if reading_orders and sorted(reading_orders) != list(range(1, len(reading_orders) + 1)):
        findings.append(
            finding(
                "invalid_reading_order_sequence",
                "SU-ORDER-002",
                None,
                "Semantic unit reading_order values must be unique and contiguous from 1.",
            )
        )

    blocker_count = sum(1 for item in findings if item["severity"] == "blocker" and item["waiver"] == "non_waivable")
    return {
        "schema_version": SEMANTIC_UNIT_SCHEMA_VERSION,
        "taxonomy_version": SEMANTIC_UNIT_TAXONOMY_VERSION,
        "unit_count": len(units),
        "valid": blocker_count == 0,
        "readiness_blocked": blocker_count > 0,
        "findings": findings,
    }


def validate_text_evidence_crop_links(
    units: list[dict[str, Any]], crop_role_by_id: dict[str, str]
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for unit in units:
        unit_id = unit.get("unit_id") if isinstance(unit.get("unit_id"), str) else None
        if unit.get("unit_scope") != "in_scope_text":
            continue
        crop_ids = unit.get("crop_ids")
        if not isinstance(crop_ids, list) or not crop_ids:
            findings.append(
                finding(
                    "missing_text_evidence_crop_link",
                    "SU-CROP-001",
                    unit_id,
                    "In-scope text semantic units must link to OCR/text evidence crop ids.",
                )
            )
            continue
        invalid = [crop_id for crop_id in crop_ids if crop_role_by_id.get(crop_id) not in TEXT_EVIDENCE_CROP_ROLES]
        if invalid:
            findings.append(
                finding(
                    "invalid_text_evidence_crop_role",
                    "SU-CROP-002",
                    unit_id,
                    "Human-review or unknown crops cannot satisfy OCR/text evidence linkage.",
                )
            )
    blocker_count = sum(1 for item in findings if item["severity"] == "blocker" and item["waiver"] == "non_waivable")
    return {"valid": blocker_count == 0, "readiness_blocked": blocker_count > 0, "findings": findings}


def semantic_map_document(
    *,
    page: str,
    package_id: str,
    map_id: str,
    units: list[dict[str, Any]],
    source: str,
) -> dict[str, Any]:
    validation = validate_semantic_units(units)
    return {
        "map_id": map_id,
        "package_id": package_id,
        "page": page,
        "schema_version": SEMANTIC_UNIT_SCHEMA_VERSION,
        "taxonomy_version": SEMANTIC_UNIT_TAXONOMY_VERSION,
        "canonical": True,
        "source": source,
        "units": sorted(units, key=lambda unit: unit["reading_order"] if isinstance(unit.get("reading_order"), int) else 0),
        "semantic_validation": validation,
        "structural_findings": validation["findings"],
        "not_evidence_for": NOT_EVIDENCE_FOR,
    }


def markdown_table_cell(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\r\n", " ").replace("\n", " ").replace("|", "\\|")
    return " ".join(text.split())


def unit_link_text(unit: dict[str, Any]) -> str:
    links = []
    for field in ("parent_unit_id", "container_unit_id", "continues_from", "continues_to", "continues_inline_to"):
        if unit.get(field):
            links.append(f"{field}={unit[field]}")
    return "; ".join(links)


def markdown_optional_unit_metadata(unit: dict[str, Any]) -> list[str]:
    rows = []
    optional_fields = [
        ("Heading level", "heading_level"),
        ("Layout role", "layout_role"),
        ("Font style", "font_style"),
        ("Line break after", "line_break_after"),
        ("Continues inline to", "continues_inline_to"),
    ]
    for label, field in optional_fields:
        if field not in unit:
            continue
        value = unit.get(field)
        if isinstance(value, bool):
            value = str(value).lower()
        elif value is None:
            value = "none"
        rows.append(f"- {label}: `{value}`")
    return rows


def markdown_fence_for_text(text: str) -> str:
    longest_run = 0
    current_run = 0
    for character in text:
        if character == "`":
            current_run += 1
            longest_run = max(longest_run, current_run)
        else:
            current_run = 0
    return "`" * max(3, longest_run + 1)


def build_semantic_map_markdown(document: dict[str, Any]) -> str:
    lines = [
        f"# Semantic Text Map - Page {document['page']}",
        "",
        f"Map: `{document['map_id']}`",
        f"Package: `{document['package_id']}`",
        f"Schema: `{document['schema_version']}`",
        f"Taxonomy: `{document['taxonomy_version']}`",
        f"Validation: `{'valid' if document['semantic_validation']['valid'] else 'blocked'}`",
        "",
        "## Unit Summary",
        "",
        "| Order | Unit ID | Type | Scope | Heading | Layout | Font | Line break after | Style | Source role | Block role | Review state | Links |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for unit in document["units"]:
        row = [
            unit.get("reading_order"),
            unit.get("unit_id"),
            unit.get("unit_type"),
            unit.get("unit_scope"),
            unit.get("heading_level"),
            unit.get("layout_role"),
            unit.get("font_style"),
            unit.get("line_break_after"),
            unit.get("display_style"),
            unit.get("source_role"),
            unit.get("block_role"),
            unit.get("review_state"),
            unit_link_text(unit),
        ]
        lines.append("| " + " | ".join(markdown_table_cell(item) for item in row) + " |")

    lines.extend(["", "## Unit Text", ""])
    for unit in document["units"]:
        text = unit.get("text") or ""
        fence = markdown_fence_for_text(text)
        lines.extend(
            [
                f"### {unit.get('unit_id')}",
                "",
                f"- Type: `{unit.get('unit_type')}`",
                f"- Scope: `{unit.get('unit_scope')}`",
                f"- Text source: `{unit.get('text_source_state')}`",
                *markdown_optional_unit_metadata(unit),
                "",
                f"{fence}text",
                text,
                fence,
                "",
            ]
        )

    lines.extend(["## Structural Findings", ""])
    findings = document["structural_findings"]
    if findings:
        for item in findings:
            lines.append(
                f"- `{item['finding_id']}` / `{item['rule_id']}` / `{item['severity']}` / `{item['waiver']}`"
                f" / `{item['unit_id']}`: {item['message']}"
            )
    else:
        lines.append("- None.")

    lines.extend(["", "## Not Evidence For", ""])
    for item in document["not_evidence_for"]:
        lines.append(f"- `{item}`")
    lines.append("")
    return "\n".join(lines)


def validate_semantic_map_markdown(markdown: str, expected_unit_count: int) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    lines = markdown.splitlines()
    try:
        summary_start = lines.index("## Unit Summary")
    except ValueError:
        summary_start = -1
    try:
        summary_end = lines.index("## Unit Text")
    except ValueError:
        summary_end = len(lines)
    if summary_start < 0 or summary_end <= summary_start:
        summary_lines: list[str] = []
    else:
        summary_lines = lines[summary_start:summary_end]
    summary_rows = [line for line in summary_lines if line.startswith("| ") and line.endswith(" |")]
    data_rows = [line for line in summary_rows if not line.startswith("| Order ") and not line.startswith("|---")]
    for line in data_rows:
        cells = line.strip("|").split(" | ")
        if len(cells) != 13:
            findings.append(
                finding(
                    "markdown_table_integrity_failed",
                    "SU-MD-001",
                    None,
                    "Semantic map summary table row has an unexpected column count.",
                )
            )
        if any(len(cell) > 120 for cell in cells):
            findings.append(
                finding(
                    "markdown_table_contains_long_prose",
                    "SU-MD-002",
                    None,
                    "Semantic map summary table must contain metadata only, not long prose.",
                )
            )
    if len(data_rows) != expected_unit_count:
        findings.append(
            finding(
                "markdown_unit_row_count_mismatch",
                "SU-MD-003",
                None,
                "Semantic map summary table row count must match semantic unit count.",
            )
        )
    try:
        unit_text_start = lines.index("## Unit Text")
    except ValueError:
        unit_text_start = -1
    try:
        unit_text_end = lines.index("## Structural Findings")
    except ValueError:
        unit_text_end = len(lines)
    if unit_text_start < 0 or unit_text_end <= unit_text_start:
        unit_text_lines: list[str] = []
    else:
        unit_text_lines = lines[unit_text_start:unit_text_end]

    fenced_text_blocks = 0
    in_fence = False
    current_fence = ""
    malformed_fence = False
    for line in unit_text_lines:
        if not in_fence and line.endswith("text") and set(line[:-4]) == {"`"} and len(line[:-4]) >= 3:
            in_fence = True
            current_fence = line[:-4]
            fenced_text_blocks += 1
            continue
        if in_fence and line == current_fence:
            in_fence = False
            current_fence = ""
    if in_fence:
        malformed_fence = True
    if fenced_text_blocks != expected_unit_count or malformed_fence:
        findings.append(
            finding(
                "markdown_unit_text_block_count_mismatch",
                "SU-MD-004",
                None,
                "Semantic map must include one fenced text block per semantic unit.",
            )
        )
    blocker_count = sum(1 for item in findings if item["severity"] == "blocker" and item["waiver"] == "non_waivable")
    return {"valid": blocker_count == 0, "readiness_blocked": blocker_count > 0, "findings": findings}


def reconcile_page_inventory(regions: list[dict[str, Any]], units: list[dict[str, Any]]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    region_ids = {region.get("region_id") for region in regions if isinstance(region.get("region_id"), str)}
    units_by_region: dict[str, list[dict[str, Any]]] = {region_id: [] for region_id in region_ids}

    for unit in units:
        unit_id = unit.get("unit_id") if isinstance(unit.get("unit_id"), str) else None
        source_region_ids = unit.get("source_region_ids")
        if not isinstance(source_region_ids, list):
            continue
        for region_id in source_region_ids:
            if region_id not in region_ids:
                findings.append(
                    finding(
                        "semantic_unit_region_not_in_inventory",
                        "SU-RECON-001",
                        unit_id,
                        "Semantic unit references a source region that is not in the page inventory.",
                    )
                )
            else:
                units_by_region[region_id].append(unit)

    for region in regions:
        region_id = region.get("region_id")
        if not isinstance(region_id, str):
            findings.append(
                finding(
                    "invalid_region_inventory_record",
                    "SU-RECON-002",
                    None,
                    "Every inventory region must have a stable string region_id.",
                )
            )
            continue

        decision = region.get("decision")
        if decision not in REGION_DECISIONS:
            findings.append(
                finding(
                    "context_only_decision_missing",
                    "SU-RECON-003",
                    None,
                    "Every inventory region must resolve to represented, absent, context_only, visual_only, excluded, unknown, or blocked.",
                )
            )
            continue

        region_units = units_by_region.get(region_id, [])
        expected_unit_types = set(region.get("expected_unit_types", []))
        representing_units = []
        for unit in region_units:
            unit_type = unit.get("unit_type")
            unit_scope = unit.get("unit_scope")
            if unit_type in UNKNOWN_UNIT_TYPES:
                continue
            if unit_scope == "in_scope_text":
                representing_units.append(unit)
            elif unit_scope in {"context_only", "visual_only"} and unit_type in expected_unit_types:
                representing_units.append(unit)
        in_scope_text_units = [unit for unit in region_units if unit.get("unit_scope") == "in_scope_text"]
        if decision == "represented" and not representing_units:
            findings.append(
                finding(
                    "unrepresented_structural_unit",
                    "SU-RECON-004",
                    None,
                    "Represented inventory region has no semantic unit.",
                )
            )
        if decision in {"absent", "excluded"} and region_units:
            findings.append(
                finding(
                    "context_only_decision_conflicts_with_units",
                    "SU-RECON-005",
                    None,
                    "Absent/excluded region must not carry semantic units.",
                )
            )
        if decision in {"context_only", "visual_only"} and in_scope_text_units:
            findings.append(
                finding(
                    "context_only_decision_conflicts_with_units",
                    "SU-RECON-005",
                    None,
                    "Context/visual-only region must not carry in-scope text semantic units.",
                )
            )
        if decision in {"unknown", "blocked"}:
            unknown_units = [unit for unit in region_units if unit.get("unit_type") in UNKNOWN_UNIT_TYPES]
            if not unknown_units:
                findings.append(
                    finding(
                        "unknown_region_without_blocking_unit",
                        "SU-RECON-006",
                        None,
                        "Unknown or blocked inventory region must have an unknown/unclassified semantic unit.",
                    )
                )
            if representing_units:
                findings.append(
                    finding(
                        "unknown_region_conflicts_with_represented_units",
                        "SU-RECON-008",
                        None,
                        "Unknown or blocked inventory region must not also contain classified in-scope text units.",
                    )
                )

        represented_unit_types = {unit.get("unit_type") for unit in representing_units}
        missing_unit_types = expected_unit_types - represented_unit_types
        if expected_unit_types and len(expected_unit_types) > 1 and len(representing_units) == 1:
            findings.append(
                finding(
                    "collapsed_units",
                    "SU-RECON-009",
                    None,
                    "Region expects multiple semantic unit types but is represented by a single unit.",
                )
            )
        if "heading" in missing_unit_types:
            findings.append(
                finding(
                    "missing_expected_heading",
                    "SU-RECON-010",
                    None,
                    "Represented inventory region is missing an expected heading unit.",
                )
            )
        if "quote" in missing_unit_types:
            findings.append(
                finding(
                    "quote_flattened",
                    "SU-RECON-011",
                    None,
                    "Represented inventory region is missing an expected quote unit.",
                )
            )
        if expected_unit_types and missing_unit_types:
            findings.append(
                finding(
                    "missing_expected_unit_type",
                    "SU-RECON-007",
                    None,
                    "Represented inventory region is missing one or more expected semantic unit types.",
                )
            )

    blocker_count = sum(1 for item in findings if item["severity"] == "blocker" and item["waiver"] == "non_waivable")
    return {
        "region_count": len(regions),
        "unit_count": len(units),
        "valid": blocker_count == 0,
        "readiness_blocked": blocker_count > 0,
        "findings": findings,
    }
