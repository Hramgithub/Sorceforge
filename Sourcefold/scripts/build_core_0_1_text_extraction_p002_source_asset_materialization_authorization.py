from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_recovery_audit_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_source_asset_materialization_authorization_G1_VIRAL_001"

LANE_ID = "C01TEP002ASSETMATAUTH-G1-VIRAL-001"
AUTHORIZATION_ID = (
    "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-SOURCE-ASSET-MATERIALIZATION-AUTHORIZATION-001"
)
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)
INPUT_LANE_ID = "C01TEP002ASSETREC-G1-VIRAL-001"
CREATION_HEAD = "b7a67515"
PAGE = "002"

PINNED_INPUTS = {
    "C01TEP002ASSETREC-G1-VIRAL-001.report": (
        INPUT_ROOT / "p002_source_asset_recovery_audit_report.json",
        "A1D88F383DDF5F8654DBBEFEEEBEE391F955EB4C61C01C490009533430B9E140",
    ),
    "C01TEP002ASSETREC-G1-VIRAL-001.summary": (
        INPUT_ROOT / "p002_source_asset_recovery_audit_summary.md",
        "B34EB8461DD931C2E18341905C056AADC5EDE78D510D249FB2B771EF8838235F",
    ),
    "C01TEP002ASSETREC-G1-VIRAL-001.manifest": (
        INPUT_ROOT / "p002_source_asset_recovery_audit_manifest.md",
        "061FE0C03A176953E585FCCF80962DB6CAA9F338E7CDF0299A9F14A8923AFDAB",
    ),
}

OUT_OF_SCOPE_PAGES_REJECTED = [
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

FALSE_BOUNDARY_FLAGS = [
    "materialization_performed",
    "review_assets_materialized",
    "bridge_blocker_cleared",
    "ocr_execution_performed",
    "tesseract_invocation_authorized",
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
    "p002_source_asset_materialization_authorization_report.json",
    "p002_source_asset_materialization_authorization_summary.md",
    "p002_source_asset_materialization_authorization_manifest.md",
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
    parser = argparse.ArgumentParser(description="Build P002 source asset materialization authorization.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 source asset materialization authorization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 source asset materialization authorization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 source asset materialization authorization requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    recovery_report = read_json(PINNED_INPUTS["C01TEP002ASSETREC-G1-VIRAL-001.report"][0])
    if recovery_report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 recovery audit input lane")
    if recovery_report["page"] != PAGE:
        raise SystemExit("P002 recovery audit page set drifted")
    if recovery_report["scope"] != "page_002_only":
        raise SystemExit("P002 recovery audit scope drifted")
    if recovery_report["bridge_blocker_cleared"] is not False:
        raise SystemExit("P002 recovery audit unexpectedly cleared the bridge blocker")
    if recovery_report["asset_recovery_classification"] != "recoverable_from_pinned_page_image_and_source_reconstruction_artifacts":
        raise SystemExit("P002 recovery audit classification drifted")
    if recovery_report["allowed_next_action"] != "separate_bounded_p002_source_asset_materialization_authorization":
        raise SystemExit("P002 recovery audit next action drifted")
    return verified, recovery_report


def build_report(verified_inputs: dict[str, dict[str, str]], recovery_report: dict[str, Any]) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_source_asset_materialization_authorization_recorded_future_lane_only_no_materialization_no_mutation",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_id": INPUT_LANE_ID,
        "input_lane_ids": [INPUT_LANE_ID],
        "page": PAGE,
        "scope": "page_002_materialization_authorization_only",
        "out_of_scope_pages_rejected": OUT_OF_SCOPE_PAGES_REJECTED,
        "human_decision": HUMAN_DECISION,
        "verified_inputs": verified_inputs,
        "recovery_audit_classification": recovery_report["asset_recovery_classification"],
        "source_acceptance_chain_authority_risk": recovery_report["source_acceptance_chain_authority_risk"],
        "stale_generator_hash_risk_preserved": True,
        "completion_builder_hash_stale": True,
        "bridge_blocker_before_authorization": recovery_report["bridge_blocker_before_audit"],
        "bridge_blocker_cleared": False,
        "authorized_future_action": "separate_bounded_p002_source_asset_materialization_lane_only",
        "future_materialization_lane_authorized": True,
        "future_materialization_authorized": True,
        "future_materialization_scope": "materialize_page_002_source_asset_surface_from_pinned_recovery_audit_only",
        "future_materialization_output_tree_must_be_locked_before_execution": True,
        "future_materialization_must_preserve_authority_split": True,
        "future_materialization_may_create_review_assets": True,
        "future_materialization_may_clear_bridge_blocker": False,
        "future_materialization_may_accept_source_or_page_status": False,
        "future_materialization_may_run_ocr_or_tesseract": False,
        "future_materialization_may_run_render_or_pdf_parsing": False,
        "this_lane_report_only": True,
        "allowed_next_action": "execute_separate_bounded_p002_source_asset_materialization_from_pinned_recovery_audit",
        "forbidden_next_actions": [
            "accept_page_002",
            "clear_bridge_blocker_in_authorization_lane",
            "run_ocr_or_tesseract",
            "mutate_source_raw_accepted_or_page_status",
            "assemble_production",
            "include_page_021_plus",
            "push_or_downstream_execution",
        ],
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
            "Page `002` source asset materialization is authorized only for a future",
            "bounded lane that consumes the pinned recovery audit. This lane does not",
            "materialize review assets, clear the bridge blocker, accept source/page",
            "status, run OCR/Tesseract, parse/render PDFs, or create production output.",
            "",
            "The stale generator-hash authority risk from the P002 source-acceptance",
            "chain is preserved; the chain remains recoverability evidence only.",
            "",
            f"Allowed next action: `{report['allowed_next_action']}`.",
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
        "- Output policy: report/summary/manifest only; no materialization, OCR, acceptance, production, or downstream execution.",
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
            "  materialization in `PROJECT_STATUS.md`, `roadmap.yaml`, and",
            "  `bounded_trial_authorizations.md`.",
        ]
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, recovery_report = verify_inputs()
    report = build_report(verified_inputs, recovery_report)
    report_path = OUT_ROOT / OUTPUT_FILES[0]
    summary_path = OUT_ROOT / OUTPUT_FILES[1]
    manifest_path = OUT_ROOT / OUTPUT_FILES[2]
    write_json(report_path, report)
    write_text(summary_path, build_summary(report))
    write_text(manifest_path, build_manifest(report, output_hashes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
