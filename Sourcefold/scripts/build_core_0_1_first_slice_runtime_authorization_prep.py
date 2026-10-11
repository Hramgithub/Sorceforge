from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_first_slice_runtime_authorization_prep.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_first_slice_runtime_authorization_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SOURCE_ROOT = TRIAL_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_first_slice_runtime_authorization_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-FIRST-SLICE-RUNTIME-AUTHORIZATION-PREP-001"
PREP_ID = "C01RSAP-G1-VIRAL-001"
SOURCE_PACKET_ID = "C01RSPLP-G1-VIRAL-001"
FIRST_SLICE_ID = "C01WP-01-phase-1-scaffold-contracts"
HUMAN_DECISION = (
    "c01rsplp packet ok; proceed to prepare Core 0.1 first-slice runtime authorization prep for C01WP-01 "
    "from C01RSPLP; no runtime implementation, no runtime source-profile lock/acceptance, "
    "no OCR/render/PDF/raw mutation, no translation/proofreading, no page 021+, no push, commit"
)

INPUT_HASHES = {
    "C01RSPLP-G1-VIRAL-001.packet": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision.json",
        "7C69F0EBEF416C5A8646836E31EC89BC66AA5A60B302080C890605830A58CC36",
    ),
    "C01RSPLP-G1-VIRAL-001.report": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_report.json",
        "A8AFDB207A40E9ADFD2624D2679BDC92E5C6055FA07CF0ECEA28E555761E20E1",
    ),
    "C01RSPLP-G1-VIRAL-001.summary": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_summary.md",
        "019266B4C3BFD1622731A914856F92104D36F92CEB410FBADC1BDDBD79D8A425",
    ),
    "C01RSPLP-G1-VIRAL-001.manifest": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_parking_decision_manifest.md",
        "11398446A0D15736CC004A2C4FAD998AD82AF75B97151B5F0F9430C8E59326FA",
    ),
}

NEGATIVE_CAPABILITIES = [
    "runtime_implementation",
    "first_slice_runtime_start",
    "first_slice_runtime_authorization_grant",
    "runtime_source_profile_lock",
    "runtime_source_profile_acceptance",
    "source_profile_acceptance_beyond_c01splpr",
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
    "new_or_broader_fixture_admission",
    "renderer_profile_acceptance",
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
    parser = argparse.ArgumentParser(description="Prepare Core 0.1 first-slice runtime authorization prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 first-slice runtime authorization prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 first-slice runtime authorization prep requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 first-slice runtime authorization prep requires the exact bounded human decision")


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

    packet = read_json(INPUT_HASHES["C01RSPLP-G1-VIRAL-001.packet"][0])
    if packet["decision_id"] != SOURCE_PACKET_ID:
        raise SystemExit("unexpected runtime source-profile parking decision input")
    if packet["status"] != "runtime_source_profile_lock_or_parking_decision_prepared_no_runtime_implementation":
        raise SystemExit("runtime source-profile parking decision is not the expected no-runtime packet")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("runtime source-profile parking decision unexpectedly authorizes runtime implementation")
    if packet["runtime_source_profile_lock_created"] or packet["runtime_source_profile_acceptance_created"]:
        raise SystemExit("runtime source-profile parking decision unexpectedly creates a runtime source-profile lock or acceptance")
    if packet["first_slice_id"] != FIRST_SLICE_ID:
        raise SystemExit("unexpected first-slice target")
    if packet["remaining_blockers"][0] != "human_review_c01rsplp_required":
        raise SystemExit("C01RSPLP human review is not the current first blocker")
    if "first_slice_runtime_authorization_required" not in packet["remaining_blockers"]:
        raise SystemExit("first-slice runtime authorization blocker is not present")
    if packet["next_possible_packets"][1] != "core_0_1_first_slice_runtime_authorization_prep_if_separately_authorized":
        raise SystemExit("first-slice runtime authorization prep is not a permitted next packet")
    return verified, packet


def build_prep(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    remaining_blockers = [
        blocker
        for blocker in packet["remaining_blockers"]
        if blocker not in {"human_review_c01rsplp_required"}
    ]
    if "first_slice_runtime_authorization_required" not in remaining_blockers:
        remaining_blockers.insert(0, "first_slice_runtime_authorization_required")
    if "human_review_c01rsap_required" not in remaining_blockers:
        remaining_blockers.insert(0, "human_review_c01rsap_required")
    prep_items = [
        {
            "item_id": "consume_c01rsplp_human_review",
            "purpose": "Record Bogdan acceptance of C01RSPLP as the direct input to prep.",
            "status": "prepared",
            "authorizes_runtime_start": False,
        },
        {
            "item_id": "canonical_runtime_authorization_prep_mapping",
            "purpose": "Map C01RSAP-G1-VIRAL-001 to core_0_1_first_slice_runtime_authorization_prep.",
            "status": "prepared",
            "authorizes_runtime_start": False,
        },
        {
            "item_id": "runtime_profile_parking_reference",
            "purpose": "Reference the parked runtime source-profile disposition without locking or accepting a profile.",
            "status": "prepared",
            "authorizes_runtime_start": False,
        },
        {
            "item_id": "runtime_authorization_guardrails",
            "purpose": "Keep implementation, runtime start, runtime source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, fixture admission, and push blocked.",
            "status": "prepared",
            "authorizes_runtime_start": False,
        },
    ]
    return {
        "prep_id": PREP_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "first_slice_runtime_authorization_prep_prepared_no_runtime_implementation",
        "purpose": "bounded_first_slice_runtime_authorization_prep_for_c01wp_01_after_runtime_source_profile_parking",
        "human_decision": HUMAN_DECISION,
        "human_review_consumed": "c01rsplp_packet_ok",
        "source_runtime_source_profile_lock_or_parking_decision": packet["decision_id"],
        "source_acceptance_matrix_trace_review": packet["source_acceptance_matrix_trace_review"],
        "source_architecture_review_packet": packet["source_architecture_review_packet"],
        "source_profile_lock_or_parking_receipt": packet["source_profile_lock_or_parking_receipt"],
        "source_first_slice_design_prep_packet": packet["source_first_slice_design_prep_packet"],
        "source_implementation_authorization_receipt": packet["source_implementation_authorization_receipt"],
        "source_whole_gate_1_acceptance_decision": packet["source_whole_gate_1_acceptance_decision"],
        "accepted_gate_1_scope": packet["accepted_gate_1_scope"],
        "first_slice_id": FIRST_SLICE_ID,
        "canonical_packet_name": "core_0_1_first_slice_runtime_authorization_prep",
        "first_slice_runtime_authorization_prep_created": True,
        "first_slice_runtime_authorization_granted": False,
        "runtime_authorization_created": False,
        "runtime_start_authorized": False,
        "runtime_source_profile_decision_created": False,
        "runtime_source_profile_parking_consumed_as_reference_only": True,
        "runtime_source_profile_disposition": packet["runtime_source_profile_disposition"],
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "runtime_source_profile_parking_recorded": False,
        "source_profile_lock_created": False,
        "source_profile_acceptance_created": False,
        "accepts_source_profile_beyond_c01splpr": False,
        "runtime_implementation_authorized": False,
        "creates_runtime_implementation": False,
        "executes_ocr": False,
        "executes_render": False,
        "mutates_source_ocr_render_pdf_raw": False,
        "creates_translation_or_proofreading": False,
        "processes_page_021_plus": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "prep_items": prep_items,
        "remaining_blockers": remaining_blockers,
        "next_possible_packets": [
            "human_review_c01rsap_packet",
            "core_0_1_first_slice_runtime_authorization_if_separately_authorized_after_human_review",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(prep: dict) -> None:
    scope = prep["accepted_gate_1_scope"]
    disposition = prep["runtime_source_profile_disposition"]
    lines = [
        "# Core 0.1 First-Slice Runtime Authorization Prep - C01RSAP-G1-VIRAL-001",
        "",
        "Status: `first_slice_runtime_authorization_prep_prepared_no_runtime_implementation`",
        "",
        "This packet prepares the first-slice runtime authorization decision context for `C01WP-01-phase-1-scaffold-contracts` after runtime source-profile parking.",
        "",
        "It does not authorize runtime implementation or runtime start.",
        "",
        "## Accepted Input Scope",
        "",
        f"- Runtime source-profile parking decision: `{prep['source_runtime_source_profile_lock_or_parking_decision']}`.",
        f"- Acceptance-matrix trace review: `{prep['source_acceptance_matrix_trace_review']}`.",
        f"- Architecture review packet: `{prep['source_architecture_review_packet']}`.",
        f"- Source-profile receipt: `{prep['source_profile_lock_or_parking_receipt']}`.",
        f"- Whole Gate 1 acceptance decision: `{prep['source_whole_gate_1_acceptance_decision']}`.",
        f"- Page range: `{scope['page_complete_accepted_pages'][0]}`-`{scope['page_complete_accepted_pages'][-1]}`.",
        f"- Fixture admission decision: `{scope['fixture_admission_decision']}`.",
        "",
        "## Runtime Authorization Prep",
        "",
        "- Canonical packet name: `core_0_1_first_slice_runtime_authorization_prep`.",
        "- Human review consumed: `c01rsplp_packet_ok`.",
        "- First-slice runtime authorization prep created: `true`.",
        "- First-slice runtime authorization granted: `false`.",
        "- Runtime authorization created: `false`.",
        "- Runtime start authorized: `false`.",
        f"- Runtime source-profile disposition referenced: `{disposition['runtime_profile_disposition']}`.",
        "- Runtime source-profile parking consumed as reference only: `true`.",
        "",
        "## Boundary",
        "",
        "- Runtime implementation: `false`.",
        "- Runtime source-profile lock: `false`.",
        "- Runtime source-profile acceptance: `false`.",
        "- Source-profile acceptance beyond `C01SPLPR`: `false`.",
        "- OCR/render/PDF/raw/source mutation: `false`.",
        "- Translation/proofreading: `false`.",
        "- Page 021+ processing/authorization: `false`.",
        "- New or broader fixture admission: `false`.",
        "- Push: `false`.",
        "",
        "## Remaining Blockers",
        "",
    ]
    for blocker in prep["remaining_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    write_text(OUT_ROOT / "core_0_1_first_slice_runtime_authorization_prep_summary.md", "\n".join(lines))


def write_report(prep: dict) -> None:
    scope = prep["accepted_gate_1_scope"]
    write_json(
        OUT_ROOT / "core_0_1_first_slice_runtime_authorization_prep_report.json",
        {
            "prep_id": PREP_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": prep["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_runtime_source_profile_lock_or_parking_decision": prep["source_runtime_source_profile_lock_or_parking_decision"],
            "first_slice_id": FIRST_SLICE_ID,
            "accepted_page_count": len(scope["page_complete_accepted_pages"]),
            "prep_item_count": len(prep["prep_items"]),
            "first_slice_runtime_authorization_prep_created": True,
            "first_slice_runtime_authorization_granted": False,
            "runtime_authorization_created": False,
            "runtime_start_authorized": False,
            "runtime_implementation_authorized": False,
            "creates_runtime_implementation": False,
            "runtime_source_profile_lock_created": False,
            "runtime_source_profile_acceptance_created": False,
            "runtime_source_profile_parking_consumed_as_reference_only": True,
            "source_profile_lock_created": False,
            "source_profile_acceptance_created": False,
            "accepts_source_profile_beyond_c01splpr": False,
            "executes_ocr": False,
            "executes_render": False,
            "mutates_source_ocr_render_pdf_raw": False,
            "creates_translation_or_proofreading": False,
            "processes_page_021_plus": False,
            "admits_new_or_broader_fixture": False,
            "push_performed": False,
            "negative_capability_matrix": prep["negative_capability_matrix"],
            "remaining_blockers": prep["remaining_blockers"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_first_slice_runtime_authorization_prep_manifest.md"
    lines = [
        "# Core 0.1 First-Slice Runtime Authorization Prep Manifest - C01RSAP-G1-VIRAL-001",
        "",
        "Status: `first_slice_runtime_authorization_prep_prepared_no_runtime_implementation`",
        "",
        "Boundary: first-slice runtime authorization prep only for C01WP-01; no runtime implementation, runtime authorization grant, runtime start, runtime source-profile lock/acceptance, OCR/render/PDF/raw/source mutation, translation, proofreading, page 021+, new fixture admission, push, or downstream action.",
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
    verified_inputs, packet = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    prep = build_prep(verified_inputs, packet)
    write_json(OUT_ROOT / "core_0_1_first_slice_runtime_authorization_prep.json", prep)
    write_summary(prep)
    write_report(prep)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
