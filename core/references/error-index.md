# Error Index

1. No tests discovered:
   Check naming conventions, source layout, and build-tool JUnit Platform activation.
2. Passes locally, fails in CI:
   Compare Java version, locale, time zone, file paths, environment variables, and execution flags.
3. Passes alone, fails in suite:
   Inspect shared mutable state, static caches, reused files, and database residue.
4. Flakes under parallel execution:
   Inspect concurrency safety before lowering assertion strength or adding sleeps.
5. Fails only on one developer machine:
   Compare JDK, build tool version, and local test data assumptions.
