from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import unicodedata
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_comparison_remediation_authorization_005_008_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_comparison_remediation_execution_005_008_G1_VIRAL_001"

LANE_ID = "C01TEP005008REMEXEC-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEP005008REMAUTH-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-COMPARISON-REMEDIATION-EXECUTION-005-008-001"
HUMAN_DECISION = "ок го"
PAGES = ["005", "006", "007", "008"]

AUTH_INPUTS = {
    "C01TEP005008REMAUTH-G1-VIRAL-001.report": (
        AUTH_ROOT / "comparison_remediation_authorization_005_008_report.json",
        "2616AE83F41A1F78911F5A8652EE8AF0CA01F20A2155E28F568082CF3D98E38B",
    ),
    "C01TEP005008REMAUTH-G1-VIRAL-001.summary": (
        AUTH_ROOT / "comparison_remediation_authorization_005_008_summary.md",
        "07D7F438F9E881B18D3CC2A7EAD1B2EAB6667ED128DABF87106A25E409F9728E",
    ),
    "C01TEP005008REMAUTH-G1-VIRAL-001.manifest": (
        AUTH_ROOT / "comparison_remediation_authorization_005_008_manifest.md",
        "53A182226919CDCA4CC347EC48D65A48C1F959BF57DF0A1D9667DB480FE4C898",
    ),
}

CANDIDATE_INPUTS = {
    "005": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "candidate_texts"
        / "page_005_full_page_psm6_candidate.md",
        "E8511E024041F4691D58AC8E17E6BC10B1D2BACA3B36AF3CEABDE02025FF7999",
    ),
    "006": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "candidate_texts"
        / "page_006_full_page_psm6_candidate.md",
        "897533EA70B021368E2A7A5953082817C1F80997C564BD9D4535AFBE33D9C162",
    ),
    "007": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "candidate_texts"
        / "page_007_full_page_psm6_candidate.md",
        "8A6405797F1F8E646059C64FA1CD54A4DA803B11B52BBAADADEC04CF59BE9F59",
    ),
    "008": (
        TRIAL_ROOT
        / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
        / "candidate_texts"
        / "page_008_full_page_psm6_candidate.md",
        "00E6C5700EA835552EBB6E1F1D8D776D4DD7AA7713018A7A74D6B992A01ACBE6",
    ),
}

REFERENCE_INPUTS = {
    "005": (
        TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_004" / "review_assets" / "page_005_ocr_verified_text_map.md",
        "0EBCB8857B7AA09D0DB98BE82D7EAA407584CF03EDABCF4FED9C22DC3B17FB8E",
    ),
    "006": (
        TRIAL_ROOT / "page_complete_review_p006_G1_VIRAL_002" / "review_assets" / "page_006_ocr_verified_text_map.md",
        "33CE4A5E34C80FFE36A5ACF8BF44D7E17CBFB1802BC125D3C3BE40A3696E124D",
    ),
    "007": (
        TRIAL_ROOT / "page_complete_review_p007_G1_VIRAL_003" / "review_assets" / "page_007_ocr_verified_text_map.md",
        "4962CA14940D9841B8E284F6D2F43577D7B394D0A3764564AFE9848E15C09BE6",
    ),
    "008": (
        TRIAL_ROOT / "page_complete_review_p008_G1_VIRAL_001" / "review_assets" / "page_008_ocr_verified_text_map.md",
        "3CC1E0850A77C7E5A24DC2F4E121C50A26C5D852422AD01C9DCE2D547A1D3981",
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
    parser = argparse.ArgumentParser(description="Run bounded 005-008 comparison-only remediation execution.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("005-008 comparison-only remediation execution is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"005-008 comparison-only remediation execution requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("005-008 comparison-only remediation execution requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in AUTH_INPUTS.items()}
    report = read_json(AUTH_INPUTS["C01TEP005008REMAUTH-G1-VIRAL-001.report"][0])
    if report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected 005-008 remediation authorization lane")
    if report["pages"] != PAGES:
        raise SystemExit(f"authorization page set drifted: {report['pages']}")
    if report["allowed_next_action"] != "separate_bounded_comparison_only_remediation_execution_for_pages_005_008":
        raise SystemExit("authorization no longer allows 005-008 remediation execution")
    if report["remediation_execution_performed"] or report["scoring_execution_performed"]:
        raise SystemExit("authorization unexpectedly executed remediation or scoring")
    if report["ocr_execution_performed"] or report["tesseract_invoked"]:
        raise SystemExit("authorization unexpectedly executed OCR")
    for page, (path, expected) in CANDIDATE_INPUTS.items():
        verified[f"candidate.page_{page}"] = verified_input(path, expected)
    for page, (path, expected) in REFERENCE_INPUTS.items():
        verified[f"reference.page_{page}"] = verified_input(path, expected)
    return verified, report


def normalize_for_metric(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\s+", " ", text).strip()


def token_set(text: str) -> set[str]:
    return set(re.findall(r"[A-Za-z0-9']+", normalize_for_metric(text)))


def metrics(candidate: str, reference: str) -> dict[str, Any]:
    candidate_norm = normalize_for_metric(candidate)
    reference_norm = normalize_for_metric(reference)
    ref_tokens = token_set(reference)
    cand_tokens = token_set(candidate)
    ratio = difflib.SequenceMatcher(None, candidate_norm, reference_norm).ratio() if reference_norm else 0.0
    recall = len(ref_tokens & cand_tokens) / len(ref_tokens) if ref_tokens else 0.0
    return {
        "sequence_similarity_ratio": round(ratio, 6),
        "token_recall": round(recall, 6),
        "candidate_chars": len(candidate_norm),
        "reference_chars": len(reference_norm),
        "threshold_met": ratio >= 0.997 and recall >= 0.993,
    }


def remediate_candidate(text: str) -> tuple[str, list[dict[str, Any]]]:
    original = text
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.strip() for line in text.split("\n")]
    collapsed_lines: list[str] = []
    blank_seen = False
    for line in lines:
        line = re.sub(r"[ \t]+", " ", line)
        if not line:
            if not blank_seen and collapsed_lines:
                collapsed_lines.append("")
            blank_seen = True
            continue
        collapsed_lines.append(line)
        blank_seen = False
    remediated = "\n".join(collapsed_lines).strip() + "\n"
    operations = [
        {
            "operation": "nfkc_lf_trim_collapse_whitespace",
            "reference_tokens_inserted": False,
            "candidate_chars_before": len(original),
            "candidate_chars_after": len(remediated),
        }
    ]
    return remediated, operations


def output_hashes(paths: list[Path]) -> dict[str, dict[str, str]]:
    return {
        path.relative_to(OUT_ROOT).as_posix(): {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
        for path in paths
    }


def build_page(page: str) -> dict[str, Any]:
    candidate_path, candidate_hash = CANDIDATE_INPUTS[page]
    reference_path, reference_hash = REFERENCE_INPUTS[page]
    candidate_text = candidate_path.read_text(encoding="utf-8-sig")
    remediated_text, operations = remediate_candidate(candidate_text)
    out_candidate_path = OUT_ROOT / "candidate_texts" / f"page_{page}_comparison_remediated_candidate.md"
    write_text(out_candidate_path, remediated_text)
    remediated_hash = sha256_file(out_candidate_path)
    reference_text = reference_path.read_text(encoding="utf-8-sig")
    page_metrics = metrics(remediated_text, reference_text)
    trace = {
        "page": page,
        "source_candidate_path": candidate_path.relative_to(ROOT).as_posix(),
        "source_candidate_sha256": candidate_hash,
        "remediated_candidate_path": out_candidate_path.relative_to(ROOT).as_posix(),
        "remediated_candidate_sha256": remediated_hash,
        "candidate_hash_sealed_before_reference_load": True,
        "reference_surface_path": reference_path.relative_to(ROOT).as_posix(),
        "reference_surface_sha256": reference_hash,
        "reference_surface_authority": "ocr_verified_text_map_comparison_only_not_acceptance_truth",
        "operations": operations,
        "diagnostic_metrics_after_remediation": page_metrics,
        "diagnostic_scoring_performed_after_candidate_hash_seal": True,
        "fresh_ocr_success": False,
        "bridge_removed": False,
        "promotable": False,
        "acceptance_effect": "none",
        "promotion_effect": "none",
    }
    trace_path = OUT_ROOT / "traces" / f"page_{page}_comparison_remediation_trace.json"
    write_json(trace_path, trace)
    trace["trace_path"] = trace_path.relative_to(ROOT).as_posix()
    trace["trace_sha256"] = sha256_file(trace_path)
    return trace


def build() -> None:
    verified_inputs, auth_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    page_entries = [build_page(page) for page in PAGES]
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "comparison_only_remediation_execution_completed_candidate_only",
        "base_commit": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "pages": PAGES,
        "verified_inputs": verified_inputs,
        "authorization_base_commit_recorded": auth_report["base_commit"],
        "page_entries": page_entries,
        "remediated_candidate_pages": PAGES,
        "fresh_ocr_success_pages": [],
        "bridge_removed_pages": [],
        "promotable_pages": [],
        "comparison_surfaces_are_diagnostic_only": True,
        "comparison_only_evidence_becomes_acceptance_truth": False,
        "comparison_only_evidence_becomes_promotion_authority": False,
        "remediation_execution_performed": True,
        "diagnostic_scoring_performed": True,
        "diagnostic_scoring_scope": "post_remediation_comparison_only_after_candidate_hash_seal",
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
        "allowed_next_action": "separate_bounded_post_remediation_diagnostic_decision_for_pages_005_008",
    }
    report_path = OUT_ROOT / "comparison_remediation_execution_005_008_report.json"
    summary_path = OUT_ROOT / "comparison_remediation_execution_005_008_summary.md"
    manifest_path = OUT_ROOT / "comparison_remediation_execution_005_008_manifest.md"
    write_json(report_path, report)
    summary_lines = [
        "# C01TEP005008REMEXEC-G1-VIRAL-001 Summary",
        "",
        "Status: `comparison_only_remediation_execution_completed_candidate_only`",
        "",
        "This lane materializes comparison-only remediated candidate outputs for pages `005`-`008` from existing candidate text.",
        "It does not run OCR/Tesseract, render, parse PDF, mutate source/raw/accepted/page-status state, remove bridge lineage, promote, accept, assemble production, include page `021+`, push, or trigger downstream execution.",
        "",
        "| Page | Similarity after remediation | Token recall after remediation | Threshold met |",
        "|---|---:|---:|---|",
    ]
    for item in page_entries:
        metric = item["diagnostic_metrics_after_remediation"]
        summary_lines.append(
            f"| `{item['page']}` | `{metric['sequence_similarity_ratio']}` | `{metric['token_recall']}` | `{str(metric['threshold_met']).lower()}` |"
        )
    summary_lines.extend(
        [
            "",
            "Fresh OCR success, bridge removal, promotion, acceptance, and production remain false until a separate reviewed decision lane.",
            "",
        ]
    )
    write_text(summary_path, "\n".join(summary_lines))
    manifest_lines = [
        "# C01TEP005008REMEXEC-G1-VIRAL-001 Manifest",
        "",
        "Boundary: comparison-only remediation candidate outputs; no OCR/Tesseract, acceptance, promotion, bridge removal, production, or source mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    output_paths = [Path(item["remediated_candidate_path"]) for item in page_entries]
    output_paths.extend(Path(item["trace_path"]) for item in page_entries)
    output_paths.extend([report_path.relative_to(ROOT), summary_path.relative_to(ROOT)])
    for rel_path, item in output_hashes([ROOT / path for path in output_paths]).items():
        manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(manifest_path, "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
