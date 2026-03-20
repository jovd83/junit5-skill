# Migration Map

1. `org.junit.Test` becomes `org.junit.jupiter.api.Test`.
2. `@Before` and `@After` become `@BeforeEach` and `@AfterEach`.
3. `@BeforeClass` and `@AfterClass` become `@BeforeAll` and `@AfterAll`.
4. Categories usually map to tags.
5. Rules and runners usually map to extensions or explicit setup code.
6. Keep migration slices small so failures stay attributable.
