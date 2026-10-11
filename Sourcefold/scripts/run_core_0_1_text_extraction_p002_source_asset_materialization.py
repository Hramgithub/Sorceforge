from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_materialization_authorization_G1_VIRAL_001"
RECOVERY_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_recovery_audit_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_materialization_G1_VIRAL_001"
SURFACE_ROOT = OUT_ROOT / "materialized_surface"
HISTORICAL_REVIEW_ASSETS = TRIAL_ROOT / "page_complete_review_p002_G1_VIRAL_001" / "review_assets"

LANE_ID = "C01TEP002ASSETMAT-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-MATERIALIZATION-001"
AUTHORIZATION_LANE_ID = "C01TEP002ASSETMATAUTH-G1-VIRAL-001"
RECOVERY_LANE_ID = "C01TEP002ASSETREC-G1-VIRAL-001"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)
CREATION_HEAD = "f7e17810"
PAGE = "002"

PINNED_INPUTS = {
    "C01TEP002ASSETMATAUTH-G1-VIRAL-001.report": (
        AUTH_ROOT / "p002_source_asset_materialization_authorization_report.json",
        "37D85ADA6E3AB6CAAA7D8F82F488F53281AE740A8BDD8D4D82AE83264FB6811B",
    ),
    "C01TEP002ASSETMATAUTH-G1-VIRAL-001.summary": (
        AUTH_ROOT / "p002_source_asset_materialization_authorization_summary.md",
        "6FAB886C6FEC44ADDCC6F06749143369779402D958AC397CAAE01EA605CE45F8",
    ),
    "C01TEP002ASSETMATAUTH-G1-VIRAL-001.manifest": (
        AUTH_ROOT / "p002_source_asset_materialization_authorization_manifest.md",
        "984FDD1BCB291F01D3E9690B5812A7DC5A3072F115BD8D2965B871E1A5541431",
    ),
    "C01TEP002ASSETREC-G1-VIRAL-001.report": (
        RECOVERY_ROOT / "p002_source_asset_recovery_audit_report.json",
        "A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140",
    ),
    "C01TEP002ASSETREC-G1-VIRAL-001.summary": (
        RECOVERY_ROOT / "p002_source_asset_recovery_audit_summary.md",
        "B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F",
    ),
    "C01TEP002ASSETREC-G1-VIRAL-001.manifest": (
        RECOVERY_ROOT / "p002_source_asset_recovery_audit_manifest.md",
        "061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB",
    ),
    "P002.page_image": (
        TRIAL_ROOT / "images" / "page_002.png",
        "ABC72B84D6CE89FE6C9B28981A39ADA33C5B9488B2864E8B35B41B120D6036C9",
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

MATERIALIZED_ASSETS = {
    "P002.page_image": "page_002.png",
    "P002.corrected_crop_ref.1": "1_SRAD-G1-VIRAL-002-R01__SRAD-G1-VIRAL-002-R01-C01.png",
    "P002.corrected_crop_ref.2": "2_SRAD-G1-VIRAL-002-R02__SRAD-G1-VIRAL-002-R02-C01.png",
}

FALSE_BOUNDARY_FLAGS = [
    "historical_page_complete_review_review_assets_mutated",
    "bridge_blocker_cleared",
    "ocr_execution_performed",
    "tesseract_invoked",
    "render_execution_performed",
    "pdf_parsing_or_text_layer_extraction_performed",
    "accepted_text_mutation_performed",
    "semantic_text_mutation_performed",
    "page_status_mutation_performed",
    "source_or_raw_mutation_performed",
    "fixture_admission_performed",
    "production_ready",
    "production_assembly_authorized",
    "acceptance_performed",
    "page_021_plus_included",
    "push_performed",
    "promotion_performed",
    "downstream_execution_performed",
]

OUTPUT_FILES = [
    "materialized_surface/page_002.png",
    "materialized_surface/1_SRAD-G1-VIRAL-002-R01__SRAD-G1-VIRAL-002-R01-C01.png",
    "materialized_surface/2_SRAD-G1-VIRAL-002-R02__SRAD-G1-VIRAL-002-R02-C01.png",
    "p002_source_asset_materialization_report.json",
    "p002_source_asset_materialization_summary.md",
    "p002_source_asset_materialization_manifest.md",
]


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
    parser = argparse.ArgumentParser(description="Materialize P002 source asset surface into a clean lane-owned output tree.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 source asset materialization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 source asset materialization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 source asset materialization requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if HISTORICAL_REVIEW_ASSETS.exists():
        raise SystemExit(f"historical review_assets path exists and is out of scope: {HISTORICAL_REVIEW_ASSETS}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    auth_report = read_json(PINNED_INPUTS["C01TEP002ASSETMATAUTH-G1-VIRAL-001.report"][0])
    recovery_report = read_json(PINNED_INPUTS["C01TEP002ASSETREC-G1-VIRAL-001.report"][0])
    if auth_report["lane_id"] != AUTHORIZATION_LANE_ID:
        raise SystemExit("unexpected P002 materialization authorization input lane")
    if auth_report["allowed_next_action"] != "execute_separate_bounded_p002_source_asset_materialization_from_pinned_recovery_audit":
        raise SystemExit("P002 materialization authorization next action drifted")
    if auth_report["future_materialization_lane_authorized"] is not True:
        raise SystemExit("P002 materialization lane is not authorized")
    if auth_report["future_materialization_may_clear_bridge_blocker"] is not False:
        raise SystemExit("P002 materialization authorization unexpectedly allows blocker clearing")
    if recovery_report["lane_id"] != RECOVERY_LANE_ID:
        raise SystemExit("unexpected P002 recovery input lane")
    if recovery_report["page"] != PAGE:
        raise SystemExit("P002 recovery page drifted")
    if recovery_report["bridge_blocker_cleared"] is not False:
        raise SystemExit("P002 recovery unexpectedly cleared bridge blocker")
    return verified, auth_report, recovery_report


def materialize_assets() -> list[dict[str, str]]:
    SURFACE_ROOT.mkdir(parents=True, exist_ok=False)
    records: list[dict[str, str]] = []
    for key, output_name in MATERIALIZED_ASSETS.items():
        source_path = PINNED_INPUTS[key][0]
        dest_path = SURFACE_ROOT / output_name
        shutil.copyfile(source_path, dest_path)
        source_hash = PINNED_INPUTS[key][1]
        dest_hash = sha256_file(dest_path)
        if dest_hash != source_hash:
            raise SystemExit(f"materialized asset hash mismatch: {dest_path.name}")
        records.append(
            {
                "input_key": key,
                "source_path": source_path.relative_to(ROOT).as_posix(),
                "source_sha256": source_hash,
                "materialized_path": dest_path.relative_to(ROOT).as_posix(),
                "materialized_sha256": dest_hash,
            }
        )
    return records


def build_report(
    verified_inputs: dict[str, dict[str, str]],
    auth_report: dict[str, Any],
    recovery_report: dict[str, Any],
    materialized_assets: list[dict[str, str]],
) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "authorization_lane_id": AUTHORIZATION_LANE_ID,
        "status": "p002_source_asset_materialization_completed_output_surface_only_no_blocker_clearance_no_mutation",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_ids": [AUTHORIZATION_LANE_ID, RECOVERY_LANE_ID],
        "page": PAGE,
        "scope": "page_002_source_asset_materialization_output_surface_only",
        "output_root": OUT_ROOT.relative_to(ROOT).as_posix(),
        "output_root_created_clean": True,
        "verified_inputs": verified_inputs,
        "materialized_surface_created": True,
        "materialized_assets": materialized_assets,
        "materialized_surface_is_recoverability_evidence_only": True,
        "source_acceptance_chain_authority_risk": recovery_report["source_acceptance_chain_authority_risk"],
        "stale_generator_hash_risk_preserved": True,
        "bridge_blocker_before_materialization": auth_report["bridge_blocker_before_authorization"],
        "bridge_blocker_cleared": False,
        "allowed_next_action": "separate_bounded_p002_materialized_surface_review_before_blocker_clearance",
    }
    for flag in FALSE_BOUNDARY_FLAGS:
        report[flag] = False
    return report


def build_summary(report: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# {LANE_ID}",
            "",
            f"Status: `{report['status']}`",
            "",
            "Materialized page `002` source asset surface into a clean lane-owned",
            "output folder from pinned existing assets only.",
            "",
            "`bridge_blocker_cleared=false`; the materialized surface is",
            "recoverability evidence only and does not accept source/page status,",
            "authorize production, or run OCR/Tesseract/render/PDF parsing.",
            "",
        ]
    )


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for name in OUTPUT_FILES:
        path = OUT_ROOT / name
        if path.exists():
            hashes[name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return hashes


def build_manifest(report: dict[str, Any], hashes: dict[str, dict[str, str]]) -> str:
    lines = [
        f"# {LANE_ID} Manifest",
        "",
        f"- Authorization: `{AUTHORIZATION_ID}`",
        f"- Status: `{report['status']}`",
        f"- Page: `{PAGE}`",
        "- Output policy: clean materialized surface plus report/summary/manifest only; no blocker clearance, acceptance, production, or downstream execution.",
        "",
        "## Inputs",
        "",
    ]
    for key, item in report["verified_inputs"].items():
        lines.append(f"- `{key}`: `{item['sha256']}`")
    lines.extend(["", "## Outputs", ""])
    for name, item in hashes.items():
        lines.append(f"- `{name}`: `{item['sha256']}`")
    lines.extend(
        [
            "",
            "## Manifest Self-Hash",
            "",
            "- This manifest does not embed its own post-write SHA-256 because doing so",
            "  would change the digest. The manifest file SHA-256 is sealed after",
            "  materialization in status, roadmap, and authorization-ledger sync surfaces.",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, auth_report, recovery_report = verify_inputs()
    materialized_assets = materialize_assets()
    report = build_report(verified_inputs, auth_report, recovery_report, materialized_assets)
    write_json(OUT_ROOT / "p002_source_asset_materialization_report.json", report)
    write_text(OUT_ROOT / "p002_source_asset_materialization_summary.md", build_summary(report))
    write_text(OUT_ROOT / "p002_source_asset_materialization_manifest.md", build_manifest(report, output_hashes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
