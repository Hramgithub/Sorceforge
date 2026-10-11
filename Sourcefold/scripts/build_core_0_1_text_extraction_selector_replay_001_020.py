from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OVERVIEW_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_overview_replay_001_020_trim_mask_psm4_G1_VIRAL_001"
MRS_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_p013_method_registry_selector_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_selector_replay_001_020_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

REPLAY_ID = "C01TESEL020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-SELECTOR-REPLAY-001-020-001"
HUMAN_DECISION = "делай"
P013_ENTRY_ID = "C01TEP013MRS-G1-VIRAL-001-P013"

INPUT_HASHES = {
    "C01TEOR020-G1-VIRAL-001.report": (
        OVERVIEW_ROOT / "overview_replay_report.json",
        "7FE37ECD8BAB5EAC4C9557C244D0E2CA618704783E6CFC9D706CFB60B46E0357",
    ),
    "C01TEOR020-G1-VIRAL-001.summary": (
        OVERVIEW_ROOT / "overview_replay_summary.md",
        "EAFF1725179931084A4DA03625C52CBE1AA0C55896D54237615280EC45A81E58",
    ),
    "C01TEP013MRS-G1-VIRAL-001.entry": (
        MRS_ROOT / "method_registry_entries" / "page_013.json",
        "B09BF185510557CDAF3E757D381A416E2DEE52A8430B93E8293A348ACD6A56EC",
    ),
    "C01TEP013MRS-G1-VIRAL-001.report": (
        MRS_ROOT / "p013_method_registry_selector_report.json",
        "988FA33843EE0E35F70562E227BE7FA613CD7715982AC5FEA4BE4D3F9847B520",
    ),
    "C01TEP013MRS-G1-VIRAL-001.manifest": (
        MRS_ROOT / "p013_method_registry_selector_manifest.md",
        "D0183C59E85C8109962B8CE9A3605660FA1D555994958CB6492B106D1DCD8B6E",
    ),
}

EXPECTED_GROUPS = {
    "not_run_ineligible": ["001", "002", "003", "004", "005", "006", "007", "008"],
    "selected_frozen_baseline": ["009", "010", "011", "015"],
    "selected_p013_mrs": ["013"],
    "unresolved_needs_method_winner": ["012", "016", "017", "018", "020"],
    "parked_candidate_policy": ["014", "019"],
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "reference_guided_repair",
    "reference_token_insertion",
    "text_token_mutation",
    "source_mutation",
    "raw_mutation",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
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
    parser = argparse.ArgumentParser(description="Build static 001-020 selector replay report.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("001-020 selector replay is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"001-020 selector replay requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("001-020 selector replay requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if "C01TESEL020-G1-VIRAL-001" not in ledger:
        raise SystemExit("C01TESEL020 authorization missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    overview = read_json(OVERVIEW_ROOT / "overview_replay_report.json")
    p013_entry = read_json(MRS_ROOT / "method_registry_entries" / "page_013.json")
    if overview["overview_id"] != "C01TEOR020-G1-VIRAL-001":
        raise SystemExit("unexpected overview replay input")
    if overview["requested_pages"] != [f"{page:03d}" for page in range(1, 21)]:
        raise SystemExit("overview replay requested pages drifted")
    if p013_entry["entry_id"] != P013_ENTRY_ID or p013_entry["page"] != "013":
        raise SystemExit("unexpected P013 MRS entry")
    if p013_entry["selector_rule_created"] or p013_entry["runtime_selector_integration"]:
        raise SystemExit("P013 MRS entry unexpectedly enabled selector behavior")
    if p013_entry["selected_candidate_id"] != "p013_sac_d_noise_then_declared_seam_fracture":
        raise SystemExit("P013 MRS selected candidate drifted")
    return verified, overview, p013_entry


def page_map(overview: dict) -> dict[str, dict]:
    return {item["page"]: item for item in overview["page_results"]}


def baseline_selection(page: str, item: dict) -> dict:
    if item["status"] != "run_completed":
        raise SystemExit(f"P{page} baseline selection requires completed overview result")
    if item["weak_flags"] not in ([], ["reference_not_ocr_verified"]):
        raise SystemExit(f"P{page} baseline selection has unexpected weak flags: {item['weak_flags']}")
    return {
        "page": page,
        "selector_decision": "selected_frozen_baseline",
        "selection_status": "selected_static_evidence_only",
        "source_lane_id": "C01TEOR020-G1-VIRAL-001",
        "method_entry_id": "frozen_trim_mask_psm4_baseline",
        "selected_output_hashes": {
            "candidate_text_sha256": item["candidate_text_sha256"],
            "normalized_text_sha256": item["normalized_text_sha256"],
            "reference_text_map_sha256": item["reference_text_map_sha256"],
        },
        "metrics": item["metrics"],
        "reference_label": item["reference_label"],
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def p013_selection(p013_entry: dict) -> dict:
    return {
        "page": "013",
        "selector_decision": "selected_p013_mrs_candidate",
        "selection_status": "selected_static_evidence_only",
        "source_lane_id": p013_entry["decision_id"],
        "method_entry_id": p013_entry["entry_id"],
        "selected_candidate_id": p013_entry["selected_candidate_id"],
        "selected_output_hashes": {
            "candidate_text_sha256": p013_entry["artifact_hashes"]["candidate_text_sha256"],
            "normalized_candidate_sha256": p013_entry["artifact_hashes"]["normalized_candidate_sha256"],
            "retained_record_trace_sha256": p013_entry["artifact_hashes"]["retained_record_trace_sha256"],
            "suppression_ledger_sha256": p013_entry["artifact_hashes"]["suppression_ledger_sha256"],
            "assembly_trace_sha256": p013_entry["artifact_hashes"]["assembly_trace_sha256"],
        },
        "metrics": p013_entry["metrics"],
        "reference_label": p013_entry["reference_dependency"]["label"],
        "reference_dependency": p013_entry["reference_dependency"],
        "excluded_equivalent_candidate": p013_entry["equivalent_candidate_not_selected"],
        "excluded_failed_variants": p013_entry["excluded_variants"],
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def unresolved_selection(page: str, item: dict) -> dict:
    return {
        "page": page,
        "selector_decision": "unresolved_needs_method_winner",
        "selection_status": "not_selected",
        "source_lane_id": "C01TEOR020-G1-VIRAL-001",
        "reason": "no_selected_method_registry_winner_for_page",
        "overview_metrics": item.get("metrics"),
        "overview_weak_flags": item.get("weak_flags", []),
        "failed_or_weak_candidate_selected": False,
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def parked_selection(page: str, item: dict) -> dict:
    return {
        "page": page,
        "selector_decision": "parked_candidate_policy",
        "selection_status": "not_selected",
        "source_lane_id": "C01TEISP-G1-VIRAL-001",
        "reason": "router_static_replay_parked_candidate_policy_requires_separate_review",
        "overview_metrics": item.get("metrics"),
        "overview_weak_flags": item.get("weak_flags", []),
        "failed_or_weak_candidate_selected": False,
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def ineligible_selection(page: str, item: dict) -> dict:
    if item["status"] != "not_run_ineligible":
        raise SystemExit(f"P{page} expected ineligible overview result")
    return {
        "page": page,
        "selector_decision": "not_run_ineligible",
        "selection_status": "not_selected",
        "source_lane_id": "C01TEOR020-G1-VIRAL-001",
        "reason": item["reason"],
        "failed_or_weak_candidate_selected": False,
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def build_page_selections(overview: dict, p013_entry: dict) -> list[dict]:
    pages = page_map(overview)
    selections: list[dict] = []
    for page in [f"{item:03d}" for item in range(1, 21)]:
        if page in EXPECTED_GROUPS["not_run_ineligible"]:
            selections.append(ineligible_selection(page, pages[page]))
        elif page in EXPECTED_GROUPS["selected_frozen_baseline"]:
            selections.append(baseline_selection(page, pages[page]))
        elif page in EXPECTED_GROUPS["selected_p013_mrs"]:
            selections.append(p013_selection(p013_entry))
        elif page in EXPECTED_GROUPS["unresolved_needs_method_winner"]:
            selections.append(unresolved_selection(page, pages[page]))
        elif page in EXPECTED_GROUPS["parked_candidate_policy"]:
            selections.append(parked_selection(page, pages[page]))
        else:
            raise SystemExit(f"unexpected page {page}")
    return selections


def selection_counts(selections: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in selections:
        counts[item["selector_decision"]] = counts.get(item["selector_decision"], 0) + 1
    return counts


def validate_selections(selections: list[dict]) -> None:
    selected = [item for item in selections if item["selection_status"] == "selected_static_evidence_only"]
    if [item["page"] for item in selected] != ["009", "010", "011", "013", "015"]:
        raise SystemExit("selected page set drifted")
    for item in selected:
        hashes = item.get("selected_output_hashes", {})
        if not hashes or not all(isinstance(value, str) and len(value) == 64 for value in hashes.values()):
            raise SystemExit(f"P{item['page']} selected hashes missing or malformed")
        if item["candidate_text_copied"] or item["production_output_created"]:
            raise SystemExit(f"P{item['page']} selection created output unexpectedly")
    for item in selections:
        if item["page"] in EXPECTED_GROUPS["unresolved_needs_method_winner"] + EXPECTED_GROUPS["parked_candidate_policy"]:
            if item["selection_status"] != "not_selected":
                raise SystemExit(f"P{item['page']} must remain not selected")
            if item["failed_or_weak_candidate_selected"]:
                raise SystemExit(f"P{item['page']} selected failed or weak candidate")


def build_report(verified_inputs: dict[str, dict[str, str]], overview: dict, p013_entry: dict) -> dict:
    selections = build_page_selections(overview, p013_entry)
    validate_selections(selections)
    selected_pages = [item["page"] for item in selections if item["selection_status"] == "selected_static_evidence_only"]
    not_selected_pages = [item["page"] for item in selections if item["selection_status"] == "not_selected"]
    return {
        "replay_id": REPLAY_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "static_selector_replay_completed_partial_coverage",
        "purpose": "prove_static_001_020_selector_routing_without_ocr_or_production_assembly",
        "human_decision": HUMAN_DECISION,
        "requested_pages": [f"{page:03d}" for page in range(1, 21)],
        "selected_pages": selected_pages,
        "not_selected_pages": not_selected_pages,
        "selection_counts": selection_counts(selections),
        "all_pages_first_pass_success": False,
        "production_ready": False,
        "production_blocked_reason": "selector_coverage_is_partial_unresolved_pages_remain",
        "page_selections": selections,
        "selected_artifact_policy": "hash_references_only_no_text_copy",
        "failed_or_superseded_candidates_selected": False,
        "p013_mrs_selected": True,
        "baseline_pages_materialized_with_output_hashes": True,
        "unresolved_pages": EXPECTED_GROUPS["unresolved_needs_method_winner"],
        "parked_pages": EXPECTED_GROUPS["parked_candidate_policy"],
        "not_run_ineligible_pages": EXPECTED_GROUPS["not_run_ineligible"],
        "verified_inputs": verified_inputs,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "ocr_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "reference_guided_repair_used": False,
        "reference_token_insertion_performed": False,
        "text_token_mutation_performed": False,
        "source_or_raw_mutation_performed": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "selector_runtime_enabled": False,
        "runtime_selector_integration": False,
        "runtime_execution_performed": False,
        "production_assembly_created": False,
        "clean_production_output_folder_created": False,
        "page_021_plus_included": False,
        "translation_or_proofreading_performed": False,
        "push_performed": False,
        "promotion_performed": False,
        "acceptance_performed": False,
        "downstream_execution_performed": False,
        "next_blocked_steps": [
            "P012_method_winner_required",
            "P016_method_winner_required",
            "P017_method_winner_required_or_selection_decision_required",
            "P018_method_winner_required_or_selection_decision_required",
            "P020_method_winner_required",
            "P014_P019_parked_policy_requires_separate_decision",
            "production_assembly_requires_full_selector_coverage_and_separate_authorization",
        ],
    }


def write_summary(report: dict) -> None:
    lines = [
        "# Core 0.1 Static Selector Replay 001-020 - C01TESEL020-G1-VIRAL-001",
        "",
        "Status: `static_selector_replay_completed_partial_coverage`",
        "",
        "This replay uses only sealed prior artifacts. It does not run OCR and does not create production output.",
        "",
        "| Page | Selector decision | Selection status | Source |",
        "|---|---|---|---|",
    ]
    for item in report["page_selections"]:
        lines.append(
            f"| `{item['page']}` | `{item['selector_decision']}` | "
            f"`{item['selection_status']}` | `{item['source_lane_id']}` |"
        )
    lines.extend(
        [
            "",
            f"Selected pages: `{', '.join(report['selected_pages'])}`.",
            f"Unresolved pages: `{', '.join(report['unresolved_pages'])}`.",
            f"Parked pages: `{', '.join(report['parked_pages'])}`.",
            "",
            "Production ready: `false`.",
            "All pages first-pass success: `false`.",
            "Failed or superseded candidates selected: `false`.",
            "",
            "## Machine-Checkable Boundary Flags",
            "",
            "- `promotion_performed=false`.",
            "- `acceptance_performed=false`.",
            "- `downstream_execution_performed=false`.",
            "- `negative_capability_matrix.promotion=false`.",
            "- `negative_capability_matrix.acceptance=false`.",
            "- `negative_capability_matrix.downstream_execution=false`.",
            "",
            "Boundary: no OCR/render/PDF/text-layer execution, no accepted/semantic/page-status/source/raw mutation, no runtime selector integration, no production assembly, no clean production output folder, no page 021+, no translation/proofreading, no push, no promotion, no acceptance, and no downstream execution.",
            "",
        ]
    )
    write_text(OUT_ROOT / "selector_replay_001_020_summary.md", "\n".join(lines))


def output_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "selector_replay_001_020_manifest.md":
            hashes[path.relative_to(OUT_ROOT).as_posix()] = sha256_file(path)
    return hashes


def write_manifest() -> None:
    lines = [
        "# Core 0.1 Static Selector Replay 001-020 Manifest - C01TESEL020-G1-VIRAL-001",
        "",
        "Boundary: static replay/report only; no production assembly.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for rel_path, digest in output_hashes().items():
        lines.append(f"| `{rel_path}` | `{digest}` |")
    lines.append("")
    write_text(OUT_ROOT / "selector_replay_001_020_manifest.md", "\n".join(lines))


def build() -> None:
    verified_inputs, overview, p013_entry = verify_inputs()
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report = build_report(verified_inputs, overview, p013_entry)
    write_json(OUT_ROOT / "selector_replay_001_020_report.json", report)
    write_json(OUT_ROOT / "selector_replay_001_020_selections.json", report["page_selections"])
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
