from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = ROOT / "fixtures" / "candidate_inputs" / "viral" / "render_trials" / "RT-G1-VIRAL-RENDER-001"
OUT_ROOT = TRIAL_ROOT / "gate_1_status_packet_G1_VIRAL_002"

AUTHORIZATION_ID = "BA-G1-VIRAL-GATE-1-STATUS-REFRESH-002"
STATUS_PACKET_ID = "G1SP-G1-VIRAL-002"

PAGE_ACCEPTANCE_HASHES = {
    "002": {
        "package_id": "P002PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p002_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "B136282C441D1E48DE9CE064356B3B06F6D45A500C1984901D53908335D8547C",
            "page_complete_acceptance_record.md": "3FF1AC29BA8CBCDED3AA8757CDD87713B0EC26011B32A528127C54C572E1EDDE",
            "page_complete_acceptance_summary.md": "C3BE5845C038BFB090C66AE678E83B0E0B87769CA9EFB4DED421F9AE53BF0CB4",
            "page_complete_acceptance_manifest.md": "D02CFFCADB96DE10382C52822DF87932DE3912C332537F5560CC6B7F438DE70A",
        },
    },
    "003": {
        "package_id": "P003PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p003_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "9D74A9B73D657A0669AD0025B40936E1873A9643F1F03F31279B87FCFAFA5F79",
            "page_complete_acceptance_record.md": "039E80726ECCAB2F0F1ACFD2794053630C560F21404739A8E02CE71551769842",
            "page_complete_acceptance_summary.md": "8EAE084049DC652D733754B9DEEE770D612AACCE7BE7ADAD30DF705CE1E414B8",
            "page_complete_acceptance_manifest.md": "7D9878C91167228E73BC67DEA28E692DA661327201A89209CB0C659F8D450835",
        },
    },
    "004": {
        "package_id": "P004PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p004_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "57D4E5B3665129732308E042B4CECEEDD170907B2DCB852468DBBF885C222035",
            "page_complete_acceptance_record.md": "A248722D3F7BC42A09F25FD2AF7450CCCAE41552B384A63ADDA8E247988328E5",
            "page_complete_acceptance_summary.md": "F401362F55BE6EE770FCB3EA7659BCA4A7E30F24CEBCC09F93FBB241220254AD",
            "page_complete_acceptance_manifest.md": "905F37C5669A4242FE45CCD51E97EAEA40308DC20E60D3E294DD7D599356E3B0",
        },
    },
    "005": {
        "package_id": "P005PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p005_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "2065A5C139E42514AD92EFB897151CE87CEEEF42208B9A7F99482B7A7F923022",
            "page_complete_acceptance_record.md": "2A5E5CC65ABCACA348E0D13002C23770A185E09E066C5CCB63E10CCB093BDE16",
            "page_complete_acceptance_summary.md": "5650BE44D46B09FFA709B03935A4BE7717C2E0935327083B2DAF1EFD3F7FB598",
            "page_complete_acceptance_manifest.md": "7E123CC8BCFB648C4F11224D54F27011EBC08D0E6841ED4DF093F5000335457F",
        },
    },
    "006": {
        "package_id": "P006PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p006_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "9D0643332F24AF2B5FF3D14518B9FF83B70B331FA1E165577A6C5245532692B5",
            "page_complete_acceptance_record.md": "F60BDBB4A2F4735DD931ED3A0CCE338F7A1A87D16EF9176F9331A7BAC17244A6",
            "page_complete_acceptance_summary.md": "0498432BECE7B8B4DC21969DC2C6EDD6EB60AECE12AFF88822C5267BE43689E9",
            "page_complete_acceptance_manifest.md": "B117B4A48B06EEECB8FABA73DDFA3233B53FFF17599CF3955BB1C7C8E32B97F1",
        },
    },
    "007": {
        "package_id": "P007PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p007_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "8A1B163709D47D9268602C8F2EEF5F5E880E450807468DC9EB360BE8C7CC80F5",
            "page_complete_acceptance_record.md": "541569B53203FC35B40CD68FBB3158131284FD1DC7AB307D1BAE63E5A539FDB2",
            "page_complete_acceptance_summary.md": "E5C0F075D427167AA12A1B509A0E211B7E223E0E1170E1DB0E414C783B87FA45",
            "page_complete_acceptance_manifest.md": "FA38D3289B923B9EC24C3999D8575E1F3888A513FC25C42A63649BB963808188",
        },
    },
    "008": {
        "package_id": "P008PCA-G1-VIRAL-001",
        "root": "page_complete_acceptance_p008_G1_VIRAL_001",
        "files": {
            "page_complete_acceptance_report.json": "44F126668C6A6F148579787917D93199D0413F51DE0E8C3C6143AAA4047B0F64",
            "page_complete_acceptance_record.md": "737DF0A54C9F6FE46BADE0BE7A3ACB5DCA4F2705C4093846593C4AEFD71F6600",
            "page_complete_acceptance_summary.md": "24C025D6C7E46251DA72B8B9123D3AE3FE1FDD5026DB73FAECA0578105F15C7A",
            "page_complete_acceptance_manifest.md": "85D817E5930A2033507A79B6BCBB1017A04E740B9F2B98CD07AB29EA01855B34",
        },
    },
}

STATUS_PREDECESSORS = {
    "G1SP-G1-VIRAL-001": {
        "root": "gate_1_status_packet_G1_VIRAL_001",
        "authority": "historical_narrow_status_not_current_full_status",
        "files": {
            "gate_1_status_packet.json": "4C7EFAFDC60DF52A09F9358AB7F334FC5354B51E95A130F5BC86D42DC0C4BE68",
            "gate_1_status_packet_report.json": "4F0AD3C7553863636B6FD15E329815EE26E62329D668C9FA8AC756CE04B24644",
            "gate_1_status_packet_manifest.md": "DA8DDB2DA56EECE600A36303383F7ACB83B5E3677888F7D980FD9183B6B3E639",
            "gate_1_status_packet_summary.md": "FEFD8CAF624F392E1F8F0E6A4A96B5D120FA76A5CC4B7BA7D675F3833077B562",
        },
    },
    "G1SRER-G1-VIRAL-001": {
        "root": "gate_1_source_recon_evidence_rollup_G1_VIRAL_001",
        "authority": "historical_7_record_durable_source_reconstruction_rollup",
        "files": {
            "gate_1_source_recon_evidence_rollup.json": "3674E136BAA0F1D62DC240FAD1C1E34FD919D56A4A7251D580106D9BEFB83380",
            "gate_1_source_recon_evidence_rollup_report.json": "CDF75D022DC29D0594CA441F02EDA2DC50CE9C0C4BA81F5C51523745318A4AEB",
            "gate_1_source_recon_evidence_rollup_manifest.md": "C5211A4F6607B6DEAE73EFA599C8F25F269833AAAACED9838FF2746AA4A1A265",
            "gate_1_source_recon_evidence_rollup_summary.md": "5740BE4D8B7AAA7D8D05DFDFD3EBA4A67EF26538B9C95E653A3D8B09C498BC8B",
        },
    },
}

SOURCE_ACCEPTANCE_SURFACES = {
    "P002C-G1-VIRAL-002": {
        "accepted_records_added": 2,
        "total_after": 9,
        "report_path": "source_reconstruction_p002_completion_and_next_review_G1_VIRAL_001/p002_completion_and_next_review_report.json",
        "report_sha256": "A2A1AD3B7AAC2CF99C9CD41608FDC00F3775302C1641D3100FE003A692D8116F",
    },
    "P003A-G1-VIRAL-003": {
        "accepted_records_added": 2,
        "total_after": 11,
        "report_path": "source_reconstruction_p003_verified_review_acceptance_G1_VIRAL_001/p003_verified_review_acceptance_report.json",
        "report_sha256": "9A9D0D5E8C08596E35FF500F3BDCCC40D0544D43145A114424CD4C89BDCE237B",
    },
    "P004A-G1-VIRAL-004": {
        "accepted_records_added": 2,
        "total_after": 13,
        "report_path": "source_reconstruction_p004_verified_review_acceptance_G1_VIRAL_001/p004_verified_review_acceptance_report.json",
        "report_sha256": "0CCB4AA33481BDB0B95B02D32A0E49FB1A20FD9A957DB7DAE1ECB0B00307622E",
    },
}

FORBIDDEN_CAPABILITIES = [
    "fixture_admission",
    "source_mutation",
    "new_source_acceptance",
    "ocr_execution",
    "render_execution",
    "pdf_parsing_or_text_layer_extraction",
    "raw_mutation",
    "translation",
    "proofreading",
    "renderer_profile_acceptance",
    "implementation",
    "push",
    "page_009_plus_processing",
    "whole_gate_1_acceptance",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def check_authorization(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Build the post-P008 Gate 1 status refresh packet.")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--authorization-id")
    args = parser.parse_args(argv)
    if not args.execute:
        raise SystemExit("Gate 1 status refresh build is fail-closed; pass --execute with exact authorization id")
    if args.authorization_id != AUTHORIZATION_ID:
        raise SystemExit(f"Gate 1 status refresh build requires {AUTHORIZATION_ID}")


def verify_hashes() -> None:
    for page, data in PAGE_ACCEPTANCE_HASHES.items():
        for filename, expected in data["files"].items():
            path = TRIAL_ROOT / data["root"] / filename
            actual = sha256_file(path)
            if actual != expected:
                raise SystemExit(f"page {page} acceptance predecessor hash mismatch: {filename}")
    for predecessor_id, data in STATUS_PREDECESSORS.items():
        for filename, expected in data["files"].items():
            path = TRIAL_ROOT / data["root"] / filename
            actual = sha256_file(path)
            if actual != expected:
                raise SystemExit(f"{predecessor_id} predecessor hash mismatch: {filename}")
    for surface_id, data in SOURCE_ACCEPTANCE_SURFACES.items():
        actual = sha256_file(TRIAL_ROOT / data["report_path"])
        if actual != data["report_sha256"]:
            raise SystemExit(f"{surface_id} source-acceptance surface hash mismatch")


def predecessor_bindings() -> dict[str, object]:
    page_acceptances = {}
    for page, data in PAGE_ACCEPTANCE_HASHES.items():
        page_acceptances[page] = {
            "package_id": data["package_id"],
            "state": "page_complete_accepted",
            "scope": f"page_{page}_only",
            "root": data["root"],
            "files": data["files"],
        }
    return {
        "page_complete_acceptances": page_acceptances,
        "status_predecessors": STATUS_PREDECESSORS,
        "source_acceptance_surfaces": SOURCE_ACCEPTANCE_SURFACES,
        "held_or_superseded_review_packets_not_consumed_as_current_status": [
            "PCRP-G1-VIRAL-P005-001",
            "PCRP-G1-VIRAL-P005-002",
            "PCRP-G1-VIRAL-P005-003",
            "PCRP-G1-VIRAL-P006-001",
            "PCRP-G1-VIRAL-P007-001",
            "PCRP-G1-VIRAL-P007-002",
        ],
    }


def build_packet() -> dict[str, object]:
    negative_capability_matrix = {name: False for name in FORBIDDEN_CAPABILITIES}
    routing_options = [
        {
            "option": "page_001_completion",
            "status": "recommended_next_candidate_not_authorized",
            "why": "closes the first-class page_001_incomplete blocker before page 009 plus continuation",
        },
        {
            "option": "pages_009_020_continuation",
            "status": "valid_later_small_slices_not_authorized",
            "why": "larger continuation scope; should stay bounded per page or small slice",
        },
        {
            "option": "ocr_benchmark_remediation",
            "status": "separate_branch_not_authorized",
            "why": "current benchmark evidence is unresolved and ran on five admitted crop images",
        },
        {
            "option": "source_profile_or_gate_1_parameter_parking_or_acceptance_review",
            "status": "separate_branch_not_authorized",
            "why": "requires explicit parameter scope and accepted/parked blockers",
        },
        {
            "option": "whole_gate_1_acceptance",
            "status": "not_ready",
            "why": (
                "not ready while page_001_incomplete, pages_009_020_unstarted, "
                "source_profile_parameters_unaccepted_or_unparked, and "
                "ocr_benchmark_remediation_unresolved remain first-class blockers"
            ),
        },
        {
            "option": "translation_proofreading_implementation",
            "status": "not_ready",
            "why": "downstream of accepted source/profile/gate decisions",
        },
    ]
    return {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": "gate_1_status_route_packet_ready_no_acceptance",
        "purpose": "post_P008_status_refresh_to_route_next_bounded_decision",
        "creates_acceptance": False,
        "baseline": {
            "page_complete_accepted_pages": ["002", "003", "004", "005", "006", "007", "008"],
            "page_complete_acceptance_scope": "individual_pages_only",
            "source_reconstruction_current_canonical_narrow_state": "13_accepted_records",
            "new_source_acceptance_rollup_created": False,
            "g1sp_001_state": "historical_narrow_stale_for_current_page_complete_status",
            "g1srer_001_state": "historical_7_record_durable_source_reconstruction_rollup",
        },
        "blocker_flags": {
            "page_001_incomplete": True,
            "pages_009_020_unstarted": True,
            "whole_gate_1_acceptance": False,
            "source_profile_parameters_unaccepted_or_unparked": True,
            "ocr_benchmark_remediation_unresolved": True,
            "gate_1_status_only_no_acceptance": True,
        },
        "negative_capability_matrix": negative_capability_matrix,
        "state_taxonomy": [
            "accepted",
            "page_complete_accepted",
            "review_packet",
            "readiness",
            "rolled_up",
            "parked",
            "blocked",
            "stale",
            "superseded",
        ],
        "predecessor_bindings": predecessor_bindings(),
        "routing_matrix": routing_options,
        "recommended_next_candidate": "page_001_completion",
    }


def write_summary(packet: dict[str, object]) -> None:
    lines = [
        "# Gate 1 Status Route Packet - G1SP-G1-VIRAL-002",
        "",
        "Status: `gate_1_status_route_packet_ready_no_acceptance`",
        "",
        "Purpose: post-P008 status refresh. This packet routes the next bounded decision; it does not authorize that next layer.",
        "",
        "## Baseline",
        "",
        "- Page-complete accepted only: `002`, `003`, `004`, `005`, `006`, `007`, `008`.",
        "- Source reconstruction current canonical narrow state: `13 accepted records`.",
        "- `G1SP-G1-VIRAL-001`: historical/narrow/stale for current page-complete status.",
        "- `G1SRER-G1-VIRAL-001`: historical 7-record durable source reconstruction rollup.",
        "- New source-acceptance rollup created here: `false`.",
        "",
        "## First-Class Blockers",
        "",
        "- `page_001_incomplete=true`",
        "- `pages_009_020_unstarted=true`",
        "- `whole_gate_1_acceptance=false`",
        "- `source_profile_parameters_unaccepted_or_unparked=true`",
        "- `ocr_benchmark_remediation_unresolved=true`",
        "- `gate_1_status_only_no_acceptance=true`",
        "",
        "## Forbidden Capabilities",
        "",
    ]
    for name, value in packet["negative_capability_matrix"].items():
        lines.append(f"- `{name}={str(value).lower()}`")
    lines.extend(
        [
            "",
            "## Routing Matrix",
            "",
            "| Option | Status |",
            "|---|---|",
        ]
    )
    for option in packet["routing_matrix"]:
        lines.append(f"| `{option['option']}` | `{option['status']}` |")
    lines.extend(
        [
            "",
            "Recommended next candidate: `page_001_completion`.",
            "",
            "Decision after review: `status packet ok` or `hold status packet: <reason>`.",
            "",
        ]
    )
    (OUT_ROOT / "gate_1_status_summary.md").write_text("\n".join(lines), encoding="utf-8")


def write_report(packet: dict[str, object]) -> dict[str, object]:
    report = {
        "status_packet_id": STATUS_PACKET_ID,
        "authorization_id": AUTHORIZATION_ID,
        "status": packet["status"],
        "generator_script": "scripts/build_gate_1_status_refresh.py",
        "generator_script_sha256": sha256_file(Path(__file__).resolve()),
        "test_contract": "tests/test_gate_1_status_packet.py",
        "test_contract_sha256": sha256_file(ROOT / "tests" / "test_gate_1_status_packet.py"),
        "creates_acceptance": False,
        "new_source_acceptance_rollup_created": False,
        "whole_gate_1_acceptance": False,
        "negative_capability_matrix": packet["negative_capability_matrix"],
        "blocker_flags": packet["blocker_flags"],
        "recommended_next_candidate": packet["recommended_next_candidate"],
    }
    write_json(OUT_ROOT / "gate_1_status_report.json", report)
    return report


def write_manifest() -> None:
    lines = [
        "# Gate 1 Status Route Manifest - G1SP-G1-VIRAL-002",
        "",
        "Status: `gate_1_status_route_packet_ready_no_acceptance`",
        "",
        "Boundary: this status route packet creates no acceptance, no source mutation, no OCR/render/PDF/raw mutation, and no next-layer authorization.",
        "",
        "## Output Hashes",
        "",
        "| Output | SHA-256 |",
        "|---|---|",
    ]
    for path in sorted(OUT_ROOT.rglob("*")):
        if path.is_file() and path.name != "gate_1_status_manifest.md":
            lines.append(f"| `{path.relative_to(OUT_ROOT).as_posix()}` | `{sha256_file(path)}` |")
    lines.append("")
    (OUT_ROOT / "gate_1_status_manifest.md").write_text("\n".join(lines), encoding="utf-8")


def build() -> None:
    verify_hashes()
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    packet = build_packet()
    write_json(OUT_ROOT / "gate_1_status_packet.json", packet)
    write_summary(packet)
    write_report(packet)
    write_manifest()


if __name__ == "__main__":
    check_authorization()
    build()
