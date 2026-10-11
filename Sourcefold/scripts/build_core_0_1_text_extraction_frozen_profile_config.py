from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_core_0_1_text_extraction_frozen_profile_config.py"
TEST_PATH = ROOT / "tests" / "test_core_0_1_text_extraction_frozen_profile_config.py"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
DECISION_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_candidate_profile_decision_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "core_0_1_text_extraction_frozen_profile_config_G1_VIRAL_001"
LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"

CONFIG_ID = "C01TEFPC-G1-VIRAL-001"
AUTHORIZATION_ID = "BA-G1-VIRAL-CORE-0-1-TEXT-EXTRACTION-FROZEN-PROFILE-CONFIG-001"
HUMAN_DECISION = "делай"
SOURCE_DECISION_ID = "C01TECPD-G1-VIRAL-001"
PROFILE_ID = "trim_mask_psm4"

INPUT_HASHES = {
    "C01TECPD-G1-VIRAL-001.packet": (
        DECISION_ROOT / "core_0_1_text_extraction_candidate_profile_decision.json",
        "EE61C584158FDB825E4C567DE86C8B47748B0FB0FE6F05B3BE7DD0E569C19B39",
    ),
    "C01TECPD-G1-VIRAL-001.report": (
        DECISION_ROOT / "core_0_1_text_extraction_candidate_profile_decision_report.json",
        "CD2ADD20A53A018331FFF1AF026AEFDD717AC220D7C09D35EF5D7028BB9E1743",
    ),
    "C01TECPD-G1-VIRAL-001.summary": (
        DECISION_ROOT / "core_0_1_text_extraction_candidate_profile_decision_summary.md",
        "783C323F511BD3E18B4257F95D350C1458BBD712756D214EF571989B4A4CBAEB",
    ),
    "C01TECPD-G1-VIRAL-001.manifest": (
        DECISION_ROOT / "core_0_1_text_extraction_candidate_profile_decision_manifest.md",
        "C7687C4C1C38D101B58713D7E15120A899718826AB6D1EED0B9D4A56A2992724",
    ),
}

NEGATIVE_CAPABILITIES = [
    "ocr_execution",
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
    parser = argparse.ArgumentParser(description="Build Core 0.1 frozen text extraction profile config.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Core 0.1 frozen profile config is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Core 0.1 frozen profile config requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit("Core 0.1 frozen profile config requires the exact bounded human decision")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    ledger = LEDGER.read_text(encoding="utf-8-sig")
    if f"## {AUTHORIZATION_ID}" not in ledger:
        raise SystemExit(f"{AUTHORIZATION_ID} missing from ledger")
    if OUT_ROOT.exists():
        raise SystemExit(f"refusing to overwrite existing output directory: {OUT_ROOT}")

    verified = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    decision = read_json(INPUT_HASHES["C01TECPD-G1-VIRAL-001.packet"][0])
    if decision["decision_id"] != SOURCE_DECISION_ID:
        raise SystemExit("unexpected candidate profile decision input")
    if not decision["candidate_profile_freeze_granted"]:
        raise SystemExit("candidate profile was not frozen by source decision")
    if decision["candidate_profile_id"] != PROFILE_ID:
        raise SystemExit("unexpected frozen candidate profile id")
    if decision["source_profile_acceptance_created"] or decision["runtime_source_profile_lock_created"]:
        raise SystemExit("source decision overclaims source/runtime profile acceptance")
    return verified, decision


def build_config(verified_inputs: dict[str, dict[str, str]], decision: dict) -> dict:
    tuple_ = decision["candidate_profile_tuple"]
    return {
        "config_id": CONFIG_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "text_extraction_frozen_profile_config_recorded_no_ocr_execution",
        "source_candidate_profile_decision": SOURCE_DECISION_ID,
        "human_decision": HUMAN_DECISION,
        "profile_id": PROFILE_ID,
        "profile_tuple": tuple_,
        "ocr_engine": {
            "engine_id": "OCR-G1-VIRAL-TESSERACT-ENG-PSM4-TRIM-MASK-001",
            "executable": "D:/NRI/.tools/tesseract/tesseract.exe",
            "language": tuple_["language"],
            "oem": tuple_["tesseract_oem"],
            "psm": tuple_["tesseract_psm"],
            "args": ["-l", tuple_["language"], "--oem", str(tuple_["tesseract_oem"]), "--psm", str(tuple_["tesseract_psm"]), "txt", "tsv"],
        },
        "preprocessing": {
            "variant": tuple_["preprocessing_variant"],
            "operation": "crop_12px_edge_mask_then_add_12px_white_padding_then_grayscale_autocontrast",
            "source_input_type": "text_evidence_crop_png",
        },
        "allowed_inputs": {
            "pages": ["009", "010", "015"],
            "input_kind": "page_complete_review_text_evidence_crop_png",
            "references": {
                "009": "reference_ocr_verified_text_map",
                "010": "reference_ocr_verified_text_map",
                "015": "reference_text_map_not_ocr_verified",
            },
        },
        "forbidden_inputs": [
            "pdf",
            "pdf_text_layer",
            "full_page_image",
            "visual_anchor",
            "triage_duplicate",
            "raw_source",
            "page_016_plus",
            "page_021_plus",
        ],
        "output_contract": "candidate_only_text_report_manifest_metrics",
        "config_can_drive_replay": True,
        "ocr_execution_performed": False,
        "source_profile_acceptance_created": False,
        "runtime_source_profile_lock_created": False,
        "runtime_source_profile_acceptance_created": False,
        "accepted_text_mutation_performed": False,
        "semantic_text_mutation_performed": False,
        "page_status_mutation_performed": False,
        "page_016_plus_included": False,
        "page_021_plus_included": False,
        "push_performed": False,
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(config: dict) -> None:
    lines = [
        "# Core 0.1 Text Extraction Frozen Profile Config - C01TEFPC-G1-VIRAL-001",
        "",
        "Status: `text_extraction_frozen_profile_config_recorded_no_ocr_execution`",
        "",
        "This artifact records the reusable Core 0.1 text extraction candidate profile config.",
        "",
        "It does not run OCR and does not create OCR/source/runtime acceptance.",
        "",
        "## Profile",
        "",
        "- Profile id: `trim_mask_psm4`.",
        "- Preprocessing: `edge_mask_trim`.",
        "- Tesseract: `-l eng --oem 1 --psm 4 txt tsv`.",
        "- Allowed inputs: text-evidence crop PNGs for P009/P010/P015 replay.",
        "- P015 reference label: `reference_text_map_not_ocr_verified`.",
        "",
        "## Boundary",
        "",
        "- OCR execution: `false`.",
        "- Source/runtime profile acceptance: `false`.",
        "- Accepted/semantic/page-status mutation: `false`.",
        "- PDF/render/runtime/page 016+/page 021+/push: `false`.",
        "",
    ]
    write_text(OUT_ROOT / "core_0_1_text_extraction_frozen_profile_config_summary.md", "\n".join(lines))


def write_report(config: dict) -> None:
    write_json(
        OUT_ROOT / "core_0_1_text_extraction_frozen_profile_config_report.json",
        {
            "config_id": CONFIG_ID,
            "authorization_id": AUTHORIZATION_ID,
            "status": config["status"],
            "generator_script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "generator_script_sha256": sha256_file(SCRIPT_PATH),
            "test_contract": TEST_PATH.relative_to(ROOT).as_posix(),
            "test_contract_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
            "source_candidate_profile_decision": SOURCE_DECISION_ID,
            "profile_id": PROFILE_ID,
            "profile_tuple": config["profile_tuple"],
            "config_can_drive_replay": True,
            "ocr_execution_performed": False,
            "source_profile_acceptance_created": False,
            "runtime_source_profile_lock_created": False,
            "accepted_text_mutation_performed": False,
            "semantic_text_mutation_performed": False,
            "page_status_mutation_performed": False,
            "page_021_plus_included": False,
            "push_performed": False,
            "negative_capability_matrix": config["negative_capability_matrix"],
        },
    )


def write_manifest() -> None:
    manifest_name = "core_0_1_text_extraction_frozen_profile_config_manifest.md"
    lines = [
        "# Core 0.1 Text Extraction Frozen Profile Config Manifest - C01TEFPC-G1-VIRAL-001",
        "",
        "Boundary: config artifact only; no OCR execution or acceptance mutation.",
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
    OUT_ROOT.mkdir(parents=True, exist_ok=False)
    config = build_config(verified_inputs, decision)
    write_json(OUT_ROOT / "core_0_1_text_extraction_frozen_profile_config.json", config)
    write_summary(config)
    write_report(config)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
