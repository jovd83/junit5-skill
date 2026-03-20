# CI Failure Patterns

1. Discovery mismatch: wrong naming, wrong source set, or missing JUnit Platform activation.
2. Java mismatch: CI runs a different JDK or bytecode target.
3. Environment mismatch: missing secrets, ports, files, locale, or time zone.
4. Shared-state flakiness: parallel execution or suite order exposes state leakage.
5. Overly broad fixes: avoid muting failures with retries before the root cause is understood.
