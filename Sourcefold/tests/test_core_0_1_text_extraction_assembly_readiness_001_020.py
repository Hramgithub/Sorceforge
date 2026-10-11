from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_assembly_readiness_001_020 import (  # noqa: E402
    AUTHORIZATION_ID,
    EXPECTED_SELECTED_HASHES,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    NOT_RUN_INELIGIBLE,
    OUT_ROOT,
    PARKED_PAGES,
    SELECTED_PAGES,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_assembly_readiness_001_020.py"
REPORT = OUT_ROOT / "assembly_readiness_001_020_report.json"
SUMMARY = OUT_ROOT / "assembly_readiness_001_020_summary.md"
MANIFEST = OUT_ROOT / "assembly_readiness_001_020_manifest.md"
SELECTED_MANIFEST = OUT_ROOT / "assembly_manifest" / "selected_pages_manifest.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("assembly-readiness output has not been generated yet")


def test_assembly_readiness_is_fail_closed():
    no_args = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_args.returncode != 0
    assert "--execute" in no_args.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "wrong", "--decision", "jr"],
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


def test_assembly_readiness_refuses_overwrite():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; overwrite refusal is covered by generated-output state")
    OUT_ROOT.mkdir(parents=True)
    try:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTHORIZATION_ID, "--decision", "jr"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
    finally:
        OUT_ROOT.rmdir()
    assert result.returncode != 0
    assert "refusing to overwrite existing output directory" in result.stderr


def test_assembly_readiness_pre_output_scope_and_pins():
    verified_inputs, mf_report, selections = verify_inputs()
    selected = [item for item in selections if item["selection_status"] == "selected_static_evidence_only"]

    assert mf_report["production_ready"] is False
    assert mf_report["all_pages_first_pass_success"] is False
    assert [item["page"] for item in selected] == SELECTED_PAGES
    assert [item["page"] for item in selections if item["selector_decision"] == "not_run_ineligible"] == NOT_RUN_INELIGIBLE
    assert [item["page"] for item in selections if item["selector_decision"] == "parked_candidate_policy"] == PARKED_PAGES
    assert sorted(verified_inputs) == [
        "C01TEMF012016020-G1-VIRAL-001.page_012_entry",
        "C01TEMF012016020-G1-VIRAL-001.page_016_entry",
        "C01TEMF012016020-G1-VIRAL-001.page_020_entry",
        "C01TEMF012016020-G1-VIRAL-001.report",
        "C01TEMF012016020-G1-VIRAL-001.selector_v3",
        "C01TEMF012016020-G1-VIRAL-001.summary",
    ]
    for item in selected:
        assert item["selected_output_hashes"] == EXPECTED_SELECTED_HASHES[item["page"]]


def test_assembly_readiness_report_is_manifest_only_and_production_blocked():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "assembly_readiness_manifest_only_production_blocked"
    assert report["selected_pages"] == SELECTED_PAGES
    assert report["not_run_ineligible_pages"] == NOT_RUN_INELIGIBLE
    assert report["parked_pages"] == PARKED_PAGES
    assert report["manifest_only"] is True
    assert report["hash_reference_only"] is True
    assert report["candidate_text_copied"] is False
    assert report["failed_or_superseded_candidates_in_manifest"] is False
    assert report["production_ready"] is False
    assert report["all_pages_first_pass_success"] is False
    assert report["production_assembly_created"] is False
    assert report["clean_production_output_folder_created"] is False
    assert report["runtime_selector_integration"] is False
    assert report["page_021_plus_included"] is False


def test_assembly_manifest_contains_only_selected_hash_references():
    require_outputs()
    selected_manifest = read_json(SELECTED_MANIFEST)

    assert [item["page"] for item in selected_manifest] == SELECTED_PAGES
    for item in selected_manifest:
        assert item["status"] == "selected_static_evidence_manifest_only"
        assert item["selected_output_hashes"] == EXPECTED_SELECTED_HASHES[item["page"]]
        assert item["candidate_text_copied"] is False
        assert item["candidate_text_inline"] is False
        assert item["production_output_path"] is None
        assert item["production_output_created"] is False
    assert {item["page"] for item in selected_manifest}.isdisjoint(NOT_RUN_INELIGIBLE + PARKED_PAGES)


def test_assembly_readiness_preserves_acceptance_and_mutation_boundaries():
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
        "page_001_020_runtime_loop_created",
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
    assert report["reference_risk_pages"] == ["012", "013", "015", "016", "017", "018", "020"]
    assert "not accepted source text" in report["reference_risk_note"]
    assert "`manifest_only=true`" in summary
    assert "`production_assembly_created=false`" in summary
    assert "`runtime_selector_integration=false`" in summary


def test_assembly_readiness_manifest_covers_required_outputs():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`assembly_manifest/selected_pages_manifest.json`" in manifest
    assert "`assembly_readiness_001_020_report.json`" in manifest
    assert "`assembly_readiness_001_020_summary.md`" in manifest
    assert "no copied candidate text" in manifest
    assert "no production assembly" in manifest
