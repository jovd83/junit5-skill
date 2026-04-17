---
name: junit5-extensions
description: Use when Codex needs to create, review, or debug JUnit 5 extensions, custom annotations, lifecycle callbacks, parameter resolvers, or reusable execution hooks.
metadata:
  author: jovd83
  version: 1.0.0
  dispatcher-category: testing
  dispatcher-capabilities: extensions, junit5-extensions
  dispatcher-accepted-intents: implement_junit_extensions
  dispatcher-input-artifacts: repo_context, extension_requirements, target_suite
  dispatcher-output-artifacts: extension_design, extension_code, usage_guidance
  dispatcher-stack-tags: junit5, extensions, jvm
  dispatcher-risk: medium
  dispatcher-writes-files: true
---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# JUnit 5 Extensions

## 1. Confirm That an Extension Is Warranted

1. Use helpers, builders, or local fixtures first.
2. Create an extension only when the behavior is cross-cutting and repeated.
3. Read [references/extension-patterns.md](references/extension-patterns.md) before adding a new extension.
4. Read [references/lifecycle-and-state.md](references/lifecycle-and-state.md) before storing state or coordinating multiple callbacks.

## 2. Implement Deliberately

1. Choose the smallest relevant callback or resolver interface.
2. Keep state explicit and scoped safely.
3. Keep extension behavior testable and unsurprising.
4. Prefer explicit registration when discoverability matters.
5. Keep meta-annotations small and intention-revealing.

## 3. Validate

1. Add focused tests for the extension itself.
2. Verify lifecycle ordering and failure behavior.
3. Avoid hidden global behavior that changes unrelated tests.
4. Read [references/extension-testing.md](references/extension-testing.md) when the extension has multiple callbacks or parameter rules.

## 4. Troubleshooting

1. Problem: The extension hides too much setup.
   Fix: Move local test setup back into the test class and keep only the true cross-cutting concern in the extension.
2. Problem: Parameter resolution is ambiguous.
   Fix: Narrow the supported parameter types or add clearer registration boundaries.
3. Problem: The extension works only when tests run in a certain order.
   Fix: Remove hidden shared state and verify callback scope explicitly.