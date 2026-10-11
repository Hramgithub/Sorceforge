import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001"
REPORT = OUT_ROOT / "overview_replay_report.json"
SUMMARY = OUT_ROOT / "overview_replay_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-OVERVIEW-REPLAY-001-020-TRIM-MASK-PSM4-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_001_020_overview_replay_is_fail_closed():
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
            "сделай 001-020",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_001_020_overview_replay_uses_tuple_without_broadening_config():
    report = read_json(REPORT)

    assert report["overview_id"] == "C01TEOR020-G1-VIRAL-001"
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["source_frozen_profile_config"] == "C01TEFPC-G1-VIRAL-001"
    assert report["frozen_config_tuple_reused_only"] is True
    assert report["frozen_config_allowed_pages_not_broadened"] is True
    assert report["profile_id"] == "trim_mask_psm4"
    assert report["profile_tuple"]["preprocessing_variant"] == "edge_mask_trim"
    assert report["profile_tuple"]["tesseract_psm"] == 4
    assert report["candidate_count"] == 1
    assert report["old_broad_runner_reused"] is False


def test_001_020_overview_replay_page_disposition_and_labels():
    report = read_json(REPORT)

    assert report["requested_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert report["eligible_run_pages"] == [f"{page:03d}" for page in range(9, 21)]
    assert report["ineligible_pages"] == [f"{page:03d}" for page in range(1, 9)]
    pages = {page["page"]: page for page in report["page_results"]}
    assert pages["001"]["status"] == "not_run_ineligible"
    assert pages["002"]["status"] == "not_run_ineligible"
    assert pages["006"]["reason"] == "reference_map_exists_but_no_text_evidence_crops"
    assert pages["009"]["reference_label"] == "reference_ocr_verified_text_map"
    assert pages["010"]["reference_label"] == "reference_ocr_verified_text_map"
    assert pages["011"]["reference_label"] == "reference_ocr_verified_text_map"
    for page in [f"{item:03d}" for item in range(12, 21)]:
        assert pages[page]["reference_label"] == "reference_text_map_not_ocr_verified"
        assert "reference_not_ocr_verified" in pages[page]["weak_flags"]


def test_001_020_overview_replay_artifact_policy_boundaries_and_metrics():
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
    assert report["runtime_source_profile_lock_created"] is False
    assert report["runtime_implementation_created"] is False
    assert report["runtime_start_performed"] is False
    assert report["page_021_plus_included"] is False
    assert report["remediation_performed"] is False
    assert report["push_performed"] is False
    assert report["aggregate_metrics"]["page_count"] == 20
    assert report["aggregate_metrics"]["run_page_count"] == 12
    assert report["aggregate_metrics"]["ineligible_page_count"] == 8
    assert report["aggregate_metrics"]["input_count"] == 43
    assert "overview/report only; no remediation" in summary
