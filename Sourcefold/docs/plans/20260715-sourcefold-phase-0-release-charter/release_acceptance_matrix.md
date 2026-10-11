# Release Acceptance Matrix

Status: draft for Phase 0 decision

| Criterion | Owner | Fixture/Test | Human Check | Evidence Artifact | Failure Behavior | Status |
|---|---|---|---|---|---|---|
| 0.1 source profile is declared. | user/orchestrator | unsupported-profile negative fixture | user approves profile | release charter and decision log | implementation remains blocked | pending |
| Canonical formats are declared. | user/orchestrator | manifest/schema validation in Phase 1 | user accepts format boundary | release charter, artifact model | implementation remains blocked | pending |
| Acceptance vocabulary is distinct. | orchestrator/user | invalid acceptance-state fixture in Phase 1 | user accepts authority model | acceptance vocabulary | implementation remains blocked | draft |
| Artifact identity fields are declared. | Sol/Terra/user | hash mismatch fixture in Phase 1 | reviewer checks identity fields | artifact lineage model | implementation remains blocked | draft |
| Valid DAG edges are declared. | Sol/Terra/user | bad-edge negative fixture | reviewer checks predecessor rules | artifact lineage model | implementation remains blocked | draft |
| Waiver policy is declared. | user/orchestrator | invalid-waiver negative fixture | user accepts waiver authority | acceptance vocabulary and future waiver schema | implementation remains blocked | pending |
| Positive fixture is selected. | user/orchestrator | positive fixture | user accepts fixture source | fixture strategy | implementation remains blocked | pending |
| Negative fixtures are selected. | orchestrator | negative fixture set | reviewer checks coverage | fixture strategy | implementation remains blocked | draft |
| No module implementation starts before Phase 0 acceptance. | orchestrator | plan/status check | user authorizes Phase 1 | plan/context/status | stop and ask | active |
| Roadmap/status are updated. | orchestrator | roadmap validator | orchestrator review | `roadmap.yaml`, `PROJECT_STATUS.md` | checkpoint blocked | pending |
| Independent critique is recorded. | Terra | handoff receipt | orchestrator confirms receipt | Terra handoff | Phase 0 review incomplete | completed |
| Architecture review is recorded. | Sol | handoff receipt | orchestrator confirms receipt | Sol handoff | Phase 0 review incomplete | completed |
| OCR-first 10-step roadmap is recorded. | Sol/orchestrator | roadmap document | user/orchestrator review | `ocr_first_10_step_roadmap.md`, Sol OCR handoff | Phase 0 profile incomplete | draft |
| Core 0.1 executable matrix skeleton exists. | orchestrator | matrix document | user/orchestrator review | `core_0_1_acceptance_matrix.md` | Phase 1 planning blocked | draft |

## Release Gate For 0.1 RC

This Phase 0 matrix is not the final 0.1 release matrix. It is the Phase 0
decision matrix that must be closed before Phase 1 executable contracts begin.
