from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_source_profile_decision_record.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_source_profile_decision_record.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PACKET_ROOT = TRIAL_ROOT / "gate_1_source_profile_decision_packet_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_source_profile_decision_record_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-SOURCE-PROFILE-DECISION-RECORD-001"
RECORD_ID = "G1SPDR-G1-VIRAL-001"

PROPOSED_PHRASE = (
    "G1SPDP accepted as options packet; prepare Gate 1 source-profile decision record with: "
    "accept 5 selected source-profile elements as Gate review candidates; park 2 OCR methodology/debt "
    "items for Core 0.1 with invalidation conditions; keep 2 render/source reconstruction rows evidence-only; "
    "keep unsupported/negative fixtures and whole Gate 1 blocked; P021+ requires separate BA; no fixture "
    "admission, no whole Gate 1 acceptance, no push"
)

INPUT_HASHES = {
    "G1SPDP-G1-VIRAL-001.packet": (
        PACKET_ROOT / "gate_1_source_profile_decision_packet.json",
        "CB528844A71328F8E7C8A281BF67243F292B1C53E991B48B42DF6C51313FD21E",
    ),
    "G1SPDP-G1-VIRAL-001.report": (
        PACKET_ROOT / "gate_1_source_profile_decision_packet_report.json",
        "AB04F38ECFA9C5384639A5B573ABB1F0F907E9CD38B4649479BB8BE0E36BE6AB",
    ),
    "G1SPDP-G1-VIRAL-001.summary": (
        PACKET_ROOT / "gate_1_source_profile_decision_packet_summary.md",
        "86D8752B5557AC5E643285BBA4911DFA801B0978BACBF7226A45140E7E8D8CA5",
    ),
    "G1SPDP-G1-VIRAL-001.manifest": (
        PACKET_ROOT / "gate_1_source_profile_decision_packet_manifest.md",
        "F58ED5D8F8F585E792A4A80330B69434C0207DAFEABAFAF2CADBB4B5EFEDFB89",
    ),
}

NEGATIVE_CAPABILITIES = [
    "source_profile_acceptance",
    "whole_gate_1_acceptance",
    "fixture_admission",
    "ocr_execution",
    "ocr_remediation_execution",
    "page_021_plus_processing",
    "source_mutation",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "translation",
    "proofreading",
    "renderer_profile_acceptance",
    "implementation",
    "push",
]

DECISION_MAP = {
    "accept_for_gate_review_candidate": "accepted_for_gate_review_candidate_status",
    "park_for_0_1_with_invalidation_conditions": "parked_for_core_0_1_with_invalidation_conditions",
    "remain_evidence_only_not_accepting": "kept_evidence_only_not_accepting",
    "hold_blocked_needs_decision": "held_blocked_needs_future_decision",
    "requires_separate_bounded_authorization": "requires_separate_bounded_authorization",
}


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
    parser = argparse.ArgumentParser(description="Build Gate 1 source-profile decision record.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 source-profile decision record is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 source-profile decision record requires {AUTHORIZATION_ID}")


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

    packet = read_json(INPUT_HASHES["G1SPDP-G1-VIRAL-001.packet"][0])
    if packet["packet_id"] != "G1SPDP-G1-VIRAL-001":
        raise SystemExit("unexpected source decision packet")
    if packet["accepts_source_profile"] or packet["creates_parking_decision"]:
        raise SystemExit("source options packet unexpectedly already decides")
    if packet["accepts_whole_gate_1"] or packet["admits_fixture"] or packet["processes_page_021_plus"]:
        raise SystemExit("source options packet boundary is too broad")
    return verified, packet


def decision_for_row(row: dict) -> dict:
    prep_category = row["decision_prep_category"]
    disposition = DECISION_MAP[prep_category]
    creates_parking = disposition == "parked_for_core_0_1_with_invalidation_conditions"
    return {
        "source_matrix_row_id": row["source_matrix_row_id"],
        "source_matrix_disposition": row["source_matrix_disposition"],
        "decision": disposition,
        "category": row["category"],
        "basis": row["basis"],
        "creates_source_profile_acceptance": False,
        "creates_gate_review_candidate_status": disposition == "accepted_for_gate_review_candidate_status",
        "creates_parking_decision": creates_parking,
        "parking_scope": "core_0_1_only" if creates_parking else None,
        "invalidation_conditions": [
            "new OCR benchmark evidence contradicts OCRHM-G1-VIRAL-001",
            "page 021+ introduces a required OCR methodology blocker",
            "Gate 1 authority decides OCR methodology must be accepted rather than parked",
        ]
        if creates_parking
        else [],
    }


def build_record(verified_inputs: dict[str, dict[str, str]], packet: dict) -> dict:
    decisions = [decision_for_row(row) for row in packet["decision_rows"]]
    counts = {
        "accepted_for_gate_review_candidate_status": 0,
        "parked_for_core_0_1_with_invalidation_conditions": 0,
        "kept_evidence_only_not_accepting": 0,
        "held_blocked_needs_future_decision": 0,
        "requires_separate_bounded_authorization": 0,
    }
    for decision in decisions:
        counts[decision["decision"]] += 1

    return {
        "record_id": RECORD_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_source_profile_decision_record_created",
        "purpose": "bounded_source_profile_candidate_and_parking_decision_record",
        "authority_provenance": {
            "assistant_proposed_phrase": PROPOSED_PHRASE,
            "bogdan_reply_raw": "ok",
            "bogdan_reply_display": "ок",
            "interpretation": "contextual approval of the immediately preceding proposed G1SPDP decision phrase",
            "not_recorded_as_verbatim_long_phrase": True,
        },
        "source_options_packet": packet["packet_id"],
        "controlling_review": packet["controlling_review"],
        "accepts_source_profile": False,
        "creates_gate_review_candidate_status": True,
        "creates_parking_decision": True,
        "parking_decision_scope": "OCR methodology/debt only for Core 0.1, with invalidation conditions",
        "accepts_whole_gate_1": False,
        "admits_fixture": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "decision_counts": counts,
        "decisions": decisions,
        "remaining_actual_decisions": [
            "fixture_admission",
            "page_021_plus_disposition",
            "whole_gate_1_acceptance",
            "unsupported_profiles_and_negative_fixtures_acceptance_or_fixture_policy",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(record: dict) -> None:
    counts = record["decision_counts"]
    lines = [
        "# Gate 1 Source-Profile Decision Record - G1SPDR-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_profile_decision_record_created`",
        "",
        "Authority: Bogdan replied `ок` to the immediately preceding proposed G1SPDP decision phrase. The long phrase is preserved as the assistant proposal, not as Bogdan's verbatim text.",
        "",
        "## Recorded Decisions",
        "",
        f"- `{counts['accepted_for_gate_review_candidate_status']}` rows accepted as Gate review candidates only.",
        f"- `{counts['parked_for_core_0_1_with_invalidation_conditions']}` OCR methodology/debt rows parked for Core 0.1 with invalidation conditions.",
        f"- `{counts['kept_evidence_only_not_accepting']}` render/source-reconstruction rows kept evidence-only.",
        f"- `{counts['held_blocked_needs_future_decision']}` rows held blocked for future decision.",
        f"- `{counts['requires_separate_bounded_authorization']}` page 021+ row still requires separate bounded authorization.",
        "",
        "## Boundaries",
        "",
        "- No whole source-profile acceptance.",
        "- No fixture admission.",
        "- No whole Gate 1 acceptance.",
        "- No page 021+ processing or authorization.",
        "- No OCR execution or remediation rerun.",
        "- No source/OCR/render/PDF/raw mutation.",
        "- No translation, proofreading, implementation, or push.",
        "",
    ]
    write_text(OUT_ROOT / "gate_1_source_profile_decision_record_summary.md", "\n".join(lines))


def write_report(record: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_source_profile_decision_record_report.json",
        {
            "record_id": RECORD_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": record["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "accepts_source_profile": False,
            "creates_gate_review_candidate_status": True,
            "creates_parking_decision": True,
            "accepts_whole_gate_1": False,
            "admits_fixture": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "decision_counts": record["decision_counts"],
            "negative_capability_matrix": record["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_source_profile_decision_record_manifest.md"
    lines = [
        "# Gate 1 Source-Profile Decision Record Manifest - G1SPDR-G1-VIRAL-001",
        "",
        "Status: `gate_1_source_profile_decision_record_created`",
        "",
        "Boundary: source-profile Gate review candidate and Core 0.1 OCR parking decision record only; no fixture admission, page 021+ authorization, or whole Gate 1 acceptance.",
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
    record = build_record(verified_inputs, packet)
    write_json(OUT_ROOT / "gate_1_source_profile_decision_record.json", record)
    write_summary(record)
    write_report(record)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
