import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_acceptance_matrix_trace_review.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_acceptance_matrix_trace_review_G1_VIRAL_001"
REVIEW = OUT_ROOT / "core_0_1_acceptance_matrix_trace_review.json"
REPORT = OUT_ROOT / "core_0_1_acceptance_matrix_trace_review_report.json"
SUMMARY = OUT_ROOT / "core_0_1_acceptance_matrix_trace_review_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-ACCEPTANCE-MATRIX-TRACE-REVIEW-001"
HUMAN_DECISION = (
    "c01fsarp packet ok; proceed to prepare acceptance-matrix trace review for C01WP-01 from C01FSARP; "
    "no runtime implementation, no source-profile lock or acceptance beyond C01SPLPR, no OCR/render/PDF/raw mutation, "
    "no translation/proofreading, no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_acceptance_matrix_trace_review_is_fail_closed():
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
            "c01fsarp packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_acceptance_matrix_trace_review_scope():
    review = read_json(REVIEW)
    report = read_json(REPORT)
    scope = review["accepted_gate_1_scope"]

    assert review["review_id"] == "C01AMTR-G1-VIRAL-001"
    assert review["authorization_id"] == AUTHORIZATION_ID
    assert review["source_architecture_review_packet"] == "C01FSARP-G1-VIRAL-001"
    assert review["source_profile_lock_or_parking_receipt"] == "C01SPLPR-G1-VIRAL-001"
    assert review["source_whole_gate_1_acceptance_decision"] == "G1WGADR-G1-VIRAL-001"
    assert review["first_slice_id"] == "C01WP-01-phase-1-scaffold-contracts"
    assert review["human_decision"] == HUMAN_DECISION
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["accepted_page_count"] == 20


def test_core_0_1_acceptance_matrix_trace_items_and_boundaries():
    review = read_json(REVIEW)
    report = read_json(REPORT)

    assert review["acceptance_matrix_trace_review_created"] is True
    assert review["claim_to_evidence_mapping_prepared"] is True
    assert report["trace_item_count"] == 5
    assert {item["claim_id"] for item in review["trace_items"]} == {
        "accepted_gate_1_scope",
        "module_boundary_contract",
        "artifact_identity_contract",
        "lineage_trace_contract",
        "negative_boundary_contract",
    }

    for payload in (review, report):
        assert payload["runtime_implementation_authorized"] is False
        assert payload["creates_runtime_implementation"] is False
        assert payload["source_profile_lock_created"] is False
        assert payload["source_profile_acceptance_created"] is False
        assert payload["accepts_source_profile_beyond_c01splpr"] is False
        assert payload["executes_ocr"] is False
        assert payload["executes_render"] is False
        assert payload["mutates_source_ocr_render_pdf_raw"] is False
        assert payload["creates_translation_or_proofreading"] is False
        assert payload["processes_page_021_plus"] is False
        assert payload["admits_new_or_broader_fixture"] is False
        assert payload["push_performed"] is False

    for key, value in review["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Runtime implementation: `false`." in summary
    assert "Runtime source-profile lock: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary


def test_core_0_1_acceptance_matrix_trace_review_keeps_runtime_blocked():
    review = read_json(REVIEW)

    assert review["remaining_blockers"][0] == "human_review_c01amtr_required"
    assert "runtime_source_profile_lock_or_runtime_parking_decision_required" in review["remaining_blockers"]
    assert "first_slice_runtime_authorization_required" in review["remaining_blockers"]
    assert review["next_possible_packets"][0] == "human_review_c01amtr_packet"
