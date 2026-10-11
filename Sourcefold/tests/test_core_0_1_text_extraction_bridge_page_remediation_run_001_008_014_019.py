from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from scripts.run_core_0_1_text_extraction_bridge_page_remediation_001_008_014_019 import (  # noqa: E402
    AUTHORIZATION_ID,
    AUDIT_LANE_ID,
    FULL_PAGE_OCR_PAGES,
    HUMAN_DECISION,
    LANE_ID,
    OUT_ROOT,
    REQUESTED_PAGES,
    SOURCE_ASSET_RECOVERY_PAGES,
    TEXT_EVIDENCE_SMOKE_PAGES,
    VISUAL_ONLY_PAGES,
    verify_authorization,
)


SCRIPT = ROOT / "scripts" / "run_core_0_1_text_extraction_bridge_page_remediation_001_008_014_019.py"
REPORT = OUT_ROOT / "bridge_page_remediation_run_001_008_014_019_report.json"
SUMMARY = OUT_ROOT / "bridge_page_remediation_run_001_008_014_019_summary.md"
MANIFEST = OUT_ROOT / "bridge_page_remediation_run_001_008_014_019_manifest.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def require_outputs() -> None:
    if not REPORT.exists():
        raise pytest.skip("bridge page remediation run output has not been generated yet")


def test_bridge_page_remediation_run_is_fail_closed():
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


def test_bridge_page_remediation_run_pre_output_pins_and_scope():
    if OUT_ROOT.exists():
        raise pytest.skip("real output already exists; pre-output pins were checked before generation")
    verified, auth_report, audit_report = verify_authorization()

    assert sorted(verified) == [
        "C01TEBRIDGEAUD020-G1-VIRAL-001.manifest",
        "C01TEBRIDGEAUD020-G1-VIRAL-001.report",
        "C01TEBRIDGEAUD020-G1-VIRAL-001.summary",
        "C01TEBRIDGEREMAUTH020-G1-VIRAL-001.manifest",
        "C01TEBRIDGEREMAUTH020-G1-VIRAL-001.report",
        "C01TEBRIDGEREMAUTH020-G1-VIRAL-001.summary",
    ]
    assert auth_report["requested_pages"] == REQUESTED_PAGES
    assert audit_report["audit_pages"] == REQUESTED_PAGES
    assert auth_report["full_page_region_candidate_pages"] == FULL_PAGE_OCR_PAGES
    assert auth_report["text_evidence_smoke_non_promotable_pages"] == TEXT_EVIDENCE_SMOKE_PAGES
    assert auth_report["visual_only_no_text_rule_pages"] == VISUAL_ONLY_PAGES
    assert auth_report["needs_source_asset_recovery_pages"] == SOURCE_ASSET_RECOVERY_PAGES


def test_bridge_page_remediation_run_no_latest_recompute_or_unpinned_scan():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = ["glob(f\"page_complete_review_p{page}", "max(", "latest", "rglob(\"*page_complete"]
    for needle in forbidden:
        assert needle not in source
    assert "AUTH_INPUT_HASHES" in source
    assert "AUDIT_INPUT_HASHES" in source


def test_bridge_page_remediation_run_report_contract_and_boundaries():
    require_outputs()
    report = read_json(REPORT)

    assert report["lane_id"] == LANE_ID
    assert report["authorization_id"] == AUTHORIZATION_ID
    assert report["status"] == "bridge_page_remediation_run_materialized_candidate_only"
    assert report["base_commit"] in {"c99006fd"} or len(report["base_commit"]) >= 8
    assert report["input_lane_id"] == "C01TEBRIDGEREMAUTH020-G1-VIRAL-001"
    assert report["audit_lane_id"] == AUDIT_LANE_ID
    assert report["requested_pages"] == REQUESTED_PAGES
    assert report["visual_only_no_text_rule_pages"] == VISUAL_ONLY_PAGES
    assert report["needs_source_asset_recovery_pages"] == SOURCE_ASSET_RECOVERY_PAGES
    assert report["full_page_region_ocr_pages"] == FULL_PAGE_OCR_PAGES
    assert report["text_evidence_smoke_non_promotable_pages"] == TEXT_EVIDENCE_SMOKE_PAGES

    false_flags = [
        "all_requested_pages_resolved_as_fresh_first_pass",
        "production_ready",
        "production_assembly_authorized",
        "production_assembly_created",
        "acceptance_performed",
        "accepted_text_mutation_performed",
        "semantic_text_mutation_performed",
        "page_status_mutation_performed",
        "source_or_raw_mutation_performed",
        "persisted_raw_ocr_output_created",
        "prepared_temp_artifact_created",
        "fixture_admission_performed",
        "clean_production_output_folder_created",
        "page_021_plus_included",
        "promotion_performed",
        "push_performed",
        "downstream_execution_performed",
    ]
    for flag in false_flags:
        assert report[flag] is False, flag


def test_bridge_page_remediation_run_surface_split_and_014_019_no_tesseract():
    require_outputs()
    report = read_json(REPORT)
    by_page = {item["page"]: item for item in report["page_entries"]}

    assert sorted(by_page) == REQUESTED_PAGES
    assert by_page["001"]["route_family"] == "visual_only_no_text_rule"
    assert by_page["001"]["ocr_execution_performed"] is False
    assert by_page["001"]["fresh_ocr_success"] is False
    assert by_page["002"]["route_family"] == "needs_source_asset_recovery"
    assert by_page["002"]["ocr_execution_performed"] is False

    for page in FULL_PAGE_OCR_PAGES:
        item = by_page[page]
        assert item["route_family"] == "full_page_region_candidate_policy"
        assert item["ocr_execution_performed"] is True
        assert item["tesseract_invoked_for_page"] is True
        assert item["candidate_hash_sealed_before_reference_scoring"] is True
        assert item["reference"]["reference_status"] in {
            "scorer_only_after_candidate_hash_sealed",
            "missing",
            "not_loaded_no_pinned_reference_for_remediation_run",
        }

    for page in TEXT_EVIDENCE_SMOKE_PAGES:
        item = by_page[page]
        assert item["route_family"] == "text_evidence_smoke_non_promotable"
        assert item["policy_route"]["route_decision"] == "smoke_non_promotable"
        assert item["ocr_execution_performed"] is False
        assert item["tesseract_invoked_for_page"] is False
        assert item["fresh_ocr_candidate_created"] is False
        assert item["fresh_ocr_success"] is False


def test_bridge_page_remediation_run_output_tree_is_clean_candidate_only():
    require_outputs()
    output_files = sorted(path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file())

    assert "bridge_page_remediation_run_001_008_014_019_report.json" in output_files
    assert "bridge_page_remediation_run_001_008_014_019_summary.md" in output_files
    assert "bridge_page_remediation_run_001_008_014_019_manifest.md" in output_files
    assert not any("021" in path or "page_021" in path for path in output_files)
    assert not any(path.startswith(("raw_ocr/", "prepared", "source/", "accepted/", "production/")) for path in output_files)
    assert all(
        path.startswith(
            (
                "candidate_texts/",
                "ocr_metadata/",
                "visual_only/",
                "blockers/",
                "smoke_non_promotable/",
                "bridge_page_remediation_run_001_008_014_019_",
            )
        )
        for path in output_files
    )

    manifest = MANIFEST.read_text(encoding="utf-8-sig")
    for path in output_files:
        if path != "bridge_page_remediation_run_001_008_014_019_manifest.md":
            assert path in manifest


def test_bridge_page_remediation_run_summary_preserves_non_production_wording():
    require_outputs()
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "candidate-only remediation evidence" in summary
    assert "Text-evidence smoke/non-promotable pages, no Tesseract: `014`, `019`" in summary
    assert "no production assembly" in summary
    assert "page `021+`" in summary
