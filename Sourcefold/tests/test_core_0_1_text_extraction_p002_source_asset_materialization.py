from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.run_core_0_1_text_extraction_p002_source_asset_materialization import (  # noqa: E402
    AUTHORIZATION_ID,
    CREATION_HEAD,
    HISTORICAL_REVIEW_ASSETS,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    OUTPUT_FILES,
    PAGE,
    PINNED_INPUTS,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_p002_source_asset_materialization.py"
REPORT = OUT_ROOT / "p002_source_asset_materialization_report.json"
SUMMARY = OUT_ROOT / "p002_source_asset_materialization_summary.md"
MANIFEST = OUT_ROOT / "p002_source_asset_materialization_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("P002 source asset materialization output has not been generated yet")


def sha256_file(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_p002_source_asset_materialization_is_fail_closed():
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


def test_p002_source_asset_materialization_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, auth_report, recovery_report = verify_inputs()
    assert sorted(verified) == sorted(PINNED_INPUTS)
    assert auth_report["lane_id"] == "C01TEP002ASSETMATAUTH-G1-VIRAL-001"
    assert auth_report["allowed_next_action"] == "execute_separate_bounded_p002_source_asset_materialization_from_pinned_recovery_audit"
    assert recovery_report["lane_id"] == "C01TEP002ASSETREC-G1-VIRAL-001"
    assert recovery_report["page"] == PAGE
    assert recovery_report["bridge_blocker_cleared"] is False


def test_p002_source_asset_materialization_report_contract():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "p002_source_asset_materialization_completed_output_surface_only_no_blocker_clearance_no_mutation"
    assert report["base_commit"] == CREATION_HEAD
    assert report["current_head"] == CREATION_HEAD
    assert report["input_lane_ids"] == ["C01TEP002ASSETMATAUTH-G1-VIRAL-001", "C01TEP002ASSETREC-G1-VIRAL-001"]
    assert report["page"] == PAGE
    assert report["scope"] == "page_002_source_asset_materialization_output_surface_only"
    assert report["output_root_created_clean"] is True
    assert report["materialized_surface_created"] is True
    assert report["materialized_surface_is_recoverability_evidence_only"] is True
    assert report["source_acceptance_chain_authority_risk"] == "stale_generator_hash_in_completion_artifact"
    assert report["stale_generator_hash_risk_preserved"] is True
    assert report["bridge_blocker_cleared"] is False


def test_p002_source_asset_materialization_copy_integrity():
    require_outputs()
    report = read_json(REPORT)
    assert len(report["materialized_assets"]) == 3
    for item in report["materialized_assets"]:
        source_path = ROOT / item["source_path"]
        materialized_path = ROOT / item["materialized_path"]
        assert materialized_path.exists()
        assert sha256_file(source_path) == item["source_sha256"]
        assert sha256_file(materialized_path) == item["materialized_sha256"]
        assert item["source_sha256"] == item["materialized_sha256"]


def test_p002_source_asset_materialization_output_tree_and_historical_boundary():
    require_outputs()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())
    assert output_files == sorted(OUTPUT_FILES)
    assert not any("021" in path or "page_021" in path for path in output_files)
    assert not HISTORICAL_REVIEW_ASSETS.exists()


def test_p002_source_asset_materialization_boundaries():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    false_flags = [
        "historical_page_complete_review_review_assets_mutated",
        "bridge_blocker_cleared",
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
        "acceptance_performed",
        "page_021_plus_included",
        "push_performed",
        "promotion_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert "recoverability evidence only" in summary
    assert "does not embed its own post-write SHA-256" in manifest


def test_p002_source_asset_materialization_script_avoids_unbounded_discovery_and_forbidden_execution():
    text = SCRIPT.read_text(encoding="utf-8")
    forbidden = [
        "latest",
        ".glob(",
        "pytesseract",
        "subprocess.run([\"tesseract\"",
        "subprocess.run(['tesseract'",
        "fitz.open",
        "pdfplumber",
        "pypdf",
    ]
    for token in forbidden:
        assert token not in text
