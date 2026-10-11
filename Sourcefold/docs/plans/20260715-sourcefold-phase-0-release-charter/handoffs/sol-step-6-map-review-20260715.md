# Sol Step 6 Pre-OCR Map Review
Verdict: NOT OK
Blocking findings:
- `pre_ocr_mapping_model.md:158-161` still says that after protocol acceptance, metadata-only intake creates or confirms both the selected-page manifest and a seed `doc_map`. This conflicts with the Step 6 contract, which requires manifest creation and map collection to be distinct bounded actions, and requires current render evidence when collection is render-bound. Remediation: rewrite the future sequence as separate gates: exact `accepted_protocol`; independently authorized selected-page manifest; independently authorized render evidence when render-bound; accepted or version-bound provisional schema/identity interfaces; then a distinct bounded map-qualification authorization. Acceptance criterion: no intake or protocol-acceptance sentence may itself authorize or combine manifest creation, map seeding, page/image observation, or annotation.
- The future map qualification record is not self-evidently sufficient for lineage and invalidation. `gate_01_qualification_protocol.md:685-704` omits explicit source/intake identity, predecessor IDs, tool/actor/time provenance, supersession, and per-map revision/hash/schema bindings; those fields exist only in the earlier generic Evidence Package Skeleton, which says records “should” carry them. Remediation: state that the map record extends the mandatory generic skeleton and explicitly bind source/intake, predecessors, tool/reviewer provenance, timestamps, supersession, and exact map revision/hash/schema data, while continuing to prohibit OCR, PDF text-layer, accepted source, and translation text. Acceptance criterion: the record alone plus its declared inherited contract closes the evidence DAG and deterministically stales the bundle when source, manifest, render evidence, schema, identity model, tool, or authorization changes.
- Live Step 7 labels are inconsistent with the required blocked state: the protocol step table and today-plan table say `pending`, while roadmap evidence checklists say `missing`; `PROJECT_STATUS.md` does not explicitly label Step 7 blocked. Remediation: synchronize current/live fields—not historical checkpoints—to `Step 6 draft-review-needed` and `Step 7 blocked pending accepted Step 6 review/user-delegated approval`, with Viral quarantine unchanged. Acceptance criterion: every current status surface in the reviewed set expresses those two states unambiguously; historical records remain immutable.
Non-blocking notes:
- The Step 6 section itself correctly limits this phase to governance/spec drafting and expressly forbids opening, rendering, inspecting, mapping, annotating, OCRing, or deriving observations from Viral.
- The `doc_map`, `content_map`, and `art_map` projection design correctly uses one shared page/region identity layer and rejects drifting independent inventories.
- The visualization boundary is sound: roadmap YAML carries control metadata only; a future viewer reads canonical artifacts, and viewer screenshots are not canonical evidence by default.
- Assumption: proceeding to Step 7 means OCR benchmark protocol drafting only and grants no candidate-derived action. This is a scoped architecture review, not a final release decision.
Exact answer:
- Do not commit the current Step 6 draft set and do not proceed to Step 7 yet. Remediate the three findings above, keep Viral quarantined, and request a narrow Sol/Terra confirmation. After those acceptance criteria pass, Step 6 may be committed and Step 7 may begin as draft-only.
Files reviewed:
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/pre_ocr_mapping_model.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/context.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/plan.md`
- `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/today_20260715_step_plan.md`
- `Sourcefold/docs/roadmap/roadmap.yaml`
- `Sourcefold/PROJECT_STATUS.md`
- Changed only this handoff receipt: `Sourcefold/docs/plans/20260715-sourcefold-phase-0-release-charter/handoffs/sol-step-6-map-review-20260715.md`.
Verification:
- Scope was limited to the listed Sourcefold text files and this handoff. No CoC, Dune, or translator content was read.
- Textual contract/dependency/status review only; no implementation, schema validation, or release approval was performed.
- No PDF was opened, parsed, rendered, OCRed, hashed, page-counted, inspected, mapped, screenshotted, annotated, or otherwise touched.
- No schema or map artifact was created; no canonical plan, context, project status, roadmap, release file, or other source file was edited.
- Blockers: three specification/status issues above. Next action: orchestrator applies bounded textual remediation and requests renewed Sol/Terra review.
- Elapsed time: approximately 12 minutes. Token use: unavailable. Timestamp: 2026-07-15T21:27:16+03:00.
