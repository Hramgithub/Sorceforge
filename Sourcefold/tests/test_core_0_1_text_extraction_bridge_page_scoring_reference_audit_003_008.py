from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008 import (  # noqa: E402
    AUDIT_PAGES,
    AUTHORIZATION_ID,
    CANDIDATE_INPUTS,
    HUMAN_DECISION,
    LANE_ID,
    OUT_OF_SCOPE_PAGES,
    OUT_ROOT,
    REFERENCE_SURFACES,
    REMEDIATION_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008.py"
REPORT = OUT_ROOT / "bridge_page_scoring_reference_audit_003_008_report.json"
SUMMARY = OUT_ROOT / "bridge_page_scoring_reference_audit_003_008_summary.md"
MANIFEST = OUT_ROOT / "bridge_page_scoring_reference_audit_003_008_manifest.md"
CREATION_HEAD = "712e01ce"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("bridge page scoring/reference audit output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_bridge_page_scoring_reference_audit_is_fail_closed():
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


def test_bridge_page_scoring_reference_audit_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, remediation_report = verify_inputs()
    assert remediation_report["lane_id"] == "C01TEBRIDGEREM020-G1-VIRAL-001"
    assert remediation_report["fresh_ocr_candidate_pages"] == AUDIT_PAGES
    for page in AUDIT_PAGES:
        assert f"candidate.page_{page}" in verified
        assert f"reference.page_{page}" in verified
    assert not any(f"candidate.page_{page}" in verified for page in OUT_OF_SCOPE_PAGES)


def test_bridge_page_scoring_reference_audit_materialized_pins_still_match_disk():
    report = read_report()
    expected = {
        **{key: item for key, item in REMEDIATION_INPUTS.items()},
        **{f"candidate.page_{page}": item for page, item in CANDIDATE_INPUTS.items()},
        **{f"reference.page_{page}": (path, expected_hash) for page, (path, expected_hash, _label) in REFERENCE_SURFACES.items()},
    }
    assert sorted(report["verified_inputs"]) == sorted(expected)
    for key, (path, expected_hash) in expected.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_bridge_page_scoring_reference_audit_no_latest_or_unbounded_discovery():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = ["latest", ".glob(", ".rglob(", "Get-ChildItem", "TESSERACT =", "run_tesseract"]
    for needle in forbidden:
        assert needle not in source
    assert "CANDIDATE_INPUTS" in source
    assert "REFERENCE_SURFACES" in source


def test_bridge_page_scoring_reference_audit_report_contract_and_scope():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "bridge_page_scoring_reference_audit_completed"
    assert report["input_lane_id"] == "C01TEBRIDGEREM020-G1-VIRAL-001"
    assert report["input_lane_base_commit_recorded"] == "c99006fd"
    assert report["current_head"] == CREATION_HEAD
    assert report["audit_pages"] == AUDIT_PAGES
    assert report["out_of_scope_pages_rejected"] == OUT_OF_SCOPE_PAGES
    assert sorted(item["page"] for item in report["page_entries"]) == AUDIT_PAGES
    assert report["independent_truth_reference_pages"] == []
    assert report["bounded_comparison_only_pages"] == AUDIT_PAGES
    assert report["fresh_ocr_success_pages"] == []
    assert report["promotable_pages"] == []
    assert report["all_audit_pages_have_pinned_reference_surface"] is True


def test_bridge_page_scoring_reference_audit_boundary_flags():
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
    for item in report["page_entries"]:
        assert item["candidate_hash_verified_before_reference_load"] is True
        assert item["scoring_scope"] == "diagnostic_comparison_only"
        assert item["fresh_ocr_success"] is False
        assert item["promotable"] is False
        assert item["acceptance_effect"] == "none"
        assert item["promotion_effect"] == "none"


def test_bridge_page_scoring_reference_audit_output_tree_is_minimal():
    report = read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "bridge_page_scoring_reference_audit_003_008_manifest.md",
        "bridge_page_scoring_reference_audit_003_008_report.json",
        "bridge_page_scoring_reference_audit_003_008_summary.md",
    ]
    assert not any("001" in path or "002" in path or "014" in path or "019" in path or "021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "diagnostic comparison audit only" in manifest
    assert "Fresh OCR success remains empty" in summary
    for output in output_files:
        if output != "bridge_page_scoring_reference_audit_003_008_manifest.md":
            assert output in manifest
    assert report["allowed_next_action"] == "bounded_candidate_scoring_authorization_or_page_002_source_asset_recovery"
