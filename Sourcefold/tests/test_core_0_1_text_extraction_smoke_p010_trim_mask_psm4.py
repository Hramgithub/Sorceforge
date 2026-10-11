import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_smoke_p010_trim_mask_psm4.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P010_ROOT = TRIAL_ROOT / "page_complete_review_p010_G1_VIRAL_001" / "review_assets"
OUTPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SMOKE-P010-TRIM-MASK-PSM4-001"
HUMAN_DECISION = "ок. пошли делать 010"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_text_extraction_smoke_p010_trim_mask_psm4_is_fail_closed():
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
            "делай 010",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_text_extraction_smoke_p010_trim_mask_psm4_boundary_flags():
    report = read_json(OUTPUT_ROOT / "smoke_report.json")
    assert report["smoke_id"] == "C01TESP010-G1-VIRAL-001"
    assert report["status"] == "candidate_only_p010_same_profile_smoke_completed"
    assert report["source_remediation"] == "C01TESRM-G1-VIRAL-001"
    assert report["page"] == "010"
    assert report["page_021_plus_included"] is False
    assert report["candidate_count"] == 1
    assert report["candidate_id"] == "trim_mask_psm4"
    assert report["variant"] == "edge_mask_trim"
    assert report["psm"] == 4
    assert report["ocr_execution_performed"] is True
    assert report["pdf_parsing_performed"] is False
    assert report["pdf_text_layer_extraction_performed"] is False
    assert report["render_execution_performed"] is False
    assert report["source_or_raw_mutation_performed"] is False
    assert report["accepted_text_mutation_performed"] is False
    assert report["semantic_text_mutation_performed"] is False
    assert report["page_status_mutation_performed"] is False
    assert report["runtime_implementation_created"] is False
    assert report["runtime_start_performed"] is False
    assert report["translation_or_proofreading_performed"] is False
    assert report["push_performed"] is False
    assert report["input_policy"] == "read_only_existing_p010_text_evidence_crops"
    assert report["output_policy"] == "candidate_only_separate_same_profile_directory"


def test_core_0_1_text_extraction_smoke_p010_trim_mask_psm4_uses_only_p010_inputs():
    report = read_json(OUTPUT_ROOT / "smoke_report.json")
    expected_inputs = {
        "p010_input_upper_left_peter_continuation_gear_text_evidence": P010_ROOT
        / "1b_P010-upper-left-continuation-gear-text-evidence.png",
        "p010_input_lower_left_hyeon_profile_text_evidence": P010_ROOT
        / "5b_P010-lower-left-hyeon-profile-text-evidence.png",
        "p010_input_upper_right_hyeon_continuation_appearance_gear_text_evidence": P010_ROOT
        / "2b_P010-upper-right-continuation-appearance-gear-text-evidence.png",
        "p010_input_lower_right_maya_profile_text_evidence": P010_ROOT
        / "6b_P010-lower-right-maya-profile-text-evidence.png",
        "reference_ocr_verified_text_map": P010_ROOT / "page_010_ocr_verified_text_map.md",
    }
    for key, path in expected_inputs.items():
        item = report["verified_inputs"][key]
        assert Path(ROOT / item["path"]) == path
        assert item["sha256"]

    raw_outputs = report["candidate_result"]["raw_outputs"]
    assert len(raw_outputs) == 4
    for raw in raw_outputs:
        assert "page_complete_review_p010_G1_VIRAL_001" in raw["source_input_path"]
        assert "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001" in raw["prepared_input_path"]
        assert "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001" in raw["txt_path"]
        assert "page_complete_review_p010_G1_VIRAL_001" not in raw["txt_path"]
        assert "page_complete_review_p009_G1_VIRAL_001" not in raw["txt_path"]


def test_core_0_1_text_extraction_smoke_p010_trim_mask_psm4_outputs_exist_and_are_single_candidate():
    report = read_json(OUTPUT_ROOT / "smoke_report.json")
    candidate = report["candidate_result"]
    assert candidate["candidate_id"] == "trim_mask_psm4"
    assert candidate["psm"] == 4
    assert candidate["variant"] == "edge_mask_trim"
    assert "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001" in candidate["candidate_text_path"]
    assert "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001" in candidate["normalized_text_path"]
    assert (OUTPUT_ROOT / "candidate_texts" / "trim_mask_psm4.md").exists()
    assert (OUTPUT_ROOT / "candidate_texts" / "trim_mask_psm4.normalized.txt").exists()
    assert (OUTPUT_ROOT / "smoke_manifest.md").exists()
    assert (OUTPUT_ROOT / "smoke_summary.md").exists()
    assert 0 <= report["metrics"]["sequence_similarity_ratio"] <= 1
    assert 0 <= report["metrics"]["token_recall"] <= 1
