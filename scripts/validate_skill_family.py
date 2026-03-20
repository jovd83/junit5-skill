from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FRONTMATTER_NAME = re.compile(r"^name:\s*([a-z0-9-]{1,64})\s*$", re.MULTILINE)
FRONTMATTER_DESC = re.compile(r"^description:\s*(.+)$", re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = read_text(path)

    if not text.startswith("---\n"):
        return [f"{path}: missing YAML frontmatter start"]

    parts = text.split("---", 2)
    if len(parts) < 3:
        return [f"{path}: malformed YAML frontmatter"]

    frontmatter = parts[1]

    name_match = FRONTMATTER_NAME.search(frontmatter)
    if not name_match:
        errors.append(f"{path}: missing or invalid frontmatter name")

    desc_match = FRONTMATTER_DESC.search(frontmatter)
    if not desc_match:
        errors.append(f"{path}: missing frontmatter description")
    else:
        description = desc_match.group(1).strip()
        if not description.startswith("Use when"):
            errors.append(f"{path}: description must start with 'Use when'")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()

    root = args.root.resolve()
    skill_files = sorted(root.rglob("SKILL.md"))

    if not skill_files:
        print("No SKILL.md files found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_file in skill_files:
        errors.extend(validate_skill(skill_file))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_files)} skill files under {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
