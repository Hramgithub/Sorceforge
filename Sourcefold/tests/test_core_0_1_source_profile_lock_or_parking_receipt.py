import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_source_profile_lock_or_parking_receipt.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_G1_VIRAL_001"
RECEIPT = OUT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt.json"
REPORT = OUT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_report.json"
SUMMARY = OUT_ROOT / "core_0_1_source_profile_lock_or_parking_receipt_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-SINGLE-SOURCE-PROFILE-LOCK-OR-PARKING-RECEIPT-001"
HUMAN_DECISION = (
    "c01fsdp packet ok; proceed to prepare single source-profile lock-or-parking receipt for C01WP-01 "
    "from C01FSDP; no runtime implementation, no source-profile lock or acceptance beyond this receipt, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_source_profile_receipt_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-WRONG",
            "--decision",
            HUMAN_DECISION,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr

    wrong_decision = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            AUTHORIZATION_ID,
            "--decision",
            "c01fsdp packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_source_profile_receipt_scope():
    receipt = read_json(RECEIPT)
    report = read_json(REPORT)
    scope = receipt["accepted_gate_1_scope"]

    assert receipt["receipt_id"] == "C01SPLPR-G1-VIRAL-001"
    assert receipt["authorization_id"] == AUTHORIZATION_ID
    assert receipt["source_first_slice_design_prep_packet"] == "C01FSDP-G1-VIRAL-001"
    assert receipt["source_whole_gate_1_acceptance_decision"] == "G1WGADR-G1-VIRAL-001"
    assert receipt["first_slice_id"] == "C01WP-01-phase-1-scaffold-contracts"
    assert receipt["human_decision"] == HUMAN_DECISION
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["accepted_page_count"] == 20


def test_core_0_1_source_profile_receipt_disposition_and_boundaries():
    receipt = read_json(RECEIPT)
    report = read_json(REPORT)
    disposition = receipt["source_profile_disposition"]

    assert disposition["profile_receipt_disposition"] == "park_source_profile_lock_for_design_prep_only"
    assert receipt["source_profile_receipt_created"] is True
    assert receipt["source_profile_parking_recorded"] is True
    assert receipt["source_profile_lock_created"] is False
    assert receipt["source_profile_acceptance_created"] is False
    assert receipt["accepts_source_profile_beyond_this_receipt"] is False

    for payload in (receipt, report):
        assert payload["runtime_implementation_authorized"] is False
        assert payload["creates_runtime_implementation"] is False
        assert payload["executes_ocr"] is False
        assert payload["executes_render"] is False
        assert payload["mutates_source_ocr_render_pdf_raw"] is False
        assert payload["creates_translation_or_proofreading"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["admits_new_or_broader_fixture"] is False
        assert payload["push_performed"] is False

    for key, value in receipt["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Source-profile lock created: `false`." in summary
    assert "Source-profile parking recorded: `true`." in summary
    assert "Runtime implementation: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary


def test_core_0_1_source_profile_receipt_keeps_runtime_blocked():
    receipt = read_json(RECEIPT)

    assert receipt["remaining_blockers"][0] == "runtime_implementation_requires_future_first_slice_authorization"
    assert "runtime_source_profile_lock_or_runtime_parking_decision_required" in receipt["remaining_blockers"]
    assert receipt["next_possible_packets"][0] == "core_0_1_first_slice_architecture_review_packet_if_separately_authorized"
