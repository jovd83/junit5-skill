---
name: junit5-core
description: Use when Codex needs to create, run, debug, evaluate, refactor, or correct JUnit 5 tests across component, integration, slice, repository, service, smoke, or regression scenarios.
metadata:
  author: jovd83
  version: 1.0.0
  dispatcher-category: testing
  dispatcher-capabilities: unit-testing, junit5-core, junit5-implementation
  dispatcher-accepted-intents: implement_unit_tests, debug_unit_tests, review_unit_tests
  dispatcher-input-artifacts: repo_context, target_code, requirements, existing_junit_suite
  dispatcher-output-artifacts: junit_test, implementation_guidance, fix_plan
  dispatcher-stack-tags: junit5, implementation, jvm
  dispatcher-risk: high
  dispatcher-writes-files: true
---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# JUnit 5 Core

## 1. Preflight

1. Inspect the build file, Java version, source layout, and current JUnit dependencies.
2. Inspect existing test conventions before adding new classes or annotations.
3. Read [references/preflight.md](references/preflight.md) before major changes.
4. Read [references/test-types.md](references/test-types.md) before choosing the test shape.
5. Read [references/framework-recipes.md](references/framework-recipes.md) when the repo uses Spring Boot, Quarkus, Micronaut, Mockito, or Testcontainers.

## 2. Choose the Test Shape

1. Use component tests for pure logic with in-memory collaborators.
2. Use slice or repository tests when a framework boundary matters but the whole application does not.
3. Use integration tests when multiple layers must collaborate realistically.
4. Use service-isolated tests when the service boundary matters but downstream dependencies should stay controlled.
5. Use service-end-to-end tests only when the real dependency chain is required by the risk.
6. Use smoke tests for narrow health checks and regression tests for previously broken behavior.
7. Read [references/service-test-strategies.md](references/service-test-strategies.md) before adding slow or infrastructure-heavy service coverage.

## 3. Implement the Test

1. Prefer JUnit Jupiter annotations and assertions for new code.
2. Prefer `@ParameterizedTest` over duplicated cases when the input matrix is systematic.
3. Prefer soft assertions (`assertAll()`) to find and fix multiple errors in one test execution cycle.
4. Use `@Nested` when scenario hierarchy clarifies behavior.
5. Use test data builders, fakes, or fixtures to reduce setup noise.
6. Keep one behavioral reason per test.
7. Keep assertions semantic and stable.
8. Read [references/junit5-authoring.md](references/junit5-authoring.md) for detailed authoring patterns.
9. Read [references/lifecycle-tags-and-parallelism.md](references/lifecycle-tags-and-parallelism.md) before changing lifecycle, tags, ordering, or parallel execution.
10. Read [references/assertion-quality-and-smells.md](references/assertion-quality-and-smells.md) when the suite has weak, noisy, or brittle assertions.

## 4. Run and Debug

1. Run the narrowest relevant test first.
2. Reproduce failures before changing code.
3. Distinguish between bad test, bad fixture, bad environment, and real product bug.
4. Read [references/execution-and-debugging.md](references/execution-and-debugging.md) when triage is non-trivial.
5. Read [references/error-index.md](references/error-index.md) when the failure pattern is common and recognizable.

## 5. Correct Safely

1. Fix the smallest responsible layer first.
2. Keep failing evidence visible until the issue is understood.
3. Do not mute flaky behavior with sleeps or test ordering.
4. Rerun narrowly after the fix, then rerun the affected suite slice.

## 6. Examples

1. Input: `Write component tests for MoneyFormatter.`
   Output: Add a focused JUnit 5 class with semantic assertions and no framework bootstrapping.
2. Input: `Fix this flaky repository test.`
   Output: Remove shared state, stabilize fixture setup, and rerun the narrow test target first.
3. Input: `Add regression coverage for the null currency bug.`
   Output: Add a targeted regression test that reproduces the historical failure and verifies the corrected behavior.
4. Input: `Cover this Spring repository query with the lightest useful test.`
   Output: Add a repository-focused slice or integration test aligned to the existing Spring test harness instead of booting the whole application without a reason.
5. Input: `Turn these six input-output examples into JUnit 5 coverage.`
   Output: Use a parameterized test if the setup and assertion logic are shared.

## 7. Troubleshooting

1. Problem: Tests pass only in suite order.
   Fix: Remove shared mutable state and reset fixtures per test.
2. Problem: The test duplicates the same case with tiny input changes.
   Fix: Replace duplication with a parameterized test.
3. Problem: The service test is slow and brittle.
   Fix: Reclassify it as slice, repository, or service-isolated when the risk allows it.
4. Problem: The test suite becomes flaky only under parallel execution.
   Fix: Inspect shared fixtures, mutable statics, file-system reuse, and external ports before changing assertions.
5. Problem: The test uses a full framework boot path for pure logic.
   Fix: Collapse it into a component test and keep only the framework-backed cases where the boundary matters.