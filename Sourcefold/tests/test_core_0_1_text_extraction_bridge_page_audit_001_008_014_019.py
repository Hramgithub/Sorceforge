from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_bridge_page_audit_001_008_014_019 import (  # noqa: E402
    AUDIT_PAGES,
    AUTHORIZATION_ID,
    HUMAN_DECISION,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    NEXT_ROUTES,
    OUT_ROOT,
    REQUESTED_PAGES,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_bridge_page_audit_001_008_014_019.py"
REPORT = OUT_ROOT / "bridge_page_audit_001_008_014_019_report.json"
SUMMARY = OUT_ROOT / "bridge_page_audit_001_008_014_019_summary.md"
MANIFEST = OUT_ROOT / "bridge_page_audit_001_008_014_019_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("bridge page audit output has not been generated yet")


def test_bridge_page_audit_is_fail_closed():
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


def test_bridge_page_audit_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, run_report, _selector_v4, bridge_entries = verify_inputs()

    assert sorted(run_report["bridge_lineage_pages"]) == AUDIT_PAGES
    assert sorted(entry["page"] for entry in bridge_entries) == AUDIT_PAGES
    assert sorted(verified) == [
        "C01TEBRIDGE020-G1-VIRAL-001.bridge_entries",
        "C01TEBRIDGE020-G1-VIRAL-001.selector_v4",
        "C01TEFPSRUN020-G1-VIRAL-001.manifest",
        "C01TEFPSRUN020-G1-VIRAL-001.report",
    ]


def test_bridge_page_audit_report_classifies_only_bridge_pages():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "bridge_page_audit_completed_no_ocr_no_mutation"
    assert report["requested_pages"] == REQUESTED_PAGES
    assert report["audited_bridge_pages"] == AUDIT_PAGES
    assert report["audit_pages"] == AUDIT_PAGES
    assert [item["page"] for item in report["page_audit"]] == AUDIT_PAGES
    assert report["all_bridge_pages_remain_non_fresh"] is True
    assert set(report["visual_only_no_text_rule_pages"]) | set(report["fresh_ocr_route_possible_pages"]) | set(
        report["fresh_ocr_assets_missing_pages"]
    ) | set(report["needs_source_asset_recovery_pages"]) == set(AUDIT_PAGES)
    assert not any(page >= "021" for page in report["audit_pages"])
    for item in report["page_audit"]:
        assert item["next_route"] in NEXT_ROUTES
        assert item["recommended_next_route"] == item["next_route"]
        assert item["asset_classification"] == "bridge_page_existing_asset_audit"
        assert item["fresh_ocr_success_created"] is False
        assert item["production_or_acceptance_created"] is False
        assert "asset_availability_only" in item["route_reason"] or item["next_route"] != "fresh_ocr_route_possible"
        assert item["acceptance_report_sha256"]
        assert item["acceptance_report_path"]
        for collection in ["text_evidence_crops", "text_maps", "ocr_verified_text_maps", "semantic_text_maps"]:
            for asset in item[collection]:
                assert (ROOT / asset["path"]).exists()
                assert asset["sha256"]


def test_bridge_page_audit_preserves_boundaries():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    false_flags = [
        "ocr_execution_performed",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "runtime_execution_performed",
        "acceptance_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "fixture_admission_performed",
        "page_021_plus_included",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert set(report["negative_capability_matrix"]) == set(NEGATIVE_CAPABILITIES)
    for capability, value in report["negative_capability_matrix"].items():
        assert value is False, capability
    assert "does not execute OCR" in summary
    assert "does not count bridge lineage as fresh first-pass success" in summary


def test_bridge_page_audit_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`bridge_page_audit_001_008_014_019_report.json`" in manifest
    assert "`bridge_page_audit_001_008_014_019_summary.md`" in manifest
    assert "no OCR execution" in manifest


def test_bridge_page_audit_output_tree_is_report_only():
    require_outputs()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())

    assert output_files == [
        "bridge_page_audit_001_008_014_019_manifest.md",
        "bridge_page_audit_001_008_014_019_report.json",
        "bridge_page_audit_001_008_014_019_summary.md",
    ]
    assert not any("021" in path or "page_021" in path for path in output_files)
