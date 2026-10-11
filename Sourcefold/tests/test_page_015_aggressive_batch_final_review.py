import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_page_015_aggressive_batch_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH = "BA-G1-VIRAL-PAGE-015-AGGRESSIVE-BATCH-001"
DECISION = "p015 aggressive batch ok"
REPORT = TRIAL_ROOT / "page_015_aggressive_batch_final_review_G1_VIRAL_001" / "page_015_aggressive_batch_final_review_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_015_aggressive_batch_final_review_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_decision = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTH, "--decision", "p015 triage ok"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert DECISION in wrong_decision.stderr


def test_page_015_aggressive_batch_final_review_records_only_final_scope():
    report = read_json(REPORT)

    assert report["decision"] == DECISION
    assert report["status"] == "page_015_aggressive_batch_final_human_review_accepted"
    assert report["human_review_scope"] == "final_bundle_and_post_p015_status_only"
    assert report["internal_stage_human_review_state"] == "human_review_skipped_by_explicit_authorization"
    assert report["accepted_page_complete_pages_current"][-1] == "015"
    assert report["remaining_page_complete_pages_unstarted"] == ["016", "017", "018", "019", "020"]
    assert report["recommended_next_candidate"] == "page_016_triage_readiness_not_authorized"
    assert report["continuation"]["history_continues_to_page"] == "016"
    assert report["continuation"]["page_016_processed"] is False

    serialized = json.dumps(report)
    assert "p015 triage ok" not in serialized
    assert "p015 text ok" not in serialized
    assert "p015 semantic map ok" not in serialized
    assert "Bogdan approved" not in serialized


def test_page_015_aggressive_batch_final_review_keeps_broad_guardrails_false():
    report = read_json(REPORT)

    for key in [
        "whole_gate_1_acceptance",
        "fixture_admission",
        "source_acceptance_mutation",
        "ocr_execution",
        "render_execution",
        "pdf_parsing_or_text_layer_extraction",
        "raw_mutation",
        "translation",
        "proofreading",
        "renderer_profile_acceptance",
        "implementation",
        "push",
        "page_016_plus_processing",
    ]:
        assert report["guardrails"][key] is False, key
