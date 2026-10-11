import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_page_008_complete.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "page_complete_acceptance_p008_G1_VIRAL_001"
REPORT = OUT_ROOT / "page_complete_acceptance_report.json"
RECORD = OUT_ROOT / "page_complete_acceptance_record.md"
AUTH = "BA-G1-VIRAL-PAGE-COMPLETE-ACCEPT-P008-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_008_complete_acceptance_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT), "--page", "008"], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-COMPLETE-REVIEW-P008-001", "--page", "008"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_page_008_complete_acceptance_allows_only_page_008():
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTH, "--page", "009"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "profile exists only for page 008" in result.stderr


def test_page_008_complete_acceptance_records_explicit_decision():
    report = read_json(REPORT)

    assert report["package_id"] == "P008PCA-G1-VIRAL-001"
    assert report["authorization_id"] == AUTH
    assert report["status"] == "page_008_complete_accepted"
    assert report["scope"] == "page_008_complete_acceptance_only"
    assert report["input_packages"] == ["PCRP-G1-VIRAL-P008-001"]
    assert report["human_decision"]["telegram_message_id"] == "1178"
    assert report["human_decision"]["decision"] == "page 008 complete ok"


def test_page_008_is_the_only_page_accepted_as_complete():
    report = read_json(REPORT)
    acceptance = report["page_complete_acceptance"]

    assert acceptance["acceptance_id"] == "P008-PAGE-COMPLETE-ACCEPTANCE-001"
    assert acceptance["accepted"] is True
    assert acceptance["accepted_page"] == "008"
    assert acceptance["accepted_pages_as_complete"] == ["008"]
    assert acceptance["reviewed_blocks"] == 7
    assert acceptance["ready_blocks"] == 7
    assert acceptance["reading_order"] == [
        "marco_proudfoot_body_page_008_continuation",
        "marco_proudfoot_appearance_gear_box",
        "corrina_trench_portrait_anchor",
        "corrina_trench_body_left_column",
        "corrina_trench_body_right_column",
        "corrina_trench_appearance_gear_box",
        "crystal_object_art_anchor",
    ]
    assert acceptance["blockers"] == []
    assert acceptance["open_questions"] == []


def test_page_008_complete_acceptance_guardrails_stay_false():
    report = read_json(REPORT)
    guardrails = report["guardrails"]

    assert guardrails["only_page_008_accepted_as_complete"] is True
    assert guardrails["accepted_pages_as_complete"] == ["008"]
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


def test_acceptance_record_is_human_readable_and_limited():
    record = RECORD.read_text(encoding="utf-8-sig")

    assert "Decision: Page 008 is accepted as complete." in record
    assert "Only Page 008 is accepted as complete." in record
    assert "Whole Gate 1 is not accepted." in record
    assert "No fixture admission is created." in record
    assert "No source acceptance is created or mutated." in record
