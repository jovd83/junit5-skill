# Version Compatibility

1. This package targets JUnit 5 style work built on JUnit Jupiter and the JUnit Platform.
2. New guidance should stay compatible with common JUnit 5 usage unless the target repo clearly uses a newer incompatible pattern.
3. If official docs expose newer site versions, prefer concepts that remain valid for JUnit 5 users.
4. Do not introduce JUnit 4 APIs in new code except during migration.
5. Do not assume parallel execution, Console Launcher usage, or advanced reporting is already enabled.
