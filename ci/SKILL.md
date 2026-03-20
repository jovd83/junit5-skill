---
name: junit5-ci
description: Use when Codex needs to run JUnit 5 tests through Maven, Gradle, or the Console Launcher, configure CI pipelines, manage tags and reports, or debug environment-specific execution issues.
metadata:
  author: jovd83
  version: "1.0.0"
---

# JUnit 5 CI

## 1. Inspect the Execution Path

1. Identify whether the repo uses Maven, Gradle, the Console Launcher, or mixed execution paths.
2. Confirm how tests are filtered, tagged, and reported.
3. Read [references/build-and-run.md](references/build-and-run.md) before changing pipeline behavior.
4. Read [references/tool-recipes.md](references/tool-recipes.md) when the repo supports more than one execution path.

## 2. Configure Safely

1. Use `useJUnitPlatform()` in Gradle-based execution.
2. Use current Surefire or Failsafe configuration already established by the repo when possible.
3. Keep tags, includes, excludes, and reporting explicit.
4. Use `junit-platform.properties` for shared execution parameters when the repo already follows that pattern.
5. Keep local and CI commands aligned unless the repo intentionally separates them.

## 3. Debug CI Failures

1. Compare local and CI Java versions.
2. Compare environment variables, locale, time zone, and file-system assumptions.
3. Compare build commands and active profiles.
4. Read [references/ci-failure-patterns.md](references/ci-failure-patterns.md) when failures reproduce only in automation.
5. Read [references/tagging-and-reporting.md](references/tagging-and-reporting.md) before changing tag filters or report outputs.

## 4. Examples

1. Input: `Make these JUnit 5 integration tests run in Maven CI only.`
   Output: Configure naming, tags, or Failsafe boundaries without breaking fast local feedback.
2. Input: `Gradle discovers no tests.`
   Output: Verify `useJUnitPlatform()`, naming conventions, and source-set wiring.
3. Input: `Split fast unit tests from slower integration coverage in Maven.`
   Output: Use tags, naming, or Surefire/Failsafe boundaries that fit the existing build model.

## 5. Troubleshooting

1. Problem: No tests are discovered.
   Fix: Check task configuration, naming conventions, and JUnit Platform enablement.
2. Problem: CI fails but local passes.
   Fix: Compare Java version, environment, and execution flags before changing test logic.
3. Problem: Reports exist locally but not in CI artifacts.
   Fix: Check report output paths, pipeline artifact collection, and the actual test task that runs in automation.
