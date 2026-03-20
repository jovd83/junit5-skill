# Test Types

- `component`: Pure logic, in-memory collaborators, no container or remote boundary.
- `slice`: A focused framework-backed slice such as web, persistence, or mapper behavior.
- `repository`: Persistence behavior with realistic schema and transaction expectations.
- `integration`: Multiple layers collaborating within one application or module boundary.
- `service-isolated`: A service boundary tested with controlled doubles or local infrastructure.
- `service-end-to-end`: Real dependency chain across service boundaries.
- `smoke`: Fast confidence checks for critical paths.
- `regression`: Reproduction and protection for previously broken behavior.
- `negative`: Validation of errors, guard rails, and exception paths.
- `migration-safety`: Tests added or adapted to preserve behavior during framework migration.
