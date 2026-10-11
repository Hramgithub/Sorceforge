from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_assembly_authorization_001_020_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

LANE_ID = "C01TEFPSAUTH020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FIRST-PASS-RUNTIME-SELECTOR-AUTHORIZATION-001-020-001"
HUMAN_DECISION = "Идем по нашему плану, делаем 1-20?"

REQUESTED_PAGES = [f"{page:03d}" for page in range(1, 21)]
INPUT_HASHES = {
    "C01TEAUTH020-G1-VIRAL-001.report": (
        AUTH_ROOT / "assembly_authorization_001_020_report.json",
        "CE668EF259DF00A4BB062259279EFE3ED2C367F3CB67E58ACC9BADB29F106429",
    ),
    "C01TEAUTH020-G1-VIRAL-001.summary": (
        AUTH_ROOT / "assembly_authorization_001_020_summary.md",
        "B3D4674A29162BD9A7F4F1F0F991080ADB269B1EA473E577096A42C46C3D35E8",
    ),
    "C01TEAUTH020-G1-VIRAL-001.manifest": (
        AUTH_ROOT / "assembly_authorization_001_020_manifest.md",
        "F3B26C015D1A043DD5201DA4A22B9C9E426AEB3B4572A3C1EDE189FFEED55765",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "reference_token_insertion",
    "candidate_text_copy",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "source_mutation",
    "raw_mutation",
    "selector_runtime_enablement",
    "runtime_selector_implementation",
    "runtime_execution",
    "production_assembly",
    "clean_production_output_folder",
    "page_021_plus_processing",
    "translation",
    "proofreading",
    "push",
    "promotion",
    "acceptance",
    "downstream_execution",
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


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build report-only first-pass runtime-selector authorization for 001-020.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("first-pass runtime-selector authorization lane is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"first-pass runtime-selector authorization lane requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("first-pass runtime-selector authorization lane requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if "Status: `assembly_authorization_checked_production_not_authorized`" not in ledger:
        raise SystemExit("predecessor C01TEAUTH020 completion is not synced in ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    auth_report = read_json(AUTH_ROOT / "assembly_authorization_001_020_report.json")
    if auth_report["lane_id"] != "C01TEAUTH020-G1-VIRAL-001":
        raise SystemExit("assembly authorization input lane drifted")
    if auth_report["covered_pages_v4"] != REQUESTED_PAGES:
        raise SystemExit(f"covered page set drifted: {auth_report['covered_pages_v4']}")
    if auth_report["all_pages_static_evidence_covered"] is not True:
        raise SystemExit("assembly authorization no longer covers all static evidence")
    if auth_report["all_pages_first_pass_success"] is not False:
        raise SystemExit("assembly authorization unexpectedly reports first-pass success")
    if auth_report["production_ready"] is not False:
        raise SystemExit("assembly authorization unexpectedly production-ready")
    if auth_report["production_assembly_authorized"] is not False:
        raise SystemExit("mixed-static production is unexpectedly authorized")
    return verified, auth_report


def build_report(verified_inputs: dict[str, dict[str, str]], auth_report: dict) -> dict:
    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "first_pass_runtime_selector_authorization_recorded_report_only",
        "human_decision": HUMAN_DECISION,
        "input_lane_id": auth_report["lane_id"],
        "requested_pages": REQUESTED_PAGES,
        "fresh_first_pass_runtime_selector_route_authorized": True,
        "authorized_future_route": "bounded_fresh_first_pass_runtime_selector_run_for_001_020_only",
        "this_lane_report_only": True,
        "runtime_selector_implementation_created": False,
        "selector_runtime_enabled": False,
        "runtime_execution_performed": False,
        "ocr_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "production_ready": False,
        "production_assembly_authorized": False,
        "production_assembly_created": False,
        "clean_production_output_folder_created": False,
        "standard_production_requires_future_clean_first_pass_success": True,
        "future_route_guardrails": [
            "page_set_must_equal_001_020",
            "same_bounded_input_set_only",
            "selected_best_methods_or_validated_bridge_lineage_only",
            "failed_and_superseded_variants_excluded_from_clean_output",
            "hash_drift_fails_closed",
            "missing_page_fails_closed",
            "page_021_plus_fails_closed",
            "source_or_raw_mutation_fails_closed",
            "accepted_text_or_page_status_mutation_fails_closed",
            "production_output_before_clean_first_pass_success_fails_closed",
        ],
        "allowed_next_action": "implement_or_execute_bounded_fresh_first_pass_runtime_selector_001_020_under_this_authorization",
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
        "verified_inputs": verified_inputs,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
    }


def write_summary(report: dict) -> None:
    lines = [
        "# First-Pass Runtime Selector Authorization 001-020 - C01TEFPSAUTH020-G1-VIRAL-001",
        "",
        "Status: `first_pass_runtime_selector_authorization_recorded_report_only`",
        "",
        "This packet authorizes the bounded future route for a fresh first-pass runtime-selector run over pages `001`-`020` only.",
        "It does not implement or execute that runtime selector and does not create production output.",
        "",
        f"Requested pages: `{', '.join(report['requested_pages'])}`.",
        f"Fresh first-pass runtime-selector route authorized: `{str(report['fresh_first_pass_runtime_selector_route_authorized']).lower()}`.",
        f"Runtime selector implementation created: `{str(report['runtime_selector_implementation_created']).lower()}`.",
        f"Runtime execution performed: `{str(report['runtime_execution_performed']).lower()}`.",
        f"Production assembly authorized: `{str(report['production_assembly_authorized']).lower()}`.",
        f"Production assembly created: `{str(report['production_assembly_created']).lower()}`.",
        "",
        "Standard production remains blocked until a future clean first-pass runtime-selector result succeeds.",
        "",
        "## Future Route Guardrails",
        "",
    ]
    lines.extend(f"- `{guardrail}`." for guardrail in report["future_route_guardrails"])
    lines.extend(
        [
            "",
            "## Boundary Flags",
            "",
            "- `ocr_execution_performed=false`.",
            "- `render_execution_performed=false`.",
            "- `runtime_selector_implementation_created=false`.",
            "- `runtime_execution_performed=false`.",
            "- `production_assembly_created=false`.",
            "- `clean_production_output_folder_created=false`.",
            "- `accepted_text_mutation_performed=false`.",
            "- `page_status_mutation_performed=false`.",
            "- `page_021_plus_included=false`.",
            "- `acceptance_performed=false`.",
            "",
        ]
    )
    write_text(OUT_ROOT / "first_pass_runtime_selector_authorization_001_020_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# First-Pass Runtime Selector Authorization 001-020 Manifest - C01TEFPSAUTH020-G1-VIRAL-001",
        "",
        "Boundary: report-only route authorization; no runtime implementation, no runtime execution, no production output, no mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "first_pass_runtime_selector_authorization_001_020_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / "first_pass_runtime_selector_authorization_001_020_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, auth_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = build_report(verified_inputs, auth_report)
    write_json(OUT_ROOT / "first_pass_runtime_selector_authorization_001_020_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
