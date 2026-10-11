import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_replay_regression_smoke_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_replay_regression_smoke_trim_mask_psm4_G1_VIRAL_001"
REPORT = OUT_ROOT / "replay_report.json"
SUMMARY = OUT_ROOT / "replay_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REPLAY-REGRESSION-SMOKE-TRIM-MASK-PSM4-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_replay_regression_smoke_is_fail_closed():
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
            "делай",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_replay_regression_smoke_uses_frozen_config_only():
    report = read_json(REPORT)

    assert report["replay_id"] == "C01TERSM-G1-VIRAL-001"
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["source_frozen_profile_config"] == "C01TEFPC-G1-VIRAL-001"
    assert report["profile_id"] == "trim_mask_psm4"
    assert report["profile_tuple"]["preprocessing_variant"] == "edge_mask_trim"
    assert report["profile_tuple"]["tesseract_psm"] == 4
    assert report["candidate_count"] == 1
    assert report["old_broad_runner_reused"] is False
    assert (
        report["verified_inputs"]["C01TEFPC-G1-VIRAL-001.config"]["sha256"]
        == "4807057B7F043DC197651CD7DBCA40496FA4CAFCD7F08ECE6A59A306C14D7987"
    )


def test_replay_regression_smoke_exact_pages_inputs_and_reference_labels():
    report = read_json(REPORT)

    assert report["pages"] == ["009", "010", "015"]
    assert report["input_count"] == 8
    page_results = {item["page"]: item for item in report["page_results"]}
    assert page_results["009"]["input_count"] == 2
    assert page_results["010"]["input_count"] == 4
    assert page_results["015"]["input_count"] == 2
    assert page_results["009"]["reference_label"] == "reference_ocr_verified_text_map"
    assert page_results["010"]["reference_label"] == "reference_ocr_verified_text_map"
    assert page_results["015"]["reference_label"] == "reference_text_map_not_ocr_verified"
    assert "page_015_text_map.md" in page_results["015"]["reference_text_map"]

    input_paths = [raw["source_input_path"] for page in report["page_results"] for raw in page["raw_outputs"]]
    assert len(input_paths) == 8
    assert not any("page_016" in path or "page_021" in path for path in input_paths)
    assert not any("visual-anchor" in path or "page_015.png" in path for path in input_paths)
    assert input_paths[0].endswith("3b_P009-left-profile-text-column-text-evidence.png")
    assert input_paths[1].endswith("4b_P009-right-profile-text-column-text-evidence.png")
    assert input_paths[2].endswith("1b_P010-upper-left-continuation-gear-text-evidence.png")
    assert input_paths[3].endswith("5b_P010-lower-left-hyeon-profile-text-evidence.png")
    assert input_paths[4].endswith("2b_P010-upper-right-continuation-appearance-gear-text-evidence.png")
    assert input_paths[5].endswith("6b_P010-lower-right-maya-profile-text-evidence.png")
    assert input_paths[6].endswith("1_P015-timeline-text-evidence.png")
    assert input_paths[7].endswith("2_P015-history-text-evidence.png")


def test_replay_regression_smoke_boundary_flags_and_metrics():
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert report["ocr_execution_performed"] is True
    assert report["pdf_parsing_performed"] is False
    assert report["pdf_text_layer_extraction_performed"] is False
    assert report["render_execution_performed"] is False
    assert report["source_or_raw_mutation_performed"] is False
    assert report["accepted_text_mutation_performed"] is False
    assert report["semantic_text_mutation_performed"] is False
    assert report["page_status_mutation_performed"] is False
    assert report["source_profile_acceptance_created"] is False
    assert report["runtime_source_profile_lock_created"] is False
    assert report["runtime_implementation_created"] is False
    assert report["runtime_start_performed"] is False
    assert report["page_016_plus_included"] is False
    assert report["page_021_plus_included"] is False
    assert report["push_performed"] is False
    assert report["aggregate_metrics"]["input_count"] == 8
    assert report["aggregate_metrics"]["min_sequence_similarity_ratio"] >= 0.997
    assert report["aggregate_metrics"]["min_token_recall"] >= 0.993
    assert "candidate-only replay" in summary
