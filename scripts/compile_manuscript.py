from pathlib import Path

OUTPUT_FILE = Path("output/manuscript.md")
CHAPTERS_DIR = Path("story/chapters")


def natural_key(path: Path):
    return path.name


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    chapter_files = sorted(CHAPTERS_DIR.glob("ch*.md"), key=natural_key)
    parts = []
    parts.append("# Manuscript\n")
    if not chapter_files:
        parts.append("_No chapters found._\n")
    else:
        for chapter_file in chapter_files:
            text = chapter_file.read_text(encoding="utf-8").strip()
            parts.append(text)
            parts.append("\n\n---\n\n")
    OUTPUT_FILE.write_text("".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Compiled manuscript to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
