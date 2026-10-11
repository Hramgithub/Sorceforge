from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_auto_search_p018_p017_column_line_segmentation.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_auto_search_p018_p017_column_line_segmentation_G1_VIRAL_001"
)
REPORT = OUT / "auto_search_p018_p017_report.json"
SUMMARY = OUT / "auto_search_p018_p017_summary.md"
MANIFEST = OUT / "auto_search_p018_p017_manifest.md"


def report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_auto_search_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-AUTO-SEARCH-P018-P017-COLUMN-LINE-001" in source
    assert "без остановок на меня" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source


def test_auto_search_exact_scope_and_budget() -> None:
    data = report()
    assert data["lane_id"] == "C01TEAS018017-G1-VIRAL-001"
    assert data["source_second_pass"] == "C01TEP2P018P017-G1-VIRAL-001"
    assert data["pages"] == ["018", "017"]
    assert data["candidate_budget"] == 7
    assert set(data["candidate_count_attempted_per_page"]) == {"018", "017"}
    assert set(data["best_by_page"]) == {"018", "017"}


def test_auto_search_records_stop_status_and_best_results() -> None:
    data = report()
    assert data["auto_stop_reason"]
    for best in data["best_by_page"].values():
        assert best["candidate_id"]
        assert best["candidate_text_path"]
        assert "sequence_similarity_ratio" in best["metrics"]
        assert "token_recall" in best["metrics"]
        assert isinstance(best["ok_level_candidate"], bool)


def test_auto_search_outputs_and_boundaries() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert (OUT / "rankings" / "page_018_candidate_rankings.json").exists()
    assert (OUT / "rankings" / "page_017_candidate_rankings.json").exists()
    for page in data["best_by_page"].values():
        for item in page["input_results"]:
            assert item["region_count"] >= 1
            for region in item["regions"]:
                assert region["region_path"]
                assert region["raw_ocr_text_path"]
                assert region["raw_ocr_tsv_path"]
    assert data["accepted_text_mutation_performed"] is False
    assert data["semantic_text_mutation_performed"] is False
    assert data["page_status_mutation_performed"] is False
    assert data["source_or_raw_mutation_performed"] is False
    assert data["pdf_text_layer_extraction_performed"] is False
    assert data["render_execution_performed"] is False
    assert data["runtime_implementation_created"] is False
    assert data["runtime_start_performed"] is False
    assert data["page_021_plus_included"] is False
    assert data["push_performed"] is False
