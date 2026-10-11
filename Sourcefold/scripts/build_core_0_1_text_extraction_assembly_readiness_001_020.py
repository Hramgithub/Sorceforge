from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
MF_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_012_016_020_method_family_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_assembly_readiness_001_020_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

LANE_ID = "C01TEASM020-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-ASSEMBLY-READINESS-001-020-001"
HUMAN_DECISION = "jr"

REQUESTED_PAGES = [f"{page:03d}" for page in range(1, 21)]
SELECTED_PAGES = ["009", "010", "011", "012", "013", "015", "016", "017", "018", "020"]
NOT_RUN_INELIGIBLE = ["001", "002", "003", "004", "005", "006", "007", "008"]
PARKED_PAGES = ["014", "019"]

INPUT_HASHES = {
    "C01TEMF012016020-G1-VIRAL-001.report": (
        MF_ROOT / "012_016_020_method_family_report.json",
        "529706EAB697961A1F1EFDD6A34EAF488B64C0082FDB87C83322A88A6578383D",
    ),
    "C01TEMF012016020-G1-VIRAL-001.summary": (
        MF_ROOT / "012_016_020_method_family_summary.md",
        "8A4808F6769002A331C29815C348D812E151D729DB693857662BFDB4F8A6B103",
    ),
    "C01TEMF012016020-G1-VIRAL-001.selector_v3": (
        MF_ROOT / "selector_replay_v3" / "selector_replay_v3_selections.json",
        "BFA0062BCA3F6CF9D56FED45DF813BC52014C85AD33CAF262DAD60EE34FA4A17",
    ),
    "C01TEMF012016020-G1-VIRAL-001.page_012_entry": (
        MF_ROOT / "method_registry_entries" / "page_012.json",
        "91B29C338E42649E2666E033F10D9B3342EAD8BC2CD0A1C376336AFCBE6B1A4F",
    ),
    "C01TEMF012016020-G1-VIRAL-001.page_016_entry": (
        MF_ROOT / "method_registry_entries" / "page_016.json",
        "C0AF109F49093C7B5182C97BCD8FA5A13704C93213F3CB66801CCE72AF3E55AF",
    ),
    "C01TEMF012016020-G1-VIRAL-001.page_020_entry": (
        MF_ROOT / "method_registry_entries" / "page_020.json",
        "01E3A3BCF497BCFBE4C3817FE808E8B40BA5FF05B4CDD00E7A447352C4945341",
    ),
}

EXPECTED_SELECTED_HASHES = {
    "009": {
        "candidate_text_sha256": "639DBD7317EE8FFF3BD884134EB0432C719F89E6F828E6C43650DF1D0744571A",
        "normalized_text_sha256": "6CAE5B305E5AE8832531254ABE0B827410701A036BA630DC281E66A51FE105EE",
        "reference_text_map_sha256": "3D3A2F6A197AD553BCEA95D20B880A64BE58B4C085392F7B1A149344BE3A4A6B",
    },
    "010": {
        "candidate_text_sha256": "4ED82383B74A74E63AFE141D7001E1FA00CD8F210A8E23B24948B522808F5826",
        "normalized_text_sha256": "D1590D716B493F62F17921118017EB1A21CE4946266785E7ED3DA439373388F5",
        "reference_text_map_sha256": "568B9B1F788E599582C24A4D7DEA95E8E5E5A7A59691DBBC0964557B06DBC20D",
    },
    "011": {
        "candidate_text_sha256": "B1ABCCD5DFD0F4AA986BECBBA99FF6B63E9AA6E74547D8434F03ED57677F26C0",
        "normalized_text_sha256": "4D53E642FAFCF020D49F7DC2678E40D371C09F39196E1210A0945A8EF86C87B5",
        "reference_text_map_sha256": "8E0C30537A0CE166DD419446C8896E6E5F67D942FBDE91AE9C3450C4D32316A3",
    },
    "012": {
        "candidate_text_sha256": "EBC229C440B4526810DD529D61D9253DEA06085322DA1A3EE39D986E56A09003",
        "normalized_candidate_sha256": "AC166FB89F550DA7DE17EFF4A93B1C9D4692C719B86074717FFFC09BBA5DB5E0",
        "source_page_image_sha256": "D5040085668216E68E617A06B513DC09CE3797E4D3F6BC6AC7BF35B68BD08ED6",
    },
    "013": {
        "candidate_text_sha256": "E24D29CE34A61755E9B92214007EFEB8FEADC4B77D4C35468ACF64DDF9D41DE4",
        "normalized_candidate_sha256": "69E406E7C3890A3862D06284B7E77D16FBBCA5B9E486E62ECC8AEA971B878E3D",
        "retained_record_trace_sha256": "4B0628DE7BC5EF395DAAB107F6B6448A230C2E08FA24C0B4005F37FE90389A19",
        "suppression_ledger_sha256": "4A54B31E63C66AE28939FAF9A9A63A8F131F19B2E1AD2E0BBA61B29DD96B5F03",
        "assembly_trace_sha256": "EC9A97A032A1562C25839AFCD46B15792A6498AAC3FB3D5B14A7B0FEC471C62D",
    },
    "015": {
        "candidate_text_sha256": "6F7629A9785DEF510D04F107E30B5CA8E2736718E339ED2946C87E1BDBD48DA8",
        "normalized_text_sha256": "19035AAEFF549FB09939345D3ADA841DB842EDF48D680BE75488CDB02866EB6E",
        "reference_text_map_sha256": "1AC358CEC610D9F696D166695F137C9EF9F36337BFF80002D63E54FF55E51AD4",
    },
    "016": {
        "candidate_text_sha256": "F1EC507098D1C6B29A2019646D40EFF9DEE4048721E414FEF288AA9081DF6092",
        "normalized_candidate_sha256": "97EDBAA53E1590120CBCF7A5BDA7F58A1A57CC98577B66E5D3C26788B9C3617D",
        "source_page_image_sha256": "7B839125E6DCDA8F78C10DAC6AB9AFB8AD6990AE39FF50A675B963CFC1836C56",
    },
    "017": {
        "candidate_text_sha256": "EE2C75BA5B7083F143EACF9B42862AB7DDBFDFE6C4AD87A66F0B18D833D4E0F2",
        "normalized_candidate_sha256": "C699DCCF11BF73A21C600C6C97BC4D1ABAAABB445CAA88DFCDA15F5B7ACF45E2",
        "source_page_image_sha256": "1198CBB7D55877B31FEEA3E32CD95EABEB504A4610CA98D7CB2047C30142E08F",
    },
    "018": {
        "candidate_text_sha256": "047189E7340BFE706FCF705B01E50551FFC4EE015A39C4DE458F0E116C2933D4",
        "normalized_candidate_sha256": "E26F13DAA0C87A19EBAA861312DB1CCEAB86E9CAC413EF404E7608501E588A2D",
        "source_page_image_sha256": "6E8F440CEB5F11A4081722ADF5CD65F74E622641884192390E9DA0CAE6C6BFD4",
    },
    "020": {
        "candidate_text_sha256": "C3CD2343656652FFBF6DFD486CF7BEDB5D2AB34065232A927E641F46C3FBB0AC",
        "normalized_candidate_sha256": "12ED07CE8BBFA7159756B9D6B35AA77DAE271B4ABC520F2154CE610B29847FF3",
        "source_page_image_sha256": "53C04DFDF02787DF16FFB26862FE5C6AB67D61DD4FF93D8A122537B8F110B56E",
    },
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "reference_guided_repair",
    "reference_token_insertion",
    "candidate_text_copy",
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
    "page_001_020_runtime_loop",
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
    parser = argparse.ArgumentParser(description="Build manifest-only 001-020 assembly-readiness report.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("assembly-readiness lane is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"assembly-readiness lane requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("assembly-readiness lane requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, list[dict]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if "Status: `method_family_candidates_selected_static_evidence_only`" not in ledger:
        raise SystemExit("predecessor C01TEMF012016020 completion is not synced in ledger")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected_hash) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected_hash:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    report = read_json(MF_ROOT / "012_016_020_method_family_report.json")
    selections = read_json(MF_ROOT / "selector_replay_v3" / "selector_replay_v3_selections.json")
    if report["lane_id"] != "C01TEMF012016020-G1-VIRAL-001":
        raise SystemExit("method-family report lane drifted")
    if report["selected_pages_v3"] != SELECTED_PAGES:
        raise SystemExit(f"unexpected selected pages v3: {report['selected_pages_v3']}")
    if report["production_ready"] is not False or report["all_pages_first_pass_success"] is not False:
        raise SystemExit("method-family report unexpectedly production-ready")
    if len(selections) != 20:
        raise SystemExit(f"selector v3 page count drifted: {len(selections)}")
    return verified, report, selections


def assert_selected_hash_pins(selections: list[dict]) -> None:
    selected = [item for item in selections if item["selection_status"] == "selected_static_evidence_only"]
    if [item["page"] for item in selected] != SELECTED_PAGES:
        raise SystemExit(f"selected pages drifted: {[item['page'] for item in selected]}")
    for item in selected:
        page = item["page"]
        actual_hashes = item.get("selected_output_hashes", {})
        if actual_hashes != EXPECTED_SELECTED_HASHES[page]:
            raise SystemExit(f"P{page} selected hash set drifted")
        if item.get("candidate_text_copied") is not False:
            raise SystemExit(f"P{page} unexpectedly copied candidate text")
        if item.get("production_output_created") is not False:
            raise SystemExit(f"P{page} unexpectedly created production output")


def build_selected_manifest(selections: list[dict]) -> list[dict]:
    manifest: list[dict] = []
    for item in selections:
        if item["selection_status"] != "selected_static_evidence_only":
            continue
        manifest.append(
            {
                "page": item["page"],
                "status": "selected_static_evidence_manifest_only",
                "source_lane_id": item["source_lane_id"],
                "method_entry_id": item["method_entry_id"],
                "selector_decision": item["selector_decision"],
                "selected_candidate_id": item.get("selected_candidate_id"),
                "selected_output_hashes": item["selected_output_hashes"],
                "metrics": item["metrics"],
                "reference_label": item["reference_label"],
                "reference_dependency": item.get("reference_dependency"),
                "reference_not_accepted_source_text": item["reference_label"] != "reference_ocr_verified_text_map",
                "candidate_text_copied": False,
                "candidate_text_inline": False,
                "production_output_path": None,
                "production_output_created": False,
            }
        )
    return manifest


def build_exclusions(selections: list[dict]) -> list[dict]:
    excluded: list[dict] = []
    for item in selections:
        if item["selection_status"] == "selected_static_evidence_only":
            continue
        page = item["page"]
        if page in NOT_RUN_INELIGIBLE:
            blocker = "not_run_ineligible"
        elif page in PARKED_PAGES:
            blocker = "parked_candidate_policy"
        else:
            raise SystemExit(f"unexpected excluded page: {page}")
        excluded.append(
            {
                "page": page,
                "selector_decision": item["selector_decision"],
                "blocker": blocker,
                "reason": item.get("reason"),
                "failed_or_weak_candidate_selected": item.get("failed_or_weak_candidate_selected") is True,
                "candidate_text_copied": False,
                "production_output_created": False,
            }
        )
    if [item["page"] for item in excluded if item["blocker"] == "not_run_ineligible"] != NOT_RUN_INELIGIBLE:
        raise SystemExit("not-run/ineligible page set drifted")
    if [item["page"] for item in excluded if item["blocker"] == "parked_candidate_policy"] != PARKED_PAGES:
        raise SystemExit("parked page set drifted")
    return excluded


def build_report(verified_inputs: dict, mf_report: dict, selections: list[dict]) -> tuple[dict, list[dict]]:
    assert_selected_hash_pins(selections)
    selected_manifest = build_selected_manifest(selections)
    excluded = build_exclusions(selections)
    reference_risk_pages = [item["page"] for item in selected_manifest if item["reference_not_accepted_source_text"]]
    return (
        {
            "lane_id": LANE_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": "assembly_readiness_manifest_only_production_blocked",
            "human_decision": HUMAN_DECISION,
            "input_lane_id": mf_report["lane_id"],
            "requested_pages": REQUESTED_PAGES,
            "selected_pages": SELECTED_PAGES,
            "excluded_pages": [item["page"] for item in excluded],
            "not_run_ineligible_pages": NOT_RUN_INELIGIBLE,
            "parked_pages": PARKED_PAGES,
            "selected_page_count": len(SELECTED_PAGES),
            "excluded_page_count": len(excluded),
            "manifest_only": True,
            "hash_reference_only": True,
            "candidate_text_copied": False,
            "candidate_text_inline": False,
            "failed_or_weak_candidate_selected": False,
            "failed_or_superseded_candidates_in_manifest": False,
            "production_ready": False,
            "all_pages_first_pass_success": False,
            "production_assembly_created": False,
            "clean_production_output_folder_created": False,
            "accepted_text_mutation_performed": False,
            "semantic_text_mutation_performed": False,
            "page_status_mutation_performed": False,
            "source_or_raw_mutation_performed": False,
            "selector_runtime_enabled": False,
            "runtime_selector_integration": False,
            "runtime_execution_performed": False,
            "page_001_020_runtime_loop_created": False,
            "page_021_plus_included": False,
            "promotion_performed": False,
            "acceptance_performed": False,
            "downstream_execution_performed": False,
            "reference_risk_pages": reference_risk_pages,
            "reference_risk_note": "static evidence only; reference_text_map_not_ocr_verified is not accepted source text",
            "selected_manifest_path": (
                OUT_ROOT / "assembly_manifest" / "selected_pages_manifest.json"
            ).relative_to(ROOT).as_posix(),
            "verified_inputs": verified_inputs,
            "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
            "excluded_page_details": excluded,
        },
        selected_manifest,
    )


def write_summary(report: dict) -> None:
    lines = [
        "# Assembly Readiness 001-020 - C01TEASM020-G1-VIRAL-001",
        "",
        "Status: `assembly_readiness_manifest_only_production_blocked`",
        "",
        "This lane writes a manifest-only, hash-reference-only readiness report for the selected static evidence inside pages `001`-`020`. It does not copy candidate text and does not create a production or clean output folder.",
        "",
        f"Selected pages: `{', '.join(report['selected_pages'])}`.",
        f"Not-run/ineligible pages: `{', '.join(report['not_run_ineligible_pages'])}`.",
        f"Parked pages: `{', '.join(report['parked_pages'])}`.",
        f"Production ready: `{str(report['production_ready']).lower()}`.",
        f"All pages first-pass success: `{str(report['all_pages_first_pass_success']).lower()}`.",
        "",
        "## Boundary Flags",
        "",
        "- `manifest_only=true`.",
        "- `hash_reference_only=true`.",
        "- `candidate_text_copied=false`.",
        "- `production_assembly_created=false`.",
        "- `clean_production_output_folder_created=false`.",
        "- `accepted_text_mutation_performed=false`.",
        "- `page_status_mutation_performed=false`.",
        "- `runtime_selector_integration=false`.",
        "- `page_021_plus_included=false`.",
        "- `acceptance_performed=false`.",
        "",
        "Reference risk remains: selected evidence that depends on `reference_text_map_not_ocr_verified` is static evidence only, not accepted source text.",
        "",
    ]
    write_text(OUT_ROOT / "assembly_readiness_001_020_summary.md", "\n".join(lines))


def write_manifest() -> None:
    lines = [
        "# Assembly Readiness 001-020 Manifest - C01TEASM020-G1-VIRAL-001",
        "",
        "Boundary: manifest-only readiness evidence; no copied candidate text, no production assembly, no clean production output folder.",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "assembly_readiness_001_020_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / "assembly_readiness_001_020_manifest.md", "\n".join(lines))


def build() -> None:
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    verified_inputs, mf_report, selections = verify_inputs()
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    report, selected_manifest = build_report(verified_inputs, mf_report, selections)
    write_json(OUT_ROOT / "assembly_manifest" / "selected_pages_manifest.json", selected_manifest)
    write_json(OUT_ROOT / "assembly_readiness_001_020_report.json", report)
    write_summary(report)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
