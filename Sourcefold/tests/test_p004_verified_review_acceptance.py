import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "accept_p004_verified_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001"
REPORT = OUT_ROOT / "p004_verified_review_acceptance_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_p004_acceptance_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004-HUMAN-VERIFY-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-P004-QA-SOURCE-ACCEPTANCE-001" in wrong_auth.stderr


def test_p004_acceptance_consumes_verified_draft_and_accepts_two_records_only():
    report = read_json(REPORT)

    assert report["package_id"] == "P004A-G1-VIRAL-004"
    assert report["input_verification_id"] == "SRCRV-G1-VIRAL-004"
    assert report["qa"]["qa_id"] == "SRCRQ-G1-VIRAL-004"
    assert report["qa"]["status"] == "passed"
    assert report["source_acceptance"]["source_acceptance_id"] == "SRSA-G1-VIRAL-004"
    assert len(report["source_acceptance"]["accepted_records"]) == 2
    assert report["rollup"]["prior_accepted_records"] == 11
    assert report["rollup"]["total_accepted_records"] == 13


def test_p004_acceptance_keeps_broad_scope_blocked():
    report = read_json(REPORT)

    assert report["page_complete_acceptance"] is False
    assert report["whole_gate_1_acceptance"] is False
    assert report["fixture_admission"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["push_authorized"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False


def test_p004_acceptance_consumes_predecessor_crop_guardrail_evidence():
    report = read_json(REPORT)
    guardrail = report["crop_guardrail"]

    assert guardrail["guardrail_id"] == "SRCG-G1-VIRAL-004"
    assert guardrail["status"] == "passed"
    assert guardrail["global_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert guardrail["policy_version"] == guardrail["predecessor_guardrail"]["policy_version"]
    assert guardrail["context_region_policy"]["status"] == "context_only_not_peer_crop_record"
    validated = {item["region_id"]: item["box_px"] for item in guardrail["predecessor_guardrail"]["validated_boxes"]}
    accepted = report["source_acceptance"]["accepted_records"]
    assert all(validated[record["review_id"]] == record["review_box_px"] for record in accepted)


def test_p004_acceptance_binds_verified_records_to_review_packet_hashes():
    report = read_json(REPORT)
    accepted = report["source_acceptance"]["accepted_records"]

    assert accepted[0]["verified_record_id"] == "SRCRV-G1-VIRAL-004-R01"
    assert accepted[0]["review_id"] == "SRCR-G1-VIRAL-004-R01"
    assert accepted[0]["accepted_text_sha256"] == "86F56FE8221F029DB2C9755CC998669A7D873C32BFA83BC9431BAFE0BB814400"
    assert accepted[1]["verified_record_id"] == "SRCRV-G1-VIRAL-004-R02"
    assert accepted[1]["review_id"] == "SRCR-G1-VIRAL-004-R02"
    assert accepted[1]["accepted_text_sha256"] == "430246F1327C4554B2D16C8D5BFE11704EE515B4B5C3DB298A7B3492716E14A2"
    assert {record["source_region_id"] for record in accepted} == {
        "PRM-G1-VIRAL-001-P004-R02",
        "PRM-G1-VIRAL-001-P004-R03",
    }
