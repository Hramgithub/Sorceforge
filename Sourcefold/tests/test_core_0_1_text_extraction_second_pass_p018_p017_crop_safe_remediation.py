from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_second_pass_p018_p017_crop_safe_remediation.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_second_pass_p018_p017_crop_safe_remediation_G1_VIRAL_001"
)
REPORT = OUT / "second_pass_p018_p017_report.json"
SUMMARY = OUT / "second_pass_p018_p017_summary.md"
MANIFEST = OUT / "second_pass_p018_p017_manifest.md"


def report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_second_pass_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SECOND-PASS-P018-P017-CROP-SAFE-001" in source
    assert "ок , собери план , сделай коммит и пробуй дальше" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source


def test_second_pass_exact_scope_and_candidate_matrix() -> None:
    data = report()
    assert data["lane_id"] == "C01TEP2P018P017-G1-VIRAL-001"
    assert data["source_diagnostics"] == "C01TEWDR-G1-VIRAL-001"
    assert data["pages"] == ["018", "017"]
    assert data["candidate_count_per_page"] == 18
    assert set(data["best_by_page"]) == {"018", "017"}
    assert len(data["shared_candidate_rankings"]) == 18


def test_second_pass_best_results_are_recorded() -> None:
    data = report()
    p018 = data["best_by_page"]["018"]
    p017 = data["best_by_page"]["017"]
    shared = data["shared_candidate_rankings"][0]
    assert p018["candidate_id"] == "wide_edge_mask_trim_psm11"
    assert p018["metrics"]["sequence_similarity_ratio"] == 0.81659
    assert p018["metrics"]["token_recall"] == 0.974435
    assert p017["candidate_id"] == "wide_edge_mask_trim_psm4"
    assert p017["metrics"]["sequence_similarity_ratio"] == 0.825557
    assert p017["metrics"]["token_recall"] == 0.987152
    assert shared["candidate_id"] == "wide_edge_mask_trim_psm11"
    assert shared["min_similarity"] == 0.81659


def test_second_pass_outputs_and_boundaries() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert (OUT / "rankings" / "page_018_candidate_rankings.json").exists()
    assert (OUT / "rankings" / "page_017_candidate_rankings.json").exists()
    for page in data["best_by_page"].values():
        assert page["candidate_text_path"]
        for item in page["input_results"]:
            assert item["prepared_input_path"]
            assert item["raw_ocr_text_path"]
            assert item["raw_ocr_tsv_path"]
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
