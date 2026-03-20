# Lifecycle And State

1. Keep extension state as small and local as possible.
2. Prefer per-test behavior over global mutable state.
3. When multiple callbacks collaborate, document and test the ordering assumptions.
4. Clean up state explicitly when the extension allocates files, ports, or other resources.
