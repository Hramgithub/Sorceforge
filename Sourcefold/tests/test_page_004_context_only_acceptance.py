import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_page_004_context_only.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_004_context_only_confirmation_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_004_context_only_confirmation_report.json"
RECORD = OUT_ROOT / "page_004_context_only_confirmation_record.md"
SUMMARY = OUT_ROOT / "page_004_context_only_confirmation_summary.md"
MANIFEST = OUT_ROOT / "page_004_context_only_confirmation_manifest.md"
AUTH = "BA-G1-VIRAL-PAGE-004-CONTEXT-ONLY-CONFIRM-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_004_context_only_confirmation_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT), "--page", "004"], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P004-001", "--page", "004"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_004_context_only_confirmation_allows_only_page_004():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTH, "--page", "003"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "profile exists only for page 004" in result.stderr


def test_page_004_context_only_confirmation_records_explicit_decision():
    report = read_json(REPORT)

    assert report["package_id"] == "P004COD-G1-VIRAL-001"
    assert report["authorization_id"] == AUTH
    assert report["status"] == "page_004_context_only_confirmed"
    assert report["scope"] == "page_004_context_region_decision_only_no_page_complete_acceptance"
    assert report["input_packages"] == ["P004CDP-G1-VIRAL-001"]
    assert report["human_decision"]["telegram_message_id"] == "758"
    assert report["human_decision"]["decision"] == "page 004 context-only ok"


def test_page_004_context_region_is_confirmed_without_page_complete_acceptance():
    report = read_json(REPORT)
    confirmation = report["context_only_confirmation"]

    assert confirmation["confirmation_id"] == "P004-CONTEXT-ONLY-CONFIRMATION-001"
    assert confirmation["accepted"] is True
    assert confirmation["context_region_id"] == "PRM-G1-VIRAL-001-P004-R01"
    assert confirmation["confirmed_status"] == "context_only_not_peer_crop_record"
    assert confirmation["body_only_structure_label"] == "text_body"
    assert confirmation["predecessor_source_review_packet_mutated"] is False
    assert [record["source_region_id"] for record in confirmation["accepted_peer_records"]] == [
        "PRM-G1-VIRAL-001-P004-R02",
        "PRM-G1-VIRAL-001-P004-R03",
    ]


def test_page_004_context_only_confirmation_guardrails_stay_false():
    guardrails = read_json(REPORT)["guardrails"]

    assert guardrails["page_complete_acceptance_created"] is False
    assert guardrails["accepted_pages_as_complete"] == []
    assert guardrails["whole_gate_1_acceptance_created"] is False
    assert guardrails["fixture_admission"] is False
    assert guardrails["source_acceptance_created_or_mutated"] is False
    assert guardrails["ocr_executed"] is False
    assert guardrails["pdf_opened_or_parsed"] is False
    assert guardrails["pdf_text_layer_used"] is False
    assert guardrails["render_executed"] is False
    assert guardrails["raw_artifacts_modified"] is False
    assert guardrails["translation_authorized"] is False
    assert guardrails["proofreading_authorized"] is False
    assert guardrails["renderer_profile_acceptance"] is False
    assert guardrails["implementation_authorized"] is False
    assert guardrails["push_authorized"] is False


def test_page_004_context_only_confirmation_outputs_are_human_readable():
    record = RECORD.read_text(encoding="utf-8-sig")
    summary = SUMMARY.read_text(encoding="utf-8-sig")
    manifest = MANIFEST.read_text(encoding="utf-8-sig")

    assert "PRM-G1-VIRAL-001-P004-R01" in record
    assert "page 004 context-only ok" in record
    assert "Body-only human-facing structure label is `text_body`, not `none`." in record
    assert "Page 004 is not accepted as complete." in summary
    assert "page_004_context_only_confirmation_report.json" in manifest
