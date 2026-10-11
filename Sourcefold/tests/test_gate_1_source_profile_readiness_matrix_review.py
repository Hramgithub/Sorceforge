import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_gate_1_source_profile_readiness_matrix_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_readiness_parking_matrix_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-READINESS-MATRIX-REVIEW-001"
DECISION = "ок принято с коментариями"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_source_profile_readiness_matrix_review_is_fail_closed():
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
            DECISION,
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
            "source profile accepted",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert DECISION in wrong_decision.stderr


def test_source_profile_readiness_matrix_review_records_route_review_only():
    report = read_json(OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_review.json")

    assert report["review_id"] == "G1SPRMREV-G1-VIRAL-001"
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["reviewed_matrix_id"] == "G1SPRM-G1-VIRAL-001"
    assert report["status"] == "source_profile_readiness_matrix_route_review_accepted_with_comments"
    assert report["human_decision_source_text"] == DECISION
    assert report["human_decision_source"]["message_id"] == "2182"
    assert report["accepts_route_review_artifact"] is True
    assert report["accepts_source_profile"] is False
    assert report["creates_parking_decision"] is False
    assert report["starts_ocr_remediation"] is False

    assert report["disposition_counts"] == {
        "ready_for_gate_review": 5,
        "parked_for_0.1": 0,
        "parked_pending_ocr_hardening": 2,
        "blocked_needs_decision": 3,
        "evidence_only_not_accepting": 2,
    }


def test_source_profile_readiness_matrix_review_preserves_boundaries():
    report = read_json(OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_review.json")

    for key in [
        "source_profile_acceptance",
        "creates_parking_decision",
        "ocr_execution",
        "ocr_remediation_execution",
        "page_021_plus_processing",
        "whole_gate_1_acceptance",
        "fixture_admission",
        "source_mutation",
        "render_execution",
        "pdf_parsing_or_text_layer_extraction",
        "raw_mutation",
        "translation",
        "proofreading",
        "renderer_profile_acceptance",
        "implementation",
        "push",
    ]:
        assert report["negative_capability_matrix"][key] is False, key

    next_branch = report["next_selected_branch"]
    assert next_branch["branch"] == "ocr_benchmark_remediation_methodology_hardening"
    assert next_branch["status"] == "selected_next_branch_requires_separate_bounded_authorization"


def test_source_profile_readiness_matrix_review_manifest_lists_outputs():
    manifest = (OUT_ROOT / "gate_1_source_profile_readiness_parking_matrix_review_manifest.md").read_text(
        encoding="utf-8"
    )

    assert "gate_1_source_profile_readiness_parking_matrix_review.json" in manifest
    assert "gate_1_source_profile_readiness_parking_matrix_review_summary.md" in manifest
