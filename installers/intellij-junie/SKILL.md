---
name: junit5-installer-intellij-junie
description: Use when Codex needs to help configure IntelliJ IDEA for JUnit 5 development, execution, debugging, and Junie-style workflows in a JVM project.
metadata:
  author: jovd83
  version: 1.0.0
  dispatcher-category: testing
  dispatcher-capabilities: editor-setup, junit5-editor-setup
  dispatcher-accepted-intents: setup_junit_editor
  dispatcher-input-artifacts: editor_choice, repo_context, local_environment
  dispatcher-output-artifacts: editor_setup_steps, configuration_guidance
  dispatcher-stack-tags: junit5, setup, editor
  dispatcher-risk: low
  dispatcher-writes-files: false
---

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

# JUnit 5 IntelliJ Setup

## 1. Confirm the Project Shape

1. Confirm the repo imports cleanly as Maven or Gradle.
2. Confirm the JDK version expected by the build.
3. Confirm JUnit 5 dependencies exist in the test scope.

## 2. Configure the IDE

1. Import the project from the build file instead of creating a detached IDE project.
2. Set the project SDK and language level to match the build.
3. Confirm IntelliJ uses the build tool or JUnit 5 runner path expected by the repo.

## 3. Validate

1. Run one focused test class.
2. Debug one test method.
3. Confirm tags and environment-sensitive tests behave as expected.