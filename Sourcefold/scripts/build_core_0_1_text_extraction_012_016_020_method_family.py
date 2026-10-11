from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps

from ocr_input_surface_policy import validate_ocr_input_surface
import run_core_0_1_text_extraction_full_page_geometry_probe_p018_p017 as fg
import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
UNRES_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_unresolved_pages_method_discovery_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001"
LEDGER = overview.LEDGER
TESSERACT = overview.TESSERACT

LANE_ID = "C01TEMF012016020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-012-016-020-METHOD-FAMILY-001"
HUMAN_DECISION = "ок, комит и делай 12,16,20 что планировал"
PAGES = ["012", "016", "020"]
EXPECTED_SELECTED_PAGES_V3 = ["009", "010", "011", "012", "013", "015", "016", "017", "018", "020"]
OK_SIMILARITY = 0.997
OK_TOKEN_RECALL = 0.993

INPUT_HASHES = {
    "C01TEUNRES020-G1-VIRAL-001.report": (
        UNRES_ROOT / "unresolved_pages_method_discovery_report.json",
        "06FF3C64CA67F5259A1AC063A7FE34C10527280AB58B07C215B848357609DDF5",
    ),
    "C01TEUNRES020-G1-VIRAL-001.selector_v2": (
        UNRES_ROOT / "selector_replay_v2" / "selector_replay_v2_selections.json",
        "801F6B67141C8CFC15A19FEFA17C94585CF70255FB875FD6DA702E9E4E0066DA",
    ),
    "C01TEUNRES020-G1-VIRAL-001.page_017_entry": (
        UNRES_ROOT / "method_registry_entries" / "page_017.json",
        "6EAD1FC9B97F19C005D06B586F90B76A4582DCE7A9BA51ED436710A0A84719A8",
    ),
    "C01TEUNRES020-G1-VIRAL-001.page_018_entry": (
        UNRES_ROOT / "method_registry_entries" / "page_018.json",
        "03FC0EE1BEE6676510387B1B3DDDE9E58306817917975841AC69640DA4CE46F8",
    ),
    "p012_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["012"] / "review_assets" / "page_012.png",
        "D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6",
    ),
    "p016_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["016"] / "review_assets" / "page_016.png",
        "7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56",
    ),
    "p020_full_page_png": (
        TRIAL_ROOT / overview.PAGE_DIRS["020"] / "review_assets" / "page_020.png",
        "53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E",
    ),
    "p012_triage_packet": (
        TRIAL_ROOT / "page_012_triage_G1_VIRAL_001" / "page_012_triage_packet.json",
        "93A2CCE7F4F639BFC10CAA33840FB587491FCA89827188ECDD53586B8E6A4689",
    ),
    "p016_triage_report": (
        TRIAL_ROOT / "page_016_triage_G1_VIRAL_001" / "page_016_triage_report.json",
        "C98349F2ED24682CCBFDD3E3F9FAFE6A4EF291FBAF5B7FA09590E25B94B2E115",
    ),
    "p020_triage_report": (
        TRIAL_ROOT / "page_020_triage_G1_VIRAL_001" / "page_020_triage_report.json",
        "92B446992A502D4DC607B9787E9A69CB13B26C1AA193F43B2C075E76F097F2F3",
    ),
}

NEGATIVE_CAPABILITIES = [
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "reference_guided_repair",
    "reference_token_insertion",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "source_mutation",
    "raw_mutation",
    "selector_runtime_enablement",
    "runtime_selector_integration",
    "runtime_execution",
    "production_assembly",
    "clean_production_output_folder",
    "page_021_plus_processing",
    "translation",
    "proofreading",
    "push",
    "promotion",
    "acceptance",
    "downstream_execution",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build P012/P016/P020 method-family OCR candidates.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("P012/P016/P020 method-family lane is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"P012/P016/P020 method-family lane requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("P012/P016/P020 method-family lane requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if not TESSERACT.exists():
        raise SystemExit(f"missing OCR executable: {TESSERACT}")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    unres_report = read_json(UNRES_ROOT / "unresolved_pages_method_discovery_report.json")
    selector_v2 = read_json(UNRES_ROOT / "selector_replay_v2" / "selector_replay_v2_selections.json")
    if unres_report["still_unresolved_pages"] != PAGES:
        raise SystemExit(f"unexpected unresolved input pages: {unres_report['still_unresolved_pages']}")
    if unres_report["production_ready"] is not False:
        raise SystemExit("unexpected production-ready input")
    return verified, unres_report, selector_v2


def page_image(page: str) -> tuple[Path, Image.Image]:
    path = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets" / f"page_{page}.png"
    return path, Image.open(path).convert("RGB")


def reference_for_page(page: str) -> tuple[str, Path, str]:
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    reference = overview.reference_for_page(page, assets)
    if reference is None:
        raise SystemExit(f"P{page} missing reference")
    label, path = reference
    return label, path, overview.extract_reference_text(path)


def ocr_surface(page: str, image_path: Path, image_sha256: str, region_id: str, box: tuple[int, int, int, int], prepared: Path, profile: str, psm: int) -> dict:
    return {
        "surface_class": "full_page_region",
        "artifact_role": "ocr_candidate_full_page_region",
        "ocr_allowed": True,
        "source_artifact": {
            "path": image_path.relative_to(ROOT).as_posix(),
            "sha256": image_sha256,
            "hash_status": "matched",
        },
        "page_id": f"P{page}",
        "regions": [
            {
                "region_id": region_id,
                "page_space_box": list(box),
                "prepared_region_path": prepared.relative_to(ROOT).as_posix(),
            }
        ],
        "preprocessing_profile": profile,
        "ocr_engine_profile": {"engine": "tesseract", "profile": f"eng_oem1_psm{psm}"},
        "allowed_purpose": "candidate_policy",
        "reference_policy": "scorer_only_after_candidate_hash",
        "authorization": {
            "full_page_region_authorization_id": AUTHORIZATION_ID,
            "page_family": "remaining_unresolved_012_016_020_method_family",
            "region_policy": "full_page_derived_page_space_regions",
            "negative_reason_not_baseline": "prior_selector_replay_unresolved_needs_method_winner",
        },
        "reference_loaded_before_candidate_hash": False,
    }


def prepare_region(source: Image.Image, box: tuple[int, int, int, int], *, scale: int = 2, threshold: int | None = None) -> Image.Image:
    crop = source.crop(box).convert("RGB")
    if scale != 1:
        crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    gray = ImageOps.autocontrast(ImageOps.grayscale(crop))
    if threshold is not None:
        gray = gray.point(lambda px: 0 if px < threshold else 255)
    return ImageOps.expand(gray.convert("RGB"), border=40, fill="white")


def run_tesseract(prepared: Path, base: Path, psm: int) -> tuple[str, list[dict], dict[str, str]]:
    command = [str(TESSERACT), str(prepared), str(base), "-l", "eng", "--oem", "1", "--psm", str(psm), "txt", "tsv"]
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if completed.returncode != 0:
        raise SystemExit(completed.stderr or completed.stdout)
    text_path = base.with_suffix(".txt")
    tsv_path = base.with_suffix(".tsv")
    stderr_path = base.with_suffix(".stderr.txt")
    stdout_path = base.with_suffix(".stdout.txt")
    write_text(stderr_path, completed.stderr)
    write_text(stdout_path, completed.stdout)
    rows: list[dict] = []
    with tsv_path.open(encoding="utf-8", errors="replace", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row.get("text", "").strip():
                rows.append(row)
    return text_path.read_text(encoding="utf-8", errors="replace"), rows, {
        "prepared_region_path": prepared.relative_to(ROOT).as_posix(),
        "prepared_region_sha256": sha256_file(prepared),
        "raw_ocr_text_path": text_path.relative_to(ROOT).as_posix(),
        "raw_ocr_text_sha256": sha256_file(text_path),
        "raw_ocr_tsv_path": tsv_path.relative_to(ROOT).as_posix(),
        "raw_ocr_tsv_sha256": sha256_file(tsv_path),
        "stderr_path": stderr_path.relative_to(ROOT).as_posix(),
        "stdout_path": stdout_path.relative_to(ROOT).as_posix(),
    }


def confidence_filter_text(rows: list[dict], min_confidence: float) -> str:
    lines: list[str] = []
    current: list[str] = []
    last_key = None
    for row in rows:
        try:
            confidence = float(row.get("conf", "-1"))
        except ValueError:
            confidence = -1
        if confidence < min_confidence:
            continue
        key = (row.get("block_num"), row.get("par_num"), row.get("line_num"))
        if last_key is not None and key != last_key and current:
            lines.append(" ".join(current))
            current = []
        current.append(row["text"].strip())
        last_key = key
    if current:
        lines.append(" ".join(current))
    return "\n".join(lines)


def normalize_p020_table(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.fullmatch(r"Roll\s+Rumou?r", stripped, flags=re.IGNORECASE):
            continue
        stripped = re.sub(r"^(\d)\s+__\s+", r"Roll \1: ", stripped)
        stripped = re.sub(r"^(\d)\s+", r"Roll \1: ", stripped)
        lines.append(stripped)
    return "\n".join(lines)


def candidate_specs() -> dict[str, dict[str, Any]]:
    return {
        "012": {
            "candidate_id": "p012_full_columns_scale2_psm6",
            "description": "Full-column scale2 PSM6 OCR over left and right text columns.",
            "psm": 6,
            "scale": 2,
            "regions": [
                {"id": "left_column", "box": (170, 210, 1250, 3160), "postprocess": "raw_text"},
                {"id": "right_column", "box": (1285, 210, 2405, 3150), "postprocess": "raw_text"},
            ],
        },
        "016": {
            "candidate_id": "p016_expanded_bottom_conf60_scale2_psm6",
            "description": "Expanded bottom geometry plus TSV confidence filtering at 60.",
            "psm": 6,
            "scale": 2,
            "regions": [
                {"id": "history_continuation", "box": (186, 146, 1274, 1514), "postprocess": "confidence_60"},
                {"id": "left_keeper_notes", "box": (191, 1466, 1264, 3024), "postprocess": "confidence_60"},
                {"id": "right_keeper_notes", "box": (1296, 206, 2354, 1144), "postprocess": "confidence_60"},
                {"id": "history_late_reports_expanded", "box": (1286, 1116, 2374, 3114), "postprocess": "confidence_60"},
            ],
        },
        "020": {
            "candidate_id": "p020_table_normalized_scale2_threshold180_psm6",
            "description": "Scale2 threshold-180 PSM6 OCR plus source-derived Roll/Rumor table normalization.",
            "psm": 6,
            "scale": 2,
            "threshold": 180,
            "regions": [
                {"id": "left_column_perla_exploration", "box": (186, 186, 1274, 3034), "postprocess": "raw_text"},
                {"id": "exploring_and_rumors", "box": (1286, 186, 2379, 3044), "postprocess": "p020_table_normalization"},
            ],
        },
    }


def postprocess_text(text: str, rows: list[dict], mode: str) -> str:
    if mode == "raw_text":
        return text.strip()
    if mode == "confidence_60":
        return confidence_filter_text(rows, 60).strip()
    if mode == "p020_table_normalization":
        return normalize_p020_table(text).strip()
    raise SystemExit(f"unknown postprocess mode: {mode}")


def generate_candidate(page: str, spec: dict[str, Any]) -> dict[str, Any]:
    image_path, source = page_image(page)
    image_sha256 = sha256_file(image_path)
    chunks: list[str] = []
    region_results: list[dict[str, Any]] = []
    for index, region in enumerate(spec["regions"], start=1):
        prepared = OUT_ROOT / "prepared_regions" / spec["candidate_id"] / f"p{page}" / f"{index:02d}_{region['id']}.png"
        base = OUT_ROOT / "raw_ocr" / spec["candidate_id"] / f"p{page}" / f"{index:02d}_{region['id']}"
        prepared.parent.mkdir(parents=True, exist_ok=True)
        base.parent.mkdir(parents=True, exist_ok=True)
        prepare_region(source, region["box"], scale=spec["scale"], threshold=spec.get("threshold")).save(prepared)
        surface = ocr_surface(page, image_path, image_sha256, region["id"], region["box"], prepared, spec["candidate_id"], spec["psm"])
        validation = validate_ocr_input_surface(surface)
        if validation["status"] != "passed":
            raise SystemExit(f"ocr input surface validation failed: {validation['findings']}")
        text, rows, ocr_result = run_tesseract(prepared, base, spec["psm"])
        chunks.append(f"## {region['id']}\n\n{postprocess_text(text, rows, region['postprocess'])}")
        region_results.append(
            {
                "region_id": region["id"],
                "page_space_box": list(region["box"]),
                "psm": spec["psm"],
                "scale": spec["scale"],
                "threshold": spec.get("threshold"),
                "postprocess": region["postprocess"],
                "ocr_input_surface": surface,
                "ocr_input_surface_validation": validation,
                "ocr_result": ocr_result,
            }
        )
    candidate_text = "\n\n".join(chunks).strip() + "\n"
    candidate_path = OUT_ROOT / "candidate_texts" / spec["candidate_id"] / f"page_{page}_candidate.md"
    write_text(candidate_path, candidate_text)
    return {
        "page": page,
        "candidate_id": spec["candidate_id"],
        "description": spec["description"],
        "source_page_image_path": image_path.relative_to(ROOT).as_posix(),
        "source_page_image_sha256": image_sha256,
        "candidate_text_path": candidate_path.relative_to(ROOT).as_posix(),
        "candidate_text_sha256": sha256_file(candidate_path),
        "region_results": region_results,
    }


def score_candidate(result: dict[str, Any]) -> dict[str, Any]:
    label, reference_path, reference_text = reference_for_page(result["page"])
    candidate_text = (ROOT / result["candidate_text_path"]).read_text(encoding="utf-8-sig")
    metrics = fg.metrics(candidate_text, reference_text)
    result["reference_label"] = label
    result["reference_path"] = reference_path.relative_to(ROOT).as_posix()
    result["reference_sha256"] = sha256_file(reference_path)
    result["reference_risk_flag"] = label != "reference_ocr_verified_text_map"
    result["metrics"] = metrics
    result["diagnostic_threshold_met"] = (
        metrics["sequence_similarity_ratio"] >= OK_SIMILARITY and metrics["token_recall"] >= OK_TOKEN_RECALL
    )
    return result


def build_entry(result: dict[str, Any]) -> dict[str, Any]:
    page = result["page"]
    return {
        "entry_id": f"{LANE_ID}-P{page}",
        "discovery_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "page": page,
        "status": "method_discovered_not_runtime",
        "selected_candidate_id": result["candidate_id"],
        "selection_rule": "fixed_method_family_candidate_threshold_then_page_specific_tie_break",
        "metrics": result["metrics"],
        "reference_dependency": {
            "label": result["reference_label"],
            "path": result["reference_path"],
            "sha256": result["reference_sha256"],
            "note": "scored_after_candidate_hash_seal_reference_not_used_for_token_insertion",
        },
        "artifact_hashes": {
            "candidate_text_sha256": result["candidate_text_sha256"],
            "normalized_candidate_sha256": result["metrics"]["candidate_normalized_sha256"],
            "source_page_image_sha256": result["source_page_image_sha256"],
        },
        "selector_rule_created": False,
        "selector_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
    }


def selected_selection(entry: dict) -> dict:
    return {
        "page": entry["page"],
        "selector_decision": "selected_012_016_020_method_family_candidate",
        "selection_status": "selected_static_evidence_only",
        "source_lane_id": entry["discovery_id"],
        "method_entry_id": entry["entry_id"],
        "selected_candidate_id": entry["selected_candidate_id"],
        "selected_output_hashes": entry["artifact_hashes"],
        "metrics": entry["metrics"],
        "reference_label": entry["reference_dependency"]["label"],
        "reference_dependency": entry["reference_dependency"],
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def selector_v3(selector_v2: list[dict], entries: list[dict]) -> list[dict]:
    entry_by_page = {entry["page"]: entry for entry in entries}
    selections: list[dict] = []
    for item in selector_v2:
        if item["page"] in entry_by_page:
            selections.append(selected_selection(entry_by_page[item["page"]]))
        else:
            selections.append(item)
    return selections


def summarize_groups(selections: list[dict]) -> dict[str, list[str]]:
    groups = {
        "not_run_ineligible": [],
        "selected_frozen_baseline": [],
        "selected_p013_discovered_candidate": [],
        "selected_unresolved_pages_discovered_candidate": [],
        "selected_012_016_020_method_family_candidate": [],
        "parked_candidate_policy": [],
    }
    for item in selections:
        decision = item["selector_decision"]
        if decision == "unresolved_needs_method_winner":
            raise SystemExit(f"selector v3 left unresolved page: {item['page']}")
        if decision not in groups:
            raise SystemExit(f"unexpected selector decision: {decision}")
        groups[decision].append(item["page"])
    return groups


def build_report(verified_inputs: dict, results: list[dict], entries: list[dict], selections: list[dict]) -> dict:
    selected_pages = [item["page"] for item in selections if item["selection_status"] == "selected_static_evidence_only"]
    if selected_pages != EXPECTED_SELECTED_PAGES_V3:
        raise SystemExit(f"unexpected selected pages v3: {selected_pages}")
    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "method_family_candidates_selected_static_evidence_only",
        "human_decision": HUMAN_DECISION,
        "input_unresolved_pages": PAGES,
        "candidate_count": len(results),
        "selected_pages": [entry["page"] for entry in entries],
        "still_unresolved_pages": [],
        "selected_pages_v3": selected_pages,
        "production_ready": False,
        "all_pages_first_pass_success": False,
        "candidate_generation_reference_text_used": False,
        "reference_text_loaded_after_candidate_hashing": True,
        "reference_token_insertion_performed": False,
        "method_candidates": results,
        "method_registry_entries": entries,
        "selector_replay_v3": {
            "scope": "static_001_020_selector_replay_v3_from_method_family_entries",
            "requested_pages": [f"{page:03d}" for page in range(1, 21)],
            "groups": summarize_groups(selections),
            "failed_or_superseded_candidates_selected": False,
            "candidate_text_copied": False,
            "production_assembly_created": False,
            "clean_production_output_folder_created": False,
            "page_021_plus_included": False,
        },
        "selections": selections,
        "verified_inputs": verified_inputs,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "ocr_execution_performed": True,
        "ocr_execution_scope": "bounded_candidate_generation_for_pages_012_016_020_only",
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "reference_guided_repair_used": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "selector_runtime_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "clean_production_output_folder_created": False,
        "page_001_020_runtime_loop_created": False,
        "page_021_plus_included": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
    }


def write_summary(report: dict) -> None:
    lines = [
        "# P012/P016/P020 Method Family - C01TEMF012016020-G1-VIRAL-001",
        "",
        "Status: `method_family_candidates_selected_static_evidence_only`",
        "",
        "This dry-run generates bounded OCR candidates for pages `012`, `016`, and `020`, seals candidate hashes before reference scoring, and records static method entries for selector replay v3.",
        "",
        f"Selected pages v3: `{', '.join(report['selected_pages_v3'])}`.",
        f"Production ready: `{str(report['production_ready']).lower()}`.",
        f"All pages first-pass success: `{str(report['all_pages_first_pass_success']).lower()}`.",
        "",
        "| Page | Entry | Candidate | Similarity | Token recall |",
        "|---|---|---|---:|---:|",
    ]
    for entry in report["method_registry_entries"]:
        metrics = entry["metrics"]
        lines.append(
            f"| `{entry['page']}` | `{entry['entry_id']}` | `{entry['selected_candidate_id']}` | "
            f"`{metrics['sequence_similarity_ratio']}` | `{metrics['token_recall']}` |"
        )
    lines.extend(
        [
            "",
            "## Boundary Flags",
            "",
            "- `ocr_execution_performed=true` and scoped only to pages `012`, `016`, `020` candidate generation.",
            "- `candidate_generation_reference_text_used=false`.",
            "- `reference_text_loaded_after_candidate_hashing=true`.",
            "- `reference_token_insertion_performed=false`.",
            "- `production_assembly_created=false`.",
            "- `accepted_text_mutation_performed=false`.",
            "- `semantic_text_mutation_performed=false`.",
            "- `page_status_mutation_performed=false`.",
            "- `source_or_raw_mutation_performed=false`.",
            "- `page_021_plus_included=false`.",
            "- `promotion_performed=false`.",
            "- `acceptance_performed=false`.",
            "- `downstream_execution_performed=false`.",
            "",
        ]
    )
    write_text(OUT_ROOT / "012_016_020_method_family_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# P012/P016/P020 Method Family Manifest - C01TEMF012016020-G1-VIRAL-001",
        "",
        "Boundary: candidate OCR method-family evidence and selector replay v3 only; no production assembly.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "012_016_020_method_family_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / "012_016_020_method_family_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, _unres_report, selector_v2 = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)

    specs = candidate_specs()
    results = [score_candidate(generate_candidate(page, specs[page])) for page in PAGES]
    if not all(result["diagnostic_threshold_met"] for result in results):
        failed = [result["page"] for result in results if not result["diagnostic_threshold_met"]]
        raise SystemExit(f"method-family candidates did not meet threshold: {failed}")
    entries = [build_entry(result) for result in results]
    selections = selector_v3(selector_v2, entries)
    report = build_report(verified_inputs, results, entries, selections)

    for entry in entries:
        write_json(OUT_ROOT / "method_registry_entries" / f"page_{entry['page']}.json", entry)
    write_json(OUT_ROOT / "selector_replay_v3" / "selector_replay_v3_selections.json", selections)
    write_json(OUT_ROOT / "012_016_020_method_family_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
