# Service Test Strategies

1. `service-isolated`: keep downstream behavior controlled with stubs, fakes, or local infrastructure when the service boundary is the focus.
2. `service-end-to-end`: use real dependencies only when the production risk depends on the full interaction chain.
3. Use narrow smoke coverage for critical path confidence and keep broader regression coverage separated when runtime cost is high.
4. Keep network, database, and queue assumptions explicit in fixtures or test setup.
5. Avoid calling external internet services from ordinary regression suites.
