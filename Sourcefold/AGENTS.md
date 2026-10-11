# Sourcefold Guidance

Sourcefold is the NRI product for reconstructing trustworthy source text,
translating it into faithful Russian, and proofreading the Russian master.
It is not a rename, copy, or compatibility layer for `translator`.

## Scope

Core modules:

- `reconstruct`: accept reliable structured source text from immutable source
  evidence.
- `translate`: create a faithful Russian draft that preserves meaning,
  structure, and data.
- `proofread`: produce and accept the Russian master.

Optional lanes:

- `press`: render Markdown, HTML, or PDF projections from an accepted RU master.
- `bridge`: export accepted artifacts to explicit external integrations.

Knowledge base generation is a future separate direction. It is not part of a
normal Sourcefold book-processing run.

## Rules

- Treat `Source/` and original PDFs/images as immutable inputs.
- Preserve layout semantics when traceability matters: headings, emphasis,
  quotes, lists, tables, cards, stat blocks, and page markers.
- Do not copy code, commands, package prompts, current status, or governance
  from `translator` without a separate migration review.
- Prefer structured parsers and reproducible tools over manual text edits.
- Prefer a reproducible working environment over custom automation: install or
  declare standard tools with a lockfile/config when that gives stronger
  guarantees than hand-written parsing or ad hoc logic.
- Prefer checked-in scripts over manual procedures when an action must be
  repeated or audited. Manual actions are allowed only for narrow repair or
  exploration work and must leave durable evidence in plan/context/status.
- When installing or changing project tooling, update `SETUP.md` and the
  relevant docs/status with what changed, why it is needed, and how to
  reproduce it on another machine.
- Keep Markdown output readable and Obsidian-compatible.
- Do not commit secrets, credentials, auth files, local environment state,
  temporary logs, OCR overlays, or browser profiles.
- Update `PROJECT_STATUS.md` for project rollup changes and use
  `docs/plans/<goal-id>/` for bundled goals.
- For user requests such as `обнови документацию`, `зафиксируй документацию`,
  `обнови статус`, or `зафиксируй статус`, use
  `scripts/documentation_checkpoint.ps1` as the checkpoint contract. Start with
  dry-run unless the update payload and target goal are explicit.
- Run `scripts/validate_roadmap.ps1` before committing roadmap or checkpoint
  changes. The checkpoint script runs it automatically unless explicitly
  skipped for a narrow repair.

## Goal Governance

Sourcefold follows `../docs/governance/nri_goal_governance.md`.

The main-chat orchestrator owns `PROJECT_STATUS.md`, goal `plan.md`, goal
`context.md`, and release evidence. Contributors receive compact task packets
and write immutable handoff receipts under the goal's `handoffs/` directory.
After a real UI-visible contributor subagent/thread completes its bounded task
and its result or receipt has been captured, the orchestrator explicitly closes
it unless a specific immediate follow-up task has already been assigned.

Role defaults:

- `gpt-6-sol`: orchestrator at medium effort.
- `gpt-6-sol`: engineering assistant at high effort.
- `gpt-6-astra`: independent critic at high effort.
- `gpt-6-astra`: analyst and architect at high effort.
- `gpt-6-luna`: bounded executor at high effort.
- `gpt-6-luna`: bounded QA support at medium effort.

These are repository-policy assignments, not proof of the model selected by a
platform. Final release approval requires an independent `gpt-6-astra` critic
review. If that is unavailable, final acceptance remains pending.

## Orchestrator Review Workflow

For bounded Sourcefold project layers, the main-chat agent acts as the
orchestrator and must use a two-reviewer gate before asking Bogdan to evaluate
target material.

- Sol is the analytical reviewer. Ask Sol to expand the plan, check expected
  artifacts, dependencies, coverage, and synchronization surfaces.
- The independent `gpt-6-astra` critic finds blockers, boundary overreach, stale
  state, missing guardrails, and wording drift.
- Proceed only when both Sol and the independent critic return OK for the same
  bounded scope.
- If either reviewer returns blockers or NOT OK, fix the concrete blockers and
  repeat the Sol/critic cycle before proceeding.
- Go to Bogdan only after the target material is ready and has passed the
  Sol/critic gate.
- When asking Bogdan to review target material, attach the relevant files in
  chat and explain what to inspect, what decision is needed, and what each
  choice affects.
- Do not ask Bogdan to verify hashes, file paths, pytest output, test keys,
  stale scans, diff checks, line-ending checks, or internal QA checklists.
  Those are the orchestrator's responsibility.

## Phase/Gate Work Rules

- Treat roadmap phases, gates, decisions, and core releases as separate layers:
  phases contain gates, gates own decision packets, and accepted gates unlock
  later implementation.
- `Gate 1 Source Profile` is the current Phase 0 gate. It must collect its
  input package, subcomponents, parameters, qualification evidence, and
  acceptance/parking decisions before Core 0.1 implementation starts.
- Candidate inputs under `fixtures/candidate_inputs/` are durable inputs for
  bounded qualification work. `G1FADAR-G1-VIRAL-001` admits the named Gate 1
  Viral fixture groups only; candidate inputs remain not accepted source
  evidence, not whole Gate acceptance, and not permission to process a book.
- Do not render, OCR, translate, proofread, or otherwise process a candidate
  input until the exact qualification protocol revision is accepted and a
  separate bounded authorization names the exact action, admitted inputs,
  allowed outputs, limits, authority, expiry, and invalidation behavior.
- For Core 0.1 text-extraction probes, do not treat human review crops or
  `*-text-evidence.png` assets as automatically OCR-safe. Follow the canonical
  OCR input-surface policy in
  `docs/plans/20260715-sourcefold-phase-0-release-charter/gate_01_qualification_protocol.md`
  and the acceptance criteria `AM-04-03` / `AM-G1-05A` in
  `core_0_1_acceptance_matrix.md`. `C01TEFG017018` remains candidate-only until
  a separate promote-or-park decision; reference-guided repair is support
  evidence only, not independent OCR validation.
- Pre-OCR map work (`doc_map`, `content_map`, `art_map`, and
  `pre_ocr_map_bundle`) is governed by Gate 1. Roadmap YAML may show node
  status, dependencies, checklist state, comments, and linked plans only; map
  payloads belong in dedicated evidence artifacts controlled by schema,
  identity, and trace-anchor decisions.
- Visualizations are readers of canonical roadmap/map artifacts, not sources of
  truth. If a viewer and YAML or evidence artifact disagree, update the
  artifact first and then refresh the viewer/state.
- Subagents working on gates must report against the gate's hierarchy:
  `Phase -> Gate -> Component -> Subcomponent -> Parameter -> Evidence`.
  Handoffs must say which parameters changed state, which evidence was checked,
  and which blockers remain.
