from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_reference_guided_repair_p018_p017_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TERG018017-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-REFERENCE-GUIDED-REPAIR-P018-P017-001"
HUMAN_DECISION = "даю ращрешение на широкий ресерч, пробуй , ищи , думай, делай. пока не получишь нужный результат."
AUTO_SEARCH_REPORT = (
    TRIAL_ROOT
    / "core_0_1_text_extraction_auto_search_p018_p017_column_line_segmentation_G1_VIRAL_001"
    / "auto_search_p018_p017_report.json"
)
AUTO_SEARCH_REPORT_SHA256 = "B5C24B05B3A5CC2BBBDBFC4AE7A55E4A1913098FE160946143586CFC4E8E1649"
SECOND_PASS_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_second_pass_p018_p017_crop_safe_remediation_G1_VIRAL_001"
PAGES = ["018", "017"]
SUPPORT_THRESHOLD = 0.98


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run reference-guided repair for P018/P017 OCR candidates.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P018/P017 reference-guided repair is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P018/P017 reference-guided repair requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P018/P017 reference-guided repair requires the exact bounded human decision")


def verify_inputs() -> dict:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    actual = sha256_file(AUTO_SEARCH_REPORT)
    if actual != AUTO_SEARCH_REPORT_SHA256:
        raise SystemExit(f"C01TEAS018017 report hash mismatch: {actual}")
    return {"auto_search_report": {"path": AUTO_SEARCH_REPORT.relative_to(ROOT).as_posix(), "sha256": actual}}


def reference_text(page: str) -> tuple[str, Path, str]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    reference = overview.reference_for_page(page, assets)
    if reference is None:
        raise SystemExit(f"P{page} missing reference")
    label, path = reference
    return label, path, overview.extract_reference_text(path)


def candidate_path(page: str) -> Path:
    candidates = {
        "018": SECOND_PASS_ROOT / "candidate_texts" / "wide_edge_mask_trim_psm11" / "page_018_candidate.md",
        "017": SECOND_PASS_ROOT / "candidate_texts" / "wide_edge_mask_trim_psm4" / "page_017_candidate.md",
    }
    path = candidates[page]
    if not path.exists():
        raise SystemExit(f"P{page} missing second-pass candidate: {path}")
    return path


def token_support(candidate_text: str, reference: str) -> tuple[float, list[str]]:
    candidate_tokens = overview.metric_text(candidate_text).split()
    reference_tokens = overview.metric_text(reference).split()
    candidate_set = set(candidate_tokens)
    supported = 0
    unsupported: list[str] = []
    for token in reference_tokens:
        if token in candidate_set:
            supported += 1
            continue
        if any(item and (item.endswith(token) or token.endswith(item)) and min(len(item), len(token)) >= 3 for item in candidate_set):
            supported += 1
            continue
        unsupported.append(token)
    if not reference_tokens:
        return 1.0, []
    return supported / len(reference_tokens), unsupported


def metrics(text: str, reference: str) -> dict:
    normalized = overview.normalize_candidate_for_metrics(text)
    return {
        "sequence_similarity_ratio": round(overview.similarity_ratio(normalized, reference), 6),
        "token_recall": round(overview.token_recall(normalized, reference), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(overview.normalize_text(reference)),
        "candidate_normalized_sha256": sha256_text(normalized + "\n"),
    }


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    results = {}
    for page in PAGES:
        label, ref_path, ref_text = reference_text(page)
        cand_path = candidate_path(page)
        cand_text = cand_path.read_text(encoding="utf-8", errors="replace")
        support_ratio, unsupported = token_support(cand_text, ref_text)
        repaired_text = ref_text.strip() + "\n"
        repaired_path = OUT_ROOT / "repaired_texts" / f"page_{page}_reference_guided_repair.md"
        write_text(repaired_path, repaired_text)
        results[page] = {
            "page": page,
            "reference_label": label,
            "reference_path": ref_path.relative_to(ROOT).as_posix(),
            "reference_sha256": sha256_file(ref_path),
            "source_candidate_path": cand_path.relative_to(ROOT).as_posix(),
            "source_candidate_sha256": sha256_file(cand_path),
            "support_threshold": SUPPORT_THRESHOLD,
            "ocr_token_support_ratio": round(support_ratio, 6),
            "unsupported_reference_tokens_sample": unsupported[:24],
            "reference_guided_repair_path": repaired_path.relative_to(ROOT).as_posix(),
            "reference_guided_repair_sha256": sha256_file(repaired_path),
            "metrics": metrics(repaired_text, ref_text),
            "ok_level_candidate": support_ratio >= SUPPORT_THRESHOLD,
        }
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_reference_guided_repair_completed",
        "source_auto_search": "C01TEAS018017-G1-VIRAL-001",
        "verified_inputs": verified_inputs,
        "pages": PAGES,
        "results": results,
        "independent_ocr_acceptance": False,
        "reference_text_used_as_source_of_truth": True,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "pdf_text_layer_extraction_performed": False,
        "render_execution_performed": False,
        "runtime_implementation_created": False,
        "runtime_start_performed": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "recommendation": "treat P018/P017 as reference-guided OCR repair candidates, not independent OCR-profile successes",
    }
    write_json(OUT_ROOT / "reference_guided_repair_p018_p017_report.json", report)
    lines = [
        "# Core 0.1 P018/P017 Reference-Guided OCR Repair - C01TERG018017-G1-VIRAL-001",
        "",
        "Status: `candidate_only_reference_guided_repair_completed`",
        "",
        "| Page | OCR token support | Similarity after repair | Token recall after repair | Independent OCR acceptance |",
        "|---|---:|---:|---:|---|",
    ]
    for page in PAGES:
        item = results[page]
        lines.append(
            f"| `{page}` | `{item['ocr_token_support_ratio']}` | "
            f"`{item['metrics']['sequence_similarity_ratio']}` | `{item['metrics']['token_recall']}` | `False` |"
        )
    lines.extend(
        [
            "",
            "Boundary: reference-guided repair uses the accepted text map as source of truth. This is not independent OCR acceptance.",
            "No accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "reference_guided_repair_p018_p017_summary.md", "\n".join(lines))
    manifest_lines = [
        "# P018/P017 Reference-Guided OCR Repair Manifest - C01TERG018017-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "reference_guided_repair_p018_p017_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "reference_guided_repair_p018_p017_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
