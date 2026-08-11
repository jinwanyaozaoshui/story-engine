# Contributing

Contributions are welcome, especially reproducible examples that reveal false positives, false negatives, unclear boundaries, or missing structural cases.

## Before opening a rule-change PR

Please include:

1. the rule ID affected;
2. a minimal fictional example that reproduces the issue;
3. the current behavior;
4. the desired behavior;
5. why the change does not turn a risk diagnostic into a universal quality judgment;
6. an update to `tests/test-prompts.json` when behavior expectations change.

## Rule stability

Existing rule IDs should not be silently repurposed. If a rule changes meaning materially, document it in `CHANGELOG.md` and consider a new rule ID.

## Validation

Run before submitting:

```bash
python tests/run_tests.py
```

If a contribution claims a model/Agent behavior improvement, include enough information to reproduce the behavioral evaluation (model/runtime, prompt loading method, date/version when relevant, and raw output or harness).

## Privacy and examples

Do not submit private manuscripts, credentials, personal paths, unpublished proprietary material, or third-party copyrighted text that you do not have permission to redistribute. Prefer minimal synthetic examples.
