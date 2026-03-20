# Build And Run

1. Maven: use Surefire for standard tests and Failsafe when the repo separates integration execution.
2. Gradle: ensure the `Test` task uses JUnit Platform.
3. Console Launcher: use it for focused local discovery or environments without build integration.
4. Keep narrow-run commands available for one class or one method whenever the tool supports it.
5. Keep reports enabled only to the degree that the repo or pipeline already expects.
