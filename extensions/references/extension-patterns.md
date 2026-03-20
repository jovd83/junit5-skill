# Extension Patterns

1. Use callbacks for setup, teardown, interception, or result processing that genuinely repeats.
2. Use parameter resolvers for dependency injection that remains obvious at the call site.
3. Use meta-annotations only when they improve clarity and remove repeated boilerplate.
4. Avoid storing mutable global state unless the lifecycle requires it and cleanup is explicit.
