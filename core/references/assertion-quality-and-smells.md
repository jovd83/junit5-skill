# Assertion Quality And Smells

1. Assert behavior, not implementation trivia.
2. Avoid assertions that merely restate mocked setup.
3. Prefer one strong semantic assertion over many weak formatting checks.
4. Avoid brittle full-string exception comparisons when type and key message fragments are enough.
5. Add regression assertions for historically broken behavior, not for every private branch.
