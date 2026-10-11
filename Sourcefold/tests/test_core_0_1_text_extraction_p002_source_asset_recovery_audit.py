from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p002_source_asset_recovery_audit import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    CURRENT_COMPLETION_BUILDER_HASH,
    HUMAN_DECISION,
    LANE_ID,
    OUT_OF_SCOPE_PAGES,
    OUT_ROOT,
    PAGE,
    PINNED_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_source_asset_recovery_audit.py"
REPORT = OUT_ROOT / "p002_source_asset_recovery_audit_report.json"
SUMMARY = OUT_ROOT / "p002_source_asset_recovery_audit_summary.md"
MANIFEST = OUT_ROOT / "p002_source_asset_recovery_audit_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 source asset recovery audit output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_source_asset_recovery_audit_is_fail_closed():
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


def test_p002_source_asset_recovery_audit_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert verified[key]["path"] == path.relative_to(ROOT).as_posix()
        assert verified[key]["sha256"] == expected_hash


def test_p002_source_asset_recovery_audit_materialized_pins_still_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert report["verified_inputs"][key]["sha256"] == expected_hash


def test_p002_source_asset_recovery_audit_no_latest_or_unbounded_discovery():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = [
        "latest",
        ".glob(",
        ".rglob(",
        "TESSERACT",
        "run_tesseract",
        "pdfplumber",
        "pypdf",
        "run_render",
        "render_pdf",
    ]
    for needle in forbidden:
        assert needle not in source
    assert "PINNED_INPUTS" in source


def test_p002_source_asset_recovery_audit_report_contract_and_scope():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_source_asset_recovery_audit_completed_report_only_no_ocr_no_mutation"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["page"] == PAGE
    assert report["scope"] == "page_002_only"
    assert report["out_of_scope_pages_rejected"] == OUT_OF_SCOPE_PAGES
    assert report["bridge_blocker_before_audit"] == "needs_source_asset_recovery"
    assert report["bridge_remediation_route_family"] == "needs_source_asset_recovery"
    assert report["bridge_blocker_cleared"] is False
    assert report["asset_recovery_classification"] == "recoverable_from_pinned_page_image_and_source_reconstruction_artifacts"
    assert report["recovery_resolution"] == "recoverable_but_not_materialized"
    assert report["allowed_next_action"] == "separate_bounded_p002_source_asset_materialization_authorization"


def test_p002_source_asset_recovery_audit_authority_risk_is_explicit():
    report = read_report()
    assert report["source_acceptance_chain_available"] is True
    assert report["source_acceptance_chain_authority_risk"] == "stale_generator_hash_in_completion_artifact"
    assert report["recorded_completion_builder_hash"] != CURRENT_COMPLETION_BUILDER_HASH
    assert report["current_completion_builder_hash"] == CURRENT_COMPLETION_BUILDER_HASH
    assert report["completion_builder_hash_stale"] is True
    assert report["human_verified_text_available"] is True
    assert report["review_assets_missing_in_original_page_complete_review"] is True
    assert report["alternate_page_image_available"] is True
    assert report["corrected_crop_refs_available"] is True


def test_p002_source_asset_recovery_audit_boundary_flags():
    report = read_report()
    false_flags = [
        "review_assets_materialized",
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
    assert all(item["materialized_by_this_lane"] is False for item in report["recovered_asset_candidates"])


def test_p002_source_asset_recovery_audit_output_tree_is_minimal():
    read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "p002_source_asset_recovery_audit_manifest.md",
        "p002_source_asset_recovery_audit_report.json",
        "p002_source_asset_recovery_audit_summary.md",
    ]
    assert not any("021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "does not materialize `review_assets`" in summary
    assert "Bridge blocker cleared: `false`" in summary
    assert "report-only recovery audit" in manifest
    for output in output_files:
        if output != "p002_source_asset_recovery_audit_manifest.md":
            assert output in manifest
