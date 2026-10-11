from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
REMEDIATION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_remediation_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_pass_decision_G1_VIRAL_001"

LANE_ID = "C01TEP002FRESHPASS-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP002FRESHREM-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-PASS-DECISION-001"
HUMAN_DECISION = "двигайемся дальше"

REMEDIATION_INPUTS = {
    "C01TEP002FRESHREM-G1-VIRAL-001.report": (
        REMEDIATION_ROOT / "p002_fresh_ocr_remediation_report.json",
        "F4A650F37B28B89787DF81D95B7526BFBDD513DFC91175895644C9E2C67C5551",
    ),
    "C01TEP002FRESHREM-G1-VIRAL-001.summary": (
        REMEDIATION_ROOT / "p002_fresh_ocr_remediation_summary.md",
        "D4A84A7FB795B87F4D21E5753D30B9CEB9F1949B1B3A81F0F9A545354F216F52",
    ),
    "C01TEP002FRESHREM-G1-VIRAL-001.manifest": (
        REMEDIATION_ROOT / "p002_fresh_ocr_remediation_manifest.md",
        "9BFA3E92BBD3953A5B2290D0CB31AFC89780ED963726F63DA08B8AE09668379F",
    ),
    "C01TEP002FRESHREM-G1-VIRAL-001.remediated_candidate": (
        REMEDIATION_ROOT / "candidate_texts" / "page_002_full_page_psm4_remediated_candidate.md",
        "E8D84506A1069EFD417028A65132F0E378C90010E421B645E593215152EA9B7C",
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
    parser = argparse.ArgumentParser(description="Build bounded P002 fresh OCR pass decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR pass decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR pass decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR pass decision requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in REMEDIATION_INPUTS.items()}
    report = read_json(REMEDIATION_INPUTS["C01TEP002FRESHREM-G1-VIRAL-001.report"][0])
    if report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 remediation input lane")
    if report["threshold_met_after_remediation"] is not True:
        raise SystemExit("P002 remediation threshold not met")
    if report["fresh_ocr_success_pages"] != [] or report["bridge_removed_for_pages"] != []:
        raise SystemExit("P002 remediation lane already changed pass state")
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
    verified_inputs, remediation_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_pass_decision_completed",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "page": "002",
        "verified_inputs": verified_inputs,
        "decision_basis": {
            "threshold_met_after_remediation": True,
            "sequence_similarity_ratio": remediation_report["diagnostic_metrics_after_remediation"]["sequence_similarity_ratio"],
            "token_recall": remediation_report["diagnostic_metrics_after_remediation"]["token_recall"],
            "remediated_candidate_text_sha256": remediation_report["remediated_candidate_text_sha256"],
        },
        "fresh_ocr_success_pages": ["002"],
        "bridge_removed_for_pages": ["002"],
        "promotable_pages": ["002"],
        "fresh_ocr_success": True,
        "bridge_blocker_cleared": True,
        "production_ready": False,
        "production_assembly_authorized": False,
        "production_assembly_created": False,
        "acceptance_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "fixture_admission_performed": False,
        "ocr_execution_performed": False,
        "tesseract_invoked": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "downstream_execution_performed": False,
        "allowed_next_action": "refresh_clean_001_020_runtime_selector_or_continue_remaining_page_pass_decisions",
    }
    report_path = OUT_ROOT / "p002_fresh_ocr_pass_decision_report.json"
    summary_path = OUT_ROOT / "p002_fresh_ocr_pass_decision_summary.md"
    manifest_path = OUT_ROOT / "p002_fresh_ocr_pass_decision_manifest.md"
    write_json(report_path, report)
    write_text(
        summary_path,
        "\n".join(
            [
                "# P002 Fresh OCR Pass Decision - C01TEP002FRESHPASS-G1-VIRAL-001",
                "",
                "Status: `p002_fresh_ocr_pass_decision_completed`",
                "",
                "Page `002` is recorded as fresh OCR success for the bounded first-pass remediation path.",
                "Bridge removal is recorded for page `002` only.",
                "No acceptance, production assembly, source/raw/page-status mutation, fixture admission, page `021+`, push, or downstream execution is created.",
                "",
            ]
        ),
    )
    manifest_lines = [
        "# P002 Fresh OCR Pass Decision Manifest - C01TEP002FRESHPASS-G1-VIRAL-001",
        "",
        "Boundary: pass decision only; no acceptance, production, fixture admission, source mutation, push, or downstream execution.",
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
