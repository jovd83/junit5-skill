---
name: junit5-documentation-root-cause
description: Use when Codex needs to analyze a failing JUnit 5 test run, identify the most likely root cause, and produce a developer-focused diagnosis with concrete next fixes.
---

# JUnit 5 Root Cause Analysis

## 1. Capture the Failure

1. Capture the failing class, method, stack trace, and environment details.
2. Reproduce the failure as narrowly as possible.
3. Separate symptom from suspected cause.

## 2. Classify the Failure

1. Check for assertion mismatch.
2. Check for fixture leakage or ordering issues.
3. Check for environment mismatch.
4. Check for timing, randomness, file system, locale, or time zone issues.
5. Check for a real production bug.

## 3. Report the Diagnosis

1. State the most likely root cause.
2. State the evidence supporting that conclusion.
3. State the smallest safe next fix.
4. State any remaining uncertainty explicitly.
