from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p014_p019_route_decision import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    OUTPUT_FILES,
    PAGES,
    PINNED_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p014_p019_route_decision.py"
REPORT = OUT_ROOT / "p014_p019_route_decision_report.json"
SUMMARY = OUT_ROOT / "p014_p019_route_decision_summary.md"
MANIFEST = OUT_ROOT / "p014_p019_route_decision_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P014/P019 route decision output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p014_p019_route_decision_is_fail_closed():
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


def test_p014_p019_route_decision_pre_output_pins_and_inputs():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, audit, remediation = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert audit["lane_id"] == "C01TEBRIDGEAUD020-G1-VIRAL-001"
    assert remediation["lane_id"] == "C01TEBRIDGEREM020-G1-VIRAL-001"
    assert remediation["text_evidence_smoke_non_promotable_pages"] == PAGES


def test_p014_p019_route_decision_report_contract():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p014_p019_route_decision_recorded_full_page_ocr_route_required_no_execution"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["pages"] == PAGES
    assert report["text_evidence_smoke_route_reviewed"] is True
    assert report["text_evidence_smoke_remains_non_promotable"] is True
    assert report["existing_smoke_outputs_clear_bridge"] is False
    assert report["existing_smoke_outputs_create_fresh_success"] is False
    assert report["future_full_page_ocr_route_authorized"] is True
    assert report["future_full_page_ocr_route_pages"] == PAGES
    assert report["future_full_page_ocr_route_must_be_separate_lane"] is True
    assert report["future_full_page_ocr_route_may_use_text_evidence_crops_as_ocr_input"] is False
    assert report["allowed_next_action"] == "separate_bounded_014_019_full_page_ocr_route_authorization_or_execution_lane"


def test_p014_p019_route_decision_page_decisions():
    report = read_report()
    assert [item["page"] for item in report["page_decisions"]] == PAGES
    for item in report["page_decisions"]:
        assert item["prior_selector_decision"] == "parked_overview_but_page_complete_accepted_bridge"
        assert item["remediation_route_family"] == "text_evidence_smoke_non_promotable"
        assert item["smoke_non_promotable"] is True
        assert item["existing_smoke_can_clear_bridge"] is False
        assert item["existing_smoke_can_count_as_fresh_ocr_success"] is False
        assert item["full_page_image_available"] is True
        assert item["future_full_page_ocr_route_authorized"] is True
        assert item["future_route_surface_class"] == "full_page_region"
        assert item["future_route_allowed_purpose"] == "candidate_policy"
        assert item["fresh_ocr_success"] is False


def test_p014_p019_route_decision_pins_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert report["verified_inputs"][key]["sha256"] == expected_hash


def test_p014_p019_route_decision_boundaries_and_output_tree():
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
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert "non-promotable" in SUMMARY.read_text(encoding="utf-8-sig")
    assert "Future full-page OCR route authorized: `true`" in MANIFEST.read_text(encoding="utf-8-sig")
    assert not any("021" in path for path in output_files)


def test_p014_p019_route_decision_avoids_unbounded_discovery_and_execution():
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
