---
name: junit5-reporting-stakeholder
description: Use when Codex needs to summarize JUnit 5 test execution results for non-technical stakeholders in clear business-oriented language instead of raw runner output.
metadata:
  author: jovd83
  version: 1.0.0
  dispatcher-category: testing
  dispatcher-capabilities: stakeholder-reporting, junit5-stakeholder-reporting
  dispatcher-accepted-intents: summarize_junit_results
  dispatcher-input-artifacts: execution_results, tested_scope, release_context
  dispatcher-output-artifacts: stakeholder_summary, release_health_report
  dispatcher-stack-tags: junit5, reporting, stakeholder
  dispatcher-risk: low
  dispatcher-writes-files: false
---

# JUnit 5 Stakeholder Reporting


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## 1. Collect the Outcome

1. Identify what ran, what passed, what failed, and what was skipped.
2. Identify whether the failures block release confidence or are isolated.

## 2. Translate into Stakeholder Language

1. Explain business impact, not stack traces.
2. Group failures by user-facing risk.
3. Call out confidence level and next action clearly.

## 3. Troubleshooting

1. Problem: The raw output is noisy.
   Fix: Collapse it into impacted capability, confidence, and next action.
