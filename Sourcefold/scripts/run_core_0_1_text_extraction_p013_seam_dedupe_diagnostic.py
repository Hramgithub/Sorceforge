from __future__ import annotations

import argparse
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
STALE_ROOT = (
    TRIAL_ROOT / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_001"
)
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_seam_dedupe_diagnostic_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEP013SDD-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-P013-SEAM-DEDUPE-DIAGNOSTIC-001"
HUMAN_DECISION = "Работай по плану"
PAGE = "013"
SOURCE_CANDIDATE_ID = "full_page_triage_boxes_expanded_psm4"
DIAGNOSTIC_SEQUENCE_SIMILARITY = 0.997
DIAGNOSTIC_TOKEN_RECALL_FLOOR = 0.993939
SOURCE_SIMILARITY = 0.242772
SOURCE_TOKEN_RECALL = 0.993939

EXPECTED_INPUT_HASHES = {
    "source_geometry_probe_report": (
        SOURCE_ROOT / "geometry_probe_012_013_016_017_018_020_report.json",
        "5A13578D917186A48ECDA8C13C5EE6998700386AA70FFF1913342FEDDB69DAFF",
    ),
    "source_p013_candidate": (
        SOURCE_ROOT / "candidate_texts" / SOURCE_CANDIDATE_ID / "page_013_candidate.md",
        "6AA2ADCDB1CDE71741F057300DC8888543F315BC14CD65F02602D71145CA5412",
    ),
    "source_p013_raw_b001": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "01_p013_b001_tes.txt",
        "5C2530221C1F90DF16A7CD1990D261A1161F50D7D9EB75D8833B002534CAAAFB",
    ),
    "source_p013_raw_b002": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "02_p013_b002_tes.txt",
        "8F35311433B2EB2C9AF8D69C5D32D307D81B3146AFFCB806A08AA649D895124B",
    ),
    "source_p013_raw_b003": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "03_p013_b003_tes.txt",
        "C88C2CCB007EDCC5DE3BB43A0CC40E29319B838C1C68746FA3EEA0F5CA0E223C",
    ),
    "source_p013_raw_b004": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "04_p013_b004_tes.txt",
        "60782A9328A0C1B7F97AD2F8B7E76BA67CF6C8EE0EB26507093896DF614E0959",
    ),
    "source_p013_raw_b005": (
        SOURCE_ROOT / "raw_ocr" / SOURCE_CANDIDATE_ID / "p013" / "05_p013_b005_tes.txt",
        "C910438BCE5C61AC30CE2EEC5683E3700CD82BB0938308A31F7C1A8471B4A3B4",
    ),
    "stale_output_marker": (
        STALE_ROOT / "INCOMPLETE_STALE_DO_NOT_USE.md",
        "03238B0A726C444B3AED24C70FDEB09427F094E522765F1F1ECAD8BFF0BD5A45",
    ),
}

BLOCKS = [
    {
        "id": "P013-B001",
        "role": "mythos_investigators_continuation",
        "path_key": "source_p013_raw_b001",
        "expanded_page_space_box": [136, 181, 1284, 669],
    },
    {
        "id": "P013-B002",
        "role": "documentary_film_crew",
        "path_key": "source_p013_raw_b002",
        "expanded_page_space_box": [186, 601, 1294, 989],
    },
    {
        "id": "P013-B003",
        "role": "tourists_left_start",
        "path_key": "source_p013_raw_b003",
        "expanded_page_space_box": [186, 936, 1294, 1124],
    },
    {
        "id": "P013-B004",
        "role": "tourists_right_continuation",
        "path_key": "source_p013_raw_b004",
        "expanded_page_space_box": [1266, 181, 2434, 929],
    },
    {
        "id": "P013-B005",
        "role": "pesky_teenagers",
        "path_key": "source_p013_raw_b005",
        "expanded_page_space_box": [1311, 881, 2419, 1119],
    },
]

SEAMS = [
    {"id": "P013-S001", "previous": "P013-B001", "current": "P013-B002"},
    {"id": "P013-S002", "previous": "P013-B002", "current": "P013-B003"},
    {"id": "P013-S003", "previous": "P013-B004", "current": "P013-B005"},
]

VARIANTS = [
    {
        "id": "sealed_raw_v1_max_tail_prefix_exact_dedupe",
        "description": "Exact normalized token overlap from previous tail to current prefix; max 80 previous tokens and 40 current prefix tokens.",
        "previous_tail_tokens": 80,
        "current_prefix_tokens": 40,
        "minimum_overlap_tokens": 3,
    },
    {
        "id": "sealed_raw_v2_window160_prefix_exact_dedupe",
        "description": "Exact normalized token overlap in a fixed approximate 160-character seam window; max 30 previous tokens and 24 current prefix tokens.",
        "previous_tail_tokens": 30,
        "current_prefix_tokens": 24,
        "minimum_overlap_tokens": 3,
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
    parser = argparse.ArgumentParser(description="Run P013 sealed-candidate seam dedupe diagnostic.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P013 seam dedupe diagnostic is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P013 seam dedupe diagnostic requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P013 seam dedupe diagnostic requires the exact bounded human decision")


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
    if not STALE_ROOT.exists() or not (STALE_ROOT / "INCOMPLETE_STALE_DO_NOT_USE.md").exists():
        raise SystemExit("_G1_VIRAL_001 stale output marker is required")
    return {
        "authorization_ledger": {
            "path": LEDGER.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(LEDGER),
        },
        "pinned_inputs": verify_expected_inputs(),
        "stale_output_root_rejected": STALE_ROOT.relative_to(ROOT).as_posix(),
    }


def token_spans(text: str) -> list[dict[str, Any]]:
    spans = []
    for match in re.finditer(r"[A-Za-z0-9']+", text.replace("\u2018", "'").replace("\u2019", "'")):
        spans.append({"token": match.group(0).lower(), "start": match.start(), "end": match.end()})
    return spans


def load_blocks() -> dict[str, str]:
    loaded = {}
    for block in BLOCKS:
        path = EXPECTED_INPUT_HASHES[block["path_key"]][0]
        loaded[block["id"]] = path.read_text(encoding="utf-8", errors="replace").strip()
    return loaded


def overlap_box(previous_box: list[int], current_box: list[int]) -> list[int] | None:
    left = max(previous_box[0], current_box[0])
    top = max(previous_box[1], current_box[1])
    right = min(previous_box[2], current_box[2])
    bottom = min(previous_box[3], current_box[3])
    if left >= right or top >= bottom:
        return None
    return [left, top, right, bottom]


def find_prefix_overlap(
    *,
    previous_text: str,
    current_text: str,
    previous_tail_tokens: int,
    current_prefix_tokens: int,
    minimum_overlap_tokens: int,
) -> dict[str, Any] | None:
    previous_tokens = token_spans(previous_text)[-previous_tail_tokens:]
    current_tokens = token_spans(current_text)[:current_prefix_tokens]
    max_len = min(len(previous_tokens), len(current_tokens))
    for length in range(max_len, minimum_overlap_tokens - 1, -1):
        previous_suffix = previous_tokens[-length:]
        prefix = [item["token"] for item in current_tokens[:length]]
        suffix = [item["token"] for item in previous_suffix]
        if suffix == prefix:
            end = current_tokens[length - 1]["end"]
            return {
                "overlap_tokens": prefix,
                "current_delete_span": [0, end],
                "previous_match_span": [previous_suffix[0]["start"], previous_suffix[-1]["end"]],
                "previous_match_ends_at_boundary": True,
                "deleted_text": current_text[:end],
                "match_basis": "exact_normalized_token_overlap",
            }
    return None


def apply_variant(block_texts: dict[str, str], variant: dict[str, Any]) -> tuple[dict[str, str], list[dict[str, Any]]]:
    repaired = dict(block_texts)
    ledger = []
    block_meta = {block["id"]: block for block in BLOCKS}
    for seam in SEAMS:
        previous = seam["previous"]
        current = seam["current"]
        proof = find_prefix_overlap(
            previous_text=repaired[previous],
            current_text=repaired[current],
            previous_tail_tokens=variant["previous_tail_tokens"],
            current_prefix_tokens=variant["current_prefix_tokens"],
            minimum_overlap_tokens=variant["minimum_overlap_tokens"],
        )
        previous_box = block_meta[previous]["expanded_page_space_box"]
        current_box = block_meta[current]["expanded_page_space_box"]
        if proof is None:
            ledger.append(
                {
                    "seam_id": seam["id"],
                    "source_block_pair": [previous, current],
                    "deletion_performed": False,
                    "expanded_page_space_overlap": overlap_box(previous_box, current_box),
                    "match_basis": "no_exact_normalized_token_overlap",
                }
            )
            continue
        start, end = proof["current_delete_span"]
        repaired[current] = repaired[current][end:].lstrip()
        ledger.append(
            {
                "seam_id": seam["id"],
                "source_block_pair": [previous, current],
                "deletion_performed": True,
                "current_source_span": [start, end],
                "previous_match_span": proof["previous_match_span"],
                "deleted_text": proof["deleted_text"],
                "deleted_token_count": len(proof["overlap_tokens"]),
                "match_basis": proof["match_basis"],
                "expanded_page_space_overlap": overlap_box(previous_box, current_box),
            }
        )
    return repaired, ledger


def candidate_markdown(block_texts: dict[str, str]) -> str:
    b001 = block_texts["P013-B001"].strip()
    b002 = block_texts["P013-B002"].replace("Documentary Film Crew \u2014", "").strip()
    b003 = block_texts["P013-B003"].replace("Tourists \u2014", "").strip()
    b004 = block_texts["P013-B004"].strip()
    b005 = block_texts["P013-B005"].replace("Pesky Teenagers \u2014", "").strip()
    chunks = [
        ("P013-TEXT-001", b001),
        ("P013-TEXT-002", f"Documentary Film Crew - {b002}"),
        ("P013-TEXT-003", f"Tourists - {b003}\n{b004}"),
        ("P013-TEXT-004", f"Pesky Teenagers - {b005}"),
    ]
    return "\n\n".join(f"## {title}\n\n{text.strip()}" for title, text in chunks).strip() + "\n"


def score_candidate(candidate_text: str) -> tuple[str, Path, dict[str, Any]]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[PAGE] / "review_assets"
    reference = overview.reference_for_page(PAGE, assets)
    if reference is None:
        raise SystemExit("P013 missing scorer reference")
    label, reference_path = reference
    reference_text = overview.extract_reference_text(reference_path)
    return label, reference_path, fg.metrics(candidate_text, reference_text)


def build() -> None:
    verified_inputs = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    raw_blocks = load_blocks()
    results = []
    for variant in VARIANTS:
        repaired_blocks, deletion_ledger = apply_variant(raw_blocks, variant)
        candidate_text = candidate_markdown(repaired_blocks)
        candidate_path = OUT_ROOT / "candidate_texts" / variant["id"] / "page_013_candidate.md"
        write_text(candidate_path, candidate_text)
        candidate_hash = sha256_file(candidate_path)
        normalized = overview.normalize_candidate_for_metrics(candidate_text)
        normalized_path = OUT_ROOT / "normalized_candidate_texts" / variant["id"] / "page_013_candidate_normalized.txt"
        write_text(normalized_path, normalized + "\n")
        deletion_ledger_path = OUT_ROOT / "deletion_ledgers" / variant["id"] / "page_013_deletion_ledger.json"
        write_json(deletion_ledger_path, deletion_ledger)
        label, reference_path, page_metrics = score_candidate(candidate_text)
        all_deletions_explainable = all(
            (not item["deletion_performed"])
            or (
                item["match_basis"] == "exact_normalized_token_overlap"
                and item["expanded_page_space_overlap"] is not None
                and item["deleted_token_count"] >= variant["minimum_overlap_tokens"]
            )
            for item in deletion_ledger
        )
        diagnostic_threshold_met = (
            page_metrics["sequence_similarity_ratio"] >= DIAGNOSTIC_SEQUENCE_SIMILARITY
            and page_metrics["token_recall"] >= DIAGNOSTIC_TOKEN_RECALL_FLOOR
            and all_deletions_explainable
        )
        results.append(
            {
                "page": PAGE,
                "candidate_id": variant["id"],
                "description": variant["description"],
                "source_candidate_id": SOURCE_CANDIDATE_ID,
                "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
                "candidate_text_sha256": candidate_hash,
                "normalized_candidate_path": normalized_path.relative_to(ROOT).as_posix(),
                "normalized_candidate_sha256": sha256_file(normalized_path),
                "deletion_ledger_path": deletion_ledger_path.relative_to(ROOT).as_posix(),
                "deletion_ledger_sha256": sha256_file(deletion_ledger_path),
                "candidate_hash_sealed_before_reference_scoring": True,
                "reference_label": label,
                "reference_path": reference_path.relative_to(ROOT).as_posix(),
                "reference_sha256": sha256_file(reference_path),
                "reference_loaded_after_candidate_hashing": True,
                "metrics": page_metrics,
                "source_metrics": {
                    "sequence_similarity_ratio": SOURCE_SIMILARITY,
                    "token_recall": SOURCE_TOKEN_RECALL,
                },
                "metric_deltas_from_source": {
                    "sequence_similarity_delta": round(page_metrics["sequence_similarity_ratio"] - SOURCE_SIMILARITY, 6),
                    "token_recall_delta": round(page_metrics["token_recall"] - SOURCE_TOKEN_RECALL, 6),
                },
                "deletion_ledger": deletion_ledger,
                "all_deletions_explainable_by_overlap": all_deletions_explainable,
                "diagnostic_threshold_met": diagnostic_threshold_met,
            }
        )
    results.sort(key=lambda item: (item["metrics"]["sequence_similarity_ratio"], item["metrics"]["token_recall"]), reverse=True)
    write_json(OUT_ROOT / "rankings" / "page_013_candidate_rankings.json", results)
    best = results[0]
    report = {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "candidate_only_p013_seam_dedupe_diagnostic_completed",
        "page": PAGE,
        "scope": "P013-only sealed-candidate assembly repair; no OCR execution",
        "verified_inputs": verified_inputs,
        "source_geometry_probe": "C01TEGP012013016017018020-G1-VIRAL-001",
        "source_candidate_id": SOURCE_CANDIDATE_ID,
        "variants": VARIANTS,
        "seams": SEAMS,
        "results": results,
        "best_candidate": best,
        "diagnostic_thresholds": {
            "sequence_similarity": DIAGNOSTIC_SEQUENCE_SIMILARITY,
            "token_recall_floor": DIAGNOSTIC_TOKEN_RECALL_FLOOR,
            "acceptance_effect": "none",
        },
        "candidate_generation_inputs": ["sealed_existing_p013_raw_ocr_text"],
        "ocr_execution_performed": False,
        "reference_guided_repair_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "runtime_implementation_created": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "recommendation": "Commit diagnostic result, then continue the failed-page loop if P013 remains below threshold.",
    }
    write_json(OUT_ROOT / "p013_seam_dedupe_diagnostic_report.json", report)
    summary_lines = [
        "# P013 Seam Dedupe Diagnostic - C01TEP013SDD-G1-VIRAL-001",
        "",
        "Status: `candidate_only_p013_seam_dedupe_diagnostic_completed`",
        "",
        "No OCR was executed. Candidate text is assembled only from sealed `_G1_VIRAL_002` P013 raw OCR text.",
        "",
        "| Candidate | Similarity | Token recall | Diagnostic threshold met | Similarity delta | Token recall delta |",
        "|---|---:|---:|---|---:|---:|",
    ]
    for result in results:
        summary_lines.append(
            f"| `{result['candidate_id']}` | `{result['metrics']['sequence_similarity_ratio']}` | "
            f"`{result['metrics']['token_recall']}` | `{result['diagnostic_threshold_met']}` | "
            f"`{result['metric_deltas_from_source']['sequence_similarity_delta']}` | "
            f"`{result['metric_deltas_from_source']['token_recall_delta']}` |"
        )
    summary_lines.extend(
        [
            "",
            "Boundary: diagnostic-only assembly repair; no reference-guided token insertion, no accepted/semantic/page-status/source mutation, no production output, no page 021+, no push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "p013_seam_dedupe_diagnostic_summary.md", "\n".join(summary_lines))
    manifest_lines = [
        "# P013 Seam Dedupe Diagnostic Manifest - C01TEP013SDD-G1-VIRAL-001",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "p013_seam_dedupe_diagnostic_manifest.md":
            manifest_lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    manifest_lines.append("")
    write_text(OUT_ROOT / "p013_seam_dedupe_diagnostic_manifest.md", "\n".join(manifest_lines))


if __name__ == "__main__":
    check_authorization()
    build()
