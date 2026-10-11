from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_core_0_1_text_extraction_p014_p019_full_page_ocr import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    OUTPUT_FILES,
    PAGES,
    PINNED_INPUTS,
    TESSERACT,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p014_p019_full_page_ocr.py"
REPORT = OUT_ROOT / "p014_p019_full_page_ocr_report.json"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P014/P019 full-page OCR output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p014_p019_full_page_ocr_is_fail_closed():
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


def test_p014_p019_full_page_ocr_pre_output_pins_and_authority():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, decision = verify_inputs()
    assert TESSERACT.exists()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert decision["lane_id"] == "C01TEP014019ROUTEDEC-G1-VIRAL-001"
    assert decision["future_full_page_ocr_route_authorized"] is True
    assert decision["future_full_page_ocr_route_may_use_text_evidence_crops_as_ocr_input"] is False


def test_p014_p019_full_page_ocr_report_contract():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p014_p019_full_page_ocr_completed_candidate_only_no_promotion"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["pages"] == PAGES
    assert report["ocr_execution_performed"] is True
    assert report["tesseract_invoked"] is True
    assert report["tesseract_invoked_pages"] == PAGES
    assert report["ocr_input_surface_class"] == "full_page_region"
    assert report["text_evidence_crops_used_as_ocr_input"] is False
    assert report["candidate_hash_sealed_before_reference_scoring"] is True
    assert report["candidate_count"] == 4
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_for_pages"] == []


def test_p014_p019_full_page_ocr_candidate_entries_are_full_page_only():
    report = read_report()
    for item in report["candidate_entries"]:
        assert item["page"] in PAGES
        assert item["psm"] in [4, 6]
        assert item["surface"]["surface_class"] == "full_page_region"
        assert item["surface"]["allowed_purpose"] == "candidate_policy"
        assert item["surface_validation"]["status"] == "passed"
        assert "text-evidence" not in item["surface"]["source_artifact"]["path"]
        assert item["candidate_hash_sealed_before_reference_scoring"] is True
        assert item["reference_authority"] == "page_complete_text_map_comparison_only_not_acceptance_truth"
        assert item["fresh_ocr_success"] is False
        assert item["acceptance_effect"] == "none"
        assert item["promotion_effect"] == "none"
        assert Path(ROOT / item["candidate_text_path"]).exists()
        assert sha256_file(ROOT / item["candidate_text_path"]) == item["candidate_text_sha256"]
        assert item["ocr_run"]["transient_ocr_output_persisted"] is False


def test_p014_p019_full_page_ocr_boundaries_and_output_tree():
    report = read_report()
    false_flags = [
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
        "push_performed",
        "promotion_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert not any("021" in path or "raw" in path or "prepared" in path for path in output_files)


def test_p014_p019_full_page_ocr_pins_match_disk():
    report = read_report()
    assert sorted(report["verified_inputs"]) == sorted(PINNED_INPUTS)
    for key, (path, expected_hash) in PINNED_INPUTS.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()
        assert report["verified_inputs"][key]["sha256"] == expected_hash
