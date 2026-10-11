from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p002_materialized_surface_review import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HUMAN_DECISION,
    INPUT_LANE_ID,
    LANE_ID,
    OUT_ROOT,
    OUTPUT_FILES,
    PAGE,
    PINNED_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_materialized_surface_review.py"
REPORT = OUT_ROOT / "p002_materialized_surface_review_report.json"
SUMMARY = OUT_ROOT / "p002_materialized_surface_review_summary.md"
MANIFEST = OUT_ROOT / "p002_materialized_surface_review_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 materialized surface review output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_materialized_surface_review_is_fail_closed():
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


def test_p002_materialized_surface_review_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, materialization_report = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert materialization_report["lane_id"] == INPUT_LANE_ID
    assert materialization_report["bridge_blocker_cleared"] is False
    assert materialization_report["allowed_next_action"] == "separate_bounded_p002_materialized_surface_review_before_blocker_clearance"


def test_p002_materialized_surface_review_materialized_pins_still_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert report["verified_inputs"][key]["sha256"] == expected_hash


def test_p002_materialized_surface_review_report_contract():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_materialized_surface_review_completed_asset_recovery_blocker_cleared_no_ocr_no_acceptance"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_id"] == INPUT_LANE_ID
    assert report["page"] == PAGE
    assert report["asset_recovery_blocker_before_review"] == "needs_source_asset_recovery"
    assert report["asset_recovery_blocker_cleared"] is True
    assert report["bridge_blocker_cleared"] is True
    assert report["next_blocker"] == "needs_fresh_ocr_route_authorization"
    assert report["p002_ready_for_fresh_ocr_route_authorization"] is True
    assert report["fresh_ocr_success"] is False
    assert report["allowed_next_action"] == "separate_bounded_p002_fresh_ocr_route_authorization_or_clean_runtime_selector_policy_update"


def test_p002_materialized_surface_review_asset_hashes_are_verified():
    report = read_report()
    assert len(report["reviewed_assets"]) == 3
    assert sorted(item["input_key"] for item in report["reviewed_assets"]) == [
        "P002.corrected_crop_ref.1",
        "P002.corrected_crop_ref.2",
        "P002.page_image",
    ]
    for item in report["reviewed_assets"]:
        path = ROOT / item["materialized_path"]
        assert path.exists()
        assert sha256_file(path) == item["materialized_sha256"]
        assert item["review_status"] == "hash_verified_materialized_surface_available"


def test_p002_materialized_surface_review_boundaries():
    report = read_report()
    false_flags = [
        "fresh_ocr_success",
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
        "promotion_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert report["source_acceptance_chain_authority_risk"] == "stale_generator_hash_in_completion_artifact"
    assert report["stale_generator_hash_risk_preserved"] is True


def test_p002_materialized_surface_review_output_tree_is_minimal():
    read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert not any("021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "asset_recovery_blocker_cleared=true" in summary
    assert "fresh_ocr_success=false" in summary
    assert "Asset recovery blocker cleared: `true`" in manifest
    assert "Fresh OCR success: `false`" in manifest


def test_p002_materialized_surface_review_avoids_unbounded_discovery_and_forbidden_execution():
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
