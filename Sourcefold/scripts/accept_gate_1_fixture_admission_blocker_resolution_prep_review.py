from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
PREP_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_G1_VIRAL_001"
OUT_ROOT = TRIAL_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_G1_VIRAL_001"

AUTHORIZATION_ID = "BA-G1-VIRAL-FIXTURE-ADMISSION-BLOCKER-RESOLUTION-PREP-REVIEW-001"
PREP_PACKET_ID = "G1FABRP-G1-VIRAL-001"
REVIEW_ID = "G1FABRPREV-G1-VIRAL-001"
HUMAN_DECISION = "ok"
HUMAN_DECISION_CONTEXT = (
    "G1FABRP-G1-VIRAL-001 accepted as blocker-resolution prep only after "
    "Sol/Terra consolidated review cleanup; no blocker resolution, no fixture "
    "admission, no whole Gate 1 acceptance, no page 021+, no push"
)
HUMAN_DECISION_MESSAGE_ID = "2275"

INPUT_HASHES = {
    "G1FABRP-G1-VIRAL-001.packet": (
        PREP_ROOT / "gate_1_fixture_admission_blocker_resolution_prep.json",
        "5CF0182E401E12E6382B3E5D39E6A3391641AD5FCC29F7E916C2D1F91D2EB9AB",
    ),
    "G1FABRP-G1-VIRAL-001.report": (
        PREP_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_report.json",
        "EAEF68EE7C826DE8C8C33693C3C99166E3CDFA93987AACAAEFAB4E7E78C75004",
    ),
    "G1FABRP-G1-VIRAL-001.summary": (
        PREP_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_summary.md",
        "5092123F70DC7B3DF9D65A78C6E777F0AC35D379DCE85895F7DC5838B100DB0E",
    ),
    "G1FABRP-G1-VIRAL-001.manifest": (
        PREP_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_manifest.md",
        "A806B34A1E20BA89F6723CBC309654DDAF366EB50CF1A653DC16061BC0257A60",
    ),
}

NEGATIVE_CAPABILITIES = [
    "blocker_resolution",
    "fixture_admission",
    "fixture_manifest_creation",
    "whole_gate_1_acceptance",
    "source_profile_acceptance",
    "page_021_plus_processing",
    "ocr_execution",
    "ocr_remediation_execution",
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
    parser = argparse.ArgumentParser(description="Accept G1FABRP as blocker-resolution prep only.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    parser.add_argument("--decision")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("G1FABRP review is fail-closed; pass --execute")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"G1FABRP review requires {AUTHORIZATION_ID}")
    if args.decision != HUMAN_DECISION:
        raise SystemExit(f"G1FABRP review requires decision: {HUMAN_DECISION}")


def verify_inputs() -> tuple[dict[str, dict[str, str]], dict]:
    verified: dict[str, dict[str, str]] = {}
    for key, (path, expected) in INPUT_HASHES.items():
        actual = sha256_file(path)
        if actual != expected:
            raise SystemExit(f"{key} hash mismatch: {actual}")
        verified[key] = {"path": path.relative_to(ROOT).as_posix(), "sha256": actual}

    prep = read_json(INPUT_HASHES["G1FABRP-G1-VIRAL-001.packet"][0])
    if prep["packet_id"] != PREP_PACKET_ID:
        raise SystemExit("G1FABRP packet id mismatch")
    if prep["creates_blocker_resolution"]:
        raise SystemExit("G1FABRP unexpectedly resolves blockers")
    if prep["admits_fixture"] or prep["creates_fixture_manifest"]:
        raise SystemExit("G1FABRP unexpectedly admits fixtures")
    if prep["accepts_whole_gate_1"] or prep["accepts_source_profile"]:
        raise SystemExit("G1FABRP unexpectedly creates acceptance")
    if prep["processes_page_021_plus"] or prep["executes_ocr"]:
        raise SystemExit("G1FABRP unexpectedly processes page 021+ or OCR")
    return verified, prep


def build_review(verified_inputs: dict[str, dict[str, str]], prep: dict) -> dict:
    return {
        "review_id": REVIEW_ID,
        "authorization_id": AUTHORIZATION_ID,
        "reviewed_packet_id": PREP_PACKET_ID,
        "status": "fixture_admission_blocker_resolution_prep_accepted_for_next_decision_prep",
        "human_decision": HUMAN_DECISION,
        "human_decision_context": HUMAN_DECISION_CONTEXT,
        "human_decision_source": {"platform": "telegram", "message_id": HUMAN_DECISION_MESSAGE_ID},
        "accepts_blocker_resolution_prep_packet": True,
        "creates_blocker_resolution": False,
        "admits_fixture": False,
        "creates_fixture_manifest": False,
        "accepts_whole_gate_1": False,
        "accepts_source_profile": False,
        "processes_page_021_plus": False,
        "executes_ocr": False,
        "reviewed_blockers": [row["blocker_id"] for row in prep["blockers"]],
        "accepted_recommended_sequence": prep["recommended_sequence"],
        "next_candidate": "unsupported_negative_fixture_policy_decision_prep",
        "negative_capability_matrix": {name: False for name in NEGATIVE_CAPABILITIES},
        "verified_inputs": verified_inputs,
    }


def write_summary(review: dict) -> None:
    lines = [
        "# Gate 1 Fixture Admission Blocker Resolution Prep Review - G1FABRPREV-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_blocker_resolution_prep_accepted_for_next_decision_prep`",
        "",
        f"Human decision: `{review['human_decision']}`",
        "",
        f"Context: {review['human_decision_context']}",
        "",
        "## Reviewed Blockers",
        "",
    ]
    for blocker in review["reviewed_blockers"]:
        lines.append(f"- `{blocker}`")
    lines.extend(
        [
            "",
            "## Next Candidate",
            "",
            f"- `{review['next_candidate']}`",
            "",
            "## Boundaries",
            "",
            "- No blocker resolution.",
            "- No fixture admission.",
            "- No fixture manifest creation.",
            "- No whole Gate 1 acceptance.",
            "- No source-profile acceptance.",
            "- No page 021+ processing.",
            "- No OCR execution or remediation rerun.",
            "- No push.",
            "",
        ]
    )
    write_text(OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review_summary.md", "\n".join(lines))


def write_manifest() -> None:
    manifest_name = "gate_1_fixture_admission_blocker_resolution_prep_review_manifest.md"
    lines = [
        "# Gate 1 Fixture Admission Blocker Resolution Prep Review Manifest - G1FABRPREV-G1-VIRAL-001",
        "",
        "Status: `fixture_admission_blocker_resolution_prep_accepted_for_next_decision_prep`",
        "",
        "Boundary: blocker-resolution prep review only; no blocker resolution, no fixture admission, no page 021+, no push, and no whole Gate 1 acceptance.",
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
    verified_inputs, prep = verify_inputs()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    review = build_review(verified_inputs, prep)
    write_json(OUT_ROOT / "gate_1_fixture_admission_blocker_resolution_prep_review.json", review)
    write_summary(review)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
