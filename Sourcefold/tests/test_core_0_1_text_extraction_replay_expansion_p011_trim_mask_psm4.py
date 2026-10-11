import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_replay_expansion_p011_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_replay_expansion_p011_trim_mask_psm4_G1_VIRAL_001"
REPORT = OUT_ROOT / "replay_expansion_report.json"
SUMMARY = OUT_ROOT / "replay_expansion_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REPLAY-EXPANSION-P011-TRIM-MASK-PSM4-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_p011_replay_expansion_is_fail_closed():
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
            "bounded replay expansion внутри 001-020",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_p011_replay_expansion_uses_frozen_tuple_without_broadening_config():
    report = read_json(REPORT)

    assert report["expansion_id"] == "C01TEREP011-G1-VIRAL-001"
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["source_frozen_profile_config"] == "C01TEFPC-G1-VIRAL-001"
    assert report["frozen_config_tuple_reused_only"] is True
    assert report["frozen_config_allowed_pages_not_broadened"] is True
    assert report["profile_id"] == "trim_mask_psm4"
    assert report["profile_tuple"]["preprocessing_variant"] == "edge_mask_trim"
    assert report["profile_tuple"]["tesseract_psm"] == 4
    assert report["candidate_count"] == 1
    assert report["old_broad_runner_reused"] is False
    assert (
        report["verified_inputs"]["C01TEFPC-G1-VIRAL-001.config"]["sha256"]
        == "4807057B7F043DC197651CD7DBCA40496FA4CAFCD7F08ECE6A59A306C14D7987"
    )


def test_p011_replay_expansion_exact_inputs_and_reference():
    report = read_json(REPORT)

    assert report["pages"] == ["011"]
    assert report["input_count"] == 2
    page = report["page_result"]
    assert page["page"] == "011"
    assert page["reference_label"] == "reference_ocr_verified_text_map"
    assert page["reference_text_map"].endswith("page_011_ocr_verified_text_map.md")
    input_paths = [item["source_input_path"] for item in page["input_results"]]
    assert len(input_paths) == 2
    assert input_paths[0].endswith("1b_P011-left-maya-continuation-secret-appearance-text-evidence.png")
    assert input_paths[1].endswith("4b_P011-right-emily-profile-text-text-evidence.png")
    assert not any("page_012" in path or "page_021" in path for path in input_paths)
    assert not any("human-context" in path or "page_011.png" in path for path in input_paths)


def test_p011_replay_expansion_boundary_flags_and_artifact_policy():
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert report["output_artifact_policy"] == "report_summary_manifest_metrics_only"
    assert report["raw_ocr_artifacts_persisted"] is False
    assert report["prepared_input_artifacts_persisted"] is False
    assert report["candidate_text_artifacts_persisted"] is False
    assert not (OUT_ROOT / "raw_ocr").exists()
    assert not (OUT_ROOT / "prepared_inputs").exists()
    assert not (OUT_ROOT / "candidate_texts").exists()
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
    assert report["page_012_plus_included"] is False
    assert report["page_016_plus_included"] is False
    assert report["page_021_plus_included"] is False
    assert report["push_performed"] is False
    assert report["aggregate_metrics"]["input_count"] == 2
    assert report["aggregate_metrics"]["min_sequence_similarity_ratio"] >= 0.989
    assert report["aggregate_metrics"]["min_token_recall"] >= 0.99
    assert "does not broaden the config allowed-pages policy" in summary
