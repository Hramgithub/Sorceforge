from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization import (  # noqa: E402
    AUTHORIZATION_ID,
    DECISION_INPUTS,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization.py"
REPORT = OUT_ROOT / "p002_fresh_ocr_remediation_authorization_report.json"
SUMMARY = OUT_ROOT / "p002_fresh_ocr_remediation_authorization_summary.md"
MANIFEST = OUT_ROOT / "p002_fresh_ocr_remediation_authorization_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 fresh OCR remediation authorization output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_fresh_ocr_remediation_authorization_is_fail_closed():
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


def test_p002_fresh_ocr_remediation_authorization_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, decision_report = verify_inputs()
    assert decision_report["lane_id"] == "C01TEP002FRESHDECIDE-G1-VIRAL-001"
    assert decision_report["selected_best_candidate"] == "psm4"
    assert decision_report["decision"] == "remediation_required_before_fresh_ocr_success"
    assert decision_report["fresh_ocr_success_pages"] == []
    assert decision_report["bridge_removed_for_pages"] == []
    assert sorted(verified) == sorted(DECISION_INPUTS)


def test_p002_fresh_ocr_remediation_authorization_materialized_pins_still_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(DECISION_INPUTS)
    for key, (path, expected_hash) in DECISION_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_p002_fresh_ocr_remediation_authorization_contract_and_boundaries():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_fresh_ocr_remediation_authorized_no_execution"
    assert report["input_lane_id"] == "C01TEP002FRESHDECIDE-G1-VIRAL-001"
    assert report["authorized_future_action"] == "bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs"
    assert report["authorized_best_candidate"] == "psm4"
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_for_pages"] == []
    assert report["promotable_pages"] == []
    false_flags = [
        "ocr_execution_performed",
        "tesseract_invoked",
        "remediation_execution_performed",
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


def test_p002_fresh_ocr_remediation_authorization_output_tree_is_minimal():
    report = read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "p002_fresh_ocr_remediation_authorization_manifest.md",
        "p002_fresh_ocr_remediation_authorization_report.json",
        "p002_fresh_ocr_remediation_authorization_summary.md",
    ]
    assert not any("001" in path or "003" in path or "014" in path or "019" in path or "021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "does not execute remediation" in summary
    assert "authorization only" in manifest
    for output in output_files:
        if output != "p002_fresh_ocr_remediation_authorization_manifest.md":
            assert output in manifest
    assert report["allowed_next_action"] == "separate_bounded_p002_fresh_ocr_remediation_execution"
