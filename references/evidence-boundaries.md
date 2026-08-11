# Validation Boundaries

Story Engine contains two rule classes: **positive structure rules** (`SE-RC-*`) and **risk-diagnosis rules** (`SE-F-*`). Both analyze supplied material; neither exists to issue absolute quality verdicts on an entire work.

## Strength of claims

| Rule | Public role | Hard judgment allowed? |
|---|---|---|
| `SE-RC-001` | Basic stage-structure check | May directly identify missing activation, goal, constraints, choices, feedback, or residue in the supplied material. |
| `SE-RC-002` | Resource-scarcity specialist | No. Flag weak resource function, number-only rewards, or transition risk. |
| `SE-RC-003` | Anti-goal specialist | No. Flag incoherent external evaluation, fixed misunderstanding, or repetition risk. |
| `SE-RC-004` | Reality/hidden dual engine | May strongly flag a side that has no sustained function, but not declare the whole work failed. |
| `SE-RC-005` | Rule-pressure specialist | No. Flag rule-complexity side effects and weakened character agency. |
| `SE-F-001` | Restart/continuity risk | No. Requires adjacent/continuous material and deletion testing. |
| `SE-F-002` | Formulaic repetition risk | No. Requires at least three comparable cycles. |
| `SE-F-003` | Multi-engine imbalance risk | No. Requires continuous-stage evidence, functional checks, and deletion testing. |

## Boundaries that must remain

- A stable genre loop is not automatically formulaic.
- Productive variation should be preserved.
- Changing map, job, task, or power does not automatically mean restart.
- Episodic fiction may reset some state while still preserving minimum cumulative consequence.
- Temporary changes in primary/secondary engine weight do not automatically mean imbalance.
- Engine transition is not engine failure.
- Terminal closure does not require another objective.
- Rule complexity does not automatically imply multi-engine imbalance.
- As rules become more complex, check whether character choice, emotion, and relationship consequences still change outcomes.

## When evidence is insufficient

Use `[UNVERIFIABLE]`, `[RISK]`, `[SUGGESTION]`, or `[ASSUMPTION]`. Do not invent missing canon and then announce that a rule has been proven.

## Eight residue categories

Story Engine checks whether stage results change identity, permission/access, resources, responsibility, relationships, knowledge, public label, and medium/location state. A stage need not cover every category.

## Powers and world rules

Use only the scope, triggers, costs, and medium constraints already confirmed by the user. Do not generalize one example's limits into a universal rule.

## Behavioral evaluation vs deterministic validation

- `tests/run_tests.py` performs **deterministic repository validation**: files, JSON, rule IDs, fields, local references, and public-hygiene checks.
- `tests/test-prompts.json` defines **model/agent behavioral-evaluation cases**. A pass claim requires an actual model/agent run evaluated against expected and forbidden behaviors.
- Deterministic repository validation passing does not imply model behavioral evaluation passing.
