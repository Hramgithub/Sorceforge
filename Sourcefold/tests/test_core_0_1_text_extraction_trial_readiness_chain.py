import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_trial_readiness_chain.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-MACHINE-REVIEW-ACCEPTANCE-001"
HUMAN_DECISION = 'делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6'

STAGES = [
    ("C01RSPLADMR-G1-VIRAL-001", "core_0_1_runtime_source_profile_lock_or_acceptance_machine_review_acceptance", "c01rspladmr_G1_VIRAL_001", "c01rspladmr"),
    ("C01RSPEP-G1-VIRAL-001", "core_0_1_runtime_source_profile_evidence_prep", "c01rspep_G1_VIRAL_001", "c01rspep"),
    ("C01RSPETD-G1-VIRAL-001", "core_0_1_runtime_source_profile_extraction_trial_lock_or_acceptance_decision", "c01rspetd_G1_VIRAL_001", "c01rspetd"),
    ("C01TETAP-G1-VIRAL-001", "core_0_1_text_extraction_trial_authorization_prep", "c01tetap_G1_VIRAL_001", "c01tetap"),
    ("C01TETD-G1-VIRAL-001", "core_0_1_text_extraction_trial_decision", "c01tetd_G1_VIRAL_001", "c01tetd"),
]


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def packet_path(artifact_dir: str, file_base: str) -> Path:
    return TRIAL_ROOT / artifact_dir / f"{file_base}.json"


def test_core_0_1_text_extraction_trial_readiness_chain_is_fail_closed():
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
            "делай 1-5",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_decision.returncode != 0
    assert "exact bounded human decision" in wrong_decision.stderr


def test_core_0_1_text_extraction_trial_readiness_chain_outputs_are_ordered():
    previous = "C01RSPLAD-G1-VIRAL-001"
    for index, (decision_id, canonical, artifact_dir, file_base) in enumerate(STAGES, start=1):
        packet = read_json(packet_path(artifact_dir, file_base))
        assert packet["decision_id"] == decision_id
        assert packet["canonical_packet_name"] == canonical
        assert packet["source_decision"] == previous
        assert packet["readiness_chain_position"] == index
        assert packet["readiness_chain_total"] == 5
        assert packet["sol_terra_replaces_human_review_for_points_1_to_5"] is True
        assert packet["requires_bogdan_call_before_point_6"] is True
        assert packet["scope"]["pages"] == [f"{page:03d}" for page in range(1, 21)]
        assert packet["scope"]["page_021_plus_included"] is False
        previous = decision_id


def test_core_0_1_text_extraction_trial_readiness_chain_blocks_actual_extraction():
    for _decision_id, _canonical, artifact_dir, file_base in STAGES:
        packet = read_json(packet_path(artifact_dir, file_base))
        report = read_json(packet_path(artifact_dir, file_base).with_name(f"{file_base}_report.json"))
        for payload in (packet, report):
            assert payload["actual_text_extraction_authorized_now"] is False
            assert payload["actual_text_extraction_executed"] is False
            assert payload["ocr_execution_performed"] is False
            assert payload["render_execution_performed"] is False
            assert payload["pdf_text_layer_extraction_authorized_now"] is False
            assert payload["runtime_implementation_authorized"] is False
            assert payload["runtime_start_authorized"] is False
            assert payload["runtime_source_profile_lock_created"] is False
            assert payload["runtime_source_profile_acceptance_created"] is False
            assert payload["page_021_plus_authorized_now"] is False
            assert "call_bogdan_before_point_6_required" in payload["remaining_blockers"]

        for key, value in packet["negative_capability_matrix"].items():
            assert value is False, key


def test_core_0_1_text_extraction_trial_readiness_chain_stops_at_point_6_call():
    final_packet = read_json(packet_path("c01tetd_G1_VIRAL_001", "c01tetd"))
    assert final_packet["decision_id"] == "C01TETD-G1-VIRAL-001"
    assert final_packet["point_6_status"] == "blocked_until_bogdan_called_and_separately_authorizes_actual_extraction"
    assert final_packet["next_possible_packets"] == ["call_bogdan_before_point_6_text_extraction_trial"]
