from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_scoring_authorization_003_008_G1_VIRAL_001"

LANE_ID = "C01TEBRIDGESCOREAUTH020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-SCORING-AUTHORIZATION-003-008-001"
INPUT_LANE_ID = "C01TEBRIDGESCOREAUD020-G1-VIRAL-001"
CREATION_HEAD = "f44cafe1"
HUMAN_DECISION = (
    "Давай уже широким планом пойдем. Бери вполном объёме. "
    "Ты оркестратор, делегируй задачи, сам расширяй план , коммиты разрешаю."
)
PAGES = ["003", "004", "005", "006", "007", "008"]

PINNED_INPUTS = {
    "C01TEBRIDGESCOREAUD020-G1-VIRAL-001.report": (
        INPUT_ROOT / "bridge_page_scoring_reference_audit_003_008_report.json",
        "7927E9B5C24C6689C6321D1CBA4FB71BFE6F4107C622B4824638C4AC068D95D5",
    ),
    "C01TEBRIDGESCOREAUD020-G1-VIRAL-001.summary": (
        INPUT_ROOT / "bridge_page_scoring_reference_audit_003_008_summary.md",
        "85A0725A721E9C0EA25BCBAB146EFD643CEB7DDE1E2337492AF3E27D686FB443",
    ),
    "C01TEBRIDGESCOREAUD020-G1-VIRAL-001.manifest": (
        INPUT_ROOT / "bridge_page_scoring_reference_audit_003_008_manifest.md",
        "0DE9E1D3F3EEA7D734841DBD3D4E897B2355A561AFC07A4EE8FC92529F5C1E2D",
    ),
}

FALSE_BOUNDARY_FLAGS = [
    "scoring_performed",
    "fresh_ocr_success",
    "promotion_authorized",
    "promotion_performed",
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
    "downstream_execution_performed",
]

OUTPUT_FILES = [
    "bridge_page_scoring_authorization_003_008_report.json",
    "bridge_page_scoring_authorization_003_008_summary.md",
    "bridge_page_scoring_authorization_003_008_manifest.md",
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
    parser = argparse.ArgumentParser(description="Build 003-008 bridge candidate scoring authorization.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("003-008 scoring authorization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"003-008 scoring authorization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("003-008 scoring authorization requires the exact broad orchestration decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in PINNED_INPUTS.items()}
    audit = read_json(PINNED_INPUTS["C01TEBRIDGESCOREAUD020-G1-VIRAL-001.report"][0])
    if audit["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected 003-008 scoring audit input lane")
    if audit["audit_pages"] != PAGES:
        raise SystemExit("003-008 scoring audit page set drifted")
    if audit["fresh_ocr_success_pages"] != []:
        raise SystemExit("003-008 scoring audit unexpectedly has fresh OCR success pages")
    if audit["promotable_pages"] != []:
        raise SystemExit("003-008 scoring audit unexpectedly has promotable pages")
    if audit["allowed_next_action"] != "bounded_candidate_scoring_authorization_or_page_002_source_asset_recovery":
        raise SystemExit("003-008 scoring audit next action drifted")
    return verified, audit


def build_report(verified_inputs: dict[str, dict[str, str]], audit: dict[str, Any]) -> dict[str, Any]:
    current_head = git_head()
    if current_head != CREATION_HEAD:
        raise SystemExit(f"unexpected creation head: {current_head}")
    report: dict[str, Any] = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "bridge_page_scoring_authorization_recorded_no_promotion_no_scoring",
        "base_commit": CREATION_HEAD,
        "current_head": current_head,
        "input_lane_id": INPUT_LANE_ID,
        "pages": PAGES,
        "verified_inputs": verified_inputs,
        "candidate_pages": audit["input_fresh_ocr_candidate_pages"],
        "comparison_surface_pages": audit["reference_surface_pages"],
        "independent_truth_reference_pages": audit["independent_truth_reference_pages"],
        "bounded_comparison_only_pages": audit["bounded_comparison_only_pages"],
        "audit_fresh_ocr_success_pages": audit["fresh_ocr_success_pages"],
        "audit_promotable_pages": audit["promotable_pages"],
        "existing_audit_metrics_authorize_fresh_success": False,
        "existing_audit_metrics_authorize_promotion": False,
        "future_scoring_decision_authorized": True,
        "future_scoring_must_remain_bounded_to_pages": PAGES,
        "future_scoring_must_treat_003_004_as_low_authority": True,
        "future_scoring_must_treat_005_008_as_comparison_only_not_acceptance_truth": True,
        "future_scoring_may_reference_existing_candidate_hashes": True,
        "future_scoring_may_promote_without_separate_authority": False,
        "future_scoring_may_mutate_acceptance_or_production": False,
        "allowed_next_action": "separate_bounded_003_008_scoring_decision_or_remediation_strategy",
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
            "Pages `003-008` are authorized only for a future bounded scoring",
            "decision or remediation strategy. Existing diagnostic audit metrics do",
            "not authorize fresh OCR success or promotion.",
            "",
            "Pages `003/004` remain low-authority comparison surfaces; pages",
            "`005-008` remain comparison-only, not acceptance truth.",
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
        "- Output policy: report/summary/manifest only; no scoring, promotion, acceptance, production, OCR, or downstream execution.",
        "",
        "## Inputs",
        "",
    ]
    for key, item in report["verified_inputs"].items():
        lines.append(f"- `{key}`: `{item['sha256']}`")
    lines.extend(["", "## Outputs", ""])
    for name, item in hashes.items():
        lines.append(f"- `{name}`: `{item['sha256']}`")
    lines.extend(["", "## Decision", "", "- Existing audit metrics authorize fresh success: `false`", "- Existing audit metrics authorize promotion: `false`"])
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    check_authorization(argv)
    verified_inputs, audit = verify_inputs()
    report = build_report(verified_inputs, audit)
    write_json(OUT_ROOT / "bridge_page_scoring_authorization_003_008_report.json", report)
    write_text(OUT_ROOT / "bridge_page_scoring_authorization_003_008_summary.md", build_summary(report))
    write_text(OUT_ROOT / "bridge_page_scoring_authorization_003_008_manifest.md", build_manifest(report, output_hashes()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
