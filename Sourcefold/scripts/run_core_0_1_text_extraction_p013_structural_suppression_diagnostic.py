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
import run_core_0_1_text_extraction_p013_expanded_lane_order_diagnostic as elo


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
ELO_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_expanded_lane_order_diagnostic_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEP013SSP-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-SUPPRESSION-DIAGNOSTIC-001"
HUMAN_DECISION = "пробуй"
PAGE = "013"
PARENT_COMMIT = "796c7044"
DIAGNOSTIC_SEQUENCE_SIMILARITY = 0.997
DIAGNOSTIC_TOKEN_RECALL = 0.993939
ELO_BEST_SIMILARITY = 0.433325
ELO_BEST_TOKEN_RECALL = 0.993939

ELO_REPORT = ELO_ROOT / "p013_expanded_lane_order_diagnostic_report.json"
ELO_MANIFEST = ELO_ROOT / "p013_expanded_lane_order_diagnostic_manifest.md"
ELO_LINE_RECORDS_RAW = ELO_ROOT / "line_records_raw.json"
ELO_BEST_TRACE = (
    ELO_ROOT
    / "line_order_traces"
    / "p013_expanded_lane_order_lane_then_y_exact_collapse"
    / "page_013_line_order_trace.json"
)
ELO_BEST_COLLAPSE_REPORT = (
    ELO_ROOT
    / "duplicate_collapse_reports"
    / "p013_expanded_lane_order_lane_then_y_exact_collapse"
    / "page_013_duplicate_collapse_report.json"
)
SOURCE_RANKING = elo.SOURCE_RANKING
P013_REFERENCE = elo.P013_REFERENCE
RAW_TSV_ROOT = elo.SOURCE_ROOT / "raw_ocr" / elo.SOURCE_CANDIDATE_ID / "p013"

EXPECTED_INPUT_HASHES = {
    "elo_report": (ELO_REPORT, "C8EFBAF8F3FFB58E0FF8CCFA41869861B6AA6F92A0E8E6DAC6F111EDC91BD3FB"),
    "elo_manifest": (ELO_MANIFEST, "74C1985E1B8DB19375E5652E2674918F9C44202F1173EF1074C5A16D757F5C87"),
    "elo_line_records_raw": (ELO_LINE_RECORDS_RAW, "1DEB381148397F9014C22C3263858C360FF9BAA8C64199572AD024CB578A2863"),
    "elo_best_trace": (ELO_BEST_TRACE, "CE27FBE19F08D9432D3D8C8C8F43FBC3E749DA05A54B995523B4BAFA0C860E94"),
    "elo_best_collapse_report": (
        ELO_BEST_COLLAPSE_REPORT,
        "DCCBF482AAE8DAC5EC7F569BAE84422ED5487EE2676442E77120345B82E8EB73",
    ),
    "source_ranking": (SOURCE_RANKING, "45A41E61A34C892328ABB69D988DD6947D33F32E9BFCE56771B6FCD36CEC4454"),
    "p013_b001_tsv": (RAW_TSV_ROOT / "01_p013_b001_tes.tsv", "998DCF0B2A04F82E807E2B2F36E5245BB2C43DD447C61629D73554398B4481F6"),
    "p013_b002_tsv": (RAW_TSV_ROOT / "02_p013_b002_tes.tsv", "E72AE092C354300245B40B66B9F7056400C11CEB09FC4B6AFB71E8401B08D722"),
    "p013_b003_tsv": (RAW_TSV_ROOT / "03_p013_b003_tes.tsv", "065D76C4F7E6588E5741227488EA2A67441B71FA0382D54E71BC3710A8123755"),
    "p013_b004_tsv": (RAW_TSV_ROOT / "04_p013_b004_tes.tsv", "285C3870200EFA14B9B26A2A3BD876BA326450D9618C93FE424F0EC3C8F80F0D"),
    "p013_b005_tsv": (RAW_TSV_ROOT / "05_p013_b005_tes.tsv", "FDD4173327CCBDE6BACADCF0FA5122BD38FCC40979E506574D346C7705D5617B"),
}
EXPECTED_REFERENCE_HASH = "7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67"

NEAR_OVERLAP_MIN_AREA_RATIO = 0.72
NEAR_OVERLAP_MAX_CENTER_Y_GAP_PX = 8
NEAR_OVERLAP_MIN_TOKEN_DICE = 0.84
CONFIDENCE_TIE_MARGIN = 1.0
LOW_CONF_NOISE_MAX_MEAN_CONF = 50.0
LOW_CONF_NOISE_MAX_HEIGHT_PX = 14
LOW_CONF_NOISE_NEIGHBOR_Y_GAP_PX = 36
PUNCTUATION_FRAGMENT_RE = re.compile(r"^[^\w]*[.,;:!?'\u2018\u2019\u201c\u201d\"-]+[^\w]*$")


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
    parser = argparse.ArgumentParser(description="Run P013 structural-suppression diagnostic.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 structural-suppression diagnostic is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 structural-suppression diagnostic requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 structural-suppression diagnostic requires the exact bounded human decision")


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


def record_key(record: dict[str, Any]) -> tuple[str, str, str, str]:
    block, par, line = record["tsv_group"]
    return (record["source_region"], block, par, line)


def tsv_confidence_index() -> dict[tuple[str, str, str, str], dict[str, Any]]:
    index: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for region in elo.source_result()["region_results"]:
        tsv_path = ROOT / region["ocr_result"]["raw_ocr_tsv_path"]
        with tsv_path.open(encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t"))
        grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
        for row in rows:
            if row.get("level") == "5" and row.get("text", "").strip():
                grouped.setdefault((row["block_num"], row["par_num"], row["line_num"]), []).append(row)
        for key, words in grouped.items():
            confs = [float(word["conf"]) for word in words if word.get("conf") not in ("", "-1")]
            index[(region["region_id"], *key)] = {
                "word_count": len(words),
                "mean_confidence": round(sum(confs) / len(confs), 6) if confs else None,
                "min_confidence": round(min(confs), 6) if confs else None,
                "word_confidences": [round(value, 6) for value in confs],
                "word_texts": [word["text"] for word in words],
            }
    return index


def enrich_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    confidence = tsv_confidence_index()
    enriched = []
    for record in records:
        block, par, line = record["tsv_group"]
        tsv_line_key = f"{record['source_region']}:{block}.{par}.{line}"
        key = record_key(record)
        if key not in confidence:
            raise SystemExit(f"missing TSV confidence row for {tsv_line_key}")
        enriched.append(
            {
                **record,
                "record_id": tsv_line_key,
                "tsv_line_key": tsv_line_key,
                "source_order": f"{record['region_index']:02d}.{record['line_index']:03d}",
                "page_bbox_half_open": record["page_space_box"],
                "confidence": confidence[key],
            }
        )
    return enriched


def elo_best_records() -> list[dict[str, Any]]:
    return enrich_records(json.loads(ELO_BEST_TRACE.read_text(encoding="utf-8")))


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def token_dice(a: str, b: str) -> float:
    left = tokens(a)
    right = tokens(b)
    if not left or not right:
        return 0.0
    common = sum(min(left.count(token), right.count(token)) for token in set(left) | set(right))
    return (2 * common) / (len(left) + len(right))


def intersection_area(a: list[int], b: list[int]) -> int:
    left = max(a[0], b[0])
    top = max(a[1], b[1])
    right = min(a[2], b[2])
    bottom = min(a[3], b[3])
    if left >= right or top >= bottom:
        return 0
    return (right - left) * (bottom - top)


def area(box: list[int]) -> int:
    return max(0, box[2] - box[0]) * max(0, box[3] - box[1])


def min_area_overlap_ratio(a: list[int], b: list[int]) -> float:
    smallest = min(area(a), area(b))
    if smallest == 0:
        return 0.0
    return intersection_area(a, b) / smallest


def same_lane_near_overlap_edge(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any] | None:
    if left["lane_id"] != right["lane_id"]:
        return None
    y_gap = abs(left["page_center"][1] - right["page_center"][1])
    if y_gap > NEAR_OVERLAP_MAX_CENTER_Y_GAP_PX:
        return None
    overlap = min_area_overlap_ratio(left["page_bbox_half_open"], right["page_bbox_half_open"])
    if overlap < NEAR_OVERLAP_MIN_AREA_RATIO:
        return None
    similarity = token_dice(left["normalized_text"], right["normalized_text"])
    if similarity < NEAR_OVERLAP_MIN_TOKEN_DICE:
        return None
    return {
        "left_record_id": left["record_id"],
        "right_record_id": right["record_id"],
        "same_lane": True,
        "center_y_gap_px": round(y_gap, 6),
        "min_area_overlap_ratio": round(overlap, 6),
        "token_dice": round(similarity, 6),
    }


def connected_components(records: list[dict[str, Any]]) -> tuple[list[list[dict[str, Any]]], list[dict[str, Any]]]:
    edges = []
    parent = {record["record_id"]: record["record_id"] for record in records}

    def find(item: str) -> str:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(a: str, b: str) -> None:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a

    for index, left in enumerate(records):
        for right in records[index + 1 :]:
            edge = same_lane_near_overlap_edge(left, right)
            if edge:
                edges.append(edge)
                union(left["record_id"], right["record_id"])
    buckets: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        buckets.setdefault(find(record["record_id"]), []).append(record)
    return list(buckets.values()), edges


def suppress_near_overlap_confidence(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    components, edges = connected_components(records)
    edge_pairs = {frozenset((edge["left_record_id"], edge["right_record_id"])) for edge in edges}
    retained: list[dict[str, Any]] = []
    suppressed: list[dict[str, Any]] = []
    component_reports = []
    for component in components:
        ordered = sorted(component, key=lambda item: item["final_ordinal"])
        if len(ordered) == 1:
            retained.extend(ordered)
            continue
        is_clique = all(
            frozenset((left["record_id"], right["record_id"])) in edge_pairs
            for index, left in enumerate(ordered)
            for right in ordered[index + 1 :]
        )
        if not is_clique:
            retained.extend(ordered)
            component_reports.append(
                {
                    "component_record_ids": [item["record_id"] for item in ordered],
                    "decision": "preserved_non_clique_transitive_component",
                    "retained_record_ids": [item["record_id"] for item in ordered],
                    "suppressed_record_ids": [],
                    "tie_margin": CONFIDENCE_TIE_MARGIN,
                }
            )
            continue
        by_conf = sorted(
            ordered,
            key=lambda item: (item["confidence"]["mean_confidence"], -item["final_ordinal"]),
            reverse=True,
        )
        top = by_conf[0]
        second = by_conf[1]
        confidence_delta = top["confidence"]["mean_confidence"] - second["confidence"]["mean_confidence"]
        ambiguous = confidence_delta <= CONFIDENCE_TIE_MARGIN
        if ambiguous:
            retained.extend(ordered)
            decision = "preserved_ambiguous_confidence_tie"
            removed = []
        else:
            retained.append(top)
            removed = [item for item in ordered if item["record_id"] != top["record_id"]]
            suppressed.extend(removed)
            decision = "retained_highest_mean_confidence"
        component_reports.append(
            {
                "component_record_ids": [item["record_id"] for item in ordered],
                "decision": decision,
                "retained_record_ids": [item["record_id"] for item in (ordered if ambiguous else [top])],
                "suppressed_record_ids": [item["record_id"] for item in removed],
                "confidence_delta": round(confidence_delta, 6),
                "tie_margin": CONFIDENCE_TIE_MARGIN,
            }
        )
    retained.sort(key=lambda item: item["final_ordinal"])
    return retained, {
        "rule_id": "near_overlap_component_highest_confidence",
        "parameters": {
            "same_lane_required": True,
            "min_area_overlap_ratio": NEAR_OVERLAP_MIN_AREA_RATIO,
            "max_center_y_gap_px": NEAR_OVERLAP_MAX_CENTER_Y_GAP_PX,
            "min_token_dice": NEAR_OVERLAP_MIN_TOKEN_DICE,
            "confidence_tie_margin": CONFIDENCE_TIE_MARGIN,
            "tie_behavior": "preserve_all_records_in_component",
        },
        "edges": edges,
        "components": component_reports,
        "suppressed_records": [suppression_summary(item, "near_overlap_lower_confidence") for item in suppressed],
    }


def vertical_gap(a: list[int], b: list[int]) -> int:
    if a[3] <= b[1]:
        return b[1] - a[3]
    if b[3] <= a[1]:
        return a[1] - b[3]
    return 0


def horizontal_gap(a: list[int], b: list[int]) -> int:
    if a[2] <= b[0]:
        return b[0] - a[2]
    if b[2] <= a[0]:
        return a[0] - b[2]
    return 0


def is_noise_line(record: dict[str, Any], preserved_records: list[dict[str, Any]]) -> tuple[bool, dict[str, Any]]:
    box = record["page_bbox_half_open"]
    height = box[3] - box[1]
    punctuation_fragment = bool(PUNCTUATION_FRAGMENT_RE.fullmatch(record["text"].strip()))
    neighbor_candidates = []
    for other in preserved_records:
        if other["record_id"] == record["record_id"] or other["lane_id"] != record["lane_id"]:
            continue
        y_gap = vertical_gap(box, other["page_bbox_half_open"])
        x_gap = horizontal_gap(box, other["page_bbox_half_open"])
        if y_gap <= LOW_CONF_NOISE_NEIGHBOR_Y_GAP_PX:
            neighbor_candidates.append(
                {
                    "record_id": other["record_id"],
                    "vertical_edge_gap_px": y_gap,
                    "horizontal_edge_gap_px": x_gap,
                }
            )
    neighbor_candidates.sort(key=lambda item: (item["vertical_edge_gap_px"], item["horizontal_edge_gap_px"], item["record_id"]))
    low_conf_thin_fragment = (
        record["confidence"]["mean_confidence"] <= LOW_CONF_NOISE_MAX_MEAN_CONF
        and height <= LOW_CONF_NOISE_MAX_HEIGHT_PX
        and bool(neighbor_candidates)
    )
    should_suppress = low_conf_thin_fragment or (punctuation_fragment and bool(neighbor_candidates))
    return should_suppress, {
        "mean_confidence": record["confidence"]["mean_confidence"],
        "height_px": height,
        "punctuation_fragment": punctuation_fragment,
        "same_lane_neighbor_requirement": "at_least_one_neighbor_with_vertical_edge_gap_le_36_px",
        "nearest_same_lane_neighbor": neighbor_candidates[0] if neighbor_candidates else None,
        "decision_basis": "low_conf_thin_fragment_or_punctuation_fragment" if should_suppress else "preserve",
    }


def suppress_noise(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    retained = []
    suppressed = []
    for record in records:
        should_suppress, proof = is_noise_line(record, records)
        if should_suppress:
            suppressed.append({"record": record, "proof": proof})
        else:
            retained.append(record)
    return retained, {
        "rule_id": "low_confidence_thin_noise_or_punctuation_fragment",
        "parameters": {
            "max_mean_confidence": LOW_CONF_NOISE_MAX_MEAN_CONF,
            "max_height_px": LOW_CONF_NOISE_MAX_HEIGHT_PX,
            "neighbor_vertical_edge_gap_px": LOW_CONF_NOISE_NEIGHBOR_Y_GAP_PX,
            "punctuation_regex": PUNCTUATION_FRAGMENT_RE.pattern,
            "evaluation_mode": "simultaneous_against_variant_input_records",
        },
        "suppressed_records": [
            {**suppression_summary(item["record"], "noise_or_punctuation_fragment"), "proof": item["proof"]}
            for item in suppressed
        ],
    }


def suppression_summary(record: dict[str, Any], reason: str) -> dict[str, Any]:
    return {
        "record_id": record["record_id"],
        "source_order": record["source_order"],
        "tsv_line_key": record["tsv_line_key"],
        "text": record["text"],
        "normalized_text": record["normalized_text"],
        "page_bbox_half_open": record["page_bbox_half_open"],
        "mean_confidence": record["confidence"]["mean_confidence"],
        "reason": reason,
    }


def score_candidate(candidate_text: str) -> tuple[str, Path, dict[str, Any]]:
    reference_text = overview.extract_reference_text(P013_REFERENCE)
    return "reference_text_map_not_ocr_verified", P013_REFERENCE, fg.metrics(candidate_text, reference_text)


def assert_elo_floor(candidate_id: str, metrics: dict[str, Any]) -> None:
    if candidate_id not in {
        "p013_ssp_a0_elo_exact_collapse_baseline",
        "p013_ssp_c_floor_guarded_near_overlap_then_noise",
    }:
        return
    similarity = metrics["sequence_similarity_ratio"]
    recall = metrics["token_recall"]
    if abs(similarity - ELO_BEST_SIMILARITY) > 0.000001 or abs(recall - ELO_BEST_TOKEN_RECALL) > 0.000001:
        raise SystemExit(
            f"{candidate_id} failed ELO floor guard: similarity={similarity}, token_recall={recall}"
        )


def apply_variant(records: list[dict[str, Any]], variant_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    ledgers = []
    if variant_id == "p013_ssp_a0_elo_exact_collapse_baseline":
        return records, ledgers
    if variant_id == "p013_ssp_a_near_overlap_confidence":
        retained, ledger = suppress_near_overlap_confidence(records)
        return retained, [ledger]
    if variant_id == "p013_ssp_b_noise_from_a0":
        retained, ledger = suppress_noise(records)
        return retained, [ledger]
    if variant_id == "p013_ssp_c_floor_guarded_near_overlap_then_noise":
        probe_retained, ledger_a = suppress_near_overlap_confidence(records)
        probe_retained, ledger_b = suppress_noise(probe_retained)
        ledger_b["evaluation_mode"] = "sequential_after_near_overlap_confidence"
        return records, [
            {
                "rule_id": "floor_guarded_combined_probe",
                "candidate_output_policy": "preserve_sealed_elo_a0_retained_set",
                "probe_retained_record_ids": [item["record_id"] for item in probe_retained],
                "probe_suppressed_record_ids": [
                    item["record_id"] for item in records if item["record_id"] not in {kept["record_id"] for kept in probe_retained}
                ],
                "floor_guard": {
                    "sequence_similarity_ratio": ELO_BEST_SIMILARITY,
                    "token_recall": ELO_BEST_TOKEN_RECALL,
                    "reason": "combined suppression cannot replace A0 as candidate output in prep unless a separately reviewed selector rule defines non-regression behavior",
                },
                "probe_ledgers": [ledger_a, ledger_b],
            }
        ]
    raise SystemExit(f"unknown SSP variant: {variant_id}")


VARIANTS = [
    "p013_ssp_a0_elo_exact_collapse_baseline",
    "p013_ssp_a_near_overlap_confidence",
    "p013_ssp_b_noise_from_a0",
    "p013_ssp_c_floor_guarded_near_overlap_then_noise",
]


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    source_records = elo_best_records()
    write_json(
        OUT_ROOT / "enriched_elo_best_records.json",
        {
            "record_schema": {
                "record_id": "<source_region>:<tsv_block>.<tsv_par>.<tsv_line>",
                "source_order": "<sealed_region_index_2_digits>.<sealed_line_index_3_digits>",
                "tsv_line_key": "<source_region>:<tsv_block>.<tsv_par>.<tsv_line>",
                "page_bbox_half_open": "page-space [x1,y1,x2,y2], half-open",
            },
            "records": source_records,
        },
    )
    sealed_candidates = []
    for variant_id in VARIANTS:
        retained, suppression_ledgers = apply_variant(source_records, variant_id)
        candidate_text = "\n".join(item["text"] for item in retained).strip() + "\n"
        candidate_path = OUT_ROOT / "candidate_texts" / variant_id / "page_013_candidate.md"
        trace_path = OUT_ROOT / "retained_record_traces" / variant_id / "page_013_retained_records.json"
        ledger_path = OUT_ROOT / "suppression_ledgers" / variant_id / "page_013_suppression_ledger.json"
        write_text(candidate_path, candidate_text)
        candidate_sha = sha256_file(candidate_path)
        normalized_path = OUT_ROOT / "normalized_candidate_texts" / variant_id / "page_013_candidate_normalized.txt"
        write_text(normalized_path, overview.normalize_candidate_for_metrics(candidate_text) + "\n")
        normalized_sha = sha256_file(normalized_path)
        write_json(trace_path, retained)
        write_json(ledger_path, suppression_ledgers)
        sealed_candidates.append(
            {
                "page": PAGE,
                "candidate_id": variant_id,
                "candidate_text": candidate_text,
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": candidate_sha,
                "normalized_candidate_path": normalized_path.relative_to(ROOT).as_posix(),
                "normalized_candidate_sha256": normalized_sha,
                "retained_record_trace_path": trace_path.relative_to(ROOT).as_posix(),
                "retained_record_trace_sha256": sha256_file(trace_path),
                "suppression_ledger_path": ledger_path.relative_to(ROOT).as_posix(),
                "suppression_ledger_sha256": sha256_file(ledger_path),
                "candidate_hash_sealed_before_reference_scoring": True,
                "suppressed_record_count": len(source_records) - len(retained),
            }
        )
    reference_sha = sha256_file(P013_REFERENCE)
    if reference_sha != EXPECTED_REFERENCE_HASH:
        raise SystemExit(f"source_reference hash mismatch: {reference_sha}")
    reference_text = overview.extract_reference_text(P013_REFERENCE)
    results = []
    for sealed in sealed_candidates:
        page_metrics = fg.metrics(sealed["candidate_text"], reference_text)
        assert_elo_floor(sealed["candidate_id"], page_metrics)
        diagnostic_threshold_met = (
            page_metrics["sequence_similarity_ratio"] >= DIAGNOSTIC_SEQUENCE_SIMILARITY
            and page_metrics["token_recall"] >= DIAGNOSTIC_TOKEN_RECALL
        )
        del sealed["candidate_text"]
        results.append(
            {
                **sealed,
                "reference_label": "reference_text_map_not_ocr_verified",
                "reference_path": P013_REFERENCE.relative_to(ROOT).as_posix(),
                "reference_sha256": reference_sha,
                "reference_loaded_after_candidate_hashing": True,
                "metrics": page_metrics,
                "elo_best_baseline_metrics": {
                    "sequence_similarity_ratio": ELO_BEST_SIMILARITY,
                    "token_recall": ELO_BEST_TOKEN_RECALL,
                },
                "metric_deltas_from_elo_best": {
                    "sequence_similarity_delta": round(page_metrics["sequence_similarity_ratio"] - ELO_BEST_SIMILARITY, 6),
                    "token_recall_delta": round(page_metrics["token_recall"] - ELO_BEST_TOKEN_RECALL, 6),
                },
                "diagnostic_threshold_met": diagnostic_threshold_met,
                "method_registry_candidate": diagnostic_threshold_met,
            }
        )
    results.sort(key=lambda item: (item["metrics"]["sequence_similarity_ratio"], item["metrics"]["token_recall"]), reverse=True)
    write_json(OUT_ROOT / "rankings" / "page_013_candidate_rankings.json", results)
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_p013_structural_suppression_diagnostic_completed",
        "page": PAGE,
        "verified_inputs": verified_inputs,
        "source_lane_id": elo.LANE_ID,
        "candidate_generation_inputs": ["sealed_p013_elo_best_retained_set", "cached_p013_raw_tsv_word_confidences"],
        "ocr_execution_performed": False,
        "reference_guided_repair_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "all_candidate_hashes_sealed_before_reference_text_load": True,
        "text_token_mutation_performed": False,
        "diagnostic_thresholds": {
            "sequence_similarity": DIAGNOSTIC_SEQUENCE_SIMILARITY,
            "token_recall": DIAGNOSTIC_TOKEN_RECALL,
            "method_registry_candidate_requires_threshold": True,
            "acceptance_effect": "none",
        },
        "suppression_parameters": {
            "near_overlap_min_area_ratio": NEAR_OVERLAP_MIN_AREA_RATIO,
            "near_overlap_max_center_y_gap_px": NEAR_OVERLAP_MAX_CENTER_Y_GAP_PX,
            "near_overlap_min_token_dice": NEAR_OVERLAP_MIN_TOKEN_DICE,
            "confidence_tie_margin": CONFIDENCE_TIE_MARGIN,
            "low_conf_noise_max_mean_conf": LOW_CONF_NOISE_MAX_MEAN_CONF,
            "low_conf_noise_max_height_px": LOW_CONF_NOISE_MAX_HEIGHT_PX,
            "low_conf_noise_neighbor_y_gap_px": LOW_CONF_NOISE_NEIGHBOR_Y_GAP_PX,
            "punctuation_fragment_regex": PUNCTUATION_FRAGMENT_RE.pattern,
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
    write_json(OUT_ROOT / "p013_structural_suppression_diagnostic_report.json", report)
    lines = [
        "# P013 Structural Suppression Diagnostic - C01TEP013SSP-G1-VIRAL-001",
        "",
        "Status: `candidate_only_p013_structural_suppression_diagnostic_completed`",
        "",
        "No OCR was executed. Candidates start from the sealed ELO best retained set and apply fixed structural suppression rules.",
        "",
        "| Candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta from ELO | Token recall delta | Suppressed records |",
        "|---|---:|---:|---|---:|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| `{result['candidate_id']}` | `{result['metrics']['sequence_similarity_ratio']}` | "
            f"`{result['metrics']['token_recall']}` | `{result['diagnostic_threshold_met']}` | "
            f"`{result['metric_deltas_from_elo_best']['sequence_similarity_delta']}` | "
            f"`{result['metric_deltas_from_elo_best']['token_recall_delta']}` | "
            f"`{result['suppressed_record_count']}` |"
        )
    lines.extend(
        [
            "",
            "Boundary: P013-only diagnostic assembly evidence; no OCR execution, no reference-guided repair, no accepted/semantic/page-status/source mutation, no method selector, no production output, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "p013_structural_suppression_diagnostic_summary.md", "\n".join(lines))
    manifest_lines = [
        "# P013 Structural Suppression Diagnostic Manifest - C01TEP013SSP-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p013_structural_suppression_diagnostic_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "p013_structural_suppression_diagnostic_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
