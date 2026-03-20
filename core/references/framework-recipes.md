# Framework Recipes

1. Plain Java: prefer constructor-based setup, direct collaborators, and no container bootstrapping.
2. Spring Boot: use the smallest test slice already accepted in the repo before reaching for full `@SpringBootTest`.
3. Quarkus: follow the repo's current test harness and avoid mixing Quarkus-managed and plain unit patterns in the same class.
4. Micronaut: keep the runtime-backed tests explicit and avoid booting the container for pure mapper or utility behavior.
5. Mockito: use mocks for collaborator control, not to mirror every line of the implementation.
6. Testcontainers: use them where infrastructure realism matters, not as the default for every repository or service test.
