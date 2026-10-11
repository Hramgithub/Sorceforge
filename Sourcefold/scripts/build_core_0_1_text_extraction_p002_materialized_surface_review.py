from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MATERIALIZATION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_materialization_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_materialized_surface_review_G1_VIRAL_001"

LANE_ID = "C01TEP002MATREVIEW-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-MATERIALIZED-SURFACE-REVIEW-001"
INPUT_LANE_ID = "C01TEP002ASSETMAT-G1-VIRAL-001"
PAGE = "002"
CREATION_HEAD = "58dc74e3"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)

PINNED_INPUTS = {
    "C01TEP002ASSETMAT-G1-VIRAL-001.report": (
        MATERIALIZATION_ROOT / "p002_source_asset_materialization_report.json",
        "82D51C020E5571C7FDB86040CC0E3469EC0CE26A1C4A49286B0135E13A39315F",
    ),
    "C01TEP002ASSETMAT-G1-VIRAL-001.summary": (
        MATERIALIZATION_ROOT / "p002_source_asset_materialization_summary.md",
        "3962117A4EE8737788B0FE60ADB57C4BB9E5338ABDE03835E1B56BEBD732B038",
    ),
    "C01TEP002ASSETMAT-G1-VIRAL-001.manifest": (
        MATERIALIZATION_ROOT / "p002_source_asset_materialization_manifest.md",
        "8F32E3FBEB3B671857B65FCD769627B8545F471B4E5F8DDF062D4FDDFD62EFE6",
    ),
}

FALSE_BOUNDARY_FLAGS = [
    "fresh_ocr_success",
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
    "production_assembly_created",
    "acceptance_performed",
    "page_021_plus_included",
    "push_performed",
    "promotion_performed",
    "downstream_execution_performed",
]

OUTPUT_FILES = [
    "p002_materialized_surface_review_report.json",
    "p002_materialized_surface_review_summary.md",
    "p002_materialized_surface_review_manifest.md",
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
    parser = argparse.ArgumentParser(description="Review materialized P002 source asset surface.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 materialized surface review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 materialized surface review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 materialized surface review requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    materialization_report = read_json(PINNED_INPUTS["C01TEP002ASSETMAT-G1-VIRAL-001.report"][0])
    if materialization_report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 materialization input lane")
    if materialization_report["page"] != PAGE:
        raise SystemExit("P002 materialization page drifted")
    if materialization_report["bridge_blocker_cleared"] is not False:
        raise SystemExit("P002 materialization unexpectedly cleared bridge blocker")
    if materialization_report["allowed_next_action"] != "separate_bounded_p002_materialized_surface_review_before_blocker_clearance":
        raise SystemExit("P002 materialization next action drifted")
    return verified, materialization_report


def review_materialized_assets(materialization_report: dict[str, Any]) -> list[dict[str, str]]:
    reviewed: list[dict[str, str]] = []
    for item in materialization_report["materialized_assets"]:
        materialized_path = ROOT / item["materialized_path"]
        actual_hash = sha256_file(materialized_path)
        if actual_hash != item["materialized_sha256"]:
            raise SystemExit(f"materialized asset hash mismatch: {materialized_path.name}")
        if actual_hash != item["source_sha256"]:
            raise SystemExit(f"source/materialized hash mismatch: {materialized_path.name}")
        reviewed.append(
            {
                "input_key": item["input_key"],
                "materialized_path": item["materialized_path"],
                "materialized_sha256": actual_hash,
                "review_status": "hash_verified_materialized_surface_available",
            }
        )
    if sorted(item["input_key"] for item in reviewed) != [
        "P002.corrected_crop_ref.1",
        "P002.corrected_crop_ref.2",
        "P002.page_image",
    ]:
        raise SystemExit("P002 materialized asset set drifted")
    return reviewed


def build_report(
    verified_inputs: dict[str, dict[str, str]],
    materialization_report: dict[str, Any],
    reviewed_assets: list[dict[str, str]],
) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_materialized_surface_review_completed_asset_recovery_blocker_cleared_no_ocr_no_acceptance",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_id": INPUT_LANE_ID,
        "page": PAGE,
        "scope": "page_002_materialized_surface_review_only",
        "verified_inputs": verified_inputs,
        "reviewed_assets": reviewed_assets,
        "materialized_surface_available": True,
        "materialized_surface_hash_verified": True,
        "asset_recovery_blocker_before_review": materialization_report["bridge_blocker_before_materialization"],
        "asset_recovery_blocker_cleared": True,
        "bridge_blocker_cleared": True,
        "next_blocker": "needs_fresh_ocr_route_authorization",
        "p002_ready_for_fresh_ocr_route_authorization": True,
        "materialized_surface_is_recoverability_evidence_only": True,
        "source_acceptance_chain_authority_risk": materialization_report["source_acceptance_chain_authority_risk"],
        "stale_generator_hash_risk_preserved": True,
        "allowed_next_action": "separate_bounded_p002_fresh_ocr_route_authorization_or_clean_runtime_selector_policy_update",
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
            "Reviewed the lane-owned page `002` materialized surface and verified",
            "the full-page image plus two corrected crop refs by SHA-256.",
            "",
            "`asset_recovery_blocker_cleared=true`, but `fresh_ocr_success=false`.",
            "The next blocker is `needs_fresh_ocr_route_authorization`; this lane",
            "does not run OCR, accept text, mutate source/page status, or authorize",
            "production.",
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
        "- Output policy: review report/summary/manifest only; no OCR, acceptance, production, source mutation, or page 021+.",
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
            "## Decision",
            "",
            "- Asset recovery blocker cleared: `true`",
            "- Fresh OCR success: `false`",
            "- Next blocker: `needs_fresh_ocr_route_authorization`",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, materialization_report = verify_inputs()
    reviewed_assets = review_materialized_assets(materialization_report)
    report = build_report(verified_inputs, materialization_report, reviewed_assets)
    write_json(OUT_ROOT / "p002_materialized_surface_review_report.json", report)
    write_text(OUT_ROOT / "p002_materialized_surface_review_summary.md", build_summary(report))
    write_text(OUT_ROOT / "p002_materialized_surface_review_manifest.md", build_manifest(report, output_hashes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
