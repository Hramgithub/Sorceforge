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
REMEDIATION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_remediation_run_001_008_014_019_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_bridge_page_scoring_reference_audit_003_008_G1_VIRAL_001"

LANE_ID = "C01TEBRIDGESCOREAUD020-G1-VIRAL-001"
INPUT_LANE_ID = "C01TEBRIDGEREM020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-BRIDGE-PAGE-SCORING-REFERENCE-AUDIT-003-008-001"
HUMAN_DECISION = "Ок иди по плану, ты оркестратор, следи чтоб все было сделанл"
AUDIT_PAGES = ["003", "004", "005", "006", "007", "008"]
OUT_OF_SCOPE_PAGES = ["001", "002", "014", "019"]

REMEDIATION_INPUTS = {
    "C01TEBRIDGEREM020-G1-VIRAL-001.report": (
        REMEDIATION_ROOT / "bridge_page_remediation_run_001_008_014_019_report.json",
        "6A135FCBB5337BDADD4F59C23BB3F79A1FB077450524BADE7C90E8EA5FCA60CB",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.summary": (
        REMEDIATION_ROOT / "bridge_page_remediation_run_001_008_014_019_summary.md",
        "3161D2355BBA24C25E727E1914BCCDF8B49FCC56BBD979C818D6668B0F8A2124",
    ),
    "C01TEBRIDGEREM020-G1-VIRAL-001.manifest": (
        REMEDIATION_ROOT / "bridge_page_remediation_run_001_008_014_019_manifest.md",
        "BBC6A64419BC7B23EFCCF429D6DA17247B05CCAE3FE0EAF81FE593D9BE1362E5",
    ),
}

CANDIDATE_INPUTS = {
    "003": (
        REMEDIATION_ROOT / "candidate_texts" / "page_003_full_page_psm6_candidate.md",
        "7DD3AB82753B6887D4F23E173DE641B5333E9E00A7390CB8CF6372AE3B624B94",
    ),
    "004": (
        REMEDIATION_ROOT / "candidate_texts" / "page_004_full_page_psm6_candidate.md",
        "89A33BADB6D31AFF09C673D4FD38327416AEF39967B4886547B82EF6D70E9268",
    ),
    "005": (
        REMEDIATION_ROOT / "candidate_texts" / "page_005_full_page_psm6_candidate.md",
        "E8511E024041F4691D58AC8E17E6BC10B1D2BACA3B36AF3CEABDE02025FF7999",
    ),
    "006": (
        REMEDIATION_ROOT / "candidate_texts" / "page_006_full_page_psm6_candidate.md",
        "897533EA70B021368E2A7A5953082817C1F80997C564BD9D4535AFBE33D9C162",
    ),
    "007": (
        REMEDIATION_ROOT / "candidate_texts" / "page_007_full_page_psm6_candidate.md",
        "8A6405797F1F8E646059C64FA1CD54A4DA803B11B52BBAADADEC04CF59BE9F59",
    ),
    "008": (
        REMEDIATION_ROOT / "candidate_texts" / "page_008_full_page_psm6_candidate.md",
        "00E6C5700EA835552EBB6E1F1D8D776D4DD7AA7713018A7A74D6B992A01ACBE6",
    ),
}

REFERENCE_SURFACES = {
    "003": (
        TRIAL_ROOT / "page_complete_review_p003_G1_VIRAL_001" / "review_assets" / "page_003_ocr_block_text.md",
        "81BC5D2AB40C6C76BBC42940D727A2E9300CE9EB51009E6ED6718DF7B9E0DCEF",
        "page_complete_review_ocr_block_text_not_independent_truth",
    ),
    "004": (
        TRIAL_ROOT / "page_complete_review_p004_G1_VIRAL_001" / "review_assets" / "page_004_ocr_block_text.md",
        "7994F6D597C0041052361533BDDBCC63511B784F1BC24D6E7A089588BAAD3DDB",
        "page_complete_review_ocr_block_text_not_independent_truth",
    ),
    "005": (
        TRIAL_ROOT / "page_complete_review_p005_G1_VIRAL_004" / "review_assets" / "page_005_ocr_verified_text_map.md",
        "0EBCB8857B7AA09D0DB98BE82D7EAA407584CF03EDABCF4FED9C22DC3B17FB8E",
        "page_complete_review_ocr_verified_text_map_bounded_comparison",
    ),
    "006": (
        TRIAL_ROOT / "page_complete_review_p006_G1_VIRAL_002" / "review_assets" / "page_006_ocr_verified_text_map.md",
        "33CE4A5E34C80FFE36A5ACF8BF44D7E17CBFB1802BC125D3C3BE40A3696E124D",
        "page_complete_review_ocr_verified_text_map_bounded_comparison",
    ),
    "007": (
        TRIAL_ROOT / "page_complete_review_p007_G1_VIRAL_003" / "review_assets" / "page_007_ocr_verified_text_map.md",
        "4962CA14940D9841B8E284F6D2F43577D7B394D0A3764564AFE9848E15C09BE6",
        "page_complete_review_ocr_verified_text_map_bounded_comparison",
    ),
    "008": (
        TRIAL_ROOT / "page_complete_review_p008_G1_VIRAL_001" / "review_assets" / "page_008_ocr_verified_text_map.md",
        "3CC1E0850A77C7E5A24DC2F4E121C50A26C5D852422AD01C9DCE2D547A1D3981",
        "page_complete_review_ocr_verified_text_map_bounded_comparison",
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
    parser = argparse.ArgumentParser(description="Build bounded bridge-page scoring/reference audit for pages 003-008.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("bridge-page scoring/reference audit is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"bridge-page scoring/reference audit requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("bridge-page scoring/reference audit requires the exact bounded human decision")


def verified_input(path: Path, expected_hash: str) -> dict[str, str]:
    actual = sha256_file(path)
    if actual != expected_hash:
        raise SystemExit(f"{path.name} hash mismatch: {actual}")
    return {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict[str, Any]]:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified = {key: verified_input(path, expected) for key, (path, expected) in REMEDIATION_INPUTS.items()}
    report = read_json(REMEDIATION_INPUTS["C01TEBRIDGEREM020-G1-VIRAL-001.report"][0])
    if report["lane_id"] != INPUT_LANE_ID:
        raise SystemExit("unexpected remediation lane")
    if report["fresh_ocr_candidate_pages"] != AUDIT_PAGES:
        raise SystemExit("candidate page set drifted")
    for page in OUT_OF_SCOPE_PAGES:
        if page in report["fresh_ocr_candidate_pages"]:
            raise SystemExit(f"out-of-scope page {page} entered candidate set")
    for page, (path, expected) in CANDIDATE_INPUTS.items():
        verified[f"candidate.page_{page}"] = verified_input(path, expected)
    for page, (path, expected, _label) in REFERENCE_SURFACES.items():
        verified[f"reference.page_{page}"] = verified_input(path, expected)
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


def classify_surface(label: str) -> str:
    if label.endswith("bounded_comparison"):
        return "bounded_reference_comparison_surface_available_not_acceptance_truth"
    return "bounded_reference_comparison_surface_available_low_authority"


def audit_page(page: str) -> dict[str, Any]:
    candidate_path, candidate_hash = CANDIDATE_INPUTS[page]
    reference_path, reference_hash, reference_label = REFERENCE_SURFACES[page]
    page_metrics = metrics(
        candidate_path.read_text(encoding="utf-8-sig"),
        reference_path.read_text(encoding="utf-8-sig"),
    )
    return {
        "page": page,
        "page_id": f"P{page}",
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": candidate_hash,
        "candidate_hash_verified_before_reference_load": True,
        "reference_surface_path": reference_path.relative_to(ROOT).as_posix(),
        "reference_surface_sha256": reference_hash,
        "reference_label": reference_label,
        "reference_authority_classification": classify_surface(reference_label),
        "diagnostic_metrics": page_metrics,
        "scoring_performed": True,
        "scoring_scope": "diagnostic_comparison_only",
        "fresh_ocr_success": False,
        "promotable": False,
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
    verified_inputs, remediation_report = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    pages = [audit_page(page) for page in AUDIT_PAGES]
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "bridge_page_scoring_reference_audit_completed",
        "current_head": git_head(),
        "input_lane_id": INPUT_LANE_ID,
        "input_lane_base_commit_recorded": remediation_report["base_commit"],
        "input_fresh_ocr_candidate_pages": remediation_report["fresh_ocr_candidate_pages"],
        "audit_pages": AUDIT_PAGES,
        "out_of_scope_pages_rejected": OUT_OF_SCOPE_PAGES,
        "verified_inputs": verified_inputs,
        "page_entries": pages,
        "reference_surface_pages": AUDIT_PAGES,
        "independent_truth_reference_pages": [],
        "bounded_comparison_only_pages": AUDIT_PAGES,
        "fresh_ocr_success_pages": [],
        "promotable_pages": [],
        "all_audit_pages_have_pinned_reference_surface": True,
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
        "allowed_next_action": "bounded_candidate_scoring_authorization_or_page_002_source_asset_recovery",
    }
    report_path = OUT_ROOT / "bridge_page_scoring_reference_audit_003_008_report.json"
    summary_path = OUT_ROOT / "bridge_page_scoring_reference_audit_003_008_summary.md"
    manifest_path = OUT_ROOT / "bridge_page_scoring_reference_audit_003_008_manifest.md"
    write_json(report_path, report)
    lines = [
        "# Bridge Page Scoring Reference Audit 003-008 - C01TEBRIDGESCOREAUD020-G1-VIRAL-001",
        "",
        "Status: `bridge_page_scoring_reference_audit_completed`",
        "",
        "This lane audits pinned comparison/reference surfaces for the remediation candidates on pages `003`-`008` only.",
        "It does not run OCR, promote candidates, accept text, mutate source/raw/page-status assets, create production output, include page `021+`, push, or run downstream work.",
        "",
        "| Page | Reference class | Similarity | Token recall | Promotable |",
        "|---|---|---:|---:|---|",
    ]
    for item in pages:
        lines.append(
            f"| `{item['page']}` | `{item['reference_authority_classification']}` | "
            f"`{item['diagnostic_metrics']['sequence_similarity_ratio']}` | "
            f"`{item['diagnostic_metrics']['token_recall']}` | `false` |"
        )
    lines.extend(
        [
            "",
            "All pages have pinned comparison surfaces, but none are treated as independent acceptance truth in this lane.",
            "Fresh OCR success remains empty until a separately authorized scoring/promotion decision exists.",
            "",
        ]
    )
    write_text(summary_path, "\n".join(lines))
    manifest_lines = [
        "# Bridge Page Scoring Reference Audit 003-008 Manifest - C01TEBRIDGESCOREAUD020-G1-VIRAL-001",
        "",
        "Boundary: diagnostic comparison audit only; no OCR, acceptance, promotion, production, or source mutation.",
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
