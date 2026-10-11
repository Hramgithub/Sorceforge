import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_remediation_G1_VIRAL_001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_remediation_triage_preserves_boundaries():
    report = read_json(OUT_ROOT / "source_reconstruction_remediation_report.json")

    assert report["status"] == "remediation_triage_only"
    assert report["source_acceptance"] is False
    assert report["qa_acceptance"] is False
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False


def test_remediation_triage_has_expected_record_routes():
    report = read_json(OUT_ROOT / "source_reconstruction_remediation_report.json")
    by_region = {record["region_admission_id"]: record for record in report["candidate_records"]}

    assert by_region["SRA-G1-VIRAL-001-R001"]["status"] == "blocked_visual_component"
    assert by_region["SRA-G1-VIRAL-001-R001"]["recommended_next_action"] == "visual_crop_remediation"
    assert by_region["SRA-G1-VIRAL-001-R001"]["cleaned_candidate_text"] is None
    assert by_region["SRA-G1-VIRAL-001-R001"]["human_review_ready"] is False
    assert by_region["SRA-G1-VIRAL-001-R002"]["cleaned_candidate_text"] == "Contents"
    assert by_region["SRA-G1-VIRAL-001-R002"]["recommended_next_action"] == "overlay_verify_after_cleanup"
    assert by_region["SRA-G1-VIRAL-001-R002"]["human_review_ready"] is False
    assert by_region["SRA-G1-VIRAL-001-R003"]["status"] == "blocked_overbroad_crop"
    assert by_region["SRA-G1-VIRAL-001-R003"]["recommended_next_action"] == "narrow_contents_crop_remediation"
    assert by_region["SRA-G1-VIRAL-001-R003"]["cleaned_candidate_text"] is None
    assert by_region["SRA-G1-VIRAL-001-R003"]["human_review_ready"] is False
    assert by_region["SRA-G1-VIRAL-001-R004"]["status"] == "text_clean_needs_overlay_verify"
    assert by_region["SRA-G1-VIRAL-001-R004"]["recommended_next_action"] == "overlay_verify"
    assert by_region["SRA-G1-VIRAL-001-R004"]["cleaned_candidate_text"] == "Introduction"
    assert by_region["SRA-G1-VIRAL-001-R004"]["human_review_ready"] is False
    assert by_region["SRA-G1-VIRAL-001-R005"]["recommended_next_action"] == "carry_forward"
    assert by_region["SRA-G1-VIRAL-001-R005"]["human_review_ready"] is True


def test_remediation_records_preserve_exact_route_anchors():
    report = read_json(OUT_ROOT / "source_reconstruction_remediation_report.json")
    required = {
        "sample_id",
        "page_id",
        "region_id",
        "predecessor_zone_id",
        "predecessor_crop_sha256",
        "page_image",
        "input_crop",
        "route_class",
        "review_class",
        "selected_config",
        "candidate_text_sha256",
        "candidate_tsv_sha256",
        "overlay_qc_status",
        "order_qc_status",
    }

    for record in report["candidate_records"]:
        assert required.issubset(record)
        assert record["predecessor_crop_sha256"]
        assert record["input_crop"]
        assert record["route_class"] == "ocr_candidate"
        assert record["review_class"]
        assert record["overlay_qc_status"]
        assert record["order_qc_status"]


def test_remediation_summary_keeps_human_review_blocked():
    report = read_json(OUT_ROOT / "source_reconstruction_remediation_report.json")

    assert report["summary"]["candidate_records"] == 5
    assert report["summary"]["ready_for_later_human_review"] == 1
    assert report["summary"]["needs_overlay_verify"] == 2
    assert report["summary"]["needs_crop_remediation"] == 2
    assert report["summary"]["visual_qc_only_records"] == 2
    assert report["next_authorization_recommendation"] == "BA-G1-VIRAL-SOURCE-RECON-CROP-REMEDIATE-001"
