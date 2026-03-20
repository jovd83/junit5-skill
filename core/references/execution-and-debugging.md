# Execution And Debugging

1. Run a single test class or method before running the full suite.
2. Capture the exact failure, stack trace, and triggering inputs.
3. Check for shared state, clocks, randomness, locale, time zone, file system residue, and fixed ports.
4. If the failure appears only in CI, compare Java version, environment variables, and build task configuration.
5. If the failure appears only in parallel runs, disable parallelism temporarily and inspect mutable shared fixtures.
