---
name: junit5-migration
description: Use when Codex needs to migrate tests from JUnit 3 or JUnit 4 to JUnit 5, replace runners and rules, reduce Vintage usage, and preserve behavioral compatibility during modernization.
metadata:
  author: jovd83
  version: "1.0.0"
  dispatcher-category: testing
  dispatcher-capabilities: framework-migration, junit5-migration
  dispatcher-accepted-intents: migrate_to_junit5
  dispatcher-input-artifacts: legacy_test_suite, repo_context, migration_scope
  dispatcher-output-artifacts: migration_plan, migrated_tests, compatibility_notes
  dispatcher-stack-tags: junit5, migration, jvm
  dispatcher-risk: high
  dispatcher-writes-files: true
---

# JUnit 5 Migration

## 1. Inspect the Current State

1. Identify JUnit 3, JUnit 4, Jupiter, and Vintage usage.
2. Identify runners, rules, categories, and old assertions.
3. Read [references/migration-map.md](references/migration-map.md) before rewriting test infrastructure.
4. Read [references/runners-rules-and-categories.md](references/runners-rules-and-categories.md) when legacy JUnit 4 infrastructure is non-trivial.

## 2. Migrate Incrementally

1. Replace JUnit 4 imports with Jupiter imports in the smallest safe slice.
2. Replace runners and rules with Jupiter extensions, lifecycle callbacks, or tags.
3. Preserve observable behavior before cleaning style.
4. Remove Vintage only when the migrated slice is stable.
5. Keep migration and cleanup separate when both are large.

## 3. Validate the Migration

1. Run the narrow slice first.
2. Rerun the affected module or suite.
3. Keep compatibility evidence visible if the migration changes behavior unexpectedly.
4. Read [references/migration-playbook.md](references/migration-playbook.md) when the suite is large or mixed-version.

## 4. Troubleshooting

1. Problem: The repo still depends on JUnit 4 runners.
   Fix: Replace them with Jupiter extensions or platform-supported alternatives one slice at a time.
2. Problem: The suite still needs Vintage.
   Fix: Limit Vintage to the remaining legacy area and keep the migration boundary explicit.
3. Problem: The migration changed the lifecycle behavior unexpectedly.
   Fix: Compare setup and teardown scope, shared fixtures, and ordering assumptions before changing assertions.
