---
name: junit5-documentation-tests
description: Use when Codex needs to document JUnit 5 automation code with clear scenario intent, suite purpose, traceability, or maintainable human-readable explanations.
---

# JUnit 5 Test Documentation

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
