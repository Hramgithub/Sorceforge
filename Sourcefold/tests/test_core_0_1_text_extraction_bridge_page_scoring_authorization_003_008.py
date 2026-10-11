from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_bridge_page_scoring_authorization_003_008 import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HUMAN_DECISION,
    INPUT_LANE_ID,
    LANE_ID,
    OUT_ROOT,
    OUTPUT_FILES,
    PAGES,
    PINNED_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_bridge_page_scoring_authorization_003_008.py"
REPORT = OUT_ROOT / "bridge_page_scoring_authorization_003_008_report.json"
SUMMARY = OUT_ROOT / "bridge_page_scoring_authorization_003_008_summary.md"
MANIFEST = OUT_ROOT / "bridge_page_scoring_authorization_003_008_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("003-008 scoring authorization output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_003_008_scoring_authorization_is_fail_closed():
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
    assert "exact broad orchestration decision" in wrong_decision.stderr


def test_003_008_scoring_authorization_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, audit = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert audit["lane_id"] == INPUT_LANE_ID
    assert audit["audit_pages"] == PAGES
    assert audit["fresh_ocr_success_pages"] == []
    assert audit["promotable_pages"] == []


def test_003_008_scoring_authorization_report_contract():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "bridge_page_scoring_authorization_recorded_no_promotion_no_scoring"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_id"] == INPUT_LANE_ID
    assert report["pages"] == PAGES
    assert report["candidate_pages"] == PAGES
    assert report["comparison_surface_pages"] == PAGES
    assert report["independent_truth_reference_pages"] == []
    assert report["audit_fresh_ocr_success_pages"] == []
    assert report["audit_promotable_pages"] == []
    assert report["existing_audit_metrics_authorize_fresh_success"] is False
    assert report["existing_audit_metrics_authorize_promotion"] is False
    assert report["future_scoring_decision_authorized"] is True
    assert report["future_scoring_may_promote_without_separate_authority"] is False
    assert report["future_scoring_may_mutate_acceptance_or_production"] is False


def test_003_008_scoring_authorization_pins_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert report["verified_inputs"][key]["sha256"] == expected_hash


def test_003_008_scoring_authorization_boundary_flags_and_outputs():
    report = read_report()
    false_flags = [
        "scoring_performed",
        "fresh_ocr_success",
        "promotion_authorized",
        "promotion_performed",
        "ocr_execution_performed",
        "tesseract_invoked",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "fixture_admission_performed",
        "production_ready",
        "production_assembly_authorized",
        "production_assembly_created",
        "acceptance_performed",
        "page_021_plus_included",
        "push_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert "fresh success: `false`" in MANIFEST.read_text(encoding="utf-8-sig")
    assert "not authorize fresh OCR success or promotion" in SUMMARY.read_text(encoding="utf-8-sig")


def test_003_008_scoring_authorization_avoids_unbounded_discovery_and_execution():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = [
        "latest",
        ".glob(",
        ".rglob(",
        "pytesseract",
        "subprocess.run([\"tesseract\"",
        "subprocess.run(['tesseract'",
        "fitz.open",
        "pdfplumber",
        "pypdf",
        "run_render",
        "render_pdf",
    ]
    for needle in forbidden:
        assert needle not in source
    assert "PINNED_INPUTS" in source
