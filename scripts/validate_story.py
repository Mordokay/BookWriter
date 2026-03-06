from pathlib import Path

REQUIRED_FILES = [
    "story/brief.md",
    "story/goals.md",
    "story/theme.md",
    "story/world.md",
    "story/characters.md",
    "story/plot.md",
    "story/timeline.md",
    "story/chapter-outline.md",
    "story/style-guide.md",
    "story/constraints.md",
    "story/user-feedback.md",
    "story/manuscript-status.md",
]

PENDING_MARKER = "Pending."


def check_file(path_str: str) -> tuple[bool, str]:
    path = Path(path_str)
    if not path.exists():
        return False, "missing"
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return False, "empty"
    if text == f"# {path.stem.replace('-', ' ').title()}\n\n{PENDING_MARKER}" or text.endswith(PENDING_MARKER):
        return False, "pending"
    return True, "ok"


def main() -> None:
    print("Story validation\n")
    ok_count = 0
    for file_path in REQUIRED_FILES:
        ok, status = check_file(file_path)
        symbol = "✅" if ok else "⚠️"
        print(f"{symbol}  {file_path}: {status}")
        if ok:
            ok_count += 1
    print(f"\nCompleted or non-pending files: {ok_count}/{len(REQUIRED_FILES)}")


if __name__ == "__main__":
    main()
