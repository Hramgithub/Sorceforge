from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "build_page_map_readiness.py"
TEST_PATH = ROOT / "tests" / "test_page_map_readiness.py"
AUTHORIZATION_LEDGER = ROOT / "docs" / "plans" / "20260715-sourcefold-phase-0-release-charter" / "bounded_trial_authorizations.md"
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PRM_REPORT = TRIAL_ROOT / "provisional_region_map_report.md"
PIPELINE_ID = "page_map_readiness_pipeline_v0"

PRM_REPORT_SHA256 = "A37F734D9D1B9DA1456FE7C3D5804D70FE352DB7197495843561B40D7A4DD35C"

PAGE_PROFILES: dict[str, dict[str, Any]] = {
    "002": {
        "source_kind": "assisted_draft_verified_rollup",
        "authorization_id": "BA-G1-VIRAL-PAGE-MAP-READINESS-PIPELINE-PILOT-002-001",
        "package_id": "PMRP-G1-VIRAL-P002-001",
        "profile_id": "page_map_profile_G1_VIRAL_P002_v0",
        "page_label": "Page 002",
        "page_id": "PG-G1-VIRAL-P002",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P002",
        "input_packages": ["PRM-G1-VIRAL-001", "SRAD-G1-VIRAL-002", "SRADV-G1-VIRAL-002", "P002C-G1-VIRAL-002"],
        "output_dir": TRIAL_ROOT / "page_map_readiness_p002_G1_VIRAL_001",
        "predecessors": {
            "prm_report": {"path": PRM_REPORT, "sha256": PRM_REPORT_SHA256},
            "assisted_draft_report": {
                "path": TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_G1_VIRAL_001" / "source_reconstruction_p002_assisted_draft_report.json",
                "sha256": "296763B5942B937B66822E4988C30FF5B96FBFBFF08952987FA5E8D22CE07F05",
                "expected_id_key": "draft_id",
                "expected_id": "SRAD-G1-VIRAL-002",
            },
            "verification_report": {
                "path": TRIAL_ROOT / "source_reconstruction_p002_assisted_draft_verify_G1_VIRAL_001" / "source_reconstruction_p002_assisted_draft_verify_report.json",
                "sha256": "BC248426E89709A2D028A68C69ACE24764A48DDEB61BC51DBD0BDA3413F84F52",
                "expected_id_key": "verification_id",
                "expected_id": "SRADV-G1-VIRAL-002",
            },
            "source_rollup_report": {
                "path": TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001" / "p002_completion_and_next_review_report.json",
                "sha256": "A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F",
                "expected_id_key": "package_id",
                "expected_id": "P002C-G1-VIRAL-002",
            },
            "source_rollup_manifest": {
                "path": TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001" / "p002_completion_and_next_review_manifest.md",
                "sha256": "8CF3BA7D578D1445C33833481325C57AD92711FBC2EC1585B6436E40B4F54DB6",
            },
        },
        "expected_blocks": [
            {
                "block_id": "P002-B001",
                "block_type": "text",
                "role": "credits",
                "source_region_id": "PRM-G1-VIRAL-001-P002-R01",
                "reading_order": 1,
                "required": True,
                "semantic_expectations": ["credits_title", "credit_role_label", "credit_value_list"],
                "protected_tokens": [
                    "Credits",
                    "Alex Guillotte",
                    "Buds RPG Review",
                    "Matthew Pook",
                    "Keith Mageau",
                    "Luca Alexander Volpino",
                    "Seth Skorkowsky",
                ],
            },
            {
                "block_id": "P002-B002",
                "block_type": "text",
                "role": "boxed_legal_footer",
                "source_region_id": "PRM-G1-VIRAL-001-P002-R02",
                "reading_order": 2,
                "required": True,
                "semantic_expectations": [
                    "special_thanks_sentence",
                    "special_thanks_body",
                    "copyright_notice",
                    "trademark_notice",
                    "publisher_url",
                    "logo_license_notice",
                ],
                "protected_tokens": [
                    "Seth Skorkowsky",
                    "Viral",
                    "2022",
                    "Alex Guillotte",
                    "Buds RPG Review",
                    "Call of Cthulhu",
                    "Chaosium Inc.",
                    "OBS Community Content",
                    "www.Chaosium.com",
                    "Miskatonic Repository Logo",
                ],
            },
        ],
        "declared_none": ["art", "inset", "table", "title_only", "unknown", "missing", "context_only"],
    },
    "003": {
        "source_kind": "verified_review_acceptance",
        "authorization_id": "BA-G1-VIRAL-PAGE-MAP-READINESS-P003-001",
        "package_id": "PMRP-G1-VIRAL-P003-001",
        "profile_id": "page_map_profile_G1_VIRAL_P003_v0",
        "page_label": "Page 003",
        "page_id": "PG-G1-VIRAL-P003",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P003",
        "input_packages": ["PRM-G1-VIRAL-001", "P002C-G1-VIRAL-002", "P003A-G1-VIRAL-003"],
        "output_dir": TRIAL_ROOT / "page_map_readiness_p003_G1_VIRAL_001",
        "expected_source_acceptance_status": "accepted_two_page_003_records_only",
        "predecessors": {
            "prm_report": {"path": PRM_REPORT, "sha256": PRM_REPORT_SHA256},
            "review_seed_report": {
                "path": TRIAL_ROOT / "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001" / "p002_completion_and_next_review_report.json",
                "sha256": "A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F",
                "expected_id_key": "package_id",
                "expected_id": "P002C-G1-VIRAL-002",
            },
            "verified_acceptance_report": {
                "path": TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001" / "p003_verified_review_acceptance_report.json",
                "sha256": "9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B",
                "expected_id_key": "package_id",
                "expected_id": "P003A-G1-VIRAL-003",
            },
            "verified_acceptance_manifest": {
                "path": TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001" / "p003_verified_review_acceptance_manifest.md",
                "sha256": "F20455232585B442E0E1AAD31F1D02A954B99B6CC6E15CC132A09ED5E9332F87",
            },
            "verified_acceptance_summary": {
                "path": TRIAL_ROOT / "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001" / "p003_verified_review_acceptance_summary.md",
                "sha256": "860A89BF62DDBBEA589055EAF226FEFA3D7BADCA3D68768E6925548F6C12B0F2",
            },
        },
        "expected_blocks": [
            {
                "block_id": "P003-B001",
                "block_type": "text",
                "role": "title_heading_like",
                "source_region_id": "PRM-G1-VIRAL-001-P003-R01",
                "source_review_id": "SRCR-G1-VIRAL-003-R01",
                "reading_order": 1,
                "required": True,
                "semantic_expectations": ["title_heading_like"],
                "protected_tokens": ["SPEKTRAL", "KREW"],
            },
            {
                "block_id": "P003-B002",
                "block_type": "text",
                "role": "main_body_text",
                "source_region_id": "PRM-G1-VIRAL-001-P003-R02",
                "source_review_id": "SRCR-G1-VIRAL-003-R02",
                "reading_order": 2,
                "required": True,
                "semantic_expectations": ["body_text"],
                "protected_tokens": [
                    "Italy baby",
                    "Maya",
                    "one million sub mark",
                    "Poveglia",
                    "Order of the Lamb",
                    "Living Jesus",
                    "Eye-talian Navy",
                    "Hyeon",
                    "second World War",
                    "A1",
                    "OK - so any questions?",
                ],
            },
        ],
        "declared_none": ["art", "inset", "table", "unknown", "missing", "context_only"],
    },
    "004": {
        "source_kind": "verified_review_acceptance",
        "authorization_id": "BA-G1-VIRAL-PAGE-MAP-READINESS-P004-001",
        "package_id": "PMRP-G1-VIRAL-P004-001",
        "profile_id": "page_map_profile_G1_VIRAL_P004_v0",
        "page_label": "Page 004",
        "page_id": "PG-G1-VIRAL-P004",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P004",
        "input_packages": ["PRM-G1-VIRAL-001", "P004A-G1-VIRAL-004", "P004COD-G1-VIRAL-001"],
        "output_dir": TRIAL_ROOT / "page_map_readiness_p004_G1_VIRAL_001",
        "expected_source_acceptance_status": "accepted_two_page_004_records_only",
        "predecessors": {
            "prm_report": {"path": PRM_REPORT, "sha256": PRM_REPORT_SHA256},
            "review_seed_report": {
                "path": TRIAL_ROOT / "source_reconstruction_next_slice_G1_VIRAL_004" / "source_reconstruction_next_slice_report.json",
                "sha256": "C3441CEA1C3F68200BD7134882A00C303D3B549EA94FE87FE4E17C79A6A0475A",
                "expected_id_key": "package_id",
                "expected_id": "SRCR-G1-VIRAL-004",
            },
            "verified_acceptance_report": {
                "path": TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001" / "p004_verified_review_acceptance_report.json",
                "sha256": "0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E",
                "expected_id_key": "package_id",
                "expected_id": "P004A-G1-VIRAL-004",
            },
            "verified_acceptance_manifest": {
                "path": TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001" / "p004_verified_review_acceptance_manifest.md",
                "sha256": "75C0C0BD96FF77E64D2F7C827D7D21B12F7EF15964E8EC9734F9428CCC064C06",
            },
            "verified_acceptance_summary": {
                "path": TRIAL_ROOT / "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001" / "p004_verified_review_acceptance_summary.md",
                "sha256": "BF664162A899765C3B614F87002792D213D70DB82A7ED4142686AA439D50C64C",
            },
            "context_only_confirmation_report": {
                "path": TRIAL_ROOT / "page_004_context_only_confirmation_G1_VIRAL_001" / "page_004_context_only_confirmation_report.json",
                "sha256": "03EBA061301B182976158EC061178AC1BEA3F4C22697B03ACA511CE805E1B349",
                "expected_id_key": "package_id",
                "expected_id": "P004COD-G1-VIRAL-001",
            },
            "context_only_confirmation_manifest": {
                "path": TRIAL_ROOT / "page_004_context_only_confirmation_G1_VIRAL_001" / "page_004_context_only_confirmation_manifest.md",
                "sha256": "A812C7BCB0E82787D48822DE98A757603EACE40833706998487AAF7EA6CFB3A7",
            },
        },
        "expected_blocks": [
            {
                "block_id": "P004-B001",
                "block_type": "text",
                "role": "warning_title",
                "source_region_id": "PRM-G1-VIRAL-001-P004-R02",
                "source_review_id": "SRCR-G1-VIRAL-004-R01",
                "reading_order": 1,
                "required": True,
                "semantic_expectations": ["warning_title"],
                "protected_tokens": ["WARNING"],
            },
            {
                "block_id": "P004-B002",
                "block_type": "text",
                "role": "safety_warning_body",
                "source_region_id": "PRM-G1-VIRAL-001-P004-R03",
                "source_review_id": "SRCR-G1-VIRAL-004-R02",
                "reading_order": 2,
                "required": True,
                "semantic_expectations": ["safety_warning_body"],
                "protected_tokens": [
                    "mature audiences",
                    "real life trauma",
                    "secret vote",
                    "safe word",
                    "fading to black",
                    "Sanity loss",
                    "roleplaying games",
                ],
            },
        ],
        "declared_none": ["art", "table", "unknown", "missing"],
        "context_only_regions": [
            {
                "source_region_id": "PRM-G1-VIRAL-001-P004-R01",
                "status": "context_only_not_peer_crop_record",
                "reason": "Full tilted inset contains the accepted title/body regions and would overlap peer crops.",
            }
        ],
    },
    "005": {
        "source_kind": "human_review_qa_fixture_slice",
        "authorization_id": "BA-G1-VIRAL-PAGE-MAP-READINESS-P005-001",
        "package_id": "PMRP-G1-VIRAL-P005-001",
        "profile_id": "page_map_profile_G1_VIRAL_P005_v0",
        "page_label": "Page 005",
        "page_id": "PG-G1-VIRAL-P005",
        "image_id": "IMG-G1-VIRAL-RENDER-001-P005",
        "page_image": "fixtures/candidate_inputs/viral/render_trials/RT-G1-VIRAL-RENDER-001/images/page_005.png",
        "page_image_sha256": "0E60ECF12F10657851617AB9F2467DDF7B8CC6C5AE52EF6A7FF960873C0C93BE",
        "input_packages": [
            "PRM-G1-VIRAL-001",
            "SRHR-G1-VIRAL-001",
            "SRQA-G1-VIRAL-001",
            "SRFA-G1-VIRAL-001",
        ],
        "output_dir": TRIAL_ROOT / "page_map_readiness_p005_G1_VIRAL_001",
        "predecessors": {
            "prm_report": {"path": PRM_REPORT, "sha256": PRM_REPORT_SHA256},
            "human_review_report": {
                "path": TRIAL_ROOT
                / "source_reconstruction_human_review_G1_VIRAL_001"
                / "source_reconstruction_human_review_report.json",
                "sha256": "FF7C9778E711D67964584CD00870762FD7ADE47E4368EA71DD3C373AB5EB4980",
                "expected_id_key": "review_id",
                "expected_id": "SRHR-G1-VIRAL-001",
            },
            "qa_report": {
                "path": TRIAL_ROOT / "source_reconstruction_qa_G1_VIRAL_001" / "source_reconstruction_qa_report.json",
                "sha256": "A98811F3368FD468618A111D9F7A85BFFBD72CE9387CCF11DA011875C80553E0",
                "expected_id_key": "qa_id",
                "expected_id": "SRQA-G1-VIRAL-001",
            },
            "fixture_admission_report": {
                "path": TRIAL_ROOT
                / "source_reconstruction_fixture_admission_G1_VIRAL_001"
                / "source_reconstruction_fixture_admission_report.json",
                "sha256": "485ECEAAC7CC1CC3FBE95341ED7A0F5E68345EF59CCC8CEB7F8F57706A541A1C",
                "expected_id_key": "admission_id",
                "expected_id": "SRFA-G1-VIRAL-001",
            },
            "admitted_fixtures": {
                "path": TRIAL_ROOT
                / "source_reconstruction_fixture_admission_G1_VIRAL_001"
                / "source_reconstruction_admitted_fixtures.json",
                "sha256": "1B9DA0A5BF9E219059065F3C1517B4C0E1265060F578F1C6007E9C2AA1611B9F",
            },
        },
        "expected_blocks": [
            {
                "block_id": "P005-B001",
                "block_type": "text",
                "role": "contents_heading",
                "source_region_id": "PRM-G1-VIRAL-001-P005-R01",
                "region_id": "RG-G1-VIRAL-P005-R001",
                "region_admission_id": "SRA-G1-VIRAL-001-R002",
                "reading_order": 1,
                "required": True,
                "box_px": [920, 260, 750, 280],
                "semantic_expectations": ["heading"],
                "protected_tokens": ["Contents"],
            },
            {
                "block_id": "P005-B002",
                "block_type": "text",
                "role": "contents_entry_group",
                "source_region_id": "PRM-G1-VIRAL-001-P005-R02",
                "region_id": "RG-G1-VIRAL-P005-R002",
                "region_admission_id": "SRA-G1-VIRAL-001-R003",
                "reading_order": 2,
                "required": True,
                "box_px": [260, 600, 2050, 2300],
                "semantic_expectations": ["table_list_entry_group"],
                "protected_tokens": ["Introduction", "Summary", "Overview", "The Spektral Krew"],
            },
        ],
        "declared_none": ["art", "inset", "unknown", "missing"],
        "context_only_regions": [
            {
                "source_region_id": "PRM-G1-VIRAL-001-P005-R03",
                "status": "visual_exclusion_not_source_text_record",
                "reason": "Margin page marker/layout component is accepted as a visual-only exclusion, not source text.",
            }
        ],
    },
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8", newline="\n")


def normalized_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def text_metrics(text: str) -> dict[str, int]:
    normalized = normalized_text(text)
    return {
        "character_count": len(text),
        "normalized_character_count": len(normalized),
        "line_count": len(text.splitlines()),
        "non_empty_line_count": sum(1 for line in text.splitlines() if line.strip()),
    }


def check_authorization(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a reusable page_map readiness packet for an authorized page profile.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--page", required=True)
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("page_map readiness pipeline is fail-closed; pass --execute with exact authorization id")
    if args.page not in PAGE_PROFILES:
        raise SystemExit(f"no page_map profile exists for page {args.page}")
    expected_auth = PAGE_PROFILES[args.page]["authorization_id"]
    if args.authorization_id != expected_auth:
        raise SystemExit(f"page_map readiness pipeline requires {expected_auth}")
    return args


def verify_authorization_ledger(authorization_id: str) -> None:
    ledger = AUTHORIZATION_LEDGER.read_text(encoding="utf-8-sig")
    if f"## {authorization_id}" not in ledger:
        raise SystemExit(f"{authorization_id} is missing from bounded trial authorization ledger")


def verify_predecessors(profile: dict[str, Any]) -> dict[str, Any]:
    verify_authorization_ledger(profile["authorization_id"])
    for predecessor in profile["predecessors"].values():
        path = predecessor["path"]
        expected_hash = predecessor["sha256"]
        if sha256_file(path) != expected_hash:
            raise SystemExit(f"predecessor hash mismatch: {path.relative_to(ROOT).as_posix()}")

    if profile["source_kind"] == "assisted_draft_verified_rollup":
        srad = read_json(profile["predecessors"]["assisted_draft_report"]["path"])
        sradv = read_json(profile["predecessors"]["verification_report"]["path"])
        source_rollup = read_json(profile["predecessors"]["source_rollup_report"]["path"])
        for payload, predecessor_key in [
            (srad, "assisted_draft_report"),
            (sradv, "verification_report"),
            (source_rollup, "source_rollup_report"),
        ]:
            predecessor = profile["predecessors"][predecessor_key]
            if payload[predecessor["expected_id_key"]] != predecessor["expected_id"]:
                raise SystemExit(f"unexpected predecessor: {predecessor_key}")
        return {"source_kind": profile["source_kind"], "srad": srad, "sradv": sradv, "source_rollup": source_rollup}

    if profile["source_kind"] == "verified_review_acceptance":
        review_seed = read_json(profile["predecessors"]["review_seed_report"]["path"])
        verified_acceptance = read_json(profile["predecessors"]["verified_acceptance_report"]["path"])
        for payload, predecessor_key in [
            (review_seed, "review_seed_report"),
            (verified_acceptance, "verified_acceptance_report"),
        ]:
            predecessor = profile["predecessors"][predecessor_key]
            if payload[predecessor["expected_id_key"]] != predecessor["expected_id"]:
                raise SystemExit(f"unexpected predecessor: {predecessor_key}")
        expected_status = profile["expected_source_acceptance_status"]
        if verified_acceptance["source_acceptance"]["status"] != expected_status:
            raise SystemExit(f"source acceptance is not in the expected narrow state: {expected_status}")
        if verified_acceptance["page_complete_acceptance"] is not False or verified_acceptance["whole_gate_1_acceptance"] is not False:
            raise SystemExit("predecessor unexpectedly accepts the page or whole Gate 1")
        result = {
            "source_kind": profile["source_kind"],
            "review_seed": review_seed,
            "verified_acceptance": verified_acceptance,
        }
        if "context_only_confirmation_report" in profile["predecessors"]:
            context_confirmation = read_json(profile["predecessors"]["context_only_confirmation_report"]["path"])
            predecessor = profile["predecessors"]["context_only_confirmation_report"]
            if context_confirmation[predecessor["expected_id_key"]] != predecessor["expected_id"]:
                raise SystemExit("unexpected context-only confirmation predecessor")
            confirmation = context_confirmation["context_only_confirmation"]
            if confirmation["context_region_id"] != "PRM-G1-VIRAL-001-P004-R01":
                raise SystemExit("unexpected page 004 context-only region")
            if confirmation["confirmed_status"] != "context_only_not_peer_crop_record":
                raise SystemExit("page 004 context-only region is not confirmed")
            if context_confirmation["guardrails"]["page_complete_acceptance_created"] is not False:
                raise SystemExit("context-only predecessor unexpectedly accepts page 004")
            result["context_only_confirmation"] = context_confirmation
        return result

    if profile["source_kind"] == "human_review_qa_fixture_slice":
        human_review = read_json(profile["predecessors"]["human_review_report"]["path"])
        qa_report = read_json(profile["predecessors"]["qa_report"]["path"])
        fixture_report = read_json(profile["predecessors"]["fixture_admission_report"]["path"])
        admitted_fixtures = read_json(profile["predecessors"]["admitted_fixtures"]["path"])
        for payload, predecessor_key in [
            (human_review, "human_review_report"),
            (qa_report, "qa_report"),
            (fixture_report, "fixture_admission_report"),
        ]:
            predecessor = profile["predecessors"][predecessor_key]
            if payload[predecessor["expected_id_key"]] != predecessor["expected_id"]:
                raise SystemExit(f"unexpected predecessor: {predecessor_key}")
        if human_review["source_acceptance"] is not True or human_review["qa_acceptance"] is not False:
            raise SystemExit("human review predecessor is not in the expected source-review-only state")
        if qa_report["source_acceptance"] is not True or qa_report["qa_acceptance"] is not True:
            raise SystemExit("QA predecessor is not in the expected accepted QA state")
        if fixture_report["fixture_admission"] is not True or fixture_report["gate_1_advancement"] is not False:
            raise SystemExit("fixture predecessor is not in the expected narrow fixture-only state")
        return {
            "source_kind": profile["source_kind"],
            "human_review": human_review,
            "qa_report": qa_report,
            "fixture_report": fixture_report,
            "admitted_fixtures": admitted_fixtures,
        }

    raise SystemExit(f"unsupported page_map source kind: {profile['source_kind']}")


def by_region(records: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    return {record[key]: record for record in records}


def extract_structure_spans(source_rollup: dict[str, Any], question_id: str) -> list[dict[str, Any]]:
    for record in source_rollup["structure_semantics"]["records"]:
        if record["question_id"] == question_id:
            return record["spans"]
    raise SystemExit(f"missing structure record for question {question_id}")


def block_report(profile_block: dict[str, Any], srad_by_region: dict[str, Any], sradv_by_region: dict[str, Any], source_rollup: dict[str, Any]) -> dict[str, Any]:
    region_id = profile_block["source_region_id"]
    if region_id not in srad_by_region or region_id not in sradv_by_region:
        raise SystemExit(f"profile block missing predecessor text: {profile_block['block_id']}")

    draft = srad_by_region[region_id]
    verified = sradv_by_region[region_id]
    draft_text = draft["draft_text"]
    verified_text = verified["verified_text"]
    question_id = verified["question_id"]
    structure_spans = extract_structure_spans(source_rollup, question_id)

    protected = []
    missing_tokens = []
    normalized_verified_text = normalized_text(verified_text)
    for token in profile_block["protected_tokens"]:
        present = normalized_text(token) in normalized_verified_text
        protected.append({"token": token, "present": present})
        if not present:
            missing_tokens.append(token)

    semantic_roles = {span["semantic_role"] for span in structure_spans}
    missing_semantics = sorted(set(profile_block["semantic_expectations"]) - semantic_roles)
    discrepancy = []
    if draft_text != verified_text:
        discrepancy.append("draft_text_differs_from_verified_text")
    if missing_tokens:
        discrepancy.append("protected_token_missing")
    if missing_semantics:
        discrepancy.append("semantic_expectation_missing")

    return {
        "block_id": profile_block["block_id"],
        "block_type": profile_block["block_type"],
        "role": profile_block["role"],
        "source_region_id": region_id,
        "reading_order": profile_block["reading_order"],
        "required": profile_block["required"],
        "status": "ready_for_page_complete_review" if not discrepancy else "blocked",
        "anchor": {
            "page_image": draft["page_image"],
            "page_image_sha256": draft["page_image_sha256"],
            "source_region_id": region_id,
            "corrected_crop_reference": verified["corrected_crop_reference"],
            "corrected_crop_reference_sha256": verified["corrected_crop_reference_sha256"],
            "box_px": draft["box_px"],
        },
        "text_fidelity": {
            "draft_text_sha256": draft["draft_text_sha256"],
            "verified_text_sha256": verified["verified_text_sha256"],
            "draft_metrics": text_metrics(draft_text),
            "verified_metrics": text_metrics(verified_text),
            "draft_matches_verified": draft_text == verified_text,
            "raw_ocr_available": False,
            "raw_ocr_comparison": "not_available_for_this_authorization",
            "protected_tokens": protected,
            "missing_protected_tokens": missing_tokens,
            "discrepancy": discrepancy,
            "discrepancy_disposition": "none" if not discrepancy else "blocker_before_page_complete_review",
        },
        "structure_semantics": {
            "structure_record_id": next(record["structure_record_id"] for record in source_rollup["structure_semantics"]["records"] if record["question_id"] == question_id),
            "semantic_roles": sorted(semantic_roles),
            "missing_semantic_expectations": missing_semantics,
            "spans": structure_spans,
        },
        "overlay_recovery": {
            "overlay_state": "no_overlap_or_duplicate_detected_in_current_profile",
            "parent_child_relation": "none",
            "recovery_role": profile_block["role"],
            "reading_order_note": "declared by page profile",
        },
    }


def accepted_review_block_report(
    profile_block: dict[str, Any],
    review_seed_by_region: dict[str, Any],
    accepted_by_review_id: dict[str, Any],
) -> dict[str, Any]:
    region_id = profile_block["source_region_id"]
    review_id = profile_block["source_review_id"]
    if region_id not in review_seed_by_region:
        raise SystemExit(f"profile block missing review seed text: {profile_block['block_id']}")
    if review_id not in accepted_by_review_id:
        raise SystemExit(f"profile block missing accepted source text: {profile_block['block_id']}")

    draft = review_seed_by_region[region_id]
    accepted = accepted_by_review_id[review_id]
    draft_text = draft["draft_text"]
    accepted_matches_draft = accepted["accepted_text_sha256"] == draft["draft_text_sha256"]
    protected = []
    missing_tokens = []
    normalized_draft_text = normalized_text(draft_text)
    for token in profile_block["protected_tokens"]:
        present = normalized_text(token) in normalized_draft_text
        protected.append({"token": token, "present": present})
        if not present:
            missing_tokens.append(token)

    semantic_roles = {span["semantic_role"] for span in draft["draft_structure"]}
    missing_semantics = sorted(set(profile_block["semantic_expectations"]) - semantic_roles)
    discrepancy = []
    if not accepted_matches_draft:
        discrepancy.append("accepted_text_hash_differs_from_review_draft")
    if accepted["crop_reference_sha256"] != draft["crop_reference_sha256"]:
        discrepancy.append("accepted_crop_hash_differs_from_review_draft")
    if missing_tokens:
        discrepancy.append("protected_token_missing")
    if missing_semantics:
        discrepancy.append("semantic_expectation_missing")

    return {
        "block_id": profile_block["block_id"],
        "block_type": profile_block["block_type"],
        "role": profile_block["role"],
        "source_region_id": region_id,
        "source_review_id": review_id,
        "source_acceptance_record_id": accepted["source_acceptance_record_id"],
        "reading_order": profile_block["reading_order"],
        "required": profile_block["required"],
        "status": "ready_for_page_complete_review" if not discrepancy else "blocked",
        "anchor": {
            "page_image": draft["page_image"],
            "page_image_sha256": draft["page_image_sha256"],
            "source_region_id": region_id,
            "corrected_crop_reference": draft["crop_reference"],
            "corrected_crop_reference_sha256": draft["crop_reference_sha256"],
            "box_px": draft["box_px"],
        },
        "text_fidelity": {
            "draft_text_sha256": draft["draft_text_sha256"],
            "verified_text_sha256": accepted["accepted_text_sha256"],
            "draft_metrics": text_metrics(draft_text),
            "verified_metrics": text_metrics(draft_text),
            "draft_matches_verified": accepted_matches_draft,
            "raw_ocr_available": False,
            "raw_ocr_comparison": "not_available_for_this_authorization",
            "protected_tokens": protected,
            "missing_protected_tokens": missing_tokens,
            "discrepancy": discrepancy,
            "discrepancy_disposition": "none" if not discrepancy else "blocker_before_page_complete_review",
        },
        "structure_semantics": {
            "structure_record_id": accepted["source_acceptance_record_id"],
            "semantic_roles": sorted(semantic_roles),
            "missing_semantic_expectations": missing_semantics,
            "spans": draft["draft_structure"],
        },
        "overlay_recovery": {
            "overlay_state": "no_overlap_or_duplicate_detected_in_current_profile",
            "parent_child_relation": "none",
            "recovery_role": profile_block["role"],
            "reading_order_note": "declared by page profile",
        },
    }


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def semantic_spans_from_human_record(record: dict[str, Any]) -> list[dict[str, Any]]:
    text = record["candidate_text"]
    hints = record.get("semantic_heading_hint")
    if hints:
        spans = []
        for hint in hints:
            spans.append(
                {
                    "text": hint["text"],
                    "semantic_role": record["review_class"],
                    "heading_level": hint["level"].lower(),
                }
            )
        return spans
    return [
        {
            "text": text,
            "semantic_role": record["review_class"],
            "heading_level": "h1_candidate" if record["review_class"] == "heading" else "text_body",
        }
    ]


def human_review_qa_block_report(
    profile: dict[str, Any],
    profile_block: dict[str, Any],
    human_by_region_admission_id: dict[str, Any],
    qa_by_region_admission_id: dict[str, Any],
    fixture_by_region_admission_id: dict[str, Any],
) -> dict[str, Any]:
    region_admission_id = profile_block["region_admission_id"]
    if region_admission_id not in human_by_region_admission_id:
        raise SystemExit(f"profile block missing human source review: {profile_block['block_id']}")
    if region_admission_id not in qa_by_region_admission_id:
        raise SystemExit(f"profile block missing QA source review: {profile_block['block_id']}")
    if region_admission_id not in fixture_by_region_admission_id:
        raise SystemExit(f"profile block missing admitted fixture: {profile_block['block_id']}")

    human = human_by_region_admission_id[region_admission_id]
    qa = qa_by_region_admission_id[region_admission_id]
    fixture = fixture_by_region_admission_id[region_admission_id]
    verified_text = human["candidate_text"]
    protected = []
    missing_tokens = []
    normalized_verified_text = normalized_text(verified_text)
    for token in profile_block["protected_tokens"]:
        present = normalized_text(token) in normalized_verified_text
        protected.append({"token": token, "present": present})
        if not present:
            missing_tokens.append(token)

    semantic_roles = {human["review_class"]}
    missing_semantics = sorted(set(profile_block["semantic_expectations"]) - semantic_roles)
    discrepancy = []
    if human["source_text_accepted"] is not True:
        discrepancy.append("human_source_text_not_accepted")
    if qa["qa_result"] != "source_text_qa_passed" or qa["qa_acceptance"] is not True:
        discrepancy.append("source_text_qa_not_passed")
    if fixture["fixture_kind"] != "positive_source_text" or fixture["fixture_admitted"] is not True:
        discrepancy.append("positive_source_text_fixture_not_admitted")
    if human["page_id"] != profile["page_id"] or qa["page_id"] != profile["page_id"]:
        discrepancy.append("page_id_mismatch")
    if human["region_id"] != profile_block["region_id"] or qa["region_id"] != profile_block["region_id"]:
        discrepancy.append("region_id_mismatch")
    if missing_tokens:
        discrepancy.append("protected_token_missing")
    if missing_semantics:
        discrepancy.append("semantic_expectation_missing")

    return {
        "block_id": profile_block["block_id"],
        "block_type": profile_block["block_type"],
        "role": profile_block["role"],
        "source_region_id": profile_block["source_region_id"],
        "region_id": profile_block["region_id"],
        "region_admission_id": region_admission_id,
        "fixture_id": fixture["fixture_id"],
        "reading_order": profile_block["reading_order"],
        "required": profile_block["required"],
        "status": "ready_for_page_complete_review" if not discrepancy else "blocked",
        "anchor": {
            "page_image": profile["page_image"],
            "page_image_sha256": profile["page_image_sha256"],
            "source_region_id": profile_block["source_region_id"],
            "corrected_crop_reference": human["visual_reference"],
            "corrected_crop_reference_sha256": human["visual_reference_sha256"],
            "box_px": profile_block["box_px"],
        },
        "text_fidelity": {
            "draft_text_sha256": sha256_text(verified_text),
            "verified_text_sha256": sha256_text(verified_text),
            "draft_metrics": text_metrics(verified_text),
            "verified_metrics": text_metrics(verified_text),
            "draft_matches_verified": True,
            "raw_ocr_available": False,
            "raw_ocr_comparison": "not_available_for_this_authorization",
            "protected_tokens": protected,
            "missing_protected_tokens": missing_tokens,
            "discrepancy": discrepancy,
            "discrepancy_disposition": "none" if not discrepancy else "blocker_before_page_complete_review",
        },
        "structure_semantics": {
            "structure_record_id": region_admission_id,
            "semantic_roles": sorted(semantic_roles),
            "missing_semantic_expectations": missing_semantics,
            "spans": semantic_spans_from_human_record(human),
        },
        "overlay_recovery": {
            "overlay_state": "no_overlap_or_duplicate_detected_in_current_profile",
            "parent_child_relation": "none",
            "recovery_role": profile_block["role"],
            "reading_order_note": "declared by page profile",
        },
    }


def ratio(numerator: int, denominator: int) -> dict[str, Any]:
    return {
        "count": numerator,
        "expected": denominator,
        "percent": round((numerator / denominator * 100.0) if denominator else 100.0, 2),
        "advisory_only": True,
    }


def build_report(page: str) -> dict[str, Any]:
    profile = PAGE_PROFILES[page]
    inputs = verify_predecessors(profile)
    if inputs["source_kind"] == "assisted_draft_verified_rollup":
        srad_by_region = by_region(inputs["srad"]["records"], "source_region_id")
        sradv_by_region = by_region(inputs["sradv"]["records"], "source_region_id")
        blocks = [
            block_report(block, srad_by_region, sradv_by_region, inputs["source_rollup"])
            for block in profile["expected_blocks"]
        ]
    elif inputs["source_kind"] == "verified_review_acceptance":
        review_seed_records = inputs["review_seed"].get("next_review_packet", {}).get("records", inputs["review_seed"].get("records"))
        if review_seed_records is None:
            raise SystemExit("review seed is missing records")
        review_seed_by_region = by_region(review_seed_records, "source_region_id")
        accepted_by_review_id = by_region(
            inputs["verified_acceptance"]["source_acceptance"]["accepted_records"], "review_id"
        )
        blocks = [
            accepted_review_block_report(block, review_seed_by_region, accepted_by_review_id)
            for block in profile["expected_blocks"]
        ]
    elif inputs["source_kind"] == "human_review_qa_fixture_slice":
        human_by_region_admission_id = by_region(inputs["human_review"]["human_review_records"], "region_admission_id")
        qa_by_region_admission_id = by_region(inputs["qa_report"]["qa_records"], "region_admission_id")
        fixture_by_region_admission_id = by_region(inputs["admitted_fixtures"]["fixtures"], "region_admission_id")
        blocks = [
            human_review_qa_block_report(
                profile,
                block,
                human_by_region_admission_id,
                qa_by_region_admission_id,
                fixture_by_region_admission_id,
            )
            for block in profile["expected_blocks"]
        ]
    else:
        raise SystemExit(f"unsupported page_map source kind: {inputs['source_kind']}")
    blockers = []
    missing_blocks = [block for block in blocks if block["status"] == "blocked"]
    for block in missing_blocks:
        blockers.append({"block_id": block["block_id"], "reason": block["text_fidelity"]["discrepancy"]})

    reading_orders = [block["reading_order"] for block in blocks]
    if sorted(reading_orders) != list(range(1, len(blocks) + 1)):
        blockers.append({"block_id": "page", "reason": ["reading_order_not_contiguous"]})

    required_blocks = [block for block in blocks if block["required"]]
    ready_blocks = [block for block in blocks if block["status"] == "ready_for_page_complete_review"]
    anchor_ready = [block for block in blocks if block["anchor"]["corrected_crop_reference"]]

    return {
        "package_id": profile["package_id"],
        "authorization_id": profile["authorization_id"],
        "pipeline_id": PIPELINE_ID,
        "profile_id": profile["profile_id"],
        "status": "ready_for_page_complete_review_packet" if not blockers else "blocked",
        "scope": "page_map_readiness_only_no_page_acceptance",
        "generator": {
            "script": SCRIPT_PATH.relative_to(ROOT).as_posix(),
            "script_sha256": sha256_file(SCRIPT_PATH),
            "test": TEST_PATH.relative_to(ROOT).as_posix() if TEST_PATH.exists() else None,
            "test_sha256": sha256_file(TEST_PATH) if TEST_PATH.exists() else None,
        },
        "page": page,
        "page_id": profile["page_id"],
        "image_id": profile["image_id"],
        "input_packages": profile["input_packages"],
        "profile": {
            "page_label": profile["page_label"],
            "expected_block_count": len(blocks),
            "declared_none": profile["declared_none"],
            "context_only_regions": profile.get("context_only_regions", []),
            "page_specific": True,
            "reusable_pipeline": True,
        },
        "block_inventory": blocks,
        "coverage_summary": {
            "inventory_coverage": ratio(len(ready_blocks), len(required_blocks)),
            "source_ready_in_scope_text_blocks": ratio(len(ready_blocks), len(required_blocks)),
            "anchor_coverage": ratio(len(anchor_ready), len(blocks)),
            "reading_order_coverage": ratio(len(set(reading_orders)), len(blocks)),
            "declared_none_categories": profile["declared_none"],
            "coverage_accepts_page": False,
        },
        "readiness_decision": {
            "readiness": "ready_for_later_page_complete_review_packet" if not blockers else "blocked",
            "blockers": blockers,
            "open_questions": [],
            "page_complete_acceptance_created": False,
            "whole_gate_1_acceptance_created": False,
        },
        "guardrails": {
            "ocr_executed": False,
            "pdf_opened_or_parsed": False,
            "pdf_text_layer_used": False,
            "render_executed": False,
            "raw_artifacts_modified": False,
            "fixture_admission": False,
            "translation_authorized": False,
            "proofreading_authorized": False,
            "renderer_profile_acceptance": False,
            "implementation_authorized": False,
            "push_authorized": False,
        },
    }


def build_packet(report: dict[str, Any]) -> str:
    blocks = report["block_inventory"]
    page_label = report["profile"]["page_label"]
    declared_none = report["profile"]["declared_none"]
    context_only_regions = report["profile"].get("context_only_regions", [])
    lines = [
        f"# Page Map Readiness Packet - {page_label}",
        "",
        "Status: `ready_for_page_complete_review_packet`",
        "",
        f"Boundary: this is readiness only. It does not accept {page_label.lower()} as complete, does not advance Gate 1, and does not admit fixtures.",
        "",
        "## Page Inventory",
        "",
        f"- Expected blocks: {report['profile']['expected_block_count']}",
        f"- Ready blocks: {report['coverage_summary']['inventory_coverage']['count']} / {report['coverage_summary']['inventory_coverage']['expected']}",
        f"- Declared none: {'/'.join(declared_none) if declared_none else 'none'}.",
        f"- Context-only regions: {len(context_only_regions)}.",
        "",
        "## Reading Order",
        "",
    ]
    for block in sorted(blocks, key=lambda item: item["reading_order"]):
        lines.append(f"{block['reading_order']}. {block['role']} ({block['source_region_id']})")
    lines.extend(["", "## Blocks", ""])
    for block in sorted(blocks, key=lambda item: item["reading_order"]):
        fidelity = block["text_fidelity"]
        lines.extend(
            [
                f"### {block['block_id']} - {block['role']}",
                "",
                f"- Region: `{block['source_region_id']}`",
                f"- Status: `{block['status']}`",
                f"- Characters: {fidelity['verified_metrics']['character_count']} raw / {fidelity['verified_metrics']['normalized_character_count']} normalized",
                f"- Lines: {fidelity['verified_metrics']['line_count']} total / {fidelity['verified_metrics']['non_empty_line_count']} non-empty",
                f"- Protected tokens: {len(fidelity['protected_tokens']) - len(fidelity['missing_protected_tokens'])} / {len(fidelity['protected_tokens'])}",
                f"- Discrepancy: `{fidelity['discrepancy_disposition']}`",
                f"- Anchor crop: `{block['anchor']['corrected_crop_reference']}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Coverage",
            "",
            f"- Inventory coverage: {report['coverage_summary']['inventory_coverage']['count']} / {report['coverage_summary']['inventory_coverage']['expected']} ({report['coverage_summary']['inventory_coverage']['percent']}%).",
            f"- Source-ready in-scope text blocks: {report['coverage_summary']['source_ready_in_scope_text_blocks']['count']} / {report['coverage_summary']['source_ready_in_scope_text_blocks']['expected']} ({report['coverage_summary']['source_ready_in_scope_text_blocks']['percent']}%).",
            f"- Anchor coverage: {report['coverage_summary']['anchor_coverage']['count']} / {report['coverage_summary']['anchor_coverage']['expected']} ({report['coverage_summary']['anchor_coverage']['percent']}%).",
            f"- Reading-order coverage: {report['coverage_summary']['reading_order_coverage']['count']} / {report['coverage_summary']['reading_order_coverage']['expected']} ({report['coverage_summary']['reading_order_coverage']['percent']}%).",
            "",
            "Coverage is advisory only. Even 100% coverage does not accept the page.",
            "",
            "## Next Decision",
            "",
            f"{page_label} is ready for a separate page-complete review packet if Bogdan wants to proceed. That next packet needs its own bounded authorization.",
            "",
        ]
    )
    return "\n".join(lines)


def build_summary(report: dict[str, Any]) -> str:
    page_label = report["profile"]["page_label"]
    ready = report["coverage_summary"]["inventory_coverage"]
    reading_order = " -> ".join(block["role"] for block in sorted(report["block_inventory"], key=lambda item: item["reading_order"]))
    declared_none = "/".join(report["profile"]["declared_none"])
    context_only_count = len(report["profile"].get("context_only_regions", []))
    return "\n".join(
        [
            f"# Page Map Readiness Summary - {page_label}",
            "",
            f"Package: `{report['package_id']}`",
            "",
            f"- {page_label} was processed through the reusable page_map readiness pipeline using a page-specific profile.",
            f"- Expected inventory: {ready['expected']} required blocks.",
            f"- Ready inventory: {ready['count']} / {ready['expected']}.",
            f"- Reading order: {reading_order}.",
            f"- {declared_none} blocks: none identified by the current profile.",
            f"- Context-only regions: {context_only_count}.",
            "- Text fidelity checks used existing draft/verified/source-accepted artifacts only.",
            "- No OCR, render, PDF parsing/text-layer extraction, raw mutation, fixture admission, page-complete acceptance, or Gate acceptance was created.",
            "- Result: ready for a later separately authorized page-complete review packet.",
            "",
        ]
    )


def build_manifest(package_id: str, out_root: Path) -> str:
    lines = [
        "# Page Map Readiness Manifest",
        "",
        f"Package: `{package_id}`",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(out_root.rglob("*")):
        if path.is_file() and path.name != "page_map_readiness_manifest.md":
            lines.append(f"| `{path.relative_to(out_root).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    return "\n".join(lines)


def build(page: str) -> None:
    if page not in PAGE_PROFILES:
        raise SystemExit(f"no page_map profile exists for page {page}")
    out_root = PAGE_PROFILES[page]["output_dir"]
    report = build_report(page)
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True, exist_ok=True)
    write_json(out_root / "page_map_readiness_report.json", report)
    (out_root / "page_map_readiness_packet.md").write_text(build_packet(report), encoding="utf-8", newline="\n")
    (out_root / "page_map_readiness_summary.md").write_text(build_summary(report), encoding="utf-8", newline="\n")
    (out_root / "page_map_readiness_manifest.md").write_text(
        build_manifest(report["package_id"], out_root), encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    parsed = check_authorization()
    build(parsed.page)
