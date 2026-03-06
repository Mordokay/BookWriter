from pathlib import Path

BRIEFS_DIR = Path("story/chapter-briefs")
CHAPTERS_DIR = Path("story/chapters")
REVIEWS_DIR = Path("story/reviews")


def main() -> None:
    brief_files = sorted(BRIEFS_DIR.glob("ch*.md"))
    chapter_files = sorted(CHAPTERS_DIR.glob("ch*.md"))
    continuity_files = sorted(REVIEWS_DIR.glob("continuity-ch*.md"))
    literary_files = sorted(REVIEWS_DIR.glob("literary-ch*.md"))

    print("Chapter status\n")
    print(f"Briefs:              {len(brief_files)}")
    print(f"Drafted chapters:    {len(chapter_files)}")
    print(f"Continuity reviews:  {len(continuity_files)}")
    print(f"Literary reviews:    {len(literary_files)}")


if __name__ == "__main__":
    main()
