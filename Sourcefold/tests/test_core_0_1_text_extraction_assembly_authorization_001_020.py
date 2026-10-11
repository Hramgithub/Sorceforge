from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_assembly_authorization_001_020 import (  # noqa: E402
    AUTHORIZATION_ID,
    BRIDGE_PAGES,
    HUMAN_DECISION,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    OUT_ROOT,
    REQUESTED_PAGES,
    STATIC_SELECTED_PAGES,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_assembly_authorization_001_020.py"
REPORT = OUT_ROOT / "assembly_authorization_001_020_report.json"
SUMMARY = OUT_ROOT / "assembly_authorization_001_020_summary.md"
MANIFEST = OUT_ROOT / "assembly_authorization_001_020_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("assembly authorization output has not been generated yet")


def test_assembly_authorization_is_fail_closed():
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


def test_assembly_authorization_refuses_overwrite():
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


def test_assembly_authorization_pre_output_scope_and_pins():
    verified, bridge_report, bridge_entries, replay_v4 = verify_inputs()

    assert bridge_report["status"] == "eligibility_bridge_static_evidence_all_pages_covered_production_blocked"
    assert bridge_report["covered_pages_v4"] == REQUESTED_PAGES
    assert bridge_report["all_pages_static_evidence_covered"] is True
    assert bridge_report["all_pages_first_pass_success"] is False
    assert bridge_report["production_ready"] is False
    assert sorted(entry["page"] for entry in bridge_entries) == BRIDGE_PAGES
    assert [entry["page"] for entry in replay_v4] == REQUESTED_PAGES
    assert sorted(verified) == [
        "C01TEBRIDGE020-G1-VIRAL-001.bridge_entries",
        "C01TEBRIDGE020-G1-VIRAL-001.report",
        "C01TEBRIDGE020-G1-VIRAL-001.selector_v4",
        "C01TEBRIDGE020-G1-VIRAL-001.summary",
    ]


def test_assembly_authorization_report_blocks_mixed_static_production():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "assembly_authorization_checked_production_not_authorized"
    assert report["covered_pages_v4"] == REQUESTED_PAGES
    assert report["bridge_pages"] == BRIDGE_PAGES
    assert report["static_selected_pages"] == STATIC_SELECTED_PAGES
    assert report["all_pages_static_evidence_covered"] is True
    assert report["all_pages_first_pass_success"] is False
    assert report["mixed_static_evidence_and_accepted_bridge"] is True
    assert report["production_ready"] is False
    assert report["production_assembly_authorized"] is False
    assert report["production_assembly_authorization_decision"] == "not_authorized_from_mixed_static_evidence_while_first_pass_false"
    assert report["production_assembly_created"] is False
    assert report["clean_production_output_folder_created"] is False
    assert "fresh_first_pass_runtime_selector_success" in report["required_before_standard_production_assembly"]
    assert report["allowed_next_routes"] == [
        "fresh_first_pass_runtime_selector_authorization_for_001_020",
        "separate_explicit_human_exception_decision_for_mixed_static_evidence_production",
    ]


def test_assembly_authorization_preserves_boundaries():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    false_flags = [
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "selector_runtime_enabled",
        "runtime_selector_integration",
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
    assert "Production assembly authorized: `false`." in summary
    assert "not authorized from mixed static evidence" in summary
    assert "`production_assembly_created=false`" in summary
    assert "`runtime_selector_integration=false`" in summary


def test_assembly_authorization_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`assembly_authorization_001_020_report.json`" in manifest
    assert "`assembly_authorization_001_020_summary.md`" in manifest
    assert "no production assembly" in manifest
