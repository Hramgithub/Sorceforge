from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_comparison_remediation_authorization_005_008 import (  # noqa: E402
    AUTHORIZATION_ID,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    PAGES,
    STRATEGY_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_comparison_remediation_authorization_005_008.py"
REPORT = OUT_ROOT / "comparison_remediation_authorization_005_008_report.json"
SUMMARY = OUT_ROOT / "comparison_remediation_authorization_005_008_summary.md"
MANIFEST = OUT_ROOT / "comparison_remediation_authorization_005_008_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("005-008 comparison remediation authorization output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_005_008_comparison_remediation_authorization_is_fail_closed():
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


def test_005_008_comparison_remediation_authorization_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, strategy_report = verify_inputs()

    assert strategy_report["lane_id"] == "C01TEP005008REMSTRAT-G1-VIRAL-001"
    assert strategy_report["pages"] == PAGES
    assert strategy_report["remediation_execution_performed"] is False
    assert strategy_report["scoring_execution_performed"] is False
    assert strategy_report["fresh_ocr_success_pages"] == []
    assert strategy_report["bridge_removed_pages"] == []
    assert sorted(verified) == sorted(STRATEGY_INPUTS)


def test_005_008_comparison_remediation_authorization_materialized_pins_still_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(STRATEGY_INPUTS)
    for key, (path, expected_hash) in STRATEGY_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_005_008_comparison_remediation_authorization_contract_and_boundaries():
    report = read_report()

    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "comparison_only_remediation_authorized_no_execution"
    assert report["input_lane_id"] == "C01TEP005008REMSTRAT-G1-VIRAL-001"
    assert report["pages"] == PAGES
    assert sorted(report["authorized_candidate_inputs"]) == PAGES
    assert sorted(report["authorized_reference_surfaces"]) == PAGES
    assert report["comparison_surfaces_are_diagnostic_only"] is True
    assert report["comparison_only_evidence_becomes_acceptance_truth"] is False
    assert report["comparison_only_evidence_becomes_promotion_authority"] is False
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_pages"] == []
    assert report["promotable_pages"] == []

    false_flags = [
        "remediation_execution_performed",
        "scoring_execution_performed",
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


def test_005_008_comparison_remediation_authorization_output_tree_is_minimal():
    report = read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "comparison_remediation_authorization_005_008_manifest.md",
        "comparison_remediation_authorization_005_008_report.json",
        "comparison_remediation_authorization_005_008_summary.md",
    ]
    assert not any("003" in path or "004" in path or "021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "does not execute remediation" in summary
    assert "authorization only" in manifest
    for output in output_files:
        if output != "comparison_remediation_authorization_005_008_manifest.md":
            assert output in manifest
    assert report["allowed_next_action"] == "separate_bounded_comparison_only_remediation_execution_for_pages_005_008"
