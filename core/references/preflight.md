# Preflight

1. Inspect `pom.xml`, `build.gradle`, or `build.gradle.kts`.
2. Confirm the Java version and whether the repo compiles with Java 8, 11, 17, or newer.
3. Confirm JUnit Jupiter dependencies and whether JUnit 4 or Vintage is still present.
4. Check for Spring Boot, Quarkus, Micronaut, Mockito, Testcontainers, WireMock, or custom test harnesses.
5. Check existing package naming and suffix conventions such as `*Test`, `*IT`, `*IntegrationTest`, or `*Tests`.
6. Check whether `junit-platform.properties` already controls tags, lifecycle, or parallel execution.
7. Inspect one or two representative test classes before introducing a new pattern.
