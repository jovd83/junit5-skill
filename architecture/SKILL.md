---
name: junit5-architecture
description: Use when Codex needs to shape or refactor JUnit 5 suite architecture, test package structure, naming, fixture ownership, reuse patterns, or boundaries between component, integration, and service tests.
---

# JUnit 5 Architecture

## 1. Inspect Before Restructuring

1. Inspect current package layout, test naming, build filters, and fixture reuse.
2. Inspect whether the repo already separates fast and slow tests by tag, source set, or naming convention.
3. Read [references/suite-shape.md](references/suite-shape.md) before moving files or changing naming conventions.

## 2. Choose Stable Boundaries

1. Separate component, slice, integration, and service tests intentionally.
2. Keep reusable setup close to its owning layer.
3. Prefer builders, helpers, and local fixtures before introducing global abstractions.
4. Use extensions only when reuse is real and cross-cutting.

## 3. Refactor for Clarity

1. Group tests by behavior or domain concept, not by incidental helper reuse.
2. Keep naming consistent with build-tool discovery.
3. Avoid base-class pyramids and magical test inheritance.

## 4. Troubleshooting

1. Problem: Shared fixtures leak across unrelated suites.
   Fix: Push fixtures down to the owning package or convert them to explicit helpers.
2. Problem: Test names and package layout hide runtime cost.
   Fix: Separate slow integration or service suites clearly by tag or naming.
