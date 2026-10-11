import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "source_reconstruction_prep_G1_VIRAL_001"
RUN_ROOT = TRIAL_ROOT / "source_reconstruction_review_G1_VIRAL_001"
MATRIX_RAW_ROOT = TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001" / "raw_outputs"
SCRIPT = ROOT / "scripts" / "build_source_reconstruction_review_package.py"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def test_prep_artifacts_preserve_non_execution_boundary():
    manifest = read_json(PREP_ROOT / "source_reconstruction_admitted_manifest.json")
    dry_run = read_json(PREP_ROOT / "source_reconstruction_dry_run_report.json")

    assert manifest["status"] == "source_reconstruction_prep_only"
    assert dry_run["status"] == "source_reconstruction_prep_only"
    assert dry_run["candidate_text_created"] is False
    assert dry_run["ocr_executed"] is False
    assert dry_run["pdf_opened_or_parsed"] is False
    assert dry_run["source_acceptance"] is False
    assert dry_run["gate_1_advancement"] is False
    assert dry_run["human_review_required_now"] is False


def test_admitted_manifest_is_exact_and_requires_source_refs():
    manifest = read_json(PREP_ROOT / "source_reconstruction_admitted_manifest.json")
    regions = manifest["admitted_regions"]

    assert manifest["manifest_id"] == "SRA-G1-VIRAL-001"
    assert len(regions) == 7
    assert sum(1 for region in regions if region["route_class"] == "ocr_candidate") == 5
    assert sum(1 for region in regions if region["route_class"] == "visual_qc_only") == 2
    assert all(region["candidate_text_allowed_in_prep"] is False for region in regions)
    assert all((ROOT / region["page_image"]).exists() for region in regions)
    assert all(region["predecessor_zone_id"] for region in regions)
    assert all(region["predecessor_crop_sha256"] for region in regions)

    route_keys = {
        (
            region["sample_id"],
            region["page_id"],
            region["region_id"],
            region["predecessor_zone_id"],
            region["predecessor_crop_sha256"],
        )
        for region in regions
    }
    assert len(route_keys) == len(regions)

    for region in regions:
        if region["route_class"] == "ocr_candidate":
            assert region["execution_authorization_required"] == "BA-G1-VIRAL-SOURCE-RECON-RUN-001"
        if region["route_class"] == "visual_qc_only":
            assert region["execution_authorization_required"] is None


def test_dry_run_report_binds_protocol_manifest_and_predecessors():
    manifest = read_json(PREP_ROOT / "source_reconstruction_admitted_manifest.json")
    dry_run = read_json(PREP_ROOT / "source_reconstruction_dry_run_report.json")

    assert dry_run["protocol"]["id"] == "SRP-G1-VIRAL-001"
    assert dry_run["admitted_manifest"]["id"] == manifest["manifest_id"]
    assert dry_run["admitted_region_count"] == len(manifest["admitted_regions"])
    assert all(check["passed"] for check in dry_run["checks"])

    expected_predecessors = {
        "pre_ocr_map_bundle",
        "gold_sample_manifest",
        "ocr_candidate_manifest",
        "remediation_review",
        "ocr_admission_candidate",
        "evidence_rollup",
        "negative_checks",
    }
    checked = {
        check["name"].split(" hash matches", 1)[0]
        for check in dry_run["checks"]
        if " hash matches " in check["name"]
    }
    assert checked == expected_predecessors


def test_script_fails_closed_without_dry_run_or_run_authorization():
    no_args = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert no_args.returncode != 0
    assert "pass --dry-run" in no_args.stderr

    execute = subprocess.run(
        [sys.executable, str(SCRIPT), "--execute", "--authorization-id", "BA-G1-VIRAL-SOURCE-RECON-PREP-001"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert execute.returncode != 0
    assert "requires BA-G1-VIRAL-SOURCE-RECON-RUN-001" in execute.stderr

    stale_hash = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--execute",
            "--authorization-id",
            "BA-G1-VIRAL-SOURCE-RECON-RUN-001",
            "--admitted-manifest-sha256",
            "BAD",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert stale_hash.returncode != 0
    assert "admitted manifest hash argument does not match" in stale_hash.stderr


def test_script_does_not_import_pdf_ocr_or_old_project_dependencies():
    source = SCRIPT.read_text(encoding="utf-8")
    forbidden = [
        "fitz",
        "pymupdf",
        "pytesseract",
        "subprocess.run",
        "D:\\\\NRI\\\\translator",
        "wormsign",
    ]
    for token in forbidden:
        assert token not in source


def test_source_reconstruction_run_package_is_human_review_only():
    run_manifest = read_json(RUN_ROOT / "source_reconstruction_run_manifest.json")
    precheck = read_json(RUN_ROOT / "source_reconstruction_precheck.json")

    assert run_manifest["authorization_id"] == "BA-G1-VIRAL-SOURCE-RECON-RUN-001"
    assert run_manifest["status"] == "candidate_review_blocked_for_remediation"
    assert run_manifest["ocr_executed"] is False
    assert run_manifest["pdf_opened_or_parsed"] is False
    assert run_manifest["candidate_text_created"] is True
    assert run_manifest["human_review_ready"] is False
    assert run_manifest["human_review_blocked"] is True
    assert run_manifest["accepted_source_text_created"] is False
    assert run_manifest["source_acceptance"] is False
    assert run_manifest["qa_acceptance"] is False
    assert run_manifest["gate_1_advancement"] is False
    assert len(run_manifest["candidate_records"]) == 5
    assert len(run_manifest["visual_qc_queue"]) == 2
    assert precheck["status"] == "evidence_precheck_only"
    assert precheck["human_review_ready"] is False
    assert precheck["human_review_blocked"] is True
    assert all(finding["blocking_for_human_review"] is True for finding in precheck["findings"])
    assert all(check["passed"] for check in precheck["checks"])


def test_candidate_records_match_selected_raw_ocr_evidence():
    run_manifest = read_json(RUN_ROOT / "source_reconstruction_run_manifest.json")

    for record in run_manifest["candidate_records"]:
        text_path = MATRIX_RAW_ROOT / (
            f"{record['sample_id']}__{record['predecessor_zone_id']}__{record['selected_config']}.txt"
        )
        tsv_path = MATRIX_RAW_ROOT / (
            f"{record['sample_id']}__{record['predecessor_zone_id']}__{record['selected_config']}.tsv"
        )
        assert text_path.exists()
        assert tsv_path.exists()
        assert sha256_file(text_path) == record["candidate_text_sha256"]
        assert sha256_file(tsv_path) == record["candidate_tsv_sha256"]
        assert text_path.read_text(encoding="utf-8-sig").strip() == record["candidate_text"]
        assert record["predecessor_crop_sha256"]
        assert record["input_crop"]


def test_human_facing_package_exposes_crop_identity_and_blocker_status():
    package = (RUN_ROOT / "raw_ocr_candidate_for_human_review.md").read_text(encoding="utf-8-sig")
    run_manifest = read_json(RUN_ROOT / "source_reconstruction_run_manifest.json")

    assert "blocked_for_remediation" in package
    assert "Do not request source approval from Bogdan yet." in package
    for record in run_manifest["candidate_records"]:
        assert record["region_admission_id"] in package
        assert record["predecessor_crop_sha256"] in package
