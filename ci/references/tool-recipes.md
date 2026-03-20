# Tool Recipes

1. Maven: use the existing Surefire and Failsafe split if the repo already has one.
2. Gradle: keep test task configuration in the build script or convention plugin rather than spreading it across ad hoc shell commands.
3. Console Launcher: use it for focused discovery or lightweight environments, not as a hidden replacement for the main build path.
4. Prefer one canonical local command per suite type so failure reproduction is straightforward.
