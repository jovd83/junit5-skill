---
name: junit5-documentation-tests
description: Use when Codex needs to document JUnit 5 automation code with clear scenario intent, suite purpose, traceability, or maintainable human-readable explanations.
metadata:
  author: jovd83
  version: "1.0.0"
  dispatcher-category: testing
  dispatcher-capabilities: automation-documentation, junit5-test-documentation
  dispatcher-accepted-intents: document_junit_tests
  dispatcher-input-artifacts: test_suite, repo_context, traceability_artifacts
  dispatcher-output-artifacts: automation_docs, documentation_update
  dispatcher-stack-tags: junit5, documentation, automation
  dispatcher-risk: low
  dispatcher-writes-files: true
---

# JUnit 5 Test Documentation


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## 1. Inspect the Tests

1. Read the target test classes before documenting them.
2. Identify suite purpose, scenario intent, and major fixture patterns.
3. Preserve existing naming conventions unless the task explicitly includes renaming.

## 2. Document What Matters

1. Explain why the suite exists.
2. Explain what behavior each test or nested group protects.
3. Explain fixture or extension behavior only when it is not self-evident.
4. Keep comments and documentation brief and maintainable.

## 3. Troubleshooting

1. Problem: The tests are too opaque to document cleanly.
   Fix: Recommend structural cleanup instead of adding bloated comments.
