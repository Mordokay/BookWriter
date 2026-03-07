#!/usr/bin/env python3
"""Export the compiled manuscript to EPUB format."""

from pathlib import Path
import argparse
import re
import io
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = PROJECT_ROOT / "output" / "manuscript.md"
IMAGE_DIR = PROJECT_ROOT / "ImageAssets"
COVER_IMAGE = IMAGE_DIR / "Book_cover.png"

DEFAULT_TITLE = "The Forest Inside"
DEFAULT_AUTHOR = "Pedro Saldanha"

COVER_MAX_WIDTH = 800
COVER_MAX_HEIGHT = 1200
CHAPTER_IMAGE_MAX = 600

CSS = """\
body {
    font-family: "Iowan Old Style", Palatino, Georgia, serif;
    line-height: 1.6;
    margin: 1em;
    color: #1a1a1a;
}
h1 {
    font-size: 1.5em;
    text-align: center;
    margin-top: 2em;
    margin-bottom: 1.5em;
    font-weight: normal;
    letter-spacing: 0.05em;
}
p {
    text-indent: 1.5em;
    margin-top: 0.3em;
    margin-bottom: 0.3em;
    text-align: justify;
}
p:first-of-type {
    text-indent: 0;
}
em {
    font-style: italic;
}
.chapter-image {
    text-align: center;
    margin-bottom: 1.5em;
    page-break-after: avoid;
}
.chapter-image img {
    max-width: 80%;
    height: auto;
}
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Export manuscript to EPUB")
    parser.add_argument("--title", default=DEFAULT_TITLE)
    parser.add_argument("--author", default=DEFAULT_AUTHOR)
    parser.add_argument("--output", default=None)
    return parser.parse_args()


def resize_image(image_path, max_w, max_h):
    """Resize image to fit within max dimensions. Returns PNG bytes."""
    try:
        from PIL import Image

        img = Image.open(image_path)
        img.thumbnail((max_w, max_h), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="PNG", optimize=True)
        return buf.getvalue()
    except ImportError:
        print(f"  Warning: Pillow not installed, using original image size for {image_path.name}")
        return image_path.read_bytes()


def md_to_html(text):
    """Convert markdown text to HTML."""
    try:
        import markdown

        return markdown.markdown(text, extensions=["smarty"])
    except ImportError:
        # Fallback: basic conversion
        text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
        paragraphs = re.split(r"\n\n+", text.strip())
        return "\n".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())


def parse_manuscript(text):
    """Split manuscript into chapters. Returns list of dicts with number, title, body_md."""
    segments = re.split(r"\n---\n", text)

    chapters = []
    for segment in segments:
        segment = segment.strip()
        match = re.match(r"^#\s+Chapter\s+(\d+):\s+(.+)$", segment, re.MULTILINE)
        if match:
            number = int(match.group(1))
            title = match.group(2).strip()
            body = segment[match.end() :].strip()
            chapters.append({"number": number, "title": title, "body_md": body})

    return chapters


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_epub(title, author, chapters, output_path):
    from ebooklib import epub

    book = epub.EpubBook()
    book.set_identifier("forest-inside-001")
    book.set_title(title)
    book.set_language("en")
    book.add_author(author)

    # CSS
    css_item = epub.EpubItem(
        uid="style", file_name="style/default.css", media_type="text/css", content=CSS.encode("utf-8")
    )
    book.add_item(css_item)

    # Cover image
    if COVER_IMAGE.exists():
        cover_bytes = resize_image(COVER_IMAGE, COVER_MAX_WIDTH, COVER_MAX_HEIGHT)
        book.set_cover("images/cover.png", cover_bytes)
        print(f"  Cover image added ({len(cover_bytes) // 1024} KB)")
    else:
        print("  Warning: No cover image found, skipping")

    # Build chapters
    epub_chapters = []
    for ch in chapters:
        chapter_filename = f"ch{ch['number']:02d}.xhtml"
        epub_ch = epub.EpubHtml(title=f"Chapter {ch['number']}: {ch['title']}", file_name=chapter_filename)
        epub_ch.add_item(css_item)

        html_parts = []

        # Chapter image
        image_name = f"{ch['title']}_final.png"
        image_path = IMAGE_DIR / image_name
        if image_path.exists():
            img_bytes = resize_image(image_path, CHAPTER_IMAGE_MAX, CHAPTER_IMAGE_MAX)
            img_item = epub.EpubImage()
            img_filename = f"images/ch{ch['number']:02d}.png"
            img_item.file_name = img_filename
            img_item.media_type = "image/png"
            img_item.content = img_bytes
            book.add_item(img_item)
            html_parts.append(f'<div class="chapter-image"><img src="{img_filename}" alt="{ch["title"]}"/></div>')
            print(f"  Ch {ch['number']:2d} image added ({len(img_bytes) // 1024} KB)")
        elif IMAGE_DIR.exists():
            print(f"  Ch {ch['number']:2d} image not found: {image_name}")

        # Chapter heading and prose
        html_parts.append(f"<h1>Chapter {ch['number']}: {ch['title']}</h1>")
        html_parts.append(md_to_html(ch["body_md"]))

        epub_ch.content = "\n".join(html_parts).encode("utf-8")
        book.add_item(epub_ch)
        epub_chapters.append(epub_ch)

    # TOC and spine
    book.toc = epub_chapters
    book.spine = ["nav"] + epub_chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Write
    output_path.parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(str(output_path), book)


def main():
    args = parse_args()

    if not MANUSCRIPT.exists():
        print(f"Error: Manuscript not found at {MANUSCRIPT}")
        print("Run 'python3 scripts/compile_manuscript.py' first.")
        sys.exit(1)

    if not IMAGE_DIR.exists():
        print(f"Warning: ImageAssets directory not found at {IMAGE_DIR}")
        print("Generating text-only EPUB.")

    text = MANUSCRIPT.read_text(encoding="utf-8")
    chapters = parse_manuscript(text)

    if not chapters:
        print("Error: No chapters found in manuscript.")
        sys.exit(1)

    print(f"Found {len(chapters)} chapters")

    output_path = Path(args.output) if args.output else PROJECT_ROOT / "output" / f"{slugify(args.title)}.epub"

    print(f"Building EPUB: {args.title} by {args.author}")
    build_epub(args.title, args.author, chapters, output_path)

    size_kb = output_path.stat().st_size // 1024
    print(f"\nExported to {output_path} ({size_kb} KB)")


if __name__ == "__main__":
    main()
