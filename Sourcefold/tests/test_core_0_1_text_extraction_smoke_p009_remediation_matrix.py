import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_smoke_p009_remediation_matrix.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUTPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-REMEDIATION-MATRIX-001"
HUMAN_DECISION = "иди по этому плану 1-5"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_text_extraction_smoke_p009_remediation_matrix_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-WRONG",
            "--decision",
            HUMAN_DECISION,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            AUTHORIZATION_ID,
            "--decision",
            "remediate",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_text_extraction_smoke_p009_remediation_matrix_boundary_flags():
    report = read_json(OUTPUT_ROOT / "remediation_report.json")
    assert report["matrix_id"] == "C01TESRM-G1-VIRAL-001"
    assert report["status"] == "candidate_only_p009_remediation_matrix_completed"
    assert report["source_smoke"] == "C01TESP-G1-VIRAL-001"
    assert report["old_broad_runner_reused"] is False
    assert report["page"] == "009"
    assert report["page_021_plus_included"] is False
    assert report["ocr_execution_performed"] is True
    assert report["pdf_parsing_performed"] is False
    assert report["pdf_text_layer_extraction_performed"] is False
    assert report["render_execution_performed"] is False
    assert report["source_or_raw_mutation_performed"] is False
    assert report["accepted_text_mutation_performed"] is False
    assert report["runtime_implementation_created"] is False
    assert report["runtime_start_performed"] is False
    assert report["translation_or_proofreading_performed"] is False
    assert report["push_performed"] is False
    assert report["input_policy"] == "read_only_existing_p009_text_evidence_crops"
    assert report["output_policy"] == "candidate_only_separate_remediation_directory"


def test_core_0_1_text_extraction_smoke_p009_remediation_matrix_dimensions():
    report = read_json(OUTPUT_ROOT / "remediation_report.json")
    assert set(report["psm_modes"]) == {4, 6, 11}
    assert {"edge_mask_trim", "grayscale_autocontrast", "binary_threshold", "denoise_sharpen"}.issubset(
        set(report["preprocessing_variants"])
    )
    assert {"full_column", "split_header_body"}.issubset(set(report["strategies"]))
    assert report["candidate_count"] == len(report["candidate_results"])
    assert len(report["variant_rankings"]) == report["candidate_count"]
    assert report["baseline_similarity"] == 0.460269
    assert 0 <= report["best_similarity"] <= 1


def test_core_0_1_text_extraction_smoke_p009_remediation_matrix_outputs_are_separate():
    report = read_json(OUTPUT_ROOT / "remediation_report.json")
    for item in report["candidate_results"]:
        assert "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001" in item["candidate_text_path"]
        assert "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001" in item["normalized_text_path"]
        for raw in item["raw_outputs"]:
            assert "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001" in raw["prepared_input_path"]
            assert "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001" in raw["txt_path"]
            assert "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001" in raw["tsv_path"]
            assert "page_complete_review_p009_G1_VIRAL_001" not in raw["txt_path"]
    assert (OUTPUT_ROOT / "variant_rankings.json").exists()
    assert (OUTPUT_ROOT / "remediation_summary.md").exists()
    assert (OUTPUT_ROOT / "remediation_manifest.md").exists()
