import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare_source_reconstruction_p002_assisted_draft.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001"
REPORT = OUT_ROOT / "source_reconstruction_p002_assisted_draft_report.json"
MANIFEST = OUT_ROOT / "source_reconstruction_p002_assisted_draft_manifest.md"
DRAFT = OUT_ROOT / "assisted_text_draft_for_bogdan.md"
SRNS_REPORT = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002" / "source_reconstruction_next_slice_report.json"
SRNS_MANIFEST = TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002" / "source_reconstruction_next_slice_manifest.md"
PAGE_002 = TRIAL_ROOT / "images" / "page_002.png"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_p002_assisted_draft_is_fail_closed_without_exact_authorization():
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
    assert "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001" in wrong_auth.stderr


def test_p002_assisted_draft_preserves_srns_lineage_and_generator_hashes():
    report = read_json(REPORT)

    assert report["draft_id"] == "SRAD-G1-VIRAL-002"
    assert report["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-P002-ASSISTED-DRAFT-001"
    assert report["generator"]["script_sha256"] == sha256_file(SCRIPT)
    assert report["generator"]["test_sha256"] == sha256_file(Path(__file__))
    assert report["input_next_slice_id"] == "SRNS-G1-VIRAL-002"
    assert report["input_next_slice_report_sha256"] == sha256_file(SRNS_REPORT)
    assert report["input_next_slice_manifest_sha256"] == sha256_file(SRNS_MANIFEST)
    assert report["selected_page"] == "002"
    assert report["selected_page_image_sha256"] == sha256_file(PAGE_002)


def test_p002_assisted_draft_records_bogdan_route_without_acceptance():
    report = read_json(REPORT)

    assert [message["telegram_message_id"] for message in report["user_review_messages"]] == ["351", "356"]
    assert "длинный для переписывания" in report["user_review_messages"][1]["raw_text"]
    assert {record["initial_user_route"] for record in report["records"]} == {
        "text_present_but_too_long_for_manual_transcription"
    }
    assert report["summary"]["records"] == 2
    assert report["summary"]["draft_text_records"] == 2
    assert report["summary"]["accepted_records"] == 0
    assert report["draft_text_created"] is True
    assert report["draft_text_is_source_accepted"] is False


def test_p002_assisted_draft_contains_corrected_split_crops_and_text():
    report = read_json(REPORT)
    records = {record["question_id"]: record for record in report["records"]}

    assert set(records) == {"1", "2"}
    assert records["1"]["crop_correction_note"] == "wider split crop; excludes lower footer/legal block overlap"
    assert records["1"]["box_px"] == [180, 90, 2190, 1860]
    assert records["2"]["crop_correction_note"] == "taller lower split crop containing the special-thanks and legal/footer text"
    assert records["2"]["box_px"] == [200, 1980, 2150, 1220]
    assert "Credits" in records["1"]["draft_text"]
    assert "Play Testers" in records["1"]["draft_text"]
    assert "Special Thanks to Seth Skorkowsky." in records["2"]["draft_text"]
    assert "www.Chaosium.com" in records["2"]["draft_text"]
    for record in records.values():
        crop = ROOT / record["corrected_crop_reference"]
        assert crop.exists()
        assert crop.suffix.lower() == ".png"
        assert record["corrected_crop_reference_sha256"] == sha256_file(crop)
        assert record["draft_text_sha256"] == sha256_text(record["draft_text"])


def test_p002_assisted_draft_uses_global_crop_layout_guardrail():
    report = read_json(REPORT)
    guardrail = report["crop_layout_guardrail"]

    assert guardrail["guardrail_policy_id"] == "SRCG-GLOBAL-CROP-BOX-LAYOUT-001"
    assert guardrail["status"] == "passed"
    assert guardrail["validated_at_stage"] == "SRAD-G1-VIRAL-002.corrected_crop_generation"
    assert "approved_boxes" in guardrail["checks"]
    assert "min_gutter" in guardrail["checks"]


def test_p002_assisted_draft_does_not_expand_gate_or_page_scope():
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


def test_p002_assisted_draft_has_no_ocr_pdf_render_or_raw_mutation():
    report = read_json(REPORT)
    source = SCRIPT.read_text(encoding="utf-8").lower()

    assert report["ocr_executed"] is False
    assert report["pdf_opened_or_parsed"] is False
    assert report["raw_ocr_outputs_modified"] is False
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
        "raw_outputs",
    ]
    for token in forbidden:
        assert token not in source

    out_files = [path.relative_to(OUT_ROOT).as_posix() for path in OUT_ROOT.rglob("*") if path.is_file()]
    assert not any("raw_outputs" in path for path in out_files)
    assert not any(path.endswith(".pdf") for path in out_files)
    assert not any(path.endswith(".tsv") for path in out_files)


def test_p002_assisted_draft_review_packet_requires_bogdan_verification():
    draft = DRAFT.read_text(encoding="utf-8")
    manifest = MANIFEST.read_text(encoding="utf-8")

    assert "ready_for_bogdan_verification_not_accepted" in draft
    assert "N - ok" in draft
    assert "N - правка:" in draft
    assert "not source acceptance" in draft
    assert "Generator Hashes" in manifest
    assert "no source acceptance, QA, fixtures, Gate 1 advancement" in manifest
