from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_core_0_1_text_extraction_comparison_remediation_005_008 import (  # noqa: E402
    AUTH_INPUTS,
    AUTHORIZATION_ID,
    CANDIDATE_INPUTS,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    PAGES,
    REFERENCE_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_comparison_remediation_005_008.py"
REPORT = OUT_ROOT / "comparison_remediation_execution_005_008_report.json"
SUMMARY = OUT_ROOT / "comparison_remediation_execution_005_008_summary.md"
MANIFEST = OUT_ROOT / "comparison_remediation_execution_005_008_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("005-008 comparison remediation execution output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_005_008_comparison_remediation_execution_is_fail_closed():
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


def test_005_008_comparison_remediation_execution_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, auth_report = verify_inputs()

    assert auth_report["lane_id"] == "C01TEP005008REMAUTH-G1-VIRAL-001"
    assert auth_report["pages"] == PAGES
    assert auth_report["allowed_next_action"] == "separate_bounded_comparison_only_remediation_execution_for_pages_005_008"
    assert sorted(verified) == sorted(
        list(AUTH_INPUTS) + [f"candidate.page_{page}" for page in PAGES] + [f"reference.page_{page}" for page in PAGES]
    )


def test_005_008_comparison_remediation_execution_materialized_pins_still_match_disk():
    report = read_report()
    expected = {
        **AUTH_INPUTS,
        **{f"candidate.page_{page}": item for page, item in CANDIDATE_INPUTS.items()},
        **{f"reference.page_{page}": item for page, item in REFERENCE_INPUTS.items()},
    }
    assert sorted(report["verified_inputs"]) == sorted(expected)
    for key, (path, expected_hash) in expected.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_005_008_comparison_remediation_execution_contract_and_boundaries():
    report = read_report()

    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "comparison_only_remediation_execution_completed_candidate_only"
    assert report["input_lane_id"] == "C01TEP005008REMAUTH-G1-VIRAL-001"
    assert report["pages"] == PAGES
    assert report["remediated_candidate_pages"] == PAGES
    assert report["remediation_execution_performed"] is True
    assert report["diagnostic_scoring_performed"] is True
    assert report["diagnostic_scoring_scope"] == "post_remediation_comparison_only_after_candidate_hash_seal"
    assert report["scoring_execution_performed"] is False
    assert report["ocr_execution_performed"] is False
    assert report["tesseract_invoked"] is False
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_pages"] == []
    assert report["promotable_pages"] == []
    assert report["comparison_only_evidence_becomes_acceptance_truth"] is False
    assert report["comparison_only_evidence_becomes_promotion_authority"] is False

    false_flags = [
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


def test_005_008_comparison_remediation_execution_page_traces_and_outputs():
    report = read_report()
    by_page = {entry["page"]: entry for entry in report["page_entries"]}
    assert sorted(by_page) == PAGES

    for page, entry in by_page.items():
        candidate = ROOT / entry["remediated_candidate_path"]
        trace = ROOT / entry["trace_path"]
        assert candidate.exists()
        assert trace.exists()
        assert sha256_file(candidate) == entry["remediated_candidate_sha256"]
        assert sha256_file(trace) == entry["trace_sha256"]
        assert entry["candidate_hash_sealed_before_reference_load"] is True
        assert entry["diagnostic_scoring_performed_after_candidate_hash_seal"] is True
        assert entry["fresh_ocr_success"] is False
        assert entry["bridge_removed"] is False
        assert entry["promotable"] is False
        assert entry["reference_surface_authority"] == "ocr_verified_text_map_comparison_only_not_acceptance_truth"
        assert entry["operations"][0]["operation"] == "nfkc_lf_trim_collapse_whitespace"
        assert entry["operations"][0]["reference_tokens_inserted"] is False

    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())
    assert not any("003" in path or "004" in path or "021" in path for path in output_files)
    for page in PAGES:
        assert f"candidate_texts/page_{page}_comparison_remediated_candidate.md" in output_files
        assert f"traces/page_{page}_comparison_remediation_trace.json" in output_files
    assert "comparison_remediation_execution_005_008_report.json" in output_files
    assert "comparison_remediation_execution_005_008_summary.md" in output_files
    assert "comparison_remediation_execution_005_008_manifest.md" in output_files


def test_005_008_comparison_remediation_execution_summary_manifest_boundaries():
    read_report()
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "does not run OCR/Tesseract" in summary
    assert "Fresh OCR success, bridge removal, promotion, acceptance, and production remain false" in summary
    assert "no OCR/Tesseract" in manifest
