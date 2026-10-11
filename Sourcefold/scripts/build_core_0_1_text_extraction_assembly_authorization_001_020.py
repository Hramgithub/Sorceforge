from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
BRIDGE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_eligibility_bridge_001_020_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_assembly_authorization_001_020_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

LANE_ID = "C01TEAUTH020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ASSEMBLY-AUTHORIZATION-001-020-001"
HUMAN_DECISION = "Ок продолжай"

REQUESTED_PAGES = [f"{page:03d}" for page in range(1, 21)]
BRIDGE_PAGES = ["001", "002", "003", "004", "005", "006", "007", "008", "014", "019"]
STATIC_SELECTED_PAGES = ["009", "010", "011", "012", "013", "015", "016", "017", "018", "020"]

INPUT_HASHES = {
    "C01TEBRIDGE020-G1-VIRAL-001.report": (
        BRIDGE_ROOT / "eligibility_bridge_001_020_report.json",
        "24BD2AC4FC990BBEC2A550341F5C8CF4858F7AB7728574EA619CB33297379998",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.summary": (
        BRIDGE_ROOT / "eligibility_bridge_001_020_summary.md",
        "DC10DD28EB2D72336C11F5EA0E8C36EBA2861FBA7957FC6199F6AEE937D5AE28",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.bridge_entries": (
        BRIDGE_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json",
        "D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.selector_v4": (
        BRIDGE_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json",
        "A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC",
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
    "runtime_selector_integration",
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
    parser = argparse.ArgumentParser(description="Build final 001-020 assembly authorization check.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("assembly-authorization lane is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"assembly-authorization lane requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("assembly-authorization lane requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict], list[dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if "Status: `eligibility_bridge_static_evidence_all_pages_covered_production_blocked`" not in ledger:
        raise SystemExit("predecessor C01TEBRIDGE020 completion is not synced in ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    bridge_report = read_json(BRIDGE_ROOT / "eligibility_bridge_001_020_report.json")
    bridge_entries = read_json(BRIDGE_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json")
    replay_v4 = read_json(BRIDGE_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json")

    if bridge_report["lane_id"] != "C01TEBRIDGE020-G1-VIRAL-001":
        raise SystemExit("eligibility bridge input lane drifted")
    if bridge_report["covered_pages_v4"] != REQUESTED_PAGES:
        raise SystemExit(f"selector replay v4 coverage drifted: {bridge_report['covered_pages_v4']}")
    if bridge_report["all_pages_static_evidence_covered"] is not True:
        raise SystemExit("eligibility bridge no longer covers all static evidence")
    if bridge_report["all_pages_first_pass_success"] is not False:
        raise SystemExit("eligibility bridge unexpectedly reports first-pass success")
    if bridge_report["production_ready"] is not False:
        raise SystemExit("eligibility bridge unexpectedly production-ready")
    if [entry["page"] for entry in replay_v4] != REQUESTED_PAGES:
        raise SystemExit("selector replay v4 page order drifted")
    if sorted(entry["page"] for entry in bridge_entries) != BRIDGE_PAGES:
        raise SystemExit("bridge page set drifted")
    return verified, bridge_report, bridge_entries, replay_v4


def build_report(
    verified_inputs: dict[str, dict[str, str]],
    bridge_report: dict,
    bridge_entries: list[dict],
    replay_v4: list[dict],
) -> dict:
    bridge_page_set = {entry["page"] for entry in bridge_entries}
    static_page_set = {entry["page"] for entry in replay_v4} - bridge_page_set
    if sorted(static_page_set) != STATIC_SELECTED_PAGES:
        raise SystemExit(f"static selected page set drifted: {sorted(static_page_set)}")

    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "assembly_authorization_checked_production_not_authorized",
        "human_decision": HUMAN_DECISION,
        "input_lane_id": bridge_report["lane_id"],
        "requested_pages": REQUESTED_PAGES,
        "covered_pages_v4": bridge_report["covered_pages_v4"],
        "bridge_pages": BRIDGE_PAGES,
        "static_selected_pages": STATIC_SELECTED_PAGES,
        "all_pages_static_evidence_covered": True,
        "all_pages_first_pass_success": False,
        "mixed_static_evidence_and_accepted_bridge": True,
        "production_ready": False,
        "production_assembly_authorized": False,
        "production_assembly_authorization_decision": "not_authorized_from_mixed_static_evidence_while_first_pass_false",
        "production_assembly_created": False,
        "clean_production_output_folder_created": False,
        "required_before_standard_production_assembly": "fresh_first_pass_runtime_selector_success_for_001_020_or_separate_explicit_human_exception",
        "allowed_next_routes": [
            "fresh_first_pass_runtime_selector_authorization_for_001_020",
            "separate_explicit_human_exception_decision_for_mixed_static_evidence_production",
        ],
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "selector_runtime_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
        "verified_inputs": verified_inputs,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
    }


def write_summary(report: dict) -> None:
    lines = [
        "# Assembly Authorization 001-020 - C01TEAUTH020-G1-VIRAL-001",
        "",
        "Status: `assembly_authorization_checked_production_not_authorized`",
        "",
        "This final check evaluates whether selector replay v4 authorizes production assembly. It does not create production output.",
        "",
        f"Covered pages v4: `{', '.join(report['covered_pages_v4'])}`.",
        f"All pages static evidence covered: `{str(report['all_pages_static_evidence_covered']).lower()}`.",
        f"All pages first-pass success: `{str(report['all_pages_first_pass_success']).lower()}`.",
        f"Mixed static evidence and accepted bridge: `{str(report['mixed_static_evidence_and_accepted_bridge']).lower()}`.",
        f"Production ready: `{str(report['production_ready']).lower()}`.",
        f"Production assembly authorized: `{str(report['production_assembly_authorized']).lower()}`.",
        "",
        "Decision: production assembly is not authorized from mixed static evidence while `all_pages_first_pass_success=false`.",
        "",
        "Allowed next routes:",
        "",
        "- Fresh first-pass runtime-selector authorization for pages `001`-`020`.",
        "- Separate explicit human exception decision for mixed static evidence production.",
        "",
        "## Boundary Flags",
        "",
        "- `production_assembly_created=false`.",
        "- `clean_production_output_folder_created=false`.",
        "- `accepted_text_mutation_performed=false`.",
        "- `page_status_mutation_performed=false`.",
        "- `runtime_selector_integration=false`.",
        "- `page_021_plus_included=false`.",
        "- `acceptance_performed=false`.",
        "",
    ]
    write_text(OUT_ROOT / "assembly_authorization_001_020_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# Assembly Authorization 001-020 Manifest - C01TEAUTH020-G1-VIRAL-001",
        "",
        "Boundary: report-only authorization check; no production assembly, no copied candidate text, no mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "assembly_authorization_001_020_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / "assembly_authorization_001_020_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, bridge_report, bridge_entries, replay_v4 = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = build_report(verified_inputs, bridge_report, bridge_entries, replay_v4)
    write_json(OUT_ROOT / "assembly_authorization_001_020_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
