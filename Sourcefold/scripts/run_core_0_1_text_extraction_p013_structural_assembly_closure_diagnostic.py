from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import run_core_0_1_text_extraction_full_page_geometry_probe_p018_p017 as fg
import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview
import run_core_0_1_text_extraction_p013_structural_suppression_diagnostic as ssp


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
SSP_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_structural_suppression_diagnostic_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEP013SAC-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-STRUCTURAL-ASSEMBLY-CLOSURE-DIAGNOSTIC-001"
HUMAN_DECISION = (
    "Следующий ход — новый цикл от этого результата: разбирать оставшийся structure/assembly gap "
    "без OCR и без reference-token insertion."
)
PAGE = "013"
SOURCEFOLD_PREDECESSOR_COMMIT = "de0d759b9947383bf21bfe4af0bacae5f1eaff21"
DIAGNOSTIC_SEQUENCE_SIMILARITY = 0.997
DIAGNOSTIC_TOKEN_RECALL = 0.993939
SSP_BEST_SIMILARITY = 0.914027
SSP_BEST_TOKEN_RECALL = 0.993939

SSP_REPORT = SSP_ROOT / "p013_structural_suppression_diagnostic_report.json"
SSP_SUMMARY = SSP_ROOT / "p013_structural_suppression_diagnostic_summary.md"
SSP_MANIFEST = SSP_ROOT / "p013_structural_suppression_diagnostic_manifest.md"
SSP_A_CANDIDATE = SSP_ROOT / "candidate_texts" / "p013_ssp_a_near_overlap_confidence" / "page_013_candidate.md"
SSP_A_NORMALIZED = (
    SSP_ROOT / "normalized_candidate_texts" / "p013_ssp_a_near_overlap_confidence" / "page_013_candidate_normalized.txt"
)
SSP_A_TRACE = SSP_ROOT / "retained_record_traces" / "p013_ssp_a_near_overlap_confidence" / "page_013_retained_records.json"
SSP_A_LEDGER = SSP_ROOT / "suppression_ledgers" / "p013_ssp_a_near_overlap_confidence" / "page_013_suppression_ledger.json"
P013_REFERENCE = ssp.P013_REFERENCE

EXPECTED_INPUT_HASHES = {
    "ssp_report": (SSP_REPORT, "712446CC642C1499E9786630D9F0E136B526CC028875BF7E6D4BA4F3E1A89D9B"),
    "ssp_summary": (SSP_SUMMARY, "0AD50E8AAE374BB02654EC25A90EE07823AB25F0E4C3EA37EA6AAA181FF92D4B"),
    "ssp_manifest": (SSP_MANIFEST, "11E29CA99CBBC60B04A3466B9A665EEB9C6978F52867720D396C6A839641183E"),
    "ssp_a_candidate": (SSP_A_CANDIDATE, "F02D342C7FFA21FC396169294EF01713D36BB4555D3DDB54094472BC0F3EC36D"),
    "ssp_a_normalized_candidate": (SSP_A_NORMALIZED, "909B81B4614346DBD0F0C74A012CD6935A2EA3A46AEA1847E46E7401B792B8E0"),
    "ssp_a_retained_records": (SSP_A_TRACE, "6C9703A0255BA3B97A5C3872C6AF7513FFACBDAE153CB899A3E5AA1CF303A9A2"),
    "ssp_a_suppression_ledger": (SSP_A_LEDGER, "14FF15526D97CD2E9E6F5B39BA4FB857F83DA761AB027860174948A4778BC424"),
    **{key: value for key, value in ssp.EXPECTED_INPUT_HASHES.items() if key.startswith("p013_b") or key == "source_ranking"},
}
EXPECTED_REFERENCE_HASH = "7E65E4DE7DB67FCBC5E384FF6A0E6AF54E0D375514E41F32066D530AA1561E67"

SEAM_MIN_AREA_OVERLAP_RATIO = 0.72
SEAM_MIN_AREA_SIZE_RATIO = 0.80
SEAM_MAX_CENTER_Y_GAP_PX = 8
SEAM_MIN_TOKEN_DICE = 0.90
DECLARED_SEAM_PAIRS = {("P013-B004-TES", "P013-B005-TES")}

VARIANTS = [
    "p013_sac_a0_ssp_best_baseline",
    "p013_sac_b_noise_after_ssp",
    "p013_sac_c_declared_seam_fracture_after_ssp",
    "p013_sac_d_noise_then_declared_seam_fracture",
    "p013_sac_e_paragraph_join_d",
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
    parser = argparse.ArgumentParser(description="Run P013 structural assembly closure diagnostic.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 structural assembly closure diagnostic is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 structural assembly closure diagnostic requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 structural assembly closure diagnostic requires the exact bounded human decision")


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
        "sourcefold_predecessor_commit": SOURCEFOLD_PREDECESSOR_COMMIT,
    }


def ssp_best_records() -> list[dict[str, Any]]:
    return json.loads(SSP_A_TRACE.read_text(encoding="utf-8"))


def source_order_key(record: dict[str, Any]) -> tuple[int, int]:
    left, right = record["source_order"].split(".")
    return int(left), int(right)


def is_region_lower_boundary(record: dict[str, Any], records: list[dict[str, Any]]) -> bool:
    region_records = [item for item in records if item["source_region"] == record["source_region"]]
    return record["final_ordinal"] == max(item["final_ordinal"] for item in region_records)


def is_region_upper_boundary(record: dict[str, Any], records: list[dict[str, Any]]) -> bool:
    region_records = [item for item in records if item["source_region"] == record["source_region"]]
    return record["final_ordinal"] == min(item["final_ordinal"] for item in region_records)


def token_containment_with_bounded_fragment_drop(earlier: str, later: str) -> dict[str, Any] | None:
    earlier_tokens = ssp.tokens(earlier)
    later_tokens = ssp.tokens(later)
    if not earlier_tokens or len(earlier_tokens) != len(later_tokens):
        return None
    mismatches = [
        (index, left, right)
        for index, (left, right) in enumerate(zip(earlier_tokens, later_tokens))
        if left != right
    ]
    if not mismatches:
        return {
            "earlier_tokens": earlier_tokens,
            "later_tokens": later_tokens,
            "mismatch_count": 0,
            "bounded_fragment_drop": False,
        }
    if len(mismatches) != 1:
        return None
    index, left, right = mismatches[0]
    bounded_drop = index in {0, len(earlier_tokens) - 1} and len(left) > len(right) and left.endswith(right)
    if not bounded_drop or len(left) - len(right) > 2:
        return None
    return {
        "earlier_tokens": earlier_tokens,
        "later_tokens": later_tokens,
        "mismatch_count": 1,
        "bounded_fragment_drop": True,
        "fragment_drop": {
            "token_index": index,
            "earlier_token": left,
            "later_token": right,
            "dropped_prefix_chars": left[: len(left) - len(right)],
        },
    }


def seam_fracture_edge(
    earlier: dict[str, Any],
    later: dict[str, Any],
    records: list[dict[str, Any]],
) -> dict[str, Any] | None:
    if (earlier["source_region"], later["source_region"]) not in DECLARED_SEAM_PAIRS:
        return None
    if not is_region_lower_boundary(earlier, records) or not is_region_upper_boundary(later, records):
        return None
    if source_order_key(earlier) >= source_order_key(later):
        return None
    if earlier["lane_id"] != later["lane_id"]:
        return None
    y_gap = abs(earlier["page_center"][1] - later["page_center"][1])
    if y_gap > SEAM_MAX_CENTER_Y_GAP_PX:
        return None
    overlap = ssp.min_area_overlap_ratio(earlier["page_bbox_half_open"], later["page_bbox_half_open"])
    if overlap < SEAM_MIN_AREA_OVERLAP_RATIO:
        return None
    area_size_ratio = min(ssp.area(earlier["page_bbox_half_open"]), ssp.area(later["page_bbox_half_open"])) / max(
        ssp.area(earlier["page_bbox_half_open"]),
        ssp.area(later["page_bbox_half_open"]),
    )
    if area_size_ratio < SEAM_MIN_AREA_SIZE_RATIO:
        return None
    dice = ssp.token_dice(earlier["normalized_text"], later["normalized_text"])
    if dice < SEAM_MIN_TOKEN_DICE:
        return None
    earlier_support = len(ssp.tokens(earlier["normalized_text"]))
    later_support = len(ssp.tokens(later["normalized_text"]))
    if earlier_support < later_support:
        return None
    containment = token_containment_with_bounded_fragment_drop(earlier["normalized_text"], later["normalized_text"])
    if containment is None:
        return None
    return {
        "earlier_record_id": earlier["record_id"],
        "later_record_id": later["record_id"],
        "declared_seam_pair": [earlier["source_region"], later["source_region"]],
        "same_lane": True,
        "center_y_gap_px": round(y_gap, 6),
        "min_area_overlap_ratio": round(overlap, 6),
        "area_size_ratio": round(area_size_ratio, 6),
        "token_dice": round(dice, 6),
        "earlier_normalized_token_support": earlier_support,
        "later_normalized_token_support": later_support,
        "boundary_position_proof": {
            "earlier_is_lower_boundary_record": True,
            "later_is_upper_boundary_record": True,
        },
        "token_containment_proof": containment,
        "decision": "suppress_later_declared_seam_fragment",
    }


def suppress_declared_seam_fractures(records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    suppressed_ids = set()
    edges = []
    ordered = sorted(records, key=lambda item: item["final_ordinal"])
    for earlier in ordered:
        for later in ordered:
            if earlier["record_id"] == later["record_id"] or later["record_id"] in suppressed_ids:
                continue
            edge = seam_fracture_edge(earlier, later, ordered)
            if edge:
                edges.append(edge)
                suppressed_ids.add(later["record_id"])
    retained = [record for record in ordered if record["record_id"] not in suppressed_ids]
    suppressed = [record for record in ordered if record["record_id"] in suppressed_ids]
    return retained, {
        "rule_id": "declared_seam_fractured_duplicate",
        "parameters": {
            "declared_seam_pairs": [list(item) for item in sorted(DECLARED_SEAM_PAIRS)],
            "same_lane_required": True,
            "min_area_overlap_ratio": SEAM_MIN_AREA_OVERLAP_RATIO,
            "min_area_size_ratio": SEAM_MIN_AREA_SIZE_RATIO,
            "max_center_y_gap_px": SEAM_MAX_CENTER_Y_GAP_PX,
            "min_token_dice": SEAM_MIN_TOKEN_DICE,
            "earlier_source_order_required": True,
            "earlier_lower_boundary_required": True,
            "later_upper_boundary_required": True,
            "earlier_normalized_token_support_gte_later": True,
            "later_tokens_contained_in_earlier_except_bounded_edge_fragment_drop": True,
            "text_literal_matching": False,
        },
        "edges": edges,
        "suppressed_records": [ssp.suppression_summary(item, "declared_seam_fractured_duplicate_later_fragment") for item in suppressed],
    }


def apply_variant(records: list[dict[str, Any]], variant_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    if variant_id == "p013_sac_a0_ssp_best_baseline":
        return records, [], "line_join"
    if variant_id == "p013_sac_b_noise_after_ssp":
        retained, ledger = ssp.suppress_noise(records)
        return retained, [ledger], "line_join"
    if variant_id == "p013_sac_c_declared_seam_fracture_after_ssp":
        retained, ledger = suppress_declared_seam_fractures(records)
        return retained, [ledger], "line_join"
    if variant_id == "p013_sac_d_noise_then_declared_seam_fracture":
        retained, ledger_b = ssp.suppress_noise(records)
        retained, ledger_c = suppress_declared_seam_fractures(retained)
        return retained, [ledger_b, ledger_c], "line_join"
    if variant_id == "p013_sac_e_paragraph_join_d":
        retained, ledger_b = ssp.suppress_noise(records)
        retained, ledger_c = suppress_declared_seam_fractures(retained)
        return retained, [ledger_b, ledger_c], "source_region_paragraph_join"
    raise SystemExit(f"unknown SAC variant: {variant_id}")


def assemble_text(records: list[dict[str, Any]], assembly_mode: str) -> tuple[str, dict[str, Any]]:
    ordered = sorted(records, key=lambda item: item["final_ordinal"])
    if assembly_mode == "line_join":
        return "\n".join(item["text"] for item in ordered).strip() + "\n", {
            "assembly_mode": assembly_mode,
            "record_text_mutation_performed": False,
            "separator_only_change": False,
        }
    if assembly_mode != "source_region_paragraph_join":
        raise SystemExit(f"unknown assembly mode: {assembly_mode}")
    groups: list[list[dict[str, Any]]] = []
    for record in ordered:
        if groups and groups[-1][-1]["source_region"] == record["source_region"]:
            groups[-1].append(record)
        else:
            groups.append([record])
    text = "\n".join(" ".join(item["text"] for item in group) for group in groups).strip() + "\n"
    return text, {
        "assembly_mode": assembly_mode,
        "record_text_mutation_performed": False,
        "separator_only_change": True,
        "grouping_key": "adjacent_source_region",
    }


def assert_ssp_floor(candidate_id: str, metrics: dict[str, Any]) -> None:
    if candidate_id != "p013_sac_a0_ssp_best_baseline":
        return
    similarity = metrics["sequence_similarity_ratio"]
    recall = metrics["token_recall"]
    if abs(similarity - SSP_BEST_SIMILARITY) > 0.000001 or abs(recall - SSP_BEST_TOKEN_RECALL) > 0.000001:
        raise SystemExit(f"{candidate_id} failed SSP best floor guard: similarity={similarity}, token_recall={recall}")


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    source_records = ssp_best_records()
    sealed_candidates = []
    for variant_id in VARIANTS:
        retained, ledgers, assembly_mode = apply_variant(source_records, variant_id)
        candidate_text, assembly_trace = assemble_text(retained, assembly_mode)
        candidate_path = OUT_ROOT / "candidate_texts" / variant_id / "page_013_candidate.md"
        normalized_path = OUT_ROOT / "normalized_candidate_texts" / variant_id / "page_013_candidate_normalized.txt"
        trace_path = OUT_ROOT / "retained_record_traces" / variant_id / "page_013_retained_records.json"
        ledger_path = OUT_ROOT / "suppression_ledgers" / variant_id / "page_013_suppression_ledger.json"
        assembly_trace_path = OUT_ROOT / "assembly_traces" / variant_id / "page_013_assembly_trace.json"
        write_text(candidate_path, candidate_text)
        write_text(normalized_path, overview.normalize_candidate_for_metrics(candidate_text) + "\n")
        write_json(trace_path, retained)
        write_json(ledger_path, ledgers)
        write_json(assembly_trace_path, {**assembly_trace, "retained_record_ids": [item["record_id"] for item in retained]})
        sealed_candidates.append(
            {
                "page": PAGE,
                "candidate_id": variant_id,
                "candidate_text": candidate_text,
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": sha256_file(candidate_path),
                "normalized_candidate_path": normalized_path.relative_to(ROOT).as_posix(),
                "normalized_candidate_sha256": sha256_file(normalized_path),
                "retained_record_trace_path": trace_path.relative_to(ROOT).as_posix(),
                "retained_record_trace_sha256": sha256_file(trace_path),
                "suppression_ledger_path": ledger_path.relative_to(ROOT).as_posix(),
                "suppression_ledger_sha256": sha256_file(ledger_path),
                "assembly_trace_path": assembly_trace_path.relative_to(ROOT).as_posix(),
                "assembly_trace_sha256": sha256_file(assembly_trace_path),
                "candidate_hash_sealed_before_reference_scoring": True,
                "suppressed_record_count": len(source_records) - len(retained),
                "assembly_mode": assembly_mode,
            }
        )
    reference_sha = sha256_file(P013_REFERENCE)
    if reference_sha != EXPECTED_REFERENCE_HASH:
        raise SystemExit(f"source_reference hash mismatch: {reference_sha}")
    reference_text = overview.extract_reference_text(P013_REFERENCE)
    results = []
    for sealed in sealed_candidates:
        page_metrics = fg.metrics(sealed["candidate_text"], reference_text)
        assert_ssp_floor(sealed["candidate_id"], page_metrics)
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
                "ssp_best_baseline_metrics": {
                    "sequence_similarity_ratio": SSP_BEST_SIMILARITY,
                    "token_recall": SSP_BEST_TOKEN_RECALL,
                },
                "metric_deltas_from_ssp_best": {
                    "sequence_similarity_delta": round(page_metrics["sequence_similarity_ratio"] - SSP_BEST_SIMILARITY, 6),
                    "token_recall_delta": round(page_metrics["token_recall"] - SSP_BEST_TOKEN_RECALL, 6),
                },
                "diagnostic_improvement_over_ssp_best": (
                    page_metrics["sequence_similarity_ratio"] > SSP_BEST_SIMILARITY
                    and page_metrics["token_recall"] >= SSP_BEST_TOKEN_RECALL
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
        "status": "candidate_only_p013_structural_assembly_closure_diagnostic_completed",
        "page": PAGE,
        "verified_inputs": verified_inputs,
        "source_lane_id": ssp.LANE_ID,
        "candidate_generation_inputs": ["sealed_p013_ssp_best_retained_set", "pinned_structural_suppression_ledgers"],
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
        "seam_fracture_parameters": {
            "declared_seam_pairs": [list(item) for item in sorted(DECLARED_SEAM_PAIRS)],
            "min_area_overlap_ratio": SEAM_MIN_AREA_OVERLAP_RATIO,
            "min_area_size_ratio": SEAM_MIN_AREA_SIZE_RATIO,
            "max_center_y_gap_px": SEAM_MAX_CENTER_Y_GAP_PX,
            "min_token_dice": SEAM_MIN_TOKEN_DICE,
            "text_literal_matching": False,
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
    write_json(OUT_ROOT / "p013_structural_assembly_closure_diagnostic_report.json", report)
    lines = [
        "# P013 Structural Assembly Closure Diagnostic - C01TEP013SAC-G1-VIRAL-001",
        "",
        "Status: `candidate_only_p013_structural_assembly_closure_diagnostic_completed`",
        "",
        "No OCR was executed. Candidates start from the sealed SSP best retained set and apply fixed structural assembly deletion rules.",
        "",
        "| Candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta from SSP | Token recall delta | Suppressed records |",
        "|---|---:|---:|---|---:|---:|---:|",
    ]
    for result in results:
        lines.append(
            f"| `{result['candidate_id']}` | `{result['metrics']['sequence_similarity_ratio']}` | "
            f"`{result['metrics']['token_recall']}` | `{result['diagnostic_threshold_met']}` | "
            f"`{result['metric_deltas_from_ssp_best']['sequence_similarity_delta']}` | "
            f"`{result['metric_deltas_from_ssp_best']['token_recall_delta']}` | "
            f"`{result['suppressed_record_count']}` |"
        )
    lines.extend(
        [
            "",
            "Boundary: P013-only diagnostic assembly evidence; no OCR execution, no reference-guided repair, no accepted/semantic/page-status/source mutation, no selector update, no production output, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "p013_structural_assembly_closure_diagnostic_summary.md", "\n".join(lines))
    manifest_lines = [
        "# P013 Structural Assembly Closure Diagnostic Manifest - C01TEP013SAC-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p013_structural_assembly_closure_diagnostic_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "p013_structural_assembly_closure_diagnostic_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
