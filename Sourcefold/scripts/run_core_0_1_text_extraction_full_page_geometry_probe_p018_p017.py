from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_full_page_geometry_probe_p018_p017_G1_VIRAL_001"
LEDGER = overview.LEDGER
TESSERACT = overview.TESSERACT

LANE_ID = "C01TEFG017018-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FULL-PAGE-GEOMETRY-P018-P017-001"
HUMAN_DECISION = "мне не нравится такой вывод. пробуй заново , зови сол и терру. думайте и пробуйте"
REFERENCE_GUIDED_REPAIR_REPORT = (
    TRIAL_ROOT
    / "core_0_1_text_extraction_reference_guided_repair_p018_p017_G1_VIRAL_001"
    / "reference_guided_repair_p018_p017_report.json"
)
REFERENCE_GUIDED_REPAIR_REPORT_SHA256 = "EEAB4CA9449AD7FA39E9C6EAC3B5BE87796E240908615BF4E115F711B1EC915D"
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
    parser = argparse.ArgumentParser(description="Run P018/P017 full-page geometry OCR probe.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P018/P017 full-page geometry probe is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P018/P017 full-page geometry probe requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P018/P017 full-page geometry probe requires the exact bounded human decision")


def verify_inputs() -> dict:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    report_hash = sha256_file(REFERENCE_GUIDED_REPAIR_REPORT)
    if report_hash != REFERENCE_GUIDED_REPAIR_REPORT_SHA256:
        raise SystemExit(f"C01TERG018017 report hash mismatch: {report_hash}")
    return {
        "reference_guided_repair_report": {
            "path": REFERENCE_GUIDED_REPAIR_REPORT.relative_to(ROOT).as_posix(),
            "sha256": report_hash,
        }
    }


def page_image_path(page: str) -> Path:
    path = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets" / f"page_{page}.png"
    if not path.exists():
        raise SystemExit(f"P{page} missing full-page review image: {path}")
    return path


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


def body_region(source: Image.Image, box: tuple[int, int, int, int], border: int) -> Image.Image:
    crop = source.crop(box).convert("RGB")
    canvas = Image.new("RGB", (crop.width + border * 2, crop.height + border * 2), "white")
    canvas.paste(crop, (border, border))
    return ImageOps.autocontrast(ImageOps.grayscale(canvas)).convert("RGB")


def bright_title_region(source: Image.Image, box: tuple[int, int, int, int], scale: int, threshold: int, border: int) -> Image.Image:
    crop = source.crop(box).convert("RGB")
    enlarged = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    gray = ImageOps.grayscale(enlarged)
    # Page 017 title is white text over illustration, so isolate bright glyphs
    # as black text on a white field before OCR.
    binary = gray.point(lambda px: 0 if px >= threshold else 255)
    cleaned = binary.filter(ImageFilter.MedianFilter(3)).convert("RGB")
    return ImageOps.expand(cleaned, border=border, fill="white")


def candidate_specs() -> dict[str, list[dict]]:
    return {
        "018": [
            {
                "id": "full_page_expanded_overlap_psm4",
                "description": "Full-page-derived expanded left/right columns with overlap-safe gutter.",
                "regions": [
                    {"id": "left_column", "kind": "body", "box": (185, 200, 1260, 3060), "psm": 4, "border": 24},
                    {"id": "right_column", "kind": "body", "box": (1245, 200, 2360, 3060), "psm": 4, "border": 24},
                ],
            },
            {
                "id": "full_page_expanded_overlap_psm6",
                "description": "Same full-page geometry with PSM 6.",
                "regions": [
                    {"id": "left_column", "kind": "body", "box": (185, 200, 1260, 3060), "psm": 6, "border": 24},
                    {"id": "right_column", "kind": "body", "box": (1245, 200, 2360, 3060), "psm": 6, "border": 24},
                ],
            },
        ],
        "017": [
            {
                "id": "full_page_body_only_psm4",
                "description": "Full-page-derived body columns without the hero title OCR region.",
                "regions": [
                    {"id": "left_body", "kind": "body", "box": (170, 1780, 1245, 3140), "psm": 4, "border": 24},
                    {"id": "right_body", "kind": "body", "box": (1245, 1740, 2360, 3100), "psm": 4, "border": 24},
                ],
            },
            {
                "id": "full_page_bright_title_body_psm7_4_4",
                "description": "Full-page hero-title bright-text isolation plus body columns.",
                "regions": [
                    {
                        "id": "hero_title",
                        "kind": "bright_title",
                        "box": (90, 90, 1300, 520),
                        "psm": 7,
                        "scale": 2,
                        "threshold": 225,
                        "border": 80,
                    },
                    {"id": "left_body", "kind": "body", "box": (170, 1780, 1245, 3140), "psm": 4, "border": 24},
                    {"id": "right_body", "kind": "body", "box": (1245, 1740, 2360, 3100), "psm": 4, "border": 24},
                ],
            },
            {
                "id": "full_page_bright_title_body_alt_psm7_4_4",
                "description": "Alternate bright-title isolation plus body columns.",
                "regions": [
                    {
                        "id": "hero_title",
                        "kind": "bright_title",
                        "box": (90, 90, 1300, 520),
                        "psm": 7,
                        "scale": 3,
                        "threshold": 205,
                        "border": 80,
                    },
                    {"id": "left_body", "kind": "body", "box": (170, 1780, 1245, 3140), "psm": 4, "border": 24},
                    {"id": "right_body", "kind": "body", "box": (1245, 1740, 2360, 3100), "psm": 4, "border": 24},
                ],
            },
        ],
    }


def prepare_region(source_image: Image.Image, spec: dict) -> Image.Image:
    box = tuple(spec["box"])
    if spec["kind"] == "body":
        return body_region(source_image, box, spec["border"])
    if spec["kind"] == "bright_title":
        return bright_title_region(source_image, box, spec["scale"], spec["threshold"], spec["border"])
    raise ValueError(f"unknown region kind: {spec['kind']}")


def run_tesseract(prepared: Path, base: Path, psm: int) -> tuple[str, dict]:
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
        "prepared_region_path": prepared.relative_to(ROOT).as_posix(),
        "prepared_region_sha256": sha256_file(prepared),
        "raw_ocr_text_path": text_path.relative_to(ROOT).as_posix(),
        "raw_ocr_text_sha256": sha256_file(text_path),
        "raw_ocr_tsv_path": tsv_path.relative_to(ROOT).as_posix(),
        "raw_ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_path": stderr_path.relative_to(ROOT).as_posix(),
        "stdout_path": stdout_path.relative_to(ROOT).as_posix(),
    }


def generate_candidate(page: str, spec: dict) -> dict:
    image_path = page_image_path(page)
    source_image = Image.open(image_path).convert("RGB")
    chunks: list[str] = []
    region_results: list[dict] = []
    for index, region in enumerate(spec["regions"], start=1):
        prepared = OUT_ROOT / "prepared_regions" / spec["id"] / f"p{page}" / f"{index:02d}_{region['id']}.png"
        base = OUT_ROOT / "raw_ocr" / spec["id"] / f"p{page}" / f"{index:02d}_{region['id']}"
        prepared.parent.mkdir(parents=True, exist_ok=True)
        base.parent.mkdir(parents=True, exist_ok=True)
        prepare_region(source_image, region).save(prepared)
        text, ocr_result = run_tesseract(prepared, base, region["psm"])
        chunks.append(f"## {region['id']}\n\n{text.strip()}")
        region_results.append(
            {
                "region_id": region["id"],
                "region_kind": region["kind"],
                "page_space_box": list(region["box"]),
                "psm": region["psm"],
                "ocr_result": ocr_result,
            }
        )
    candidate_text = "\n\n".join(chunks).strip() + "\n"
    candidate_path = OUT_ROOT / "candidate_texts" / spec["id"] / f"page_{page}_candidate.md"
    write_text(candidate_path, candidate_text)
    return {
        "page": page,
        "candidate_id": spec["id"],
        "description": spec["description"],
        "source_page_image_path": image_path.relative_to(ROOT).as_posix(),
        "source_page_image_sha256": sha256_file(image_path),
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_path),
        "region_results": region_results,
    }


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)

    page_results: dict[str, list[dict]] = {}
    for page, specs in candidate_specs().items():
        page_results[page] = [generate_candidate(page, spec) for spec in specs]

    # No-leak boundary: reference text is loaded only after all candidate text
    # files exist and have recorded hashes.
    for page, results in page_results.items():
        label, reference_path, reference_text = reference_for_page(page)
        for result in results:
            candidate_path = ROOT / result["candidate_text_path"]
            candidate_text = candidate_path.read_text(encoding="utf-8", errors="replace")
            page_metrics = metrics(candidate_text, reference_text)
            result["reference_label"] = label
            result["reference_path"] = reference_path.relative_to(ROOT).as_posix()
            result["reference_sha256"] = sha256_file(reference_path)
            result["reference_risk_flag"] = label != "reference_ocr_verified_text_map"
            result["metrics"] = page_metrics
            result["ok_level_candidate"] = (
                page_metrics["sequence_similarity_ratio"] >= OK_SIMILARITY
                and page_metrics["token_recall"] >= OK_TOKEN_RECALL
            )
        results.sort(
            key=lambda item: (
                item["metrics"]["sequence_similarity_ratio"],
                item["metrics"]["token_recall"],
            ),
            reverse=True,
        )
        write_json(OUT_ROOT / "rankings" / f"page_{page}_candidate_rankings.json", results)

    best_by_page = {page: results[0] for page, results in page_results.items()}
    all_pages_ok = all(item["ok_level_candidate"] for item in best_by_page.values())
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_full_page_geometry_probe_completed",
        "source_reference_guided_repair": "C01TERG018017-G1-VIRAL-001",
        "verified_inputs": verified_inputs,
        "pages": PAGES,
        "ok_thresholds": {"similarity": OK_SIMILARITY, "token_recall": OK_TOKEN_RECALL},
        "candidate_generation_reference_text_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "candidate_generation_inputs": ["full_page_review_png", "fixed_page_space_geometry", "tesseract_ocr"],
        "candidate_count_per_page": {page: len(results) for page, results in page_results.items()},
        "best_by_page": best_by_page,
        "all_pages_ok_level": all_pages_ok,
        "reference_guided_repair_used": False,
        "independent_ocr_candidate": True,
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
        "recommendation": (
            "Promote full-page-derived geometry as the next independent OCR candidate policy "
            "for P017/P018-like complex pages; keep reference maps labeled as not OCR verified."
        ),
    }
    write_json(OUT_ROOT / "full_page_geometry_probe_p018_p017_report.json", report)

    lines = [
        "# Core 0.1 P018/P017 Full-Page Geometry OCR Probe - C01TEFG017018-G1-VIRAL-001",
        "",
        "Status: `candidate_only_full_page_geometry_probe_completed`",
        "",
        "Candidate generation uses full-page PNG geometry and Tesseract only; reference text is scorer-only after candidate hashes are sealed.",
        "",
        "| Page | Best candidate | Similarity | Token recall | OK-level | Reference risk |",
        "|---|---|---:|---:|---|---|",
    ]
    for page in PAGES:
        best = best_by_page[page]
        lines.append(
            f"| `{page}` | `{best['candidate_id']}` | "
            f"`{best['metrics']['sequence_similarity_ratio']}` | `{best['metrics']['token_recall']}` | "
            f"`{best['ok_level_candidate']}` | `{best['reference_risk_flag']}` |"
        )
    lines.extend(
        [
            "",
            f"All pages OK-level: `{all_pages_ok}`",
            "",
            "Boundary: candidate-only independent OCR probe; no reference-guided repair, no accepted/semantic/page-status/source/runtime mutation, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "full_page_geometry_probe_p018_p017_summary.md", "\n".join(lines))

    manifest_lines = [
        "# P018/P017 Full-Page Geometry OCR Probe Manifest - C01TEFG017018-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "full_page_geometry_probe_p018_p017_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "full_page_geometry_probe_p018_p017_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
