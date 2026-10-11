from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
DECISION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_scoring_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization_G1_VIRAL_001"

LANE_ID = "C01TEP002FRESHREMAUTH-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP002FRESHDECIDE-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-REMEDIATION-AUTHORIZATION-001"
HUMAN_DECISION = "двигайся"

DECISION_INPUTS = {
    "C01TEP002FRESHDECIDE-G1-VIRAL-001.report": (
        DECISION_ROOT / "p002_fresh_ocr_scoring_decision_report.json",
        "C745B2EBF02001D0F4ACD4AD836DFC534C59B799911A2FAB96785CBB3F50471B",
    ),
    "C01TEP002FRESHDECIDE-G1-VIRAL-001.summary": (
        DECISION_ROOT / "p002_fresh_ocr_scoring_decision_summary.md",
        "7B72F72E6480BDDDD6FF61947F2425F8BB0E5DF8446AF1EEA56F3EDF02CD3D50",
    ),
    "C01TEP002FRESHDECIDE-G1-VIRAL-001.manifest": (
        DECISION_ROOT / "p002_fresh_ocr_scoring_decision_manifest.md",
        "0283F681EE24683AA6BBC6EA1F2818F7DC9680E6DCB8D56B1D91FCE476260713",
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
    parser = argparse.ArgumentParser(description="Build bounded P002 fresh OCR remediation authorization.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR remediation authorization is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR remediation authorization requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR remediation authorization requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in DECISION_INPUTS.items()}
    report = read_json(DECISION_INPUTS["C01TEP002FRESHDECIDE-G1-VIRAL-001.report"][0])
    if report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 scoring decision input lane")
    if report["selected_best_candidate"] != "psm4":
        raise SystemExit("unexpected P002 best candidate")
    if report["decision"] != "remediation_required_before_fresh_ocr_success":
        raise SystemExit("P002 scoring decision no longer requires remediation")
    if report["fresh_ocr_success_pages"] != [] or report["bridge_removed_for_pages"] != []:
        raise SystemExit("P002 scoring decision unexpectedly cleared bridge")
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
    verified_inputs, decision_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_remediation_authorized_no_execution",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "page": "002",
        "verified_inputs": verified_inputs,
        "authorized_future_action": "bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs",
        "authorized_best_candidate": decision_report["selected_best_candidate"],
        "authorized_reference_surface": "human_verified_source_reconstruction_comparison_only",
        "allowed_future_outputs": [
            "lane_owned_remediated_candidate_text",
            "lane_owned_remediation_report_summary_manifest",
        ],
        "fresh_ocr_success_pages": [],
        "bridge_removed_for_pages": [],
        "promotable_pages": [],
        "ocr_execution_performed": False,
        "tesseract_invoked": False,
        "remediation_execution_performed": False,
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
        "allowed_next_action": "separate_bounded_p002_fresh_ocr_remediation_execution",
    }
    report_path = OUT_ROOT / "p002_fresh_ocr_remediation_authorization_report.json"
    summary_path = OUT_ROOT / "p002_fresh_ocr_remediation_authorization_summary.md"
    manifest_path = OUT_ROOT / "p002_fresh_ocr_remediation_authorization_manifest.md"
    write_json(report_path, report)
    write_text(
        summary_path,
        "\n".join(
            [
                "# P002 Fresh OCR Remediation Authorization - C01TEP002FRESHREMAUTH-G1-VIRAL-001",
                "",
                "Status: `p002_fresh_ocr_remediation_authorized_no_execution`",
                "",
                "Authorizes a future bounded remediation execution for page `002` from best candidate `psm4` and visual-verified discrepancy evidence.",
                "This lane does not execute remediation, run OCR, clear bridge lineage, promote, accept, or create production output.",
                "",
            ]
        ),
    )
    manifest_lines = [
        "# P002 Fresh OCR Remediation Authorization Manifest - C01TEP002FRESHREMAUTH-G1-VIRAL-001",
        "",
        "Boundary: authorization only; no OCR, remediation execution, acceptance, promotion, bridge removal, production, or source mutation.",
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
