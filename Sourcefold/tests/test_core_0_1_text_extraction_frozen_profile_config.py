import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_core_0_1_text_extraction_frozen_profile_config.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_frozen_profile_config_G1_VIRAL_001"
CONFIG = OUT_ROOT / "core_0_1_text_extraction_frozen_profile_config.json"
REPORT = OUT_ROOT / "core_0_1_text_extraction_frozen_profile_config_report.json"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FROZEN-PROFILE-CONFIG-001"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def test_frozen_profile_config_is_fail_closed():
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
            "делай",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert wrong_auth.returncode != 0
    assert AUTHORIZATION_ID in wrong_auth.stderr


def test_frozen_profile_config_tuple_and_source_binding():
    config = read_json(CONFIG)
    report = read_json(REPORT)

    assert config["config_id"] == "C01TEFPC-G1-VIRAL-001"
    assert config["authorization_id"] == AUTHORIZATION_ID
    assert config["source_candidate_profile_decision"] == "C01TECPD-G1-VIRAL-001"
    assert config["profile_id"] == "trim_mask_psm4"
    assert config["profile_tuple"] == {
        "candidate_id": "trim_mask_psm4",
        "preprocessing_variant": "edge_mask_trim",
        "tesseract_psm": 4,
        "tesseract_oem": 1,
        "language": "eng",
        "strategy": "full_column",
    }
    assert config["ocr_engine"]["args"] == ["-l", "eng", "--oem", "1", "--psm", "4", "txt", "tsv"]
    assert report["config_can_drive_replay"] is True
    assert (
        config["verified_inputs"]["C01TECPD-G1-VIRAL-001.packet"]["sha256"]
        == "EE61C584158FDB825E4C567DE86C8B47748B0FB0FE6F05B3BE7DD0E569C19B39"
    )


def test_frozen_profile_config_boundaries():
    config = read_json(CONFIG)
    report = read_json(REPORT)

    for payload in (config, report):
        assert payload["ocr_execution_performed"] is False
        assert payload["source_profile_acceptance_created"] is False
        assert payload["runtime_source_profile_lock_created"] is False
        assert payload["accepted_text_mutation_performed"] is False
        assert payload["semantic_text_mutation_performed"] is False
        assert payload["page_status_mutation_performed"] is False
        assert payload["page_021_plus_included"] is False
        assert payload["push_performed"] is False

    assert config["page_016_plus_included"] is False
    assert config["allowed_inputs"]["pages"] == ["009", "010", "015"]
    assert config["allowed_inputs"]["references"]["015"] == "reference_text_map_not_ocr_verified"
    assert "page_021_plus" in config["forbidden_inputs"]
    for key, value in config["negative_capability_matrix"].items():
        assert value is False, key
