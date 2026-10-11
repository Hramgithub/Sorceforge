import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_source_reconstruction_next_slice_004.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_004"
REPORT = OUT_ROOT / "source_reconstruction_next_slice_report.json"
REVIEW_PACKET = OUT_ROOT / "human_review_packet.md"
MANIFEST = OUT_ROOT / "source_reconstruction_next_slice_manifest.md"
P003A_ROOT = TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001"
P003A_REPORT = P003A_ROOT / "p003_verified_review_acceptance_report.json"
P003A_MANIFEST = P003A_ROOT / "p003_verified_review_acceptance_manifest.md"
P003A_SUMMARY = P003A_ROOT / "p003_verified_review_acceptance_summary.md"
PRM_REPORT = TRIAL_ROOT / "provisional_region_map_report.md"
PAGE_004 = TRIAL_ROOT / "images" / "page_004.png"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_page_004_next_slice_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004" in wrong_auth.stderr


def test_page_004_next_slice_consumes_p003a_and_region_lineage():
    report = read_json(REPORT)

    assert report["package_id"] == "SRCR-G1-VIRAL-004"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-004"
    assert report["generator"]["script"] == "scripts/build_source_reconstruction_next_slice_004.py"
    assert report["generator"]["script_sha256"]
    assert report["generator"]["test"] == "tests/test_source_reconstruction_next_slice_004.py"
    assert report["generator"]["test_sha256"]
    assert report["input_package_id"] == "P003A-G1-VIRAL-003"
    assert report["input_report_sha256"] == sha256_file(P003A_REPORT)
    assert report["input_manifest_sha256"] == sha256_file(P003A_MANIFEST)
    assert report["input_summary_sha256"] == sha256_file(P003A_SUMMARY)
    assert report["input_region_map_id"] == "PRM-G1-VIRAL-001"
    assert report["input_region_map_sha256"] == sha256_file(PRM_REPORT)
    assert report["selected_page"] == "004"
    assert report["selected_page_image_sha256"] == sha256_file(PAGE_004)


def test_page_004_next_slice_contains_two_peer_review_records_and_context_only_r01():
    report = read_json(REPORT)
    records = report["records"]

    assert report["summary"]["records"] == 2
    assert report["summary"]["draft_text_records"] == 2
    assert report["summary"]["requires_bogdan_review_records"] == 2
    assert report["summary"]["accepted_records"] == 0
    assert report["summary"]["prior_accepted_records_preserved"] == 11
    assert report["context_region"]["source_region_id"] == "PRM-G1-VIRAL-001-P004-R01"
    assert report["context_region"]["status"] == "context_only_not_peer_crop_record"
    assert {record["source_region_id"] for record in records} == {
        "PRM-G1-VIRAL-001-P004-R02",
        "PRM-G1-VIRAL-001-P004-R03",
    }
    assert [record["question_id"] for record in records] == ["1", "2"]
    assert all(record["page_id"] == "PG-G1-VIRAL-P004" for record in records)
    assert all(record["requires_bogdan_review"] is True for record in records)


def test_page_004_next_slice_crop_references_match_disk_and_are_pngs():
    report = read_json(REPORT)

    for record in report["records"]:
        crop = ROOT / record["crop_reference"]
        assert crop.exists()
        assert crop.suffix.lower() == ".png"
        assert record["crop_reference_sha256"] == sha256_file(crop)
        assert record["page_image_sha256"] == sha256_file(PAGE_004)


def test_page_004_next_slice_uses_global_crop_layout_guardrail_with_approved_boxes():
    report = read_json(REPORT)
    guardrail = report["crop_layout_guardrail"]

    assert guardrail["guardrail_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert guardrail["status"] == "passed"
    assert guardrail["validated_at_stage"] == "SRCR-G1-VIRAL-004.review_crop_generation"
    assert "approved_boxes" in guardrail["checks"]
    assert "no_overlap" in guardrail["checks"]
    assert "min_gutter" in guardrail["checks"]
    assert guardrail["min_gutter_px"] >= 24
    boxes = {item["region_id"]: item["box_px"] for item in guardrail["validated_boxes"]}
    assert boxes == {
        "SRCR-G1-VIRAL-004-R01": [720, 330, 1100, 270],
        "SRCR-G1-VIRAL-004-R02": [330, 630, 1950, 2520],
    }


def test_page_004_next_slice_includes_draft_text_structure_and_numbered_review_packet():
    report = read_json(REPORT)
    packet = REVIEW_PACKET.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")

    assert report["records"][0]["draft_text"] == "WARNING"
    assert "Viral is intended for mature audiences." in report["records"][1]["draft_text"]
    assert "changed or eliminated as the Keeper sees fit." in report["records"][1]["draft_text"]
    assert report["records"][0]["draft_structure"][0]["semantic_role"] == "warning_title"
    assert report["records"][1]["draft_structure"][0]["semantic_role"] == "safety_warning_body"
    assert "1 - ok / correction / blocker" in packet
    assert "2 - ok / correction / blocker" in packet
    assert "Context note" in packet
    assert "Draft text SHA-256" in manifest


def test_page_004_next_slice_does_not_expand_acceptance_or_gate_scope():
    report = read_json(REPORT)

    assert report["summary"]["accepted_pages_as_complete"] is False
    assert report["summary"]["whole_gate_1_acceptance"] is False
    for payload in [report, *report["records"]]:
        assert payload["source_acceptance"] is False
        assert payload["qa_acceptance"] is False
        assert payload["fixture_admission"] is False
        assert payload["gate_1_advancement"] is False
    assert report["page_complete_acceptance"] is False
    assert report["whole_gate_1_acceptance"] is False
    assert report["translation_authorized"] is False
    assert report["proofreading_authorized"] is False
    assert report["renderer_profile_acceptance"] is False
    assert report["implementation_authorized"] is False
    assert report["push_authorized"] is False
    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False


def test_page_004_next_slice_script_has_no_ocr_pdf_render_or_raw_mutation_dependencies():
    source = SCRIPT.read_text(encoding="utf-8").lower()

    forbidden = [
        "tesseract",
        "subprocess.run(",
        "pypdf",
        "pdfminer",
        "fitz",
        "pymupdf",
        "pdftotext",
        "pdftoppm",
        "render_page(",
        "render_pdf",
        "page_render",
        "raw_outputs",
    ]
    for token in forbidden:
        assert token not in source

    out_files = [path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file()]
    assert not any("raw_outputs" in path for path in out_files)
    assert not any(path.endswith(".pdf") for path in out_files)
    assert not any(path.endswith(".tsv") for path in out_files)
