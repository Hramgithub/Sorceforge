from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_first_pass_runtime_selector_run_001_020 import (  # noqa: E402
    AUTHORIZATION_ID,
    BRIDGE_PAGES,
    HUMAN_DECISION,
    LANE_ID,
    NEGATIVE_CAPABILITIES,
    OUT_ROOT,
    REQUESTED_PAGES,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_first_pass_runtime_selector_run_001_020.py"
REPORT = OUT_ROOT / "first_pass_runtime_selector_run_001_020_report.json"
SUMMARY = OUT_ROOT / "first_pass_runtime_selector_run_001_020_summary.md"
MANIFEST = OUT_ROOT / "first_pass_runtime_selector_run_001_020_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("first-pass runtime selector run output has not been generated yet")


def test_first_pass_runtime_selector_run_is_fail_closed():
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


def test_first_pass_runtime_selector_run_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, auth_report, selector_v4 = verify_inputs()

    assert auth_report["fresh_first_pass_runtime_selector_route_authorized"] is True
    assert auth_report["requested_pages"] == REQUESTED_PAGES
    assert [item["page"] for item in selector_v4] == REQUESTED_PAGES
    assert sorted(verified) == [
        "C01TEASM020-G1-VIRAL-001.selected_pages_manifest",
        "C01TEAUTH020-G1-VIRAL-001.manifest",
        "C01TEAUTH020-G1-VIRAL-001.report",
        "C01TEBRIDGE020-G1-VIRAL-001.bridge_entries",
        "C01TEBRIDGE020-G1-VIRAL-001.selector_v4",
        "C01TEFPSAUTH020-G1-VIRAL-001.manifest",
        "C01TEFPSAUTH020-G1-VIRAL-001.report",
        "C01TEFPSAUTH020-G1-VIRAL-001.summary",
    ]


def test_first_pass_runtime_selector_run_report_materializes_all_pages_but_not_all_fresh_ocr():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "first_pass_runtime_selector_output_surface_materialized_with_bridge_lineage"
    assert report["requested_pages"] == REQUESTED_PAGES
    assert report["materialized_pages"] == REQUESTED_PAGES
    assert report["all_pages_materialized"] is True
    assert report["runtime_execution_performed"] is True
    assert report["runtime_output_surface_created"] is True
    assert report["fresh_ocr_runtime_pages"] == ["009", "010", "011", "012", "013", "015", "016", "017", "018", "020"]
    assert report["fresh_ocr_execution_pages"] == ["009", "010", "011", "015"]
    assert report["bridge_lineage_pages"] == sorted(BRIDGE_PAGES)
    assert report["all_pages_fresh_ocr_success"] is False
    assert report["production_ready"] is False
    assert report["production_assembly_authorized"] is False


def test_first_pass_runtime_selector_run_outputs_are_bounded():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert len(report["page_results"]) == 20
    for item in report["page_results"]:
        output_path = ROOT / item["output_path"]
        assert output_path.exists()
        assert item["output_sha256"]
        if item["page"] in BRIDGE_PAGES:
            assert item["bridge_lineage"] is True
            assert item["fresh_ocr_execution"] is False
        else:
            assert item["selected_candidate_text_hash_matched"] is True
    assert "Bridge lineage pages are not counted as fresh OCR" in summary
    assert "`page_021_plus_included=false`" in summary


def test_first_pass_runtime_selector_run_preserves_negative_boundaries():
    require_outputs()
    report = read_json(REPORT)

    false_flags = [
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "fixture_admission_performed",
        "whole_gate_1_acceptance_performed",
        "acceptance_performed",
        "page_021_plus_included",
        "push_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert set(report["negative_capability_matrix"]) == set(NEGATIVE_CAPABILITIES)
    for capability, value in report["negative_capability_matrix"].items():
        assert value is False, capability


def test_first_pass_runtime_selector_run_manifest_covers_report_summary_and_pages():
    require_outputs()
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "`first_pass_runtime_selector_run_001_020_report.json`" in manifest
    assert "`first_pass_runtime_selector_run_001_020_summary.md`" in manifest
    assert "`pages/page_001_bridge_lineage.md`" in manifest
    assert "`pages/page_020_selected_text.md`" in manifest


def test_first_pass_runtime_selector_run_output_tree_is_exactly_bounded():
    require_outputs()
    report = read_json(REPORT)
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())

    page_outputs = [path for path in output_files if path.startswith("pages/")]
    assert len(page_outputs) == 20
    assert not any("021" in path or "page_21" in path for path in output_files)
    assert not any("accepted" in path or "page_status" in path or "source" in path or "raw" in path for path in output_files)
    assert sorted(item["output_path"] for item in report["page_results"]) == sorted(
        (OUT_ROOT / path).relative_to(ROOT).as_posix() for path in page_outputs
    )
