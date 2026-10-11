import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_page_014_aggressive_batch.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH = "BA-G1-VIRAL-PAGE-014-AGGRESSIVE-BATCH-001"

TRIAGE = TRIAL_ROOT / "page_014_triage_G1_VIRAL_001" / "page_014_triage_packet.json"
TEXT = TRIAL_ROOT / "page_014_text_extraction_G1_VIRAL_001" / "page_014_text_extraction_packet.json"
SEM = TRIAL_ROOT / "page_014_semantic_text_map_G1_VIRAL_001" / "page_014_semantic_text_map.json"
PCRP = TRIAL_ROOT / "page_complete_review_p014_G1_VIRAL_001" / "page_complete_review_report.json"
PCA = TRIAL_ROOT / "page_complete_acceptance_p014_G1_VIRAL_001" / "page_complete_acceptance_report.json"
STATUS = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_009" / "gate_1_status_packet.json"
BATCH = TRIAL_ROOT / "page_014_aggressive_batch_G1_VIRAL_001" / "page_014_aggressive_batch_report.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_page_014_aggressive_batch_is_fail_closed():
    no_execute = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, capture_output=True, text=True)
    assert no_execute.returncode != 0
    assert "fail-closed" in no_execute.stderr

    wrong_auth = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-PAGE-014-TRIAGE-001"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTH in wrong_auth.stderr


def test_internal_stages_record_skipped_human_review_and_sol_terra():
    for path in [TRIAGE, TEXT, SEM, PCRP, PCA, STATUS]:
        payload = read_json(path)
        gate = payload["review_gate"]
        assert gate["status"] == "passed"
        assert gate["human_review_state"] == "human_review_skipped_by_explicit_authorization"
        assert gate["delegated_review_state"] == "review_delegated_to_Sol_Terra"
        assert gate["sol"]["status"] == "OK"
        assert gate["terra"]["status"] == "OK"
        serialized = json.dumps(payload)
        assert "Bogdan approved" not in serialized
        assert "p014 triage ok" not in serialized
        assert "p014 text ok" not in serialized
        assert "p014 semantic map ok" not in serialized


def test_page_014_scope_and_sequence_are_hash_bound():
    triage = read_json(TRIAGE)
    text = read_json(TEXT)
    sem = read_json(SEM)
    pcrp = read_json(PCRP)
    pca = read_json(PCA)
    status = read_json(STATUS)

    predecessors = {item["name"]: item for item in triage["predecessors"]}
    assert predecessors["post_p013_status_route_packet"]["sha256"] == "EED84F376597007FECA15774E4DCFEDEFC3F619278985BEB11E0D46295565725"
    assert predecessors["p013_final_batch_review"]["sha256"] == "3C9AF88656119DE46753B6F8454B5BE36C331BE212E3A133A3E5BF8F163D63F4"
    assert predecessors["page_014_image"]["sha256"] == "24271ACED987DDF04850975ABE27D3B9BD4D48C74D81226E381D98D5E82948EA"
    assert text["predecessor"]["package_id"] == "P014TR-G1-VIRAL-001"
    assert sem["predecessor"]["package_id"] == "P014TXT-G1-VIRAL-001"
    assert pcrp["predecessor"]["package_id"] == "P014SEM-G1-VIRAL-001"
    assert pca["predecessor"]["package_id"] == "PCRP-G1-VIRAL-P014-001"
    assert status["predecessor"]["package_id"] == "P014PCA-G1-VIRAL-001"
    assert pca["accepted_pages"] == ["014"]


def test_page_014_text_evidence_crops_have_explicit_contracts():
    triage = read_json(TRIAGE)
    blocks = {block["block_id"]: block for block in triage["review_blocks"]}

    assert len(blocks) == 9
    assert [block["block_id"] for block in triage["visual_only_blocks"]] == ["P014-V001"]
    for block in blocks.values():
        assert block["crop_contract"]["context_allowed"] is False
        assert block["crop_contract"]["coverage"] == "full_text_region"

    assert blocks["P014-B001"]["role"] == "spektral_krew_gear_title_and_carried_intro"
    assert blocks["P014-B004"]["role"] == "keeper_notes_emf_meter"
    assert blocks["P014-B007"]["role"] == "static_base_station_and_notes"
    assert blocks["P014-B009"]["crop_box_px"][0] >= 1260


def test_page_014_semantic_map_preserves_heading_depth():
    sem = read_json(SEM)
    units = {unit["unit_id"]: unit for unit in sem["units"]}

    assert units["SU-P014-GEAR-001"]["text"] == "Spektral Krew Gear"
    assert units["SU-P014-GEAR-001"]["heading_level"] == "h2"
    assert units["SU-P014-GEAR-002"]["text"] == "Carried"
    assert units["SU-P014-GEAR-002"]["heading_level"] == "h3"
    assert units["SU-P014-GEAR-020"]["text"] == "Static"
    assert units["SU-P014-GEAR-020"]["heading_level"] == "h3"

    h4_headings = {
        "Equipment Satchel",
        "Handheld Night Vision Cameras (2)",
        "EMF Meter",
        "Keeper's Notes",
        "Spirit Box",
        "EVP Recorder SCD1",
        "FLIR Camera for Smartphone",
        "Base Station",
        "Cellular Wi-Fi Repeaters/Transmitters (2)",
        "UPS Batteries (3)",
        "Night Vision Cameras (6)",
        "Drone",
    }
    for unit in sem["units"]:
        if unit["unit_type"] == "heading" and unit["text"] in h4_headings:
            assert unit["heading_level"] == "h4"
    assert sem["unit_count"] == 35
    assert sem["semantic_split_validation"]["valid"] is True

    for unit_id in ["SU-P014-GEAR-011", "SU-P014-GEAR-015", "SU-P014-GEAR-025", "SU-P014-GEAR-029"]:
        assert units[unit_id]["display_style"] == "callout_body"
        assert units[unit_id]["semantic_split_contract"]["boundary_kind"] == "callout_extends_to_text_block_end"


def test_text_extraction_is_manual_and_no_ocr_was_run():
    text = read_json(TEXT)

    assert text["extraction_method"] == "manual_from_text_evidence_region"
    assert text["ocr_executed"] is False
    assert text["logical_reading_order"] == [f"P014-TEXT-{i:03d}" for i in range(1, 10)]


def test_page_015_and_broad_capabilities_remain_blocked():
    status = read_json(STATUS)
    pca = read_json(PCA)
    batch = read_json(BATCH)

    assert status["page_complete_accepted_pages"] == [f"{i:03d}" for i in range(1, 15)]
    assert status["remaining_page_complete_pages_unstarted"] == ["015", "016", "017", "018", "019", "020"]
    assert status["recommended_next_candidate"] == "page_015_triage_readiness_not_authorized"
    for payload in [status, pca, batch]:
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
            "page_015_plus_processing",
        ]:
            assert payload["guardrails"][key] is False, key


def test_final_bundle_is_the_only_human_review_target():
    batch = read_json(BATCH)

    assert batch["status"] == "ready_for_bogdan_final_batch_review"
    assert batch["human_review_model"] == "final_bundle_and_post_p014_status_only"
    assert batch["internal_stage_human_review_state"] == "human_review_skipped_by_explicit_authorization"
    assert batch["decision_options"] == ["p014 aggressive batch ok", "hold p014 batch: <reason>"]
