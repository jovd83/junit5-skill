# Migration Playbook

1. Inventory the legacy area first.
2. Migrate one package, module, or suite slice at a time.
3. Keep behavior stable before cleaning naming and style.
4. Remove Vintage only after the migrated slice proves stable.
5. Leave clear boundaries around the remaining legacy area so new code does not drift back into JUnit 4.
