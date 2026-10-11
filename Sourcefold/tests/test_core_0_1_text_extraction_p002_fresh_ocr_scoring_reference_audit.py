from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit import (  # noqa: E402
    AUTHORIZATION_ID,
    CANDIDATE_INPUTS,
    FRESH_OCR_INPUTS,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    REFERENCE_SURFACES,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit.py"
REPORT = OUT_ROOT / "p002_fresh_ocr_scoring_reference_audit_report.json"
SUMMARY = OUT_ROOT / "p002_fresh_ocr_scoring_reference_audit_summary.md"
MANIFEST = OUT_ROOT / "p002_fresh_ocr_scoring_reference_audit_manifest.md"
CREATION_HEAD = "a99e43f7"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 fresh OCR scoring/reference audit output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_fresh_ocr_scoring_reference_audit_is_fail_closed():
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


def test_p002_fresh_ocr_scoring_reference_audit_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, candidate_report = verify_inputs()
    assert candidate_report["lane_id"] == "C01TEP002FRESHOCR-G1-VIRAL-001"
    assert candidate_report["page"] == "002"
    assert candidate_report["candidate_count"] == 2
    assert candidate_report["candidate_hash_sealed_before_reference_scoring"] is True
    assert candidate_report["reference_scoring_performed"] is False
    for label in CANDIDATE_INPUTS:
        assert f"candidate.{label}" in verified
    for label in REFERENCE_SURFACES:
        assert f"reference.{label}" in verified


def test_p002_fresh_ocr_scoring_reference_audit_materialized_pins_still_match_disk():
    report = read_report()
    expected = {
        **{key: item for key, item in FRESH_OCR_INPUTS.items()},
        **{f"candidate.{label}": item for label, item in CANDIDATE_INPUTS.items()},
        **{
            f"reference.{label}": (path, expected_hash)
            for label, (path, expected_hash, _surface_label) in REFERENCE_SURFACES.items()
        },
    }
    assert sorted(report["verified_inputs"]) == sorted(expected)
    for key, (path, expected_hash) in expected.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_p002_fresh_ocr_scoring_reference_audit_no_latest_or_unbounded_discovery():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = ["latest", ".glob(", ".rglob(", "Get-ChildItem", "TESSERACT =", "run_tesseract"]
    for needle in forbidden:
        assert needle not in source
    assert "CANDIDATE_INPUTS" in source
    assert "REFERENCE_SURFACES" in source


def test_p002_fresh_ocr_scoring_reference_audit_report_contract_and_scope():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_fresh_ocr_scoring_reference_audit_completed"
    assert report["base_commit"] == "cc0fe001"
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_id"] == "C01TEP002FRESHOCR-G1-VIRAL-001"
    assert report["page"] == "002"
    assert report["candidate_labels"] == ["psm4", "psm6"]
    assert report["independent_truth_reference_pages"] == []
    assert report["bounded_comparison_only_pages"] == ["002"]
    assert report["fresh_ocr_success_pages"] == []
    assert report["promotable_pages"] == []
    assert report["bridge_removed_for_pages"] == []
    assert report["all_candidates_have_pinned_reference_surfaces"] is True
    assert report["reference_scoring_performed"] is True
    assert report["scoring_scope"] == "diagnostic_comparison_only"


def test_p002_fresh_ocr_scoring_reference_audit_boundary_flags():
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
    for item in report["candidate_entries"]:
        assert item["candidate_hash_verified_before_reference_load"] is True
        assert item["scoring_scope"] == "diagnostic_comparison_only"
        assert item["fresh_ocr_success"] is False
        assert item["promotable"] is False
        assert item["bridge_removal_effect"] == "none"
        assert item["acceptance_effect"] == "none"
        assert item["promotion_effect"] == "none"
        assert all(
            ref["reference_authority_classification"] == "bounded_comparison_only_not_acceptance_truth"
            for ref in item["reference_entries"]
        )


def test_p002_fresh_ocr_scoring_reference_audit_output_tree_is_minimal():
    report = read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "p002_fresh_ocr_scoring_reference_audit_manifest.md",
        "p002_fresh_ocr_scoring_reference_audit_report.json",
        "p002_fresh_ocr_scoring_reference_audit_summary.md",
    ]
    assert not any("001" in path or "003" in path or "014" in path or "019" in path or "021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "comparison-only" in summary
    assert "diagnostic comparison audit only" in manifest
    for output in output_files:
        if output != "p002_fresh_ocr_scoring_reference_audit_manifest.md":
            assert output in manifest
    assert report["allowed_next_action"] == "separate_bounded_p002_candidate_scoring_or_remediation_decision"
