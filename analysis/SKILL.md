---
name: junit5-analysis
description: Use when Codex needs to derive JUnit 5 test scenarios from requirements, code, or existing test case definitions such as TDD, BDD, and plain-text specifications.
metadata:
  author: jovd83
  version: "1.0.0"
  dispatcher-category: testing
  dispatcher-capabilities: requirements-analysis, junit5-requirements-analysis
  dispatcher-accepted-intents: analyze_junit_requirements
  dispatcher-input-artifacts: requirements, target_code, repo_context
  dispatcher-output-artifacts: analysis_baseline, test_candidates, open_questions
  dispatcher-stack-tags: junit5, analysis, jvm
  dispatcher-risk: low
  dispatcher-writes-files: false
---

# JUnit 5 Analysis


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## 1. Inspect the Source Artifact

1. Identify whether the source is a requirement, code path, defect report, TDD case, BDD scenario, or plain-text test definition.
2. Extract the concrete behavior, inputs, outputs, side effects, preconditions, and edge cases.
3. Keep explicit source traceability in the notes or output.
4. Read [references/source-artifact-types.md](references/source-artifact-types.md) when the source format mixes prose, examples, and implementation detail.

## 2. Normalize the Behavior

1. Convert narrative language into executable behaviors.
2. Separate confirmed behavior from inferred coverage.
3. Label inferred scenarios explicitly instead of presenting them as sourced facts.
4. Use [references/traceability-patterns.md](references/traceability-patterns.md) when the user needs the result mapped back to story IDs, sections, or scenario names.

## 3. Choose the JUnit Shape

1. Map small deterministic behavior to component tests.
2. Map framework-backed behavior to slice, repository, or integration tests.
3. Map service behavior to service-isolated or service-end-to-end tests.
4. Use parameterized tests for scenario tables or repeated examples.
5. Read [references/source-mapping.md](references/source-mapping.md) when mapping narrative artifacts into code.
6. Read [references/narrative-formats.md](references/narrative-formats.md) when converting TDD, BDD, or plain-text cases into a JUnit 5 structure.

## 4. Produce Actionable Output

1. Output a scenario list, test-class plan, or directly implement the tests when requested.
2. Preserve the source wording only when it improves traceability.
3. Flag missing acceptance criteria or ambiguity instead of inventing rules.
4. When asked to implement directly, keep inferred additions separated from source-backed cases in comments, notes, or test naming.

## 5. Examples

1. Input: `Turn these Gherkin scenarios into JUnit 5 tests.`
   Output: A traceable list of parameterized and focused test cases aligned to the scenarios.
2. Input: `Derive tests from this service class.`
   Output: A behavioral matrix covering happy path, edge cases, validation, and exception handling.
3. Input: `Convert this plain-text test checklist into executable scenarios.`
   Output: A structured JUnit-oriented scenario plan with inferred gaps labeled separately.
4. Input: `Derive tests from this acceptance criteria section and preserve story traceability.`
   Output: A scenario list or test plan that names the source item and marks any extra inferred coverage explicitly.

## 6. Troubleshooting

1. Problem: The source artifact is ambiguous.
   Fix: Separate confirmed behavior from inferred coverage and call out the gap.
2. Problem: The narrative cases are repetitive.
   Fix: Collapse them into parameterized inputs when the assertion logic is shared.
3. Problem: The code path exposes too many internal branches.
   Fix: Group by externally visible behavior, not by every private implementation detail.
4. Problem: The requirement and the code disagree.
   Fix: Report the disagreement explicitly and avoid silently treating one source as authoritative unless the task says to.
