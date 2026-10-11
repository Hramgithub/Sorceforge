from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_weak_page_diagnostics_p018_remediation_G1_VIRAL_001"
LEDGER = overview.LEDGER
TESSERACT = overview.TESSERACT

LANE_ID = "C01TEWDR-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-WEAK-DIAGNOSTICS-P018-REMEDIATION-001"
HUMAN_DECISION = "ок иди по плану 1-7"
OVERVIEW_REPORT = (
    TRIAL_ROOT
    / "core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001"
    / "overview_replay_report.json"
)
OVERVIEW_REPORT_SHA256 = "7FE37ECD8BAB5EAC4C9557C244D0E2CA618704783E6CFC9D706CFB60B46E0357"

WEAK_PAGES = ["012", "013", "014", "016", "017", "018", "019", "020"]
MINI_REPLAY_PAGES = ["017", "019", "014"]
P018_PAGE = "018"


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
    parser = argparse.ArgumentParser(description="Run weak-page diagnostics and P018 remediation probe.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("weak diagnostics/remediation is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"weak diagnostics/remediation requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("weak diagnostics/remediation requires the exact bounded human decision")


def verify_inputs() -> dict:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    actual = sha256_file(OVERVIEW_REPORT)
    if actual != OVERVIEW_REPORT_SHA256:
        raise SystemExit(f"overview report hash mismatch: {actual}")
    return {
        "overview_report": {
            "path": OVERVIEW_REPORT.relative_to(ROOT).as_posix(),
            "sha256": actual,
        }
    }


def reference_for_page(page: str) -> tuple[str, Path, str]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    reference = overview.reference_for_page(page, assets)
    if reference is None:
        raise SystemExit(f"P{page} has no reference")
    label, path = reference
    return label, path, overview.extract_reference_text(path)


def crop_paths_for_page(page: str) -> list[Path]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    paths = overview.crop_paths_for_page(page, assets)
    missing = [path for path in paths if not path.exists()]
    if missing:
        raise SystemExit(f"P{page} missing expected input: {missing[0]}")
    return paths


def transform_image(source: Image.Image, variant: str) -> Image.Image:
    image = source.convert("RGB")
    if variant == "edge_mask_trim":
        return overview.transform_trim_mask(image)
    if variant == "grayscale_autocontrast":
        return ImageOps.autocontrast(ImageOps.grayscale(image)).convert("RGB")
    if variant == "threshold_180":
        gray = ImageOps.autocontrast(ImageOps.grayscale(image))
        return gray.point(lambda px: 255 if px >= 180 else 0).convert("RGB")
    if variant == "wide_edge_mask_trim":
        trimmed = image.crop((4, 4, image.width - 4, image.height - 4))
        canvas = Image.new("RGB", (trimmed.width + 16, trimmed.height + 16), "white")
        canvas.paste(trimmed, (8, 8))
        return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")
    raise ValueError(f"unknown transform variant: {variant}")


def run_tesseract(
    input_path: Path,
    output_base: Path,
    prepared_path: Path,
    preprocess_variant: str,
    psm: int,
    persist: bool,
) -> tuple[str, dict]:
    prepared_path.parent.mkdir(parents=True, exist_ok=True)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    transform_image(Image.open(input_path), preprocess_variant).save(prepared_path)
    command = [
        str(TESSERACT),
        str(prepared_path),
        str(output_base),
        "-l",
        "eng",
        "--oem",
        "1",
        "--psm",
        str(psm),
        "txt",
        "tsv",
    ]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    text_path = output_base.with_suffix(".txt")
    tsv_path = output_base.with_suffix(".tsv")
    text = text_path.read_text(encoding="utf-8", errors="replace")
    stderr_path = output_base.with_suffix(".stderr.txt")
    stdout_path = output_base.with_suffix(".stdout.txt")
    if persist:
        write_text(stderr_path, completed.stderr)
        write_text(stdout_path, completed.stdout)
    return text, {
        "input_id": output_base.name,
        "source_input_path": input_path.relative_to(ROOT).as_posix(),
        "source_input_sha256": sha256_file(input_path),
        "prepared_input_path": prepared_path.relative_to(ROOT).as_posix() if persist else None,
        "prepared_input_sha256": sha256_file(prepared_path),
        "raw_ocr_text_path": text_path.relative_to(ROOT).as_posix() if persist else None,
        "raw_ocr_text_sha256": sha256_file(text_path),
        "raw_ocr_tsv_path": tsv_path.relative_to(ROOT).as_posix() if persist else None,
        "raw_ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_path": stderr_path.relative_to(ROOT).as_posix() if persist else None,
        "stdout_path": stdout_path.relative_to(ROOT).as_posix() if persist else None,
        "preprocessing_variant": preprocess_variant,
        "psm": psm,
    }


def candidate_from_paths(
    page: str,
    paths: list[Path],
    preprocess_variant: str,
    psm: int,
    root: Path,
    persist: bool,
) -> tuple[str, list[dict]]:
    chunks = []
    input_results = []
    for path in paths:
        id_ = overview.input_id(path)
        base = root / "raw_ocr" / f"p{page}" / id_
        prepared = root / "prepared_inputs" / f"p{page}" / f"{id_}.png"
        text, item = run_tesseract(path, base, prepared, preprocess_variant, psm, persist)
        chunks.append(f"## {id_}\n\n{text.strip()}")
        input_results.append(item)
    return "\n\n".join(chunks).strip() + "\n", input_results


def metrics(candidate_text: str, reference_text: str) -> dict:
    normalized = overview.normalize_candidate_for_metrics(candidate_text)
    return {
        "sequence_similarity_ratio": round(overview.similarity_ratio(normalized, reference_text), 6),
        "token_recall": round(overview.token_recall(normalized, reference_text), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(overview.normalize_text(reference_text)),
        "candidate_normalized_sha256": sha256_text(normalized + "\n"),
    }


def classify(page_metrics: dict, reference_label: str) -> list[str]:
    flags = []
    if page_metrics["sequence_similarity_ratio"] < 0.997:
        flags.append("sequence_order_or_layout_issue")
    if page_metrics["token_recall"] < 0.993:
        flags.append("token_recall_issue")
    if page_metrics["token_recall"] >= 0.97 and page_metrics["sequence_similarity_ratio"] < 0.7:
        flags.append("high_recall_low_sequence_alignment")
    if reference_label != "reference_ocr_verified_text_map":
        flags.append("reference_not_ocr_verified")
    return flags


def diagnose_page(page: str) -> dict:
    reference_label, reference_path, reference_text = reference_for_page(page)
    paths = crop_paths_for_page(page)
    candidate_text, inputs = candidate_from_paths(page, paths, "edge_mask_trim", 4, OUT_ROOT, True)
    page_metrics = metrics(candidate_text, reference_text)
    candidate_path = OUT_ROOT / "candidate_texts" / f"page_{page}_candidate.md"
    normalized_candidate = overview.normalize_candidate_for_metrics(candidate_text)
    normalized_reference = overview.normalize_text(reference_text)
    write_text(candidate_path, candidate_text)
    write_text(OUT_ROOT / "normalized" / f"page_{page}_candidate.normalized.txt", normalized_candidate + "\n")
    write_text(OUT_ROOT / "normalized" / f"page_{page}_reference.normalized.txt", normalized_reference + "\n")
    hint = {
        "page": page,
        "diagnostic_flags": classify(page_metrics, reference_label),
        "candidate_prefix": normalized_candidate[:500],
        "reference_prefix": normalized_reference[:500],
    }
    write_json(OUT_ROOT / "diff_hints" / f"page_{page}_diff_hints.json", hint)
    return {
        "page": page,
        "status": "diagnostic_completed",
        "reference_label": reference_label,
        "reference_path": reference_path.relative_to(ROOT).as_posix(),
        "reference_sha256": sha256_file(reference_path),
        "input_count": len(paths),
        "input_results": inputs,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_path),
        "metrics": page_metrics,
        "diagnostic_flags": hint["diagnostic_flags"],
    }


def p018_matrix() -> dict:
    reference_label, reference_path, reference_text = reference_for_page(P018_PAGE)
    paths = crop_paths_for_page(P018_PAGE)
    variants = [
        ("edge_mask_trim", 4),
        ("edge_mask_trim", 6),
        ("edge_mask_trim", 11),
        ("grayscale_autocontrast", 4),
        ("grayscale_autocontrast", 6),
        ("threshold_180", 4),
        ("wide_edge_mask_trim", 4),
    ]
    orders = [("normal", paths), ("reverse", list(reversed(paths)))]
    results = []
    with tempfile.TemporaryDirectory(prefix="sourcefold_p018_remediation_matrix_") as scratch:
        scratch_root = Path(scratch)
        for preprocess_variant, psm in variants:
            for order_id, ordered_paths in orders:
                candidate_text, input_results = candidate_from_paths(
                    P018_PAGE,
                    ordered_paths,
                    preprocess_variant,
                    psm,
                    scratch_root / f"{preprocess_variant}_psm{psm}_{order_id}",
                    False,
                )
                page_metrics = metrics(candidate_text, reference_text)
                result = {
                    "candidate_id": f"{preprocess_variant}_psm{psm}_{order_id}",
                    "preprocessing_variant": preprocess_variant,
                    "psm": psm,
                    "assembly_order": order_id,
                    "input_order": [path.name for path in ordered_paths],
                    "metrics": page_metrics,
                    "candidate_text_sha256": sha256_text(candidate_text),
                    "input_results": input_results,
                }
                results.append(result)
    results.sort(
        key=lambda item: (
            item["metrics"]["sequence_similarity_ratio"],
            item["metrics"]["token_recall"],
        ),
        reverse=True,
    )
    best = results[0]
    write_json(OUT_ROOT / "p018_remediation_matrix" / "p018_candidate_rankings.json", results)
    write_text(
        OUT_ROOT / "p018_remediation_matrix" / "p018_remediation_summary.md",
        "\n".join(
            [
                "# P018 Remediation Probe",
                "",
                f"Best candidate: `{best['candidate_id']}`",
                f"Similarity: `{best['metrics']['sequence_similarity_ratio']}`",
                f"Token recall: `{best['metrics']['token_recall']}`",
                "",
            ]
        ),
    )
    return {
        "page": P018_PAGE,
        "reference_label": reference_label,
        "reference_path": reference_path.relative_to(ROOT).as_posix(),
        "candidate_count": len(results),
        "best_candidate": best,
        "rankings_path": (OUT_ROOT / "p018_remediation_matrix" / "p018_candidate_rankings.json").relative_to(ROOT).as_posix(),
    }


def mini_replay(best_candidate: dict) -> dict:
    preprocess_variant = best_candidate["preprocessing_variant"]
    psm = best_candidate["psm"]
    page_results = []
    for page in MINI_REPLAY_PAGES:
        reference_label, reference_path, reference_text = reference_for_page(page)
        paths = crop_paths_for_page(page)
        candidate_text, input_results = candidate_from_paths(
            page,
            paths,
            preprocess_variant,
            psm,
            OUT_ROOT / "mini_replay_scratch",
            True,
        )
        page_metrics = metrics(candidate_text, reference_text)
        candidate_path = OUT_ROOT / "mini_replay_candidate_texts" / f"page_{page}_{preprocess_variant}_psm{psm}.md"
        write_text(candidate_path, candidate_text)
        page_results.append(
            {
                "page": page,
                "reference_label": reference_label,
                "reference_path": reference_path.relative_to(ROOT).as_posix(),
                "reference_sha256": sha256_file(reference_path),
                "input_count": len(paths),
                "input_results": input_results,
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": sha256_file(candidate_path),
                "metrics": page_metrics,
                "diagnostic_flags": classify(page_metrics, reference_label),
            }
        )
    return {
        "source_best_p018_candidate": best_candidate["candidate_id"],
        "preprocessing_variant": preprocess_variant,
        "psm": psm,
        "pages": page_results,
    }


def output_hashes() -> dict[str, dict[str, str]]:
    return {
        path.relative_to(OUT_ROOT).as_posix(): {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(path),
        }
        for path in sorted(OUT_ROOT.rglob("*"))
        if path.is_file()
    }


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    diagnostics = [diagnose_page(page) for page in WEAK_PAGES]
    remediation = p018_matrix()
    replay = mini_replay(remediation["best_candidate"])
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_weak_diagnostics_p018_remediation_completed",
        "source_overview": "C01TEOR020-G1-VIRAL-001",
        "verified_inputs": verified_inputs,
        "diagnostic_pages": WEAK_PAGES,
        "p018_remediation_performed": True,
        "mini_replay_pages": MINI_REPLAY_PAGES,
        "diagnostics": diagnostics,
        "p018_remediation": remediation,
        "mini_replay": replay,
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
        "recommendation": "review P018 best candidate and decide whether to authorize broader weak-page remediation",
    }
    write_json(OUT_ROOT / "weak_diagnostics_p018_remediation_report.json", report)
    lines = [
        "# Core 0.1 Weak Page Diagnostics + P018 Remediation - C01TEWDR-G1-VIRAL-001",
        "",
        "Status: `candidate_only_weak_diagnostics_p018_remediation_completed`",
        "",
        "## Diagnostics",
        "",
        "| Page | Similarity | Token recall | Flags |",
        "|---|---:|---:|---|",
    ]
    for item in diagnostics:
        lines.append(
            f"| `{item['page']}` | `{item['metrics']['sequence_similarity_ratio']}` | "
            f"`{item['metrics']['token_recall']}` | `{', '.join(item['diagnostic_flags']) or 'none'}` |"
        )
    best = remediation["best_candidate"]
    lines.extend(
        [
            "",
            "## P018 Remediation Probe",
            "",
            f"Best candidate: `{best['candidate_id']}`",
            f"P018 similarity: `{best['metrics']['sequence_similarity_ratio']}`",
            f"P018 token recall: `{best['metrics']['token_recall']}`",
            "",
            "## Mini Replay",
            "",
            "| Page | Similarity | Token recall | Flags |",
            "|---|---:|---:|---|",
        ]
    )
    for item in replay["pages"]:
        lines.append(
            f"| `{item['page']}` | `{item['metrics']['sequence_similarity_ratio']}` | "
            f"`{item['metrics']['token_recall']}` | `{', '.join(item['diagnostic_flags']) or 'none'}` |"
        )
    lines.extend(
        [
            "",
            "Boundary: diagnostic/remediation evidence only; no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "weak_diagnostics_p018_remediation_summary.md", "\n".join(lines))
    manifest_lines = [
        "# Weak Diagnostics + P018 Remediation Manifest - C01TEWDR-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "weak_diagnostics_p018_remediation_manifest.md":
            manifest_lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "weak_diagnostics_p018_remediation_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
