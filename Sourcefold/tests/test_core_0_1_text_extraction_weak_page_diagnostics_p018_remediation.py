from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_weak_page_diagnostics_p018_remediation.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_weak_page_diagnostics_p018_remediation_G1_VIRAL_001"
)
REPORT = OUT / "weak_diagnostics_p018_remediation_report.json"
SUMMARY = OUT / "weak_diagnostics_p018_remediation_summary.md"
MANIFEST = OUT / "weak_diagnostics_p018_remediation_manifest.md"


def load_report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_weak_diagnostics_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-WEAK-DIAGNOSTICS-P018-REMEDIATION-001" in source
    assert "ок иди по плану 1-7" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source


def test_weak_diagnostics_exact_scope_and_artifact_policy() -> None:
    report = load_report()
    assert report["lane_id"] == "C01TEWDR-G1-VIRAL-001"
    assert report["source_overview"] == "C01TEOR020-G1-VIRAL-001"
    assert report["diagnostic_pages"] == ["012", "013", "014", "016", "017", "018", "019", "020"]
    assert report["mini_replay_pages"] == ["017", "019", "014"]
    assert report["p018_remediation_performed"] is True

    for page in report["diagnostics"]:
        assert page["status"] == "diagnostic_completed"
        assert page["candidate_text_path"]
        assert page["input_results"]
        for item in page["input_results"]:
            assert item["prepared_input_path"]
            assert item["raw_ocr_text_path"]
            assert item["raw_ocr_tsv_path"]
            assert item["stderr_path"]
            assert item["stdout_path"]


def test_p018_remediation_and_mini_replay_results_are_recorded() -> None:
    report = load_report()
    remediation = report["p018_remediation"]
    best = remediation["best_candidate"]
    assert remediation["candidate_count"] == 14
    assert best["candidate_id"] == "wide_edge_mask_trim_psm4_normal"
    assert best["metrics"]["sequence_similarity_ratio"] == 0.814888
    assert best["metrics"]["token_recall"] == 0.976401
    assert best["assembly_order"] == "normal"

    mini = {item["page"]: item for item in report["mini_replay"]["pages"]}
    assert sorted(mini) == ["014", "017", "019"]
    assert mini["017"]["metrics"]["sequence_similarity_ratio"] == 0.825557
    assert mini["019"]["metrics"]["sequence_similarity_ratio"] == 0.534684
    assert mini["014"]["metrics"]["sequence_similarity_ratio"] == 0.766091


def test_weak_diagnostics_boundaries_and_outputs() -> None:
    report = load_report()
    assert report["accepted_text_mutation_performed"] is False
    assert report["semantic_text_mutation_performed"] is False
    assert report["page_status_mutation_performed"] is False
    assert report["source_or_raw_mutation_performed"] is False
    assert report["pdf_text_layer_extraction_performed"] is False
    assert report["render_execution_performed"] is False
    assert report["runtime_implementation_created"] is False
    assert report["runtime_start_performed"] is False
    assert report["page_021_plus_included"] is False
    assert report["push_performed"] is False

    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert (OUT / "p018_remediation_matrix" / "p018_candidate_rankings.json").exists()
    assert not any("page_021" in path.as_posix().lower() for path in OUT.rglob("*"))
