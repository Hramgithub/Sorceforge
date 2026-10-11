import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.ocr_benchmark_candidate_contract import (  # noqa: E402
    OCR_BENCHMARK_CANDIDATE_SCHEMA_VERSION,
    require_ocr_benchmark_candidate_contract,
    validate_ocr_benchmark_candidate_contract,
)


def raw_outputs():
    return {"txt_sha256": "A", "tsv_sha256": "B", "log_sha256": "C", "stderr_sha256": "D"}


def run(**overrides):
    payload = {
        "ocr_profile_id": "OBR-G1-VIRAL-001",
        "threshold_changed_after_results": False,
        "pdf_text_layer_used": False,
        "raw_outputs_mutated": False,
        "ocr_acceptance_created": False,
        "unauthorized_rerun": False,
        "zones": [
            {
                "zone_id": "z01",
                "page_id": "PG-G1-VIRAL-P005",
                "zone_role": "ocr_candidate",
                "crop_sha256": "CROP",
                "raw_outputs": raw_outputs(),
            },
            {
                "zone_id": "z02",
                "page_id": "PG-G1-VIRAL-P001",
                "zone_role": "visual_qc_only",
                "crop_sha256": "VISUAL",
                "raw_outputs": {},
            },
        ],
    }
    payload.update(overrides)
    return payload


def test_ocr_benchmark_candidate_contract_accepts_exact_candidates_and_visual_qc():
    result = validate_ocr_benchmark_candidate_contract(run=run(), admitted_zone_ids={"z01", "z02"})

    assert result["schema_version"] == OCR_BENCHMARK_CANDIDATE_SCHEMA_VERSION
    assert result["status"] == "passed"


def test_ocr_benchmark_candidate_contract_blocks_leakage_and_bad_outputs():
    bad_run = run(
        pdf_text_layer_used=True,
        raw_outputs_mutated=True,
        zones=[
            {"zone_id": "z01", "page_id": "PG", "zone_role": "ocr_candidate", "crop_sha256": "CROP", "raw_outputs": {}},
            {"zone_id": "z02", "page_id": "PG", "zone_role": "visual_qc_only", "crop_sha256": "CROP", "raw_outputs": raw_outputs()},
        ],
    )

    result = validate_ocr_benchmark_candidate_contract(run=bad_run, admitted_zone_ids={"z01", "z02"})

    finding_ids = {finding["finding_id"] for finding in result["findings"]}
    assert result["status"] == "blocked"
    assert "ocr_benchmark_pdf_text_layer_leakage" in finding_ids
    assert "ocr_benchmark_raw_output_mutation" in finding_ids
    assert "ocr_benchmark_missing_raw_output_hashes" in finding_ids
    assert "ocr_benchmark_visual_qc_has_ocr_output" in finding_ids


def test_ocr_benchmark_candidate_consumer_fails_closed_on_unadmitted_zone():
    with pytest.raises(ValueError, match="OCR benchmark candidate contract"):
        require_ocr_benchmark_candidate_contract(
            run=run(),
            admitted_zone_ids={"z01"},
            consumer="ocr_acceptance",
        )
