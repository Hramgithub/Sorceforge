import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_candidate_profile_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_candidate_profile_decision_G1_VIRAL_001"
DECISION = OUT_ROOT / "core_0_1_text_extraction_candidate_profile_decision.json"
REPORT = OUT_ROOT / "core_0_1_text_extraction_candidate_profile_decision_report.json"
SUMMARY = OUT_ROOT / "core_0_1_text_extraction_candidate_profile_decision_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-CANDIDATE-PROFILE-DECISION-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_text_extraction_candidate_profile_decision_is_fail_closed():
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
            "ок",
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
            "profile lock ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_text_extraction_candidate_profile_decision_freezes_candidate_only():
    decision = read_json(DECISION)
    report = read_json(REPORT)

    assert decision["decision_id"] == "C01TECPD-G1-VIRAL-001"
    assert decision["authorization_id"] == AUTHORIZATION_ID
    assert decision["status"] == "text_extraction_candidate_profile_decision_recorded_candidate_profile_frozen"
    assert decision["candidate_profile_decision_recorded"] is True
    assert decision["candidate_profile_freeze_granted"] is True
    assert decision["candidate_profile_id"] == "trim_mask_psm4"
    assert decision["candidate_profile_tuple"] == {
        "candidate_id": "trim_mask_psm4",
        "preprocessing_variant": "edge_mask_trim",
        "tesseract_psm": 4,
        "tesseract_oem": 1,
        "language": "eng",
        "strategy": "full_column",
    }
    assert decision["candidate_profile_scope"] == "Core_0_1_text_extraction_candidate_profile_only"
    assert report["candidate_profile_freeze_granted"] is True


def test_text_extraction_candidate_profile_decision_evidence_ladder():
    decision = read_json(DECISION)
    evidence = decision["evidence"]

    assert [item["evidence_id"] for item in evidence] == [
        "C01TESRM-G1-VIRAL-001",
        "C01TESP010-G1-VIRAL-001",
        "C01TESP015-G1-VIRAL-001",
    ]
    assert [item["page"] for item in evidence] == ["009", "010", "015"]
    assert [item["selected_candidate"] for item in evidence] == ["trim_mask_psm4"] * 3
    assert [item["variant"] for item in evidence] == ["edge_mask_trim"] * 3
    assert [item["psm"] for item in evidence] == [4, 4, 4]
    assert evidence[0]["reference_label"] == "reference_ocr_verified_text_map"
    assert evidence[1]["reference_label"] == "reference_ocr_verified_text_map"
    assert evidence[2]["reference_label"] == "reference_text_map_not_ocr_verified"
    assert evidence[0]["sequence_similarity_ratio"] == 0.9993
    assert evidence[1]["sequence_similarity_ratio"] == 0.998867
    assert evidence[2]["sequence_similarity_ratio"] == 0.997252
    assert decision["aggregate_metrics"]["min_sequence_similarity_ratio"] == 0.997252
    assert decision["aggregate_metrics"]["min_token_recall"] == 0.993985


def test_text_extraction_candidate_profile_decision_boundary_flags():
    decision = read_json(DECISION)
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    for payload in (decision, report):
        assert payload["source_profile_acceptance_created"] is False
        assert payload["runtime_source_profile_lock_created"] is False
        assert payload["runtime_source_profile_acceptance_created"] is False
        assert payload["ocr_execution_performed"] is False
        assert payload["render_execution_performed"] is False
        assert payload["pdf_parsing_or_text_layer_extraction_performed"] is False
        assert payload["source_or_raw_mutation_performed"] is False
        assert payload["accepted_text_mutation_performed"] is False
        assert payload["semantic_text_mutation_performed"] is False
        assert payload["page_status_mutation_performed"] is False
        assert payload["page_021_plus_included"] is False
        assert payload["push_performed"] is False

    assert decision["page_016_plus_included"] is False
    assert decision["runtime_implementation_created"] is False
    assert decision["runtime_start_performed"] is False
    assert "not OCR acceptance" in summary
    assert "not an OCR-verified text map" not in summary
    for key, value in decision["negative_capability_matrix"].items():
        assert value is False, key


def test_text_extraction_candidate_profile_decision_verified_inputs_and_next_steps():
    decision = read_json(DECISION)

    assert "C01TESP015-G1-VIRAL-001.manifest" in decision["verified_inputs"]
    assert (
        decision["verified_inputs"]["C01TESP015-G1-VIRAL-001.manifest"]["sha256"]
        == "39E150A2A86B5005C2E84FD3A6C31E8E119E26A344FFE5D64F6B2A9A38A0B1DA"
    )
    assert decision["evidence_lineage"] == [
        "C01TESP-G1-VIRAL-001",
        "C01TESRM-G1-VIRAL-001",
        "C01TESP010-G1-VIRAL-001",
        "C01TESP015-G1-VIRAL-001",
    ]
    assert decision["next_possible_packets"][0] == "core_0_1_text_extraction_frozen_profile_config_if_separately_authorized"
    assert "runtime_source_profile_lock_requires_separate_authorization" in decision["remaining_blockers"]
    assert "page_021_plus_remains_separate_bounded_lane_if_selected" in decision["remaining_blockers"]
