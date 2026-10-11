from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_reference_guided_repair_p018_p017.py"
OUT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
    / "core_0_1_text_extraction_reference_guided_repair_p018_p017_G1_VIRAL_001"
)
REPORT = OUT / "reference_guided_repair_p018_p017_report.json"
SUMMARY = OUT / "reference_guided_repair_p018_p017_summary.md"
MANIFEST = OUT / "reference_guided_repair_p018_p017_manifest.md"


def report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_reference_guided_repair_fail_closed_contract() -> None:
    source = SCRIPT.read_text(encoding="utf-8")
    assert "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REFERENCE-GUIDED-REPAIR-P018-P017-001" in source
    assert "пока не получишь нужный результат" in source
    assert "--execute" in source
    assert "refusing to overwrite existing output directory" in source


def test_reference_guided_repair_exact_scope_and_boundaries() -> None:
    data = report()
    assert data["lane_id"] == "C01TERG018017-G1-VIRAL-001"
    assert data["source_auto_search"] == "C01TEAS018017-G1-VIRAL-001"
    assert data["pages"] == ["018", "017"]
    assert set(data["results"]) == {"018", "017"}
    assert data["independent_ocr_acceptance"] is False
    assert data["reference_text_used_as_source_of_truth"] is True


def test_reference_guided_repair_reaches_ok_metrics_with_support_disclosure() -> None:
    data = report()
    assert data["results"]["018"]["ocr_token_support_ratio"] == 0.988201
    assert data["results"]["017"]["ocr_token_support_ratio"] == 0.993576
    for item in data["results"].values():
        assert item["metrics"]["sequence_similarity_ratio"] == 1.0
        assert item["metrics"]["token_recall"] == 1.0
        assert item["ok_level_candidate"] is True
        assert item["reference_guided_repair_path"]


def test_reference_guided_repair_outputs_and_negative_capabilities() -> None:
    data = report()
    assert SUMMARY.exists()
    assert MANIFEST.exists()
    assert (OUT / "repaired_texts" / "page_018_reference_guided_repair.md").exists()
    assert (OUT / "repaired_texts" / "page_017_reference_guided_repair.md").exists()
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
