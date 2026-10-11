from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_recovery_audit_G1_VIRAL_001"

LANE_ID = "C01TEP002ASSETREC-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-RECOVERY-AUDIT-001"
HUMAN_DECISION = "Ок иди по плану, ты оркестратор, следи чтоб все было сделанл"
PAGE = "002"
CREATION_HEAD = "abdd13ac"
OUT_OF_SCOPE_PAGES = [
    "001",
    "003",
    "004",
    "005",
    "006",
    "007",
    "008",
    "009",
    "010",
    "011",
    "012",
    "013",
    "014",
    "015",
    "016",
    "017",
    "018",
    "019",
    "020",
    "021+",
]

PINNED_INPUTS = {
    "C01TEBRIDGEAUD020-G1-VIRAL-001.report": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
        / "bridge_page_audit_001_008_014_019_report.json",
        "25CF7B2DB7864EFD1FA7B58095905724FFE087E84E34BDEB81FB34D404008E02",
    ),
    "C01TEBRIDGEAUD020-G1-VIRAL-001.summary": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
        / "bridge_page_audit_001_008_014_019_summary.md",
        "744A454B62EAA08F197276C770C4CEAEF496FF7ED173E1D9B909A65CD64A6639",
    ),
    "C01TEBRIDGEAUD020-G1-VIRAL-001.manifest": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_audit_001_008_014_019_G1_VIRAL_001"
        / "bridge_page_audit_001_008_014_019_manifest.md",
        "D69D1286238213ECDB957667428D0FC721C352DB44FB737B34E5BC7B26E6B738",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.report": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "bridge_page_remediation_run_001_008_014_019_report.json",
        "6A135FCBB5337BDADD4F59C23BB3F79A1FB077450524BADE7C90E8EA5FCA60CB",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.summary": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "bridge_page_remediation_run_001_008_014_019_summary.md",
        "3161D2355BBA24C25E727E1914BCCDF8B49FCC56BBD979C818D6668B0F8A2124",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.manifest": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "bridge_page_remediation_run_001_008_014_019_manifest.md",
        "BBC6A64419BC7B23EFCCF429D6DA17247B05CCAE3FE0EAF81FE593D9BE1362E5",
    ),
    "C01TEBRIDGESCOREAUD020-G1-VIRAL-001.report": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008_G1_VIRAL_001"
        / "bridge_page_scoring_reference_audit_003_008_report.json",
        "7927E9B5C24C6689C6321D1CBA4FB71BFE6F4107C622B4824638C4AC068D95D5",
    ),
    "C01TEBRIDGESCOREAUD020-G1-VIRAL-001.summary": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008_G1_VIRAL_001"
        / "bridge_page_scoring_reference_audit_003_008_summary.md",
        "85A0725A721E9C0EA25BCBAB146EFD643CEB7DDE1E2337492AF3E27D686FB443",
    ),
    "C01TEBRIDGESCOREAUD020-G1-VIRAL-001.manifest": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008_G1_VIRAL_001"
        / "bridge_page_scoring_reference_audit_003_008_manifest.md",
        "0DE9E1D3F3EEA7D734841DBD3D4E897B2355A561AFC07A4EE8FC92529F5C1E2D",
    ),
    "P002.page_image": (
        TRIAL_ROOT / "images" / "page_002.png",
        "ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9",
    ),
    "P002.page_complete_acceptance.report": (
        TRIAL_ROOT / "page_complete_acceptance_p002_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C",
    ),
    "P002.page_complete_review.report": (
        TRIAL_ROOT / "page_complete_review_p002_G1_VIRAL_001" / "page_complete_review_report.json",
        "D84968D6E839D2CF07603FDFD4A7D05112B7F8DBE1984E21788F1BA253C23BB9",
    ),
    "P002.page_complete_review.manifest": (
        TRIAL_ROOT / "page_complete_review_p002_G1_VIRAL_001" / "page_complete_review_manifest.md",
        "9323EE68AED33840FD8C9031630749CED4709A7A1499965BD491B22E145E9D5E",
    ),
    "P002.page_map_readiness.report": (
        TRIAL_ROOT / "page_map_readiness_p002_G1_VIRAL_001" / "page_map_readiness_report.json",
        "3F957442194211F6F0EC39775ED292DEF126222E98EEFB5BFFD1530D8EA702D6",
    ),
    "P002.page_map_readiness.manifest": (
        TRIAL_ROOT / "page_map_readiness_p002_G1_VIRAL_001" / "page_map_readiness_manifest.md",
        "5AB662AF36355A75F73758EF4B73BF13F0315986AF40B2F9234BBE84B489173A",
    ),
    "P002.source_reconstruction_next_slice.report": (
        TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002" / "source_reconstruction_next_slice_report.json",
        "1A9A693883277635B02E02F143284280C1FBA1F928FF950843586B8A1C5EC224",
    ),
    "P002.source_reconstruction_next_slice.manifest": (
        TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_002" / "source_reconstruction_next_slice_manifest.md",
        "B4D8E6AA3D08DFD78D16F72FD3774B57051F4AABCE32062C3B36E924466C6DCD",
    ),
    "P002.assisted_draft.report": (
        TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001" / "source_reconstruction_p002_assisted_draft_report.json",
        "296763B5942B937B66822E4988C30FF5B96FBFBFF08952987FA5E8D22CE07F05",
    ),
    "P002.assisted_draft.manifest": (
        TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001" / "source_reconstruction_p002_assisted_draft_manifest.md",
        "D6E50079093DEDA2F178D744E19DA29650CF3B2667B1F5418D4CB02F018E4280",
    ),
    "P002.assisted_draft.verify.report": (
        TRIAL_ROOT
        / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"
        / "source_reconstruction_p002_assisted_draft_verify_report.json",
        "BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52",
    ),
    "P002.assisted_draft.verify.manifest": (
        TRIAL_ROOT
        / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"
        / "source_reconstruction_p002_assisted_draft_verify_manifest.md",
        "B6E3D871FCA061D1672CB5E73A1BFF6C73AAE7D0C7F8B2A7044BD451FAC9159A",
    ),
    "P002.completion_and_next_review.report": (
        TRIAL_ROOT
        / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
        / "p002_completion_and_next_review_report.json",
        "A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F",
    ),
    "P002.completion_and_next_review.manifest": (
        TRIAL_ROOT
        / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001"
        / "p002_completion_and_next_review_manifest.md",
        "8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6",
    ),
    "P002.corrected_crop_ref.1": (
        TRIAL_ROOT
        / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001"
        / "corrected_region_refs"
        / "1_SRAD-G1-VIRAL-002-R01__SRAD-G1-VIRAL-002-R01-C01.png",
        "D281969D790D4BF7661DDF841924FA6A0B9F8965088580A0FA89B64DA9599E6D",
    ),
    "P002.corrected_crop_ref.2": (
        TRIAL_ROOT
        / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001"
        / "corrected_region_refs"
        / "2_SRAD-G1-VIRAL-002-R02__SRAD-G1-VIRAL-002-R02-C01.png",
        "D167F253964076DA67D7A6D625BB236875CA05E634710C10F1FD816C46B1BE4B",
    ),
}

CURRENT_COMPLETION_BUILDER_HASH = "F67C4B4D06F3A984E864D90E5DFBA4CC4FE9CE60DC50D2FEEAAD8FDBF70B9938"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def git_head() -> str:
    result = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build P002 source asset recovery audit.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 source asset recovery audit is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 source asset recovery audit requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 source asset recovery audit requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> dict[str, dict[str, str]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    return {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}


def build_report(verified_inputs: dict[str, dict[str, str]]) -> dict[str, Any]:
    bridge_audit = read_json(PINNED_INPUTS["C01TEBRIDGEAUD020-G1-VIRAL-001.report"][0])
    remediation = read_json(PINNED_INPUTS["C01TEBRIDGEREM020-G1-VIRAL-001.report"][0])
    completion = read_json(PINNED_INPUTS["P002.completion_and_next_review.report"][0])
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    p002_audit_entry = next(item for item in bridge_audit["page_audit"] if item["page"] == PAGE)
    p002_remediation_entry = next(item for item in remediation["page_entries"] if item["page"] == PAGE)
    recorded_completion_builder_hash = completion["generator"]["script_sha256"]
    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_source_asset_recovery_audit_completed_report_only_no_ocr_no_mutation",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "page": PAGE,
        "scope": "page_002_only",
        "out_of_scope_pages_rejected": OUT_OF_SCOPE_PAGES,
        "input_lane_ids": [
            "C01TEBRIDGEAUD020-G1-VIRAL-001",
            "C01TEBRIDGEREM020-G1-VIRAL-001",
            "C01TEBRIDGESCOREAUD020-G1-VIRAL-001",
            "SRNS-G1-VIRAL-002",
            "SRAD-G1-VIRAL-002",
            "SRADV-G1-VIRAL-002",
            "P002C-G1-VIRAL-002",
            "P002PCA-G1-VIRAL-001",
        ],
        "verified_inputs": verified_inputs,
        "bridge_blocker_before_audit": p002_audit_entry["next_route"],
        "bridge_remediation_route_family": p002_remediation_entry["route_family"],
        "bridge_blocker_cleared": False,
        "asset_recovery_classification": "recoverable_from_pinned_page_image_and_source_reconstruction_artifacts",
        "review_assets_missing_in_original_page_complete_review": p002_audit_entry["missing_assets"] == ["review_assets"],
        "alternate_page_image_available": True,
        "corrected_crop_refs_available": True,
        "human_verified_text_available": True,
        "source_acceptance_chain_available": completion.get("source_acceptance") is True,
        "source_acceptance_chain_authority_risk": "stale_generator_hash_in_completion_artifact",
        "recorded_completion_builder_hash": recorded_completion_builder_hash,
        "current_completion_builder_hash": CURRENT_COMPLETION_BUILDER_HASH,
        "completion_builder_hash_stale": recorded_completion_builder_hash != CURRENT_COMPLETION_BUILDER_HASH,
        "recovered_asset_candidates": [
            {
                "asset_id": "page_002_full_page_image",
                "asset_class": "page_image",
                "path": verified_inputs["P002.page_image"]["path"],
                "sha256": verified_inputs["P002.page_image"]["sha256"],
                "materialized_by_this_lane": False,
            },
            {
                "asset_id": "page_002_corrected_crop_1",
                "asset_class": "corrected_crop_reference",
                "path": verified_inputs["P002.corrected_crop_ref.1"]["path"],
                "sha256": verified_inputs["P002.corrected_crop_ref.1"]["sha256"],
                "materialized_by_this_lane": False,
            },
            {
                "asset_id": "page_002_corrected_crop_2",
                "asset_class": "corrected_crop_reference",
                "path": verified_inputs["P002.corrected_crop_ref.2"]["path"],
                "sha256": verified_inputs["P002.corrected_crop_ref.2"]["sha256"],
                "materialized_by_this_lane": False,
            },
        ],
        "recovery_resolution": "recoverable_but_not_materialized",
        "allowed_next_action": "separate_bounded_p002_source_asset_materialization_authorization",
        "review_assets_materialized": False,
        "ocr_execution_performed": False,
        "tesseract_invoked": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "production_ready": False,
        "production_assembly_authorized": False,
        "production_assembly_created": False,
        "acceptance_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "fixture_admission_performed": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "push_performed": False,
        "downstream_execution_performed": False,
    }


def output_hashes(paths: list[Path]) -> dict[str, dict[str, str]]:
    return {
        path.relative_to(OUT_ROOT).as_posix(): {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
        for path in paths
    }


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = build_report(verified_inputs)
    report_path = OUT_ROOT / "p002_source_asset_recovery_audit_report.json"
    summary_path = OUT_ROOT / "p002_source_asset_recovery_audit_summary.md"
    manifest_path = OUT_ROOT / "p002_source_asset_recovery_audit_manifest.md"
    write_json(report_path, report)
    summary = [
        "# P002 Source Asset Recovery Audit - C01TEP002ASSETREC-G1-VIRAL-001",
        "",
        "Status: `p002_source_asset_recovery_audit_completed_report_only_no_ocr_no_mutation`",
        "",
        "Page `002` is recoverable from pinned existing page image and source-reconstruction artifacts, but this lane does not materialize `review_assets`, clear the bridge blocker, accept source/page status, or create production output.",
        "",
        "- Bridge blocker before audit: `needs_source_asset_recovery`.",
        "- Recovery classification: `recoverable_from_pinned_page_image_and_source_reconstruction_artifacts`.",
        "- Source-acceptance chain authority risk: `stale_generator_hash_in_completion_artifact`.",
        "- Bridge blocker cleared: `false`.",
        "- OCR/Tesseract executed: `false`.",
        "- Production/acceptance/mutation/push/downstream: `false`.",
        "",
        "Next allowed action: separate bounded P002 source-asset materialization authorization.",
        "",
    ]
    write_text(summary_path, "\n".join(summary))
    manifest_lines = [
        "# P002 Source Asset Recovery Audit Manifest - C01TEP002ASSETREC-G1-VIRAL-001",
        "",
        "Boundary: report-only recovery audit; no OCR, materialization, acceptance, production, or mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes([report_path, summary_path]).items():
        manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(manifest_path, "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
