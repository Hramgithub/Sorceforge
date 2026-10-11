from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
ASM_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_eligibility_bridge_001_020_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

LANE_ID = "C01TEBRIDGE020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ELIGIBILITY-BRIDGE-001-020-001"
HUMAN_DECISION = "ок делай"

REQUESTED_PAGES = [f"{page:03d}" for page in range(1, 21)]
BRIDGE_PAGES = ["001", "002", "003", "004", "005", "006", "007", "008", "014", "019"]
ASSEMBLY_SELECTED_PAGES = ["009", "010", "011", "012", "013", "015", "016", "017", "018", "020"]
ALL_COVERED_PAGES = REQUESTED_PAGES

INPUT_HASHES = {
    "C01TEASM020-G1-VIRAL-001.report": (
        ASM_ROOT / "assembly_readiness_001_020_report.json",
        "EC9A291300335CE3B05F7BF541D3C0A273FC047B4415DBC29F1E981937A7D6AB",
    ),
    "C01TEASM020-G1-VIRAL-001.selected_manifest": (
        ASM_ROOT / "assembly_manifest" / "selected_pages_manifest.json",
        "090352D6B97AABA628CEE692F67E1305C896D0723C8214579AE4469CF1850DE9",
    ),
    "P001PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p001_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "0ED79F4FE7A9E239E6992CEDA9C9A73CDD3B39E6BD71BBDEC68DBCFDF6C9BF0B",
    ),
    "P002PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p002_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C",
    ),
    "P003PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p003_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "9D74A9B73D657A0669AD0025B40936E1873A9643F1F03F31279B87FCFAFA5F79",
    ),
    "P004PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p004_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "57D4E5B3665129732308E042B4CECEEDD170907B2DCB852468DBBF885C222035",
    ),
    "P005PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p005_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "2065A5C139E42514AD92EFB897151CE87CEEEF42208B9A7F99482B7A7F923022",
    ),
    "P006PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p006_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "9D0643332F24AF2B5FF3D14518B9FF83B70B331FA1E165577A6C5245532692B5",
    ),
    "P007PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p007_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "8A1B163709D47D9268602C8F2EEF5F5E880E450807468DC9EB360BE8C7CC80F5",
    ),
    "P008PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p008_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "44F126668C6A6F148579787917D93199D0413F51DE0E8C3C6143AAA4047B0F64",
    ),
    "P014PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p014_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "D4F8A985DCA3E7CCAB0960B1B65719E5CF59902A29AF943F32482FFA533E6946",
    ),
    "P019PCA-G1-VIRAL-001.report": (
        TRIAL_ROOT / "page_complete_acceptance_p019_G1_VIRAL_001" / "page_complete_acceptance_report.json",
        "67FCCB6B34A266EC7EC007AF656E1E162B0C6CC294F275496CC1E92B40611985",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
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


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build static eligibility bridge for 001-020.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("eligibility bridge lane is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"eligibility bridge lane requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("eligibility bridge lane requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict], dict[str, dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if "Status: `assembly_readiness_manifest_only_production_blocked`" not in ledger:
        raise SystemExit("predecessor C01TEASM020 completion is not synced in ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    asm_report = read_json(ASM_ROOT / "assembly_readiness_001_020_report.json")
    asm_manifest = read_json(ASM_ROOT / "assembly_manifest" / "selected_pages_manifest.json")
    if asm_report["lane_id"] != "C01TEASM020-G1-VIRAL-001":
        raise SystemExit("assembly-readiness input lane drifted")
    if asm_report["selected_pages"] != ASSEMBLY_SELECTED_PAGES:
        raise SystemExit(f"assembly selected pages drifted: {asm_report['selected_pages']}")
    if asm_report["production_assembly_created"] is not False:
        raise SystemExit("assembly-readiness unexpectedly created production output")

    acceptances: dict[str, dict] = {}
    for page in BRIDGE_PAGES:
        acceptances[page] = read_json(
            TRIAL_ROOT / f"page_complete_acceptance_p{page}_G1_VIRAL_001" / "page_complete_acceptance_report.json"
        )
    return verified, asm_report, asm_manifest, acceptances


def accepted_page(report: dict) -> str:
    if "page" in report:
        return report["page"]
    if "accepted_page" in report:
        return report["accepted_page"]
    if "accepted_pages" in report and len(report["accepted_pages"]) == 1:
        return report["accepted_pages"][0]
    accepted = report.get("page_complete_acceptance", {}).get("accepted_pages_as_complete")
    if accepted and len(accepted) == 1:
        return accepted[0]
    raise SystemExit("could not identify accepted page")


def assert_acceptance_guardrails(page: str, report: dict) -> None:
    if accepted_page(report) != page:
        raise SystemExit(f"P{page} acceptance page drifted")
    status = report.get("status", "")
    if "accepted" not in status and "acceptance_created" not in status:
        raise SystemExit(f"P{page} status is not accepted: {status}")

    guardrails = report.get("guardrails", {})
    false_keys = [
        "whole_gate_1_acceptance",
        "whole_gate_1_acceptance_created",
        "fixture_admission",
        "source_acceptance_mutation",
        "source_acceptance_created_or_mutated",
        "ocr_execution",
        "ocr_executed",
        "render_execution",
        "render_executed",
        "pdf_parsing_or_text_layer_extraction",
        "pdf_opened_or_parsed",
        "pdf_text_layer_used",
        "raw_mutation",
        "raw_artifacts_modified",
        "translation",
        "translation_authorized",
        "proofreading",
        "proofreading_authorized",
        "implementation",
        "implementation_authorized",
        "push",
        "push_authorized",
    ]
    for key in false_keys:
        if key in guardrails and guardrails[key] is not False:
            raise SystemExit(f"P{page} guardrail {key} drifted")


def build_bridge_entry(page: str, report: dict, verified_inputs: dict) -> dict:
    assert_acceptance_guardrails(page, report)
    if page in {"014", "019"}:
        decision = "parked_overview_but_page_complete_accepted_bridge"
    else:
        decision = "accepted_page_complete_bridge"
    key = f"P{page}PCA-G1-VIRAL-001.report"
    return {
        "page": page,
        "selector_decision": decision,
        "selection_status": "selected_static_evidence_only",
        "source_lane_id": report.get("package_id") or report.get("acceptance_id"),
        "method_entry_id": f"{LANE_ID}-P{page}",
        "acceptance_report_path": verified_inputs[key]["path"],
        "acceptance_report_sha256": verified_inputs[key]["sha256"],
        "accepted_page_complete_only": True,
        "imported_from_prior_accepted_lane": True,
        "new_first_pass_ocr_selector_result": False,
        "candidate_text_copied": False,
        "production_output_created": False,
    }


def selector_replay_v4(asm_manifest: list[dict], bridge_entries: list[dict]) -> list[dict]:
    selected = []
    by_page = {entry["page"]: entry for entry in bridge_entries}
    by_page.update({entry["page"]: entry for entry in asm_manifest})
    for page in REQUESTED_PAGES:
        if page not in by_page:
            raise SystemExit(f"missing replay v4 page: {page}")
        selected.append(by_page[page])
    return selected


def build_report(verified_inputs: dict, asm_report: dict, asm_manifest: list[dict], acceptances: dict[str, dict]) -> tuple[dict, list[dict], list[dict]]:
    bridge_entries = [build_bridge_entry(page, acceptances[page], verified_inputs) for page in BRIDGE_PAGES]
    replay_v4 = selector_replay_v4(asm_manifest, bridge_entries)
    if [item["page"] for item in replay_v4] != ALL_COVERED_PAGES:
        raise SystemExit("selector replay v4 is not full 001-020 coverage")
    return (
        {
            "lane_id": LANE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": "eligibility_bridge_static_evidence_all_pages_covered_production_blocked",
            "human_decision": HUMAN_DECISION,
            "input_lane_id": asm_report["lane_id"],
            "requested_pages": REQUESTED_PAGES,
            "bridge_pages": BRIDGE_PAGES,
            "assembly_selected_pages": ASSEMBLY_SELECTED_PAGES,
            "covered_pages_v4": ALL_COVERED_PAGES,
            "all_pages_static_evidence_covered": True,
            "all_pages_first_pass_success": False,
            "first_pass_success_blocker": "coverage_includes_prior_accepted_page_complete_bridge_not_new_ocr_selector_first_pass",
            "production_ready": False,
            "production_assembly_created": False,
            "clean_production_output_folder_created": False,
            "accepted_text_mutation_performed": False,
            "semantic_text_mutation_performed": False,
            "page_status_mutation_performed": False,
            "source_or_raw_mutation_performed": False,
            "selector_runtime_enabled": False,
            "runtime_selector_integration": False,
            "runtime_execution_performed": False,
            "page_021_plus_included": False,
            "promotion_performed": False,
            "acceptance_performed": False,
            "downstream_execution_performed": False,
            "bridge_entries": bridge_entries,
            "selector_replay_v4_path": (OUT_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json").relative_to(ROOT).as_posix(),
            "verified_inputs": verified_inputs,
            "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        },
        bridge_entries,
        replay_v4,
    )


def write_summary(report: dict) -> None:
    lines = [
        "# Eligibility Bridge 001-020 - C01TEBRIDGE020-G1-VIRAL-001",
        "",
        "Status: `eligibility_bridge_static_evidence_all_pages_covered_production_blocked`",
        "",
        "This dry-run bridges prior page-complete acceptance evidence into the static selector surface. It does not run OCR, copy text, mutate acceptance/page status, or create production output.",
        "",
        f"Bridge pages: `{', '.join(report['bridge_pages'])}`.",
        f"Covered pages v4: `{', '.join(report['covered_pages_v4'])}`.",
        f"All pages static evidence covered: `{str(report['all_pages_static_evidence_covered']).lower()}`.",
        f"All pages first-pass success: `{str(report['all_pages_first_pass_success']).lower()}`.",
        f"Production ready: `{str(report['production_ready']).lower()}`.",
        "",
        "## Boundary Flags",
        "",
        "- `production_assembly_created=false`.",
        "- `clean_production_output_folder_created=false`.",
        "- `accepted_text_mutation_performed=false`.",
        "- `page_status_mutation_performed=false`.",
        "- `runtime_selector_integration=false`.",
        "- `page_021_plus_included=false`.",
        "- `acceptance_performed=false`.",
        "",
    ]
    write_text(OUT_ROOT / "eligibility_bridge_001_020_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# Eligibility Bridge 001-020 Manifest - C01TEBRIDGE020-G1-VIRAL-001",
        "",
        "Boundary: static bridge/report only; no OCR, no production output, no acceptance mutation.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "eligibility_bridge_001_020_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / "eligibility_bridge_001_020_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, asm_report, asm_manifest, acceptances = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report, bridge_entries, replay_v4 = build_report(verified_inputs, asm_report, asm_manifest, acceptances)
    write_json(OUT_ROOT / "bridge_entries" / "accepted_page_complete_bridge_entries.json", bridge_entries)
    write_json(OUT_ROOT / "selector_replay_v4" / "selector_replay_v4_selections.json", replay_v4)
    write_json(OUT_ROOT / "eligibility_bridge_001_020_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
