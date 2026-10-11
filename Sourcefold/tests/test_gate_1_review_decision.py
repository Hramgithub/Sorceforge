import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "record_gate_1_review_decision.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
BRIEF_ROOT = TRIAL_ROOT / "gate_1_review_decision_brief_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_review_decision_G1_VIRAL_001"
REPORT = OUT_ROOT / "gate_1_review_decision_report.json"
RECORD = OUT_ROOT / "gate_1_review_decision_record.json"
RECORD_MD = OUT_ROOT / "gate_1_review_decision_record.md"
BRIEF_REPORT = BRIEF_ROOT / "gate_1_review_decision_brief_report.json"
BRIEF_JSON = BRIEF_ROOT / "gate_1_review_decision_brief.json"
BRIEF_MD = BRIEF_ROOT / "gate_1_review_decision_brief.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_gate_1_review_decision_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-BRIEF-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001" in wrong_auth.stderr


def test_gate_1_review_decision_preserves_brief_lineage():
    report = read_json(REPORT)

    assert report["decision_id"] == "G1RD-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-GATE-1-REVIEW-DECISION-001"
    assert report["status"] == "gate_1_source_reconstruction_evidence_slice_accepted"
    assert report["input_brief_id"] == "G1RDB-G1-VIRAL-001"
    assert report["input_brief_report_sha256"] == sha256_file(BRIEF_REPORT)
    assert report["input_brief_json_sha256"] == sha256_file(BRIEF_JSON)
    assert report["input_brief_markdown_sha256"] == sha256_file(BRIEF_MD)
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"] == sha256_file(ROOT / "tests" / "test_gate_1_review_decision.py")


def test_gate_1_review_decision_records_narrow_acceptance_scope():
    decision = read_json(RECORD)
    report = read_json(REPORT)

    assert decision["user_decision"] == {
        "actor": "Bogdan",
        "telegram_message_id": 303,
        "raw_text": "1 принято",
        "normalized_decision": "accept",
        "accepted_answer": "1 - принять",
        "decision_timestamp": "2026-07-18T15:28:14Z",
    }
    assert decision["accepted_scope"] == "exact_G1RP_G1_VIRAL_001_source_reconstruction_evidence_slice_only"
    assert decision["direct_packet_lineage"] == {
        "packet_id": "G1RP-G1-VIRAL-001",
        "packet_report_sha256": "AE3695954BE26DB60EB541CD9819532CE5CA98F961D0F0B21F06C0BE5F96D990",
        "packet_manifest_sha256": "E21D57630A3AB235AE901D3A27375F16527A81F0DE584D80EEA5527AA382DE86",
        "packet_payload_sha256": "8197860F5176CB25423D6CE6EDB30B831E603D369C100A3F79105620894EDCF9",
        "packet_summary_sha256": "93424483B2C870028A2330F79C81F0A3C270A2E5A9085314D4687C89D2F628EC",
    }
    assert report["direct_packet_lineage"] == decision["direct_packet_lineage"]
    assert decision["accepted_records"] == 7
    assert decision["accepted_source_text_records"] == 4
    assert decision["accepted_visual_exclusion_records"] == 3
    assert decision["accepted_pages_as_complete"] is False
    assert decision["whole_gate_1_acceptance"] is False
    assert decision["gate_1_decision_recorded"] is True
    assert decision["gate_1_advancement"] is True
    assert decision["gate_1_advancement_scope"] == "seven_reviewed_records_only_pages_not_complete"
    assert report["requires_rollup_before_broader_gate_use"] is True


def test_gate_1_review_decision_keeps_forbidden_work_blocked():
    decision = read_json(RECORD)

    assert decision["translation_authorized"] is False
    assert decision["proofreading_authorized"] is False
    assert decision["renderer_profile_acceptance"] is False
    assert decision["implementation_authorized"] is False
    assert decision["push_authorized"] is False
    assert decision["ocr_executed"] is False
    assert decision["pdf_opened_or_parsed"] is False
    assert decision["raw_ocr_outputs_modified"] is False
    assert decision["non_waivable_result"] == {
        "blocking_items": 0,
        "missing_qa_coverage": False,
        "stale_lineage": False,
        "waiver_or_parking_bypass": False,
        "pdf_text_layer_leakage": False,
        "unauthorized_ocr_pdf_render_raw_mutation": False,
    }


def test_gate_1_review_decision_markdown_states_pages_not_complete():
    record_md = RECORD_MD.read_text(encoding="utf-8")

    assert "Accepted records: `7`" in record_md
    assert "Pages accepted as complete: `false`" in record_md
    assert "Whole Gate 1 accepted: `false`" in record_md
    assert "Telegram message id: `303`" in record_md


def test_gate_1_review_decision_script_has_no_ocr_pdf_or_raw_mutation_dependencies():
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
