import json
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "source_reconstruction_remediation_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_crop_overlay_G1_VIRAL_001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_crop_overlay_remediation_preserves_boundaries():
    report = read_json(OUT_ROOT / "source_reconstruction_crop_overlay_report.json")

    assert report["status"] == "crop_overlay_remediation_evidence_only"
    assert report["source_acceptance"] is False
    assert report["qa_acceptance"] is False
    assert report["gate_1_advancement"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
    assert report["human_review_ready"] is False
    assert report["human_review_blocked"] is True


def test_crop_overlay_remediation_has_expected_routes():
    report = read_json(OUT_ROOT / "source_reconstruction_crop_overlay_report.json")
    by_region = {record["region_admission_id"]: record for record in report["candidate_records"]}

    assert by_region["SRA-G1-VIRAL-001-R001"]["remediation_status"] == "visual_component_demoted_from_text_review"
    assert by_region["SRA-G1-VIRAL-001-R001"]["cleaned_candidate_text"] is None
    assert by_region["SRA-G1-VIRAL-001-R001"]["new_ocr_required"] is False
    assert by_region["SRA-G1-VIRAL-001-R002"]["remediation_status"] == "noise_stripped_overlay_reference_ready"
    assert by_region["SRA-G1-VIRAL-001-R002"]["cleaned_candidate_text"] == "Contents"
    assert by_region["SRA-G1-VIRAL-001-R003"]["remediation_status"] == "narrow_subcrop_prepared_for_later_ocr_rerun"
    assert by_region["SRA-G1-VIRAL-001-R003"]["new_ocr_required"] is True
    assert by_region["SRA-G1-VIRAL-001-R004"]["remediation_status"] == "clean_text_overlay_reference_ready"
    assert by_region["SRA-G1-VIRAL-001-R004"]["cleaned_candidate_text"] == "Introduction"
    assert by_region["SRA-G1-VIRAL-001-R005"]["remediation_status"] == "carried_forward_candidate"
    assert by_region["SRA-G1-VIRAL-001-R005"]["human_review_ready"] is True


def test_crop_overlay_remediation_preserves_route_anchors_against_triage():
    report = read_json(OUT_ROOT / "source_reconstruction_crop_overlay_report.json")
    triage = read_json(INPUT_ROOT / "source_reconstruction_remediation_report.json")
    upstream_records = {
        record["region_admission_id"]: record
        for record in triage["candidate_records"] + triage["visual_qc_records"]
    }
    anchor_fields = {
        "sample_id",
        "page_id",
        "region_id",
        "predecessor_zone_id",
        "predecessor_crop_sha256",
        "page_image",
        "input_crop",
        "route_class",
        "review_class",
    }

    for record in report["candidate_records"] + report["visual_qc_records"]:
        upstream = upstream_records[record["region_admission_id"]]
        for field in anchor_fields:
            assert record[field] == upstream[field]


def test_crop_overlay_remediation_hashes_match_disk_bytes():
    report = read_json(OUT_ROOT / "source_reconstruction_crop_overlay_report.json")

    for record in report["candidate_records"] + report["visual_qc_records"]:
        artifact = record["crop_overlay_artifact"]
        artifact_path = ROOT / artifact["path"]
        source_path = ROOT / artifact["source_input_crop"]
        assert artifact_path.exists()
        assert source_path.exists()
        assert artifact["sha256"] == sha256_file(artifact_path)
        assert artifact["source_input_crop_sha256"] == sha256_file(source_path)
        assert artifact["size_px"]["width"] > 0
        assert artifact["size_px"]["height"] > 0


def test_crop_overlay_summary_keeps_next_authorization_narrow():
    report = read_json(OUT_ROOT / "source_reconstruction_crop_overlay_report.json")

    assert report["summary"]["candidate_records"] == 5
    assert report["summary"]["visual_qc_records"] == 2
    assert report["summary"]["ready_for_later_human_review"] == 1
    assert report["summary"]["overlay_reference_ready"] == 2
    assert report["summary"]["new_ocr_required"] == 1
    assert report["next_authorization_recommendation"] == "BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001"
