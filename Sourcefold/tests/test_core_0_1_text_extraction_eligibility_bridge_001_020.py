from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_eligibility_bridge_001_020 import (  # noqa: E402
    ALL_COVERED_PAGES,
    AUTHORIZATION_ID,
    BRIDGE_PAGES,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    OUT_ROOT,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_eligibility_bridge_001_020.py"
REPORT = OUT_ROOT / "eligibility_bridge_001_020_report.json"
SUMMARY = OUT_ROOT / "eligibility_bridge_001_020_summary.md"
MANIFEST = OUT_ROOT / "eligibility_bridge_001_020_manifest.md"
BRIDGE_ENTRIES = OUT_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json"
REPLAY_V4 = OUT_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("eligibility bridge output has not been generated yet")


def test_eligibility_bridge_is_fail_closed():
    no_args = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_args.returncode != 0
    assert "--execute" in no_args.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "wrong", "--decision", "ок делай"],
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


def test_eligibility_bridge_refuses_overwrite():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; overwrite refusal is covered by generated-output state")
    OUT_ROOT.mkdir(parents=True)
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTHORIZATION_ID, "--decision", "ок делай"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    finally:
        OUT_ROOT.rmdir()
    assert result.returncode != 0
    assert "refusing to overwrite existing output directory" in result.stderr


def test_eligibility_bridge_pre_output_scope_and_pins():
    verified, asm_report, _asm_manifest, acceptances = verify_inputs()

    assert asm_report["status"] == "assembly_readiness_manifest_only_production_blocked"
    assert asm_report["production_ready"] is False
    assert sorted(acceptances) == BRIDGE_PAGES
    assert len(verified) == 12
    for page in BRIDGE_PAGES:
        key = f"P{page}PCA-G1-VIRAL-001.report"
        assert verified[key]["sha256"]


def test_eligibility_bridge_report_covers_all_pages_but_keeps_production_blocked():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "eligibility_bridge_static_evidence_all_pages_covered_production_blocked"
    assert report["bridge_pages"] == BRIDGE_PAGES
    assert report["covered_pages_v4"] == ALL_COVERED_PAGES
    assert report["all_pages_static_evidence_covered"] is True
    assert report["all_pages_first_pass_success"] is False
    assert report["production_ready"] is False
    assert report["production_assembly_created"] is False
    assert report["clean_production_output_folder_created"] is False


def test_eligibility_bridge_entries_classify_ineligible_and_parked_pages():
    require_outputs()
    entries = read_json(BRIDGE_ENTRIES)
    by_page = {entry["page"]: entry for entry in entries}

    assert sorted(by_page) == BRIDGE_PAGES
    for page in ["001", "002", "003", "004", "005", "006", "007", "008"]:
        assert by_page[page]["selector_decision"] == "accepted_page_complete_bridge"
        assert by_page[page]["accepted_page_complete_only"] is True
        assert by_page[page]["imported_from_prior_accepted_lane"] is True
    for page in ["014", "019"]:
        assert by_page[page]["selector_decision"] == "parked_overview_but_page_complete_accepted_bridge"
        assert by_page[page]["accepted_page_complete_only"] is True
    for entry in entries:
        assert entry["new_first_pass_ocr_selector_result"] is False
        assert entry["candidate_text_copied"] is False
        assert entry["production_output_created"] is False


def test_selector_replay_v4_routes_all_pages_without_runtime_or_production():
    require_outputs()
    replay = read_json(REPLAY_V4)

    assert [entry["page"] for entry in replay] == ALL_COVERED_PAGES
    selected_statuses = {"selected_static_evidence_only", "selected_static_evidence_manifest_only"}
    assert {entry["page"] for entry in replay if entry.get("selection_status") in selected_statuses or entry.get("status") in selected_statuses} == set(
        ALL_COVERED_PAGES
    )
    bridge_decisions = {entry["selector_decision"] for entry in replay if entry["page"] in BRIDGE_PAGES}
    assert bridge_decisions == {"accepted_page_complete_bridge", "parked_overview_but_page_complete_accepted_bridge"}
    assert all(entry.get("production_output_created") is False for entry in replay)


def test_eligibility_bridge_preserves_boundaries():
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
    assert "All pages first-pass success: `false`." in summary
    assert "`production_assembly_created=false`" in summary
    assert "`acceptance_performed=false`" in summary


def test_eligibility_bridge_manifest_covers_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`bridge_entries/accepted_page_complete_bridge_entries.json`" in manifest
    assert "`selector_replay_v4/selector_replay_v4_selections.json`" in manifest
    assert "`eligibility_bridge_001_020_report.json`" in manifest
    assert "no production output" in manifest
