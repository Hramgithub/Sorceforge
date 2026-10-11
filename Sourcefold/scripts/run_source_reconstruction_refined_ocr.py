from __future__ import annotations

import csv
import hashlib
import json
import argparse
import re
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
INPUT_ROOT = TRIAL_ROOT / "source_reconstruction_crop_overlay_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "source_reconstruction_refined_ocr_G1_VIRAL_001"
PREP_ROOT = OUT_ROOT / "prepared_inputs"
RAW_ROOT = OUT_ROOT / "raw_outputs"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-RECON-REFINED-OCR-001"
RUN_ID = "SRFO-G1-VIRAL-001"
INPUT_REPORT_ID = "SRCO-G1-VIRAL-001"
INPUT_REPORT_SHA256 = "08B77397484FF43C6E4E466632531B15829EA3C34A75F79C6DE84B70E433C78F"
ONLY_REGION_ADMISSION_ID = "SRA-G1-VIRAL-001-R003"
ONLY_SAMPLE_ID = "GS-G1-VIRAL-003"
ONLY_PAGE_ID = "PG-G1-VIRAL-P005"
ONLY_PREDECESSOR_ZONE_ID = "z01"
ONLY_SOURCE_CROP_SHA256 = "54E0E3B0A956EA0BA215987D25B242EED3A803100AD87C2E8949E3EA4592F66A"
ONLY_REFINED_CROP_SHA256 = "A09B5848048C3BD20FEB71B0FC37FC55E108AA08454BCFB1156D3FAD62E5B40F"

TESSERACT = Path(r"D:\NRI\.tools\tesseract\tesseract.exe")
ENGINE_SHA256 = "BABB405F4366B480D02CD8FF2BAC8D497170F6C1711CE6F3D5D8BF0FB7FA6ED9"
ENG_SHA256 = "7D4322BD2A7749724879683FC3912CB542F19906C83BCC1A52132556427170B2"
OSD_SHA256 = "9CF5D576FCC47564F11265841E5CA839001E7E6F38FF7F7AACF46D15A96B00FF"

PSMS = (1, 4, 8, 11)
EXPECTED_TEXT_BY_REGION = {
    "SRA-G1-VIRAL-001-R003": "Introduction Summary",
}


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def repo_path(path: Path) -> str:
    return str(path.relative_to(ROOT))


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


def preprocess_variants(source: Path) -> dict[str, Path]:
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
        path = PREP_ROOT / f"{source.stem}__{name}.png"
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
    return {"exit_code": proc.returncode, "stderr": stderr_path, "log": log_path, "command": cmd}


def parse_tsv(tsv_path: Path, image_size: tuple[int, int]) -> dict[str, object]:
    if not tsv_path.exists():
        return {"blocks": [], "summary": {"status": "missing_tsv", "word_count": 0, "avg_confidence": 0.0}}
    blocks: dict[str, dict[str, object]] = {}
    with tsv_path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
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
        words = [str(word) for word in block["words"]]
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
    word_count = sum(int(item["word_count"]) for item in records)
    char_count = sum(int(item["char_count"]) for item in records)
    status = "ok"
    if word_count <= 10 and char_count <= 80:
        status = "short_text"
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


def order_qc(blocks: list[dict[str, object]]) -> dict[str, object]:
    if not blocks:
        return {"status": "blocked", "normalized_order_score": 0.0, "review_required": True}
    tops = [int(block["bbox"][1]) for block in blocks]
    violations = sum(1 for a, b in zip(tops, tops[1:]) if b + 8 < a)
    score = round(1.0 - min(1.0, violations / max(1, len(blocks) - 1)), 4)
    status = "auto_qc_pass" if violations == 0 else "auto_qc_warn"
    return {"status": status, "normalized_order_score": score, "review_required": status != "auto_qc_pass"}


def rank_candidate(item: dict[str, object]) -> tuple[bool, float, float, float]:
    return (
        bool(item["normalized_exact"]),
        float(item["token_recall"]),
        float(item["overlay_qc"]["summary"]["avg_confidence"]),
        -float(item["char_error_rate"]),
    )


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run one bounded refined OCR evidence step.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("refined OCR is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"refined OCR requires {AUTHORIZATION_ID}")


def build() -> None:
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    PREP_ROOT.mkdir(parents=True, exist_ok=True)
    RAW_ROOT.mkdir(parents=True, exist_ok=True)

    input_report_path = INPUT_ROOT / "source_reconstruction_crop_overlay_report.json"
    if sha256_file(input_report_path) != INPUT_REPORT_SHA256:
        raise SystemExit("SRCO input report hash mismatch")
    srco = read_json(input_report_path)
    if srco["report_id"] != INPUT_REPORT_ID:
        raise SystemExit(f"input report must be {INPUT_REPORT_ID}")

    refined_inputs = [record for record in srco["candidate_records"] if record["new_ocr_required"] is True]
    if len(refined_inputs) != 1:
        raise SystemExit("refined OCR run must remain bounded to exactly one SRCO record")
    only = refined_inputs[0]
    if only["region_admission_id"] != ONLY_REGION_ADMISSION_ID:
        raise SystemExit(f"refined OCR target must be {ONLY_REGION_ADMISSION_ID}")
    if only["sample_id"] != ONLY_SAMPLE_ID or only["page_id"] != ONLY_PAGE_ID:
        raise SystemExit("refined OCR target sample/page identity mismatch")
    if only["predecessor_zone_id"] != ONLY_PREDECESSOR_ZONE_ID:
        raise SystemExit("refined OCR predecessor zone mismatch")
    if only["predecessor_crop_sha256"] != ONLY_SOURCE_CROP_SHA256:
        raise SystemExit("refined OCR source crop hash mismatch")

    all_rows: list[dict[str, object]] = []
    input_results: list[dict[str, object]] = []
    for record in refined_inputs:
        region_id = str(record["region_admission_id"])
        expected = EXPECTED_TEXT_BY_REGION[region_id]
        artifact = record["crop_overlay_artifact"]
        crop_path = ROOT / str(artifact["path"])
        if artifact["sha256"] != ONLY_REFINED_CROP_SHA256 or sha256_file(crop_path) != ONLY_REFINED_CROP_SHA256:
            raise SystemExit(f"crop hash mismatch for {region_id}")
        if artifact["source_input_crop_sha256"] != ONLY_SOURCE_CROP_SHA256:
            raise SystemExit(f"source crop hash mismatch for {region_id}")
        variants = preprocess_variants(crop_path)
        candidates = []
        for variant_name, variant_path in variants.items():
            for psm in PSMS:
                config_id = f"{variant_name}__psm{psm}"
                output_base = RAW_ROOT / f"{region_id}__{config_id}"
                run_meta = run_tesseract(variant_path, output_base, psm)
                txt_path = output_base.with_suffix(".txt")
                tsv_path = output_base.with_suffix(".tsv")
                text = txt_path.read_text(encoding="utf-8", errors="replace") if txt_path.exists() else ""
                overlay = parse_tsv(tsv_path, Image.open(variant_path).size)
                candidate = {
                    "region_admission_id": region_id,
                    "sample_id": record["sample_id"],
                    "page_id": record["page_id"],
                    "region_id": record["region_id"],
                    "predecessor_zone_id": record["predecessor_zone_id"],
                    "route_class": record["route_class"],
                    "review_class": record["review_class"],
                    "config_id": config_id,
                    "variant": variant_name,
                    "psm": psm,
                    "exit_code": run_meta["exit_code"],
                    "prepared_input": repo_path(variant_path),
                    "prepared_input_sha256": sha256_file(variant_path),
                    "raw_text": repo_path(txt_path) if txt_path.exists() else None,
                    "raw_text_sha256": sha256_file(txt_path) if txt_path.exists() else None,
                    "raw_tsv": repo_path(tsv_path) if tsv_path.exists() else None,
                    "raw_tsv_sha256": sha256_file(tsv_path) if tsv_path.exists() else None,
                    "stderr_sha256": sha256_file(run_meta["stderr"]),
                    "log_sha256": sha256_file(run_meta["log"]),
                    "normalized_exact": normalize_text(expected) in normalize_text(text),
                    "token_recall": round(token_recall(text, expected), 4),
                    "char_error_rate": round(char_error_rate(text, expected), 4),
                    "overlay_qc": overlay,
                    "order_qc": order_qc(overlay["blocks"]),
                    "source_acceptance": False,
                }
                candidates.append(candidate)
                row = dict(candidate)
                row.pop("overlay_qc", None)
                all_rows.append(row)
        best = sorted(candidates, key=rank_candidate, reverse=True)[0]
        input_results.append(
            {
                "region_admission_id": region_id,
                "sample_id": record["sample_id"],
                "page_id": record["page_id"],
                "region_id": record["region_id"],
                "predecessor_zone_id": record["predecessor_zone_id"],
                "route_class": record["route_class"],
                "review_class": record["review_class"],
                "input_crop": artifact["path"],
                "input_crop_sha256": artifact["sha256"],
                "source_input_crop": artifact["source_input_crop"],
                "source_input_crop_sha256": artifact["source_input_crop_sha256"],
                "expected_metric_text_sha256": hashlib.sha256(expected.encode("utf-8")).hexdigest().upper(),
                "metric_scope": "refined_crop_visible_text_only",
                "replaces_full_region_text": False,
                "selected_config": best["config_id"],
                "selected_text_sha256": best["raw_text_sha256"],
                "selected_tsv_sha256": best["raw_tsv_sha256"],
                "normalized_exact": best["normalized_exact"],
                "token_recall": best["token_recall"],
                "char_error_rate": best["char_error_rate"],
                "overlay_qc": best["overlay_qc"]["summary"],
                "order_qc": best["order_qc"],
                "human_review_ready": False,
                "source_acceptance": False,
                "next_action": "rebuild_source_reconstruction_package_after_overlay_and_visual_qc_review",
            }
        )

    report = {
        "run_id": RUN_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "refined_ocr_evidence_only",
        "input_report_id": INPUT_REPORT_ID,
        "input_report_sha256": INPUT_REPORT_SHA256,
        "source_acceptance": False,
        "qa_acceptance": False,
        "gate_1_advancement": False,
        "pdf_opened_or_parsed": False,
        "raw_ocr_outputs_modified": False,
        "ocr_executed": True,
        "engine": {
            "path": str(TESSERACT),
            "version": subprocess.run([str(TESSERACT), "--version"], capture_output=True, text=True).stdout.splitlines()[0],
            "executable_sha256": ENGINE_SHA256,
            "language": "eng",
            "eng_traineddata_sha256": ENG_SHA256,
            "osd_traineddata_sha256": OSD_SHA256,
            "oem": 1,
            "psm_modes": list(PSMS),
            "disabled_default_psm_modes": [3, 6],
        },
        "inputs": input_results,
        "summary": {
            "refined_input_records": len(input_results),
            "matrix_rows": len(all_rows),
            "normalized_exact_records": sum(1 for item in input_results if item["normalized_exact"] is True),
            "human_review_ready": False,
            "human_review_blocked": True,
        },
        "scope_note": "SRFO evaluates the visible text inside the refined subcrop only; it does not replace the full contents/list region and does not accept source text.",
        "next_authorization_recommendation": "BA-G1-VIRAL-SOURCE-RECON-REBUILD-001",
    }
    write_json(OUT_ROOT / "source_reconstruction_refined_ocr_report.json", report)
    write_json(OUT_ROOT / "source_reconstruction_refined_ocr_rows.json", all_rows)

    lines = [
        "# Source Reconstruction Refined OCR - SRFO-G1-VIRAL-001",
        "",
        "Status: `refined_ocr_evidence_only`",
        "",
        "Boundary: this is a bounded OCR rerun over one SRCO refined crop only. It is not source acceptance, QA acceptance, fixture creation, translation, proofreading, implementation, or Gate 1 advancement.",
        "",
        "## Summary",
        "",
        f"- Refined input records: `{report['summary']['refined_input_records']}`",
        f"- Matrix rows: `{report['summary']['matrix_rows']}`",
        f"- Normalized exact records: `{report['summary']['normalized_exact_records']}`",
        "- Human review ready: `false`",
        "- Scope: refined crop visible text only; not a full contents-region replacement.",
        "",
        "## Selected Evidence",
        "",
        "| Region admission | Selected config | Normalized exact | Token recall | Overlay QC | Order QC |",
        "|---|---|---:|---:|---|---|",
    ]
    for item in input_results:
        lines.append(
            f"| `{item['region_admission_id']}` | `{item['selected_config']}` | `{str(item['normalized_exact']).lower()}` | `{item['token_recall']}` | `{item['overlay_qc']['status']}` | `{item['order_qc']['status']}` |"
        )
    lines.extend(
        [
            "",
            "## Output Hashes",
            "",
            "| Output | SHA-256 |",
            "|---|---|",
        ]
    )
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "source_reconstruction_refined_ocr_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.extend(
        [
            "",
            "## Limits Preserved",
            "",
            "- No PDF opening, parsing, rendering, rehashing, recounting, or inspection.",
            "- OCR executed only for `SRA-G1-VIRAL-001-R003` refined crop from `SRCO-G1-VIRAL-001`.",
            "- Raw OCR outputs are new SRFO evidence files; predecessor raw outputs were not modified.",
            "- No OCR text is promoted to accepted source text.",
            "- Human review remains blocked pending package rebuild plus overlay/visual-QC review.",
            "",
        ]
    )
    (OUT_ROOT / "source_reconstruction_refined_ocr_manifest.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    check_authorization()
    build()
