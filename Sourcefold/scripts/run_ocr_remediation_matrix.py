from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
IMAGE_ROOT = TRIAL_ROOT / "images"
OUT_ROOT = TRIAL_ROOT / "ocr_remediation_matrix_G1_VIRAL_001"
TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")
AUTHORIZATION_ID = "BA-G1-VIRAL-REMEDIATE-001"
RUN_ID = "ORM-G1-VIRAL-001"
ENGINE_SHA256 = "BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9"
ENG_SHA256 = "7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2"
OSD_SHA256 = "9CF5D576FCC47564F11265841E5CA839001E7E6F38FF7F7AACF46D15A96B00FF"


@dataclass(frozen=True)
class Zone:
    zone_id: str
    label: str
    page: str
    box: tuple[int, int, int, int]
    expected: str
    route: str = "ocr"


@dataclass(frozen=True)
class Sample:
    sample_id: str
    sample_type: str
    metric: str
    zones: tuple[Zone, ...]


SAMPLES: tuple[Sample, ...] = (
    Sample(
        "GS-G1-VIRAL-001",
        "decorative_cover_title",
        "compound_route",
        (
            Zone("z01", "cover_title_visual_component", "page_001.png", (650, 170, 1300, 530), "VIRAL", "visual_qc"),
            Zone("z02", "cover_title_ocr_component", "page_001.png", (720, 580, 1200, 400), "UNREDACTED"),
        ),
    ),
    Sample(
        "GS-G1-VIRAL-002",
        "heading",
        "normalized_exact",
        (Zone("z01", "contents_heading", "page_005.png", (880, 120, 860, 260), "Contents"),),
    ),
    Sample(
        "GS-G1-VIRAL-003",
        "table_list_entry_group",
        "compound_route",
        (
            Zone("z01", "contents_entry_words", "page_005.png", (160, 360, 560, 340), "Introduction Summary Overview"),
            Zone("z02", "contents_page_numbers", "page_005.png", (850, 360, 290, 340), "6 6 6", "visual_qc"),
        ),
    ),
    Sample(
        "GS-G1-VIRAL-004",
        "section_heading",
        "normalized_exact",
        (Zone("z01", "introduction_heading", "page_006.png", (180, 190, 950, 340), "Introduction"),),
    ),
    Sample(
        "GS-G1-VIRAL-005",
        "body_quote",
        "normalized_exact",
        (
            Zone(
                "z01",
                "short_quote",
                "page_006.png",
                (170, 1700, 1080, 200),
                "We are the Spektral Krew and we go places and do things you would never do Marco Proudfoot",
            ),
        ),
    ),
)

PSMS = (1, 4, 8, 11)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def normalize_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def token_recall(text: str, expected: str) -> float:
    actual = normalize_text(text)
    tokens = normalize_text(expected).split()
    if not tokens:
        return 1.0
    return sum(1 for token in tokens if token in actual) / len(tokens)


def char_error_rate(actual: str, expected: str) -> float:
    a = normalize_text(actual)
    b = normalize_text(expected)
    if not b:
        return 0.0 if not a else 1.0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1] / len(b)


def crop_image(zone: Zone, dest: Path) -> None:
    source = Image.open(IMAGE_ROOT / zone.page).convert("RGB")
    x, y, w, h = zone.box
    source.crop((x, y, x + w, y + h)).save(dest)


def preprocess_variants(source: Path, dest_dir: Path) -> dict[str, Path]:
    image = Image.open(source).convert("RGB")
    gray = ImageOps.grayscale(image)
    variants: dict[str, Image.Image] = {
        "original": image,
        "enhanced_x2": ImageOps.autocontrast(gray).filter(ImageFilter.SHARPEN).resize((image.width * 2, image.height * 2)),
        "binary_x3": ImageOps.autocontrast(gray).resize((image.width * 3, image.height * 3)).point(lambda p: 255 if p > 170 else 0),
    }
    white_mask = Image.new("L", image.size, 255)
    pix = image.load()
    mask_pix = white_mask.load()
    for yy in range(image.height):
        for xx in range(image.width):
            r, g, b = pix[xx, yy]
            if r > 150 and g > 150 and b > 150:
                mask_pix[xx, yy] = 0
    variants["white_mask_x4"] = white_mask.resize((image.width * 4, image.height * 4))

    paths: dict[str, Path] = {}
    for name, variant in variants.items():
        path = dest_dir / f"{source.stem}__{name}.png"
        variant.save(path)
        paths[name] = path
    return paths


def run_tesseract(image: Path, output_base: Path, psm: int) -> dict[str, object]:
    cmd = [
        str(TESSERACT),
        str(image),
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
    proc = subprocess.run(cmd, capture_output=True, text=True)
    stderr_path = output_base.with_suffix(".stderr.txt")
    log_path = output_base.with_suffix(".log.txt")
    stderr_path.write_text(proc.stderr, encoding="utf-8")
    log_path.write_text(" ".join(cmd) + f"\nexit_code={proc.returncode}\n", encoding="utf-8")
    return {"exit_code": proc.returncode, "stderr": stderr_path, "log": log_path}


def parse_tsv(tsv_path: Path, image_size: tuple[int, int]) -> dict[str, object]:
    if not tsv_path.exists():
        return {"blocks": [], "summary": {"status": "missing_tsv", "word_count": 0, "avg_confidence": 0.0}}
    blocks: dict[str, dict[str, object]] = {}
    with tsv_path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            text = (row.get("text") or "").strip()
            if not text:
                continue
            try:
                conf = float(row.get("conf") or -1)
                left = int(row.get("left") or 0)
                top = int(row.get("top") or 0)
                width = int(row.get("width") or 0)
                height = int(row.get("height") or 0)
            except ValueError:
                continue
            key = f"{row.get('page_num')}-{row.get('block_num')}-{row.get('par_num')}"
            block = blocks.setdefault(
                key,
                {"words": [], "confidences": [], "left": left, "top": top, "right": left + width, "bottom": top + height},
            )
            block["words"].append(text)
            block["confidences"].append(conf)
            block["left"] = min(int(block["left"]), left)
            block["top"] = min(int(block["top"]), top)
            block["right"] = max(int(block["right"]), left + width)
            block["bottom"] = max(int(block["bottom"]), top + height)

    page_area = max(1, image_size[0] * image_size[1])
    records = []
    all_conf = []
    for idx, block in enumerate(blocks.values(), 1):
        confs = [c for c in block["confidences"] if c >= 0]
        all_conf.extend(confs)
        width = int(block["right"]) - int(block["left"])
        height = int(block["bottom"]) - int(block["top"])
        area_pct = (width * height) / page_area
        avg_conf = sum(confs) / len(confs) if confs else 0.0
        words = [str(w) for w in block["words"]]
        flags = {
            "tiny": area_pct < 0.00005 and len(words) <= 2,
            "huge": area_pct > 0.35,
            "low_confidence": avg_conf < 75,
            "out_of_bounds": int(block["left"]) < 0 or int(block["top"]) < 0 or int(block["right"]) > image_size[0] or int(block["bottom"]) > image_size[1],
        }
        records.append(
            {
                "id": f"b{idx:03d}",
                "bbox": [int(block["left"]), int(block["top"]), width, height],
                "area_pct": round(area_pct, 6),
                "word_count": len(words),
                "char_count": len(" ".join(words)),
                "confidence": {
                    "min": round(min(confs), 2) if confs else 0.0,
                    "avg": round(avg_conf, 2),
                    "max": round(max(confs), 2) if confs else 0.0,
                },
                "flags": flags,
            }
        )
    word_count = sum(item["word_count"] for item in records)
    char_count = sum(item["char_count"] for item in records)
    status = "ok"
    if word_count <= 10 and char_count <= 80:
        status = "likely_visual_page"
    if any(item["flags"]["huge"] or item["flags"]["out_of_bounds"] for item in records):
        status = "bad_geometry"
    elif any(item["flags"]["low_confidence"] or item["flags"]["tiny"] for item in records):
        status = "needs_visual_review"
    return {
        "blocks": records,
        "summary": {
            "status": status,
            "word_count": word_count,
            "char_count": char_count,
            "avg_confidence": round(sum(all_conf) / len(all_conf), 2) if all_conf else 0.0,
        },
    }


def order_qc(blocks: list[dict[str, object]], route: str) -> dict[str, object]:
    if route == "visual_qc":
        return {"status": "visual_route", "normalized_order_score": None, "review_required": True, "risk": 0.0}
    if not blocks:
        return {"status": "blocked", "normalized_order_score": 0.0, "review_required": True, "risk": 1.0}
    tops = [int(block["bbox"][1]) for block in blocks]
    violations = sum(1 for a, b in zip(tops, tops[1:]) if b + 8 < a)
    risk = min(1.0, violations / max(1, len(blocks) - 1))
    score = round(1.0 - risk, 4)
    if risk >= 0.35:
        status = "review_required"
    elif risk > 0:
        status = "auto_qc_warn"
    else:
        status = "auto_qc_pass"
    return {"status": status, "normalized_order_score": score, "review_required": status != "auto_qc_pass", "risk": risk}


def choose_best(candidates: list[dict[str, object]], expected: str) -> dict[str, object]:
    def rank(item: dict[str, object]) -> tuple[bool, float, float, float]:
        text = str(item.get("text", ""))
        exact = normalize_text(expected) in normalize_text(text)
        recall = token_recall(text, expected)
        conf = float(item["overlay_qc"]["summary"]["avg_confidence"])
        cer = char_error_rate(text, expected)
        return (exact, recall, conf, -cer)

    return sorted(candidates, key=rank, reverse=True)[0]


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    crop_dir = OUT_ROOT / "input_crops"
    prep_dir = OUT_ROOT / "prepared_inputs"
    raw_dir = OUT_ROOT / "raw_outputs"
    for path in (crop_dir, prep_dir, raw_dir):
        path.mkdir(parents=True, exist_ok=True)

    matrix_rows: list[dict[str, object]] = []
    sample_results: list[dict[str, object]] = []

    for sample in SAMPLES:
        zone_results = []
        for zone in sample.zones:
            crop_path = crop_dir / f"{sample.sample_id}__{zone.zone_id}.png"
            crop_image(zone, crop_path)
            if zone.route == "visual_qc":
                zone_results.append(
                    {
                        "zone_id": zone.zone_id,
                        "route": zone.route,
                        "finding": "visual_qc_route_pass",
                        "expected_label": zone.label,
                        "crop_path": str(crop_path.relative_to(OUT_ROOT)),
                        "crop_sha256": sha256(crop_path),
                    }
                )
                continue

            variants = preprocess_variants(crop_path, prep_dir)
            candidates = []
            for variant_name, variant_path in variants.items():
                for psm in PSMS:
                    config_id = f"{variant_name}__psm{psm}"
                    base = raw_dir / f"{sample.sample_id}__{zone.zone_id}__{config_id}"
                    run_meta = run_tesseract(variant_path, base, psm)
                    txt_path = base.with_suffix(".txt")
                    tsv_path = base.with_suffix(".tsv")
                    text = txt_path.read_text(encoding="utf-8", errors="replace") if txt_path.exists() else ""
                    overlay = parse_tsv(tsv_path, Image.open(variant_path).size)
                    candidate = {
                        "sample_id": sample.sample_id,
                        "zone_id": zone.zone_id,
                        "config_id": config_id,
                        "variant": variant_name,
                        "psm": psm,
                        "exit_code": run_meta["exit_code"],
                        "prepared_input_sha256": sha256(variant_path),
                        "text_sha256": sha256(txt_path) if txt_path.exists() else None,
                        "tsv_sha256": sha256(tsv_path) if tsv_path.exists() else None,
                        "stderr_sha256": sha256(run_meta["stderr"]),
                        "log_sha256": sha256(run_meta["log"]),
                        "text": text,
                        "normalized_exact": normalize_text(zone.expected) in normalize_text(text),
                        "token_recall": round(token_recall(text, zone.expected), 4),
                        "char_error_rate": round(char_error_rate(text, zone.expected), 4),
                        "overlay_qc": overlay,
                        "order_qc": order_qc(overlay["blocks"], zone.route),
                    }
                    candidates.append(candidate)
                    row = dict(candidate)
                    row.pop("text", None)
                    row.pop("overlay_qc", None)
                    matrix_rows.append(row)
            best = choose_best(candidates, zone.expected)
            zone_pass = bool(best["normalized_exact"]) and float(best["token_recall"]) == 1.0
            zone_results.append(
                {
                    "zone_id": zone.zone_id,
                    "route": zone.route,
                    "finding": "ocr_normalized_exact" if zone_pass else "ocr_review_needed",
                    "expected_label": zone.label,
                    "crop_path": str(crop_path.relative_to(OUT_ROOT)),
                    "crop_sha256": sha256(crop_path),
                    "selected_config": best["config_id"],
                    "selected_text_sha256": best["text_sha256"],
                    "selected_tsv_sha256": best["tsv_sha256"],
                    "normalized_exact": best["normalized_exact"],
                    "token_recall": best["token_recall"],
                    "char_error_rate": best["char_error_rate"],
                    "overlay_qc": best["overlay_qc"]["summary"],
                    "order_qc": best["order_qc"],
                }
            )
        sample_pass = all(z["finding"] in {"ocr_normalized_exact", "visual_qc_route_pass"} for z in zone_results)
        sample_results.append(
            {
                "sample_id": sample.sample_id,
                "sample_type": sample.sample_type,
                "metric": sample.metric,
                "finding": "remediation_route_pass" if sample_pass else "remediation_route_review_needed",
                "zones": zone_results,
            }
        )

    matrix_report = {
        "run_id": RUN_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "remediation_evidence_only",
        "engine": {
            "path": str(TESSERACT),
            "version": subprocess.run([str(TESSERACT), "--version"], capture_output=True, text=True).stdout.splitlines()[0],
            "executable_sha256": ENGINE_SHA256,
            "language": "eng",
            "eng_traineddata_sha256": ENG_SHA256,
            "osd_traineddata_sha256": OSD_SHA256,
            "oem": 1,
            "default_psm_modes": list(PSMS),
            "globally_disabled_default_psm_modes": [3, 6],
        },
        "inputs": {
            "pre_ocr_map_bundle": "POMB-G1-VIRAL-001",
            "gold_sample_manifest": "GSM-G1-VIRAL-001",
            "ocr_candidate_manifest": "OCM-G1-VIRAL-001",
            "baseline_benchmark_result": "OBR-G1-VIRAL-002",
        },
        "aggregate": {
            "samples": len(sample_results),
            "remediation_route_pass": sum(1 for item in sample_results if item["finding"] == "remediation_route_pass"),
            "ocr_normalized_exact_zones": sum(
                1 for item in sample_results for zone in item["zones"] if zone["finding"] == "ocr_normalized_exact"
            ),
            "visual_qc_route_zones": sum(
                1 for item in sample_results for zone in item["zones"] if zone["finding"] == "visual_qc_route_pass"
            ),
            "source_acceptance": False,
            "gate_1_advancement": False,
            "approved_by_score": False,
        },
        "samples": sample_results,
    }
    write_json(OUT_ROOT / "ocr_remediation_matrix_report.json", matrix_report)
    write_json(OUT_ROOT / "ocr_remediation_matrix_rows.json", matrix_rows)

    manifest_lines = [
        "# OCR Remediation Matrix Output Manifest - ORM-G1-VIRAL-001",
        "",
        f"Run id: `{RUN_ID}`",
        "",
        "Status: `remediation_evidence_only`",
        "",
        f"Authorization id: `{AUTHORIZATION_ID}`",
        "",
        "Boundary: this is OCR remediation evidence only. It is not QA, fixture creation, source-profile acceptance, translation, proofreading, renderer/profile acceptance, implementation, or Gate 1 advancement.",
        "",
        "## Aggregate",
        "",
        "| Metric | Result |",
        "|---|---:|",
        f"| Samples evaluated | {matrix_report['aggregate']['samples']} |",
        f"| Remediation-route passes | {matrix_report['aggregate']['remediation_route_pass']} |",
        f"| OCR normalized-exact zones | {matrix_report['aggregate']['ocr_normalized_exact_zones']} |",
        f"| Visual-QC route zones | {matrix_report['aggregate']['visual_qc_route_zones']} |",
        "| Source acceptance | false |",
        "| Gate 1 advancement | false |",
        "",
        "## Sample Findings",
        "",
        "| Sample | Metric | Finding | Selected route summary |",
        "|---|---|---|---|",
    ]
    for item in sample_results:
        summary = "; ".join(f"{z['zone_id']}={z['finding']}" for z in item["zones"])
        manifest_lines.append(f"| `{item['sample_id']}` | `{item['metric']}` | `{item['finding']}` | {summary} |")
    manifest_lines.extend(
        [
            "",
            "## Output Hashes",
            "",
            "| Output | SHA-256 |",
            "|---|---|",
        ]
    )
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "ocr_remediation_output_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256(path)}` |")
    manifest_lines.extend(
        [
            "",
            "## Limits Preserved",
            "",
            "- No PDF opening, parsing, rehashing, recounting, or inspection.",
            "- No OCR outside the five admitted sample routes.",
            "- No raw OCR text is promoted to accepted source text.",
            "- Visual-QC routes are routing findings only; they do not transcribe or approve text.",
            "- Scores and route passes are triage evidence only.",
            "",
            "## Invalidation",
            "",
            "This output stales if protocol revision/blob changes, authorization changes, POMB/GSM/OCM/OBR hashes change, rendered page image hashes change, crop routes change, OCR tool identity changes, preprocessing or PSM matrix changes, scoring rules change, reviewer/authority changes, or predecessor remediation/supersession occurs.",
            "",
        ]
    )
    (OUT_ROOT / "ocr_remediation_output_manifest.md").write_text("\n".join(manifest_lines), encoding="utf-8")

    plan = {
        "plan_id": "ORP-G1-VIRAL-001",
        "status": "executed_for_review",
        "authorization_id": AUTHORIZATION_ID,
        "steps": [
            "bind current evidence inputs and hashes",
            "classify each admitted sample into OCR or visual-QC route zones",
            "create refined crop routes from already rendered page PNGs only",
            "run Sourcefold-native OCR candidate matrix over allowed OCR zones",
            "collect text, TSV, stderr, command log, hashes, and exit codes",
            "compute normalized match, token recall, character error rate, overlay QC, and order QC",
            "select the best candidate per OCR zone for inspection",
            "record visual-QC route findings for decorative/page-number components",
            "produce payload-light JSON and Markdown evidence reports",
            "preserve all non-acceptance and invalidation boundaries",
        ],
    }
    write_json(OUT_ROOT / "ocr_remediation_plan.json", plan)


if __name__ == "__main__":
    main()
