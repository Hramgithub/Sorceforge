import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_p003_verified_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001"
REPORT = OUT_ROOT / "p003_verified_review_acceptance_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_p003_acceptance_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-P003-HUMAN-REVIEW-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-P003-QA-SOURCE-ACCEPTANCE-001" in wrong_auth.stderr


def test_p003_acceptance_consumes_verified_draft_and_accepts_two_records_only():
    report = read_json(REPORT)

    assert report["package_id"] == "P003A-G1-VIRAL-003"
    assert report["qa"]["qa_id"] == "SRCRQ-G1-VIRAL-003"
    assert report["qa"]["status"] == "passed"
    assert report["source_acceptance"]["source_acceptance_id"] == "SRSA-G1-VIRAL-003"
    assert len(report["source_acceptance"]["accepted_records"]) == 2
    assert report["rollup"]["total_accepted_records"] == 11


def test_p003_acceptance_keeps_broad_scope_blocked():
    report = read_json(REPORT)

    assert report["page_complete_acceptance"] is False
    assert report["whole_gate_1_acceptance"] is False
    assert report["fixture_admission"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["push_authorized"] is False


def test_p003_crop_guardrail_blocks_old_tight_boxes_and_requires_padded_boxes():
    report = read_json(REPORT)
    guardrail = report["crop_guardrail"]

    assert guardrail["guardrail_id"] == "SRCG-G1-VIRAL-003"
    assert guardrail["status"] == "passed"
    assert guardrail["global_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert guardrail["policy_version"] == guardrail["predecessor_guardrail"]["policy_version"]
    assert [270, 860, 2050, 2240] in [item["box_px"] for item in guardrail["accepted_validated_boxes"]]
    assert "overlap another crop" in guardrail["debt"]


def test_p003_acceptance_consumes_predecessor_crop_guardrail_evidence():
    report = read_json(REPORT)
    guardrail = report["crop_guardrail"]["predecessor_guardrail"]

    assert guardrail["status"] == "passed"
    assert guardrail["validated_at_stage"] == "SRCR-G1-VIRAL-003.review_crop_generation"
    accepted = report["source_acceptance"]["accepted_records"]
    validated = {item["region_id"]: item["box_px"] for item in guardrail["validated_boxes"]}
    assert all(validated[record["review_id"]] for record in accepted)
