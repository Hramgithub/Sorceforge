import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_009_semantic_text_map.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_009_semantic_text_map_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_009_semantic_text_map_report.json"
SEMANTIC_JSON = OUT_ROOT / "page_009_semantic_text_map.json"
SEMANTIC_MD = OUT_ROOT / "page_009_semantic_text_map.md"
SUMMARY = OUT_ROOT / "page_009_semantic_text_map_summary.md"
AUTH = "BA-G1-VIRAL-PAGE-009-SEMANTIC-TEXT-MAP-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_009_semantic_text_map_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-009-TEXT-EXTRACTION-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_009_semantic_map_validates_units_projection_inventory_and_crop_links():
    report = read_json(REPORT)

    assert report["package_id"] == "P009SEM-G1-VIRAL-001"
    assert report["authorization_id"] == AUTH
    assert report["status"] == "semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance"
    assert report["unit_count"] == 14
    assert report["semantic_validation"]["valid"] is True
    assert report["markdown_projection_validation"]["valid"] is True
    assert report["crop_linkage_validation"]["valid"] is True
    assert report["inventory_reconciliation"]["valid"] is True
    assert report["pcrp_created"] is False
    assert report["page_complete_acceptance_created"] is False
    assert report["source_acceptance_created"] is False
    assert report["ocr_acceptance_created"] is False


def test_page_009_semantic_map_splits_headings_paragraphs_and_boxed_sections():
    semantic_map = read_json(SEMANTIC_JSON)
    units = {unit["unit_id"]: unit for unit in semantic_map["units"]}

    assert semantic_map["map_id"] == "SM-G1-VIRAL-P009-001"
    assert semantic_map["package_id"] == "P009SEM-G1-VIRAL-001"
    assert units["SU-P009-L-001"]["unit_type"] == "heading"
    assert units["SU-P009-L-001"]["heading_level"] == "h2"
    assert units["SU-P009-L-005"]["text"] == "APPEARANCE"
    assert units["SU-P009-L-005"]["heading_level"] == "h3"
    assert units["SU-P009-L-007"]["text"] == "GEAR CARRIED"
    assert units["SU-P009-R-001"]["heading_level"] == "h2"
    assert units["SU-P009-R-005"]["heading_level"] == "h3"
    assert all("\n\n" not in unit["text"] for unit in semantic_map["units"])
    assert units["SU-P009-L-002"]["crop_ids"] == ["P009-B003-TEXT-EVIDENCE"]
    assert units["SU-P009-R-002"]["crop_ids"] == ["P009-B004-TEXT-EVIDENCE"]


def test_page_009_semantic_markdown_and_summary_are_review_only():
    markdown = SEMANTIC_MD.read_text(encoding="utf-8-sig")
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "## Unit Summary" in markdown
    assert "## Unit Text" in markdown
    assert "Enoch Jeremiah Eakins" in markdown
    assert "Peter Wharton" in markdown
    assert "page_complete_acceptance" in markdown
    assert "semantic_text_map_ready_for_bogdan_review_no_pcrp_acceptance" in summary
    assert "p009 semantic map ok" in summary
