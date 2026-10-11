import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_runtime_source_profile_lock_or_acceptance_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_G1_VIRAL_001"
DECISION = OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision.json"
REPORT = OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_report.json"
SUMMARY = OUT_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-DECISION-001"
HUMAN_DECISION = (
    "c01rsad packet ok; proceed to prepare Core 0.1 runtime source-profile lock-or-acceptance decision for C01WP-01 "
    "from C01RSAD; no runtime implementation, no runtime start/execution, no OCR/render/PDF/raw mutation, "
    "no translation/proofreading, no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_runtime_source_profile_lock_or_acceptance_decision_is_fail_closed():
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
            "c01rsad packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_runtime_source_profile_lock_or_acceptance_decision_scope():
    decision = read_json(DECISION)
    report = read_json(REPORT)
    scope = decision["accepted_gate_1_scope"]

    assert decision["decision_id"] == "C01RSPLAD-G1-VIRAL-001"
    assert decision["authorization_id"] == AUTHORIZATION_ID
    assert decision["canonical_packet_name"] == "core_0_1_runtime_source_profile_lock_or_acceptance_decision"
    assert decision["source_first_slice_runtime_authorization_decision"] == "C01RSAD-G1-VIRAL-001"
    assert decision["source_first_slice_runtime_authorization_prep"] == "C01RSAP-G1-VIRAL-001"
    assert decision["source_runtime_source_profile_lock_or_parking_decision"] == "C01RSPLP-G1-VIRAL-001"
    assert decision["source_acceptance_matrix_trace_review"] == "C01AMTR-G1-VIRAL-001"
    assert decision["source_architecture_review_packet"] == "C01FSARP-G1-VIRAL-001"
    assert decision["source_profile_lock_or_parking_receipt"] == "C01SPLPR-G1-VIRAL-001"
    assert decision["source_whole_gate_1_acceptance_decision"] == "G1WGADR-G1-VIRAL-001"
    assert decision["first_slice_id"] == "C01WP-01-phase-1-scaffold-contracts"
    assert decision["human_decision"] == HUMAN_DECISION
    assert decision["human_review_consumed"] == "c01rsad_packet_ok"
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["accepted_page_count"] == 20


def test_core_0_1_runtime_source_profile_lock_or_acceptance_decision_grants_no_profile_lock_or_acceptance():
    decision = read_json(DECISION)
    report = read_json(REPORT)
    outcome = decision["runtime_source_profile_decision_outcome"]

    assert decision["runtime_source_profile_lock_or_acceptance_decision_recorded"] is True
    assert outcome["decision"] == "no_runtime_source_profile_lock_or_acceptance"
    assert outcome["runtime_source_profile_lock_granted"] is False
    assert outcome["runtime_source_profile_acceptance_granted"] is False
    assert outcome["runtime_source_profile_remains_parked"] is True
    assert outcome["blocks_runtime_implementation"] is True

    for payload in (decision, report):
        assert payload["runtime_source_profile_lock_granted"] is False
        assert payload["runtime_source_profile_acceptance_granted"] is False
        assert payload["runtime_source_profile_lock_created"] is False
        assert payload["runtime_source_profile_acceptance_created"] is False
        assert payload["runtime_start_authorized"] is False
        assert payload["runtime_execution_authorized"] is False
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

    for key, value in decision["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Runtime source-profile lock granted: `false`." in summary
    assert "Runtime source-profile acceptance granted: `false`." in summary
    assert "Runtime source-profile remains parked: `true`." in summary
    assert "Runtime implementation remains blocked by profile decision: `true`." in summary


def test_core_0_1_runtime_source_profile_lock_or_acceptance_decision_keeps_implementation_blocked():
    decision = read_json(DECISION)

    assert "human_review_c01rsad_required" not in decision["remaining_blockers"]
    assert "runtime_source_profile_lock_or_acceptance_requires_separate_authorization" not in decision["remaining_blockers"]
    assert decision["remaining_blockers"][0] == "runtime_source_profile_lock_or_acceptance_not_granted_blocks_implementation"
    assert "runtime_implementation_authorization_required" in decision["remaining_blockers"]
    assert "runtime_start_execution_requires_separate_authorization" in decision["remaining_blockers"]
    assert decision["next_possible_packets"][0] == "human_review_c01rsplad_packet"
