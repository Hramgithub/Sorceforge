import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_010_semantic_text_map.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_010_semantic_text_map_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_010_semantic_text_map_report.json"
SEMANTIC_JSON = OUT_ROOT / "page_010_semantic_text_map.json"
SEMANTIC_MD = OUT_ROOT / "page_010_semantic_text_map.md"
SUMMARY = OUT_ROOT / "page_010_semantic_text_map_summary.md"
AUTH = "BA-G1-VIRAL-PAGE-010-SEMANTIC-TEXT-MAP-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_010_semantic_text_map_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-010-TEXT-EXTRACTION-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_010_semantic_map_validates_units_projection_inventory_and_gates():
    report = read_json(REPORT)

    assert report["package_id"] == "P010SEM-G1-VIRAL-001"
    assert report["authorization_id"] == AUTH
    assert report["status"] == "semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance"
    assert report["unit_count"] == 14
    assert report["semantic_validation"]["valid"] is True
    assert report["markdown_projection_validation"]["valid"] is True
    assert report["crop_linkage_validation"]["valid"] is True
    assert report["inventory_reconciliation"]["valid"] is True
    assert report["text_extraction_consumer_gate"]["status"] == "passed"
    assert report["human_review_gate"]["status"] == "passed"
    assert report["pcrp_created"] is False
    assert report["page_complete_acceptance_created"] is False
    assert report["source_acceptance_created"] is False
    assert report["ocr_acceptance_created"] is False
    assert report["pages_011_020_processing_created"] is False


def test_page_010_semantic_map_preserves_logical_order_and_continuations():
    semantic_map = read_json(SEMANTIC_JSON)
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}
    ordered_crop_ids = [unit["crop_ids"][0] for unit in semantic_map["units"]]

    assert semantic_map["map_id"] == "SM-G1-VIRAL-P010-001"
    assert semantic_map["package_id"] == "P010SEM-G1-VIRAL-001"
    assert ordered_crop_ids == [
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
    assert units["SU-P010-HYEON-003"]["continues_to"] == "SU-P010-HYEON-004"
    assert units["SU-P010-HYEON-004"]["continues_from"] == "SU-P010-HYEON-003"
    assert units["SU-P010-PETER-001"]["external_continues_from"] == "P009/SU-P009-R-006"
    assert units["SU-P010-MAYA-003"]["external_continues_to"] == "P011/Maya continuation"


def test_page_010_semantic_map_splits_headings_paragraphs_and_crop_links():
    semantic_map = read_json(SEMANTIC_JSON)
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}

    assert units["SU-P010-HYEON-001"]["unit_type"] == "heading"
    assert units["SU-P010-HYEON-001"]["heading_level"] == "h2"
    assert units["SU-P010-HYEON-005"]["text"] == "APPEARANCE"
    assert units["SU-P010-HYEON-005"]["heading_level"] == "h3"
    assert units["SU-P010-HYEON-007"]["text"] == "GEAR CARRIED"
    assert units["SU-P010-MAYA-001"]["heading_level"] == "h2"
    assert all("\n\n" not in unit["text"] for unit in semantic_map["units"])
    assert units["SU-P010-HYEON-002"]["crop_ids"] == ["P010-B005-TES"]
    assert units["SU-P010-HYEON-004"]["crop_ids"] == ["P010-B002-TES"]
    assert units["SU-P010-MAYA-002"]["crop_ids"] == ["P010-B006-TES"]


def test_page_010_semantic_markdown_and_summary_are_review_only():
    markdown = SEMANTIC_MD.read_text(encoding="utf-8-sig")
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "## Unit Summary" in markdown
    assert "## Unit Text" in markdown
    assert "Ku Hyeon" in markdown
    assert "Maya Adeduwon" in markdown
    assert "page_complete_acceptance" in markdown
    assert "semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance" in summary
    assert "p010 semantic map ok" in summary
