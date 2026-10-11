import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_p002_completion_and_next_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
REPORT = OUT_ROOT / "p002_completion_and_next_review_report.json"
NEXT_PACKET = OUT_ROOT / "next_review_packet_for_bogdan.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_p002_completion_chain_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-QA-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-P002-QA-STRUCTURE-SOURCE-AND-NEXT-REVIEW-001" in wrong_auth.stderr


def test_p002_completion_chain_records_qa_structure_acceptance_and_rollup():
    report = read_json(REPORT)

    assert report["package_id"] == "P002C-G1-VIRAL-002"
    assert report["qa"]["qa_id"] == "SRADQ-G1-VIRAL-002"
    assert report["qa"]["status"] == "passed"
    assert report["structure_semantics"]["structure_id"] == "SRSS-G1-VIRAL-002"
    assert report["structure_semantics"]["special_thanks_heading_level"] == "none"
    assert report["structure_qa"]["structure_qa_id"] == "SRSSQ-G1-VIRAL-002"
    assert report["source_acceptance_record"]["source_acceptance_id"] == "SRSA-G1-VIRAL-002"
    assert report["source_acceptance_record"]["accepted_records"] == 2
    assert report["rollup"]["total_accepted_records"] == 9


def test_p002_completion_chain_keeps_broad_scope_blocked():
    report = read_json(REPORT)

    assert report["source_acceptance"] is True
    assert report["accepted_records"] == 2
    assert report["page_complete_acceptance"] is False
    assert report["whole_gate_1_acceptance"] is False
    assert report["fixture_admission"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["push_authorized"] is False


def test_p002_completion_structure_has_heading_and_presentation_fields():
    report = read_json(REPORT)
    spans = [span for record in report["structure_semantics"]["records"] for span in record["spans"]]

    credits = next(span for span in spans if span["text"] == "Credits")
    special = next(span for span in spans if span["text"] == "Special Thanks to Seth Skorkowsky.")
    labels = [span for span in spans if span["semantic_role"] == "credit_role_label"]

    assert credits["heading_level"] == "h1"
    assert special["heading_level"] == "none"
    assert labels
    assert all(label["heading_level"] == "none" for label in labels)
    for span in spans:
        assert {"bold", "italic", "underline", "centered", "font_scale"}.issubset(span)


def test_next_review_packet_has_text_structure_semantics_and_crops_but_no_acceptance():
    report = read_json(REPORT)
    packet = NEXT_PACKET.read_text(encoding="utf-8")
    next_review = report["next_review_packet"]

    assert next_review["review_packet_id"] == "SRCR-G1-VIRAL-003"
    assert next_review["status"] == "draft_for_bogdan_review_not_accepted"
    assert next_review["source_acceptance"] is False
    assert next_review["page_complete_acceptance"] is False
    assert len(next_review["records"]) == 2
    for record in next_review["records"]:
        assert (ROOT / record["crop_reference"]).exists()
        assert record["draft_text"]
        assert record["draft_structure"]
        assert record["draft_structure"][0]["semantic_role"]
    assert "Answer shape" in packet
    assert "draft_for_bogdan_review_not_accepted" in packet


def test_next_review_crop_remediation_uses_padded_boxes_and_rebuilt_text_layer():
    report = read_json(REPORT)
    records = report["next_review_packet"]["records"]
    by_id = {record["review_id"]: record for record in records}

    title = by_id["SRCR-G1-VIRAL-003-R01"]
    body = by_id["SRCR-G1-VIRAL-003-R02"]

    assert title["box_px"] == [500, 130, 1550, 650]
    assert title["draft_text"] == "SPEKTRAL\nKREW"
    assert body["box_px"] == [270, 860, 2050, 2240]
    assert body["draft_text"].startswith("OK guys, here's the thing.")
    assert "OK - so any questions?" in body["draft_text"]
    assert "after_crop_remediation" in body["draft_text_basis"]
    assert report["next_review_packet"]["ocr_executed_for_draft"] is False


def test_next_review_crop_remediation_uses_global_no_overlap_guardrail():
    report = read_json(REPORT)
    guardrail = report["next_review_packet"]["crop_layout_guardrail"]

    assert guardrail["guardrail_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert guardrail["status"] == "passed"
    assert guardrail["validated_at_stage"] == "SRCR-G1-VIRAL-003.review_crop_generation"
    assert "historical_blocked_tight_boxes" in guardrail["checks"]
    assert "approved_boxes" in guardrail["checks"]
    assert "no_overlap" in guardrail["checks"]
    assert "min_gutter" in guardrail["checks"]
    assert guardrail["min_gutter_px"] >= 24


def test_next_review_human_feedback_is_recorded_without_acceptance():
    report = read_json(REPORT)
    feedback = report["next_review_human_verification"]

    assert feedback["verification_id"] == "SRCRV-G1-VIRAL-003"
    assert feedback["telegram_message_id"] == "437"
    assert [record["decision"] for record in feedback["records"]] == ["ok", "ok"]
    assert feedback["source_acceptance"] is False
    assert feedback["qa_acceptance"] is False
    assert feedback["fixture_admission"] is False
    assert feedback["page_complete_acceptance"] is False
    assert feedback["whole_gate_1_acceptance"] is False
