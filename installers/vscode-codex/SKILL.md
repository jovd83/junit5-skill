---
name: junit5-installer-vscode-codex
description: Use when Codex needs to help configure Visual Studio Code for JUnit 5 development, execution, debugging, and Codex-driven workflows in a JVM project.
---

# JUnit 5 VS Code Setup

## 1. Confirm the Project Shape

1. Confirm the repo uses Maven or Gradle.
2. Confirm the expected JDK version.
3. Confirm test dependencies resolve successfully.

## 2. Configure the Workspace

1. Open the repo root, not a detached subfolder.
2. Ensure Java tooling and test execution extensions are active.
3. Let the build tool remain the source of truth for classpath and runner behavior.

## 3. Validate

1. Run one focused test class.
2. Debug one test method.
3. Confirm terminal execution matches IDE execution.
