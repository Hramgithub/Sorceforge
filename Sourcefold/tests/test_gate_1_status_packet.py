import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_gate_1_status_packet.py"
REFRESH_SCRIPT = ROOT / "scripts" / "build_gate_1_status_refresh.py"
TRIAL_ROOT = (
    ROOT
    / "fixtures"
    / "candidate_inputs"
    / "viral"
    / "render_trials"
    / "RT-G1-VIRAL-RENDER-001"
)
ROLLUP_ROOT = TRIAL_ROOT / "gate_1_source_recon_evidence_rollup_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_001"
REFRESH_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_002"
STATUS_PACKET = OUT_ROOT / "gate_1_status_packet.json"
REPORT = OUT_ROOT / "gate_1_status_packet_report.json"
SUMMARY = OUT_ROOT / "gate_1_status_packet_summary.md"
REFRESH_PACKET = REFRESH_ROOT / "gate_1_status_packet.json"
REFRESH_REPORT = REFRESH_ROOT / "gate_1_status_report.json"
REFRESH_SUMMARY = REFRESH_ROOT / "gate_1_status_summary.md"
ROLLUP_REPORT = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup_report.json"
ROLLUP_MANIFEST = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup_manifest.md"
ROLLUP_PAYLOAD = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup.json"
ROLLUP_SUMMARY = ROLLUP_ROOT / "gate_1_source_recon_evidence_rollup_summary.md"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def test_gate_1_status_packet_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-GATE-1-SOURCE-RECON-EVIDENCE-ROLLUP-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-GATE-1-STATUS-PACKET-001" in wrong_auth.stderr


def test_gate_1_status_packet_preserves_rollup_lineage():
    report = read_json(REPORT)

    assert report["status_packet_id"] == "G1SP-G1-VIRAL-001"
    assert report["authorization_id"] == "BA-G1-VIRAL-GATE-1-STATUS-PACKET-001"
    assert report["input_rollup_id"] == "G1SRER-G1-VIRAL-001"
    assert report["input_rollup_report_sha256"] == sha256_file(ROLLUP_REPORT)
    assert report["input_rollup_manifest_sha256"] == sha256_file(ROLLUP_MANIFEST)
    assert report["input_rollup_payload_sha256"] == sha256_file(ROLLUP_PAYLOAD)
    assert report["input_rollup_summary_sha256"] == sha256_file(ROLLUP_SUMMARY)
    assert report["generator_script_sha256"] == sha256_file(SCRIPT)
    assert report["test_contract_sha256"]


def test_gate_1_status_packet_summarizes_only_one_narrow_slice():
    packet = read_json(STATUS_PACKET)
    source_slice = packet["accepted_evidence"]["source_reconstruction_slice"]

    assert packet["status"] == "gate_1_status_packet_ready_narrow_slice_only"
    assert packet["current_gate_1_state"] == "partial_narrow_source_reconstruction_evidence_accepted"
    assert source_slice["rollup_id"] == "G1SRER-G1-VIRAL-001"
    assert source_slice["accepted_scope"] == "seven_reviewed_records_only_pages_not_complete"
    assert source_slice["accepted_records"] == 7
    assert source_slice["accepted_source_text_records"] == 4
    assert source_slice["accepted_visual_exclusion_records"] == 3
    assert source_slice["accepted_pages"] == ["001", "005", "006"]
    assert source_slice["accepted_pages_as_complete"] is False
    assert source_slice["page_complete_acceptance"] is False
    assert source_slice["whole_gate_1_acceptance"] is False
    assert packet["new_gate_1_advancement_created"] is False
    assert packet["inherited_gate_1_advancement_scope"] == "seven_reviewed_records_only_pages_not_complete"


def test_gate_1_status_packet_keeps_broader_gate_and_pages_pending():
    packet = read_json(STATUS_PACKET)
    report = read_json(REPORT)

    for item in [
        "page_001_complete",
        "page_005_complete",
        "page_006_complete",
        "whole_viral_pdf",
        "whole_gate_1",
        "source_profile",
    ]:
        assert item in packet["not_accepted"]

    for item in [
        "additional_source_reconstruction_slices",
        "page_complete_review_if_needed",
        "whole_gate_1_review",
        "source_profile_parameter_acceptance",
    ]:
        assert item in packet["pending"]

    for payload in [packet, report]:
        assert payload["whole_gate_1_ready"] is False
        assert payload["source_profile_accepted"] is False
        assert payload["page_complete_acceptance"] is False
        assert payload["translation_authorized"] is False
        assert payload["proofreading_authorized"] is False
        assert payload["renderer_profile_acceptance"] is False
        assert payload["implementation_authorized"] is False
        assert payload["push_authorized"] is False
        assert payload["ocr_executed"] is False
        assert payload["pdf_opened_or_parsed"] is False
        assert payload["raw_ocr_outputs_modified"] is False


def test_gate_1_status_packet_summary_is_human_readable_and_bounded():
    summary = SUMMARY.read_text(encoding="utf-8")

    assert "Accepted records: `7`" in summary
    assert "Page 001 complete: `false`" in summary
    assert "Whole Viral PDF: `false`" in summary
    assert "Whole Gate 1: `false`" in summary
    assert "Additional source reconstruction slices." in summary
    assert "seven_reviewed_records_only_pages_not_complete" in summary


def test_gate_1_status_packet_script_has_no_ocr_pdf_or_raw_mutation_dependencies():
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


def test_gate_1_status_refresh_is_fail_closed_without_exact_authorization():
    no_execute = subprocess.run([sys.executable, str(REFRESH_SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(REFRESH_SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-GATE-1-STATUS-PACKET-001",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert "BA-G1-VIRAL-GATE-1-STATUS-REFRESH-002" in wrong_auth.stderr


def test_gate_1_status_refresh_records_post_p008_baseline_without_acceptance():
    packet = read_json(REFRESH_PACKET)
    report = read_json(REFRESH_REPORT)

    assert packet["status_packet_id"] == "G1SP-G1-VIRAL-002"
    assert packet["authorization_id"] == "BA-G1-VIRAL-GATE-1-STATUS-REFRESH-002"
    assert packet["creates_acceptance"] is False
    assert packet["baseline"]["page_complete_accepted_pages"] == ["002", "003", "004", "005", "006", "007", "008"]
    assert packet["baseline"]["g1sp_001_state"] == "historical_narrow_stale_for_current_page_complete_status"
    assert packet["baseline"]["source_reconstruction_current_canonical_narrow_state"] == "13_accepted_records"
    assert packet["baseline"]["new_source_acceptance_rollup_created"] is False
    assert report["creates_acceptance"] is False
    assert report["new_source_acceptance_rollup_created"] is False
    assert report["whole_gate_1_acceptance"] is False


def test_gate_1_status_refresh_has_first_class_blockers_and_negative_capability_matrix():
    packet = read_json(REFRESH_PACKET)
    flags = packet["blocker_flags"]

    assert flags["page_001_incomplete"] is True
    assert flags["pages_009_020_unstarted"] is True
    assert flags["whole_gate_1_acceptance"] is False
    assert flags["source_profile_parameters_unaccepted_or_unparked"] is True
    assert flags["ocr_benchmark_remediation_unresolved"] is True
    assert flags["gate_1_status_only_no_acceptance"] is True

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    for key in [
        "fixture_admission",
        "source_mutation",
        "new_source_acceptance",
        "ocr_execution",
        "render_execution",
        "pdf_parsing_or_text_layer_extraction",
        "raw_mutation",
        "translation",
        "proofreading",
        "renderer_profile_acceptance",
        "implementation",
        "push",
        "page_009_plus_processing",
        "whole_gate_1_acceptance",
    ]:
        assert packet["negative_capability_matrix"][key] is False


def test_gate_1_status_refresh_binds_predecessors_and_state_taxonomy():
    packet = read_json(REFRESH_PACKET)
    bindings = packet["predecessor_bindings"]

    assert sorted(bindings["page_complete_acceptances"]) == ["002", "003", "004", "005", "006", "007", "008"]
    assert bindings["page_complete_acceptances"]["008"]["package_id"] == "P008PCA-G1-VIRAL-001"
    assert bindings["status_predecessors"]["G1SP-G1-VIRAL-001"]["authority"] == "historical_narrow_status_not_current_full_status"
    assert bindings["status_predecessors"]["G1SRER-G1-VIRAL-001"]["authority"] == "historical_7_record_durable_source_reconstruction_rollup"
    assert bindings["source_acceptance_surfaces"]["P004A-G1-VIRAL-004"]["total_after"] == 13

    for state in [
        "accepted",
        "page_complete_accepted",
        "review_packet",
        "readiness",
        "rolled_up",
        "parked",
        "blocked",
        "stale",
        "superseded",
    ]:
        assert state in packet["state_taxonomy"]


def test_gate_1_status_refresh_routing_matrix_presents_options_without_authorizing():
    packet = read_json(REFRESH_PACKET)
    options = {item["option"]: item["status"] for item in packet["routing_matrix"]}
    reasons = {item["option"]: item["why"] for item in packet["routing_matrix"]}

    assert options["page_001_completion"] == "recommended_next_candidate_not_authorized"
    assert options["pages_009_020_continuation"] == "valid_later_small_slices_not_authorized"
    assert options["ocr_benchmark_remediation"] == "separate_branch_not_authorized"
    assert options["source_profile_or_gate_1_parameter_parking_or_acceptance_review"] == "separate_branch_not_authorized"
    assert options["whole_gate_1_acceptance"] == "not_ready"
    assert options["translation_proofreading_implementation"] == "not_ready"
    whole_gate_reason = reasons["whole_gate_1_acceptance"]
    assert "page_001_incomplete" in whole_gate_reason
    assert "pages_009_020_unstarted" in whole_gate_reason
    assert "source_profile_parameters_unaccepted_or_unparked" in whole_gate_reason
    assert "ocr_benchmark_remediation_unresolved" in whole_gate_reason
    assert packet["recommended_next_candidate"] == "page_001_completion"


def test_gate_1_status_refresh_summary_is_human_readable_and_bounded():
    summary = REFRESH_SUMMARY.read_text(encoding="utf-8")

    assert "Gate 1 Status Route Packet - G1SP-G1-VIRAL-002" in summary
    assert "Page-complete accepted only: `002`, `003`, `004`, `005`, `006`, `007`, `008`." in summary
    assert "`page_001_incomplete=true`" in summary
    assert "`pages_009_020_unstarted=true`" in summary
    assert "`whole_gate_1_acceptance=false`" in summary
    assert "Recommended next candidate: `page_001_completion`." in summary
    assert "Decision after review: `status packet ok` or `hold status packet: <reason>`." in summary
