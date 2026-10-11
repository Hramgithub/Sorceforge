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
FRESH_OCR_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_candidate_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p002_fresh_ocr_scoring_reference_audit_G1_VIRAL_001"

LANE_ID = "C01TEP002FRESHSCOREAUD-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP002FRESHOCR-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P002-FRESH-OCR-SCORING-REFERENCE-AUDIT-001"
HUMAN_DECISION = "двигайся"
AUDIT_PAGE = "002"

FRESH_OCR_INPUTS = {
    "C01TEP002FRESHOCR-G1-VIRAL-001.report": (
        FRESH_OCR_ROOT / "p002_fresh_ocr_candidate_report.json",
        "5686F161296BD696E8F97B00DB9560F2374E6FAC74B4DA223490FF2ECFC473D2",
    ),
    "C01TEP002FRESHOCR-G1-VIRAL-001.summary": (
        FRESH_OCR_ROOT / "p002_fresh_ocr_candidate_summary.md",
        "4AE2AE00372FADB5E523982A438ABDDAD69F5CB6EA8EB5F706A2D87FA399A3A5",
    ),
    "C01TEP002FRESHOCR-G1-VIRAL-001.manifest": (
        FRESH_OCR_ROOT / "p002_fresh_ocr_candidate_manifest.md",
        "FEE45C27C759FCCBD67DF2CC44B8F65D4249644FCC3DA9A289612FBDC721B155",
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

REFERENCE_SURFACES = {
    "page_complete_review_packet": (
        TRIAL_ROOT / "page_complete_review_p002_G1_VIRAL_001" / "page_complete_review_packet.md",
        "C1BE97EB71B950FD423C805457F0CA60367C1BB4759E7C63A0DA9D175293268C",
        "page_complete_review_packet_bounded_comparison_not_independent_truth",
    ),
    "page_map_readiness_packet": (
        TRIAL_ROOT / "page_map_readiness_p002_G1_VIRAL_001" / "page_map_readiness_packet.md",
        "5DAAB049DC28C9C4633490348991DF822FF8E049460AC0978EBF8163D75C1734",
        "page_map_readiness_packet_advisory_comparison_not_acceptance_truth",
    ),
    "page_complete_acceptance_record": (
        TRIAL_ROOT / "page_complete_acceptance_p002_G1_VIRAL_001" / "page_complete_acceptance_record.md",
        "3FF1AC29BA8CBCDED3AA8757CDD87713B0EC26011B32A528127C54C572E1EDDE",
        "historical_page_complete_acceptance_record_comparison_only_not_fresh_ocr_truth",
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
    parser = argparse.ArgumentParser(description="Build bounded P002 fresh OCR scoring/reference audit.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P002 fresh OCR scoring/reference audit is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P002 fresh OCR scoring/reference audit requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P002 fresh OCR scoring/reference audit requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in FRESH_OCR_INPUTS.items()}
    report = read_json(FRESH_OCR_INPUTS["C01TEP002FRESHOCR-G1-VIRAL-001.report"][0])
    if report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected P002 fresh OCR input lane")
    if report["page"] != AUDIT_PAGE:
        raise SystemExit("unexpected P002 audit page")
    if report["candidate_count"] != 2:
        raise SystemExit("P002 candidate count drifted")
    if report["candidate_hash_sealed_before_reference_scoring"] is not True:
        raise SystemExit("candidate hashes were not sealed before reference/scoring")
    if report["reference_scoring_performed"] is not False:
        raise SystemExit("input lane already performed reference scoring")
    for label, (path, expected) in CANDIDATE_INPUTS.items():
        verified[f"candidate.{label}"] = verified_input(path, expected)
    for label, (path, expected, _surface_label) in REFERENCE_SURFACES.items():
        verified[f"reference.{label}"] = verified_input(path, expected)
    return verified, report


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def token_set(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9']+", normalize_text(text)))


def metrics(candidate: str, reference: str) -> dict[str, Any]:
    candidate_norm = normalize_text(candidate)
    reference_norm = normalize_text(reference)
    ref_tokens = token_set(reference_norm)
    cand_tokens = token_set(candidate_norm)
    return {
        "sequence_similarity_ratio": round(difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio(), 6)
        if reference_norm
        else 0.0,
        "token_recall": round(len(ref_tokens & cand_tokens) / len(ref_tokens), 6) if ref_tokens else 0.0,
        "candidate_chars": len(candidate_norm),
        "reference_chars": len(reference_norm),
    }


def candidate_entry(label: str) -> dict[str, Any]:
    candidate_path, candidate_hash = CANDIDATE_INPUTS[label]
    candidate_text = candidate_path.read_text(encoding="utf-8-sig")
    reference_entries = []
    for ref_label, (reference_path, reference_hash, authority_label) in REFERENCE_SURFACES.items():
        reference_entries.append(
            {
                "reference_label": ref_label,
                "reference_surface_path": reference_path.relative_to(ROOT).as_posix(),
                "reference_surface_sha256": reference_hash,
                "reference_authority_label": authority_label,
                "reference_authority_classification": "bounded_comparison_only_not_acceptance_truth",
                "diagnostic_metrics": metrics(candidate_text, reference_path.read_text(encoding="utf-8-sig")),
            }
        )
    return {
        "page": AUDIT_PAGE,
        "candidate_label": label,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": candidate_hash,
        "candidate_hash_verified_before_reference_load": True,
        "reference_entries": reference_entries,
        "scoring_performed": True,
        "scoring_scope": "diagnostic_comparison_only",
        "fresh_ocr_success": False,
        "promotable": False,
        "bridge_removal_effect": "none",
        "acceptance_effect": "none",
        "promotion_effect": "none",
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
    verified_inputs, candidate_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    candidates = [candidate_entry(label) for label in CANDIDATE_INPUTS]
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "p002_fresh_ocr_scoring_reference_audit_completed",
        "base_commit": candidate_report["base_commit"],
        "current_head": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "page": AUDIT_PAGE,
        "verified_inputs": verified_inputs,
        "candidate_labels": list(CANDIDATE_INPUTS),
        "reference_surface_labels": list(REFERENCE_SURFACES),
        "reference_surface_pages": [AUDIT_PAGE],
        "independent_truth_reference_pages": [],
        "bounded_comparison_only_pages": [AUDIT_PAGE],
        "candidate_entries": candidates,
        "fresh_ocr_success_pages": [],
        "promotable_pages": [],
        "bridge_removed_for_pages": [],
        "all_candidates_have_pinned_reference_surfaces": True,
        "reference_scoring_performed": True,
        "scoring_scope": "diagnostic_comparison_only",
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
        "allowed_next_action": "separate_bounded_p002_candidate_scoring_or_remediation_decision",
    }
    report_path = OUT_ROOT / "p002_fresh_ocr_scoring_reference_audit_report.json"
    summary_path = OUT_ROOT / "p002_fresh_ocr_scoring_reference_audit_summary.md"
    manifest_path = OUT_ROOT / "p002_fresh_ocr_scoring_reference_audit_manifest.md"
    write_json(report_path, report)
    lines = [
        "# P002 Fresh OCR Scoring Reference Audit - C01TEP002FRESHSCOREAUD-G1-VIRAL-001",
        "",
        "Status: `p002_fresh_ocr_scoring_reference_audit_completed`",
        "",
        "This lane audits pinned comparison/reference surfaces for the page `002` fresh OCR candidates only.",
        "It does not run OCR, promote candidates, remove bridge lineage, accept text, mutate source/raw/page-status assets, create production output, include page `021+`, push, or run downstream work.",
        "",
        "| Candidate | Reference | Similarity | Token recall | Promotable |",
        "|---|---|---:|---:|---|",
    ]
    for candidate in candidates:
        for ref in candidate["reference_entries"]:
            lines.append(
                f"| `{candidate['candidate_label']}` | `{ref['reference_label']}` | "
                f"`{ref['diagnostic_metrics']['sequence_similarity_ratio']}` | "
                f"`{ref['diagnostic_metrics']['token_recall']}` | `false` |"
            )
    lines.extend(
        [
            "",
            "All reference surfaces are comparison-only. None are treated as independent acceptance truth in this lane.",
            "Fresh OCR success remains empty until a separately authorized scoring/remediation decision exists.",
            "",
        ]
    )
    write_text(summary_path, "\n".join(lines))
    manifest_lines = [
        "# P002 Fresh OCR Scoring Reference Audit Manifest - C01TEP002FRESHSCOREAUD-G1-VIRAL-001",
        "",
        "Boundary: diagnostic comparison audit only; no OCR, acceptance, promotion, bridge removal, production, or source mutation.",
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
