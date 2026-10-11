# NRI Goal Governance

## Scope And Boundary

This is the canonical NRI-wide standard for goals, durable context, plans,
handoffs, independent review, and release evidence. It applies to all projects
under this workspace.

`Sourcefold` is the first product that will adopt this standard from its first
scaffold. `CoC` and `Dune` adopt it only for new substantial goals. `translator`
is legacy implementation evidence: it may inform future work but is not the
source of truth for NRI governance.

## Default Orchestration Role And Platform Boundary

For every NRI task and goal, the repository-policy default main-chat
orchestrator is `gpt-6-sol` at `medium` reasoning effort. This applies without a
user reminder and is restored whenever work starts, resumes, or recovers from
context compaction.

The main-chat orchestrator owns task classification, goal initiation, canonical
plan and context state, contributor dispatch, integration, stop-or-ask
decisions, and user-facing synthesis. Assigning a contributor role or model
never transfers orchestration ownership.

Repository policy assigns responsibilities; it does not select, switch, or
prove the model or reasoning effort used by the Codex platform. Record actual
model or effort only when the platform exposes a verifiable value; otherwise
record `unavailable` rather than claiming a switch occurred.

If the verified runtime differs from the policy default, continue as
`orchestrator-policy-fallback` unless the user made that exact model or effort a
hard requirement. A hard-requirement mismatch requires a stop-and-ask decision.

A user may explicitly override the orchestrator or effort for one task or one
goal. The narrowest stated scope applies and is recorded in the canonical plan.
Such an override does not change the workspace default and cannot waive safety,
canonical-state ownership, critic independence, or the independent critic release gate.

The default contributor role matrix is:

- engineering: `gpt-6-sol` at `high`;
- independent critic: `gpt-6-astra` at `high`;
- architect: `gpt-6-astra` at `high`;
- bounded executor: `gpt-6-luna` at `high`;
- bounded QA: `gpt-6-luna` at `medium`.

The deprecated `nri-release-reviewer` profile uses `gpt-6-sol` at `medium`
by explicit user request (2026-09-26). It retains the review procedure but does
not substitute for the mandatory independent `gpt-6-astra` release gate.
Previously recorded assignments and reviews remain historical evidence.

## When A Goal Bundle Is Required

Before work, the main-chat orchestrator reads applicable instructions and any
assigned plan or status, then classifies the task as exempt or bundled.

A platform runtime goal, a durable goal bundle, and a task packet's `goal_id`
are distinct records. Creating one does not satisfy the requirements of another.

Create a goal bundle before work when at least one condition is true:

- a subagent is delegated work;
- work will resume in another turn or chat;
- a formal review or release decision is required;
- the work has two dependent write, generate, or verify stages.

A task is exempt only when all conditions are true: it is read-only, has no
delegation, has no side effect, makes no acceptance decision, and is expected to
finish in the current turn. Materialize the bundle before the task crosses any
of those boundaries.

Use a project-local immutable goal id: `YYYYMMDD-kebab-slug`; append `-02`,
`-03`, and so on for a same-day collision. A goal state is one of `active`,
`paused`, `blocked`, `completed`, `cancelled`, or `superseded`. Release state is
separate from goal state.

## Durable State Layout

Each project keeps its `PROJECT_STATUS.md` as a concise project rollup and an
index of active or paused goals. It links to, but does not duplicate, each
goal's detailed history.

For a bundled goal, use the project's established plans root. A new project,
including Sourcefold, uses this layout:

```text
docs/plans/<goal-id>/
  plan.md
  context.md
  handoffs/
  release.md              # only for a frozen release candidate
```

`plan.md` records steps, owner, effort, dependencies, Definition of Done,
status, evidence, blocker, and next action. `context.md` is the orchestrator's
current checkpoint: objective, accepted decisions and constraints, completed
evidence, active step, blockers, next action, and relevant links.

Every bundled-goal plan also records the role contract version, policy
orchestrator and effort, contributor role assignments, assignment state
(`matched`, `platform-unverified`, `platform-mismatch`, or `user-overridden`),
and the scoped override or `none`. Record actual platform model or effort only
when it is verifiable.

Only the main-chat orchestrator edits `PROJECT_STATUS.md`, `plan.md`,
`context.md`, and `release.md`. This prevents concurrent contributors from
overwriting canonical state.

## Contributor Receipts And Token Hygiene

At dispatch, the orchestrator gives a contributor a compact task packet:

```text
goal_id, step_id, contributor role and requested effort,
orchestrator policy owner,
relevant paths, expected artifact, acceptance criteria,
forbidden scope, handoff path, and expected completion condition.
```

Do not copy broad chat history into task packets. Contributors read the linked
project artifacts locally and return only a compact summary to the main chat.

Every non-exempt contributor writes an immutable receipt under `handoffs/`.
It records: goal id, step id, role, model, effort, scope, result, files checked
or changed, verification/evidence, blockers, next action, elapsed time, token
use or `unavailable`, timestamp, orchestrator policy owner, assignment state,
and scoped override or `none`. A correction supersedes a prior receipt; it does
not rewrite it.

A contributor assignment never changes the goal's orchestrator. Only an
explicit override recorded in canonical plan state can do so.

When a real UI-visible contributor subagent or agent thread completes its
bounded task, the orchestrator captures the compact result and verifies the
required receipt or artifact, then explicitly closes that subagent or thread.
Keep a completed contributor open only when a specific immediate follow-up task
has already been assigned to the same contributor. Otherwise, leaving completed
subagents open is a resource leak and violates NRI token hygiene.

## Recovery And Watchdog

The orchestrator does not silently repeat an active delegated task. If the
expected receipt or artifact is absent, it first requests a checkpoint, then
resumes or restarts the same narrow task, and verifies the expected artifact.
Only after repeated failure, invalid evidence, invalid scope, or a real blocker
may the orchestrator take over the task itself; it records the reason in the
goal context.

The watchdog is event-driven, not a fixed polling interval. At dispatch, define
the expected artifact and completion condition. Check on command completion,
the declared subtask deadline, a blocked dependency, a user status request, or
an explicit timeout. If evidence is absent at that point, request a checkpoint
and apply the recovery rule.

On every bundled-goal continuation or context recovery, reread applicable
`AGENTS.md` instructions, this governance standard, and the assigned
plan/context before work. Restore orchestration ownership from canonical plan
state. A contributor packet, receipt, recent speaker, or model label must not
silently replace that owner.

## Seed Defects And Full-Scope Closure

Any user-provided example of a pipeline defect is treated as a seed case for a
defect class until proven otherwise. The orchestrator must expand the task from
the single example to the full relevant scope before closing it.

The standard closure path is:

```text
seed case -> defect class -> full-scope audit -> pipeline fix -> rebuild -> evidence
```

For each defect class, the orchestrator records the earliest failing layer,
such as source reconstruction, translation preservation, projection, rendering,
asset placement, or release packaging. A defect is not closed by a final
artifact edit alone. It is closed only after the relevant source/config/script
or QA control is updated, all analogous cases in scope are searched, rebuilt
artifacts are produced when applicable, and evidence for the full-scope pass is
linked from the plan or status.

## Independent Criticism And Release

The independent critic is `gpt-6-astra` at `high` reasoning effort. Review
kinds are `concept`, `architecture`, `process`, `implementation`, and `release`.
Only `release` is a mandatory final gate for a frozen candidate.

The critic must not have implemented or materially designed the candidate under
review. This is a documented procedure, not something a model profile can prove.

A release receipt records the candidate revision or SHA-256 manifest, freeze
time, implementer/designer participation declaration, QA artifact references,
intentional exclusions, critic identity, findings, and recommendation. Any
candidate mutation invalidates the release receipt and requires a new review.

## Legacy Adoption

Do not backfill old plans, add a global goal database, require hashes for
ordinary receipts, create locks/leases, or migrate historical project state.
Adopt this standard only for new bundled goals. Existing project-specific plan
roots may remain in use when they already provide equivalent durable state.
