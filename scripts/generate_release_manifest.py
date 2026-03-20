from __future__ import annotations

import argparse
import re
from pathlib import Path


NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
DISPLAY_RE = re.compile(r'^\s*display_name:\s*"(.+)"\s*$', re.MULTILINE)
SHORT_RE = re.compile(r'^\s*short_description:\s*"(.+)"\s*$', re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def humanize_name(name: str) -> str:
    parts = [part for part in name.split("-") if part]
    words: list[str] = []

    for part in parts:
        if part == "junit5":
            words.extend(["JUnit", "5"])
        elif part == "ci":
            words.append("CI")
        elif part == "vscode":
            words.extend(["VS", "Code"])
        elif part == "intellij":
            words.append("IntelliJ")
        elif part == "root":
            words.append("Root")
        else:
            words.append(part.capitalize())

    return " ".join(words)


def parse_skill(path: Path, root: Path) -> tuple[str, str, str]:
    text = read_text(path)
    name = NAME_RE.search(text).group(1).strip()  # type: ignore[union-attr]
    description = DESC_RE.search(text).group(1).strip()  # type: ignore[union-attr]
    relative_dir = path.parent.relative_to(root)
    display_name = humanize_name(name)

    if relative_dir == Path("."):
        openai_yaml = root / "agents" / "openai.yaml"
        if openai_yaml.exists():
            openai_text = read_text(openai_yaml)
            display_match = DISPLAY_RE.search(openai_text)
            short_match = SHORT_RE.search(openai_text)
            if display_match:
                display_name = display_match.group(1)
            if short_match:
                description = short_match.group(1)

    absolute_dir = str(path.parent.resolve())
    return name, display_name, absolute_dir, description


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.root.resolve()
    skills = sorted(root.rglob("SKILL.md"))

    rows = [parse_skill(skill, root) for skill in skills]

    lines = [
        "# Release Manifest",
        "",
        "## Summary",
        "",
        f"- Root: `{root}`",
        f"- Skills: {len(rows)}",
        "",
        "## Skills",
        "",
        "| Skill Name | Display Name | Path | Short Description |",
        "|---|---|---|---|",
    ]

    for name, display_name, path, description in rows:
        lines.append(f"| `{name}` | {display_name} | `{path}` | {description} |")

    output = args.output.resolve()
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote release manifest to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
