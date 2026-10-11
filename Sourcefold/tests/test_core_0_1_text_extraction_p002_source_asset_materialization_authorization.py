from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_p002_source_asset_materialization_authorization import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    PAGE,
    PINNED_INPUTS,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_p002_source_asset_materialization_authorization.py"
REPORT = OUT_ROOT / "p002_source_asset_materialization_authorization_report.json"
SUMMARY = OUT_ROOT / "p002_source_asset_materialization_authorization_summary.md"
MANIFEST = OUT_ROOT / "p002_source_asset_materialization_authorization_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("P002 materialization authorization output has not been generated yet")


def sha256_file(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_p002_materialization_authorization_is_fail_closed():
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


def test_p002_materialization_authorization_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, recovery_report = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert recovery_report["lane_id"] == "C01TEP002ASSETREC-G1-VIRAL-001"
    assert recovery_report["page"] == PAGE
    assert recovery_report["bridge_blocker_cleared"] is False
    assert recovery_report["allowed_next_action"] == "separate_bounded_p002_source_asset_materialization_authorization"


def test_p002_materialization_authorization_report_contract():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "p002_source_asset_materialization_authorization_recorded_future_lane_only_no_materialization_no_mutation"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_id"] == "C01TEP002ASSETREC-G1-VIRAL-001"
    assert report["page"] == PAGE
    assert report["scope"] == "page_002_materialization_authorization_only"
    assert report["input_lane_ids"] == ["C01TEP002ASSETREC-G1-VIRAL-001"]
    assert report["out_of_scope_pages_rejected"] == [
        "001",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
        "009",
        "010",
        "011",
        "012",
        "013",
        "014",
        "015",
        "016",
        "017",
        "018",
        "019",
        "020",
        "021+",
    ]
    assert report["recovery_audit_classification"] == "recoverable_from_pinned_page_image_and_source_reconstruction_artifacts"
    assert report["source_acceptance_chain_authority_risk"] == "stale_generator_hash_in_completion_artifact"
    assert report["stale_generator_hash_risk_preserved"] is True
    assert report["completion_builder_hash_stale"] is True
    assert report["authorized_future_action"] == "separate_bounded_p002_source_asset_materialization_lane_only"
    assert report["future_materialization_lane_authorized"] is True
    assert report["future_materialization_authorized"] is True
    assert report["future_materialization_may_create_review_assets"] is True
    assert report["future_materialization_may_clear_bridge_blocker"] is False
    assert report["future_materialization_may_accept_source_or_page_status"] is False
    assert report["future_materialization_may_run_ocr_or_tesseract"] is False
    assert report["future_materialization_may_run_render_or_pdf_parsing"] is False
    assert report["allowed_next_action"] == "execute_separate_bounded_p002_source_asset_materialization_from_pinned_recovery_audit"


def test_p002_materialization_authorization_pins_match_disk_after_materialization():
    require_outputs()
    report = read_json(REPORT)
    for key, item in report["verified_inputs"].items():
        expected_path, _ = PINNED_INPUTS[key]
        assert item["path"] == expected_path.relative_to(ROOT).as_posix()
        assert item["sha256"] == sha256_file(expected_path)


def test_p002_materialization_authorization_boundaries_and_output_tree():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    false_flags = [
        "materialization_performed",
        "review_assets_materialized",
        "bridge_blocker_cleared",
        "ocr_execution_performed",
        "tesseract_invocation_authorized",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "fixture_admission_performed",
        "production_ready",
        "production_assembly_authorized",
        "acceptance_performed",
        "page_021_plus_included",
        "push_performed",
        "promotion_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert "does not" in summary
    assert "stale generator-hash authority risk" in summary
    assert "report/summary/manifest only" in manifest
    assert "does not embed its own post-write SHA-256" in manifest
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.iterdir() if path.is_file())
    assert output_files == [
        "p002_source_asset_materialization_authorization_manifest.md",
        "p002_source_asset_materialization_authorization_report.json",
        "p002_source_asset_materialization_authorization_summary.md",
    ]
    assert not any("021" in path or "page_021" in path for path in output_files)
    review_assets = (
        ROOT
        / "fixtures"
        / "candidate_inputs"
        / "viral"
        / "render_trials"
        / "RT-G1-VIRAL-RENDER-001"
        / "page_complete_review_p002_G1_VIRAL_001"
        / "review_assets"
    )
    assert not review_assets.exists()


def test_p002_materialization_authorization_script_avoids_unbounded_discovery_and_execution():
    text = SCRIPT.read_text(encoding="utf-8")
    forbidden = [
        ".glob(",
        ".rglob(",
        "latest",
        "pytesseract",
        "subprocess.run([\"tesseract\"",
        "subprocess.run(['tesseract'",
        "fitz.open",
        "pdfplumber",
        "pypdf",
        "shutil.copy",
        "review_assets.mkdir",
    ]
    for token in forbidden:
        assert token not in text
