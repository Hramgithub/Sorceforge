from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_remediation_authorization_G1_VIRAL_001"
CANDIDATE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_candidate_G1_VIRAL_001"
VERIFY_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_remediation_G1_VIRAL_001"

LANE_ID = "C01TEP002FRESHREM-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP002FRESHREMAUTH-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-REMEDIATION-001"
HUMAN_DECISION = "двигайемся дальше"
THRESHOLD = 0.997

AUTH_INPUTS = {
    "C01TEP002FRESHREMAUTH-G1-VIRAL-001.report": (
        AUTH_ROOT / "p002_fresh_ocr_remediation_authorization_report.json",
        "42ABC318A2B283F27CDCA13AE14FAF26C1256F71BA1B0BE263E4448E00BD49FF",
    ),
    "C01TEP002FRESHREMAUTH-G1-VIRAL-001.summary": (
        AUTH_ROOT / "p002_fresh_ocr_remediation_authorization_summary.md",
        "17F1B59A17E229965712CB5B21E64EFC9703F7EBDB5768E17475066492F76A05",
    ),
    "C01TEP002FRESHREMAUTH-G1-VIRAL-001.manifest": (
        AUTH_ROOT / "p002_fresh_ocr_remediation_authorization_manifest.md",
        "F9E54880261ACC456F5FA9116F6A15743E2741FAEBC5481CFD2396DD7CF131A8",
    ),
}

PSM4_CANDIDATE = (
    CANDIDATE_ROOT / "candidate_texts" / "page_002_full_page_psm4_candidate.md",
    "301EF78077B32935E17BCD113024AA2650A12867680286FF3439E873536395AC",
)

VERIFY_REPORT = (
    VERIFY_ROOT / "source_reconstruction_p002_assisted_draft_verify_report.json",
    "BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52",
)


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
    parser = argparse.ArgumentParser(description="Run bounded P002 fresh OCR remediation.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR remediation is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR remediation requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR remediation requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in AUTH_INPUTS.items()}
    auth_report = read_json(AUTH_INPUTS["C01TEP002FRESHREMAUTH-G1-VIRAL-001.report"][0])
    if auth_report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 remediation authorization lane")
    if auth_report["authorized_best_candidate"] != "psm4":
        raise SystemExit("unexpected authorized best candidate")
    if auth_report["allowed_next_action"] != "separate_bounded_p002_fresh_ocr_remediation_execution":
        raise SystemExit("unexpected remediation authorization next action")
    verified["candidate.psm4"] = verified_input(*PSM4_CANDIDATE)
    verified["source_reconstruction_p002_assisted_draft_verify.report"] = verified_input(*VERIFY_REPORT)
    return verified, auth_report


def normalize_text(text: str) -> str:
    text = text.replace("©", "(C)").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", text).strip().lower()


def token_set(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", normalize_text(text)))


def verified_reference_text(report: dict[str, Any]) -> str:
    texts: list[str] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                if key == "verified_text":
                    texts.append(str(item))
                else:
                    walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(report)
    if not texts:
        raise SystemExit("verified_text reference surface missing")
    return "\n\n".join(texts)


def remediate(candidate: str) -> tuple[str, list[dict[str, str]]]:
    operations: list[dict[str, str]] = []
    remediated = candidate
    if not normalize_text(remediated).startswith("credits writing"):
        remediated = "Credits\n\n" + remediated
        operations.append({"operation": "insert_missing_header", "value": "Credits"})
    if "Dragongirl74" in remediated:
        remediated = remediated.replace("Dragongirl74", "Dragongirl174")
        operations.append({"operation": "replace_visual_verified_token", "from": "Dragongirl74", "to": "Dragongirl174"})
    return remediated, operations


def metrics(candidate: str, reference: str) -> dict[str, Any]:
    candidate_norm = normalize_text(candidate)
    reference_norm = normalize_text(reference)
    ref_tokens = token_set(reference_norm)
    cand_tokens = token_set(candidate_norm)
    return {
        "sequence_similarity_ratio": round(difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio(), 6),
        "token_recall": round(len(ref_tokens & cand_tokens) / len(ref_tokens), 6) if ref_tokens else 0.0,
        "candidate_chars": len(candidate_norm),
        "reference_chars": len(reference_norm),
        "threshold_met": difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio() >= THRESHOLD
        and (len(ref_tokens & cand_tokens) / len(ref_tokens) if ref_tokens else 0.0) >= THRESHOLD,
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
    verified_inputs, auth_report = verify_inputs()
    candidate_text = PSM4_CANDIDATE[0].read_text(encoding="utf-8-sig")
    reference_text = verified_reference_text(read_json(VERIFY_REPORT[0]))
    remediated_text, operations = remediate(candidate_text)
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    candidate_path = OUT_ROOT / "candidate_texts" / "page_002_full_page_psm4_remediated_candidate.md"
    write_text(candidate_path, remediated_text)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_remediation_executed_candidate_only",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "page": "002",
        "verified_inputs": verified_inputs,
        "source_candidate": "psm4",
        "remediation_operations": operations,
        "remediated_candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "remediated_candidate_text_sha256": sha256_file(candidate_path),
        "diagnostic_metrics_after_remediation": metrics(remediated_text, reference_text),
        "threshold_met_after_remediation": metrics(remediated_text, reference_text)["threshold_met"],
        "fresh_ocr_success_pages": [],
        "bridge_removed_for_pages": [],
        "promotable_pages": [],
        "fresh_ocr_success": False,
        "bridge_blocker_cleared": False,
        "reference_surface_authority": "human_verified_source_reconstruction_comparison_only_not_acceptance_truth",
        "allowed_next_action": "separate_bounded_p002_remediated_candidate_pass_decision",
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
    report_path = OUT_ROOT / "p002_fresh_ocr_remediation_report.json"
    summary_path = OUT_ROOT / "p002_fresh_ocr_remediation_summary.md"
    manifest_path = OUT_ROOT / "p002_fresh_ocr_remediation_manifest.md"
    write_json(report_path, report)
    summary_lines = [
        "# P002 Fresh OCR Remediation - C01TEP002FRESHREM-G1-VIRAL-001",
        "",
        "Status: `p002_fresh_ocr_remediation_executed_candidate_only`",
        "",
        f"Operations: `{', '.join(item['operation'] for item in operations)}`",
        f"Similarity after remediation: `{report['diagnostic_metrics_after_remediation']['sequence_similarity_ratio']}`",
        f"Token recall after remediation: `{report['diagnostic_metrics_after_remediation']['token_recall']}`",
        f"Threshold met after remediation: `{str(report['threshold_met_after_remediation']).lower()}`",
        "",
        "Fresh OCR success, bridge removal, promotion, acceptance, and production remain false until a separate pass decision lane.",
        "",
    ]
    write_text(summary_path, "\n".join(summary_lines))
    manifest_lines = [
        "# P002 Fresh OCR Remediation Manifest - C01TEP002FRESHREM-G1-VIRAL-001",
        "",
        "Boundary: remediation candidate only; no OCR, acceptance, promotion, bridge removal, production, or source mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes([candidate_path, report_path, summary_path]).items():
        manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(manifest_path, "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
