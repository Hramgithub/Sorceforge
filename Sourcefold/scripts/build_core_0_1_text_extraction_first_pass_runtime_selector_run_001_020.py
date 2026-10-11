from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
from pathlib import Path
from typing import Any

import run_core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4 as overview


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = overview.TRIAL_ROOT
AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_first_pass_runtime_selector_authorization_001_020_G1_VIRAL_001"
ASSEMBLY_AUTH_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_assembly_authorization_001_020_G1_VIRAL_001"
READINESS_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001"
BRIDGE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_eligibility_bridge_001_020_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_first_pass_runtime_selector_run_001_020_G1_VIRAL_001"
LEDGER = overview.LEDGER

LANE_ID = "C01TEFPSRUN020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FIRST-PASS-RUNTIME-SELECTOR-RUN-001-020-001"
HUMAN_DECISION = "Давай уже реально поработаем"

REQUESTED_PAGES = [f"{page:03d}" for page in range(1, 21)]
FRESH_BASELINE_PAGES = {"009", "010", "011", "015"}
BRIDGE_PAGES = {"001", "002", "003", "004", "005", "006", "007", "008", "014", "019"}
RUNTIME_SELECTED_PAGES = ["009", "010", "011", "012", "013", "015", "016", "017", "018", "020"]

INPUT_HASHES = {
    "C01TEFPSAUTH020-G1-VIRAL-001.report": (
        AUTH_ROOT / "first_pass_runtime_selector_authorization_001_020_report.json",
        "40A0D2607B4CA2861B54ECA7E2A41742AAE1E7EAA618631F0EC08F2A335F16FF",
    ),
    "C01TEFPSAUTH020-G1-VIRAL-001.summary": (
        AUTH_ROOT / "first_pass_runtime_selector_authorization_001_020_summary.md",
        "C2C5867A96DFEC30004C8AF7211CCE0B400079C5B1D5CAA2450924D9FF096E0B",
    ),
    "C01TEFPSAUTH020-G1-VIRAL-001.manifest": (
        AUTH_ROOT / "first_pass_runtime_selector_authorization_001_020_manifest.md",
        "6A5D2F992E8DCCCE5C3596990815CC894F9B90E130E4FB505D22AD83E89844DF",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.selector_v4": (
        BRIDGE_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json",
        "A94BFC2D22AFDDB870FE93CC6A8308F96A56EA516507EA8B7CBF067414D1DCCC",
    ),
    "C01TEBRIDGE020-G1-VIRAL-001.bridge_entries": (
        BRIDGE_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json",
        "D9557AD7A8C38383D13AF7373BED7E97ADCB48AE42B27EFF78F3CFCA8B18A231",
    ),
    "C01TEASM020-G1-VIRAL-001.selected_pages_manifest": (
        READINESS_ROOT / "assembly_manifest" / "selected_pages_manifest.json",
        "090352D6B97AABA628CEE692F67E1305C896D0723C8214579AE4469CF1850DE9",
    ),
    "C01TEAUTH020-G1-VIRAL-001.report": (
        ASSEMBLY_AUTH_ROOT / "assembly_authorization_001_020_report.json",
        "CE668EF259DF00A4BB062259279EFE3ED2C367F3CB67E58ACC9BADB29F106429",
    ),
    "C01TEAUTH020-G1-VIRAL-001.manifest": (
        ASSEMBLY_AUTH_ROOT / "assembly_authorization_001_020_manifest.md",
        "F3B26C015D1A043DD5201DA4A22B9C9E426AEB3B4572A3C1EDE189FFEED55765",
    ),
}

SELECTED_CANDIDATE_SOURCES = {
    "012": TRIAL_ROOT
    / "core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001"
    / "candidate_texts"
    / "p012_full_columns_scale2_psm6"
    / "page_012_candidate.md",
    "013": TRIAL_ROOT
    / "core_0_1_text_extraction_p013_structural_assembly_closure_diagnostic_G1_VIRAL_001"
    / "candidate_texts"
    / "p013_sac_d_noise_then_declared_seam_fracture"
    / "page_013_candidate.md",
    "016": TRIAL_ROOT
    / "core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001"
    / "candidate_texts"
    / "p016_expanded_bottom_conf60_scale2_psm6"
    / "page_016_candidate.md",
    "017": TRIAL_ROOT
    / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002"
    / "candidate_texts"
    / "full_page_bright_title_body_psm7_4_4"
    / "page_017_candidate.md",
    "018": TRIAL_ROOT
    / "core_0_1_text_extraction_geometry_probe_012_013_016_017_018_020_G1_VIRAL_002"
    / "candidate_texts"
    / "full_page_expanded_overlap_psm4"
    / "page_018_candidate.md",
    "020": TRIAL_ROOT
    / "core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001"
    / "candidate_texts"
    / "p020_table_normalized_scale2_threshold180_psm6"
    / "page_020_candidate.md",
}

NEGATIVE_CAPABILITIES = [
    "source_mutation",
    "raw_mutation",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "fixture_admission",
    "whole_gate_1_acceptance",
    "page_021_plus_processing",
    "translation",
    "proofreading",
    "push",
    "downstream_execution",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Materialize bounded first-pass runtime selector output surface for 001-020.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("first-pass runtime selector run is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"first-pass runtime selector run requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("first-pass runtime selector run requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if "Status: `first_pass_runtime_selector_authorization_recorded_report_only`" not in ledger:
        raise SystemExit("predecessor route authorization is not synced in ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}
    auth_report = read_json(AUTH_ROOT / "first_pass_runtime_selector_authorization_001_020_report.json")
    selector_v4 = read_json(BRIDGE_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json")
    if auth_report["fresh_first_pass_runtime_selector_route_authorized"] is not True:
        raise SystemExit("runtime selector route is not authorized")
    if auth_report["requested_pages"] != REQUESTED_PAGES:
        raise SystemExit("authorized page set drifted")
    if [item["page"] for item in selector_v4] != REQUESTED_PAGES:
        raise SystemExit("selector v4 page set drifted")
    return verified, auth_report, selector_v4


def selected_hashes(item: dict) -> dict[str, str]:
    hashes = item.get("selected_output_hashes")
    if isinstance(hashes, dict):
        return hashes
    return {}


def write_baseline_page(page: str, selector_item: dict, scratch_root: Path) -> dict:
    expected_hash = selected_hashes(selector_item)["candidate_text_sha256"]
    assets = TRIAL_ROOT / overview.PAGE_DIRS[page] / "review_assets"
    chunks = []
    for path in overview.crop_paths_for_page(page, assets):
        id_ = overview.input_id(path)
        ocr_text, _ = overview.run_tesseract(path, id_, 4, scratch_root / f"p{page}")
        chunks.append(f"## {id_}\n\n{ocr_text.strip()}")
    text = "\n\n".join(chunks).strip() + "\n"
    actual_hash = sha256_text(text)
    if actual_hash != expected_hash:
        raise SystemExit(f"P{page} fresh baseline hash mismatch: {actual_hash}")
    out_path = OUT_ROOT / "pages" / f"page_{page}_selected_text.md"
    write_text(out_path, text)
    return {
        "page": page,
        "materialization_mode": "fresh_baseline_ocr_execution",
        "selector_decision": selector_item["selector_decision"],
        "source_lane_id": selector_item["source_lane_id"],
        "output_path": out_path.relative_to(ROOT).as_posix(),
        "output_sha256": sha256_file(out_path),
        "fresh_ocr_execution": True,
        "runtime_selected_page": True,
        "bridge_lineage": False,
        "selected_candidate_text_hash_matched": True,
        "metrics": selector_item.get("metrics"),
    }


def write_candidate_page(page: str, selector_item: dict) -> dict:
    source = SELECTED_CANDIDATE_SOURCES[page]
    expected_hash = selected_hashes(selector_item)["candidate_text_sha256"]
    actual_hash = sha256_file(source)
    if actual_hash != expected_hash:
        raise SystemExit(f"P{page} selected candidate hash mismatch: {actual_hash}")
    out_path = OUT_ROOT / "pages" / f"page_{page}_selected_text.md"
    write_text(out_path, source.read_text(encoding="utf-8-sig"))
    return {
        "page": page,
        "materialization_mode": "hash_pinned_selected_candidate_materialized",
        "selector_decision": selector_item["selector_decision"],
        "source_lane_id": selector_item["source_lane_id"],
        "selected_candidate_id": selector_item.get("selected_candidate_id"),
        "source_path": source.relative_to(ROOT).as_posix(),
        "source_sha256": actual_hash,
        "output_path": out_path.relative_to(ROOT).as_posix(),
        "output_sha256": sha256_file(out_path),
        "fresh_ocr_execution": False,
        "runtime_selected_page": True,
        "bridge_lineage": False,
        "selected_candidate_text_hash_matched": True,
        "metrics": selector_item.get("metrics"),
    }


def write_bridge_page(page: str, selector_item: dict) -> dict:
    report_path = ROOT / selector_item["acceptance_report_path"]
    expected_hash = selector_item["acceptance_report_sha256"]
    actual_hash = sha256_file(report_path)
    if actual_hash != expected_hash:
        raise SystemExit(f"P{page} bridge acceptance hash mismatch: {actual_hash}")
    out_path = OUT_ROOT / "pages" / f"page_{page}_bridge_lineage.md"
    text = "\n".join(
        [
            f"# Page {page} Bridge Lineage",
            "",
            "This page is materialized through prior page-complete acceptance bridge lineage.",
            "It is not a fresh OCR runtime-selector success for this lane.",
            "",
            f"- Source lane: `{selector_item['source_lane_id']}`",
            f"- Method entry: `{selector_item['method_entry_id']}`",
            f"- Acceptance report: `{selector_item['acceptance_report_path']}`",
            f"- Acceptance report SHA-256: `{actual_hash}`",
            "",
        ]
    )
    write_text(out_path, text)
    return {
        "page": page,
        "materialization_mode": "page_complete_acceptance_bridge_lineage_record",
        "selector_decision": selector_item["selector_decision"],
        "source_lane_id": selector_item["source_lane_id"],
        "acceptance_report_path": selector_item["acceptance_report_path"],
        "acceptance_report_sha256": actual_hash,
        "output_path": out_path.relative_to(ROOT).as_posix(),
        "output_sha256": sha256_file(out_path),
        "fresh_ocr_execution": False,
        "runtime_selected_page": False,
        "bridge_lineage": True,
        "selected_candidate_text_hash_matched": None,
    }


def materialize_page(selector_item: dict, scratch_root: Path) -> dict:
    page = selector_item["page"]
    if page not in REQUESTED_PAGES:
        raise SystemExit(f"page outside lane: {page}")
    if page in BRIDGE_PAGES:
        return write_bridge_page(page, selector_item)
    if page in FRESH_BASELINE_PAGES:
        return write_baseline_page(page, selector_item, scratch_root)
    return write_candidate_page(page, selector_item)


def output_hashes() -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file():
            hashes[path.relative_to(OUT_ROOT).as_posix()] = {
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
    return hashes


def build_report(verified_inputs: dict[str, dict[str, str]], page_results: list[dict]) -> dict:
    bridge_pages = [item["page"] for item in page_results if item["bridge_lineage"]]
    fresh_ocr_execution_pages = [item["page"] for item in page_results if item["fresh_ocr_execution"]]
    runtime_selected_pages = [item["page"] for item in page_results if item["runtime_selected_page"]]
    candidate_materialized_pages = [
        item["page"] for item in page_results if item["materialization_mode"] == "hash_pinned_selected_candidate_materialized"
    ]
    return {
        "lane_id": LANE_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "first_pass_runtime_selector_output_surface_materialized_with_bridge_lineage",
        "human_decision": HUMAN_DECISION,
        "requested_pages": REQUESTED_PAGES,
        "materialized_pages": [item["page"] for item in page_results],
        "all_pages_materialized": [item["page"] for item in page_results] == REQUESTED_PAGES,
        "fresh_ocr_runtime_pages": runtime_selected_pages,
        "fresh_ocr_execution_pages": fresh_ocr_execution_pages,
        "candidate_materialized_pages": candidate_materialized_pages,
        "bridge_lineage_pages": bridge_pages,
        "all_pages_fresh_ocr_success": False,
        "runtime_execution_performed": True,
        "runtime_output_surface_created": True,
        "production_ready": False,
        "production_assembly_authorized": False,
        "acceptance_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "fixture_admission_performed": False,
        "whole_gate_1_acceptance_performed": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
        "page_results": page_results,
    }


def write_summary(report: dict) -> None:
    lines = [
        "# First-Pass Runtime Selector Run 001-020 - C01TEFPSRUN020-G1-VIRAL-001",
        "",
        "Status: `first_pass_runtime_selector_output_surface_materialized_with_bridge_lineage`",
        "",
        f"All pages materialized: `{str(report['all_pages_materialized']).lower()}`.",
        f"All pages fresh OCR success: `{str(report['all_pages_fresh_ocr_success']).lower()}`.",
        f"Runtime execution performed: `{str(report['runtime_execution_performed']).lower()}`.",
        f"Runtime output surface created: `{str(report['runtime_output_surface_created']).lower()}`.",
        f"Production ready: `{str(report['production_ready']).lower()}`.",
        "",
        "## Page Modes",
        "",
        "| Page | Mode | Output |",
        "|---|---|---|",
    ]
    for item in report["page_results"]:
        lines.append(f"| `{item['page']}` | `{item['materialization_mode']}` | `{item['output_path']}` |")
    lines.extend(
        [
            "",
            "Bridge lineage pages are not counted as fresh OCR runtime-selector success.",
            "",
            "## Boundary Flags",
            "",
            "- `accepted_text_mutation_performed=false`.",
            "- `semantic_text_mutation_performed=false`.",
            "- `page_status_mutation_performed=false`.",
            "- `source_or_raw_mutation_performed=false`.",
            "- `fixture_admission_performed=false`.",
            "- `whole_gate_1_acceptance_performed=false`.",
            "- `page_021_plus_included=false`.",
            "",
        ]
    )
    write_text(OUT_ROOT / "first_pass_runtime_selector_run_001_020_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# First-Pass Runtime Selector Run 001-020 Manifest - C01TEFPSRUN020-G1-VIRAL-001",
        "",
        "Boundary: clean output surface only; no source/raw/accepted/page-status mutation, no fixture admission, no page 021+.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, item in output_hashes().items():
        if rel_path != "first_pass_runtime_selector_run_001_020_manifest.md":
            lines.append(f"| `{rel_path}` | `{item['sha256']}` |")
    lines.append("")
    write_text(OUT_ROOT / "first_pass_runtime_selector_run_001_020_manifest.md", "\n".join(lines))


def build() -> None:
    verified_inputs, _auth_report, selector_v4 = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="sourcefold_fpsrun020_") as scratch:
        page_results = [materialize_page(item, Path(scratch)) for item in selector_v4]
    report = build_report(verified_inputs, page_results)
    write_json(OUT_ROOT / "first_pass_runtime_selector_run_001_020_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
