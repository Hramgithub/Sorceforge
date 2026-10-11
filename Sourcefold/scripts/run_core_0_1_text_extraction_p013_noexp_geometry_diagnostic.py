from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image

import run_core_0_1_text_extraction_full_page_geometry_probe_p018_p017 as fg
import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
TESSERACT = overview.TESSERACT
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_noexp_geometry_diagnostic_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEP013GNO-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-NOEXP-GEOMETRY-DIAGNOSTIC-001"
HUMAN_DECISION = "Работай по плану"
PAGE = "013"
PARENT_COMMIT = "e8af6677"
PSM = 4
OCR_PROFILE = "eng_oem1_psm4"
DIAGNOSTIC_SEQUENCE_SIMILARITY = 0.997
DIAGNOSTIC_TOKEN_RECALL = 0.993939
BASELINE_SIMILARITY = 0.25788
BASELINE_TOKEN_RECALL = 0.993939

P013_IMAGE = TRIAL_ROOT / overview.PAGE_DIRS[PAGE] / "review_assets" / "page_013.png"
P013_REFERENCE = TRIAL_ROOT / overview.PAGE_DIRS[PAGE] / "review_assets" / "page_013_text_map.md"
P013_PREVIOUS_REPORT = (
    TRIAL_ROOT
    / "core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001"
    / "p013_seam_dedupe_diagnostic_report.json"
)

EXPECTED_INPUT_HASHES = {
    "p013_full_page_png": (
        P013_IMAGE,
        "DC9BF562A4B3B7E43B38F29F484B64B13958330F449672D6A695B36E0D8F0935",
    ),
    "p013_reference_text_map": (
        P013_REFERENCE,
        "7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67",
    ),
    "p013_seam_dedupe_report": (
        P013_PREVIOUS_REPORT,
        "C99424139DBEBDC2F90025CC97CEB912B6E4D439820F3A68AE1281247C09E1E7",
    ),
}

ORIGINAL_BOXES_XYWH = {
    "P013-B001": [160, 205, 1100, 440],
    "P013-B002": [210, 625, 1060, 340],
    "P013-B003": [210, 960, 1060, 140],
    "P013-B004": [1290, 205, 1120, 700],
    "P013-B005": [1335, 905, 1060, 190],
}

ROLES = {
    "P013-B001": "mythos_investigators_continuation",
    "P013-B002": "documentary_film_crew",
    "P013-B003": "tourists_left_start",
    "P013-B004": "tourists_right_continuation",
    "P013-B005": "pesky_teenagers",
}

ASSEMBLIES = [
    {
        "id": "p013_geo_noexp_5box_triage_order",
        "description": "No-expansion non-overlap OCR assembled in sealed triage physical block order.",
        "units": [["P013-B001"], ["P013-B002"], ["P013-B003"], ["P013-B004"], ["P013-B005"]],
    },
    {
        "id": "p013_geo_noexp_4unit_triage_logical_order",
        "description": "No-expansion non-overlap OCR assembled by sealed triage logical roles: B003+B004 forms the Tourists unit.",
        "units": [["P013-B001"], ["P013-B002"], ["P013-B003", "P013-B004"], ["P013-B005"]],
    },
    {
        "id": "p013_geo_noexp_4unit_column_order_control",
        "description": "Fixed reading-order control using the same OCR crops with the Tourists unit ordered B004+B003.",
        "units": [["P013-B001"], ["P013-B002"], ["P013-B004", "P013-B003"], ["P013-B005"]],
    },
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run P013 no-expansion geometry OCR diagnostic.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 no-expansion geometry diagnostic is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 no-expansion geometry diagnostic requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 no-expansion geometry diagnostic requires the exact bounded human decision")


def verify_expected_inputs() -> dict[str, dict[str, str]]:
    verified = {}
    for key, (path, expected) in EXPECTED_INPUT_HASHES.items():
        if not path.exists():
            raise SystemExit(f"{key} missing: {path}")
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    if commit.returncode != 0 or commit.stdout.strip() != PARENT_COMMIT:
        raise SystemExit(f"expected HEAD at parent commit {PARENT_COMMIT}")
    return verified


def verify_inputs() -> dict[str, Any]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")
    return {
        "authorization_ledger": {
            "path": LEDGER.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(LEDGER),
        },
        "pinned_inputs": verify_expected_inputs(),
        "parent_commit": PARENT_COMMIT,
    }


def xywh_to_half_open(box: list[int]) -> list[int]:
    x, y, width, height = box
    if x < 0 or y < 0 or width <= 0 or height <= 0:
        raise SystemExit(f"invalid xywh box: {box}")
    return [x, y, x + width, y + height]


def boxes_overlap(a: list[int], b: list[int]) -> bool:
    return max(a[0], b[0]) < min(a[2], b[2]) and max(a[1], b[1]) < min(a[3], b[3])


def clipped_boxes() -> dict[str, dict[str, Any]]:
    boxes = {block: xywh_to_half_open(box) for block, box in ORIGINAL_BOXES_XYWH.items()}
    adjustments = []
    for previous, current in [("P013-B001", "P013-B002"), ("P013-B002", "P013-B003"), ("P013-B004", "P013-B005")]:
        before_previous = list(boxes[previous])
        before_current = list(boxes[current])
        if boxes_overlap(boxes[previous], boxes[current]):
            boxes[previous][3] = min(boxes[previous][3], boxes[current][1])
            adjustments.append(
                {
                    "previous_block_yielded": previous,
                    "current_block": current,
                    "rule": "half_open_previous_bottom_clipped_to_current_top",
                    "previous_before": before_previous,
                    "current_before": before_current,
                    "previous_after": list(boxes[previous]),
                    "current_after": list(boxes[current]),
                }
            )
        else:
            adjustments.append(
                {
                    "previous_block_yielded": None,
                    "block_pair": [previous, current],
                    "rule": "half_open_no_overlap_no_clip",
                    "previous_before": before_previous,
                    "current_before": before_current,
                }
            )
    for left, left_box in boxes.items():
        for right, right_box in boxes.items():
            if left >= right:
                continue
            if boxes_overlap(left_box, right_box):
                raise SystemExit(f"post-clipping boxes overlap: {left} {right}")
    return {
        block: {
            "original_xywh": ORIGINAL_BOXES_XYWH[block],
            "original_half_open": xywh_to_half_open(ORIGINAL_BOXES_XYWH[block]),
            "clipped_half_open": boxes[block],
            "role": ROLES[block],
        }
        for block in ORIGINAL_BOXES_XYWH
    } | {"_adjustments": adjustments}


def run_tesseract(prepared: Path, base: Path) -> tuple[str, dict[str, str]]:
    command = [
        str(TESSERACT),
        str(prepared),
        str(base),
        "-l",
        "eng",
        "--oem",
        "1",
        "--psm",
        str(PSM),
        "txt",
        "tsv",
    ]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    stderr_path = base.with_suffix(".stderr.txt")
    stdout_path = base.with_suffix(".stdout.txt")
    write_text(stderr_path, completed.stderr)
    write_text(stdout_path, completed.stdout)
    text_path = base.with_suffix(".txt")
    tsv_path = base.with_suffix(".tsv")
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


def ocr_regions(box_records: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    source = Image.open(P013_IMAGE).convert("RGB")
    results = {}
    for index, block in enumerate(ORIGINAL_BOXES_XYWH, start=1):
        box = box_records[block]["clipped_half_open"]
        if box[2] > source.width or box[3] > source.height:
            raise SystemExit(f"{block} clipped box out of page bounds: {box}")
        prepared = OUT_ROOT / "prepared_regions" / "p013_geo_noexp_nonoverlap_psm4" / f"{index:02d}_{block.lower()}.png"
        base = OUT_ROOT / "raw_ocr" / "p013_geo_noexp_nonoverlap_psm4" / f"{index:02d}_{block.lower()}"
        prepared.parent.mkdir(parents=True, exist_ok=True)
        base.parent.mkdir(parents=True, exist_ok=True)
        source.crop(tuple(box)).convert("RGB").save(prepared)
        text, ocr_result = run_tesseract(prepared, base)
        results[block] = {
            "block": block,
            "role": ROLES[block],
            "text": text.strip(),
            "box": box_records[block],
            "ocr_profile": OCR_PROFILE,
            "ocr_result": ocr_result,
        }
    return results


def render_candidate(assembly: dict[str, Any], ocr: dict[str, dict[str, Any]]) -> str:
    chunks = []
    for index, unit in enumerate(assembly["units"], start=1):
        title = "+".join(unit)
        body = "\n".join(ocr[block]["text"] for block in unit).strip()
        chunks.append(f"## P013-UNIT-{index:03d} {title}\n\n{body}")
    return "\n\n".join(chunks).strip() + "\n"


def score_candidate(candidate_text: str) -> tuple[str, Path, dict[str, Any]]:
    reference_text = overview.extract_reference_text(P013_REFERENCE)
    return "reference_text_map_not_ocr_verified", P013_REFERENCE, fg.metrics(candidate_text, reference_text)


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    box_records = clipped_boxes()
    ocr = ocr_regions(box_records)
    lineage = {
        "lane_id": LANE_ID,
        "parent_commit": PARENT_COMMIT,
        "page": "P013",
        "coordinate_semantics": "half_open_xyxy",
        "original_box_encoding": "triage_xywh",
        "clipping_rule": "for declared vertical conflicts, previous/top block bottom is clipped to current block top; no padding or expansion",
        "box_records": box_records,
        "ocr_engine_profile": OCR_PROFILE,
        "no_expansion": True,
        "padding_px": 0,
        "dedupe_enabled": False,
        "candidate_assemblies": ASSEMBLIES,
    }
    write_json(OUT_ROOT / "lineage.json", lineage)
    candidates = []
    for assembly in ASSEMBLIES:
        candidate_text = render_candidate(assembly, ocr)
        candidate_path = OUT_ROOT / "candidate_texts" / assembly["id"] / "page_013_candidate.md"
        write_text(candidate_path, candidate_text)
        candidate_sha = sha256_file(candidate_path)
        normalized = overview.normalize_candidate_for_metrics(candidate_text)
        normalized_path = OUT_ROOT / "normalized_candidate_texts" / assembly["id"] / "page_013_candidate_normalized.txt"
        write_text(normalized_path, normalized + "\n")
        normalized_sha = sha256_file(normalized_path)
        label, reference_path, page_metrics = score_candidate(candidate_text)
        diagnostic_threshold_met = (
            page_metrics["sequence_similarity_ratio"] >= DIAGNOSTIC_SEQUENCE_SIMILARITY
            and page_metrics["token_recall"] >= DIAGNOSTIC_TOKEN_RECALL
        )
        candidates.append(
            {
                "page": PAGE,
                "candidate_id": assembly["id"],
                "description": assembly["description"],
                "units": assembly["units"],
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": candidate_sha,
                "normalized_candidate_path": normalized_path.relative_to(ROOT).as_posix(),
                "normalized_candidate_sha256": normalized_sha,
                "candidate_hash_sealed_before_reference_scoring": True,
                "reference_label": label,
                "reference_path": reference_path.relative_to(ROOT).as_posix(),
                "reference_sha256": sha256_file(reference_path),
                "reference_loaded_after_candidate_hashing": True,
                "metrics": page_metrics,
                "baseline_metrics": {
                    "sequence_similarity_ratio": BASELINE_SIMILARITY,
                    "token_recall": BASELINE_TOKEN_RECALL,
                },
                "metric_deltas_from_p013_dedupe_baseline": {
                    "sequence_similarity_delta": round(page_metrics["sequence_similarity_ratio"] - BASELINE_SIMILARITY, 6),
                    "token_recall_delta": round(page_metrics["token_recall"] - BASELINE_TOKEN_RECALL, 6),
                },
                "diagnostic_improvement_over_dedupe_baseline": page_metrics["sequence_similarity_ratio"] > BASELINE_SIMILARITY,
                "diagnostic_threshold_met": diagnostic_threshold_met,
                "method_registry_candidate": diagnostic_threshold_met,
            }
        )
    candidates.sort(key=lambda item: (item["metrics"]["sequence_similarity_ratio"], item["metrics"]["token_recall"]), reverse=True)
    write_json(OUT_ROOT / "rankings" / "page_013_candidate_rankings.json", candidates)
    best = candidates[0]
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_p013_noexp_geometry_diagnostic_completed",
        "page": PAGE,
        "verified_inputs": verified_inputs,
        "lineage_path": (OUT_ROOT / "lineage.json").relative_to(ROOT).as_posix(),
        "lineage_sha256": sha256_file(OUT_ROOT / "lineage.json"),
        "ocr_results": {block: {key: value for key, value in data.items() if key != "text"} for block, data in ocr.items()},
        "candidate_generation_inputs": ["p013_full_page_png", "declared_triage_xywh_boxes"],
        "candidate_generation_previous_ocr_text_used": False,
        "no_expansion": True,
        "padding_px": 0,
        "dedupe_enabled": False,
        "ocr_engine_profile": OCR_PROFILE,
        "results": candidates,
        "best_candidate": best,
        "diagnostic_thresholds": {
            "sequence_similarity": DIAGNOSTIC_SEQUENCE_SIMILARITY,
            "token_recall": DIAGNOSTIC_TOKEN_RECALL,
            "registry_candidate_requires_threshold": True,
            "acceptance_effect": "none",
        },
        "ocr_execution_performed": True,
        "reference_guided_repair_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "runtime_implementation_created": False,
        "production_assembly_created": False,
        "page_021_plus_included": False,
        "push_performed": False,
    }
    write_json(OUT_ROOT / "p013_noexp_geometry_diagnostic_report.json", report)
    summary_lines = [
        "# P013 No-Expansion Geometry Diagnostic - C01TEP013GNO-G1-VIRAL-001",
        "",
        "Status: `candidate_only_p013_noexp_geometry_diagnostic_completed`",
        "",
        "Fresh OCR was executed only over P013 full-page-derived non-overlap crops with no expansion and no padding.",
        "",
        "| Candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta | Token recall delta |",
        "|---|---:|---:|---|---:|---:|",
    ]
    for result in candidates:
        summary_lines.append(
            f"| `{result['candidate_id']}` | `{result['metrics']['sequence_similarity_ratio']}` | "
            f"`{result['metrics']['token_recall']}` | `{result['diagnostic_threshold_met']}` | "
            f"`{result['metric_deltas_from_p013_dedupe_baseline']['sequence_similarity_delta']}` | "
            f"`{result['metric_deltas_from_p013_dedupe_baseline']['token_recall_delta']}` |"
        )
    summary_lines.extend(
        [
            "",
            "Boundary: P013-only diagnostic OCR evidence; no reference-guided repair, no accepted/semantic/page-status/source mutation, no method selector, no production output, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "p013_noexp_geometry_diagnostic_summary.md", "\n".join(summary_lines))
    manifest_lines = [
        "# P013 No-Expansion Geometry Diagnostic Manifest - C01TEP013GNO-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p013_noexp_geometry_diagnostic_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "p013_noexp_geometry_diagnostic_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
