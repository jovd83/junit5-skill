# JUnit 5 Authoring

1. Use `org.junit.jupiter.api.Test` for ordinary tests.
2. Use `@BeforeEach` and `@AfterEach` for per-test fixture control.
3. Use `@ParameterizedTest` with explicit sources for structured input variation.
4. Use `@Nested` when setup or domain language becomes clearer through hierarchy.
5. Use `assertThrows` for exception behavior and assert the meaningful parts only.
6. Use `assertAll` when multiple related assertions belong to the same behavior.
7. Avoid giant inheritance trees for test reuse. Prefer helpers, builders, or extensions.
