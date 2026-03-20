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
- Keep assertions semantic and behavior-focused.
- Use `@Nested`, tags, lifecycle control, and extensions deliberately, not as decoration.
- Keep heavy framework behavior and infrastructure logic out of plain unit tests.
- Preserve failing evidence before changing assertions or production code.

## Read By Need

- Read [references/capability-map.md](references/capability-map.md) when choosing scope.
- Read [references/family-conventions.md](references/family-conventions.md) before adding new package content.
- Read [references/version-compatibility.md](references/version-compatibility.md) when build or dependency versions are unclear.
- Read [references/release-checklist.md](references/release-checklist.md) before publishing or cutting a release.

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
