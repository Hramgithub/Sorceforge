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
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_auto_search_p018_p017_column_line_segmentation_G1_VIRAL_001"
LEDGER = overview.LEDGER
TESSERACT = overview.TESSERACT

LANE_ID = "C01TEAS018017-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-AUTO-SEARCH-P018-P017-COLUMN-LINE-001"
HUMAN_DECISION = "понял, тогда может в цикле делать драй ран пока не получится реально нормальный результат? без остановок на меня?"
SECOND_PASS_REPORT = (
    TRIAL_ROOT
    / "core_0_1_text_extraction_second_pass_p018_p017_crop_safe_remediation_G1_VIRAL_001"
    / "second_pass_p018_p017_report.json"
)
SECOND_PASS_REPORT_SHA256 = "A648F1585463124EC17BDFB99BDA47B7E3B94C305D9F100990B88B25D93E6D09"
PAGES = ["018", "017"]
OK_SIMILARITY = 0.997
OK_TOKEN_RECALL = 0.993


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
    parser = argparse.ArgumentParser(description="Run bounded auto-search for P018/P017 OCR column/line segmentation.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P018/P017 auto-search is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P018/P017 auto-search requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P018/P017 auto-search requires the exact bounded human decision")


def verify_inputs() -> dict:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    actual = sha256_file(SECOND_PASS_REPORT)
    if actual != SECOND_PASS_REPORT_SHA256:
        raise SystemExit(f"C01TEP2P018P017 report hash mismatch: {actual}")
    return {"second_pass_report": {"path": SECOND_PASS_REPORT.relative_to(ROOT).as_posix(), "sha256": actual}}


def crop_paths_for_page(page: str) -> list[Path]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    paths = overview.crop_paths_for_page(page, assets)
    if len(paths) != 2:
        raise SystemExit(f"P{page} expected exactly 2 text-evidence crops")
    for path in paths:
        if not path.exists():
            raise SystemExit(f"P{page} missing expected input: {path}")
    return paths


def reference_for_page(page: str) -> tuple[str, Path, str]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    reference = overview.reference_for_page(page, assets)
    if reference is None:
        raise SystemExit(f"P{page} missing reference")
    label, path = reference
    return label, path, overview.extract_reference_text(path)


def metrics(candidate_text: str, reference_text: str) -> dict:
    normalized = overview.normalize_candidate_for_metrics(candidate_text)
    return {
        "sequence_similarity_ratio": round(overview.similarity_ratio(normalized, reference_text), 6),
        "token_recall": round(overview.token_recall(normalized, reference_text), 6),
        "normalized_candidate_chars": len(normalized),
        "reference_chars": len(overview.normalize_text(reference_text)),
        "candidate_normalized_sha256": sha256_text(normalized + "\n"),
    }


def text_bbox(image: Image.Image, threshold: int = 244) -> tuple[int, int, int, int]:
    gray = ImageOps.grayscale(image)
    px = gray.load()
    xs: list[int] = []
    ys: list[int] = []
    for y in range(gray.height):
        for x in range(gray.width):
            if px[x, y] < threshold:
                xs.append(x)
                ys.append(y)
    if not xs:
        return (0, 0, image.width, image.height)
    return (min(xs), min(ys), max(xs) + 1, max(ys) + 1)


def crop_with_padding(image: Image.Image, bbox: tuple[int, int, int, int], pad: int) -> Image.Image:
    x1, y1, x2, y2 = bbox
    x1 = max(0, x1 - pad)
    y1 = max(0, y1 - pad)
    x2 = min(image.width, x2 + pad)
    y2 = min(image.height, y2 + pad)
    cropped = image.crop((x1, y1, x2, y2)).convert("RGB")
    canvas = Image.new("RGB", (cropped.width + pad * 2, cropped.height + pad * 2), "white")
    canvas.paste(cropped, (pad, pad))
    return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")


def line_bands(image: Image.Image, threshold: int, gap: int, min_height: int) -> list[tuple[int, int]]:
    gray = ImageOps.grayscale(image)
    rows = []
    for y in range(gray.height):
        dark = 0
        for x in range(gray.width):
            if gray.getpixel((x, y)) < threshold:
                dark += 1
        if dark >= 4:
            rows.append(y)
    if not rows:
        return [(0, image.height)]
    bands: list[tuple[int, int]] = []
    start = prev = rows[0]
    for y in rows[1:]:
        if y - prev > gap:
            if prev - start + 1 >= min_height:
                bands.append((start, prev + 1))
            start = y
        prev = y
    if prev - start + 1 >= min_height:
        bands.append((start, prev + 1))
    return bands


def prepared_regions(source: Path, candidate_id: str, variant: dict, page: str) -> list[Path]:
    source_image = Image.open(source).convert("RGB")
    input_id = overview.input_id(source)
    out_dir = OUT_ROOT / "prepared_inputs" / candidate_id / f"p{page}" / input_id
    out_dir.mkdir(parents=True, exist_ok=True)
    regions: list[Path] = []
    if variant["kind"] == "bbox":
        region = crop_with_padding(source_image, text_bbox(source_image, variant["threshold"]), variant["pad"])
        path = out_dir / "region_001.png"
        region.save(path)
        return [path]
    if variant["kind"] == "line_bands":
        bbox = text_bbox(source_image, variant["threshold"])
        base = crop_with_padding(source_image, bbox, variant["outer_pad"])
        bands = line_bands(base, variant["threshold"], variant["gap"], variant["min_height"])
        for index, (y1, y2) in enumerate(bands, start=1):
            pad = variant["line_pad"]
            band = base.crop((0, max(0, y1 - pad), base.width, min(base.height, y2 + pad))).convert("RGB")
            canvas = Image.new("RGB", (band.width + pad * 2, band.height + pad * 2), "white")
            canvas.paste(band, (pad, pad))
            path = out_dir / f"line_{index:03d}.png"
            ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB").save(path)
            regions.append(path)
        return regions
    raise ValueError(f"unknown candidate kind: {variant['kind']}")


def run_tesseract(region: Path, base: Path, psm: int) -> tuple[str, dict]:
    command = [
        str(TESSERACT),
        str(region),
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
        "region_path": region.relative_to(ROOT).as_posix(),
        "region_sha256": sha256_file(region),
        "raw_ocr_text_path": text_path.relative_to(ROOT).as_posix(),
        "raw_ocr_text_sha256": sha256_file(text_path),
        "raw_ocr_tsv_path": tsv_path.relative_to(ROOT).as_posix(),
        "raw_ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_path": stderr_path.relative_to(ROOT).as_posix(),
        "stdout_path": stdout_path.relative_to(ROOT).as_posix(),
    }


def candidate_variants() -> list[dict]:
    return [
        {"id": "bbox_pad24_psm6", "kind": "bbox", "threshold": 244, "pad": 24, "psm": 6},
        {"id": "bbox_pad48_psm6", "kind": "bbox", "threshold": 244, "pad": 48, "psm": 6},
        {"id": "bbox_pad64_psm11", "kind": "bbox", "threshold": 244, "pad": 64, "psm": 11},
        {"id": "line_bands_pad16_gap6_psm7", "kind": "line_bands", "threshold": 244, "outer_pad": 24, "line_pad": 16, "gap": 6, "min_height": 8, "psm": 7},
        {"id": "line_bands_pad24_gap8_psm7", "kind": "line_bands", "threshold": 244, "outer_pad": 32, "line_pad": 24, "gap": 8, "min_height": 8, "psm": 7},
        {"id": "line_bands_pad32_gap10_psm7", "kind": "line_bands", "threshold": 244, "outer_pad": 48, "line_pad": 32, "gap": 10, "min_height": 8, "psm": 7},
        {"id": "line_bands_pad24_gap8_psm13", "kind": "line_bands", "threshold": 244, "outer_pad": 32, "line_pad": 24, "gap": 8, "min_height": 8, "psm": 13},
    ]


def build_candidate(page: str, variant: dict) -> tuple[str, list[dict]]:
    chunks = []
    inputs = []
    candidate_id = variant["id"]
    for crop_path in crop_paths_for_page(page):
        crop_id = overview.input_id(crop_path)
        region_paths = prepared_regions(crop_path, candidate_id, variant, page)
        region_chunks = []
        region_items = []
        for index, region in enumerate(region_paths, start=1):
            base = OUT_ROOT / "raw_ocr" / candidate_id / f"p{page}" / crop_id / f"region_{index:03d}"
            base.parent.mkdir(parents=True, exist_ok=True)
            text, item = run_tesseract(region, base, variant["psm"])
            region_chunks.append(text.strip())
            region_items.append(item)
        chunks.append(f"## {crop_id}\n\n" + "\n".join(part for part in region_chunks if part).strip())
        inputs.append(
            {
                "input_id": crop_id,
                "source_input_path": crop_path.relative_to(ROOT).as_posix(),
                "source_input_sha256": sha256_file(crop_path),
                "region_count": len(region_items),
                "regions": region_items,
            }
        )
    return "\n\n".join(chunks).strip() + "\n", inputs


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    variants = candidate_variants()
    page_results = {page: [] for page in PAGES}
    stop_reached = False
    stop_reason = "budget_exhausted_without_ok_level_candidate"
    for variant in variants:
        for page in PAGES:
            label, reference_path, reference_text = reference_for_page(page)
            candidate_text, inputs = build_candidate(page, variant)
            candidate_path = OUT_ROOT / "candidate_texts" / variant["id"] / f"page_{page}_candidate.md"
            write_text(candidate_path, candidate_text)
            item = {
                "page": page,
                "candidate_id": variant["id"],
                "variant": variant,
                "reference_label": label,
                "reference_path": reference_path.relative_to(ROOT).as_posix(),
                "reference_sha256": sha256_file(reference_path),
                "input_count": len(inputs),
                "input_results": inputs,
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": sha256_file(candidate_path),
                "metrics": metrics(candidate_text, reference_text),
            }
            item["ok_level_candidate"] = (
                item["metrics"]["sequence_similarity_ratio"] >= OK_SIMILARITY
                and item["metrics"]["token_recall"] >= OK_TOKEN_RECALL
            )
            page_results[page].append(item)
            if item["ok_level_candidate"]:
                stop_reached = True
                stop_reason = f"ok_level_candidate_found_for_p{page}_{variant['id']}"
        if stop_reached:
            break
    best_by_page = {}
    for page, results in page_results.items():
        results.sort(key=lambda item: (item["metrics"]["sequence_similarity_ratio"], item["metrics"]["token_recall"]), reverse=True)
        best_by_page[page] = results[0]
        write_json(OUT_ROOT / "rankings" / f"page_{page}_candidate_rankings.json", results)
    shared = []
    candidate_ids = sorted({item["candidate_id"] for results in page_results.values() for item in results})
    for candidate_id in candidate_ids:
        by_page = {page: next((item for item in page_results[page] if item["candidate_id"] == candidate_id), None) for page in PAGES}
        if any(item is None for item in by_page.values()):
            continue
        shared.append(
            {
                "candidate_id": candidate_id,
                "min_similarity": min(item["metrics"]["sequence_similarity_ratio"] for item in by_page.values() if item is not None),
                "min_token_recall": min(item["metrics"]["token_recall"] for item in by_page.values() if item is not None),
                "p018_similarity": by_page["018"]["metrics"]["sequence_similarity_ratio"],
                "p017_similarity": by_page["017"]["metrics"]["sequence_similarity_ratio"],
            }
        )
    shared.sort(key=lambda item: (item["min_similarity"], item["min_token_recall"]), reverse=True)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_auto_search_completed",
        "source_second_pass": "C01TEP2P018P017-G1-VIRAL-001",
        "verified_inputs": verified_inputs,
        "pages": PAGES,
        "candidate_budget": len(variants),
        "candidate_count_attempted_per_page": {page: len(page_results[page]) for page in PAGES},
        "auto_stop_reached": stop_reached,
        "auto_stop_reason": stop_reason,
        "ok_thresholds": {"similarity": OK_SIMILARITY, "token_recall": OK_TOKEN_RECALL},
        "best_by_page": best_by_page,
        "shared_candidate_rankings": shared,
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
        "recommendation": "compare candidate text against references and decide whether to create line/column assembly rule or park P018/P017 for reference-guided handling",
    }
    write_json(OUT_ROOT / "auto_search_p018_p017_report.json", report)
    lines = [
        "# Core 0.1 P018/P017 Auto-Search Column/Line Segmentation - C01TEAS018017-G1-VIRAL-001",
        "",
        "Status: `candidate_only_auto_search_completed`",
        "",
        f"Auto-stop: `{stop_reason}`",
        "",
        "| Page | Best candidate | Similarity | Token recall | OK-level |",
        "|---|---|---:|---:|---|",
    ]
    for page in PAGES:
        best = best_by_page[page]
        lines.append(
            f"| `{page}` | `{best['candidate_id']}` | "
            f"`{best['metrics']['sequence_similarity_ratio']}` | `{best['metrics']['token_recall']}` | "
            f"`{best['ok_level_candidate']}` |"
        )
    if shared:
        lines.extend(
            [
                "",
                "## Best Shared Candidate",
                "",
                f"Candidate: `{shared[0]['candidate_id']}`",
                f"Minimum similarity across P018/P017: `{shared[0]['min_similarity']}`",
                f"Minimum token recall across P018/P017: `{shared[0]['min_token_recall']}`",
                "",
            ]
        )
    lines.extend(
        [
            "Boundary: candidate-only auto-search; no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "auto_search_p018_p017_summary.md", "\n".join(lines))
    manifest_lines = [
        "# P018/P017 Auto-Search Column/Line Segmentation Manifest - C01TEAS018017-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "auto_search_p018_p017_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "auto_search_p018_p017_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
