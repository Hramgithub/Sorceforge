from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_gate_1_fixture_admission_readiness_prep.py"
TEST_PATH = ROOT / "tests" / "test_gate_1_fixture_admission_readiness_prep.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
G1SPDR_ROOT = TRIAL_ROOT / "gate_1_source_profile_decision_record_G1_VIRAL_001"
G1SP17_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_017"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_readiness_prep_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-GATE-1-READINESS-PREP-001"
PACKET_ID = "G1FARP-G1-VIRAL-001"

INPUT_HASHES = {
    "G1SPDR-G1-VIRAL-001.record": (
        G1SPDR_ROOT / "gate_1_source_profile_decision_record.json",
        "E00E17879BE98340A00582B8C128E8C1C7C984657FDC142513447618591691C1",
    ),
    "G1SPDR-G1-VIRAL-001.report": (
        G1SPDR_ROOT / "gate_1_source_profile_decision_record_report.json",
        "15EA6C81E2269D0289549C0BC682418CE581D8391EB07D20759461CF436BB125",
    ),
    "G1SPDR-G1-VIRAL-001.summary": (
        G1SPDR_ROOT / "gate_1_source_profile_decision_record_summary.md",
        "8E4A21C9EF5AD8661867F5D12A285EBA3DC54282BECA644CABBCBDE4E5A1EA26",
    ),
    "G1SPDR-G1-VIRAL-001.manifest": (
        G1SPDR_ROOT / "gate_1_source_profile_decision_record_manifest.md",
        "E2908F97C39BB32F317B318E76286E06375A3637C30A367C2A20C2CDEEBA8C1D",
    ),
    "G1SP-G1-VIRAL-017.packet": (
        G1SP17_ROOT / "gate_1_status_packet.json",
        "DA9B421CD8A5BC503FCCEE24F6043FBCEC9F86262AF3E9E9018C460D871E4ED6",
    ),
    "G1SP-G1-VIRAL-017.report": (
        G1SP17_ROOT / "gate_1_status_report.json",
        "007F7F1F6FC73FC4F9B9268CB3969F895517D20B054FCC1D787851E4609D2F68",
    ),
    "G1SP-G1-VIRAL-017.summary": (
        G1SP17_ROOT / "gate_1_status_summary.md",
        "FF3F3D7F9F3EA0352C95448124821DE2C2255E63DCFEB9D6879A6EA722166CF3",
    ),
    "G1SP-G1-VIRAL-017.manifest": (
        G1SP17_ROOT / "gate_1_status_manifest.md",
        "4A7DDDC454034FC8CFC75C184856B66D27B17ECEA0E5E8447C331B07CCD381A9",
    ),
}

NEGATIVE_CAPABILITIES = [
    "source_profile_acceptance",
    "whole_gate_1_acceptance",
    "fixture_admission",
    "fixture_manifest_creation",
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
    parser = argparse.ArgumentParser(description="Build Gate 1 fixture/Gate acceptance readiness prep.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 fixture admission readiness prep is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 fixture admission readiness prep requires {AUTHORIZATION_ID}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict, dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")

    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    decision_record = read_json(INPUT_HASHES["G1SPDR-G1-VIRAL-001.record"][0])
    status_packet = read_json(INPUT_HASHES["G1SP-G1-VIRAL-017.packet"][0])
    if decision_record["record_id"] != "G1SPDR-G1-VIRAL-001":
        raise SystemExit("unexpected decision record")
    if decision_record["accepts_source_profile"] or decision_record["accepts_whole_gate_1"]:
        raise SystemExit("decision record is too broad")
    if decision_record["admits_fixture"] or decision_record["processes_page_021_plus"]:
        raise SystemExit("decision record unexpectedly admits fixtures or processes page 021+")
    if status_packet["status_packet_id"] != "G1SP-G1-VIRAL-017":
        raise SystemExit("unexpected status packet")
    return verified, decision_record, status_packet


def build_packet(verified_inputs: dict[str, dict[str, str]], decision_record: dict, status_packet: dict) -> dict:
    decisions = decision_record["decisions"]
    candidate_rows = [row["source_matrix_row_id"] for row in decisions if row["creates_gate_review_candidate_status"]]
    parked_rows = [row for row in decisions if row["creates_parking_decision"]]
    evidence_rows = [row["source_matrix_row_id"] for row in decisions if row["decision"] == "kept_evidence_only_not_accepting"]
    blocked_rows = [row["source_matrix_row_id"] for row in decisions if row["decision"] == "held_blocked_needs_future_decision"]
    separate_ba_rows = [row["source_matrix_row_id"] for row in decisions if row["decision"] == "requires_separate_bounded_authorization"]

    return {
        "packet_id": PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_fixture_admission_readiness_prep_ready_for_review",
        "purpose": "fixture_admission_and_whole_gate_acceptance_readiness_prep_only",
        "source_decision_record": decision_record["record_id"],
        "source_status_packet": status_packet["status_packet_id"],
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "creates_new_parking_decision": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "accepted_gate_review_candidate_rows": candidate_rows,
        "parked_ocr_methodology_rows": [
            {
                "source_matrix_row_id": row["source_matrix_row_id"],
                "parking_scope": row["parking_scope"],
                "invalidation_conditions": row["invalidation_conditions"],
            }
            for row in parked_rows
        ],
        "evidence_only_rows": evidence_rows,
        "blocked_rows": blocked_rows,
        "page_021_plus_boundary": {
            "rows": separate_ba_rows,
            "requires_separate_bounded_authorization": True,
            "included_in_this_packet": False,
        },
        "readiness_rows": [
            {
                "row_id": "fixture_admission_readiness",
                "status": "not_ready_requires_future_decision",
                "present_evidence": [
                    "G1SPDR gate-review candidate rows",
                    "G1SP-G1-VIRAL-017 pages 001-020 page-complete accepted-only status",
                    "render/source reconstruction evidence kept non-accepting",
                ],
                "missing_or_blocked": [
                    "fixture admission decision",
                    "fixture strategy fit check",
                    "unsupported/negative fixture policy decision",
                    "whole Gate 1 acceptance decision",
                ],
            },
            {
                "row_id": "unsupported_negative_fixture_policy",
                "status": "blocked_needs_future_decision",
                "present_evidence": ["G1SPDR keeps unsupported/negative fixture row blocked"],
                "missing_or_blocked": ["future explicit unsupported/negative fixture policy decision"],
            },
            {
                "row_id": "whole_gate_1_acceptance_readiness",
                "status": "not_ready_requires_future_decision",
                "present_evidence": ["G1SPDR candidate/parking/evidence-only decisions"],
                "missing_or_blocked": [
                    "fixture admission decision",
                    "whole Gate 1 acceptance decision",
                    "page 021+ disposition remains separate",
                ],
            },
        ],
        "remaining_actual_decisions": [
            "fixture_admission",
            "whole_gate_1_acceptance",
            "unsupported_profiles_and_negative_fixtures_acceptance_or_fixture_policy",
            "page_021_plus_disposition",
        ],
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(packet: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Readiness Prep - G1FARP-G1-VIRAL-001",
        "",
        "Status: `gate_1_fixture_admission_readiness_prep_ready_for_review`",
        "",
        "Purpose: readiness prep only for future fixture admission and whole Gate 1 acceptance decisions.",
        "",
        "## Inputs Preserved",
        "",
        f"- `{len(packet['accepted_gate_review_candidate_rows'])}` Gate review candidate rows from `G1SPDR-G1-VIRAL-001`.",
        f"- `{len(packet['parked_ocr_methodology_rows'])}` existing Core 0.1 OCR parking outcomes with invalidation conditions.",
        f"- `{len(packet['evidence_only_rows'])}` render/source-reconstruction evidence-only rows.",
        f"- `{len(packet['blocked_rows'])}` blocked rows.",
        "- Page 021+ remains separate bounded authorization only.",
        "",
        "## Readiness",
        "",
    ]
    for row in packet["readiness_rows"]:
        lines.append(f"- `{row['row_id']}`: `{row['status']}`")
    lines.extend(
        [
            "",
            "## Boundaries",
            "",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No whole source-profile acceptance.",
            "- No page 021+ processing or authorization.",
            "- No OCR execution or remediation rerun.",
            "- No source/OCR/render/PDF/raw mutation.",
            "- No translation, proofreading, implementation, or push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_fixture_admission_readiness_prep_summary.md", "\n".join(lines))


def write_report(packet: dict) -> None:
    write_json(
        OUT_ROOT / "gate_1_fixture_admission_readiness_prep_report.json",
        {
            "packet_id": PACKET_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": packet["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "admits_fixture": False,
            "creates_fixture_manifest": False,
            "accepts_whole_gate_1": False,
            "accepts_source_profile": False,
            "creates_new_parking_decision": False,
            "processes_page_021_plus": False,
            "executes_ocr": False,
            "negative_capability_matrix": packet["negative_capability_matrix"],
            "remaining_actual_decisions": packet["remaining_actual_decisions"],
        },
    )


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_admission_readiness_prep_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Readiness Prep Manifest - G1FARP-G1-VIRAL-001",
        "",
        "Status: `gate_1_fixture_admission_readiness_prep_ready_for_review`",
        "",
        "Boundary: readiness prep only; no fixture admission, no fixture manifest creation, no page 021+ authorization, and no whole Gate 1 acceptance.",
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
    verified_inputs, decision_record, status_packet = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet(verified_inputs, decision_record, status_packet)
    write_json(OUT_ROOT / "gate_1_fixture_admission_readiness_prep.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
