---
name: junit5-installer-intellij-junie
description: Use when Codex needs to help configure IntelliJ IDEA for JUnit 5 development, execution, debugging, and Junie-style workflows in a JVM project.
---

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
