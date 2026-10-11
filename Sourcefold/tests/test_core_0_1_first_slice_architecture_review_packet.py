import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_first_slice_architecture_review_packet.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_first_slice_architecture_review_packet_G1_VIRAL_001"
PACKET = OUT_ROOT / "core_0_1_first_slice_architecture_review_packet.json"
REPORT = OUT_ROOT / "core_0_1_first_slice_architecture_review_packet_report.json"
SUMMARY = OUT_ROOT / "core_0_1_first_slice_architecture_review_packet_summary.md"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-ARCHITECTURE-REVIEW-PACKET-001"
HUMAN_DECISION = (
    "c01splpr packet ok; proceed to prepare Core 0.1 first-slice architecture review packet for C01WP-01 "
    "from C01SPLPR; no runtime implementation, no source-profile lock or acceptance beyond C01SPLPR, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit"
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_core_0_1_architecture_review_packet_is_fail_closed():
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
            "c01splpr packet ok",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_architecture_review_packet_scope():
    packet = read_json(PACKET)
    report = read_json(REPORT)
    scope = packet["accepted_gate_1_scope"]

    assert packet["packet_id"] == "C01FSARP-G1-VIRAL-001"
    assert packet["authorization_id"] == AUTHORIZATION_ID
    assert packet["source_profile_lock_or_parking_receipt"] == "C01SPLPR-G1-VIRAL-001"
    assert packet["source_first_slice_design_prep_packet"] == "C01FSDP-G1-VIRAL-001"
    assert packet["source_whole_gate_1_acceptance_decision"] == "G1WGADR-G1-VIRAL-001"
    assert packet["first_slice_id"] == "C01WP-01-phase-1-scaffold-contracts"
    assert packet["human_decision"] == HUMAN_DECISION
    assert scope["page_complete_accepted_pages"] == [f"{page:03d}" for page in range(1, 21)]
    assert scope["fixture_admission_decision"] == "G1FADAR-G1-VIRAL-001"
    assert report["accepted_page_count"] == 20


def test_core_0_1_architecture_review_targets_and_boundaries():
    packet = read_json(PACKET)
    report = read_json(REPORT)

    assert packet["architecture_review_packet_created"] is True
    assert packet["sol_architecture_review_targets_prepared"] is True
    assert packet["terra_critique_targets_prepared"] is True
    assert report["review_target_count"] == 5
    assert {target["target_id"] for target in packet["review_targets"]} == {
        "module_boundary_contract",
        "artifact_identity_contract",
        "lineage_trace_contract",
        "acceptance_matrix_trace_contract",
        "negative_boundary_contract",
    }

    for payload in (packet, report):
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

    for key, value in packet["negative_capability_matrix"].items():
        assert value is False, key

    summary = SUMMARY.read_text(encoding="utf-8-sig")
    assert "Runtime implementation: `false`." in summary
    assert "Runtime source-profile lock: `false`." in summary
    assert "Page 021+ processing/authorization: `false`." in summary


def test_core_0_1_architecture_review_packet_keeps_runtime_blocked():
    packet = read_json(PACKET)

    assert packet["remaining_blockers"][0] == "sol_architecture_review_go_required"
    assert "terra_critique_go_required" in packet["remaining_blockers"]
    assert "acceptance_matrix_claim_to_evidence_mapping_required_for_c01wp_01" in packet["remaining_blockers"]
    assert packet["next_possible_packets"][0] == "human_review_c01fsarp_packet"
