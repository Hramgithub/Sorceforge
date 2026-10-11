from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_core_0_1_text_extraction_p002_fresh_ocr_candidate import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HUMAN_DECISION,
    INPUT_LANE_ID,
    LANE_ID,
    OUT_ROOT,
    OUTPUT_FILES,
    PAGE,
    PINNED_INPUTS,
    PSM_VALUES,
    TESSERACT,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p002_fresh_ocr_candidate.py"
REPORT = OUT_ROOT / "p002_fresh_ocr_candidate_report.json"
MANIFEST = OUT_ROOT / "p002_fresh_ocr_candidate_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 fresh OCR candidate output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_fresh_ocr_candidate_is_fail_closed():
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


def test_p002_fresh_ocr_candidate_pre_output_pins_and_authority():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, route = verify_inputs()
    assert TESSERACT.exists()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert route["lane_id"] == INPUT_LANE_ID
    assert route["page"] == PAGE
    assert route["fresh_ocr_route_authorized"] is True
    assert route["corrected_crop_refs_authorized_as_ocr_input"] is False


def test_p002_fresh_ocr_candidate_report_contract():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_fresh_ocr_candidate_executed_candidate_only_no_scoring_no_promotion"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_id"] == INPUT_LANE_ID
    assert report["page"] == PAGE
    assert report["ocr_execution_performed"] is True
    assert report["tesseract_invoked"] is True
    assert report["tesseract_invoked_pages"] == [PAGE]
    assert report["psm_values"] == PSM_VALUES
    assert report["ocr_input_surface_class"] == "full_page_region"
    assert report["corrected_crop_refs_used_as_ocr_input"] is False
    assert report["candidate_hash_sealed_before_reference_scoring"] is True
    assert report["reference_scoring_performed"] is False
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_for_pages"] == []


def test_p002_fresh_ocr_candidate_entries_are_full_page_only():
    report = read_report()
    assert len(report["candidate_entries"]) == 2
    for item in report["candidate_entries"]:
        assert item["page"] == PAGE
        assert item["psm"] in PSM_VALUES
        assert item["surface"]["surface_class"] == "full_page_region"
        assert item["surface"]["allowed_purpose"] == "candidate_policy"
        assert item["surface_validation"]["status"] == "passed"
        assert "crop" not in item["surface"]["source_artifact"]["path"].lower()
        assert item["candidate_hash_sealed"] is True
        assert item["reference_scoring_performed"] is False
        assert item["fresh_ocr_success"] is False
        assert item["acceptance_effect"] == "none"
        assert item["promotion_effect"] == "none"
        assert Path(ROOT / item["candidate_text_path"]).exists()
        assert sha256_file(ROOT / item["candidate_text_path"]) == item["candidate_text_sha256"]
        assert item["ocr_run"]["transient_ocr_output_persisted"] is False


def test_p002_fresh_ocr_candidate_boundaries_and_output_tree():
    report = read_report()
    false_flags = [
        "fresh_ocr_success",
        "bridge_blocker_cleared",
        "reference_scoring_performed",
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
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert not any("021" in path or "raw" in path or "prepared" in path for path in output_files)
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "`p002_fresh_ocr_candidate_manifest.md`: sealed by external sync surfaces" in manifest
    assert sha256_file(MANIFEST) not in manifest


def test_p002_fresh_ocr_candidate_pins_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert report["verified_inputs"][key]["sha256"] == expected_hash


def test_p002_fresh_ocr_candidate_avoids_unbounded_discovery_and_forbidden_inputs():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = [
        "latest",
        ".glob(",
        ".rglob(",
        "pytesseract",
        "fitz.open",
        "pdfplumber",
        "pypdf",
        "run_render",
        "render_pdf",
    ]
    for needle in forbidden:
        assert needle not in source
    assert "crop_reference_comparison_only_not_ocr_input" in source
