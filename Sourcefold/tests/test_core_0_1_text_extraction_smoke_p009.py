import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_smoke_p009.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P009_ROOT = TRIAL_ROOT / "page_complete_review_p009_G1_VIRAL_001" / "review_assets"
OUTPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_G1_VIRAL_001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P009-001"
HUMAN_DECISION = "теперь согласен, приступай"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_text_extraction_smoke_p009_is_fail_closed():
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
            "приступай",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_text_extraction_smoke_p009_outputs_are_candidate_only():
    report = read_json(OUTPUT_ROOT / "smoke_report.json")
    assert report["smoke_id"] == "C01TESP-G1-VIRAL-001"
    assert report["status"] == "candidate_ocr_smoke_completed_no_source_mutation"
    assert report["source_decision"] == "C01TETD-G1-VIRAL-001"
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
    assert report["output_policy"] == "candidate_only_separate_directory"


def test_core_0_1_text_extraction_smoke_p009_did_not_overwrite_p009_inputs():
    report = read_json(OUTPUT_ROOT / "smoke_report.json")
    expected_inputs = {
        "P009.left_profile_text_evidence": P009_ROOT / "3b_P009-left-profile-text-column-text-evidence.png",
        "P009.right_profile_text_evidence": P009_ROOT / "4b_P009-right-profile-text-column-text-evidence.png",
        "P009.reference_ocr_verified_text_map": P009_ROOT / "page_009_ocr_verified_text_map.md",
        "P009.reference_semantic_map": P009_ROOT / "page_009_semantic_text_map.md",
        "P009.reference_semantic_json": P009_ROOT / "page_009_semantic_text_map.json",
        "P009.full_page_image_read_only": P009_ROOT / "page_009.png",
    }
    for key, path in expected_inputs.items():
        item = report["verified_inputs"][key]
        assert Path(ROOT / item["path"]) == path
        assert item["sha256"]

    output_paths = [Path(item["path"]) for item in report["raw_results"].values() for item in [{"path": item["txt_path"]}, {"path": item["tsv_path"]}]]
    for path in output_paths:
        assert "core_0_1_text_extraction_smoke_p009_G1_VIRAL_001" in path.as_posix()


def test_core_0_1_text_extraction_smoke_p009_metrics_exist():
    report = read_json(OUTPUT_ROOT / "smoke_report.json")
    metrics = report["metrics"]
    assert metrics["normalized_candidate_chars"] > 0
    assert metrics["reference_chars"] > 0
    assert 0 <= metrics["sequence_similarity_ratio"] <= 1
    assert (OUTPUT_ROOT / "candidate_text.md").exists()
    assert (OUTPUT_ROOT / "normalized_candidate_text.txt").exists()
    assert (OUTPUT_ROOT / "smoke_manifest.md").exists()
