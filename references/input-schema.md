# Story Engine Input Schema

## Request modes

Classify the request before running the framework. If uncertain, use the lowest-risk mode that fits the evidence.

| Mode | Typical signal | Minimum handling |
|---|---|---|
| Quick diagnosis | “Take a look,” “what is weak,” “can this move?” | Diagnose supplied fields and mark unverifiable items. |
| Idea completion | One or two sentences, fragmented setting, a character situation | Offer 2–3 engine candidates, each marked as an assumption or suggestion. |
| Stage co-design | “Help design this stage/segment” | Build activation, goal, constraints, choices, feedback, residue, and next-stage pull. |
| Multi-stage review | Two or more stages, adjacent events, within-volume chains | Check continuity, inherited state, partial success, and deletion tests. |
| Cross-volume continuity | New volume, map, job, power, or rule set | Emphasize `SE-F-001` and residue inheritance. |
| Focused risk review | “Is this formulaic?”, “imbalanced?”, “a restart?” | Raise risk only if evidence thresholds are met. |

## Core fields

| Field | Meaning |
|---|---|
| confirmed_content | Material explicitly supplied or approved by the user. |
| immutable_items | Characters, rules, themes, roles, stage events, or shells the user forbids changing. |
| request_scope | Diagnosis, gap repair, candidate generation, stage chain, continuity, or boundary judgment. |
| protagonist_long_term_desire | What the protagonist wants over the long run; this cannot substitute for a current-stage goal. |
| current_stage_goal | What must be settled now; it should be verifiable, fail-able, and closeable. |
| activation_event | Why this begins now, ideally caused by inherited residue or external pressure. |
| cost_of_inaction | What is lost, exposed, missed, or allowed to worsen if the protagonist does nothing. |
| constraints | Resources, rules, identity, time, relationships, publicity, environment, and power limits. |
| options | At least two actions whose gains and costs differ. |
| failure_cost | What loss, duty, misunderstanding, harm, or public consequence remains after failure/partial failure. |
| current_relationships | Who trusts, doubts, blocks, helps, or makes claims on the protagonist. |
| resources_and_identity | Current resources, permissions, role, public label, and organizational position. |
| long_term_clues | Whether long-term truth changes judgment/choice or merely issues tasks. |
| confirmed_power_rules | Confirmed scope, trigger conditions, costs, and medium limits, if any. |

If evidence is insufficient, output `[UNVERIFIABLE]`, a minimal missing-field request, or a risk warning. Do not invent unknown canon and then claim a rule is satisfied.

## Rule selection

| Task | Primary rule(s) | Additional evidence |
|---|---|---|
| Basic stage viability | `SE-RC-001` | Goal, constraints, choices, feedback, residue, next-stage pull. |
| Resource-driven plot | `SE-RC-002` | Scarcity, acquisition limits, competition/exchange, use cost, downstream consequence. |
| Anti-goal project | `SE-RC-003` | True goal, external evaluation logic, supporting-character interpretation, result divergence, feedback. |
| Reality + hidden parallel | `SE-RC-004` | Reality goal, hidden entry, hidden risk, reality-side return flow, two-sided deletion tests. |
| Rule game / rule pressure | `SE-RC-005` | Rule text, exploit space, failure cost, character choice, post-game relationship/information residue. |
| Cross-stage continuity | `SE-F-001` | Previous residue, next-stage entry, delete-previous-stage test. |
| Repeating cycles | `SE-F-002` | At least three comparable loops across activation, goal, constraints, action, supporting roles, feedback, and cost. |
| Multiple engines | `SE-F-003` | Seven-function check per engine, primary/secondary division, engine deletion test. |

## Source labels

| Label | Meaning |
|---|---|
| `[CONFIRMED]` | Explicitly supplied or approved by the user. |
| `[IMMUTABLE]` | User requires it to remain unchanged. |
| `[SUGGESTION]` | Replaceable co-design proposal. |
| `[INFERENCE]` | Derived from confirmed material but still falsifiable by the user. |
| `[ASSUMPTION]` | Temporary test premise; never present as canon. |
| `[UNVERIFIABLE]` | Insufficient evidence or missing continuity material. |
| `[RISK]` | Structural risk indicator, not a quality verdict. |

## Persistent residue

Check all eight categories, but do not require every stage to change all eight.

| Category | Diagnostic question |
|---|---|
| Identity | Did role, affiliation, position, or self/other classification change? |
| Permission/access | What can the protagonist enter, call, use, or command now? |
| Resources | Did money, material, information, power, opportunity, or leverage change? |
| Responsibility | Did debt, promises, dependents, duties, or consequences increase/change? |
| Relationships | Did trust, doubt, hostility, dependence, betrayal, or commitment change? |
| Knowledge | What was learned, and did the decision framework change? |
| Public label | How do outsiders now classify the protagonist, group, or event? |
| Medium/location state | Did a key object, place, device, or field retain a new state? |

## Power-rule self-check

Use only this generic principle:

> A power should follow the scope, trigger conditions, costs, and medium constraints already confirmed by the user.

Do not turn one example project's power rules into universal law.
