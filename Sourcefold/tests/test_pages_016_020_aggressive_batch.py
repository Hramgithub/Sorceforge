import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_pages_016_020_aggressive_batch.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH = "BA-G1-VIRAL-P016-P020-SEQUENTIAL-AGGRESSIVE-RUN-PREP-001"
PAGES = ("016", "017", "018", "019", "020")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_pages_016_020_sequential_run_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_pages = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", AUTH, "--pages", "016,018"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_pages.returncode != 0
    assert "exactly pages 016,017,018,019,020" in wrong_pages.stderr


def test_pages_016_020_outputs_exist_and_are_ready_for_final_review():
    for page in PAGES:
        batch = read_json(TRIAL_ROOT / f"page_{page}_aggressive_batch_G1_VIRAL_001" / f"page_{page}_aggressive_batch_report.json")
        sem = read_json(TRIAL_ROOT / f"page_{page}_semantic_text_map_G1_VIRAL_001" / f"page_{page}_semantic_text_map.json")
        status = read_json(TRIAL_ROOT / f"gate_1_status_packet_G1_VIRAL_{int(page) - 5:03d}" / "gate_1_status_packet.json")

        assert batch["status"] == "ready_for_bogdan_final_batch_review"
        assert batch["internal_stage_human_review_state"] == "human_review_skipped_by_explicit_authorization"
        assert batch["human_packet_default_assets"] == [
            f"images/page_{page}.png",
            f"page_{page}_semantic_text_map_G1_VIRAL_001/page_{page}_semantic_text_map.md",
        ]
        assert sem["status"] == "semantic_text_map_machine_reviewed_human_review_skipped"
        assert sem["semantic_split_validation"]["valid"] is True
        assert status["page_complete_accepted_pages"][-1] == page


def test_page_016_consumes_page_015_history_continuation():
    sem = read_json(TRIAL_ROOT / "page_016_semantic_text_map_G1_VIRAL_001" / "page_016_semantic_text_map.json")
    first = sem["semantic_units"][0]

    assert first["semantic_role"] == "history_continuation_from_page_015"
    assert first["continuation_from_page"] == "015"
    assert first["heading_level"] is None


def test_page_016_late_history_is_not_consumed_by_keeper_notes():
    sem = read_json(TRIAL_ROOT / "page_016_semantic_text_map_G1_VIRAL_001" / "page_016_semantic_text_map.json")
    units = {unit["unit_id"]: unit for unit in sem["semantic_units"]}

    keeper = units["SU-P016-KEEPER-005"]
    late_history = units["SU-P016-HIST-003"]

    assert "The Keeper can decide if the investigators can glean anything relevant" in keeper["text"]
    assert "In 1961, the island was deemed off limits" not in keeper["text"]
    assert "Throughout the 1970s and 80s" not in keeper["text"]
    assert late_history["semantic_role"] == "history_late_reports_post_keeper"
    assert late_history["text"].startswith("In 1961, the island was deemed off limits")
    assert "Throughout the 1970s and 80s" in late_history["text"]
    assert keeper["semantic_split_contract"]["boundary_kind"] == "explicit_body_end_marker"


def test_page_018_piazza_body_is_not_consumed_by_keeper_notes():
    sem = read_json(TRIAL_ROOT / "page_018_semantic_text_map_G1_VIRAL_001" / "page_018_semantic_text_map.json")
    units = {unit["unit_id"]: unit for unit in sem["semantic_units"]}

    keeper = units["SU-P018-KEEPER-002"]
    piazza = units["SU-P018-WELCOME-004"]

    assert keeper["semantic_role"] == "keeper_notes_helpers"
    assert keeper["text"].endswith("but won't ask for one.")
    assert "The hotel is located right on the town piazza" not in keeper["text"]
    assert piazza["semantic_role"] == "piazza_village_description"
    assert piazza["text"].startswith("The hotel is located right on the town piazza")
    assert piazza["continuation_target"] == "page_019"
    assert keeper["semantic_split_contract"]["boundary_kind"] == "explicit_body_end_marker"


def test_pages_017_019_020_human_review_ok_pages_keep_expected_semantic_controls():
    p017 = read_json(TRIAL_ROOT / "page_017_semantic_text_map_G1_VIRAL_001" / "page_017_semantic_text_map.json")
    p019 = read_json(TRIAL_ROOT / "page_019_semantic_text_map_G1_VIRAL_001" / "page_019_semantic_text_map.json")
    p020 = read_json(TRIAL_ROOT / "page_020_semantic_text_map_G1_VIRAL_001" / "page_020_semantic_text_map.json")

    p017_units = {unit["unit_id"]: unit for unit in p017["semantic_units"]}
    p019_roles = {unit["semantic_role"] for unit in p019["semantic_units"]}
    p020_units = {unit["unit_id"]: unit for unit in p020["semantic_units"]}

    assert p017_units["SU-P017-KEEPER-002"]["semantic_split_contract"]["boundary_kind"] == "callout_extends_to_text_block_end"
    assert "keeper_notes" not in " ".join(p019_roles)
    assert p020_units["SU-P020-KEEPER-002"]["semantic_split_contract"]["boundary_kind"] == "next_segment_start_marker"
    assert "Communication." not in p020_units["SU-P020-KEEPER-002"]["text"]
    assert p020_units["SU-P020-PERLA-005"]["semantic_role"] == "communication"


def test_page_020_marks_page_021_continuation_without_processing_it():
    sem = read_json(TRIAL_ROOT / "page_020_semantic_text_map_G1_VIRAL_001" / "page_020_semantic_text_map.json")
    status = read_json(TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_015" / "gate_1_status_packet.json")

    rumor = sem["semantic_units"][-1]
    assert rumor["continuation_target"] == "page_021"
    assert status["continuation"]["page_021_processed"] is False
    assert status["guardrails"]["page_021_plus_processing"] is False


def test_pages_016_020_keep_broad_guardrails_false():
    for page in PAGES:
        batch = read_json(TRIAL_ROOT / f"page_{page}_aggressive_batch_G1_VIRAL_001" / f"page_{page}_aggressive_batch_report.json")
        for key in [
            "whole_gate_1_acceptance",
            "fixture_admission",
            "source_acceptance_mutation",
            "ocr_execution",
            "render_execution",
            "pdf_parsing_or_text_layer_extraction",
            "raw_mutation",
            "translation",
            "proofreading",
            "renderer_profile_acceptance",
            "implementation",
            "push",
            "page_021_plus_processing",
            "final_human_batch_review_acceptance",
        ]:
            assert batch["guardrails"][key] is False, (page, key)
