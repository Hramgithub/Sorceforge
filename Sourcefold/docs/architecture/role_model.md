# Role Model

Sourcefold uses the NRI role model from
`../../../docs/governance/nri_goal_governance.md` through project-local goal
bundles.

## Roles

| Role | Model | Effort | Responsibility |
|---|---|---|---|
| Orchestrator | `gpt-6-sol` | medium | Owns project rollup, goal context, plan state, integration, stop/ask decisions, and user-facing synthesis. |
| Engineering assistant | `gpt-6-sol` | high | Reviews reusable implementation, tests, and engineering risks within a bounded task packet. |
| Independent critic | `gpt-6-astra` | high | Performs independent criticism or release review and must not own implementation under review. |
| Analyst/architect | `gpt-6-astra` | high | Handles root-cause analysis, architecture, dependency reasoning, and remediation specifications. |
| Bounded executor | `gpt-6-luna` | high | Performs mechanical edits against an accepted specification. |
| Bounded QA | `gpt-6-luna` | medium | Collects bounded verification evidence without owning the implementation. |

These assignments are repository policy; they do not prove or change the model
selected by the execution platform. If an independent `gpt-6-astra` release
critic is unavailable, final acceptance remains pending.

## Handoffs

Every non-exempt contributor receives a compact task packet and writes an
immutable receipt under `docs/plans/<goal-id>/handoffs/`. Receipts summarize
scope, result, files checked or changed, evidence, blockers, next action, and
token use when available.

The orchestrator owns canonical context and may update plan/status from
handoff evidence. Contributors do not edit canonical project state unless a
specific task packet explicitly grants that scope.
