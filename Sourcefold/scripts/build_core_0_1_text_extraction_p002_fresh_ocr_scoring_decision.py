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
AUDIT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit_G1_VIRAL_001"
FRESH_OCR_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_candidate_G1_VIRAL_001"
VERIFY_ROOT = TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_scoring_decision_G1_VIRAL_001"

LANE_ID = "C01TEP002FRESHDECIDE-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP002FRESHSCOREAUD-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-SCORING-DECISION-001"
HUMAN_DECISION = "двигайся"
THRESHOLD = 0.997

AUDIT_INPUTS = {
    "C01TEP002FRESHSCOREAUD-G1-VIRAL-001.report": (
        AUDIT_ROOT / "p002_fresh_ocr_scoring_reference_audit_report.json",
        "0834F4A864105F6D15D243198F743158C9D91ECDAF5AAEA4A4281913DD481740",
    ),
    "C01TEP002FRESHSCOREAUD-G1-VIRAL-001.summary": (
        AUDIT_ROOT / "p002_fresh_ocr_scoring_reference_audit_summary.md",
        "3E42702616B3C4F1267559290F9D4BE303DC1A5CDC342C10ED11F8E32C396D7E",
    ),
    "C01TEP002FRESHSCOREAUD-G1-VIRAL-001.manifest": (
        AUDIT_ROOT / "p002_fresh_ocr_scoring_reference_audit_manifest.md",
        "BF9B57598F7FAC66DEDFAF25D6CC1692C278AB9CA185BAC9DE06FD0AE4839FFB",
    ),
}

CANDIDATE_INPUTS = {
    "psm4": (
        FRESH_OCR_ROOT / "candidate_texts" / "page_002_full_page_psm4_candidate.md",
        "301EF78077B32935E17BCD113024AA2650A12867680286FF3439E873536395AC",
    ),
    "psm6": (
        FRESH_OCR_ROOT / "candidate_texts" / "page_002_full_page_psm6_candidate.md",
        "901EC2451AB5CC1465F7E2E57C20F4E31588FC00EE300D88BDA32E3AAD3DA7E9",
    ),
}

VERIFY_INPUTS = {
    "source_reconstruction_p002_assisted_draft_verify.report": (
        VERIFY_ROOT / "source_reconstruction_p002_assisted_draft_verify_report.json",
        "BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52",
    ),
    "source_reconstruction_p002_assisted_draft_verify.summary": (
        VERIFY_ROOT / "assisted_draft_human_verification_summary.md",
        "225DC38D81F9BD4133D05823ACDDBED538E5CBA790DEF1A33A4E4AFCCBF7E13D",
    ),
    "source_reconstruction_p002_assisted_draft_verify.manifest": (
        VERIFY_ROOT / "source_reconstruction_p002_assisted_draft_verify_manifest.md",
        "B6E3D871FCA061D1672CB5E73A1BFF6C73AAE7D0C7F8B2A7044BD451FAC9159A",
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
    parser = argparse.ArgumentParser(description="Build bounded P002 fresh OCR scoring decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR scoring decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR scoring decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR scoring decision requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in AUDIT_INPUTS.items()}
    audit_report = read_json(AUDIT_INPUTS["C01TEP002FRESHSCOREAUD-G1-VIRAL-001.report"][0])
    if audit_report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 scoring audit input lane")
    if audit_report["fresh_ocr_success_pages"] != []:
        raise SystemExit("input audit unexpectedly contains fresh OCR success")
    for label, (path, expected) in CANDIDATE_INPUTS.items():
        verified[f"candidate.{label}"] = verified_input(path, expected)
    for label, (path, expected) in VERIFY_INPUTS.items():
        verified[label] = verified_input(path, expected)
    verify_report = read_json(VERIFY_INPUTS["source_reconstruction_p002_assisted_draft_verify.report"][0])
    return verified, audit_report, verify_report


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


def metrics(candidate: str, reference: str) -> dict[str, Any]:
    candidate_norm = normalize_text(candidate)
    reference_norm = normalize_text(reference)
    ref_tokens = token_set(reference_norm)
    cand_tokens = token_set(candidate_norm)
    missing_tokens = sorted(ref_tokens - cand_tokens)
    extra_tokens = sorted(cand_tokens - ref_tokens)
    return {
        "sequence_similarity_ratio": round(difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio(), 6),
        "token_recall": round(len(ref_tokens & cand_tokens) / len(ref_tokens), 6) if ref_tokens else 0.0,
        "candidate_chars": len(candidate_norm),
        "reference_chars": len(reference_norm),
        "missing_reference_tokens_sample": missing_tokens[:20],
        "extra_candidate_tokens_sample": extra_tokens[:20],
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
    verified_inputs, audit_report, verify_report = verify_inputs()
    reference = verified_reference_text(verify_report)
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    entries = []
    for label, (path, candidate_hash) in CANDIDATE_INPUTS.items():
        page_metrics = metrics(path.read_text(encoding="utf-8-sig"), reference)
        entries.append(
            {
                "candidate_label": label,
                "candidate_text_path": path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": candidate_hash,
                "candidate_hash_verified_before_reference_load": True,
                "reference_surface": "source_reconstruction_p002_assisted_draft_verify.verified_text",
                "reference_surface_authority": "human_verified_source_reconstruction_comparison_only",
                "diagnostic_metrics": page_metrics,
                "strict_threshold": THRESHOLD,
                "threshold_met": page_metrics["sequence_similarity_ratio"] >= THRESHOLD
                and page_metrics["token_recall"] >= THRESHOLD,
                "fresh_ocr_success": False,
                "promotable": False,
                "bridge_removal_effect": "none",
            }
        )
    best = max(entries, key=lambda item: (item["diagnostic_metrics"]["sequence_similarity_ratio"], item["diagnostic_metrics"]["token_recall"]))
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_scoring_decision_completed_remediation_required",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "input_audit_status": audit_report["status"],
        "page": "002",
        "verified_inputs": verified_inputs,
        "reference_surface_authority": "human_verified_source_reconstruction_comparison_only_not_acceptance_truth",
        "candidate_entries": entries,
        "selected_best_candidate": best["candidate_label"],
        "selected_best_candidate_threshold_met": best["threshold_met"],
        "strict_threshold": THRESHOLD,
        "decision": "remediation_required_before_fresh_ocr_success",
        "fresh_ocr_success_pages": [],
        "bridge_removed_for_pages": [],
        "promotable_pages": [],
        "allowed_next_action": "bounded_p002_candidate_remediation_from_best_candidate_and_visual_verified_diffs",
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
    report_path = OUT_ROOT / "p002_fresh_ocr_scoring_decision_report.json"
    summary_path = OUT_ROOT / "p002_fresh_ocr_scoring_decision_summary.md"
    manifest_path = OUT_ROOT / "p002_fresh_ocr_scoring_decision_manifest.md"
    write_json(report_path, report)
    lines = [
        "# P002 Fresh OCR Scoring Decision - C01TEP002FRESHDECIDE-G1-VIRAL-001",
        "",
        "Status: `p002_fresh_ocr_scoring_decision_completed_remediation_required`",
        "",
        "| Candidate | Similarity | Token recall | Threshold met |",
        "|---|---:|---:|---|",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry['candidate_label']}` | `{entry['diagnostic_metrics']['sequence_similarity_ratio']}` | "
            f"`{entry['diagnostic_metrics']['token_recall']}` | `{str(entry['threshold_met']).lower()}` |"
        )
    lines.extend(
        [
            "",
            f"Best candidate: `{best['candidate_label']}`.",
            "Decision: remediation is required before any fresh OCR success or bridge removal.",
            "Reference surface is human-verified source-reconstruction comparison evidence, not acceptance truth in this lane.",
            "",
        ]
    )
    write_text(summary_path, "\n".join(lines))
    manifest_lines = [
        "# P002 Fresh OCR Scoring Decision Manifest - C01TEP002FRESHDECIDE-G1-VIRAL-001",
        "",
        "Boundary: scoring decision only; no OCR, acceptance, promotion, bridge removal, production, or source mutation.",
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
