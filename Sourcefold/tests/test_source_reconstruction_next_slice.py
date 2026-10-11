import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_source_reconstruction_next_slice.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002"
REPORT = OUT_ROOT / "source_reconstruction_next_slice_report.json"
REVIEW_PACKET = OUT_ROOT / "human_review_packet.md"
MANIFEST = OUT_ROOT / "source_reconstruction_next_slice_manifest.md"
STATUS_PACKET = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_001" / "gate_1_status_packet.json"
STATUS_REPORT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_001" / "gate_1_status_packet_report.json"
PRM_REPORT = TRIAL_ROOT / "provisional_region_map_report.md"
PAGE_002 = TRIAL_ROOT / "images" / "page_002.png"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_next_slice_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-GATE-1-STATUS-PACKET-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001" in wrong_auth.stderr


def test_next_slice_preserves_status_packet_and_region_lineage():
    report = read_json(REPORT)

    assert report["package_id"] == "SRNS-G1-VIRAL-002"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-NEXT-SLICE-001"
    assert report["generator"]["script"] == "scripts/build_source_reconstruction_next_slice.py"
    assert report["generator"]["script_sha256"] == sha256_file(SCRIPT)
    assert report["generator"]["test"] == "tests/test_source_reconstruction_next_slice.py"
    assert report["generator"]["test_sha256"] == sha256_file(Path(__file__))
    assert report["input_status_packet_id"] == "G1SP-G1-VIRAL-001"
    assert report["input_status_packet_report_sha256"] == sha256_file(STATUS_REPORT)
    assert report["input_status_packet_payload_sha256"] == sha256_file(STATUS_PACKET)
    assert report["input_region_map_id"] == "PRM-G1-VIRAL-001"
    assert report["input_region_map_sha256"] == sha256_file(PRM_REPORT)
    assert report["selected_page"] == "002"
    assert report["selected_page_image_sha256"] == sha256_file(PAGE_002)
    assert report["selected_scope"] == "page_002_two_region_review_packet_only"


def test_next_slice_contains_only_page_002_two_region_review_packet():
    report = read_json(REPORT)
    records = report["records"]

    assert report["summary"]["records"] == 2
    assert report["summary"]["source_text_candidate_records"] == 0
    assert report["summary"]["requires_bogdan_review_records"] == 2
    assert {record["source_region_id"] for record in records} == {
        "PRM-G1-VIRAL-001-P002-R01",
        "PRM-G1-VIRAL-001-P002-R02",
    }
    assert [record["question_id"] for record in records] == ["1", "2"]
    assert all(record["page_id"] == "PG-G1-VIRAL-P002" for record in records)
    assert all(record["candidate_text"] is None for record in records)
    assert all(record["candidate_text_created"] is False for record in records)
    assert all(record["requires_bogdan_review"] is True for record in records)


def test_next_slice_crop_references_match_disk_and_are_pngs():
    report = read_json(REPORT)

    for record in report["records"]:
        crop = ROOT / record["crop_reference"]
        assert crop.exists()
        assert crop.suffix.lower() == ".png"
        assert record["crop_reference_sha256"] == sha256_file(crop)
        assert record["page_image_sha256"] == sha256_file(PAGE_002)


def test_next_slice_uses_global_crop_layout_guardrail():
    report = read_json(REPORT)
    guardrail = report["crop_layout_guardrail"]

    assert guardrail["guardrail_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert guardrail["status"] == "passed"
    assert "no_overlap" in guardrail["checks"]
    assert "min_gutter" in guardrail["checks"]
    assert guardrail["min_gutter_px"] >= 24
    boxes = [record["box_px"] for record in report["records"]]
    assert boxes == [[520, 350, 1500, 2100], [520, 2480, 1500, 420]]


def test_next_slice_does_not_expand_acceptance_or_gate_scope():
    report = read_json(REPORT)

    assert report["previous_accepted_scope_preserved"] == "G1SP-G1-VIRAL-001 seven-record slice remains unchanged"
    assert report["summary"]["accepted_records"] == 0
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


def test_next_slice_review_packet_uses_numbered_answer_shape():
    packet = REVIEW_PACKET.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")

    assert "### 1 - PRM-G1-VIRAL-001-P002-R01" in packet
    assert "### 2 - PRM-G1-VIRAL-001-P002-R02" in packet
    assert "1 - text:" in packet
    assert "2 - text:" in packet
    assert "no candidate text, source acceptance, QA acceptance, fixtures, Gate 1 advancement" in packet
    assert "page 002 two-region packet only" in manifest


def test_next_slice_script_has_no_ocr_pdf_render_or_raw_mutation_dependencies():
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
