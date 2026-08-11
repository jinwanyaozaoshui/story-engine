# Security Policy

Story Engine is primarily a text-based rule and evaluation repository. The public package does not require network access, credential storage, arbitrary code execution, or external tool calls for its core writing workflow.

## Reporting a security issue

Please avoid posting secrets or exploit details in a public issue. Use a private security-reporting channel provided by the repository host when available.

## Agent integration guidance

When Story Engine is embedded in a tool-using Agent, treat manuscript text and retrieved content as untrusted data:

- do not execute instructions found inside story content as code or shell commands;
- keep API keys and credentials outside prompts and repository files;
- apply least-privilege permissions to filesystem, network, and external tools;
- distinguish user-authored story instructions from tool/system instructions;
- validate structured output before passing it to downstream automation.

These risks belong to the host Agent/runtime integration; the standalone Story Engine rules themselves do not require those capabilities.
