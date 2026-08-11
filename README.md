# Story Engine

**Story Engine** is an open-source skill/framework for diagnosing and co-designing sustainable plot progression in long-form fiction.

It focuses on the mechanics that keep a story moving: **activation, a settleable stage goal, cost of inaction, constraints, costly choices, action/feedback, gains and costs, persistent state changes, and the pull into the next stage**.

The project is designed to be usable as a standalone writing framework or as a component inside an AI/agent workflow.

> Public status: **0.1.1 — English documentation maintenance release.** The repository does not claim external adoption or model-evaluation pass rates that cannot be reproduced.

## Why this is more than a prompt

Story Engine includes:

- eight stable rule IDs (`SE-RC-*`, `SE-F-*`);
- an explicit input schema and source-marking discipline;
- deletion tests and counterfactual tests;
- risk boundaries that prevent overconfident quality judgments;
- machine-readable behavioral evaluation cases;
- a deterministic repository validator;
- a generic structured-output contract and JSON Schema;
- examples for stage diagnosis, continuity, and dual-engine stories.

## Core rules

### Positive structure rules

| Rule | Purpose |
|---|---|
| `SE-RC-001` | General plot-engine loop |
| `SE-RC-002` | Resource-scarcity engine |
| `SE-RC-003` | Anti-goal engine |
| `SE-RC-004` | Reality-goal + hidden-task dual engine |
| `SE-RC-005` | Rule-pressure engine |

### Risk-diagnosis rules

| Rule | Purpose |
|---|---|
| `SE-F-001` | Restart / continuity risk |
| `SE-F-002` | Formulaic repetition risk |
| `SE-F-003` | Multi-engine imbalance risk |

The `SE-F-*` rules are **risk diagnostics, not hard judgments that a work is bad or broken**.

## Quick start

1. Read or load `SKILL.md` as the main instruction file.
2. Provide the current story idea, stage outline, or adjacent stages.
3. Let the skill select the relevant rule cards under `references/`.
4. For structured integrations, use `references/integration-contract.md` and optionally validate output against `schemas/story-engine-output.schema.json`.

Example request:

```text
Use Story Engine to diagnose these two adjacent plot stages.
Preserve everything I mark as confirmed. Do not invent missing canon.
Check whether stage 2 actually depends on the consequences of stage 1.
```

## Source-marking discipline

Story Engine distinguishes:

- `[CONFIRMED]` confirmed by the user;
- `[IMMUTABLE]` explicitly immutable;
- `[SUGGESTION]` replaceable proposal;
- `[INFERENCE]` inference from confirmed material;
- `[ASSUMPTION]` temporary assumption for testing;
- `[UNVERIFIABLE]` insufficient evidence.

New characters, organizations, powers, rules, events, or endings must not be presented as confirmed canon unless the user supplied or approved them.

## Repository layout

```text
story-engine/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── rule-cards.md
│   ├── input-schema.md
│   ├── output-templates.md
│   ├── diagnostic-tests.md
│   ├── evidence-boundaries.md
│   └── integration-contract.md
├── schemas/
│   └── story-engine-output.schema.json
├── examples/
│   ├── basic-diagnosis.md
│   ├── stage-transition.md
│   └── dual-engine.md
├── tests/
│   ├── test-prompts.json
│   ├── test-cases.md
│   ├── behavioral-eval.md
│   └── run_tests.py
└── .github/
    └── workflows/
        └── validate.yml
```

## Validation

Run the deterministic repository checks:

```bash
python tests/run_tests.py
```

This validates repository structure, rule IDs, test definitions, local references, JSON files, and public-release hygiene. It **does not** pretend to execute an LLM.

For model/agent behavior evaluation, follow `tests/behavioral-eval.md` and use `tests/test-prompts.json`.

## Examples

- `examples/basic-diagnosis.md` — diagnose a single stage.
- `examples/stage-transition.md` — test continuity between adjacent stages.
- `examples/dual-engine.md` — check whether two plot engines actually feed each other.

## Scope

Story Engine is primarily for plot progression and continuity. It is not a replacement for prose editing, full character-arc design, encyclopedic worldbuilding, factual research, or style imitation.

## Contributing

Issues and pull requests are welcome. See `CONTRIBUTING.md` for the rule-change and test expectations.

## License

MIT. See `LICENSE`.
