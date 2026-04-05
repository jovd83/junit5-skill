---
name: junit5-skill
description: Use when Codex needs to create, run, evaluate, debug, correct, modernize, document, or route JUnit 5 tests and related workflows across component, integration, slice, repository, service, regression, smoke, and migration scenarios.
metadata:
  author: jovd83
  version: "1.0"
---

# JUnit 5 Skill Family

Use this root skill as the package entrypoint for general JUnit 5 requests. Route broad work to the smallest useful subskill. Keep this file light. Read only the subskill and reference files that materially help with the current task.

## Responsibilities

- Route broad or ambiguous JUnit 5 requests.
- Apply the shared standards of this package.
- Keep package boundaries clear across authoring, migration, CI, analysis, extensions, architecture, and documentation workflows.

## Boundaries

- Do not assume every JVM repo uses Spring, Testcontainers, Mockito, or parallel execution.
- Do not add JUnit 4 APIs in new code unless the task is explicitly about migration.
- Do not silently convert unstable integration tests into mocked unit tests just to make them pass.
- Do not treat JUnit 6 branding as permission to generate non-JUnit-5-compatible patterns for a repo that still targets JUnit 5.

## Routing Map

| Need | Use |
|---|---|
| Generic JUnit 5 request or unclear starting point | [core/SKILL.md](core/SKILL.md) |
| Writing, fixing, running, or correcting JUnit 5 tests | [core/SKILL.md](core/SKILL.md) |
| Deriving scenarios from requirements, code, or test case definitions | [analysis/SKILL.md](analysis/SKILL.md) |
| Suite structure, fixture ownership, or naming conventions | [architecture/SKILL.md](architecture/SKILL.md) |
| Maven, Gradle, Console Launcher, CI, or reporting setup | [ci/SKILL.md](ci/SKILL.md) |
| JUnit 4 to JUnit 5 migration | [migration/SKILL.md](migration/SKILL.md) |
| Custom extensions, callbacks, or parameter resolvers | [extensions/SKILL.md](extensions/SKILL.md) |
| Human-readable automation documentation | [documentation/tests/SKILL.md](documentation/tests/SKILL.md) |
| Root-cause analysis for failing tests | [documentation/root_cause/SKILL.md](documentation/root_cause/SKILL.md) |
| Non-technical summaries of test outcomes | [reporting/stakeholder/SKILL.md](reporting/stakeholder/SKILL.md) |
| IDE-specific local setup help | [installers/intellij-junie/SKILL.md](installers/intellij-junie/SKILL.md) or [installers/vscode-codex/SKILL.md](installers/vscode-codex/SKILL.md) |

## Operating Workflow

1. Inspect the repo before prescribing structure. Check build files, Java version, dependencies, test layout, and current JUnit usage.
2. Run `scripts/detect-junit-test-context.ps1` when repo structure or toolchain is unclear.
3. Classify the work as component, integration, slice, repository, service-isolated, service-end-to-end, smoke, regression, migration, or extension work.
4. Route to the smallest subskill that can complete the task well.
5. Run the narrowest relevant test first.
6. Preserve traceability to the requirement, code path, or test-case definition when the work begins from source artifacts.
7. Keep JUnit 5 compatibility explicit unless the repo has already moved beyond it.

## Shared Standards

- Prefer JUnit Jupiter APIs for new test code.
- Prefer deterministic tests over order-dependent or environment-dependent tests.
- Use the lightest test type that still validates the real risk.
- Prefer parameterized tests over copy-pasted examples when inputs vary systematically.
- Prefer soft assertions (`assertAll()`) to report multiple failures in one run, ensuring faster correction cycles.
- Keep assertions semantic and behavior-focused.
- Use `@Nested`, tags, lifecycle control, and extensions deliberately, not as decoration.
- Keep heavy framework behavior and infrastructure logic out of plain unit tests.
- Preserve failing evidence before changing assertions or production code.

## Read By Need

- Read [references/capability-map.md](references/capability-map.md) when choosing scope.
- Read [references/family-conventions.md](references/family-conventions.md) before adding new package content.
- Read [references/version-compatibility.md](references/version-compatibility.md) when build or dependency versions are unclear.
- Read [references/release-checklist.md](references/release-checklist.md) before publishing or cutting a release.

## Gotchas

- **Static Lifecycle**: `@BeforeAll` and `@AfterAll` must be `static` by default. Use `@TestInstance(Lifecycle.PER_CLASS)` only when non-static lifecycle is explicitly required.
- **Assertion Order**: Always use `assertEquals(expected, actual)`. Swapping them makes failure reports misleading (e.g., "Expected: 5, Actual: 10" when the actual value was 5).
- **Assertion Masking**: Sequential assertions stop at the first failure. Prefer **soft assertions** (`assertAll()`) to execute and report on multiple independent assertions within a single test, allowing many errors to be fixed at once.
- **Visibility**: JUnit 5 test classes and methods should be package-private (no `public` modifier) unless they must be accessed from other packages.
- **Import Conflicts**: Ensure you import from `org.junit.jupiter.api` rather than the old `org.junit` (JUnit 4) package. Mixing them leads to tests that "pass" because they never ran.
- **Mocking Leakage**: When mocking static methods or constructors (e.g., with Mockito), always use a try-with-resources block or an `@AfterEach` cleanup to prevent state leakage.
- **Tag Selection**: Using `@Tag` without corresponding build-tool configuration (Maven/Gradle) means the tests will run even when you think you've excluded them.

## Official References

- JUnit overview: https://docs.junit.org/5.14.3/overview.html
- JUnit 5 user guide landing page: https://junit.org/junit5/

## Package Shape

- `core/` is the default path for daily JUnit 5 work.
- `analysis/` derives executable scenarios from requirements, code, or narrative test definitions.
- `architecture/` governs suite shape, ownership, and reuse.
- `ci/` covers execution, build tools, and pipeline behavior.
- `migration/` handles JUnit 4 to JUnit 5 modernization.
- `extensions/` handles reusable callbacks, parameter resolution, and custom annotations.
- `documentation/`, `reporting/`, and `installers/` are optional extensions, not prerequisites for routine test authoring.
