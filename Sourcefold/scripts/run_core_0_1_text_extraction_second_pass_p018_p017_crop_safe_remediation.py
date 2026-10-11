from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageOps

import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_second_pass_p018_p017_crop_safe_remediation_G1_VIRAL_001"
LEDGER = overview.LEDGER
TESSERACT = overview.TESSERACT

LANE_ID = "C01TEP2P018P017-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SECOND-PASS-P018-P017-CROP-SAFE-001"
HUMAN_DECISION = "ок , собери план , сделай коммит и пробуй дальше"
C01TEWDR_REPORT = (
    TRIAL_ROOT
    / "core_0_1_text_extraction_weak_page_diagnostics_p018_remediation_G1_VIRAL_001"
    / "weak_diagnostics_p018_remediation_report.json"
)
C01TEWDR_REPORT_SHA256 = "9D1A424946064EB19F20D31E51797A38BFC01C10B45606B6EE67CA72C2EE06C9"
PAGES = ["018", "017"]


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
    parser = argparse.ArgumentParser(description="Run crop-safe second-pass remediation for P018/P017.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P018/P017 second pass is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P018/P017 second pass requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P018/P017 second pass requires the exact bounded human decision")


def verify_inputs() -> dict:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    actual = sha256_file(C01TEWDR_REPORT)
    if actual != C01TEWDR_REPORT_SHA256:
        raise SystemExit(f"C01TEWDR report hash mismatch: {actual}")
    return {"C01TEWDR_report": {"path": C01TEWDR_REPORT.relative_to(ROOT).as_posix(), "sha256": actual}}


def crop_paths_for_page(page: str) -> list[Path]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    paths = overview.crop_paths_for_page(page, assets)
    missing = [path for path in paths if not path.exists()]
    if missing:
        raise SystemExit(f"P{page} missing expected input: {missing[0]}")
    return paths


def reference_for_page(page: str) -> tuple[str, Path, str]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    reference = overview.reference_for_page(page, assets)
    if reference is None:
        raise SystemExit(f"P{page} missing reference")
    label, path = reference
    return label, path, overview.extract_reference_text(path)


def add_border(image: Image.Image, border: int) -> Image.Image:
    canvas = Image.new("RGB", (image.width + border * 2, image.height + border * 2), "white")
    canvas.paste(image, (border, border))
    return canvas


def transform_image(source: Image.Image, variant: str) -> Image.Image:
    image = source.convert("RGB")
    if variant == "wide_edge_mask_trim":
        trimmed = image.crop((4, 4, image.width - 4, image.height - 4))
        return ImageOps.autocontrast(ImageOps.grayscale(add_border(trimmed, 16))).convert("RGB")
    if variant == "no_trim_pad32":
        return ImageOps.autocontrast(ImageOps.grayscale(add_border(image, 32))).convert("RGB")
    if variant == "no_trim_pad64":
        return ImageOps.autocontrast(ImageOps.grayscale(add_border(image, 64))).convert("RGB")
    if variant == "no_trim_pad96":
        return ImageOps.autocontrast(ImageOps.grayscale(add_border(image, 96))).convert("RGB")
    if variant == "no_trim_threshold_pad64":
        gray = ImageOps.autocontrast(ImageOps.grayscale(add_border(image, 64)))
        return gray.point(lambda px: 255 if px >= 180 else 0).convert("RGB")
    if variant == "left_pad96_no_trim":
        canvas = Image.new("RGB", (image.width + 112, image.height + 32), "white")
        canvas.paste(image, (96, 16))
        return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")
    raise ValueError(f"unknown variant: {variant}")


def run_tesseract(input_path: Path, candidate_id: str, page: str, psm: int, variant: str) -> tuple[str, dict]:
    id_ = overview.input_id(input_path)
    prepared = OUT_ROOT / "prepared_inputs" / candidate_id / f"p{page}" / f"{id_}.png"
    base = OUT_ROOT / "raw_ocr" / candidate_id / f"p{page}" / id_
    prepared.parent.mkdir(parents=True, exist_ok=True)
    base.parent.mkdir(parents=True, exist_ok=True)
    transform_image(Image.open(input_path), variant).save(prepared)
    command = [
        str(TESSERACT),
        str(prepared),
        str(base),
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
    text_path = base.with_suffix(".txt")
    tsv_path = base.with_suffix(".tsv")
    stderr_path = base.with_suffix(".stderr.txt")
    stdout_path = base.with_suffix(".stdout.txt")
    write_text(stderr_path, completed.stderr)
    write_text(stdout_path, completed.stdout)
    text = text_path.read_text(encoding="utf-8", errors="replace")
    return text, {
        "input_id": id_,
        "source_input_path": input_path.relative_to(ROOT).as_posix(),
        "source_input_sha256": sha256_file(input_path),
        "prepared_input_path": prepared.relative_to(ROOT).as_posix(),
        "prepared_input_sha256": sha256_file(prepared),
        "raw_ocr_text_path": text_path.relative_to(ROOT).as_posix(),
        "raw_ocr_text_sha256": sha256_file(text_path),
        "raw_ocr_tsv_path": tsv_path.relative_to(ROOT).as_posix(),
        "raw_ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_path": stderr_path.relative_to(ROOT).as_posix(),
        "stdout_path": stdout_path.relative_to(ROOT).as_posix(),
    }


def metrics(candidate_text: str, reference_text: str) -> dict:
    normalized = overview.normalize_candidate_for_metrics(candidate_text)
    return {
        "sequence_similarity_ratio": round(overview.similarity_ratio(normalized, reference_text), 6),
        "token_recall": round(overview.token_recall(normalized, reference_text), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(overview.normalize_text(reference_text)),
        "candidate_normalized_sha256": sha256_text(normalized + "\n"),
    }


def candidate_for_page(page: str, candidate_id: str, variant: str, psm: int) -> tuple[str, list[dict]]:
    chunks = []
    inputs = []
    for path in crop_paths_for_page(page):
        text, item = run_tesseract(path, candidate_id, page, psm, variant)
        chunks.append(f"## {overview.input_id(path)}\n\n{text.strip()}")
        inputs.append(item)
    return "\n\n".join(chunks).strip() + "\n", inputs


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    variants = ["wide_edge_mask_trim", "no_trim_pad32", "no_trim_pad64", "no_trim_pad96", "no_trim_threshold_pad64", "left_pad96_no_trim"]
    psms = [4, 6, 11]
    page_results = {page: [] for page in PAGES}
    for variant in variants:
        for psm in psms:
            candidate_id = f"{variant}_psm{psm}"
            for page in PAGES:
                label, reference_path, reference_text = reference_for_page(page)
                candidate_text, inputs = candidate_for_page(page, candidate_id, variant, psm)
                page_metrics = metrics(candidate_text, reference_text)
                candidate_path = OUT_ROOT / "candidate_texts" / candidate_id / f"page_{page}_candidate.md"
                write_text(candidate_path, candidate_text)
                page_results[page].append(
                    {
                        "page": page,
                        "candidate_id": candidate_id,
                        "preprocessing_variant": variant,
                        "psm": psm,
                        "reference_label": label,
                        "reference_path": reference_path.relative_to(ROOT).as_posix(),
                        "reference_sha256": sha256_file(reference_path),
                        "input_count": len(inputs),
                        "input_results": inputs,
                        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                        "candidate_text_sha256": sha256_file(candidate_path),
                        "metrics": page_metrics,
                    }
                )
    best_by_page = {}
    for page, results in page_results.items():
        results.sort(
            key=lambda item: (
                item["metrics"]["sequence_similarity_ratio"],
                item["metrics"]["token_recall"],
            ),
            reverse=True,
        )
        best_by_page[page] = results[0]
        write_json(OUT_ROOT / "rankings" / f"page_{page}_candidate_rankings.json", results)
    shared_candidates = []
    for variant in variants:
        for psm in psms:
            candidate_id = f"{variant}_psm{psm}"
            p018 = next(item for item in page_results["018"] if item["candidate_id"] == candidate_id)
            p017 = next(item for item in page_results["017"] if item["candidate_id"] == candidate_id)
            shared_candidates.append(
                {
                    "candidate_id": candidate_id,
                    "preprocessing_variant": variant,
                    "psm": psm,
                    "min_similarity": min(
                        p018["metrics"]["sequence_similarity_ratio"],
                        p017["metrics"]["sequence_similarity_ratio"],
                    ),
                    "min_token_recall": min(p018["metrics"]["token_recall"], p017["metrics"]["token_recall"]),
                    "p018_similarity": p018["metrics"]["sequence_similarity_ratio"],
                    "p017_similarity": p017["metrics"]["sequence_similarity_ratio"],
                }
            )
    shared_candidates.sort(key=lambda item: (item["min_similarity"], item["min_token_recall"]), reverse=True)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_second_pass_p018_p017_completed",
        "source_diagnostics": "C01TEWDR-G1-VIRAL-001",
        "verified_inputs": verified_inputs,
        "pages": PAGES,
        "candidate_count_per_page": len(variants) * len(psms),
        "best_by_page": best_by_page,
        "shared_candidate_rankings": shared_candidates,
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
        "recommendation": "review whether shared crop-safe candidate is sufficient for P018/P017 or requires page-specific handling",
    }
    write_json(OUT_ROOT / "second_pass_p018_p017_report.json", report)
    lines = [
        "# Core 0.1 P018/P017 Crop-Safe Remediation Second Pass - C01TEP2P018P017-G1-VIRAL-001",
        "",
        "Status: `candidate_only_second_pass_p018_p017_completed`",
        "",
        "| Page | Best candidate | Similarity | Token recall |",
        "|---|---|---:|---:|",
    ]
    for page in PAGES:
        best = best_by_page[page]
        lines.append(
            f"| `{page}` | `{best['candidate_id']}` | "
            f"`{best['metrics']['sequence_similarity_ratio']}` | `{best['metrics']['token_recall']}` |"
        )
    shared = shared_candidates[0]
    lines.extend(
        [
            "",
            "## Best Shared Candidate",
            "",
            f"Candidate: `{shared['candidate_id']}`",
            f"Minimum similarity across P018/P017: `{shared['min_similarity']}`",
            f"Minimum token recall across P018/P017: `{shared['min_token_recall']}`",
            "",
            "Boundary: candidate-only second pass; no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "second_pass_p018_p017_summary.md", "\n".join(lines))
    manifest_lines = [
        "# P018/P017 Crop-Safe Remediation Second Pass Manifest - C01TEP2P018P017-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "second_pass_p018_p017_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "second_pass_p018_p017_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
