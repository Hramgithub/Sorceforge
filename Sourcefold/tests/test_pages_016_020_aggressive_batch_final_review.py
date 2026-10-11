import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_pages_016_020_aggressive_batch_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
RUN_AUTH = "BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001"
DECISION = "p016 corrected semantic map ok; p018 corrected semantic map ok; p016-p020 aggressive batch ok"
PAGES = ("016", "017", "018", "019", "020")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def report_path(page: str) -> Path:
    return TRIAL_ROOT / f"page_{page}_aggressive_batch_final_review_G1_VIRAL_001" / f"page_{page}_aggressive_batch_final_review_report.json"


def test_pages_016_020_aggressive_batch_final_review_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_decision = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--run-authorization-id",
            RUN_AUTH,
            "--decision",
            "p016-p020 ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert DECISION in wrong_decision.stderr


def test_pages_016_020_aggressive_batch_final_review_records_only_final_scope():
    for page in PAGES:
        report = read_json(report_path(page))

        assert report["review_id"] == f"P{page}BATCHREV-G1-VIRAL-001"
        assert report["run_authorization_id"] == RUN_AUTH
        assert report["authorization_id"] == f"BA-G1-VIRAL-PAGE-{page}-AGGRESSIVE-BATCH-001"
        assert report["human_decision"] == DECISION
        assert report["batch_decision"] == "p016-p020 aggressive batch ok"
        assert report["status"] == f"page_{page}_aggressive_batch_final_human_review_accepted"
        assert report["human_review_scope"] == f"final_bundle_and_post_p{page}_status_only"
        assert report["internal_stage_human_review_state"] == "human_review_skipped_by_explicit_authorization"
        assert report["accepted_page_complete_pages_current"][-1] == page

        page_num = int(page)
        expected_remaining = [f"{candidate:03d}" for candidate in range(page_num + 1, 21)]
        assert report["remaining_page_complete_pages_unstarted"] == expected_remaining

        serialized = json.dumps(report)
        assert f"p{page} triage ok" not in serialized
        assert f"p{page} text ok" not in serialized
        assert f"p{page} semantic map ok" not in serialized
        assert "Bogdan approved" not in serialized


def test_pages_016_020_aggressive_batch_final_review_records_correction_decisions():
    report = read_json(report_path("020"))

    assert report["corrected_semantic_map_decisions"] == {
        "016": "p016 corrected semantic map ok",
        "018": "p018 corrected semantic map ok",
    }
    assert report["recommended_next_candidate"] is None
    assert report["continuation"]["page_021_processed"] is False


def test_pages_016_020_aggressive_batch_final_review_keeps_broad_guardrails_false():
    for page in PAGES:
        report = read_json(report_path(page))

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
            "page_021_plus_processing",
        ]:
            assert report["guardrails"][key] is False, key
