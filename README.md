# JUnit 5 Skill Family

[![Validate Skills](https://github.com/jovd83/junit5-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/jovd83/junit5-skill/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-1.0-blue)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

Battle-tested JUnit 5 skill guides for creating, running, evaluating, correcting, migrating, documenting, and operationalizing JVM tests. This repository packages a full Agent Skills family for component tests, integration tests, repository tests, slice tests, service tests, regression coverage, migration work, CI flows, and extension authoring.

## What are Agent Skills?

[Agent Skills](https://github.com/agentskills/agentskills) are an open format for giving AI agents portable capabilities and procedural expertise. A skill is a folder containing instructions plus optional scripts, references, and assets that agents can discover and use.

## Installation

Install the full family and let the agent route to the right subskill:

```bash
npx skills add jovd83/junit5-skill
```

Install only selected packs if you want a smaller setup:

```bash
npx skills add jovd83/junit5-skill/core
npx skills add jovd83/junit5-skill/analysis
npx skills add jovd83/junit5-skill/migration
npx skills add jovd83/junit5-skill/ci
npx skills add jovd83/junit5-skill/extensions
```

Manual alternative:

```bash
git clone https://github.com/jovd83/junit5-skill.git
```

Then place the repository where your agent looks for local skills, such as:

- `~/.agents/skills/`
- `~/.cursor/skills/`
- other IDE-specific local skill directories

## Skills Overview

| Skill Pack | Scope | What It Covers |
|---|---|---|
| `SKILL.md` | Root routing | Entry point, package standards, subskill routing |
| `core/` | Daily JUnit 5 work | Create, run, debug, evaluate, refactor, and correct tests |
| `analysis/` | Input analysis | Derive tests from requirements, code, TDD, BDD, and plain-text definitions |
| `architecture/` | Suite design | Boundaries, naming, fixture ownership, and reuse |
| `ci/` | Execution and delivery | Maven, Gradle, Console Launcher, CI, and environment triage |
| `migration/` | Modernization | JUnit 3 and JUnit 4 to JUnit 5 migration |
| `extensions/` | Reuse mechanisms | Custom extensions, callbacks, resolvers, and annotations |
| `documentation/` | Explain and diagnose | Test documentation and root-cause analysis |
| `reporting/` | Stakeholder communication | Human-readable summaries of test outcomes |
| `installers/` | Local setup | IntelliJ + Junie and VS Code + Codex workflows |

## Supported Test Types

- component tests
- unit tests
- slice tests
- repository tests
- integration tests
- service tests in isolation
- service tests with real dependencies
- smoke tests
- regression tests
- negative-path tests
- migration-safety tests

## Supported Workflows

- create tests
- run tests
- evaluate failures
- correct broken tests
- correct code under test when the test reveals a real bug
- derive scenarios from requirements, code, or narrative test definitions
- modernize JUnit 4 suites
- document test intent
- diagnose root cause
- summarize execution outcomes
- configure execution in IDEs and CI

## Repository Layout

```text
SKILL.md
agents/
analysis/
architecture/
assets/
ci/
core/
documentation/
extensions/
installers/
migration/
references/
reporting/
scripts/
```

## Validation

Validate the family metadata and file layout:

```powershell
python .\scripts\validate_skill_family.py --root .
```

Generate a release manifest for packaging review:

```powershell
python .\scripts\generate_release_manifest.py --root . --output .\release-manifest.md
```

Inspect the local repo context with the bundled PowerShell helper:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\detect-junit-test-context.ps1 -Root .
```

## Design Principles

- Keep the package explicitly aligned to JUnit 5 and JUnit Jupiter workflows.
- Use progressive disclosure: short `SKILL.md` files, deeper guidance in `references/`.
- Prefer the lightest test type that still validates the real risk.
- Preserve traceability when tests come from requirements, source code, or narrative definitions.
- Avoid JUnit 4 APIs in new code except during migration.

## License

MIT. See [LICENSE](LICENSE).
