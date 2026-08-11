#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_IDS = {
    "SE-RC-001", "SE-RC-002", "SE-RC-003", "SE-RC-004", "SE-RC-005",
    "SE-F-001", "SE-F-002", "SE-F-003",
}
REQUIRED_FILES = [
    "README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
    "SECURITY.md", "SKILL.md", "agents/openai.yaml",
    "references/rule-cards.md", "references/input-schema.md", "references/output-templates.md",
    "references/diagnostic-tests.md", "references/evidence-boundaries.md",
    "references/integration-contract.md", "schemas/story-engine-output.schema.json",
    "tests/test-prompts.json", "tests/test-cases.md", "tests/behavioral-eval.md",
    "examples/basic-diagnosis.md", "examples/stage-transition.md", "examples/dual-engine.md",
    "docs/design-principles.md",
]

class ValidationError(Exception):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)

def read_text(rel: str) -> str:
    p = ROOT / rel
    require(p.exists(), f"missing file: {rel}")
    return p.read_text(encoding="utf-8")

def validate_required_files() -> None:
    for rel in REQUIRED_FILES:
        require((ROOT / rel).is_file(), f"required file not found: {rel}")
    require(not (ROOT / "tests/test-results.md").exists(), "public package must not contain pre-written test-results.md")

def validate_skill() -> None:
    text = read_text("SKILL.md")
    require(text.startswith("---\n"), "SKILL.md must start with frontmatter")
    parts = text.split("---", 2)
    require(len(parts) == 3, "SKILL.md frontmatter is not closed")
    front = parts[1]
    require(re.search(r"(?m)^name:\s*story-engine\s*$", front) is not None, "SKILL.md name must be story-engine")
    require(re.search(r"(?m)^description:\s*.+$", front) is not None, "SKILL.md description is required")
    for rid in RULE_IDS:
        require(rid in text, f"SKILL.md missing rule reference {rid}")

    # Check local file paths mentioned in backticks.
    for path in re.findall(r"`((?:references|tests|schemas|examples|docs)/[^`]+)`", text):
        require((ROOT / path).exists(), f"SKILL.md references missing path: {path}")

def validate_agent_metadata() -> None:
    text = read_text("agents/openai.yaml")
    for key in ["skill_name", "display_name", "short_description", "default_prompt"]:
        require(re.search(rf"(?m)^\s{{2}}{re.escape(key)}:\s*.+$", text) is not None, f"agents/openai.yaml missing {key}")

def validate_rule_cards() -> None:
    text = read_text("references/rule-cards.md")
    for rid in RULE_IDS:
        require(rid in text, f"rule-cards.md missing {rid}")

def validate_json_files() -> None:
    tests = json.loads(read_text("tests/test-prompts.json"))
    require(tests.get("skill") == "story-engine", "test-prompts.json skill must be story-engine")
    require(tests.get("version") == "0.1.0", "test-prompts.json version must match public release")
    cases = tests.get("test_cases")
    require(isinstance(cases, list) and cases, "test_cases must be a non-empty list")
    seen = set()
    required = {"id", "category", "prompt", "expected_trigger", "expected_rules", "expected_behavior", "forbidden_behavior", "pass_criteria"}
    for case in cases:
        require(isinstance(case, dict), "each test case must be an object")
        missing = required - set(case)
        require(not missing, f"{case.get('id', '<unknown>')} missing fields: {sorted(missing)}")
        cid = case["id"]
        require(re.fullmatch(r"SE-T\d{3}", cid) is not None, f"invalid test id: {cid}")
        require(cid not in seen, f"duplicate test id: {cid}")
        seen.add(cid)
        require(case["category"] in {"should-trigger", "should-not-trigger", "edge"}, f"invalid category in {cid}")
        require(isinstance(case["expected_trigger"], bool), f"expected_trigger must be bool in {cid}")
        require(isinstance(case["expected_rules"], list), f"expected_rules must be list in {cid}")
        require(set(case["expected_rules"]) <= RULE_IDS, f"unknown rule id in {cid}")
        if case["category"] == "should-not-trigger":
            require(case["expected_trigger"] is False, f"should-not-trigger case {cid} must expect false")
            require(case["expected_rules"] == [], f"should-not-trigger case {cid} must not require rules")
        for field in ["prompt", "expected_behavior"]:
            require(isinstance(case[field], str) and case[field].strip(), f"{field} must be non-empty in {cid}")
        for field in ["forbidden_behavior", "pass_criteria"]:
            require(isinstance(case[field], list) and all(isinstance(x, str) and x.strip() for x in case[field]), f"{field} invalid in {cid}")

    schema = json.loads(read_text("schemas/story-engine-output.schema.json"))
    enum = set(schema["properties"]["rules"]["items"]["enum"])
    require(enum == RULE_IDS, "JSON Schema rule enum must match RULE_IDS")

def validate_public_hygiene() -> None:
    # Intentionally exclude this validator itself because it defines the patterns.
    patterns = [
        re.compile(r"\b[A-Z]:\\"),
        re.compile(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*[\"\'][A-Za-z0-9_\-]{20,}[\"\']"),
    ]
    text_suffixes = {".md", ".json", ".yaml", ".yml", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == Path(__file__).resolve() or path.suffix.lower() not in text_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        for pat in patterns:
            require(pat.search(text) is None, f"private/internal marker found in {path.relative_to(ROOT)}: {pat.pattern}")

def main() -> int:
    checks = [
        ("required files", validate_required_files),
        ("skill frontmatter and references", validate_skill),
        ("agent metadata", validate_agent_metadata),
        ("rule cards", validate_rule_cards),
        ("JSON and test definitions", validate_json_files),
        ("public-release hygiene", validate_public_hygiene),
    ]
    try:
        for label, fn in checks:
            fn()
            print(f"PASS: {label}")
    except (ValidationError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("ALL DETERMINISTIC VALIDATION CHECKS PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
