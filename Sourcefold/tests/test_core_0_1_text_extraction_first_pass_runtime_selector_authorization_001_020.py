from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020 import (  # noqa: E402
    AUTHORIZATION_ID,
    HUMAN_DECISION,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    OUT_ROOT,
    REQUESTED_PAGES,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020.py"
REPORT = OUT_ROOT / "first_pass_runtime_selector_authorization_001_020_report.json"
SUMMARY = OUT_ROOT / "first_pass_runtime_selector_authorization_001_020_summary.md"
MANIFEST = OUT_ROOT / "first_pass_runtime_selector_authorization_001_020_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("first-pass runtime-selector authorization output has not been generated yet")


def test_first_pass_runtime_selector_authorization_is_fail_closed():
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


def test_first_pass_runtime_selector_authorization_refuses_overwrite():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; overwrite refusal is covered by generated-output state")
    OUT_ROOT.mkdir(parents=True)
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTHORIZATION_ID, "--decision", HUMAN_DECISION],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    finally:
        OUT_ROOT.rmdir()
    assert result.returncode != 0
    assert "refusing to overwrite existing output directory" in result.stderr


def test_first_pass_runtime_selector_authorization_pre_output_scope_and_pins():
    verified, auth_report = verify_inputs()

    assert auth_report["status"] == "assembly_authorization_checked_production_not_authorized"
    assert auth_report["covered_pages_v4"] == REQUESTED_PAGES
    assert auth_report["all_pages_first_pass_success"] is False
    assert auth_report["production_ready"] is False
    assert auth_report["production_assembly_authorized"] is False
    assert sorted(verified) == [
        "C01TEAUTH020-G1-VIRAL-001.manifest",
        "C01TEAUTH020-G1-VIRAL-001.report",
        "C01TEAUTH020-G1-VIRAL-001.summary",
    ]


def test_first_pass_runtime_selector_authorization_report_defines_future_route_only():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "first_pass_runtime_selector_authorization_recorded_report_only"
    assert report["requested_pages"] == REQUESTED_PAGES
    assert report["fresh_first_pass_runtime_selector_route_authorized"] is True
    assert report["authorized_future_route"] == "bounded_fresh_first_pass_runtime_selector_run_for_001_020_only"
    assert report["this_lane_report_only"] is True
    assert report["runtime_selector_implementation_created"] is False
    assert report["selector_runtime_enabled"] is False
    assert report["runtime_execution_performed"] is False
    assert report["production_ready"] is False
    assert report["production_assembly_authorized"] is False
    assert report["production_assembly_created"] is False
    assert report["clean_production_output_folder_created"] is False
    assert report["standard_production_requires_future_clean_first_pass_success"] is True
    assert report["allowed_next_action"] == "implement_or_execute_bounded_fresh_first_pass_runtime_selector_001_020_under_this_authorization"


def test_first_pass_runtime_selector_authorization_preserves_boundaries():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    false_flags = [
        "ocr_execution_performed",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "selector_runtime_enabled",
        "runtime_selector_implementation_created",
        "runtime_execution_performed",
        "page_021_plus_included",
        "promotion_performed",
        "acceptance_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert set(report["negative_capability_matrix"]) == set(NEGATIVE_CAPABILITIES)
    for capability, value in report["negative_capability_matrix"].items():
        assert value is False, capability
    assert "Runtime selector implementation created: `false`." in summary
    assert "Runtime execution performed: `false`." in summary
    assert "Production assembly authorized: `false`." in summary
    assert "`page_021_plus_included=false`" in summary


def test_first_pass_runtime_selector_authorization_guardrails_are_explicit():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert report["future_route_guardrails"] == [
        "page_set_must_equal_001_020",
        "same_bounded_input_set_only",
        "selected_best_methods_or_validated_bridge_lineage_only",
        "failed_and_superseded_variants_excluded_from_clean_output",
        "hash_drift_fails_closed",
        "missing_page_fails_closed",
        "page_021_plus_fails_closed",
        "source_or_raw_mutation_fails_closed",
        "accepted_text_or_page_status_mutation_fails_closed",
        "production_output_before_clean_first_pass_success_fails_closed",
    ]
    assert "`page_021_plus_fails_closed`." in summary
    assert "`production_output_before_clean_first_pass_success_fails_closed`." in summary


def test_first_pass_runtime_selector_authorization_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`first_pass_runtime_selector_authorization_001_020_report.json`" in manifest
    assert "`first_pass_runtime_selector_authorization_001_020_summary.md`" in manifest
    assert "no runtime execution" in manifest
    assert "no production output" in manifest
