---
name: story-engine
description: Use for fiction plot-engine diagnosis and co-creation: stage goals, constraints, costly choices, feedback, persistent state changes, adjacent/cross-volume continuity, dual engines, resource/anti-goal/rule-pressure engines, restart/formula/imbalance risks, engine transition, and terminal closure. Not for prose polishing, full character arcs, encyclopedic worldbuilding, or style imitation.
---

# Story Engine

Story Engine is a structural diagnosis and co-design skill for long-form fiction and continuous plot progression. It does not treat a setting, power, or task label as a plot engine by itself. Instead, it checks **what forces the story to start now, what the protagonist must settle in the current stage, what constraints make choices costly, what feedback follows action, what persistent state change remains, and how that residue pulls the next stage into motion.**

## Core method

A viable stage usually needs:

1. an activation condition;
2. a settleable current-stage goal;
3. a cost of inaction;
4. meaningful constraints;
5. at least two materially different costly choices;
6. action and feedback;
7. gains and costs;
8. persistent state residue;
9. a pull into the next stage, except at terminal closure.

Story Engine supports both diagnosis and co-creation. In diagnosis mode, it identifies structural gaps and applies deletion/counterfactual tests. In co-design mode, it preserves confirmed canon and proposes replaceable candidates only where gaps exist, with source labels.

Risk rules identify structural risks in the supplied material. They are not universal judgments of a work's quality.

## Rule set

Positive structure rules:

- `SE-RC-001` General plot-engine loop
- `SE-RC-002` Resource-scarcity engine
- `SE-RC-003` Anti-goal engine
- `SE-RC-004` Reality-goal + hidden-task dual engine
- `SE-RC-005` Rule-pressure engine

Risk-diagnosis rules:

- `SE-F-001` Restart / continuity risk
- `SE-F-002` Formulaic repetition risk
- `SE-F-003` Multi-engine imbalance risk

## When to trigger

Good fits include:

- “Can this stage keep moving?”
- “Am I missing a goal, cost, obstacle, choice, or feedback loop?”
- “Does the next volume actually inherit consequences from the previous one?”
- “Do the reality line and hidden line feed each other?”
- “Are three consecutive cycles becoming too repetitive?”
- “Which of the resource, rule, identity, or relationship lines has no real function?”
- “Should the ending open another objective, or close consequences instead?”

Do not use Story Engine as the primary tool for pure prose polishing, complete character-arc design, encyclopedic worldbuilding, style imitation, or factual lookup.

## Execution flow

1. **Identify request mode**: quick diagnosis, idea completion, stage co-design, multi-stage review, cross-volume continuity, or focused risk review.
2. **Protect source boundaries**: distinguish `[CONFIRMED]`, `[IMMUTABLE]`, `[SUGGESTION]`, `[INFERENCE]`, `[ASSUMPTION]`, and `[UNVERIFIABLE]`. Any new character, organization, power, rule, event, or ending must be source-marked.
3. **Check input sufficiency**: if material is incomplete, diagnose what exists first. Do not ask a long questionnaire merely to fill a template.
4. **Start with `SE-RC-001`**: activation, goal, inaction cost, constraints, choices, action, feedback, gains/costs, persistent residue, and next-stage pull.
5. **Select specialist positive rules when relevant**: resource scarcity → `SE-RC-002`; anti-goal → `SE-RC-003`; reality/hidden parallel structure → `SE-RC-004`; rule pressure → `SE-RC-005`.
6. **Select risk rules only when evidence is sufficient**: adjacent stages/cross-volume/map-job-power changes → `SE-F-001`; at least three comparable loops → `SE-F-002`; multiple engines in parallel → `SE-F-003`.
7. **Run deletion and counterfactual tests** as needed: remove the previous stage, one side of a dual engine, an engine line, a task giver, or a long-term clue; test partial success, old-solution failure, resource backlash, power-change continuity, engine transition, and terminal closure.
8. **Trim the output** to the user's actual task, then verify that every newly invented story element is source-marked.

## Hard boundaries

- `SE-F-001`, `SE-F-002`, and `SE-F-003` are not hard failure verdicts.
- A stable genre loop is not automatically formulaic.
- Changing map, job, task type, or power does not automatically mean a restart.
- Temporary shifts in primary/secondary engine weight do not automatically mean imbalance.
- Engine transition is not engine failure.
- Terminal closure does not require another objective.
- Greater rule complexity does not automatically imply multi-engine imbalance.

Eight residue categories: identity, permission/access, resources, responsibility, relationships, knowledge, public label, and medium/location state. A stage does not need to change all eight.

## Read on demand

- `references/rule-cards.md`: the eight detailed rule cards and boundaries.
- `references/input-schema.md`: request modes, input fields, and residue categories.
- `references/output-templates.md`: diagnosis and co-design output templates.
- `references/diagnostic-tests.md`: deletion and counterfactual tests.
- `references/evidence-boundaries.md`: evidence thresholds and risk-rule boundaries.
- `references/integration-contract.md`: generic structured integration contract.
- `schemas/story-engine-output.schema.json`: optional structured-output JSON Schema.
- `tests/test-prompts.json`: behavioral-evaluation prompts, expected rules, and forbidden behaviors.
- `tests/run_tests.py`: deterministic repository validation.

## Version

Public release: `0.1.0`.
