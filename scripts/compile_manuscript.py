#!/usr/bin/env python3
"""Compile all chapter prose into a single manuscript file, stripping metadata."""

import re
from pathlib import Path

OUTPUT_FILE = Path("output/manuscript.md")
CHAPTERS_DIR = Path("story/chapters")


def natural_key(path: Path):
    return path.name


def strip_metadata(text: str) -> str:
    """Remove Continuity Notes, Revision Log, and Chapter Intent sections."""
    # Find the first --- that precedes a ## heading (metadata boundary)
    # Pattern: a line that is just "---" followed by blank line and ## heading
    match = re.search(r'\n---\n\n## (Continuity Notes|Revision Log)', text)
    if match:
        return text[:match.start()].rstrip()
    # Fallback: try just ## Continuity Notes without ---
    match = re.search(r'\n## Continuity Notes', text)
    if match:
        return text[:match.start()].rstrip()
    return text.rstrip()


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    chapter_files = sorted(CHAPTERS_DIR.glob("ch*.md"), key=natural_key)
    parts = []

    if not chapter_files:
        parts.append("_No chapters found._\n")
    else:
        for chapter_file in chapter_files:
            text = chapter_file.read_text(encoding="utf-8").strip()
            prose = strip_metadata(text)
            parts.append(prose)
            parts.append("\n\n---\n\n")

    OUTPUT_FILE.write_text("".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Compiled {len(chapter_files)} chapters to {OUTPUT_FILE}")

    # Quick word count
    full_text = OUTPUT_FILE.read_text(encoding="utf-8")
    words = len(full_text.split())
    print(f"Total words: {words:,}")


if __name__ == "__main__":
    main()
