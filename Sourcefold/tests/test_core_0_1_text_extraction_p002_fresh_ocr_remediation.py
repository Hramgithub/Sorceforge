from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_core_0_1_text_extraction_p002_fresh_ocr_remediation import (  # noqa: E402
    AUTH_INPUTS,
    AUTHORIZATION_ID,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    PSM4_CANDIDATE,
    VERIFY_REPORT,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p002_fresh_ocr_remediation.py"
REPORT = OUT_ROOT / "p002_fresh_ocr_remediation_report.json"
SUMMARY = OUT_ROOT / "p002_fresh_ocr_remediation_summary.md"
MANIFEST = OUT_ROOT / "p002_fresh_ocr_remediation_manifest.md"
REMEDIATED = OUT_ROOT / "candidate_texts" / "page_002_full_page_psm4_remediated_candidate.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 fresh OCR remediation output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_fresh_ocr_remediation_is_fail_closed():
    no_args = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_args.returncode != 0
    assert "--execute" in no_args.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "wrong", "--decision", HUMAN_DECISION],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTHORIZATION_ID, "--decision", "wrong"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_p002_fresh_ocr_remediation_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, auth_report = verify_inputs()
    assert auth_report["lane_id"] == "C01TEP002FRESHREMAUTH-G1-VIRAL-001"
    assert auth_report["authorized_best_candidate"] == "psm4"
    assert auth_report["allowed_next_action"] == "separate_bounded_p002_fresh_ocr_remediation_execution"
    assert "candidate.psm4" in verified
    assert "source_reconstruction_p002_assisted_draft_verify.report" in verified


def test_p002_fresh_ocr_remediation_materialized_pins_still_match_disk():
    report = read_report()
    expected = {
        **{key: item for key, item in AUTH_INPUTS.items()},
        "candidate.psm4": PSM4_CANDIDATE,
        "source_reconstruction_p002_assisted_draft_verify.report": VERIFY_REPORT,
    }
    assert sorted(report["verified_inputs"]) == sorted(expected)
    for key, (path, expected_hash) in expected.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_p002_fresh_ocr_remediation_contract_and_result():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_fresh_ocr_remediation_executed_candidate_only"
    assert report["input_lane_id"] == "C01TEP002FRESHREMAUTH-G1-VIRAL-001"
    assert report["source_candidate"] == "psm4"
    assert [item["operation"] for item in report["remediation_operations"]] == [
        "insert_missing_header",
        "replace_visual_verified_token",
    ]
    assert report["threshold_met_after_remediation"] is True
    assert report["diagnostic_metrics_after_remediation"]["sequence_similarity_ratio"] == 1.0
    assert report["diagnostic_metrics_after_remediation"]["token_recall"] == 1.0
    assert report["fresh_ocr_success"] is False
    assert report["bridge_blocker_cleared"] is False
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_for_pages"] == []
    assert report["allowed_next_action"] == "separate_bounded_p002_remediated_candidate_pass_decision"
    text = REMEDIATED.read_text(encoding="utf-8-sig")
    assert text.startswith("Credits\n\nWriting")
    assert "Dragongirl174" in text
    assert "Dragongirl74" not in text


def test_p002_fresh_ocr_remediation_boundary_flags():
    report = read_report()
    false_flags = [
        "ocr_execution_performed",
        "tesseract_invoked",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "production_ready",
        "production_assembly_authorized",
        "production_assembly_created",
        "acceptance_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "fixture_admission_performed",
        "page_021_plus_included",
        "promotion_performed",
        "push_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag


def test_p002_fresh_ocr_remediation_output_tree_is_bounded():
    report = read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())
    assert output_files == [
        "candidate_texts/page_002_full_page_psm4_remediated_candidate.md",
        "p002_fresh_ocr_remediation_manifest.md",
        "p002_fresh_ocr_remediation_report.json",
        "p002_fresh_ocr_remediation_summary.md",
    ]
    assert not any("001" in path or "003" in path or "014" in path or "019" in path or "021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "Threshold met after remediation: `true`" in summary
    assert "remediation candidate only" in manifest
    assert report["remediated_candidate_text_sha256"] == sha256_file(REMEDIATED)
