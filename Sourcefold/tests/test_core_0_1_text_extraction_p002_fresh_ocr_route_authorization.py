from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p002_fresh_ocr_route_authorization import (  # noqa: E402
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


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_fresh_ocr_route_authorization.py"
REPORT = OUT_ROOT / "p002_fresh_ocr_route_authorization_report.json"
SUMMARY = OUT_ROOT / "p002_fresh_ocr_route_authorization_summary.md"
MANIFEST = OUT_ROOT / "p002_fresh_ocr_route_authorization_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 fresh OCR route authorization output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_fresh_ocr_route_authorization_is_fail_closed():
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


def test_p002_fresh_ocr_route_authorization_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, review_report = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert review_report["lane_id"] == INPUT_LANE_ID
    assert review_report["page"] == PAGE
    assert review_report["p002_ready_for_fresh_ocr_route_authorization"] is True
    assert review_report["next_blocker"] == "needs_fresh_ocr_route_authorization"


def test_p002_fresh_ocr_route_authorization_report_contract():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_fresh_ocr_route_authorized_no_execution"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_id"] == INPUT_LANE_ID
    assert report["page"] == PAGE
    assert report["fresh_ocr_route_authorized"] is True
    assert report["authorized_future_ocr_page_image"] == "P002.page_image"
    assert report["authorized_future_ocr_surface_class"] == "full_page_region"
    assert report["corrected_crop_refs_authorized_as_ocr_input"] is False
    assert report["corrected_crop_refs_authorized_for_comparison_only"] is True
    assert report["candidate_hash_must_be_sealed_before_reference_scoring"] is True
    assert report["allowed_next_action"] == "separate_bounded_p002_fresh_ocr_candidate_execution"


def test_p002_fresh_ocr_route_authorization_surface_roles_and_hashes():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert sha256_file(path) == expected_hash
    roles = {item["input_key"]: item["authorized_role"] for item in report["materialized_surface_entries"]}
    assert roles["P002.page_image"] == "full_page_region_candidate_input"
    assert roles["P002.corrected_crop_ref.1"] == "crop_reference_comparison_only_not_ocr_input"
    assert roles["P002.corrected_crop_ref.2"] == "crop_reference_comparison_only_not_ocr_input"
    for item in report["materialized_surface_entries"]:
        assert sha256_file(ROOT / item["path"]) == item["sha256"]


def test_p002_fresh_ocr_route_authorization_boundaries_and_output_tree():
    report = read_report()
    false_flags = [
        "ocr_execution_performed",
        "tesseract_invoked",
        "fresh_ocr_success",
        "candidate_text_created",
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
        "bridge_blocker_cleared",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert not any("021" in path for path in output_files)
    assert "OCR execution performed: `false`" in SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "Fresh OCR success: `false`" in manifest
    assert "`p002_fresh_ocr_route_authorization_manifest.md`: sealed by external sync surfaces" in manifest
    assert sha256_file(MANIFEST) not in manifest


def test_p002_fresh_ocr_route_authorization_avoids_execution_and_unbounded_discovery():
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
