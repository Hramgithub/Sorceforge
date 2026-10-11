from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_full_page_geometry_probe_p018_p017.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_full_page_geometry_probe_p018_p017_G1_VIRAL_001"
)
REPORT = OUT / "full_page_geometry_probe_p018_p017_report.json"
SUMMARY = OUT / "full_page_geometry_probe_p018_p017_summary.md"
MANIFEST = OUT / "full_page_geometry_probe_p018_p017_manifest.md"


def report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_full_page_geometry_probe_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FULL-PAGE-GEOMETRY-P018-P017-001" in source
    assert "зови сол и терру" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source


def test_full_page_geometry_probe_exact_scope_and_no_leak_boundary() -> None:
    data = report()
    assert data["lane_id"] == "C01TEFG017018-G1-VIRAL-001"
    assert data["source_reference_guided_repair"] == "C01TERG018017-G1-VIRAL-001"
    assert data["pages"] == ["018", "017"]
    assert data["candidate_generation_reference_text_used"] is False
    assert data["reference_text_loaded_after_candidate_hashing"] is True
    assert data["reference_guided_repair_used"] is False
    assert data["independent_ocr_candidate"] is True


def test_full_page_geometry_probe_reaches_ok_level_independent_candidates() -> None:
    data = report()
    assert data["all_pages_ok_level"] is True
    p018 = data["best_by_page"]["018"]
    p017 = data["best_by_page"]["017"]
    assert p018["candidate_id"] == "full_page_expanded_overlap_psm4"
    assert p018["metrics"]["sequence_similarity_ratio"] == 0.999466
    assert p018["metrics"]["token_recall"] == 0.996067
    assert p018["ok_level_candidate"] is True
    assert p017["candidate_id"] == "full_page_bright_title_body_psm7_4_4"
    assert p017["metrics"]["sequence_similarity_ratio"] == 0.99923
    assert p017["metrics"]["token_recall"] == 0.997859
    assert p017["ok_level_candidate"] is True


def test_full_page_geometry_probe_outputs_and_negative_capabilities() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert (OUT / "rankings" / "page_018_candidate_rankings.json").exists()
    assert (OUT / "rankings" / "page_017_candidate_rankings.json").exists()
    for page in data["best_by_page"].values():
        assert page["candidate_text_path"]
        assert page["source_page_image_path"].endswith(".png")
        assert page["reference_label"] == "reference_text_map_not_ocr_verified"
        for item in page["region_results"]:
            assert item["page_space_box"]
            assert item["ocr_result"]["prepared_region_path"]
            assert item["ocr_result"]["raw_ocr_text_path"]
            assert item["ocr_result"]["raw_ocr_tsv_path"]
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
