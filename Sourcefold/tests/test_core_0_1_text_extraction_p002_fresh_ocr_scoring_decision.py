from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_core_0_1_text_extraction_p002_fresh_ocr_scoring_decision import (  # noqa: E402
    AUDIT_INPUTS,
    AUTHORIZATION_ID,
    CANDIDATE_INPUTS,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    THRESHOLD,
    VERIFY_INPUTS,
    sha256_file,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_fresh_ocr_scoring_decision.py"
REPORT = OUT_ROOT / "p002_fresh_ocr_scoring_decision_report.json"
SUMMARY = OUT_ROOT / "p002_fresh_ocr_scoring_decision_summary.md"
MANIFEST = OUT_ROOT / "p002_fresh_ocr_scoring_decision_manifest.md"


def read_report() -> dict:
    if not REPORT.exists():
        pytest.skip("P002 fresh OCR scoring decision output has not been generated yet")
    return json.loads(REPORT.read_text(encoding="utf-8-sig"))


def test_p002_fresh_ocr_scoring_decision_is_fail_closed():
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


def test_p002_fresh_ocr_scoring_decision_pre_output_pins():
    if OUT_ROOT.exists():
        pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, audit_report, verify_report = verify_inputs()
    assert audit_report["lane_id"] == "C01TEP002FRESHSCOREAUD-G1-VIRAL-001"
    assert audit_report["fresh_ocr_success_pages"] == []
    assert "verified_text" in json.dumps(verify_report)
    for label in CANDIDATE_INPUTS:
        assert f"candidate.{label}" in verified
    for label in VERIFY_INPUTS:
        assert label in verified


def test_p002_fresh_ocr_scoring_decision_materialized_pins_still_match_disk():
    report = read_report()
    expected = {
        **{key: item for key, item in AUDIT_INPUTS.items()},
        **{f"candidate.{label}": item for label, item in CANDIDATE_INPUTS.items()},
        **VERIFY_INPUTS,
    }
    assert sorted(report["verified_inputs"]) == sorted(expected)
    for key, (path, expected_hash) in expected.items():
        assert sha256_file(path) == expected_hash
        assert report["verified_inputs"][key]["sha256"] == expected_hash
        assert report["verified_inputs"][key]["path"] == path.relative_to(ROOT).as_posix()


def test_p002_fresh_ocr_scoring_decision_no_latest_or_unbounded_discovery():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = ["latest", ".glob(", ".rglob(", "Get-ChildItem", "TESSERACT =", "run_tesseract"]
    for needle in forbidden:
        assert needle not in source
    assert "AUDIT_INPUTS" in source
    assert "VERIFY_INPUTS" in source


def test_p002_fresh_ocr_scoring_decision_contract_and_result():
    report = read_report()
    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_fresh_ocr_scoring_decision_completed_remediation_required"
    assert report["input_lane_id"] == "C01TEP002FRESHSCOREAUD-G1-VIRAL-001"
    assert report["page"] == "002"
    assert report["strict_threshold"] == THRESHOLD
    assert report["selected_best_candidate"] == "psm4"
    assert report["selected_best_candidate_threshold_met"] is False
    assert report["decision"] == "remediation_required_before_fresh_ocr_success"
    assert report["fresh_ocr_success_pages"] == []
    assert report["bridge_removed_for_pages"] == []
    assert report["promotable_pages"] == []
    psm4 = next(item for item in report["candidate_entries"] if item["candidate_label"] == "psm4")
    psm6 = next(item for item in report["candidate_entries"] if item["candidate_label"] == "psm6")
    assert psm4["diagnostic_metrics"]["sequence_similarity_ratio"] > psm6["diagnostic_metrics"]["sequence_similarity_ratio"]
    assert psm4["diagnostic_metrics"]["sequence_similarity_ratio"] < THRESHOLD
    assert psm4["diagnostic_metrics"]["token_recall"] < THRESHOLD


def test_p002_fresh_ocr_scoring_decision_boundary_flags():
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
        assert item["fresh_ocr_success"] is False
        assert item["promotable"] is False
        assert item["bridge_removal_effect"] == "none"


def test_p002_fresh_ocr_scoring_decision_output_tree_is_minimal():
    report = read_report()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "p002_fresh_ocr_scoring_decision_manifest.md",
        "p002_fresh_ocr_scoring_decision_report.json",
        "p002_fresh_ocr_scoring_decision_summary.md",
    ]
    assert not any("001" in path or "003" in path or "014" in path or "019" in path or "021" in path for path in output_files)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    assert "remediation is required" in summary
    assert "scoring decision only" in manifest
    for output in output_files:
        if output != "p002_fresh_ocr_scoring_decision_manifest.md":
            assert output in manifest
    assert report["allowed_next_action"] == "bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs"
