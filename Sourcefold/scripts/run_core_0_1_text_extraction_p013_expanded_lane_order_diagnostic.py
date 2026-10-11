from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import run_core_0_1_text_extraction_full_page_geometry_probe_p018_p017 as fg
import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
SOURCE_ROOT = (
    TRIAL_ROOT / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002"
)
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEP013ELO-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-EXPANDED-LANE-ORDER-DIAGNOSTIC-001"
HUMAN_DECISION = "пробуй"
PAGE = "013"
PARENT_COMMIT = "460cb459"
SOURCE_CANDIDATE_ID = "full_page_triage_boxes_expanded_psm4"
PREPARED_BORDER_PX = 24
LANE_SPLIT_X = 1200
LINE_BAND_TOLERANCE_PX = 18
DIAGNOSTIC_SEQUENCE_SIMILARITY = 0.997
DIAGNOSTIC_TOKEN_RECALL = 0.993939
BASELINE_SIMILARITY = 0.25788
BASELINE_TOKEN_RECALL = 0.993939

SOURCE_RANKING = SOURCE_ROOT / "rankings" / "page_013_candidate_rankings.json"
SOURCE_CANDIDATE = SOURCE_ROOT / "candidate_texts" / SOURCE_CANDIDATE_ID / "page_013_candidate.md"
P013_REFERENCE = TRIAL_ROOT / overview.PAGE_DIRS[PAGE] / "review_assets" / "page_013_text_map.md"

EXPECTED_INPUT_HASHES = {
    "source_ranking": (SOURCE_RANKING, "45A41E61A34C892328ABB69D988DD6947D33F32E9BFCE56771B6FCD36CEC4454"),
    "source_candidate": (SOURCE_CANDIDATE, "6AA2ADCDB1CDE71741F057300DC8888543F315BC14CD65F02602D71145CA5412"),
    "source_reference": (P013_REFERENCE, "7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67"),
    "p013_b001_txt": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "01_p013_b001_tes.txt",
        "5C2530221C1F90DF16A7CD1990D261A1161F50D7D9EB75D8833B002534CAAAFB",
    ),
    "p013_b001_tsv": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "01_p013_b001_tes.tsv",
        "998DCF0B2A04F82E807E2B2F36E5245BB2C43DD447C61629D73554398B4481F6",
    ),
    "p013_b001_png": (
        SOURCE_ROOT / "prepared_regions" / SOURCE_CANDIDATE_ID / "p013" / "01_p013_b001_tes.png",
        "750CE047D59286FDD5EC4B71483E4616D6DC8F0561175A28F5450880D864E2AF",
    ),
    "p013_b002_txt": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "02_p013_b002_tes.txt",
        "8F35311433B2EB2C9AF8D69C5D32D307D81B3146AFFCB806A08AA649D895124B",
    ),
    "p013_b002_tsv": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "02_p013_b002_tes.tsv",
        "E72AE092C354300245B40B66B9F7056400C11CEB09FC4B6AFB71E8401B08D722",
    ),
    "p013_b002_png": (
        SOURCE_ROOT / "prepared_regions" / SOURCE_CANDIDATE_ID / "p013" / "02_p013_b002_tes.png",
        "8BD0EA3379029F3272CF77B895F9A167A453CFC7312746CCF560D918232EC1CE",
    ),
    "p013_b003_txt": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "03_p013_b003_tes.txt",
        "C88C2CCB007EDCC5DE3BB43A0CC40E29319B838C1C68746FA3EEA0F5CA0E223C",
    ),
    "p013_b003_tsv": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "03_p013_b003_tes.tsv",
        "065D76C4F7E6588E5741227488EA2A67441B71FA0382D54E71BC3710A8123755",
    ),
    "p013_b003_png": (
        SOURCE_ROOT / "prepared_regions" / SOURCE_CANDIDATE_ID / "p013" / "03_p013_b003_tes.png",
        "CF6416EDD4A4D7364CD17809CAFA86AACD0958F0D0AE560C7056A9704783A8E6",
    ),
    "p013_b004_txt": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "04_p013_b004_tes.txt",
        "60782A9328A0C1B7F97AD2F8B7E76BA67CF6C8EE0EB26507093896DF614E0959",
    ),
    "p013_b004_tsv": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "04_p013_b004_tes.tsv",
        "285C3870200EFA14B9B26A2A3BD876BA326450D9618C93FE424F0EC3C8F80F0D",
    ),
    "p013_b004_png": (
        SOURCE_ROOT / "prepared_regions" / SOURCE_CANDIDATE_ID / "p013" / "04_p013_b004_tes.png",
        "B17F4AA8520C710D3F484FA099E401F9951955CA5107BAEAAC40CA308ECDDAC5",
    ),
    "p013_b005_txt": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "05_p013_b005_tes.txt",
        "C910438BCE5C61AC30CE2EEC5683E3700CD82BB0938308A31F7C1A8471B4A3B4",
    ),
    "p013_b005_tsv": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "05_p013_b005_tes.tsv",
        "FDD4173327CCBDE6BACADCF0FA5122BD38FCC40979E506574D346C7705D5617B",
    ),
    "p013_b005_png": (
        SOURCE_ROOT / "prepared_regions" / SOURCE_CANDIDATE_ID / "p013" / "05_p013_b005_tes.png",
        "E5964281A60E4B73328403537E2F8EEC8A49CC98FF06B0E811CC9EBD5676EBE7",
    ),
}


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
    parser = argparse.ArgumentParser(description="Run P013 expanded-geometry lane-order diagnostic.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 expanded lane-order diagnostic is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 expanded lane-order diagnostic requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 expanded lane-order diagnostic requires the exact bounded human decision")


def verify_expected_inputs() -> dict[str, dict[str, str]]:
    verified = {}
    for key, (path, expected) in EXPECTED_INPUT_HASHES.items():
        if not path.exists():
            raise SystemExit(f"{key} missing: {path}")
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    return verified


def verify_inputs() -> dict[str, Any]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    return {
        "authorization_ledger": {"path": LEDGER.relative_to(ROOT).as_posix(), "sha256": sha256_file(LEDGER)},
        "pinned_inputs": verify_expected_inputs(),
        "parent_commit": PARENT_COMMIT,
    }


def source_result() -> dict[str, Any]:
    data = json.loads(SOURCE_RANKING.read_text(encoding="utf-8"))
    for candidate in data:
        if candidate["candidate_id"] == SOURCE_CANDIDATE_ID:
            return candidate
    raise SystemExit(f"missing source candidate {SOURCE_CANDIDATE_ID}")


def norm_line(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def line_records() -> list[dict[str, Any]]:
    records = []
    for region_index, region in enumerate(source_result()["region_results"], start=1):
        page_box = region["page_space_box"]
        tsv_path = ROOT / region["ocr_result"]["raw_ocr_tsv_path"]
        with tsv_path.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
        for row in rows:
            if row.get("level") == "5" and row.get("text", "").strip():
                key = (row["block_num"], row["par_num"], row["line_num"])
                grouped.setdefault(key, []).append(row)
        for line_index, (key, words) in enumerate(sorted(grouped.items()), start=1):
            left = min(int(word["left"]) for word in words)
            top = min(int(word["top"]) for word in words)
            right = max(int(word["left"]) + int(word["width"]) for word in words)
            bottom = max(int(word["top"]) + int(word["height"]) for word in words)
            text = " ".join(word["text"] for word in words).strip()
            page_left = page_box[0] + left - PREPARED_BORDER_PX
            page_top = page_box[1] + top - PREPARED_BORDER_PX
            page_right = page_box[0] + right - PREPARED_BORDER_PX
            page_bottom = page_box[1] + bottom - PREPARED_BORDER_PX
            lane_id = "left_lane" if ((page_left + page_right) / 2) < LANE_SPLIT_X else "right_lane"
            records.append(
                {
                    "source_region": region["region_id"],
                    "region_index": region_index,
                    "line_index": line_index,
                    "tsv_group": list(key),
                    "text": text,
                    "normalized_text": norm_line(text),
                    "tsv_box": [left, top, right, bottom],
                    "page_space_box": [page_left, page_top, page_right, page_bottom],
                    "page_center": [(page_left + page_right) / 2, (page_top + page_bottom) / 2],
                    "lane_id": lane_id,
                }
            )
    return records


def assign_bands(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered = sorted(records, key=lambda item: (item["page_center"][1], item["page_center"][0]))
    band_centers: list[float] = []
    for record in ordered:
        y = record["page_center"][1]
        for band_index, center in enumerate(band_centers):
            if abs(y - center) <= LINE_BAND_TOLERANCE_PX:
                record["band_id"] = f"band_{band_index + 1:03d}"
                band_centers[band_index] = (center + y) / 2
                break
        else:
            band_centers.append(y)
            record["band_id"] = f"band_{len(band_centers):03d}"
    return ordered


def ordered_records(records: list[dict[str, Any]], mode: str) -> list[dict[str, Any]]:
    if mode == "source_region_order":
        ordered = sorted(records, key=lambda item: (item["region_index"], item["line_index"]))
    elif mode == "lane_then_y":
        ordered = sorted(records, key=lambda item: (0 if item["lane_id"] == "left_lane" else 1, item["page_center"][1], item["page_center"][0]))
    elif mode == "band_then_lane":
        ordered = sorted(assign_bands([dict(item) for item in records]), key=lambda item: (item["band_id"], 0 if item["lane_id"] == "left_lane" else 1, item["page_center"][0]))
    else:
        raise SystemExit(f"unknown ordering mode: {mode}")
    return [{**item, "final_ordinal": index} for index, item in enumerate(ordered, start=1)]


def iou(a: list[int], b: list[int]) -> float:
    left = max(a[0], b[0])
    top = max(a[1], b[1])
    right = min(a[2], b[2])
    bottom = min(a[3], b[3])
    if left >= right or top >= bottom:
        return 0.0
    inter = (right - left) * (bottom - top)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)


def collapse_exact_duplicates(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    kept: list[dict[str, Any]] = []
    collapse_report: list[dict[str, Any]] = []
    for record in records:
        duplicate_of = None
        for existing in kept:
            same_text = record["normalized_text"] and record["normalized_text"] == existing["normalized_text"]
            same_lane = record["lane_id"] == existing["lane_id"]
            overlap = iou(record["page_space_box"], existing["page_space_box"])
            if same_text and same_lane and overlap >= 0.85:
                duplicate_of = {**existing, "overlap_iou": round(overlap, 6)}
                break
        if duplicate_of is None:
            kept.append(record)
        else:
            collapse_report.append(
                {
                    "removed_final_ordinal": record["final_ordinal"],
                    "kept_final_ordinal": duplicate_of["final_ordinal"],
                    "text": record["text"],
                    "normalized_text": record["normalized_text"],
                    "removed_page_space_box": record["page_space_box"],
                    "kept_page_space_box": duplicate_of["page_space_box"],
                    "overlap_iou": duplicate_of["overlap_iou"],
                    "match_basis": "exact_normalized_line_text_same_lane_iou_ge_0_85",
                }
            )
    return kept, collapse_report


VARIANTS = [
    {"id": "p013_expanded_lane_order_source_region_baseline", "mode": "source_region_order", "collapse": False},
    {"id": "p013_expanded_lane_order_lane_then_y", "mode": "lane_then_y", "collapse": False},
    {"id": "p013_expanded_lane_order_band_then_lane", "mode": "band_then_lane", "collapse": False},
    {"id": "p013_expanded_lane_order_lane_then_y_exact_collapse", "mode": "lane_then_y", "collapse": True},
]


def score_candidate(candidate_text: str) -> tuple[str, Path, dict[str, Any]]:
    reference_text = overview.extract_reference_text(P013_REFERENCE)
    return "reference_text_map_not_ocr_verified", P013_REFERENCE, fg.metrics(candidate_text, reference_text)


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    records = line_records()
    write_json(
        OUT_ROOT / "line_records_raw.json",
        {
            "coordinate_transform": "page_x = region_page_space_left + tsv_left - prepared_border_px; page_y = region_page_space_top + tsv_top - prepared_border_px",
            "prepared_border_px": PREPARED_BORDER_PX,
            "lane_split_x": LANE_SPLIT_X,
            "line_band_tolerance_px": LINE_BAND_TOLERANCE_PX,
            "records": records,
        },
    )
    results = []
    for variant in VARIANTS:
        ordered = ordered_records(records, variant["mode"])
        collapse_report: list[dict[str, Any]] = []
        if variant["collapse"]:
            ordered, collapse_report = collapse_exact_duplicates(ordered)
        trace_path = OUT_ROOT / "line_order_traces" / variant["id"] / "page_013_line_order_trace.json"
        collapse_path = OUT_ROOT / "duplicate_collapse_reports" / variant["id"] / "page_013_duplicate_collapse_report.json"
        candidate_text = "\n".join(item["text"] for item in ordered).strip() + "\n"
        candidate_path = OUT_ROOT / "candidate_texts" / variant["id"] / "page_013_candidate.md"
        write_json(trace_path, ordered)
        write_json(collapse_path, collapse_report)
        write_text(candidate_path, candidate_text)
        candidate_sha = sha256_file(candidate_path)
        normalized_path = OUT_ROOT / "normalized_candidate_texts" / variant["id"] / "page_013_candidate_normalized.txt"
        write_text(normalized_path, overview.normalize_candidate_for_metrics(candidate_text) + "\n")
        normalized_sha = sha256_file(normalized_path)
        label, reference_path, page_metrics = score_candidate(candidate_text)
        diagnostic_threshold_met = (
            page_metrics["sequence_similarity_ratio"] >= DIAGNOSTIC_SEQUENCE_SIMILARITY
            and page_metrics["token_recall"] >= DIAGNOSTIC_TOKEN_RECALL
        )
        results.append(
            {
                "page": PAGE,
                "candidate_id": variant["id"],
                "ordering_mode": variant["mode"],
                "duplicate_collapse_enabled": variant["collapse"],
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": candidate_sha,
                "normalized_candidate_path": normalized_path.relative_to(ROOT).as_posix(),
                "normalized_candidate_sha256": normalized_sha,
                "line_order_trace_path": trace_path.relative_to(ROOT).as_posix(),
                "line_order_trace_sha256": sha256_file(trace_path),
                "duplicate_collapse_report_path": collapse_path.relative_to(ROOT).as_posix(),
                "duplicate_collapse_report_sha256": sha256_file(collapse_path),
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
                "metric_deltas_from_p013_best_failed_baseline": {
                    "sequence_similarity_delta": round(page_metrics["sequence_similarity_ratio"] - BASELINE_SIMILARITY, 6),
                    "token_recall_delta": round(page_metrics["token_recall"] - BASELINE_TOKEN_RECALL, 6),
                },
                "diagnostic_improvement_over_best_failed_baseline": (
                    page_metrics["sequence_similarity_ratio"] > BASELINE_SIMILARITY
                    and page_metrics["token_recall"] >= DIAGNOSTIC_TOKEN_RECALL
                ),
                "diagnostic_threshold_met": diagnostic_threshold_met,
                "method_registry_candidate": diagnostic_threshold_met,
            }
        )
    results.sort(key=lambda item: (item["metrics"]["sequence_similarity_ratio"], item["metrics"]["token_recall"]), reverse=True)
    write_json(OUT_ROOT / "rankings" / "page_013_candidate_rankings.json", results)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_p013_expanded_lane_order_diagnostic_completed",
        "page": PAGE,
        "verified_inputs": verified_inputs,
        "source_candidate_id": SOURCE_CANDIDATE_ID,
        "candidate_generation_inputs": ["cached_p013_expanded_psm4_tsv_geometry"],
        "candidate_generation_previous_ocr_text_used": False,
        "ocr_execution_performed": False,
        "reference_guided_repair_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "text_token_mutation_performed": False,
        "diagnostic_thresholds": {
            "sequence_similarity": DIAGNOSTIC_SEQUENCE_SIMILARITY,
            "token_recall": DIAGNOSTIC_TOKEN_RECALL,
            "method_registry_candidate_requires_threshold": True,
            "acceptance_effect": "none",
        },
        "variants": VARIANTS,
        "results": results,
        "best_candidate": results[0],
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "runtime_implementation_created": False,
        "production_assembly_created": False,
        "page_021_plus_included": False,
        "push_performed": False,
    }
    write_json(OUT_ROOT / "p013_expanded_lane_order_diagnostic_report.json", report)
    lines = [
        "# P013 Expanded Lane-Order Diagnostic - C01TEP013ELO-G1-VIRAL-001",
        "",
        "Status: `candidate_only_p013_expanded_lane_order_diagnostic_completed`",
        "",
        "No OCR was executed. Candidates are assembled from cached expanded PSM4 TSV line records mapped into page space.",
        "",
        "| Candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta | Token recall delta |",
        "|---|---:|---:|---|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| `{result['candidate_id']}` | `{result['metrics']['sequence_similarity_ratio']}` | "
            f"`{result['metrics']['token_recall']}` | `{result['diagnostic_threshold_met']}` | "
            f"`{result['metric_deltas_from_p013_best_failed_baseline']['sequence_similarity_delta']}` | "
            f"`{result['metric_deltas_from_p013_best_failed_baseline']['token_recall_delta']}` |"
        )
    lines.extend(
        [
            "",
            "Boundary: P013-only diagnostic assembly evidence; no OCR execution, no reference-guided repair, no accepted/semantic/page-status/source mutation, no method selector, no production output, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "p013_expanded_lane_order_diagnostic_summary.md", "\n".join(lines))
    manifest_lines = [
        "# P013 Expanded Lane-Order Diagnostic Manifest - C01TEP013ELO-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p013_expanded_lane_order_diagnostic_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "p013_expanded_lane_order_diagnostic_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
