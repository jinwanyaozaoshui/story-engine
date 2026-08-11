# Behavioral Evaluation

`test-prompts.json` is a model/agent behavioral-evaluation set, not a deterministic unit-test suite.

## Why these are separate

`tests/run_tests.py` can deterministically validate repository structure, rule IDs, JSON fields, local references, and public-release hygiene. It cannot prove that a language model will perform the intended narrative diagnosis.

## Recommended evaluation procedure

1. Choose the model or agent runtime to evaluate.
2. Load `SKILL.md` and the required reference files.
3. Run each `prompt` in `test-prompts.json`.
4. Record model name/version, run date, system prompt or skill-loading method, and raw output.
5. Score the output against `expected_trigger`, `expected_rules`, `expected_behavior`, `forbidden_behavior`, and `pass_criteria`.
6. Publish a pass-rate claim only when the execution method or raw records can be reproduced.

## Do not conflate

- **Repository validation passed** means the public repository structure and test definitions are internally consistent.
- **Behavioral evaluation passed** means a specific model/agent, in a specific runtime, met the behavioral criteria.

They are not the same claim.
