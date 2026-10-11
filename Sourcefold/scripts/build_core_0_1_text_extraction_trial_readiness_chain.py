from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_trial_readiness_chain.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_trial_readiness_chain.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
SOURCE_ROOT = TRIAL_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

HUMAN_DECISION = 'делай 1-5 с проверкой через сол и терру, вместо "хуман ревью". зови перед запуском п.6'

SOURCE_HASHES = {
    "C01RSPLAD-G1-VIRAL-001.packet": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision.json",
        "416A7687AC9CD95DD00A909A642C2E8C64C17339E47E1010F3C6E700DDC58DB7",
    ),
    "C01RSPLAD-G1-VIRAL-001.report": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_report.json",
        "1D797D66CB1B9ECDDA2AD2EB9DC2C201C1246AA5B922A6C15F91F6EA7EEBFDA0",
    ),
    "C01RSPLAD-G1-VIRAL-001.summary": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_summary.md",
        "8C5570DA88CFC0D2CB162C61F8EA76187CD4A016FD526EECDBC5E141F8510A84",
    ),
    "C01RSPLAD-G1-VIRAL-001.manifest": (
        SOURCE_ROOT / "core_0_1_runtime_source_profile_lock_or_acceptance_decision_manifest.md",
        "A46062E47A18DC8DDED198B4AC8B61F5DA90C98EDC244B4C8105F130F98E3399",
    ),
}

AUTHORIZATIONS = [
    "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-LOCK-OR-ACCEPTANCE-MACHINE-REVIEW-ACCEPTANCE-001",
    "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-EVIDENCE-PREP-001",
    "BA-G1-VIRAL-CORE-0-1-RUNTIME-SOURCE-PROFILE-EXTRACTION-TRIAL-LOCK-OR-ACCEPTANCE-DECISION-001",
    "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-TRIAL-AUTHORIZATION-PREP-001",
    "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-TRIAL-DECISION-001",
]

STAGES = [
    {
        "decision_id": "C01RSPLADMR-G1-VIRAL-001",
        "canonical_packet_name": "core_0_1_runtime_source_profile_lock_or_acceptance_machine_review_acceptance",
        "artifact_dir": "c01rspladmr_G1_VIRAL_001",
        "file_base": "c01rspladmr",
        "status": "sol_terra_machine_review_acceptance_recorded_for_points_1_to_5_only",
        "auth": AUTHORIZATIONS[0],
        "source": "C01RSPLAD-G1-VIRAL-001",
        "summary": "Sol/Terra machine review accepts C01RSPLAD for points 1-5 only.",
    },
    {
        "decision_id": "C01RSPEP-G1-VIRAL-001",
        "canonical_packet_name": "core_0_1_runtime_source_profile_evidence_prep",
        "artifact_dir": "c01rspep_G1_VIRAL_001",
        "file_base": "c01rspep",
        "status": "runtime_source_profile_evidence_prep_recorded_no_extraction",
        "auth": AUTHORIZATIONS[1],
        "source": "C01RSPLADMR-G1-VIRAL-001",
        "summary": "Evidence-prep surfaces are prepared for future extraction-trial profile review.",
    },
    {
        "decision_id": "C01RSPETD-G1-VIRAL-001",
        "canonical_packet_name": "core_0_1_runtime_source_profile_extraction_trial_lock_or_acceptance_decision",
        "artifact_dir": "c01rspetd_G1_VIRAL_001",
        "file_base": "c01rspetd",
        "status": "future_extraction_trial_profile_decision_recorded_no_actual_lock_artifact",
        "auth": AUTHORIZATIONS[2],
        "source": "C01RSPEP-G1-VIRAL-001",
        "summary": "A future extraction-trial profile decision is recorded without creating actual runtime lock artifacts.",
    },
    {
        "decision_id": "C01TETAP-G1-VIRAL-001",
        "canonical_packet_name": "core_0_1_text_extraction_trial_authorization_prep",
        "artifact_dir": "c01tetap_G1_VIRAL_001",
        "file_base": "c01tetap",
        "status": "text_extraction_trial_authorization_prep_recorded_no_extraction",
        "auth": AUTHORIZATIONS[3],
        "source": "C01RSPETD-G1-VIRAL-001",
        "summary": "Text extraction trial authorization prep is recorded, with execution still blocked.",
    },
    {
        "decision_id": "C01TETD-G1-VIRAL-001",
        "canonical_packet_name": "core_0_1_text_extraction_trial_decision",
        "artifact_dir": "c01tetd_G1_VIRAL_001",
        "file_base": "c01tetd",
        "status": "text_extraction_trial_decision_recorded_call_bogdan_before_point_6",
        "auth": AUTHORIZATIONS[4],
        "source": "C01TETAP-G1-VIRAL-001",
        "summary": "A non-executing future text extraction trial decision is recorded; call Bogdan before point 6.",
    },
]

NEGATIVE_CAPABILITIES = [
    "actual_text_extraction",
    "ocr_execution",
    "render_execution",
    "pdf_parsing",
    "pdf_text_layer_extraction",
    "source_mutation",
    "raw_mutation",
    "runtime_implementation",
    "runtime_start",
    "runtime_execution",
    "actual_runtime_source_profile_lock_artifact",
    "actual_runtime_source_profile_acceptance_artifact",
    "page_021_plus_processing",
    "new_or_broader_fixture_admission",
    "translation",
    "proofreading",
    "push",
]

COMMON_BLOCKERS = [
    "call_bogdan_before_point_6_required",
    "actual_text_extraction_requires_new_explicit_authorization",
    "ocr_execution_requires_new_explicit_authorization",
    "pdf_text_layer_extraction_requires_new_explicit_authorization",
    "runtime_implementation_authorization_required",
    "runtime_start_execution_requires_separate_authorization",
    "page_021_plus_requires_separate_authorization",
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
    parser = argparse.ArgumentParser(description="Build Core 0.1 text extraction trial readiness chain.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 text extraction readiness chain is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATIONS[0]:
        raise SystemExit(f"Core 0.1 text extraction readiness chain requires {AUTHORIZATIONS[0]}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 text extraction readiness chain requires the exact bounded human decision")


def verify_inputs() -> dict[str, dict[str, str]]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    for auth in AUTHORIZATIONS:
        if f"## {auth}" not in ledger:
            raise SystemExit(f"{auth} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in SOURCE_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    packet = read_json(SOURCE_HASHES["C01RSPLAD-G1-VIRAL-001.packet"][0])
    if packet["decision_id"] != "C01RSPLAD-G1-VIRAL-001":
        raise SystemExit("unexpected runtime source-profile lock-or-acceptance decision input")
    if packet["runtime_source_profile_lock_granted"] or packet["runtime_source_profile_acceptance_granted"]:
        raise SystemExit("C01RSPLAD unexpectedly grants runtime source-profile lock/acceptance")
    if packet["runtime_start_authorized"] or packet["runtime_execution_authorized"]:
        raise SystemExit("C01RSPLAD unexpectedly authorizes runtime start/execution")
    if packet["runtime_implementation_authorized"] or packet["creates_runtime_implementation"]:
        raise SystemExit("C01RSPLAD unexpectedly authorizes runtime implementation")
    return verified


def stage_root(stage: dict) -> Path:
    return TRIAL_ROOT / stage["artifact_dir"]


def stage_base(stage: dict) -> str:
    return stage["file_base"]


def output_hashes(root: Path, manifest_name: str) -> dict[str, dict[str, str]]:
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            hashes[path.name] = {"path": path.relative_to(ROOT).as_posix(), "sha256": sha256_file(path)}
    return hashes


def write_stage(stage: dict, predecessor_hashes: dict[str, dict[str, str]]) -> dict[str, dict[str, str]]:
    root = stage_root(stage)
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)

    packet_name = f"{stage_base(stage)}.json"
    report_name = f"{stage_base(stage)}_report.json"
    summary_name = f"{stage_base(stage)}_summary.md"
    manifest_name = f"{stage_base(stage)}_manifest.md"

    payload = {
        "decision_id": stage["decision_id"],
        "authorization_id": stage["auth"],
        "status": stage["status"],
        "canonical_packet_name": stage["canonical_packet_name"],
        "human_decision": HUMAN_DECISION,
        "sol_terra_replaces_human_review_for_points_1_to_5": True,
        "requires_bogdan_call_before_point_6": True,
        "source_decision": stage["source"],
        "first_slice_id": "C01WP-01-phase-1-scaffold-contracts",
        "scope": {
            "pages": [f"{page:03d}" for page in range(1, 21)],
            "page_021_plus_included": False,
            "fixture_admission_decision": "G1FADAR-G1-VIRAL-001",
            "actual_extraction_scope": "none_this_layer",
        },
        "readiness_chain_position": STAGES.index(stage) + 1,
        "readiness_chain_total": len(STAGES),
        "stage_summary": stage["summary"],
        "actual_text_extraction_authorized_now": False,
        "actual_text_extraction_executed": False,
        "ocr_execution_authorized_now": False,
        "ocr_execution_performed": False,
        "render_execution_authorized_now": False,
        "render_execution_performed": False,
        "pdf_parsing_authorized_now": False,
        "pdf_text_layer_extraction_authorized_now": False,
        "source_or_raw_mutation_authorized_now": False,
        "runtime_implementation_authorized": False,
        "runtime_start_authorized": False,
        "runtime_execution_authorized": False,
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "runtime_source_profile_lock_granted_for_actual_runtime": False,
        "runtime_source_profile_acceptance_granted_for_actual_runtime": False,
        "translation_or_proofreading_authorized_now": False,
        "page_021_plus_authorized_now": False,
        "admits_new_or_broader_fixture": False,
        "push_performed": False,
        "remaining_blockers": COMMON_BLOCKERS,
        "next_possible_packets": ["call_bogdan_before_point_6_text_extraction_trial"],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": predecessor_hashes,
    }
    if stage["decision_id"] == "C01RSPLADMR-G1-VIRAL-001":
        payload["consumes_blocker"] = "human_review_c01rsplad_required"
    if stage["decision_id"] == "C01RSPETD-G1-VIRAL-001":
        payload["future_extraction_trial_profile_decision_recorded"] = True
        payload["future_extraction_trial_profile_state"] = "bounded_for_future_user_called_trial_only"
    if stage["decision_id"] == "C01TETD-G1-VIRAL-001":
        payload["point_6_status"] = "blocked_until_bogdan_called_and_separately_authorizes_actual_extraction"

    write_json(root / packet_name, payload)
    write_json(
        root / report_name,
        {
            "decision_id": stage["decision_id"],
            "authorization_id": stage["auth"],
            "status": stage["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "actual_text_extraction_authorized_now": False,
            "actual_text_extraction_executed": False,
            "ocr_execution_performed": False,
            "render_execution_performed": False,
            "pdf_text_layer_extraction_authorized_now": False,
            "runtime_implementation_authorized": False,
            "runtime_start_authorized": False,
            "runtime_source_profile_lock_created": False,
            "runtime_source_profile_acceptance_created": False,
            "page_021_plus_authorized_now": False,
            "requires_bogdan_call_before_point_6": True,
            "remaining_blockers": COMMON_BLOCKERS,
            "negative_capability_matrix": payload["negative_capability_matrix"],
        },
    )
    write_text(
        root / summary_name,
        "\n".join(
            [
                f"# {stage['canonical_packet_name']} - {stage['decision_id']}",
                "",
                f"Status: `{stage['status']}`",
                "",
                stage["summary"],
                "",
                "This is points 1-5 readiness material only. It does not run OCR, render, PDF parsing/text-layer extraction, or text extraction.",
                "",
                "Point 6 remains blocked until Bogdan is called and gives separate explicit authorization.",
                "",
                "Boundary:",
                "",
                "- Actual text extraction: `false`.",
                "- OCR/render/PDF parsing/text-layer extraction: `false`.",
                "- Runtime implementation/start/execution: `false`.",
                "- Runtime source-profile lock/acceptance artifact creation: `false`.",
                "- Page 021+: `false`.",
                "- Translation/proofreading: `false`.",
                "- Push: `false`.",
                "",
            ]
        ),
    )
    lines = [
        f"# {stage['canonical_packet_name']} Manifest - {stage['decision_id']}",
        "",
        "Boundary: points 1-5 readiness material only; point 6 actual extraction remains blocked until Bogdan is called.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.name != manifest_name:
            lines.append(f"| `{path.relative_to(root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    write_text(root / manifest_name, "\n".join(lines))
    return output_hashes(root, manifest_name)


def build() -> None:
    predecessor_hashes = verify_inputs()
    for stage in STAGES:
        predecessor_hashes = write_stage(stage, predecessor_hashes)


if __name__ == "__main__":
    check_authorization()
    build()
