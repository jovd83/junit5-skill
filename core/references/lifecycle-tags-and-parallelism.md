# Lifecycle, Tags, And Parallelism

1. Default to per-test isolation unless the repo already relies on shared lifecycle setup.
2. Use tags to slice fast, slow, smoke, integration, or migration work when the repo already supports filtering.
3. Keep ordering as a last resort; fix hidden state dependencies instead of encoding them into the suite.
4. Treat parallel execution as an optimization, not a default assumption.
5. Before enabling parallel execution, inspect mutable statics, file-system reuse, ports, clock assumptions, and shared external dependencies.
