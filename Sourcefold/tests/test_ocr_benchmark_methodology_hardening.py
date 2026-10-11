import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_ocr_benchmark_methodology_hardening.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "ocr_benchmark_methodology_hardening_G1_VIRAL_001"
PACKET = OUT_ROOT / "ocr_benchmark_methodology_hardening.json"
REPORT = OUT_ROOT / "ocr_benchmark_methodology_hardening_report.json"
SUMMARY = OUT_ROOT / "ocr_benchmark_methodology_hardening_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-OCR-BENCHMARK-METHODOLOGY-HARDENING-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_ocr_benchmark_methodology_hardening_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-WRONG"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_ocr_benchmark_methodology_hardening_records_existing_evidence_only():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["hardening_id"] == "OCRHM-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["status"] == "ocr_benchmark_methodology_hardened_for_gate_review_no_acceptance"
    assert packet["baseline_matrix_review"] == "G1SPRMREV-G1-VIRAL-001"
    assert packet["ocr_evidence"]["orm_run_id"] == "ORM-G1-VIRAL-001"
    assert packet["ocr_evidence"]["orr_review_id"] == "ORR-G1-VIRAL-001"
    assert packet["ocr_evidence"]["aggregate"]["samples"] == 5
    assert packet["ocr_evidence"]["aggregate"]["remediation_route_pass"] == 5

    assert packet["creates_acceptance"] is False
    assert packet["creates_parking_decision"] is False
    assert packet["executes_ocr"] is False
    assert packet["starts_remediation_run"] is False
    assert report["creates_acceptance"] is False
    assert report["creates_parking_decision"] is False
    assert report["executes_ocr"] is False
    assert report["starts_remediation_run"] is False


def test_ocr_benchmark_methodology_hardening_rules_cover_core_debt():
    packet = read_json(PACKET)
    rows = {row["id"]: row for row in packet["methodology_rules"]}

    assert packet["methodology_rule_counts"] == {
        "hardened_for_gate_review": 8,
        "requires_future_gate_decision": 1,
    }
    for expected in [
        "exact_predecessor_lineage",
        "no_new_ocr_or_pdf_execution",
        "engine_config_and_psm_policy",
        "benchmark_pass_fail_policy",
        "visual_qc_route_policy",
        "overlay_order_qc_interpretation",
        "raw_payload_containment",
        "human_review_deferral_policy",
        "remaining_gate_decisions",
    ]:
        assert expected in rows
    assert rows["benchmark_pass_fail_policy"]["status"] == "hardened_for_gate_review"
    assert rows["remaining_gate_decisions"]["status"] == "requires_future_gate_decision"


def test_ocr_benchmark_methodology_hardening_preserves_negative_capabilities():
    packet = read_json(PACKET)

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key
    assert packet["next_status"] == {
        "ocr_benchmark_remediation_debt": "methodology_hardened_for_gate_review",
        "source_profile_acceptance": "still_requires_future_gate_decision",
        "recommended_next_packet": "post_ocr_hardening_gate_1_readiness_refresh",
    }


def test_ocr_benchmark_methodology_hardening_summary_is_human_readable():
    summary = SUMMARY.read_text(encoding="utf-8-sig")

    assert "OCR Benchmark Methodology Hardening - OCRHM-G1-VIRAL-001" in summary
    assert "No OCR execution or remediation rerun." in summary
    assert "No source-profile acceptance." in summary
    assert "post_ocr_hardening_gate_1_readiness_refresh" in summary
