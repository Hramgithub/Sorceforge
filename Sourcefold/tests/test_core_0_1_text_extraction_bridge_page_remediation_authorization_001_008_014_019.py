from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.build_core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019 import (  # noqa: E402
    AUTHORIZATION_ID,
    FULL_PAGE_OCR_CANDIDATE_PAGES,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    REQUESTED_PAGES,
    SOURCE_ASSET_RECOVERY_PAGES,
    TEXT_EVIDENCE_SMOKE_PAGES,
    VISUAL_ONLY_PAGES,
    verify_inputs,
)


SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_bridge_page_remediation_authorization_001_008_014_019.py"
REPORT = OUT_ROOT / "bridge_page_remediation_authorization_001_008_014_019_report.json"
SUMMARY = OUT_ROOT / "bridge_page_remediation_authorization_001_008_014_019_summary.md"
MANIFEST = OUT_ROOT / "bridge_page_remediation_authorization_001_008_014_019_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("bridge page remediation authorization output has not been generated yet")


def test_bridge_page_remediation_authorization_is_fail_closed():
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


def test_bridge_page_remediation_authorization_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, audit = verify_inputs()

    assert sorted(verified) == [
        "C01TEBRIDGEAUD020-G1-VIRAL-001.manifest",
        "C01TEBRIDGEAUD020-G1-VIRAL-001.report",
        "C01TEBRIDGEAUD020-G1-VIRAL-001.summary",
    ]
    assert audit["audit_pages"] == REQUESTED_PAGES
    assert audit["visual_only_no_text_rule_pages"] == VISUAL_ONLY_PAGES
    assert audit["needs_source_asset_recovery_pages"] == SOURCE_ASSET_RECOVERY_PAGES


def test_bridge_page_remediation_authorization_report_contract():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["status"] == "bridge_page_remediation_authorization_recorded_report_only"
    assert report["base_commit"] == "79dffc1e"
    assert report["requested_pages"] == REQUESTED_PAGES
    assert report["visual_only_no_text_rule_pages"] == VISUAL_ONLY_PAGES
    assert report["full_page_region_candidate_pages"] == FULL_PAGE_OCR_CANDIDATE_PAGES
    assert report["text_evidence_smoke_non_promotable_pages"] == TEXT_EVIDENCE_SMOKE_PAGES
    assert report["needs_source_asset_recovery_pages"] == SOURCE_ASSET_RECOVERY_PAGES
    assert report["page_002_blocker"] == "needs_source_asset_recovery"
    assert report["remediation_route_authorized_for_future_runner"] is True
    assert report["this_lane_report_only"] is True
    assert report["ocr_execution_performed"] is False
    assert report["page_001_ocr_execution_authorized"] is False
    assert report["page_001_fresh_ocr_success_authorized"] is False
    assert report["page_002_remains_blocked"] is True
    assert report["verified_inputs"] == {
        "C01TEBRIDGEAUD020-G1-VIRAL-001.report": {
            "path": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001/bridge_page_audit_001_008_014_019_report.json",
            "sha256": "25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02",
        },
        "C01TEBRIDGEAUD020-G1-VIRAL-001.summary": {
            "path": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001/bridge_page_audit_001_008_014_019_summary.md",
            "sha256": "744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639",
        },
        "C01TEBRIDGEAUD020-G1-VIRAL-001.manifest": {
            "path": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001/bridge_page_audit_001_008_014_019_manifest.md",
            "sha256": "D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738",
        },
    }


def test_bridge_page_remediation_authorization_surface_policy_split():
    require_outputs()
    report = read_json(REPORT)
    by_page = {item["page"]: item for item in report["surface_validations"]}

    assert sorted(by_page) == sorted(FULL_PAGE_OCR_CANDIDATE_PAGES + TEXT_EVIDENCE_SMOKE_PAGES)
    for page in FULL_PAGE_OCR_CANDIDATE_PAGES:
        surface = by_page[page]["surface"]
        validation = by_page[page]["validation"]
        assert surface["surface_class"] == "full_page_region"
        assert surface["allowed_purpose"] == "candidate_policy"
        assert surface["ocr_allowed"] is True
        assert validation["status"] == "passed"
        assert not validation["findings"]
    for page in TEXT_EVIDENCE_SMOKE_PAGES:
        surface = by_page[page]["surface"]
        validation = by_page[page]["validation"]
        assert surface["surface_class"] == "text_evidence_crop"
        assert surface["allowed_purpose"] == "smoke_non_promotable"
        assert surface["ocr_allowed"] is False
        assert validation["status"] == "passed"
        assert not validation["findings"]


def test_bridge_page_remediation_authorization_boundaries_and_outputs():
    require_outputs()
    report = read_json(REPORT)
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    false_flags = [
        "ocr_execution_performed",
        "runtime_execution_performed",
        "render_execution_performed",
        "pdf_parsing_or_text_layer_extraction_performed",
        "production_ready",
        "production_assembly_authorized",
        "acceptance_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "fixture_admission_performed",
        "clean_candidate_output_folder_created",
        "clean_production_output_folder_created",
        "page_021_plus_included",
        "push_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag
    assert "does not execute OCR" in summary
    assert "Page `002` remains blocked" in summary
    assert "no OCR execution" in manifest
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())
    assert output_files == [
        "bridge_page_remediation_authorization_001_008_014_019_manifest.md",
        "bridge_page_remediation_authorization_001_008_014_019_report.json",
        "bridge_page_remediation_authorization_001_008_014_019_summary.md",
    ]
    assert not any("021" in path or "page_021" in path for path in output_files)
