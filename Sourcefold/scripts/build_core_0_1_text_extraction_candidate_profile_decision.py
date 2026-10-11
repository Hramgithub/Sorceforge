from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_candidate_profile_decision.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_candidate_profile_decision.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
P009_REMEDIATION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p009_remediation_matrix_G1_VIRAL_001"
P010_SMOKE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p010_trim_mask_psm4_G1_VIRAL_001"
P015_SMOKE_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_smoke_p015_trim_mask_psm4_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_candidate_profile_decision_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-CANDIDATE-PROFILE-DECISION-001"
DECISION_ID = "C01TECPD-G1-VIRAL-001"
HUMAN_DECISION = "ок"
PROFILE_ID = "trim_mask_psm4"
PROFILE_VARIANT = "edge_mask_trim"
PROFILE_PSM = 4

INPUT_HASHES = {
    "C01TESRM-G1-VIRAL-001.report": (
        P009_REMEDIATION_ROOT / "remediation_report.json",
        "622B90068710E8F1A6EBBD5667F643641A51B765CB8DB077A49DB5C67AFDFEA5",
    ),
    "C01TESRM-G1-VIRAL-001.summary": (
        P009_REMEDIATION_ROOT / "remediation_summary.md",
        "F48907CD2CF49FE7FCF95454B193F2564EE42E9EC7375AF3A07E35F65593F1FF",
    ),
    "C01TESRM-G1-VIRAL-001.manifest": (
        P009_REMEDIATION_ROOT / "remediation_manifest.md",
        "AD0DF2BB6E75F585717BF13AC856890958AC9B989EDAD85CA446B96F8BBFB009",
    ),
    "C01TESRM-G1-VIRAL-001.rankings": (
        P009_REMEDIATION_ROOT / "variant_rankings.json",
        "28BF755676BE6DD3CAA1952B3561301D62904EF99C67E3A10687B3261855ACB2",
    ),
    "C01TESP010-G1-VIRAL-001.report": (
        P010_SMOKE_ROOT / "smoke_report.json",
        "544EC833934E63B7EBDFC40DB7B25D71ED878AF800B300CE2F9A4950DFCDC4D6",
    ),
    "C01TESP010-G1-VIRAL-001.summary": (
        P010_SMOKE_ROOT / "smoke_summary.md",
        "448F92E29134AF00E3924EAD5EE7F713CD9A2D96B020110BF30268D84485D616",
    ),
    "C01TESP010-G1-VIRAL-001.manifest": (
        P010_SMOKE_ROOT / "smoke_manifest.md",
        "D95B1B851310F36A954162C8030EE18E2B8E69642C03E336E5CA54B953C374CA",
    ),
    "C01TESP010-G1-VIRAL-001.candidate_text": (
        P010_SMOKE_ROOT / "candidate_texts" / "trim_mask_psm4.md",
        "2C0B879FF21122D86D9D000934DBEF8227E461C3CBDE38D52902468DF5C13744",
    ),
    "C01TESP015-G1-VIRAL-001.report": (
        P015_SMOKE_ROOT / "smoke_report.json",
        "3D3536957B7DE4C7B0C23DF5C425A20C6D620E3B309B549BAFF43E63F1774492",
    ),
    "C01TESP015-G1-VIRAL-001.summary": (
        P015_SMOKE_ROOT / "smoke_summary.md",
        "0D3A8D0C66790C108502B106D18D9BB9802F4B0E6FAF1ACD67238C3128F7EF5B",
    ),
    "C01TESP015-G1-VIRAL-001.manifest": (
        P015_SMOKE_ROOT / "smoke_manifest.md",
        "39E150A2A86B5005C2E84FD3A6C31E8E119E26A344FFE5D64F6B2A9A38A0B1DA",
    ),
    "C01TESP015-G1-VIRAL-001.candidate_text": (
        P015_SMOKE_ROOT / "candidate_texts" / "trim_mask_psm4.md",
        "DF40D4AB2A60E2F76A784C4E4657E9E202C1702A250F99309959DFE8DB5061F9",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
    "ocr_remediation_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "source_mutation",
    "raw_mutation",
    "accepted_text_mutation",
    "semantic_text_mutation",
    "page_status_mutation",
    "source_profile_acceptance",
    "runtime_source_profile_lock",
    "runtime_source_profile_acceptance",
    "runtime_implementation",
    "runtime_start",
    "runtime_execution",
    "page_016_plus_processing",
    "page_021_plus_processing",
    "page_021_plus_authorization",
    "translation",
    "proofreading",
    "push",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 text extraction candidate profile decision.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 text extraction candidate profile decision is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 text extraction candidate profile decision requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 text extraction candidate profile decision requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    remediation = read_json(P009_REMEDIATION_ROOT / "remediation_report.json")
    p010 = read_json(P010_SMOKE_ROOT / "smoke_report.json")
    p015 = read_json(P015_SMOKE_ROOT / "smoke_report.json")
    if remediation["matrix_id"] != "C01TESRM-G1-VIRAL-001":
        raise SystemExit("unexpected P009 remediation input")
    if remediation["best_candidate_id"] != PROFILE_ID:
        raise SystemExit("P009 remediation did not select trim_mask_psm4")
    for report, expected_id, expected_page in [
        (p010, "C01TESP010-G1-VIRAL-001", "010"),
        (p015, "C01TESP015-G1-VIRAL-001", "015"),
    ]:
        if report["smoke_id"] != expected_id or report["page"] != expected_page:
            raise SystemExit(f"unexpected same-profile smoke input for {expected_page}")
        if report["candidate_id"] != PROFILE_ID or report["variant"] != PROFILE_VARIANT or report["psm"] != PROFILE_PSM:
            raise SystemExit(f"{expected_id} does not use the selected candidate tuple")
        if report["candidate_count"] != 1:
            raise SystemExit(f"{expected_id} is not a single-candidate smoke")
        for key in [
            "pdf_parsing_performed",
            "pdf_text_layer_extraction_performed",
            "render_execution_performed",
            "source_or_raw_mutation_performed",
            "accepted_text_mutation_performed",
            "semantic_text_mutation_performed",
            "page_status_mutation_performed",
            "runtime_implementation_created",
            "runtime_start_performed",
            "translation_or_proofreading_performed",
            "push_performed",
        ]:
            if report[key]:
                raise SystemExit(f"{expected_id} violates boundary flag {key}")
    if "reference_ocr_verified_text_map" in p015.get("verified_inputs", {}):
        raise SystemExit("P015 must not be labeled as OCR-verified reference")
    if "page_015_text_map.md" not in p015["reference_text_map"]["path"]:
        raise SystemExit("P015 must compare against page_015_text_map.md")
    return verified, remediation, p010, p015


def build_decision(verified_inputs: dict[str, dict[str, str]], remediation: dict, p010: dict, p015: dict) -> dict:
    evidence = [
        {
            "evidence_id": remediation["matrix_id"],
            "page": "009",
            "role": "remediation_selection",
            "reference_label": "reference_ocr_verified_text_map",
            "selected_candidate": remediation["best_candidate_id"],
            "variant": PROFILE_VARIANT,
            "psm": PROFILE_PSM,
            "sequence_similarity_ratio": remediation["best_similarity"],
            "token_recall": remediation["best_token_recall"],
        },
        {
            "evidence_id": p010["smoke_id"],
            "page": "010",
            "role": "same_profile_generalization",
            "reference_label": "reference_ocr_verified_text_map",
            "selected_candidate": p010["candidate_id"],
            "variant": p010["variant"],
            "psm": p010["psm"],
            "sequence_similarity_ratio": p010["metrics"]["sequence_similarity_ratio"],
            "token_recall": p010["metrics"]["token_recall"],
        },
        {
            "evidence_id": p015["smoke_id"],
            "page": "015",
            "role": "same_profile_ladder_evidence",
            "reference_label": "reference_text_map_not_ocr_verified",
            "selected_candidate": p015["candidate_id"],
            "variant": p015["variant"],
            "psm": p015["psm"],
            "sequence_similarity_ratio": p015["metrics"]["sequence_similarity_ratio"],
            "token_recall": p015["metrics"]["token_recall"],
        },
    ]
    min_similarity = min(item["sequence_similarity_ratio"] for item in evidence)
    min_token_recall = min(item["token_recall"] for item in evidence)
    return {
        "decision_id": DECISION_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "text_extraction_candidate_profile_decision_recorded_candidate_profile_frozen",
        "purpose": "close_p009_p010_p015_smoke_ladder_and_freeze_candidate_profile_for_future_replay_decision",
        "human_decision": HUMAN_DECISION,
        "human_decision_context": "Bogdan accepted the proposed next plan: close smoke ladder evidence, prepare profile-lock decision packet, and run Sol/Terra gate.",
        "sol_gate": {
            "status": "ok",
            "scope": "points_1_3_only",
            "blockers": [],
        },
        "terra_gate": {
            "status": "ok",
            "scope": "points_1_3_only",
            "blockers": [],
            "wording_guardrail": "P015 uses reference_text_map, not reference_ocr_verified_text_map.",
        },
        "candidate_profile_decision_recorded": True,
        "candidate_profile_freeze_granted": True,
        "candidate_profile_id": PROFILE_ID,
        "candidate_profile_tuple": {
            "candidate_id": PROFILE_ID,
            "preprocessing_variant": PROFILE_VARIANT,
            "tesseract_psm": PROFILE_PSM,
            "tesseract_oem": 1,
            "language": "eng",
            "strategy": "full_column",
        },
        "candidate_profile_scope": "Core_0_1_text_extraction_candidate_profile_only",
        "source_profile_acceptance_created": False,
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "ocr_acceptance_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "runtime_implementation_created": False,
        "runtime_start_performed": False,
        "ocr_execution_performed": False,
        "render_execution_performed": False,
        "pdf_parsing_or_text_layer_extraction_performed": False,
        "source_or_raw_mutation_performed": False,
        "page_016_plus_included": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "evidence_lineage": [
            "C01TESP-G1-VIRAL-001",
            "C01TESRM-G1-VIRAL-001",
            "C01TESP010-G1-VIRAL-001",
            "C01TESP015-G1-VIRAL-001",
        ],
        "evidence": evidence,
        "aggregate_metrics": {
            "min_sequence_similarity_ratio": min_similarity,
            "min_token_recall": min_token_recall,
            "page_count": 3,
            "same_profile_pages": ["010", "015"],
            "selection_page": "009",
        },
        "decision_outcome": "freeze_trim_mask_psm4_as_candidate_profile_for_future_config_and_replay_only",
        "next_possible_packets": [
            "core_0_1_text_extraction_frozen_profile_config_if_separately_authorized",
            "core_0_1_text_extraction_replay_regression_smoke_if_separately_authorized",
            "park_ocr_layer_and_prepare_runtime_integration_design_if_separately_authorized",
        ],
        "remaining_blockers": [
            "frozen_profile_config_requires_separate_authorization",
            "replay_regression_smoke_requires_separate_authorization",
            "runtime_integration_design_requires_separate_authorization",
            "runtime_source_profile_lock_requires_separate_authorization",
            "accepted_text_or_semantic_mutation_requires_separate_authorization",
            "page_021_plus_remains_separate_bounded_lane_if_selected",
            "push_requires_separate_authorization",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(decision: dict) -> None:
    lines = [
        "# Core 0.1 Text Extraction Candidate Profile Decision - C01TECPD-G1-VIRAL-001",
        "",
        "Status: `text_extraction_candidate_profile_decision_recorded_candidate_profile_frozen`",
        "",
        "`trim_mask_psm4` is frozen as a Core 0.1 text extraction candidate profile for future config/replay work only.",
        "",
        "This is not OCR acceptance, source-profile acceptance, accepted text, semantic acceptance, page-status mutation, runtime profile lock, or runtime implementation authorization.",
        "",
        "## Candidate Profile",
        "",
        "- Candidate: `trim_mask_psm4`.",
        "- Preprocessing variant: `edge_mask_trim`.",
        "- Tesseract PSM: `4`.",
        "- Tesseract OEM: `1`.",
        "- Language: `eng`.",
        "- Scope: `Core_0_1_text_extraction_candidate_profile_only`.",
        "",
        "## Evidence Ladder",
        "",
        "| Evidence | Page | Role | Reference | Similarity | Token recall |",
        "|---|---:|---|---|---:|---:|",
    ]
    for item in decision["evidence"]:
        lines.append(
            f"| `{item['evidence_id']}` | `{item['page']}` | `{item['role']}` | "
            f"`{item['reference_label']}` | `{item['sequence_similarity_ratio']}` | `{item['token_recall']}` |"
        )
    lines.extend(
        [
            "",
            "## Decision",
            "",
            "- Candidate profile decision recorded: `true`.",
            "- Candidate profile freeze granted: `true`.",
            "- Decision outcome: `freeze_trim_mask_psm4_as_candidate_profile_for_future_config_and_replay_only`.",
            "- Minimum ladder similarity: "
            f"`{decision['aggregate_metrics']['min_sequence_similarity_ratio']}`.",
            "- Minimum ladder token recall: "
            f"`{decision['aggregate_metrics']['min_token_recall']}`.",
            "",
            "## Boundary",
            "",
            "- OCR execution in this layer: `false`.",
            "- Render/PDF/text-layer extraction: `false`.",
            "- Source/raw/accepted/semantic/page-status mutation: `false`.",
            "- Source-profile acceptance: `false`.",
            "- Runtime source-profile lock/acceptance: `false`.",
            "- Runtime implementation/start/execution: `false`.",
            "- Page 016+/021+ processing: `false`.",
            "- Push: `false`.",
            "",
            "## Remaining Blockers",
            "",
        ]
    )
    for blocker in decision["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_text_extraction_candidate_profile_decision_summary.md", "\n".join(lines))


def write_report(decision: dict) -> None:
    write_json(
        OUT_ROOT / "core_0_1_text_extraction_candidate_profile_decision_report.json",
        {
            "decision_id": DECISION_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": decision["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "candidate_profile_id": PROFILE_ID,
            "candidate_profile_freeze_granted": True,
            "source_profile_acceptance_created": False,
            "runtime_source_profile_lock_created": False,
            "runtime_source_profile_acceptance_created": False,
            "ocr_execution_performed": False,
            "render_execution_performed": False,
            "pdf_parsing_or_text_layer_extraction_performed": False,
            "source_or_raw_mutation_performed": False,
            "accepted_text_mutation_performed": False,
            "semantic_text_mutation_performed": False,
            "page_status_mutation_performed": False,
            "page_021_plus_included": False,
            "push_performed": False,
            "evidence": decision["evidence"],
            "aggregate_metrics": decision["aggregate_metrics"],
            "negative_capability_matrix": decision["negative_capability_matrix"],
            "remaining_blockers": decision["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_text_extraction_candidate_profile_decision_manifest.md"
    lines = [
        "# Core 0.1 Text Extraction Candidate Profile Decision Manifest - C01TECPD-G1-VIRAL-001",
        "",
        "Status: `text_extraction_candidate_profile_decision_recorded_candidate_profile_frozen`",
        "",
        "Boundary: candidate-profile decision only; no OCR execution, render, PDF text-layer extraction, source/raw/accepted/semantic/page-status mutation, source-profile acceptance, runtime lock/acceptance, runtime implementation/start/execution, page 016+/021+, translation/proofreading, push, or downstream action.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(OUT_ROOT / manifest_name, "\n".join(lines))


def build() -> None:
    verified_inputs, remediation, p010, p015 = verify_inputs()
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    decision = build_decision(verified_inputs, remediation, p010, p015)
    write_json(OUT_ROOT / "core_0_1_text_extraction_candidate_profile_decision.json", decision)
    write_summary(decision)
    write_report(decision)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
