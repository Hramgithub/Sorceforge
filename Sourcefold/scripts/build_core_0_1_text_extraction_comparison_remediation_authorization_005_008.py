from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
STRATEGY_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_comparison_remediation_strategy_005_008_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_comparison_remediation_authorization_005_008_G1_VIRAL_001"

LANE_ID = "C01TEP005008REMAUTH-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP005008REMSTRAT-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-COMPARISON-REMEDIATION-AUTHORIZATION-005-008-001"
HUMAN_DECISION = "делай - не справишвай апрув на комит"

PAGES = ["005", "006", "007", "008"]

STRATEGY_INPUTS = {
    "C01TEP005008REMSTRAT-G1-VIRAL-001.report": (
        STRATEGY_ROOT / "comparison_remediation_strategy_005_008_report.json",
        "FFCEED1AF265E241A3C549DA7CE06B0631B6E02D9F4441FDB31188B708D6C843",
    ),
    "C01TEP005008REMSTRAT-G1-VIRAL-001.summary": (
        STRATEGY_ROOT / "comparison_remediation_strategy_005_008_summary.md",
        "70BF51FDA3E5B5C10AABBE1A3D0778B7FB83E6D54E3336EF4C61E27013D019F0",
    ),
    "C01TEP005008REMSTRAT-G1-VIRAL-001.manifest": (
        STRATEGY_ROOT / "comparison_remediation_strategy_005_008_manifest.md",
        "66351A7B8D6CF27501605F24E823827310B3114521C904FFDC06A1CA7A128925",
    ),
}


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
    parser = argparse.ArgumentParser(description="Build bounded 005-008 comparison remediation authorization.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("005-008 comparison remediation authorization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"005-008 comparison remediation authorization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("005-008 comparison remediation authorization requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in STRATEGY_INPUTS.items()}
    report = read_json(STRATEGY_INPUTS["C01TEP005008REMSTRAT-G1-VIRAL-001.report"][0])
    if report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected 005-008 remediation strategy input lane")
    if report["pages"] != PAGES:
        raise SystemExit(f"005-008 remediation strategy page set drifted: {report['pages']}")
    if report["strategy_scope"] != "comparison_only_remediation_strategy_for_pages_005_008":
        raise SystemExit("unexpected 005-008 remediation strategy scope")
    if report["remediation_execution_performed"] or report["scoring_execution_performed"]:
        raise SystemExit("input strategy unexpectedly performed remediation or scoring")
    if report["ocr_execution_performed"] or report["tesseract_invoked"]:
        raise SystemExit("input strategy unexpectedly performed OCR")
    if report["fresh_ocr_success_pages"] != [] or report["bridge_removed_pages"] != []:
        raise SystemExit("input strategy unexpectedly cleared bridge lineage")
    if report["comparison_only_evidence_becomes_acceptance_truth"]:
        raise SystemExit("input strategy promoted comparison evidence to acceptance truth")
    return verified, report


def output_hashes(paths: list[Path]) -> dict[str, dict[str, str]]:
    return {
        path.relative_to(OUT_ROOT).as_posix(): {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
        for path in paths
    }


def build() -> None:
    verified_inputs, strategy_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "comparison_only_remediation_authorized_no_execution",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "pages": PAGES,
        "verified_inputs": verified_inputs,
        "authorized_future_action": "separate_bounded_comparison_only_remediation_execution_for_pages_005_008",
        "authorized_candidate_inputs": {
            item["page"]: item["future_candidate_input"] for item in strategy_report["page_entries"]
        },
        "authorized_reference_surfaces": {
            item["page"]: item["future_reference_surface"] for item in strategy_report["page_entries"]
        },
        "authorized_future_remediation_families": strategy_report["future_remediation_families"],
        "normalization_contract_for_future_lane": strategy_report["normalization_contract_for_future_lane"],
        "future_metric_contract": strategy_report["future_metric_contract"],
        "comparison_surfaces_are_diagnostic_only": True,
        "comparison_only_evidence_becomes_acceptance_truth": False,
        "comparison_only_evidence_becomes_promotion_authority": False,
        "fresh_ocr_success_pages": [],
        "bridge_removed_pages": [],
        "promotable_pages": [],
        "remediation_execution_performed": False,
        "scoring_execution_performed": False,
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
        "allowed_next_action": "separate_bounded_comparison_only_remediation_execution_for_pages_005_008",
    }
    report_path = OUT_ROOT / "comparison_remediation_authorization_005_008_report.json"
    summary_path = OUT_ROOT / "comparison_remediation_authorization_005_008_summary.md"
    manifest_path = OUT_ROOT / "comparison_remediation_authorization_005_008_manifest.md"
    write_json(report_path, report)
    write_text(
        summary_path,
        "\n".join(
            [
                "# C01TEP005008REMAUTH-G1-VIRAL-001 Summary",
                "",
                "Status: `comparison_only_remediation_authorized_no_execution`",
                "",
                "This lane authorizes only a future bounded comparison-only remediation execution for pages `005`-`008`.",
                "It consumes committed `C01TEP005008REMSTRAT-G1-VIRAL-001` by exact output hashes.",
                "",
                "The lane does not execute remediation, scoring, OCR/Tesseract, render execution, PDF parsing, mutation, bridge removal, promotion, production, page `021+`, push, or downstream execution.",
                "Comparison surfaces remain diagnostic-only and do not become acceptance truth or promotion authority.",
                "",
            ]
        ),
    )
    manifest_lines = [
        "# C01TEP005008REMAUTH-G1-VIRAL-001 Manifest",
        "",
        "Boundary: authorization only; no remediation execution, scoring execution, OCR/Tesseract, acceptance, promotion, bridge removal, production, page `021+`, or source mutation.",
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
