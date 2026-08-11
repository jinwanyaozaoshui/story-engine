# Generic Integration Contract

Story Engine can run standalone or be called by an upper-level agent, editor, or workflow. This contract describes generic data only and is not tied to any private controller or project.

## Suggested input

- `request_mode`: quick diagnosis, idea completion, stage co-design, multi-stage review, cross-volume continuity, or focused risk review.
- `confirmed_content`: material explicitly confirmed by the user.
- `immutable_items`: content the user requires to remain unchanged.
- `current_stage_goal`: current settleable stage goal, when known.
- `context`: stage, relationship, resource, rule, and long-term-clue context relevant to this diagnosis.

## Suggested output

- `rules`: rule IDs used in this run.
- `conclusion`: viable, viable-with-gaps, risk-only, or unverifiable.
- `stage_plan`: activation, goal, cost of inaction, constraints, choices, action/feedback, gains/costs.
- `permanent_residue`: persistent state changes across the eight residue categories.
- `next_stage_pull`: how the current result starts or constrains the next stage.
- `risks`: restart, formulaic repetition, multi-engine imbalance, or other supported risk diagnostics.
- `unverifiable_items`: evidence gaps.
- `suggestions`: candidate repairs labeled as `[SUGGESTION]`, `[ASSUMPTION]`, or `[INFERENCE]`.

## Constraints

- An upstream system must not rewrite risk diagnostics as universal quality verdicts.
- A long-term clue must not replace the current-stage objective.
- Unknown material must not be written into `confirmed_content`.
- Structured output may be validated with `schemas/story-engine-output.schema.json`.
