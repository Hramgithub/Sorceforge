import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.page_review_semantic_units import (  # noqa: E402
    SEMANTIC_UNIT_SCHEMA_VERSION,
    SEMANTIC_UNIT_TAXONOMY_VERSION,
    build_semantic_map_markdown,
    keeper_notes_callout_heading_level,
    reconcile_page_inventory,
    semantic_map_document,
    validate_text_evidence_crop_links,
    validate_semantic_map_markdown,
    validate_semantic_units,
)
from scripts.semantic_segmentation_contract import callout_body_contract  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_complete_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P002_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p002_G1_VIRAL_001"
P002_REPORT = P002_OUT_ROOT / "page_complete_review_report.json"
P002_PACKET = P002_OUT_ROOT / "page_complete_review_packet.md"


def test_keeper_notes_callout_heading_level_is_h4_only():
    assert keeper_notes_callout_heading_level() == "h4"
P002_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P002-001"
P003_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p003_G1_VIRAL_001"
P003_REPORT = P003_OUT_ROOT / "page_complete_review_report.json"
P003_PACKET = P003_OUT_ROOT / "page_complete_review_packet.md"
P003_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P003-001"
P004_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p004_G1_VIRAL_001"
P004_REPORT = P004_OUT_ROOT / "page_complete_review_report.json"
P004_PACKET = P004_OUT_ROOT / "page_complete_review_packet.md"
P004_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P004-001"
P005_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_001"
P005_REPORT = P005_OUT_ROOT / "page_complete_review_report.json"
P005_PACKET = P005_OUT_ROOT / "page_complete_review_packet.md"
P005_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-001"
P005_002_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_002"
P005_002_REPORT = P005_002_OUT_ROOT / "page_complete_review_report.json"
P005_002_PACKET = P005_002_OUT_ROOT / "page_complete_review_packet.md"
P005_002_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-002"
P005_003_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_003"
P005_003_REPORT = P005_003_OUT_ROOT / "page_complete_review_report.json"
P005_003_PACKET = P005_003_OUT_ROOT / "page_complete_review_packet.md"
P005_003_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-003"
P005_004_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_004"
P005_004_REPORT = P005_004_OUT_ROOT / "page_complete_review_report.json"
P005_004_PACKET = P005_004_OUT_ROOT / "page_complete_review_packet.md"
P005_004_SEMANTIC_MAP_JSON = P005_004_OUT_ROOT / "review_assets" / "page_005_semantic_text_map.json"
P005_004_SEMANTIC_MAP_MARKDOWN = P005_004_OUT_ROOT / "review_assets" / "page_005_semantic_text_map.md"
P005_004_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P005-004"
P006_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p006_G1_VIRAL_001"
P006_REPORT = P006_OUT_ROOT / "page_complete_review_report.json"
P006_PACKET = P006_OUT_ROOT / "page_complete_review_packet.md"
P006_SUMMARY = P006_OUT_ROOT / "page_complete_review_summary.md"
P006_SEMANTIC_MAP_JSON = P006_OUT_ROOT / "review_assets" / "page_006_semantic_text_map.json"
P006_SEMANTIC_MAP_MARKDOWN = P006_OUT_ROOT / "review_assets" / "page_006_semantic_text_map.md"
P006_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-001"
P006_002_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p006_G1_VIRAL_002"
P006_002_REPORT = P006_002_OUT_ROOT / "page_complete_review_report.json"
P006_002_PACKET = P006_002_OUT_ROOT / "page_complete_review_packet.md"
P006_002_SUMMARY = P006_002_OUT_ROOT / "page_complete_review_summary.md"
P006_002_TEXT_MAP = P006_002_OUT_ROOT / "review_assets" / "page_006_ocr_verified_text_map.md"
P006_002_SEMANTIC_MAP_JSON = P006_002_OUT_ROOT / "review_assets" / "page_006_semantic_text_map.json"
P006_002_SEMANTIC_MAP_MARKDOWN = P006_002_OUT_ROOT / "review_assets" / "page_006_semantic_text_map.md"
P006_002_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P006-002"
P007_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p007_G1_VIRAL_003"
P007_REPORT = P007_OUT_ROOT / "page_complete_review_report.json"
P007_PACKET = P007_OUT_ROOT / "page_complete_review_packet.md"
P007_TEXT_MAP = P007_OUT_ROOT / "review_assets" / "page_007_ocr_verified_text_map.md"
P007_SEMANTIC_MAP_JSON = P007_OUT_ROOT / "review_assets" / "page_007_semantic_text_map.json"
P007_SEMANTIC_MAP_MARKDOWN = P007_OUT_ROOT / "review_assets" / "page_007_semantic_text_map.md"
P007_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P007-003"
P008_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p008_G1_VIRAL_001"
P008_REPORT = P008_OUT_ROOT / "page_complete_review_report.json"
P008_PACKET = P008_OUT_ROOT / "page_complete_review_packet.md"
P008_TEXT_MAP = P008_OUT_ROOT / "review_assets" / "page_008_ocr_verified_text_map.md"
P008_SEMANTIC_MAP_JSON = P008_OUT_ROOT / "review_assets" / "page_008_semantic_text_map.json"
P008_SEMANTIC_MAP_MARKDOWN = P008_OUT_ROOT / "review_assets" / "page_008_semantic_text_map.md"
P008_ACTION_BACKLOG = P008_OUT_ROOT / "review_assets" / "page_008_action_backlog.md"
P008_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P008-001"
P001_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p001_G1_VIRAL_001"
P001_REPORT = P001_OUT_ROOT / "page_complete_review_report.json"
P001_PACKET = P001_OUT_ROOT / "page_complete_review_packet.md"
P001_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P001-001"
P009_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p009_G1_VIRAL_001"
P009_REPORT = P009_OUT_ROOT / "page_complete_review_report.json"
P009_PACKET = P009_OUT_ROOT / "page_complete_review_packet.md"
P009_TEXT_MAP = P009_OUT_ROOT / "review_assets" / "page_009_ocr_verified_text_map.md"
P009_SEMANTIC_MAP_JSON = P009_OUT_ROOT / "review_assets" / "page_009_semantic_text_map.json"
P009_SEMANTIC_MAP_MARKDOWN = P009_OUT_ROOT / "review_assets" / "page_009_semantic_text_map.md"
P009_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P009-001"
P010_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p010_G1_VIRAL_001"
P010_REPORT = P010_OUT_ROOT / "page_complete_review_report.json"
P010_PACKET = P010_OUT_ROOT / "page_complete_review_packet.md"
P010_TEXT_MAP = P010_OUT_ROOT / "review_assets" / "page_010_ocr_verified_text_map.md"
P010_SEMANTIC_MAP_JSON = P010_OUT_ROOT / "review_assets" / "page_010_semantic_text_map.json"
P010_SEMANTIC_MAP_MARKDOWN = P010_OUT_ROOT / "review_assets" / "page_010_semantic_text_map.md"
P010_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P010-001"
P011_OUT_ROOT = TRIAL_ROOT / "page_complete_review_p011_G1_VIRAL_001"
P011_REPORT = P011_OUT_ROOT / "page_complete_review_report.json"
P011_PACKET = P011_OUT_ROOT / "page_complete_review_packet.md"
P011_TEXT_MAP = P011_OUT_ROOT / "review_assets" / "page_011_ocr_verified_text_map.md"
P011_SEMANTIC_MAP_JSON = P011_OUT_ROOT / "review_assets" / "page_011_semantic_text_map.json"
P011_SEMANTIC_MAP_MARKDOWN = P011_OUT_ROOT / "review_assets" / "page_011_semantic_text_map.md"
P011_AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P011-001"


def semantic_unit(**overrides):
    unit = {
        "unit_id": "SU-G1-VIRAL-P006-001",
        "schema_version": SEMANTIC_UNIT_SCHEMA_VERSION,
        "taxonomy_version": SEMANTIC_UNIT_TAXONOMY_VERSION,
        "unit_type": "heading",
        "unit_scope": "in_scope_text",
        "reading_order": 1,
        "source_region_ids": ["PRM-G1-VIRAL-001-P006-R02"],
        "crop_ids": ["P006-001-ATT-CROP-TITLE"],
        "evidence_predecessors": ["PCRP-G1-VIRAL-P006-001"],
        "text_source_state": "human_verified",
        "text": "Introduction",
        "heading_level": "h2",
        "display_style": "section_heading",
        "source_role": "human_verified_span",
        "block_role": "title_region",
        "source_block_id": "P006-B001",
        "span_ids": ["P006-B001-S001"],
        "review_state": "ready_for_review",
    }
    unit.update(overrides)
    if (
        unit.get("unit_type") in {"paragraph", "quote", "list", "continuation"}
        and unit.get("display_style") in {"callout_body", "sidebar_body", "card_body"}
        and "semantic_split_contract" not in unit
    ):
        unit["semantic_split_contract"] = callout_body_contract(callout_heading="Synthetic Box")
    return unit


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_semantic_unit_contract_accepts_versioned_heading_unit():
    result = validate_semantic_units([semantic_unit()])

    assert result["schema_version"] == SEMANTIC_UNIT_SCHEMA_VERSION
    assert result["taxonomy_version"] == SEMANTIC_UNIT_TAXONOMY_VERSION
    assert result["valid"] is True
    assert result["readiness_blocked"] is False
    assert result["findings"] == []


def test_semantic_unit_contract_rejects_quote_heading_level():
    result = validate_semantic_units(
        [
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-QUOTE-001",
                unit_type="quote",
                text='"We are the Spektral Krew..." - Marco Proudfoot',
                heading_level="quote",
                display_style="pull_quote",
            )
        ]
    )

    assert result["valid"] is False
    assert result["readiness_blocked"] is True
    assert any(finding["finding_id"] == "invalid_heading_level" for finding in result["findings"])


def test_semantic_unit_contract_requires_blocked_unknown_fallback():
    result = validate_semantic_units(
        [
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-UNKNOWN-001",
                unit_type="unknown_unsupported",
                unit_scope="in_scope_text",
                heading_level=None,
                text_source_state="not_applicable",
            )
        ]
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "unknown_unit_without_blocker" for finding in result["findings"])


def test_semantic_unit_contract_blocks_unregistered_unit_type_without_unknown_scope():
    result = validate_semantic_units(
        [
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-UNREGISTERED-001",
                unit_type="decorative_pull_panel",
                unit_scope="in_scope_text",
                heading_level=None,
                display_style="unknown",
                source_role="unknown",
                block_role="unknown_region",
                text_source_state="not_applicable",
            )
        ]
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["valid"] is False
    assert "unknown_semantic_unit_type" in finding_ids
    assert "unknown_unit_without_blocker" in finding_ids


def test_semantic_unit_contract_blocks_display_style_leaking_block_role():
    result = validate_semantic_units(
        [
            semantic_unit(
                display_style="text_column",
                block_role="text_column",
            )
        ]
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["readiness_blocked"] is True
    assert "invalid_display_style" in finding_ids
    assert "style_is_block_role" in finding_ids


def test_semantic_unit_contract_validates_continuation_links():
    result = validate_semantic_units(
        [
            semantic_unit(unit_id="SU-G1-VIRAL-P006-OVERVIEW-L", heading_level=None, unit_type="paragraph", continues_to="missing"),
        ]
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "missing_semantic_unit_link" for finding in result["findings"])


def test_semantic_unit_contract_blocks_embedded_paragraph_boundaries():
    result = validate_semantic_units(
        [
            semantic_unit(
                unit_id="SU-G1-VIRAL-P007-BODY-FLATTENED",
                heading_level=None,
                unit_type="paragraph",
                text="The first source paragraph ends here.\n\nThe next source paragraph starts here.",
            )
        ]
    )

    findings = result["findings"]
    assert result["valid"] is False
    assert result["readiness_blocked"] is True
    assert any(finding["finding_id"] == "paragraph_boundary_flattened" for finding in findings)
    assert any(finding["rule_id"] == "SU-PARA-001" for finding in findings)


def test_semantic_unit_contract_rejects_list_valued_links_without_crashing():
    result = validate_semantic_units(
        [
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-OVERVIEW-L",
                heading_level=None,
                unit_type="paragraph",
                continues_to=["SU-G1-VIRAL-P006-OVERVIEW-R"],
            ),
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-OVERVIEW-R",
                heading_level=None,
                unit_type="paragraph",
                reading_order=2,
                continues_from="SU-G1-VIRAL-P006-OVERVIEW-L",
            ),
        ]
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "invalid_semantic_unit_link_type" for finding in result["findings"])


def test_semantic_unit_contract_requires_non_empty_evidence_lists():
    result = validate_semantic_units(
        [
            semantic_unit(
                source_region_ids=[],
                crop_ids=[],
                evidence_predecessors=[],
            )
        ]
    )

    assert result["valid"] is False
    findings = [finding for finding in result["findings"] if finding["finding_id"] == "invalid_semantic_unit_cardinality"]
    assert {finding["rule_id"] for finding in findings} == {"SU-CARD-002"}


def test_semantic_text_units_require_text_evidence_crop_roles():
    result = validate_text_evidence_crop_links(
        [semantic_unit(crop_ids=["P009-B003-HUMAN"])],
        {"P009-B003-HUMAN": "human_review_crop"},
    )

    assert result["valid"] is False
    assert result["readiness_blocked"] is True
    assert any(finding["finding_id"] == "invalid_text_evidence_crop_role" for finding in result["findings"])


def test_semantic_text_units_accept_ocr_and_text_evidence_crop_roles():
    result = validate_text_evidence_crop_links(
        [semantic_unit(crop_ids=["P009-B003-OCR", "P009-B003-TEXT"])],
        {"P009-B003-OCR": "ocr_candidate_crop", "P009-B003-TEXT": "text_evidence_crop"},
    )

    assert result["valid"] is True
    assert result["readiness_blocked"] is False
    assert result["findings"] == []


def test_semantic_unit_contract_requires_contiguous_reading_order():
    result = validate_semantic_units(
        [
            semantic_unit(unit_id="SU-G1-VIRAL-P006-A", reading_order=1),
            semantic_unit(unit_id="SU-G1-VIRAL-P006-B", reading_order=1),
        ]
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "invalid_reading_order_sequence" for finding in result["findings"])


def test_semantic_map_document_is_canonical_json_not_markdown_source():
    units = [
        semantic_unit(unit_id="SU-G1-VIRAL-P006-TITLE", reading_order=1),
        semantic_unit(
            unit_id="SU-G1-VIRAL-P006-QUOTE",
            reading_order=2,
            unit_type="quote",
            heading_level=None,
            display_style="pull_quote",
            block_role="text_column",
            text='"We are the Spektral Krew, and we go places and do things you would never do." - Marco Proudfoot',
        ),
    ]

    document = semantic_map_document(
        page="006",
        package_id="PCRP-G1-VIRAL-P006-002",
        map_id="SM-G1-VIRAL-P006-002",
        units=units,
        source="unit_test",
    )

    assert document["canonical"] is True
    assert document["semantic_validation"]["valid"] is True
    assert document["structural_findings"] == []
    assert document["not_evidence_for"] == [
        "source_acceptance",
        "ocr_acceptance",
        "pdf_text_extraction",
        "render_acceptance",
        "fixture_admission",
        "page_complete_acceptance",
        "whole_gate_acceptance",
    ]


def test_semantic_map_markdown_uses_metadata_table_and_per_unit_text_blocks():
    long_body = (
        "Producers of a popular ghost hunting YouTube channel called Spektral Krew are planning to illegally visit "
        "Isola di Malamente | an island off the coast of Sicily to broadcast live as they attempt to uncover evidence."
    )
    document = semantic_map_document(
        page="006",
        package_id="PCRP-G1-VIRAL-P006-002",
        map_id="SM-G1-VIRAL-P006-002",
        source="unit_test",
        units=[
            semantic_unit(unit_id="SU-G1-VIRAL-P006-INTRO", reading_order=1),
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-BODY",
                reading_order=2,
                unit_type="paragraph",
                heading_level=None,
                display_style="body",
                block_role="text_column",
                text=long_body,
                continues_to="SU-G1-VIRAL-P006-BODY-R",
            ),
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-BODY-R",
                reading_order=3,
                unit_type="continuation",
                heading_level=None,
                display_style="body",
                block_role="text_column",
                text="Age, offering countless sacrifices over the millennia.",
                continues_from="SU-G1-VIRAL-P006-BODY",
            ),
        ],
    )

    markdown = build_semantic_map_markdown(document)
    projection = validate_semantic_map_markdown(markdown, expected_unit_count=3)

    assert projection["valid"] is True
    assert "| 2 | SU-G1-VIRAL-P006-BODY | paragraph | in_scope_text |  |  |  |  | body |" in markdown
    assert "Isola di Malamente \\| an island" not in markdown.split("## Unit Summary", 1)[1].split("## Unit Text", 1)[0]
    assert long_body in markdown
    assert markdown.count("```text") == 3
    assert "- `page_complete_acceptance`" in markdown


def test_semantic_map_markdown_validator_rejects_long_prose_table_cells():
    markdown = "\n".join(
            [
                "# Semantic Text Map - Page 006",
                "",
                "## Unit Summary",
                "",
                "| Order | Unit ID | Type | Scope | Heading | Layout | Font | Line break after | Style | Source role | Block role | Review state | Links |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
                "| 1 | SU | paragraph | in_scope_text |  |  |  |  | body | human_verified_span | text_column | ready_for_review | "
                + ("long prose " * 20)
                + " |",
                "",
                "## Unit Text",
                "",
                "```text",
                "full text",
                "```",
        ]
    )

    result = validate_semantic_map_markdown(markdown, expected_unit_count=1)

    assert result["valid"] is False
    assert any(finding["finding_id"] == "markdown_table_contains_long_prose" for finding in result["findings"])


def test_semantic_map_markdown_validator_ignores_table_like_fenced_text():
    document = semantic_map_document(
        page="006",
        package_id="PCRP-G1-VIRAL-P006-002",
        map_id="SM-G1-VIRAL-P006-002",
        source="unit_test",
        units=[
            semantic_unit(
                text="This full text may include a table-like line:\n| label | value |\n|---|---|\n| Taint | active |",
            )
        ],
    )

    markdown = build_semantic_map_markdown(document)
    result = validate_semantic_map_markdown(markdown, expected_unit_count=1)

    assert result["valid"] is True
    assert "| Taint | active |" in markdown


def test_semantic_map_markdown_uses_longer_fence_when_text_contains_backticks():
    document = semantic_map_document(
        page="006",
        package_id="PCRP-G1-VIRAL-P006-002",
        map_id="SM-G1-VIRAL-P006-002",
        source="unit_test",
        units=[semantic_unit(text="The raw text contains ``` inside it.")],
    )

    markdown = build_semantic_map_markdown(document)
    result = validate_semantic_map_markdown(markdown, expected_unit_count=1)

    assert result["valid"] is True
    assert "````text" in markdown


def test_semantic_map_markdown_validator_rejects_unclosed_fence():
    markdown = "\n".join(
        [
            "# Semantic Text Map - Page 006",
            "",
            "## Unit Summary",
            "",
            "| Order | Unit ID | Type | Scope | Heading | Layout | Font | Line break after | Style | Source role | Block role | Review state | Links |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
            "| 1 | SU | paragraph | in_scope_text |  |  |  |  | body | human_verified_span | text_column | ready_for_review | |",
            "",
            "## Unit Text",
            "",
            "```text",
            "full text",
        ]
    )

    result = validate_semantic_map_markdown(markdown, expected_unit_count=1)

    assert result["valid"] is False
    assert any(finding["finding_id"] == "markdown_unit_text_block_count_mismatch" for finding in result["findings"])


def test_semantic_map_markdown_validator_ignores_stray_fences_outside_unit_text():
    markdown = "\n".join(
        [
            "# Semantic Text Map - Page 006",
            "",
            "```text",
            "stray text before the unit section",
            "```",
            "",
            "## Unit Summary",
            "",
            "| Order | Unit ID | Type | Scope | Heading | Layout | Font | Line break after | Style | Source role | Block role | Review state | Links |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
            "| 1 | SU | paragraph | in_scope_text |  |  |  |  | body | human_verified_span | text_column | ready_for_review | |",
            "",
            "## Unit Text",
            "",
            "## Structural Findings",
            "",
            "- None.",
        ]
    )

    result = validate_semantic_map_markdown(markdown, expected_unit_count=1)

    assert result["valid"] is False
    assert any(finding["finding_id"] == "markdown_unit_text_block_count_mismatch" for finding in result["findings"])


def test_semantic_units_support_inline_layout_hints_in_markdown():
    document = semantic_map_document(
        page="011",
        package_id="P011SEM-G1-VIRAL-001",
        map_id="SM-G1-VIRAL-P011-001",
        source="unit_test",
        units=[
            semantic_unit(
                unit_id="SU-P011-EMILY-003",
                unit_type="heading",
                reading_order=1,
                text="Super Fan Option.",
                heading_level="h3",
                display_style="section_heading",
                layout_role="inline_heading",
                font_style="italic",
                line_break_after=False,
                continues_inline_to="SU-P011-EMILY-004",
            ),
            semantic_unit(
                unit_id="SU-P011-EMILY-004",
                unit_type="paragraph",
                reading_order=2,
                text="Em is a stalker super fan of the channel.",
                heading_level=None,
                display_style="body",
                layout_role="body",
                font_style="normal",
            ),
        ],
    )

    markdown = build_semantic_map_markdown(document)
    result = validate_semantic_map_markdown(markdown, expected_unit_count=2)

    assert result["valid"] is True
    assert "| 1 | SU-P011-EMILY-003 | heading | in_scope_text | h3 | inline_heading | italic | False | section_heading |" in markdown
    assert "continues_inline_to=SU-P011-EMILY-004" in markdown
    assert "- Heading level: `h3`" in markdown
    assert "- Layout role: `inline_heading`" in markdown
    assert "- Font style: `italic`" in markdown
    assert "- Line break after: `false`" in markdown
    assert "- Continues inline to: `SU-P011-EMILY-004`" in markdown


def test_page_inventory_reconciliation_accepts_represented_and_declared_context_regions():
    units = [
        semantic_unit(
            unit_id="SU-G1-VIRAL-P006-INTRO",
            source_region_ids=["PRM-G1-VIRAL-001-P006-R02"],
        )
    ]
    regions = [
        {
            "region_id": "PRM-G1-VIRAL-001-P006-R02",
            "decision": "represented",
            "expected_unit_types": ["heading"],
        },
        {
            "region_id": "PRM-G1-VIRAL-001-P006-R01",
            "decision": "visual_only",
            "expected_unit_types": [],
        },
    ]

    result = reconcile_page_inventory(regions, units)

    assert result["valid"] is True
    assert result["findings"] == []


def test_page_inventory_reconciliation_blocks_represented_region_without_unit():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R03-L", "decision": "represented"}],
        units=[],
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "unrepresented_structural_unit" for finding in result["findings"])


def test_page_inventory_reconciliation_requires_in_scope_representing_unit():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R03-L", "decision": "represented"}],
        units=[
            semantic_unit(
                unit_type="unknown_unsupported",
                unit_scope="unknown",
                heading_level=None,
                display_style="unknown",
                source_role="unknown",
                block_role="unknown_region",
                text_source_state="not_applicable",
                source_region_ids=["PRM-G1-VIRAL-001-P006-R03-L"],
            )
        ],
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "unrepresented_structural_unit" for finding in result["findings"])


def test_page_inventory_reconciliation_blocks_missing_decision():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R04"}],
        units=[],
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "context_only_decision_missing" for finding in result["findings"])


def test_page_inventory_reconciliation_blocks_unknown_region_without_unknown_unit():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R05", "decision": "unknown"}],
        units=[],
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "unknown_region_without_blocking_unit" for finding in result["findings"])


def test_page_inventory_reconciliation_accepts_unknown_region_with_blocking_unit():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R05", "decision": "unknown"}],
        units=[
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-UNKNOWN",
                unit_type="unknown_unsupported",
                unit_scope="unknown",
                heading_level=None,
                display_style="unknown",
                source_role="unknown",
                block_role="unknown_region",
                text_source_state="not_applicable",
                source_region_ids=["PRM-G1-VIRAL-001-P006-R05"],
            )
        ],
    )

    assert result["valid"] is True
    assert result["findings"] == []


def test_page_inventory_reconciliation_blocks_unknown_region_with_classified_in_scope_unit():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R05", "decision": "unknown"}],
        units=[
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-UNKNOWN",
                unit_type="unknown_unsupported",
                unit_scope="unknown",
                heading_level=None,
                display_style="unknown",
                source_role="unknown",
                block_role="unknown_region",
                text_source_state="not_applicable",
                source_region_ids=["PRM-G1-VIRAL-001-P006-R05"],
            ),
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-CLASSIFIED",
                reading_order=2,
                unit_type="paragraph",
                heading_level=None,
                display_style="body",
                block_role="text_column",
                source_region_ids=["PRM-G1-VIRAL-001-P006-R05"],
            ),
        ],
    )

    assert result["valid"] is False
    assert any(
        finding["finding_id"] == "unknown_region_conflicts_with_represented_units"
        for finding in result["findings"]
    )


def test_page_inventory_reconciliation_blocks_region_references_outside_inventory():
    result = reconcile_page_inventory(
        regions=[{"region_id": "PRM-G1-VIRAL-001-P006-R02", "decision": "represented"}],
        units=[semantic_unit(source_region_ids=["PRM-G1-VIRAL-001-P006-R99"])],
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "semantic_unit_region_not_in_inventory" for finding in result["findings"])


def test_page_inventory_reconciliation_blocks_missing_expected_unit_type():
    result = reconcile_page_inventory(
        regions=[
            {
                "region_id": "PRM-G1-VIRAL-001-P006-R03-L",
                "decision": "represented",
                "expected_unit_types": ["heading", "quote"],
            }
        ],
        units=[
            semantic_unit(
                source_region_ids=["PRM-G1-VIRAL-001-P006-R03-L"],
            )
        ],
    )

    assert result["valid"] is False
    assert any(finding["finding_id"] == "missing_expected_unit_type" for finding in result["findings"])


def test_page_inventory_reconciliation_blocks_collapsed_heading_quote_body_region():
    result = reconcile_page_inventory(
        regions=[
            {
                "region_id": "PRM-G1-VIRAL-001-P006-R03-L",
                "decision": "represented",
                "expected_unit_types": ["heading", "quote", "paragraph"],
            }
        ],
        units=[
            semantic_unit(
                unit_id="SU-G1-VIRAL-P006-COLLAPSED",
                unit_type="paragraph",
                heading_level=None,
                display_style="body",
                block_role="text_column",
                source_region_ids=["PRM-G1-VIRAL-001-P006-R03-L"],
                text='Summary "We are the Spektral Krew..." - Marco Proudfoot Producers... Overview This scenario...',
            )
        ],
    )

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["readiness_blocked"] is True
    assert {"collapsed_units", "missing_expected_heading", "quote_flattened", "missing_expected_unit_type"}.issubset(
        finding_ids
    )


def test_semantic_regression_toc_rows_preserve_list_items_and_page_refs():
    region_id = "SYN-G1-PAGE-TOC-COL-A"
    units = [
        semantic_unit(unit_id="SU-SYN-TOC-HEAD", source_region_ids=[region_id], text="Contents"),
        semantic_unit(
            unit_id="SU-SYN-TOC-ITEM",
            reading_order=2,
            unit_type="list_item",
            heading_level=None,
            display_style="list_item",
            block_role="list_region",
            source_region_ids=[region_id],
            text="Introduction",
        ),
        semantic_unit(
            unit_id="SU-SYN-TOC-PAGE-REF",
            reading_order=3,
            unit_type="page_ref",
            heading_level=None,
            display_style="page_ref",
            block_role="list_region",
            source_region_ids=[region_id],
            text="6",
        ),
    ]

    document = semantic_map_document(page="toc", package_id="PCRP-SYN-TOC", map_id="SM-SYN-TOC", source="unit_test", units=units)
    reconciliation = reconcile_page_inventory(
        [{"region_id": region_id, "decision": "represented", "expected_unit_types": ["heading", "list_item", "page_ref"]}],
        units,
    )

    assert document["semantic_validation"]["valid"] is True
    assert reconciliation["valid"] is True
    assert reconciliation["findings"] == []


def test_semantic_regression_art_caption_region_allows_visual_art_and_text_caption():
    region_id = "SYN-G1-PAGE-ART-CAPTION"
    units = [
        semantic_unit(
            unit_id="SU-SYN-ART",
            unit_type="art",
            unit_scope="visual_only",
            display_style="visual_art",
            source_role="visual_context",
            block_role="art_region",
            text_source_state="not_applicable",
            review_state="visual_only",
            heading_level=None,
            source_region_ids=[region_id],
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-CAPTION",
            reading_order=2,
            unit_type="caption",
            display_style="caption",
            block_role="caption_region",
            heading_level=None,
            source_region_ids=[region_id],
            text="Figure: Isola di Malamente at dusk.",
        ),
    ]

    validation = validate_semantic_units(units)
    reconciliation = reconcile_page_inventory(
        [{"region_id": region_id, "decision": "represented", "expected_unit_types": ["art", "caption"]}],
        units,
    )

    assert validation["valid"] is True
    assert reconciliation["valid"] is True
    assert reconciliation["findings"] == []


def test_semantic_regression_represented_region_requires_expected_type_for_visual_unit():
    result = reconcile_page_inventory(
        [{"region_id": "SYN-G1-PAGE-ART", "decision": "represented", "expected_unit_types": []}],
        [
            semantic_unit(
                unit_id="SU-SYN-ART-ONLY",
                unit_type="art",
                unit_scope="visual_only",
                display_style="visual_art",
                source_role="visual_context",
                block_role="art_region",
                text_source_state="not_applicable",
                review_state="visual_only",
                heading_level=None,
                source_region_ids=["SYN-G1-PAGE-ART"],
                text="",
            )
        ],
    )

    assert result["readiness_blocked"] is True
    assert any(finding["finding_id"] == "unrepresented_structural_unit" for finding in result["findings"])


def test_semantic_regression_table_header_and_body_cells_remain_structured():
    region_id = "SYN-G1-PAGE-TABLE"
    units = [
        semantic_unit(
            unit_id="SU-SYN-TABLE",
            unit_type="table",
            display_style="table_cell",
            block_role="table_region",
            heading_level=None,
            source_region_ids=[region_id],
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-TABLE-ROW-H",
            reading_order=2,
            unit_type="table_row",
            display_style="table_cell",
            block_role="table_region",
            heading_level=None,
            source_region_ids=[region_id],
            parent_unit_id="SU-SYN-TABLE",
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-TABLE-H1",
            reading_order=3,
            unit_type="table_cell",
            display_style="table_header",
            block_role="table_region",
            heading_level=None,
            source_region_ids=[region_id],
            parent_unit_id="SU-SYN-TABLE-ROW-H",
            container_unit_id="SU-SYN-TABLE",
            text="Name",
        ),
        semantic_unit(
            unit_id="SU-SYN-TABLE-B1",
            reading_order=4,
            unit_type="table_cell",
            display_style="table_cell",
            block_role="table_region",
            heading_level=None,
            source_region_ids=[region_id],
            parent_unit_id="SU-SYN-TABLE-ROW-H",
            container_unit_id="SU-SYN-TABLE",
            text="Hastalÿk",
        ),
    ]

    validation = validate_semantic_units(units)
    reconciliation = reconcile_page_inventory(
        [{"region_id": region_id, "decision": "represented", "expected_unit_types": ["table", "table_row", "table_cell"]}],
        units,
    )

    assert validation["valid"] is True
    assert reconciliation["valid"] is True


def test_semantic_regression_callout_sidebar_card_and_stat_units_keep_container_children():
    units = [
        semantic_unit(
            unit_id="SU-SYN-CALLOUT",
            unit_type="callout",
            display_style="callout_body",
            block_role="callout_region",
            heading_level=None,
            source_region_ids=["SYN-CALLOUT"],
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-CALLOUT-BODY",
            reading_order=2,
            unit_type="paragraph",
            display_style="callout_body",
            block_role="callout_region",
            heading_level=None,
            source_region_ids=["SYN-CALLOUT"],
            parent_unit_id="SU-SYN-CALLOUT",
            text="Keeper note",
        ),
        semantic_unit(
            unit_id="SU-SYN-SIDEBAR",
            reading_order=3,
            unit_type="sidebar",
            display_style="sidebar_body",
            block_role="sidebar_region",
            heading_level=None,
            source_region_ids=["SYN-SIDEBAR"],
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-SIDEBAR-BODY",
            reading_order=4,
            unit_type="paragraph",
            display_style="sidebar_body",
            block_role="sidebar_region",
            heading_level=None,
            source_region_ids=["SYN-SIDEBAR"],
            parent_unit_id="SU-SYN-SIDEBAR",
            text="Sidebar body",
        ),
        semantic_unit(
            unit_id="SU-SYN-CARD",
            reading_order=5,
            unit_type="card",
            display_style="card_body",
            block_role="card_region",
            heading_level=None,
            source_region_ids=["SYN-CARD"],
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-CARD-BODY",
            reading_order=6,
            unit_type="paragraph",
            display_style="card_body",
            block_role="card_region",
            heading_level=None,
            source_region_ids=["SYN-CARD"],
            parent_unit_id="SU-SYN-CARD",
            text="NPC card",
        ),
        semantic_unit(
            unit_id="SU-SYN-STAT-BLOCK",
            reading_order=7,
            unit_type="stat_block",
            display_style="stat_label",
            block_role="stat_block_region",
            heading_level=None,
            source_region_ids=["SYN-STAT"],
            text="STR 70",
        ),
        semantic_unit(
            unit_id="SU-SYN-STAT-LABEL",
            reading_order=8,
            unit_type="stat_label",
            display_style="stat_label",
            block_role="stat_block_region",
            heading_level=None,
            source_region_ids=["SYN-STAT"],
            parent_unit_id="SU-SYN-STAT-BLOCK",
            text="STR",
        ),
        semantic_unit(
            unit_id="SU-SYN-STAT-VALUE",
            reading_order=9,
            unit_type="stat_value",
            display_style="stat_value",
            block_role="stat_block_region",
            heading_level=None,
            source_region_ids=["SYN-STAT"],
            parent_unit_id="SU-SYN-STAT-BLOCK",
            text="70",
        ),
    ]
    regions = [
        {"region_id": "SYN-CALLOUT", "decision": "represented", "expected_unit_types": ["callout"]},
        {"region_id": "SYN-SIDEBAR", "decision": "represented", "expected_unit_types": ["sidebar"]},
        {"region_id": "SYN-CARD", "decision": "represented", "expected_unit_types": ["card"]},
        {"region_id": "SYN-STAT", "decision": "represented", "expected_unit_types": ["stat_block", "stat_label", "stat_value"]},
    ]

    validation = validate_semantic_units(units)
    reconciliation = reconcile_page_inventory(regions, units)

    assert validation["valid"] is True
    assert reconciliation["valid"] is True


def test_semantic_regression_callout_body_requires_boundary_contract():
    units = [
        semantic_unit(
            unit_id="SU-SYN-CALLOUT-BODY",
            unit_type="paragraph",
            display_style="callout_body",
            block_role="callout_region",
            heading_level=None,
            source_region_ids=["SYN-CALLOUT"],
            text="Keeper note",
            semantic_split_contract=None,
        ),
    ]

    validation = validate_semantic_units(units)
    finding_ids = {finding["finding_id"] for finding in validation["findings"]}

    assert validation["readiness_blocked"] is True
    assert "missing_semantic_split_contract" in finding_ids


def test_semantic_regression_blocks_flattened_table_stat_and_callout_topology():
    units = [
        semantic_unit(
            unit_id="SU-SYN-FLAT-TABLE",
            unit_type="table",
            display_style="table_cell",
            block_role="table_region",
            heading_level=None,
            source_region_ids=["SYN-FLAT-TABLE"],
            text="",
        ),
        semantic_unit(
            unit_id="SU-SYN-FLAT-ROW",
            reading_order=2,
            unit_type="table_row",
            display_style="table_cell",
            block_role="table_region",
            heading_level=None,
            source_region_ids=["SYN-FLAT-TABLE"],
            text="Name | Value",
        ),
        semantic_unit(
            unit_id="SU-SYN-FLAT-CELL",
            reading_order=3,
            unit_type="table_cell",
            display_style="table_cell",
            block_role="table_region",
            heading_level=None,
            source_region_ids=["SYN-FLAT-TABLE"],
            text="Hastalÿk",
        ),
        semantic_unit(
            unit_id="SU-SYN-FLAT-STAT",
            reading_order=4,
            unit_type="stat_label",
            display_style="stat_label",
            block_role="stat_block_region",
            heading_level=None,
            source_region_ids=["SYN-FLAT-STAT"],
            text="STR",
        ),
        semantic_unit(
            unit_id="SU-SYN-FLAT-CALLOUT",
            reading_order=5,
            unit_type="callout",
            display_style="callout_body",
            block_role="callout_region",
            heading_level=None,
            source_region_ids=["SYN-FLAT-CALLOUT"],
            text="Keeper note without linked children.",
        ),
    ]

    validation = validate_semantic_units(units)
    finding_ids = {finding["finding_id"] for finding in validation["findings"]}

    assert validation["readiness_blocked"] is True
    assert {"table_structure_flattened", "stat_block_flattened", "callout_container_unresolved"}.issubset(
        finding_ids
    )


def test_semantic_regression_visual_page_marker_and_context_inset_do_not_require_text_scope():
    units = [
        semantic_unit(
            unit_id="SU-SYN-PAGE-MARKER",
            unit_type="page_marker",
            unit_scope="visual_only",
            display_style="page_marker",
            source_role="visual_context",
            block_role="page_marker_region",
            text_source_state="not_applicable",
            review_state="visual_only",
            heading_level=None,
            source_region_ids=["SYN-PAGE-MARKER"],
            text="6",
        ),
        semantic_unit(
            unit_id="SU-SYN-CONTEXT-INSET",
            reading_order=2,
            unit_type="art",
            unit_scope="context_only",
            display_style="visual_art",
            source_role="visual_context",
            block_role="context_region",
            text_source_state="not_applicable",
            review_state="context_only",
            heading_level=None,
            source_region_ids=["SYN-CONTEXT-INSET"],
            text="",
        ),
    ]
    regions = [
        {"region_id": "SYN-PAGE-MARKER", "decision": "visual_only", "expected_unit_types": ["page_marker"]},
        {"region_id": "SYN-CONTEXT-INSET", "decision": "context_only", "expected_unit_types": ["art"]},
    ]

    validation = validate_semantic_units(units)
    reconciliation = reconcile_page_inventory(regions, units)

    assert validation["valid"] is True
    assert reconciliation["valid"] is True
    assert reconciliation["findings"] == []


def test_semantic_regression_unknown_unsupported_region_remains_blocked_but_represented():
    units = [
        semantic_unit(
            unit_id="SU-SYN-UNKNOWN",
            unit_type="unknown_unsupported",
            unit_scope="blocked",
            display_style="unknown",
            source_role="unknown",
            block_role="unknown_region",
            text_source_state="not_applicable",
            review_state="blocked",
            heading_level=None,
            source_region_ids=["SYN-UNKNOWN"],
            text="Unsupported mixed object.",
        )
    ]

    validation = validate_semantic_units(units)
    reconciliation = reconcile_page_inventory(
        [{"region_id": "SYN-UNKNOWN", "decision": "blocked", "expected_unit_types": []}],
        units,
    )

    assert validation["valid"] is True
    assert reconciliation["valid"] is True
    assert reconciliation["findings"] == []


def test_page_complete_review_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT), "--page", "002"], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-PAGE-MAP-READINESS-PIPELINE-PILOT-002-001",
            "--page",
            "002",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert P002_AUTH in wrong_auth.stderr


def test_page_complete_review_is_profile_gated():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", P002_AUTH, "--page", "009"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert P009_AUTH in result.stderr


def test_page_007_review_uses_natural_page_profile_key_and_auth_gate():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", P002_AUTH, "--page", "007"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert P007_AUTH in result.stderr


def test_page_001_review_uses_triage_route_and_auth_gate():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", P002_AUTH, "--page", "001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert P001_AUTH in result.stderr


def test_page_002_review_uses_readiness_input_without_acceptance():
    report = read_json(P002_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P002-001"
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["PMRP-G1-VIRAL-P002-001"]
    assert report["readiness_input"]["package_id"] == "PMRP-G1-VIRAL-P002-001"
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["review_decision"]["fixture_admission_created"] is False


def test_page_002_review_inventory_has_no_blockers_or_open_questions():
    report = read_json(P002_REPORT)
    review = report["page_complete_review"]

    assert review["expected_blocks"] == 2
    assert review["reviewed_blocks"] == 2
    assert review["ready_blocks"] == 2
    assert review["reading_order"] == ["credits", "boxed_legal_footer"]
    assert review["coverage_advisory_only"] is True
    assert review["blockers"] == []
    assert review["open_questions"] == []
    assert review["recommendation"] == "page_complete_decision_ready_for_bogdan"
    assert set(review["declared_none_categories"]) == {
        "art",
        "inset",
        "table",
        "title_only",
        "unknown",
        "missing",
        "context_only",
    }


def test_page_002_review_blocks_preserve_readiness_fidelity():
    report = read_json(P002_REPORT)
    blocks = {block["block_id"]: block for block in report["page_complete_review"]["blocks"]}

    assert blocks["P002-B001"]["role"] == "credits"
    assert blocks["P002-B002"]["role"] == "boxed_legal_footer"
    assert blocks["P002-B001"]["protected_tokens_matched"] == 7
    assert blocks["P002-B001"]["protected_tokens_total"] == 7
    assert blocks["P002-B002"]["protected_tokens_matched"] == 10
    assert blocks["P002-B002"]["protected_tokens_total"] == 10
    assert blocks["P002-B001"]["draft_matches_verified"] is True
    assert blocks["P002-B002"]["draft_matches_verified"] is True
    assert blocks["P002-B001"]["discrepancy_disposition"] == "none"
    assert blocks["P002-B002"]["discrepancy_disposition"] == "none"


def test_page_003_review_uses_p003_readiness_input_without_acceptance():
    report = read_json(P003_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P003-001"
    assert report["authorization_id"] == P003_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["PMRP-G1-VIRAL-P003-001"]
    assert report["readiness_input"]["package_id"] == "PMRP-G1-VIRAL-P003-001"
    assert report["readiness_input"]["profile_id"] == "page_map_profile_G1_VIRAL_P003_v0"
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["review_decision"]["fixture_admission_created"] is False
    assert [attachment["package_path"] for attachment in report["review_attachments"]] == [
        "review_assets/page_003.png",
        "review_assets/1_SRCR-G1-VIRAL-003-R01.png",
        "review_assets/2_SRCR-G1-VIRAL-003-R02.png",
        "review_assets/page_003_ocr_block_text.md",
    ]


def test_page_003_review_inventory_has_no_blockers_or_open_questions():
    report = read_json(P003_REPORT)
    review = report["page_complete_review"]

    assert review["expected_blocks"] == 2
    assert review["reviewed_blocks"] == 2
    assert review["ready_blocks"] == 2
    assert review["reading_order"] == ["title_heading_like", "main_body_text"]
    assert review["coverage_advisory_only"] is True
    assert review["blockers"] == []
    assert review["open_questions"] == []
    assert review["recommendation"] == "page_complete_decision_ready_for_bogdan"
    assert set(review["declared_none_categories"]) == {"art", "inset", "table", "unknown", "missing", "context_only"}


def test_page_003_review_blocks_preserve_readiness_fidelity():
    report = read_json(P003_REPORT)
    blocks = {block["block_id"]: block for block in report["page_complete_review"]["blocks"]}

    assert blocks["P003-B001"]["role"] == "title_heading_like"
    assert blocks["P003-B002"]["role"] == "main_body_text"
    assert blocks["P003-B001"]["protected_tokens_matched"] == 2
    assert blocks["P003-B001"]["protected_tokens_total"] == 2
    assert blocks["P003-B002"]["protected_tokens_matched"] == 11
    assert blocks["P003-B002"]["protected_tokens_total"] == 11
    assert blocks["P003-B001"]["draft_matches_verified"] is True
    assert blocks["P003-B002"]["draft_matches_verified"] is True
    assert blocks["P003-B001"]["discrepancy_disposition"] == "none"
    assert blocks["P003-B002"]["discrepancy_disposition"] == "none"


def test_page_complete_review_guardrails_stay_false_for_all_profiles():
    for path in [
        P002_REPORT,
        P003_REPORT,
        P004_REPORT,
        P005_REPORT,
        P005_002_REPORT,
        P005_003_REPORT,
        P006_REPORT,
        P006_002_REPORT,
        P007_REPORT,
    ]:
        report = read_json(path)
        for key in [
            "ocr_executed",
            "pdf_opened_or_parsed",
            "pdf_text_layer_used",
            "render_executed",
            "raw_artifacts_modified",
            "source_acceptance_created",
            "page_complete_acceptance_created",
            "whole_gate_1_acceptance_created",
            "fixture_admission",
            "translation_authorized",
            "proofreading_authorized",
            "renderer_profile_acceptance",
            "implementation_authorized",
            "push_authorized",
        ]:
            assert report["guardrails"][key] is False


def test_human_packets_are_decision_facing_and_not_internal_qa_dumps():
    expectations = [
        (P002_PACKET, "page 002 complete ok", "hold page 002"),
        (P003_PACKET, "page 003 complete ok", "hold page 003"),
        (P004_PACKET, "page 004 complete ok", "hold page 004"),
    ]
    for path, accept_text, hold_text in expectations:
        packet = path.read_text(encoding="utf-8-sig")
        forbidden = ["SHA-256", "pytest", "test key", "diff-check", "stale scan"]
        assert all(item not in packet for item in forbidden)
        assert accept_text in packet
        assert hold_text in packet
        assert "This packet itself creates no acceptance" in packet

    p005_packet = P005_PACKET.read_text(encoding="utf-8-sig")
    assert "page 005 complete ok" not in p005_packet
    assert "hold page 005" in p005_packet
    assert "Page 005 is blocked before any page-complete decision" in p005_packet

    p005_002_packet = P005_002_PACKET.read_text(encoding="utf-8-sig")
    assert "page 005 complete ok" in p005_002_packet
    assert "hold page 005" in p005_002_packet

    p006_packet = P006_PACKET.read_text(encoding="utf-8-sig")
    assert "page 006 complete ok" not in p006_packet
    assert "hold page 006" in p006_packet
    assert "Page 006 is blocked before any page-complete decision" in p006_packet
    assert "Requires superseding packet: `PCRP-G1-VIRAL-P006-002`" in p006_packet

    p006_002_packet = P006_002_PACKET.read_text(encoding="utf-8-sig")
    assert "page 006 complete ok" in p006_002_packet
    assert "hold page 006" in p006_002_packet
    assert "Page 006 is blocked before any page-complete decision" not in p006_002_packet


def test_page_003_review_packet_packages_visual_and_text_attachments():
    report = read_json(P003_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_003.png",
        "review_assets/1_SRCR-G1-VIRAL-003-R01.png",
        "review_assets/2_SRCR-G1-VIRAL-003-R02.png",
        "review_assets/page_003_ocr_block_text.md",
    }
    for package_path, attachment in attachments.items():
        target = P003_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    packet = P003_PACKET.read_text(encoding="utf-8-sig")
    assert "## Review Attachments" in packet
    assert "review_assets/page_003.png" in packet
    assert "review_assets/1_SRCR-G1-VIRAL-003-R01.png" in packet
    assert "review_assets/2_SRCR-G1-VIRAL-003-R02.png" in packet
    assert "review_assets/page_003_ocr_block_text.md" in packet


def test_page_004_review_uses_p004_readiness_input_without_acceptance():
    report = read_json(P004_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P004-001"
    assert report["authorization_id"] == P004_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["PMRP-G1-VIRAL-P004-001"]
    assert report["readiness_input"]["package_id"] == "PMRP-G1-VIRAL-P004-001"
    assert report["readiness_input"]["profile_id"] == "page_map_profile_G1_VIRAL_P004_v0"
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["review_decision"]["fixture_admission_created"] is False
    assert [attachment["package_path"] for attachment in report["review_attachments"]] == [
        "review_assets/page_004.png",
        "review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png",
        "review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png",
        "review_assets/page_004_ocr_block_text.md",
    ]


def test_page_004_review_inventory_has_no_blockers_or_open_questions():
    report = read_json(P004_REPORT)
    review = report["page_complete_review"]

    assert review["expected_blocks"] == 2
    assert review["reviewed_blocks"] == 2
    assert review["ready_blocks"] == 2
    assert review["reading_order"] == ["warning_title", "safety_warning_body"]
    assert review["coverage_advisory_only"] is True
    assert review["blockers"] == []
    assert review["open_questions"] == []
    assert review["recommendation"] == "page_complete_decision_ready_for_bogdan"
    assert set(review["declared_none_categories"]) == {"art", "table", "unknown", "missing"}
    assert review["context_only_regions"][0]["source_region_id"] == "PRM-G1-VIRAL-001-P004-R01"


def test_page_004_review_blocks_preserve_readiness_fidelity():
    report = read_json(P004_REPORT)
    blocks = {block["block_id"]: block for block in report["page_complete_review"]["blocks"]}

    assert blocks["P004-B001"]["role"] == "warning_title"
    assert blocks["P004-B002"]["role"] == "safety_warning_body"
    assert blocks["P004-B001"]["protected_tokens_matched"] == 1
    assert blocks["P004-B001"]["protected_tokens_total"] == 1
    assert blocks["P004-B002"]["protected_tokens_matched"] == 7
    assert blocks["P004-B002"]["protected_tokens_total"] == 7
    assert blocks["P004-B001"]["draft_matches_verified"] is True
    assert blocks["P004-B002"]["draft_matches_verified"] is True
    assert blocks["P004-B001"]["discrepancy_disposition"] == "none"
    assert blocks["P004-B002"]["discrepancy_disposition"] == "none"


def test_page_004_review_packet_packages_visual_and_text_attachments():
    report = read_json(P004_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_004.png",
        "review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png",
        "review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png",
        "review_assets/page_004_ocr_block_text.md",
    }
    for package_path, attachment in attachments.items():
        target = P004_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    packet = P004_PACKET.read_text(encoding="utf-8-sig")
    assert "## Review Attachments" in packet
    assert "review_assets/page_004.png" in packet
    assert "review_assets/1_SRCR-G1-VIRAL-004-R01__PRM-G1-VIRAL-001-P004-R02.png" in packet
    assert "review_assets/2_SRCR-G1-VIRAL-004-R02__PRM-G1-VIRAL-001-P004-R03.png" in packet
    assert "review_assets/page_004_ocr_block_text.md" in packet
    assert "Context-only regions: 1" in packet


def test_page_005_review_uses_p005_readiness_input_without_acceptance():
    report = read_json(P005_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P005-001"
    assert report["authorization_id"] == P005_AUTH
    assert report["status"] == "blocked"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["PMRP-G1-VIRAL-P005-001"]
    assert report["readiness_input"]["package_id"] == "PMRP-G1-VIRAL-P005-001"
    assert report["readiness_input"]["profile_id"] == "page_map_profile_G1_VIRAL_P005_v0"
    assert report["review_decision"]["requires_bogdan_decision"] is False
    assert report["review_decision"]["requires_superseding_review_packet"] is True
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["review_decision"]["fixture_admission_created"] is False
    assert [attachment["package_path"] for attachment in report["review_attachments"]] == [
        "review_assets/page_005.png",
        "review_assets/1_SRA-G1-VIRAL-001-R002__PRM-G1-VIRAL-001-P005-R01.png",
        "review_assets/2_SRA-G1-VIRAL-001-R003__PRM-G1-VIRAL-001-P005-R02.png",
        "review_assets/page_005_ocr_block_text.md",
    ]


def test_page_005_review_inventory_blocks_narrow_visual_proof_crop():
    report = read_json(P005_REPORT)
    review = report["page_complete_review"]

    assert review["expected_blocks"] == 2
    assert review["reviewed_blocks"] == 2
    assert review["ready_blocks"] == 2
    assert review["reading_order"] == ["contents_heading", "contents_entry_group"]
    assert review["coverage_advisory_only"] is True
    assert review["blockers"] == [
        {"block_id": "P005-B001", "reason": "visual_crop_smaller_than_declared_block_box"},
        {"block_id": "P005-B002", "reason": "visual_crop_smaller_than_declared_block_box"},
    ]
    assert review["open_questions"] == []
    assert review["recommendation"] == "blocked_before_bogdan_decision"
    assert review["decision_options"] == ["hold_page_005_for_corrections_or_additional_review"]
    assert set(review["declared_none_categories"]) == {"art", "inset", "unknown", "missing"}
    assert review["context_only_regions"][0]["source_region_id"] == "PRM-G1-VIRAL-001-P005-R03"
    assert review["context_only_regions"][0]["status"] == "visual_exclusion_not_source_text_record"

    visual_checks = {check["block_id"]: check for check in review["visual_proof_checks"]}
    assert visual_checks["P005-B001"]["status"] == "blocked"
    assert visual_checks["P005-B001"]["crop_size"] == {"width": 860, "height": 260}
    assert visual_checks["P005-B001"]["declared_box_size"] == {"width": 750, "height": 280}
    assert visual_checks["P005-B001"]["width_ratio"] >= 1.0
    assert visual_checks["P005-B001"]["height_ratio"] < 1.0
    assert visual_checks["P005-B002"]["status"] == "blocked"
    assert visual_checks["P005-B002"]["crop_size"] == {"width": 560, "height": 235}
    assert visual_checks["P005-B002"]["declared_box_size"] == {"width": 2050, "height": 2300}
    assert visual_checks["P005-B002"]["width_ratio"] < 0.9
    assert visual_checks["P005-B002"]["height_ratio"] < 0.9


def test_page_005_review_blocks_preserve_readiness_fidelity():
    report = read_json(P005_REPORT)
    blocks = {block["block_id"]: block for block in report["page_complete_review"]["blocks"]}

    assert blocks["P005-B001"]["role"] == "contents_heading"
    assert blocks["P005-B002"]["role"] == "contents_entry_group"
    assert blocks["P005-B001"]["protected_tokens_matched"] == 1
    assert blocks["P005-B001"]["protected_tokens_total"] == 1
    assert blocks["P005-B002"]["protected_tokens_matched"] == 4
    assert blocks["P005-B002"]["protected_tokens_total"] == 4
    assert blocks["P005-B001"]["draft_matches_verified"] is True
    assert blocks["P005-B002"]["draft_matches_verified"] is True
    assert blocks["P005-B001"]["discrepancy_disposition"] == "none"
    assert blocks["P005-B002"]["discrepancy_disposition"] == "none"


def test_page_005_review_packet_packages_visual_and_text_attachments():
    report = read_json(P005_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_005.png",
        "review_assets/1_SRA-G1-VIRAL-001-R002__PRM-G1-VIRAL-001-P005-R01.png",
        "review_assets/2_SRA-G1-VIRAL-001-R003__PRM-G1-VIRAL-001-P005-R02.png",
        "review_assets/page_005_ocr_block_text.md",
    }
    for package_path, attachment in attachments.items():
        target = P005_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    block_text = (P005_OUT_ROOT / "review_assets" / "page_005_ocr_block_text.md").read_text(encoding="utf-8-sig")
    assert "Contents" in block_text
    assert "The Spektral Krew" in block_text

    packet = P005_PACKET.read_text(encoding="utf-8-sig")
    assert "## Review Attachments" in packet
    assert "review_assets/page_005.png" in packet
    assert "review_assets/1_SRA-G1-VIRAL-001-R002__PRM-G1-VIRAL-001-P005-R01.png" in packet
    assert "review_assets/2_SRA-G1-VIRAL-001-R003__PRM-G1-VIRAL-001-P005-R02.png" in packet
    assert "review_assets/page_005_ocr_block_text.md" in packet
    assert "Context-only regions: 1" in packet
    assert "`P005-B001`: `visual_crop_smaller_than_declared_block_box`" in packet
    assert "`P005-B002`: `visual_crop_smaller_than_declared_block_box`" in packet


def test_page_005_superseding_review_uses_declared_block_crops_without_acceptance():
    report = read_json(P005_002_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P005-002"
    assert report["authorization_id"] == P005_002_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["PMRP-G1-VIRAL-P005-001"]
    assert report["readiness_input"]["package_id"] == "PMRP-G1-VIRAL-P005-001"
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["requires_superseding_review_packet"] is False
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert [attachment["package_path"] for attachment in report["review_attachments"]] == [
        "review_assets/page_005.png",
        "review_assets/1_P005-B001__declared_box__PRM-G1-VIRAL-001-P005-R01.png",
        "review_assets/2_P005-B002__declared_box__PRM-G1-VIRAL-001-P005-R02.png",
        "review_assets/page_005_ocr_block_text.md",
    ]


def test_page_005_superseding_review_visual_proof_covers_declared_boxes():
    report = read_json(P005_002_REPORT)
    review = report["page_complete_review"]

    assert review["expected_blocks"] == 2
    assert review["reviewed_blocks"] == 2
    assert review["ready_blocks"] == 2
    assert review["blockers"] == []
    assert review["recommendation"] == "page_complete_decision_ready_for_bogdan"
    assert review["decision_options"] == [
        "accept_page_005_as_complete_in_a_later_explicit_decision",
        "hold_page_005_for_corrections_or_additional_review",
    ]

    visual_checks = {check["block_id"]: check for check in review["visual_proof_checks"]}
    assert visual_checks["P005-B001"]["status"] == "passed"
    assert visual_checks["P005-B001"]["crop_size"] == {"width": 750, "height": 280}
    assert visual_checks["P005-B001"]["declared_box_size"] == {"width": 750, "height": 280}
    assert visual_checks["P005-B001"]["width_ratio"] == 1.0
    assert visual_checks["P005-B001"]["height_ratio"] == 1.0
    assert visual_checks["P005-B002"]["status"] == "passed"
    assert visual_checks["P005-B002"]["crop_size"] == {"width": 2050, "height": 2300}
    assert visual_checks["P005-B002"]["declared_box_size"] == {"width": 2050, "height": 2300}
    assert visual_checks["P005-B002"]["width_ratio"] == 1.0
    assert visual_checks["P005-B002"]["height_ratio"] == 1.0


def test_page_005_superseding_review_packet_packages_full_visual_and_text_assets():
    report = read_json(P005_002_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_005.png",
        "review_assets/1_P005-B001__declared_box__PRM-G1-VIRAL-001-P005-R01.png",
        "review_assets/2_P005-B002__declared_box__PRM-G1-VIRAL-001-P005-R02.png",
        "review_assets/page_005_ocr_block_text.md",
    }
    for package_path, attachment in attachments.items():
        target = P005_002_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    packet = P005_002_PACKET.read_text(encoding="utf-8-sig")
    assert "## Review Attachments" in packet
    assert "review_assets/page_005.png" in packet
    assert "review_assets/1_P005-B001__declared_box__PRM-G1-VIRAL-001-P005-R01.png" in packet
    assert "review_assets/2_P005-B002__declared_box__PRM-G1-VIRAL-001-P005-R02.png" in packet
    assert "review_assets/page_005_ocr_block_text.md" in packet
    assert "page 005 complete ok" in packet
    assert "visual_crop_smaller_than_declared_block_box" not in packet


def test_page_005_readable_review_packet_uses_three_human_crops_and_text_map():
    report = read_json(P005_003_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P005-003"
    assert report["authorization_id"] == P005_003_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert [attachment["package_path"] for attachment in report["review_attachments"]] == [
        "review_assets/page_005.png",
        "review_assets/1_P005-title__contents_heading.png",
        "review_assets/2_P005-left-column__contents_entries.png",
        "review_assets/3_P005-right-column__contents_entries.png",
        "review_assets/page_005_ocr_verified_text_map.md",
    ]


def test_page_005_readable_review_crop_edge_checks_pass():
    report = read_json(P005_003_REPORT)
    review = report["page_complete_review"]

    assert review["blockers"] == []
    assert review["visual_proof_checks"] == []
    checks = {check["label"]: check for check in review["human_review_crop_checks"]}
    assert set(checks) == {"contents_title", "contents_left_column", "contents_right_column"}
    for check in checks.values():
        assert check["status"] == "passed"
        assert check["reason"] is None
        assert max(check["edge_ink_ratios"].values()) <= check["maximum_allowed_edge_ink_ratio"]


def test_page_005_readable_review_text_map_matches_crop_content_and_heading_depth():
    text_map = (P005_003_OUT_ROOT / "review_assets" / "page_005_ocr_verified_text_map.md").read_text(
        encoding="utf-8-sig"
    )

    assert "## contents_title" in text_map
    assert "| Contents |  | `h1` | `red_display_heading` |" in text_map
    assert "| Introduction | 6 | `h2` | `bold` |" in text_map
    assert "| Summary | 6 | `h3` | `italic` |" in text_map
    assert "| Isola di Malamente: Locations | 33 | `h2_major` | `bold_large` |" in text_map
    assert "| Hospital Locations | 39 | `h4` | `italic` |" in text_map
    assert "| Hastalÿk Awakens | 49 | `h2` | `bold` |" in text_map
    assert "| Iuramentum Corruptionis | 67 | `h4` | `italic` |" in text_map
    assert "| Pre-Gens | 111 | `h2_major` | `bold_large` |" in text_map


def test_page_005_semantic_refresh_packet_validates_current_contract():
    report = read_json(P005_004_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P005-004"
    assert report["authorization_id"] == P005_004_AUTH
    assert report["input_packages"] == ["PCRP-G1-VIRAL-P005-003"]
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert review["semantic_units_validated"] is True
    assert review["semantic_validation"]["valid"] is True
    assert review["markdown_projection_validation"]["valid"] is True
    assert review["inventory_reconciliation"]["valid"] is True
    assert review["structural_findings"] == []
    assert review["blockers"] == []
    assert review["open_questions"] == []
    assert review["decision_options"] == [
        "accept_page_005_as_complete_in_a_later_explicit_decision",
        "hold_page_005_for_corrections_or_additional_review",
    ]


def test_page_005_semantic_refresh_emits_contents_units_and_projection():
    semantic_map = read_json(P005_004_SEMANTIC_MAP_JSON)
    semantic_markdown = P005_004_SEMANTIC_MAP_MARKDOWN.read_text(encoding="utf-8-sig")
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}

    assert semantic_map["canonical"] is True
    assert semantic_map["map_id"] == "SM-G1-VIRAL-P005-004"
    assert semantic_map["package_id"] == "PCRP-G1-VIRAL-P005-004"
    assert semantic_map["semantic_validation"]["unit_count"] == 74
    assert units["SU-P005-B001-S001"]["unit_type"] == "heading"
    assert units["SU-P005-B001-S001"]["heading_level"] == "h1"
    assert units["SU-P005-B002-S001"]["unit_type"] == "list"
    assert units["SU-P005-B002-S001"]["block_role"] == "list_region"
    assert units["SU-P005-B002-S002"]["unit_type"] == "list_item"
    assert units["SU-P005-B002-S002"]["parent_unit_id"] == "SU-P005-B002-S001"
    assert units["SU-P005-B002-S002"]["text"] == "Introduction 6"
    assert units["SU-P005-B002-S073"]["text"] == "Pre-Gens 111"
    assert "## Unit Summary" in semantic_markdown
    assert "## Unit Text" in semantic_markdown
    assert "```text" in semantic_markdown
    assert "page_complete_acceptance" in semantic_map["not_evidence_for"]


def test_page_006_readable_review_packet_uses_three_human_crops_and_text_map():
    report = read_json(P006_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P006-001"
    assert report["authorization_id"] == P006_AUTH
    assert report["status"] == "blocked"
    assert report["review_decision"]["requires_bogdan_decision"] is False
    assert report["review_decision"]["requires_superseding_review_packet"] is True
    assert report["review_decision"]["requires_superseding_package_id"] == "PCRP-G1-VIRAL-P006-002"
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["post_review_state"]["status"] == "held_after_bogdan_review"
    assert report["post_review_state"]["reason"] == "text_map_semantics_and_formatting_blocker"
    assert report["post_review_state"]["human_review_crop_decision"] == "ok_as_review_assets_only"
    assert report["post_review_state"]["negative_regression_input"] == "review_assets/page_006_ocr_verified_text_map.md"
    assert report["page_complete_review"]["semantic_units_validated"] is True
    assert report["page_complete_review"]["semantic_validation"]["readiness_blocked"] is True
    assert report["page_complete_review"]["inventory_reconciliation"]["valid"] is True
    assert report["page_complete_review"]["inventory_reconciliation"]["readiness_blocked"] is False
    assert report["page_complete_review"]["inventory_reconciliation"]["findings"] == []
    assert report["page_complete_review"]["decision_options"] == ["hold_page_006_for_corrections_or_additional_review"]
    assert not any("accept_page_006" in option for option in report["page_complete_review"]["decision_options"])
    assert [finding["finding_id"] for finding in report["page_complete_review"]["structural_findings"]] == [
        "invalid_heading_level"
    ]
    assert [attachment["package_path"] for attachment in report["review_attachments"]] == [
        "review_assets/page_006.png",
        "review_assets/1_P006-title__introduction_heading.png",
        "review_assets/2_P006-left-column__summary_overview.png",
        "review_assets/3_P006-right-column__overview_continuation.png",
        "review_assets/page_006_ocr_verified_text_map.md",
        "review_assets/page_006_semantic_text_map.json",
        "review_assets/page_006_semantic_text_map.md",
    ]


def test_page_006_readable_review_crop_edge_checks_pass():
    report = read_json(P006_REPORT)
    review = report["page_complete_review"]

    assert review["blockers"] == [
        {
            "block_id": "P006-001-ATT-SEMANTIC-MAP-JSON",
            "reason": "semantic_validation_blocker",
            "finding_count": 1,
        },
        {
            "block_id": "PCRP-G1-VIRAL-P006-001",
            "reason": "text_map_semantics_and_formatting_blocker",
            "decision_id": "hold_page_006_text_map_semantics_messages_896_897",
            "requires_superseding_package_id": "PCRP-G1-VIRAL-P006-002",
        }
    ]
    assert review["decision_options"] == ["hold_page_006_for_corrections_or_additional_review"]
    assert review["visual_proof_checks"] == []
    checks = {check["label"]: check for check in review["human_review_crop_checks"]}
    assert set(checks) == {"introduction_title", "summary_overview_left_column", "overview_right_column"}
    for check in checks.values():
        assert check["status"] == "passed"
        assert check["reason"] is None


def test_page_006_readable_review_text_map_matches_crop_content_and_heading_depth():
    text_map = (P006_OUT_ROOT / "review_assets" / "page_006_ocr_verified_text_map.md").read_text(
        encoding="utf-8-sig"
    )

    assert "## introduction_title" in text_map
    assert "Introduction" in text_map
    assert "## summary_overview_left_column" in text_map
    assert "Summary" in text_map
    assert "We are the Spektral Krew" in text_map
    assert "Isola di Malamente" in text_map
    assert "Overview" in text_map
    assert "## overview_right_column" in text_map
    assert "Plague Monks" in text_map
    assert "Innsmouth Protocol" in text_map
    assert "four to eight hours" in text_map


def test_page_006_builder_emits_semantic_map_artifacts_from_spans_without_acceptance():
    report = read_json(P006_REPORT)
    semantic_json_attachment = next(
        attachment for attachment in report["review_attachments"] if attachment["role"] == "semantic_text_map_json"
    )
    semantic_md_attachment = next(
        attachment for attachment in report["review_attachments"] if attachment["role"] == "semantic_text_map_markdown"
    )
    semantic_map = read_json(P006_SEMANTIC_MAP_JSON)
    semantic_markdown = P006_SEMANTIC_MAP_MARKDOWN.read_text(encoding="utf-8-sig")

    assert semantic_json_attachment["package_path"] == "review_assets/page_006_semantic_text_map.json"
    assert semantic_md_attachment["package_path"] == "review_assets/page_006_semantic_text_map.md"
    assert semantic_map["canonical"] is True
    assert semantic_map["map_id"] == "SM-G1-VIRAL-P006-001"
    assert semantic_map["package_id"] == "PCRP-G1-VIRAL-P006-001"
    assert len(semantic_map["units"]) == 7
    assert semantic_map["markdown_projection_validation"]["valid"] is True
    assert "## Unit Summary" in semantic_markdown
    assert "## Unit Text" in semantic_markdown
    assert "```text" in semantic_markdown
    assert "page_complete_acceptance" in semantic_map["not_evidence_for"]
    assert semantic_json_attachment["semantic_validation"]["readiness_blocked"] is True
    assert semantic_json_attachment["markdown_projection_validation"]["valid"] is True
    assert report["status"] == "blocked"
    assert report["review_decision"]["page_complete_acceptance_created"] is False


def test_page_006_review_packet_surfaces_inventory_reconciliation_gate():
    packet = P006_PACKET.read_text(encoding="utf-8-sig")
    summary = P006_SUMMARY.read_text(encoding="utf-8-sig")

    assert "- Inventory reconciliation: `valid`" in packet
    assert "- Inventory reconciliation: True." in summary
    assert "inventory_reconciliation_blocker" not in packet


def test_page_006_superseding_review_packet_is_ready_without_acceptance():
    report = read_json(P006_002_REPORT)

    assert report["package_id"] == "PCRP-G1-VIRAL-P006-002"
    assert report["authorization_id"] == P006_002_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["requires_superseding_review_packet"] is False
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["review_decision"]["fixture_admission_created"] is False
    assert report["page_complete_review"]["blockers"] == []
    assert report["page_complete_review"]["structural_findings"] == []
    assert report["page_complete_review"]["decision_options"] == [
        "accept_page_006_as_complete_in_a_later_explicit_decision",
        "hold_page_006_for_corrections_or_additional_review",
    ]


def test_page_006_superseding_semantic_map_preserves_units_and_continuation():
    semantic_map = read_json(P006_002_SEMANTIC_MAP_JSON)
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}

    assert semantic_map["canonical"] is True
    assert semantic_map["map_id"] == "SM-G1-VIRAL-P006-002"
    assert semantic_map["package_id"] == "PCRP-G1-VIRAL-P006-002"
    assert semantic_map["semantic_validation"]["valid"] is True
    assert semantic_map["markdown_projection_validation"]["valid"] is True
    assert semantic_map["structural_findings"] == []
    assert len(units) == 7
    assert units["SU-P006-B001-S001"]["text"] == "Introduction"
    assert units["SU-P006-B001-S001"]["heading_level"] == "h2"
    assert units["SU-P006-B002-S001"]["text"] == "Summary"
    assert units["SU-P006-B002-S001"]["unit_type"] == "heading"
    assert units["SU-P006-B002-S002"]["unit_type"] == "quote"
    assert units["SU-P006-B002-S002"]["heading_level"] is None
    assert units["SU-P006-B002-S004"]["text"] == "Overview"
    assert units["SU-P006-B002-S004"]["unit_type"] == "heading"
    assert units["SU-P006-B002-S005"]["continues_to"] == "SU-P006-B003-S001"
    assert units["SU-P006-B003-S001"]["unit_type"] == "continuation"
    assert units["SU-P006-B003-S001"]["continues_from"] == "SU-P006-B002-S005"


def test_page_006_superseding_text_map_uses_metadata_table_and_full_text_blocks():
    text_map = P006_002_TEXT_MAP.read_text(encoding="utf-8-sig")
    semantic_markdown = P006_002_SEMANTIC_MAP_MARKDOWN.read_text(encoding="utf-8-sig")

    assert "| Unit | Text preview | Page | Heading level | Style |" in text_map
    assert "| SU-P006-B001-S001 | Introduction |  | `h2` | `chapter_heading` |" in text_map
    assert "| SU-P006-B002-S002 | \"We are the Spektral Krew" in text_map
    assert "| SU-P006-B002-S003 | Producers of a popular ghost hunting YouTube channel" in text_map
    assert "### Full Text - SU-P006-B002-S003" in text_map
    assert "### Full Text - SU-P006-B003-S001" in text_map
    assert "Overview" in text_map
    assert "four to eight hours" in text_map
    assert "## Unit Summary" in semantic_markdown
    assert "## Unit Text" in semantic_markdown


def test_page_007_review_packet_is_ready_without_acceptance():
    report = read_json(P007_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P007-003"
    assert report["authorization_id"] == P007_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["input_packages"] == ["P007-INLINE-MAP-G1-VIRAL-003"]
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["requires_superseding_review_packet"] is False
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["review_decision"]["fixture_admission_created"] is False
    assert review["expected_blocks"] == 3
    assert review["reviewed_blocks"] == 3
    assert review["ready_blocks"] == 3
    assert review["blockers"] == []
    assert review["structural_findings"] == []
    assert review["semantic_validation"]["valid"] is True
    assert review["markdown_projection_validation"]["valid"] is True
    assert review["inventory_reconciliation"]["valid"] is True
    assert review["decision_options"] == [
        "accept_page_007_as_complete_in_a_later_explicit_decision",
        "hold_page_007_for_corrections_or_additional_review",
    ]
    assert review["reading_order"] == [
        "spektral_krew_ui_art_anchor",
        "marco_proudfoot_body_left_column",
        "marco_proudfoot_body_right_column",
    ]
    blocks = {block["block_id"]: block for block in review["blocks"]}
    assert blocks["P007-B001"]["block_type"] == "visual_anchor"
    assert blocks["P007-B001"]["content_kind"] == "ui_art_anchor"
    assert blocks["P007-B001"]["extraction_policy"] == "anchor_only_defer_visual"
    assert blocks["P007-B001"]["character_count"] == 0
    assert blocks["P007-B001"]["anchor_metadata"]["anchor_id"] == "ART-G1-VIRAL-P007-001"
    assert blocks["P007-B001"]["anchor_metadata"]["not_source_text"] is True
    assert blocks["P007-B002"]["role"] == "marco_proudfoot_body_left_column"


def test_page_007_review_packet_packages_promo_body_and_semantic_maps():
    report = read_json(P007_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_007.png",
        "review_assets/1_P007-spektral-krew-ui-art-anchor.png",
        "review_assets/2_P007-marco-proudfoot-body-left.png",
        "review_assets/3_P007-marco-proudfoot-body-right.png",
        "review_assets/page_007_ocr_verified_text_map.md",
        "review_assets/page_007_semantic_text_map.json",
        "review_assets/page_007_semantic_text_map.md",
    }
    for package_path, attachment in attachments.items():
        target = P007_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    packet = P007_PACKET.read_text(encoding="utf-8-sig")
    assert "page 007 complete ok" in packet
    assert "hold page 007" in packet
    assert "This packet itself creates no acceptance" in packet
    assert "does not advance Gate 1" in packet
    assert "Content kind: `ui_art_anchor`" in packet
    assert "Anchor id: `ART-G1-VIRAL-P007-001`" in packet


def test_page_007_semantic_map_preserves_promo_article_and_page_continuation_boundary():
    semantic_map = read_json(P007_SEMANTIC_MAP_JSON)
    semantic_markdown = P007_SEMANTIC_MAP_MARKDOWN.read_text(encoding="utf-8-sig")
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}

    assert semantic_map["canonical"] is True
    assert semantic_map["map_id"] == "SM-G1-VIRAL-P007-003"
    assert semantic_map["package_id"] == "PCRP-G1-VIRAL-P007-003"
    assert semantic_map["semantic_validation"]["unit_count"] == 7
    assert "SPEKTRAL KREW" not in json.dumps(semantic_map)
    assert "Become a Patron" not in json.dumps(semantic_map)
    assert units["SU-P007-B002-S001"]["unit_type"] == "heading"
    assert units["SU-P007-B002-S001"]["text"] == "Marco 'Proudfoot' Maglioni (Lead Investigator)"
    assert units["SU-P007-B002-S002"]["unit_type"] == "paragraph"
    assert units["SU-P007-B002-S002"]["text"].endswith("Tolkien fan.")
    assert units["SU-P007-B002-S003"]["unit_type"] == "paragraph"
    assert units["SU-P007-B002-S003"]["text"].startswith("His family moved")
    assert units["SU-P007-B002-S003"]["continues_to"] == "SU-P007-B003-S001"
    assert units["SU-P007-B003-S001"]["unit_type"] == "continuation"
    assert units["SU-P007-B003-S001"]["continues_from"] == "SU-P007-B002-S003"
    assert units["SU-P007-B003-S002"]["text"].startswith("Spektral Krew actually started")
    assert units["SU-P007-B003-S003"]["text"].startswith("Marco is an absolute believer")
    assert units["SU-P007-B003-S004"]["text"].startswith("He came up with")
    assert units["SU-P007-B003-S004"]["text"].endswith("do things that you")
    assert units["SU-P007-B003-S004"]["page_boundary"] == "visible_text_continues_beyond_page_007_without_processing_page_008"
    assert "PAGE-008" not in json.dumps(semantic_map)
    assert "## Unit Summary" in semantic_markdown
    assert "## Unit Text" in semantic_markdown
    assert "page_complete_acceptance" in semantic_map["not_evidence_for"]


def test_page_007_text_map_uses_metadata_table_and_full_text_blocks():
    text_map = P007_TEXT_MAP.read_text(encoding="utf-8-sig")

    assert "| Unit | Text preview | Page | Heading level | Style |" in text_map
    assert "| SU-P007-B002-S001 | Marco 'Proudfoot' Maglioni" in text_map
    assert "Meet the Krew" not in text_map
    assert "Become a Patron" not in text_map
    assert "Become a Patreon" not in text_map
    assert "Marco 'Proudfoot' Maglioni" in text_map
    assert "### Full Text - SU-P007-B002-S001" in text_map
    assert "### Full Text - SU-P007-B002-S002" in text_map
    assert "### Full Text - SU-P007-B002-S003" in text_map
    assert "### Full Text - SU-P007-B003-S001" in text_map
    assert "### Full Text - SU-P007-B003-S004" in text_map
    assert "Tolkien fan. His family moved" not in text_map
    assert "EVERYTHING unexplained is demonic" in text_map
    assert "do things that you" in text_map


def test_page_001_review_packet_is_visual_title_ready_without_acceptance():
    report = read_json(P001_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P001-001"
    assert report["authorization_id"] == P001_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["P001TR-G1-VIRAL-001"]
    assert report["readiness_input"]["authorization_id"] == "BA-G1-VIRAL-PAGE-001-TRIAGE-001"
    assert review["expected_blocks"] == 3
    assert review["reviewed_blocks"] == 3
    assert review["ready_blocks"] == 3
    assert review["blockers"] == []
    assert review["open_questions"] == []
    assert review["semantic_units_validated"] is False
    assert review["decision_options"] == [
        "accept_page_001_as_complete_in_a_later_explicit_decision",
        "hold_page_001_for_corrections_or_additional_review",
    ]
    assert report["review_decision"]["requires_bogdan_decision"] is True
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["guardrails"]["ocr_executed"] is False
    assert report["guardrails"]["render_executed"] is False
    assert report["guardrails"]["pdf_opened_or_parsed"] is False
    assert report["guardrails"]["raw_artifacts_modified"] is False
    assert report["guardrails"]["push_authorized"] is False
    summary = (P001_OUT_ROOT / "page_complete_review_summary.md").read_text(encoding="utf-8-sig")
    assert "Inventory reconciliation: not_applicable_no_semantic_text_units" in summary


def test_page_001_review_packet_packages_cover_title_and_footer_anchors():
    report = read_json(P001_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_001.png",
        "review_assets/1_P001-full-page-cover-anchor.png",
        "review_assets/2_P001-title-logo-area.png",
        "review_assets/3_P001-footer-title-credit-like-block.png",
    }
    for package_path, attachment in attachments.items():
        target = P001_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    review = report["page_complete_review"]
    blocks = {block["block_id"]: block for block in review["blocks"]}
    assert blocks["P001-B001"]["content_kind"] == "cover_visual_anchor"
    assert blocks["P001-B001"]["extraction_policy"] == "anchor_only_defer_visual"
    assert blocks["P001-B001"]["anchor_metadata"]["anchor_id"] == "ART-G1-VIRAL-P001-001"
    assert blocks["P001-B002"]["content_kind"] == "title_visual_anchor"
    assert blocks["P001-B002"]["anchor_metadata"]["visible_text_hint"] == "VIRAL / UNREDACTED"
    assert blocks["P001-B003"]["content_kind"] == "mixed_footer_visual_anchor"
    assert all(block["character_count"] == 0 for block in blocks.values())
    assert all(block["anchor_metadata"]["not_source_text"] is True for block in blocks.values())

    packet = P001_PACKET.read_text(encoding="utf-8-sig")
    assert "page 001 complete ok" in packet
    assert "hold page 001" in packet
    assert "This packet itself creates no acceptance" in packet
    assert "Content kind: `title_visual_anchor`" in packet
    assert "Anchor id: `ART-G1-VIRAL-P001-002`" in packet


def test_page_009_review_packet_consumes_crop_text_and_semantic_predecessors_without_acceptance():
    report = read_json(P009_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P009-001"
    assert report["authorization_id"] == P009_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == [
        "P009TR-G1-VIRAL-003",
        "P009TXT-G1-VIRAL-001",
        "P009SEM-G1-VIRAL-001",
    ]
    assert review["expected_blocks"] == 4
    assert review["reviewed_blocks"] == 4
    assert review["ready_blocks"] == 4
    assert review["blockers"] == []
    assert review["structural_findings"] == []
    assert review["semantic_units_validated"] is True
    assert review["semantic_validation"]["valid"] is True
    assert review["markdown_projection_validation"]["valid"] is True
    assert review["inventory_reconciliation"]["valid"] is True
    assert review["decision_options"] == [
        "accept_page_009_as_complete_in_a_later_explicit_decision",
        "hold_page_009_for_corrections_or_additional_review",
    ]
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["guardrails"]["ocr_executed"] is False
    assert report["guardrails"]["source_acceptance_created"] is False
    assert report["guardrails"]["push_authorized"] is False


def test_page_009_review_packet_packages_text_evidence_and_semantic_assets():
    report = read_json(P009_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert {
        "review_assets/page_009.png",
        "review_assets/1_P009-left-portrait-image-area-readable.png",
        "review_assets/2_P009-right-portrait-image-area-readable.png",
        "review_assets/3_P009-left-profile-text-column-human-context.png",
        "review_assets/4_P009-right-profile-text-column-human-context.png",
        "review_assets/3b_P009-left-profile-text-column-text-evidence.png",
        "review_assets/4b_P009-right-profile-text-column-text-evidence.png",
        "review_assets/page_009_ocr_verified_text_map.md",
        "review_assets/page_009_semantic_text_map.json",
        "review_assets/page_009_semantic_text_map.md",
    }.issubset(set(attachments))
    for path in [P009_PACKET, P009_TEXT_MAP, P009_SEMANTIC_MAP_JSON, P009_SEMANTIC_MAP_MARKDOWN]:
        assert path.is_file()

    semantic_map = read_json(P009_SEMANTIC_MAP_JSON)
    assert semantic_map["package_id"] == "PCRP-G1-VIRAL-P009-001"
    assert len(semantic_map["units"]) == 14
    assert {unit["source_block_id"] for unit in semantic_map["units"]} == {"P009-B003", "P009-B004"}
    assert {tuple(unit["crop_ids"]) for unit in semantic_map["units"]} == {
        ("P009-B003-TEXT-EVIDENCE",),
        ("P009-B004-TEXT-EVIDENCE",),
    }


def test_page_010_review_packet_consumes_crop_text_and_semantic_predecessors_without_acceptance():
    report = read_json(P010_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P010-001"
    assert report["authorization_id"] == P010_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == [
        "P010TR-G1-VIRAL-001",
        "P010TXT-G1-VIRAL-001",
        "P010SEM-G1-VIRAL-001",
    ]
    assert review["expected_blocks"] == 6
    assert review["reviewed_blocks"] == 6
    assert review["ready_blocks"] == 6
    assert review["reading_order"] == [
        "upper_left_peter_continuation_gear_text",
        "lower_left_hyeon_profile_text_start",
        "upper_right_hyeon_continuation_appearance_gear_text",
        "lower_right_maya_profile_text_start",
        "left_hyeon_portrait_image_area_art_anchor",
        "right_maya_portrait_image_area_art_anchor",
    ]
    assert review["blockers"] == []
    assert review["structural_findings"] == []
    assert review["semantic_units_validated"] is True
    assert review["semantic_validation"]["valid"] is True
    assert review["markdown_projection_validation"]["valid"] is True
    assert review["inventory_reconciliation"]["valid"] is True
    assert review["decision_options"] == [
        "accept_page_010_as_complete_in_a_later_explicit_decision",
        "hold_page_010_for_corrections_or_additional_review",
    ]
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["guardrails"]["ocr_executed"] is False
    assert report["guardrails"]["source_acceptance_created"] is False
    assert report["guardrails"]["push_authorized"] is False


def test_page_010_review_packet_packages_text_evidence_and_semantic_assets():
    report = read_json(P010_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert report["review_asset_deduplication"]["schema_version"] == "sourcefold_review_asset_deduplication.v1"
    assert report["review_asset_deduplication"]["status"] == "passed"
    assert report["review_asset_deduplication"]["deduplicated_binding_count"] == 4
    assert len(report["package_assets"]) == 12
    assert len(report["review_attachments"]) == 16
    assert {
        "review_assets/page_010.png",
        "review_assets/3_P010-left-hyeon-portrait-image-area-human-context.png",
        "review_assets/4_P010-right-maya-portrait-image-area-human-context.png",
        "review_assets/1b_P010-upper-left-continuation-gear-text-evidence.png",
        "review_assets/5b_P010-lower-left-hyeon-profile-text-evidence.png",
        "review_assets/2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
        "review_assets/6b_P010-lower-right-maya-profile-text-evidence.png",
        "review_assets/page_010_ocr_verified_text_map.md",
        "review_assets/page_010_semantic_text_map.json",
        "review_assets/page_010_semantic_text_map.md",
    }.issubset(set(attachments))
    physical_paths = {asset["package_path"] for asset in report["package_assets"]}
    assert "review_assets/1_P010-upper-left-continuation-gear-human-context.png" not in physical_paths
    assert "review_assets/2_P010-upper-right-continuation-appearance-gear-human-context.png" not in physical_paths
    assert "review_assets/5_P010-lower-left-hyeon-profile-human-context.png" not in physical_paths
    assert "review_assets/6_P010-lower-right-maya-profile-human-context.png" not in physical_paths
    logical_human = {
        item["attachment_id"]: item
        for item in report["role_bindings"]
        if item["attachment_id"].startswith("P010-001-ATT-HUMAN-") and item.get("deduplicated_with")
    }
    assert logical_human == {
        "P010-001-ATT-HUMAN-UPPER-LEFT": {
            "attachment_id": "P010-001-ATT-HUMAN-UPPER-LEFT",
            "role": "human_context_crop",
            "package_path": "review_assets/1b_P010-upper-left-continuation-gear-text-evidence.png",
            "sha256": "C5B10AF894F47363FE406A6676803EA79378BDAF20251BF0C80D5BA2AB31C10A",
            "deduplicated_with": "P010-B001-TEXT-EVIDENCE",
            "original_package_path": "review_assets/1_P010-upper-left-continuation-gear-human-context.png",
        },
        "P010-001-ATT-HUMAN-UPPER-RIGHT": {
            "attachment_id": "P010-001-ATT-HUMAN-UPPER-RIGHT",
            "role": "human_context_crop",
            "package_path": "review_assets/2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
            "sha256": "8F27D91B5F3A27448C04119463F0D3A83BBA9FB086DE02756300A61734BF706A",
            "deduplicated_with": "P010-B002-TEXT-EVIDENCE",
            "original_package_path": "review_assets/2_P010-upper-right-continuation-appearance-gear-human-context.png",
        },
        "P010-001-ATT-HUMAN-LOWER-LEFT": {
            "attachment_id": "P010-001-ATT-HUMAN-LOWER-LEFT",
            "role": "human_context_crop",
            "package_path": "review_assets/5b_P010-lower-left-hyeon-profile-text-evidence.png",
            "sha256": "23F99207C9A7D86CEB740D1DD6608DB7B5B20E35DED71E782528711BB2915130",
            "deduplicated_with": "P010-B005-TEXT-EVIDENCE",
            "original_package_path": "review_assets/5_P010-lower-left-hyeon-profile-human-context.png",
        },
        "P010-001-ATT-HUMAN-LOWER-RIGHT": {
            "attachment_id": "P010-001-ATT-HUMAN-LOWER-RIGHT",
            "role": "human_context_crop",
            "package_path": "review_assets/6b_P010-lower-right-maya-profile-text-evidence.png",
            "sha256": "C5EAAD2782C5724AAD052868C2798B04773E2FC4C14A6EF3239EF504CC8E1946",
            "deduplicated_with": "P010-B006-TEXT-EVIDENCE",
            "original_package_path": "review_assets/6_P010-lower-right-maya-profile-human-context.png",
        },
    }
    delivery_paths = [item["package_path"] for item in report["delivery_assets"]]
    assert "review_assets/1_P010-upper-left-continuation-gear-human-context.png" not in delivery_paths
    assert "review_assets/2_P010-upper-right-continuation-appearance-gear-human-context.png" not in delivery_paths
    assert "review_assets/5_P010-lower-left-hyeon-profile-human-context.png" not in delivery_paths
    assert "review_assets/6_P010-lower-right-maya-profile-human-context.png" not in delivery_paths
    assert "review_assets/1b_P010-upper-left-continuation-gear-text-evidence.png" in delivery_paths
    assert "review_assets/2b_P010-upper-right-continuation-appearance-gear-text-evidence.png" in delivery_paths
    assert "review_assets/5b_P010-lower-left-hyeon-profile-text-evidence.png" in delivery_paths
    assert "review_assets/6b_P010-lower-right-maya-profile-text-evidence.png" in delivery_paths
    for path in [P010_PACKET, P010_TEXT_MAP, P010_SEMANTIC_MAP_JSON, P010_SEMANTIC_MAP_MARKDOWN]:
        assert path.is_file()

    semantic_map = read_json(P010_SEMANTIC_MAP_JSON)
    assert semantic_map["package_id"] == "P010SEM-G1-VIRAL-001"
    assert len(semantic_map["units"]) == 14
    assert [unit["crop_ids"][0] for unit in semantic_map["units"]] == [
        "P010-B001-TES",
        "P010-B001-TES",
        "P010-B001-TES",
        "P010-B005-TES",
        "P010-B005-TES",
        "P010-B005-TES",
        "P010-B002-TES",
        "P010-B002-TES",
        "P010-B002-TES",
        "P010-B002-TES",
        "P010-B002-TES",
        "P010-B006-TES",
        "P010-B006-TES",
        "P010-B006-TES",
    ]
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}
    assert units["SU-P010-HYEON-003"]["continues_to"] == "SU-P010-HYEON-004"
    assert units["SU-P010-HYEON-004"]["continues_from"] == "SU-P010-HYEON-003"
    assert units["SU-P010-MAYA-003"]["external_continues_to"] == "P011/Maya continuation"


def test_page_011_review_packet_consumes_crop_text_and_semantic_predecessors_without_acceptance():
    report = read_json(P011_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P011-001"
    assert report["authorization_id"] == P011_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == [
        "P011TR-G1-VIRAL-001",
        "P011TXT-G1-VIRAL-001",
        "P011SEM-G1-VIRAL-001",
    ]
    assert review["expected_blocks"] == 4
    assert review["reviewed_blocks"] == 4
    assert review["ready_blocks"] == 4
    assert review["reading_order"] == [
        "left_maya_continuation_secret_appearance_text",
        "right_emily_profile_text_start",
        "emily_em_lavigne_portrait_image_area_art_anchor",
        "lower_left_screen_image_area_art_anchor",
    ]
    assert review["blockers"] == []
    assert review["structural_findings"] == []
    assert review["semantic_units_validated"] is True
    assert review["semantic_validation"]["valid"] is True
    assert review["markdown_projection_validation"]["valid"] is True
    assert review["inventory_reconciliation"]["valid"] is True
    assert review["decision_options"] == [
        "accept_page_011_as_complete_in_a_later_explicit_decision",
        "hold_page_011_for_corrections_or_additional_review",
    ]
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["guardrails"]["ocr_executed"] is False
    assert report["guardrails"]["source_acceptance_created"] is False
    assert report["guardrails"]["push_authorized"] is False


def test_page_011_review_packet_packages_visual_anchors_and_layout_hinted_semantic_assets():
    report = read_json(P011_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert report["review_asset_deduplication"]["schema_version"] == "sourcefold_review_asset_deduplication.v1"
    assert report["review_asset_deduplication"]["status"] == "passed"
    assert report["review_asset_deduplication"]["deduplicated_binding_count"] == 2
    assert len(report["package_assets"]) == 10
    assert len(report["review_attachments"]) == 12
    assert {
        "review_assets/page_011.png",
        "review_assets/2_P011-emily-em-lavigne-portrait-image-area-human-context.png",
        "review_assets/3_P011-lower-left-screen-image-area-human-context.png",
        "review_assets/1b_P011-left-maya-continuation-secret-appearance-text-evidence.png",
        "review_assets/4b_P011-right-emily-profile-text-text-evidence.png",
        "review_assets/page_011_ocr_verified_text_map.md",
        "review_assets/page_011_semantic_text_map.json",
        "review_assets/page_011_semantic_text_map.md",
    }.issubset(set(attachments))
    physical_paths = {asset["package_path"] for asset in report["package_assets"]}
    assert "review_assets/1_P011-left-maya-continuation-secret-appearance-human-context.png" not in physical_paths
    assert "review_assets/4_P011-right-emily-profile-text-human-context.png" not in physical_paths
    assert "review_assets/2_P011-emily-em-lavigne-portrait-image-area-human-context.png" in physical_paths
    assert "review_assets/3_P011-lower-left-screen-image-area-human-context.png" in physical_paths
    delivery_paths = [item["package_path"] for item in report["delivery_assets"]]
    assert "review_assets/1_P011-left-maya-continuation-secret-appearance-human-context.png" not in delivery_paths
    assert "review_assets/4_P011-right-emily-profile-text-human-context.png" not in delivery_paths
    assert "review_assets/1b_P011-left-maya-continuation-secret-appearance-text-evidence.png" in delivery_paths
    assert "review_assets/4b_P011-right-emily-profile-text-text-evidence.png" in delivery_paths
    for path in [P011_PACKET, P011_TEXT_MAP, P011_SEMANTIC_MAP_JSON, P011_SEMANTIC_MAP_MARKDOWN]:
        assert path.is_file()

    semantic_map = read_json(P011_SEMANTIC_MAP_JSON)
    assert semantic_map["package_id"] == "P011SEM-G1-VIRAL-001"
    assert len(semantic_map["units"]) == 12
    assert {unit["source_block_id"] for unit in semantic_map["units"]} == {"P011-B001", "P011-B004"}
    assert [unit["crop_ids"][0] for unit in semantic_map["units"]] == [
        "P011-B001-TES",
        "P011-B001-TES",
        "P011-B001-TES",
        "P011-B001-TES",
        "P011-B001-TES",
        "P011-B001-TES",
        "P011-B001-TES",
        "P011-B004-TES",
        "P011-B004-TES",
        "P011-B004-TES",
        "P011-B004-TES",
        "P011-B004-TES",
    ]
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}
    assert units["SU-P011-MAYA-001"]["external_continues_from"] == "P010/SU-P010-MAYA-003"
    assert units["SU-P011-EMILY-003"]["layout_role"] == "inline_heading"
    assert units["SU-P011-EMILY-003"]["font_style"] == "italic"
    assert units["SU-P011-EMILY-003"]["line_break_after"] is False
    assert units["SU-P011-EMILY-003"]["continues_inline_to"] == "SU-P011-EMILY-004"
    assert units["SU-P011-EMILY-005"]["external_continues_to"] == "P012/Emily continuation"


def test_page_008_review_packet_is_ready_without_acceptance():
    report = read_json(P008_REPORT)
    review = report["page_complete_review"]

    assert report["package_id"] == "PCRP-G1-VIRAL-P008-001"
    assert report["authorization_id"] == P008_AUTH
    assert report["status"] == "ready_for_bogdan_page_complete_decision"
    assert report["scope"] == "page_complete_review_packet_only_no_acceptance"
    assert report["input_packages"] == ["P008-INLINE-MAP-G1-VIRAL-001"]
    assert review["expected_blocks"] == 7
    assert review["ready_blocks"] == 7
    assert review["blockers"] == []
    assert review["open_questions"] == []
    assert review["decision_options"] == [
        "accept_page_008_as_complete_in_a_later_explicit_decision",
        "hold_page_008_for_corrections_or_additional_review",
    ]
    assert report["review_decision"]["page_complete_acceptance_created"] is False
    assert report["review_decision"]["accepted_pages_as_complete"] == []
    assert report["review_decision"]["whole_gate_1_acceptance_created"] is False
    assert report["guardrails"]["push_authorized"] is False


def test_page_008_review_packet_packages_text_art_anchors_and_action_backlog():
    report = read_json(P008_REPORT)
    attachments = {attachment["package_path"]: attachment for attachment in report["review_attachments"]}

    assert set(attachments) == {
        "review_assets/page_008.png",
        "review_assets/1_P008-marco-proudfoot-body-continuation.png",
        "review_assets/2_P008-marco-proudfoot-appearance-gear.png",
        "review_assets/3_P008-corrina-trench-portrait-anchor.png",
        "review_assets/4_P008-corrina-trench-body-left.png",
        "review_assets/5_P008-corrina-trench-body-right.png",
        "review_assets/6_P008-corrina-trench-appearance-gear.png",
        "review_assets/7_P008-crystal-object-art-anchor.png",
        "review_assets/page_008_ocr_verified_text_map.md",
        "review_assets/page_008_semantic_text_map.json",
        "review_assets/page_008_semantic_text_map.md",
        "review_assets/page_008_action_backlog.md",
    }
    for package_path, attachment in attachments.items():
        target = P008_OUT_ROOT / package_path
        assert target.is_file()
        assert attachment["sha256"]

    packet = P008_PACKET.read_text(encoding="utf-8-sig")
    assert "page 008 complete ok" in packet
    assert "hold page 008" in packet
    assert "Content kind: `photo_anchor`" in packet
    assert "Content kind: `art_anchor`" in packet
    assert "Anchor id: `ART-G1-VIRAL-P008-001`" in packet
    assert "Anchor id: `ART-G1-VIRAL-P008-002`" in packet

    backlog = P008_ACTION_BACKLOG.read_text(encoding="utf-8-sig")
    assert "Tool:view_image" in backlog
    assert "Script:build_page_complete_review.py" in backlog
    assert "Review packet only" in backlog


def test_page_008_semantic_map_preserves_art_anchors_and_paragraph_boundaries():
    semantic_map = read_json(P008_SEMANTIC_MAP_JSON)
    semantic_markdown = P008_SEMANTIC_MAP_MARKDOWN.read_text(encoding="utf-8-sig")
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}

    assert semantic_map["canonical"] is True
    assert semantic_map["map_id"] == "SM-G1-VIRAL-P008-001"
    assert semantic_map["package_id"] == "PCRP-G1-VIRAL-P008-001"
    assert semantic_map["semantic_validation"]["valid"] is True
    assert semantic_map["semantic_validation"]["unit_count"] == 14
    assert "ART-G1-VIRAL-P008-001" not in json.dumps(semantic_map)
    assert "ART-G1-VIRAL-P008-002" not in json.dumps(semantic_map)
    assert units["SU-P008-B001-S001"]["unit_type"] == "continuation"
    assert units["SU-P008-B001-S001"]["page_boundary"] == "visible_text_continues_from_page_007_without_processing_page_007"
    assert units["SU-P008-B004-S001"]["unit_type"] == "heading"
    assert units["SU-P008-B004-S002"]["unit_type"] == "paragraph"
    assert "continues_to" not in units["SU-P008-B004-S002"]
    assert units["SU-P008-B005-S001"]["unit_type"] == "paragraph"
    assert "continues_from" not in units["SU-P008-B005-S001"]
    assert units["SU-P008-B005-S002"]["text"].startswith("In preparation for this investigation")
    assert all("\n\n" not in unit["text"] for unit in semantic_map["units"])
    assert "## Unit Summary" in semantic_markdown
    assert "page_complete_acceptance" in semantic_map["not_evidence_for"]


def test_page_008_text_map_uses_metadata_table_and_full_text_blocks():
    text_map = P008_TEXT_MAP.read_text(encoding="utf-8-sig")

    assert "| Unit | Text preview | Page | Heading level | Style |" in text_map
    assert "### Full Text - SU-P008-B001-S001" in text_map
    assert "### Full Text - SU-P008-B005-S002" in text_map
    assert "Corrina Trench (Investigator)" in text_map
    assert "People tend to judge her" in text_map
    assert "Crystal/object art" not in text_map
    assert "Corrina Trench (Investigator) Corrina is a firm believer" not in text_map
