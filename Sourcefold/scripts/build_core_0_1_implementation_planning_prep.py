from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_implementation_planning_prep.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_implementation_planning_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
DECISION_ROOT = TRIAL_ROOT / "gate_1_whole_gate_acceptance_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_implementation_planning_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-IMPLEMENTATION-PLANNING-PREP-001"
PACKET_ID = "C01IPP-G1-VIRAL-001"
SOURCE_DECISION_ID = "G1WGADR-G1-VIRAL-001"
HUMAN_DECISION = (
    "proceed with core_0_1_implementation_planning_prep from G1WGADR; no implementation, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, "
    "no source-profile acceptance beyond G1WGADR, no push, commit"
)

INPUT_HASHES = {
    "G1WGADR-G1-VIRAL-001.acceptance": (
        DECISION_ROOT / "gate_1_whole_gate_acceptance_decision.json",
        "0E10B81021474344A5D244CAA7DA51660A4D8756C153023D911C4DD51A790379",
    ),
    "G1WGADR-G1-VIRAL-001.report": (
        DECISION_ROOT / "gate_1_whole_gate_acceptance_decision_report.json",
        "0784A6AE4F1FD39002AAB5533AC58973E63251BD24108468DBC4792217633547",
    ),
    "G1WGADR-G1-VIRAL-001.summary": (
        DECISION_ROOT / "gate_1_whole_gate_acceptance_decision_summary.md",
        "0B64928DC5F48152C9F6AEE90D51C9578159C9743344C20540F8D2D96D57AB09",
    ),
    "G1WGADR-G1-VIRAL-001.manifest": (
        DECISION_ROOT / "gate_1_whole_gate_acceptance_decision_manifest.md",
        "CC88C898E3943A7EE8E27484BCF13F51537014B3E9B6116307D4965744196D29",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "implementation_authorization_receipt",
    "ocr_execution",
    "ocr_remediation_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "source_mutation",
    "raw_mutation",
    "translation",
    "proofreading",
    "page_021_plus_processing",
    "page_021_plus_authorization",
    "source_profile_acceptance_beyond_g1wgadr",
    "new_or_broader_fixture_admission",
    "renderer_profile_acceptance",
    "push",
]

WORK_PACKAGES = [
    {
        "work_package_id": "C01WP-01-phase-1-scaffold-contracts",
        "title": "Phase 1 scaffold and contract inventory",
        "planning_disposition": "candidate_first_slice",
        "may_start_now": False,
        "separate_authorization_required": True,
        "forbidden_in_this_packet": [
            "create_runtime_modules",
            "change_runtime_behavior",
            "execute_candidate_processing",
        ],
        "expected_contracts": [
            "module_boundary_inventory",
            "artifact_identity_contract",
            "lineage_trace_contract",
            "acceptance_matrix_trace_contract",
        ],
    },
    {
        "work_package_id": "C01WP-02-core-artifact-schema-contracts",
        "title": "Core artifact schema contract planning",
        "planning_disposition": "candidate_after_scaffold",
        "may_start_now": False,
        "separate_authorization_required": True,
        "forbidden_in_this_packet": [
            "write_schema_implementation",
            "migrate_existing_artifacts",
            "mutate_candidate_inputs",
        ],
        "expected_contracts": [
            "reconstruction_input_schema_contract",
            "translation_input_schema_contract",
            "proofreading_input_schema_contract",
        ],
    },
    {
        "work_package_id": "C01WP-03-reconstruct-dry-contracts",
        "title": "Reconstruct lane dry contract planning",
        "planning_disposition": "candidate_future_slice",
        "may_start_now": False,
        "separate_authorization_required": True,
        "forbidden_in_this_packet": [
            "execute_ocr",
            "execute_render",
            "parse_pdf",
            "generate_runtime_reconstruction_output",
        ],
        "expected_contracts": [
            "accepted_page_input_contract",
            "fixture_group_input_contract",
            "negative_fixture_failure_contract",
        ],
    },
    {
        "work_package_id": "C01WP-04-ocr-profile-execution-authorization-prep",
        "title": "OCR/profile execution authorization prep",
        "planning_disposition": "blocked_until_separate_authorization",
        "may_start_now": False,
        "separate_authorization_required": True,
        "forbidden_in_this_packet": [
            "accept_source_profile_beyond_g1wgadr",
            "execute_ocr",
            "rerun_remediation",
            "mutate_render_pdf_raw_assets",
        ],
        "expected_contracts": [
            "single_source_profile_lock_receipt",
            "ocr_execution_boundary_receipt",
            "rollback_and_invalidation_receipt",
        ],
    },
    {
        "work_package_id": "C01WP-05-translation-proofreading-future-lanes",
        "title": "Translation and proofreading future-lane planning",
        "planning_disposition": "blocked_downstream",
        "may_start_now": False,
        "separate_authorization_required": True,
        "forbidden_in_this_packet": [
            "translate_content",
            "proofread_content",
            "claim_release_candidate_readiness",
        ],
        "expected_contracts": [
            "translation_input_readiness_contract",
            "proofreading_input_readiness_contract",
            "release_candidate_evidence_contract",
        ],
    },
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 implementation planning packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 implementation planning prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 implementation planning prep requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 implementation planning prep requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    decision = read_json(INPUT_HASHES["G1WGADR-G1-VIRAL-001.acceptance"][0])
    if decision["acceptance_id"] != SOURCE_DECISION_ID:
        raise SystemExit("unexpected whole Gate 1 acceptance decision input")
    if decision["status"] != "whole_gate_1_acceptance_decision_accepted":
        raise SystemExit("whole Gate 1 acceptance decision is not accepted")
    if not decision["accepts_whole_gate_1"]:
        raise SystemExit("whole Gate 1 is not accepted by the source decision")
    if decision["creates_implementation"]:
        raise SystemExit("source decision already creates implementation")
    if decision["processes_page_021_plus"]:
        raise SystemExit("source decision includes page 021+")
    if decision["accepts_source_profile_beyond_gate_1_record"]:
        raise SystemExit("source decision accepts a broader source profile")
    if decision["next_possible_packets"][0] != "core_0_1_implementation_planning_if_separately_authorized":
        raise SystemExit("Core 0.1 implementation planning is not the next packet")
    scope = decision["whole_gate_1_acceptance_scope"]
    if scope["page_complete_accepted_pages"] != [f"{page:03d}" for page in range(1, 21)]:
        raise SystemExit("Core 0.1 planning prep must inherit pages 001-020 only")
    if scope["fixture_admission_decision"] != "G1FADAR-G1-VIRAL-001":
        raise SystemExit("Core 0.1 planning prep must inherit the G1FADAR fixture decision")
    return verified, decision


def build_packet(verified_inputs: dict[str, dict[str, str]], decision: dict) -> dict:
    scope = decision["whole_gate_1_acceptance_scope"]
    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "core_0_1_implementation_planning_prep_ready_for_review",
        "purpose": "bounded_core_0_1_implementation_planning_prep_only_no_implementation",
        "human_decision": HUMAN_DECISION,
        "source_whole_gate_1_acceptance_decision": decision["acceptance_id"],
        "accepted_gate_1_scope": {
            "page_complete_accepted_pages": scope["page_complete_accepted_pages"],
            "fixture_admission_decision": scope["fixture_admission_decision"],
            "positive_fixture_groups": scope["positive_fixture_groups"],
            "negative_fixture_groups": scope["negative_fixture_groups"],
            "page_021_plus_included": False,
            "source_profile_acceptance_beyond_g1wgadr": False,
        },
        "creates_implementation": False,
        "creates_implementation_authorization_receipt": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "accepts_source_profile_beyond_g1wgadr": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "implementation_planning": {
            "phase_transition": "gate_1_accepted_to_core_0_1_planning_prep",
            "recommended_first_slice": "C01WP-01-phase-1-scaffold-contracts",
            "first_slice_authorized": False,
            "planning_only": True,
            "work_packages": WORK_PACKAGES,
        },
        "required_before_runtime_implementation": [
            "implementation_authorization_receipt_with_separate_human_authorization",
            "single_core_0_1_source_profile_lock_or_explicitly_parked_equivalent",
            "acceptance_matrix_claim_to_evidence_mapping_for_first_slice",
            "sol_architecture_review_for_first_slice",
            "terra_critique_for_first_slice",
            "roadmap_validation_for_first_slice",
        ],
        "remaining_blockers": [
            "runtime_implementation_requires_separate_authorization",
            "ocr_render_pdf_raw_mutation_requires_separate_authorization",
            "translation_proofreading_requires_separate_authorization",
            "page_021_plus_remains_separate_bounded_lane_if_selected",
            "source_profile_acceptance_beyond_g1wgadr_requires_separate_authorization",
            "push_requires_separate_authorization",
        ],
        "next_possible_packets": [
            "core_0_1_implementation_authorization_receipt_if_separately_authorized",
            "core_0_1_first_slice_design_prep_if_separately_authorized",
            "page_021_plus_separate_bounded_authorization_if_selected",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    scope = packet["accepted_gate_1_scope"]
    lines = [
        "# Core 0.1 Implementation Planning Prep - C01IPP-G1-VIRAL-001",
        "",
        "Status: `core_0_1_implementation_planning_prep_ready_for_review`",
        "",
        "This packet prepares the Core 0.1 implementation planning transition after `G1WGADR-G1-VIRAL-001`.",
        "",
        "It does not authorize or create runtime implementation.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Whole Gate 1 acceptance decision: `{packet['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        f"- Positive fixture groups: `{len(scope['positive_fixture_groups'])}`.",
        f"- Negative fixture groups: `{len(scope['negative_fixture_groups'])}`.",
        "- Page 021+ included: `false`.",
        "- Source-profile acceptance beyond G1WGADR: `false`.",
        "",
        "## Work Packages",
        "",
    ]
    for row in packet["implementation_planning"]["work_packages"]:
        lines.append(f"- `{row['work_package_id']}`: {row['title']} (`{row['planning_disposition']}`); authorized now: `false`.")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- Runtime implementation: `false`.",
            "- Implementation authorization receipt: `false`.",
            "- OCR/render/PDF/raw/source mutation: `false`.",
            "- Translation/proofreading: `false`.",
            "- Page 021+ processing/authorization: `false`.",
            "- Source-profile acceptance beyond G1WGADR: `false`.",
            "- New or broader fixture admission: `false`.",
            "- Push: `false`.",
            "",
            "## Required Before Runtime Implementation",
            "",
        ]
    )
    for item in packet["required_before_runtime_implementation"]:
        lines.append(f"- `{item}`")
    lines.extend(["", "## Remaining Blockers", ""])
    for blocker in packet["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_implementation_planning_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    scope = packet["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_implementation_planning_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "positive_fixture_group_count": len(scope["positive_fixture_groups"]),
            "negative_fixture_group_count": len(scope["negative_fixture_groups"]),
            "work_package_count": len(packet["implementation_planning"]["work_packages"]),
            "recommended_first_slice": packet["implementation_planning"]["recommended_first_slice"],
            "creates_implementation": False,
            "creates_implementation_authorization_receipt": False,
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "processes_page_021_plus": False,
            "accepts_source_profile_beyond_g1wgadr": False,
            "admits_new_or_broader_fixture": False,
            "push_performed": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_blockers": packet["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_implementation_planning_prep_manifest.md"
    lines = [
        "# Core 0.1 Implementation Planning Prep Manifest - C01IPP-G1-VIRAL-001",
        "",
        "Status: `core_0_1_implementation_planning_prep_ready_for_review`",
        "",
        "Boundary: planning prep only from G1WGADR; no implementation, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, source-profile broadening, new fixture admission, push, or downstream action.",
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
    verified_inputs, decision = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, decision)
    write_json(OUT_ROOT / "core_0_1_implementation_planning_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
