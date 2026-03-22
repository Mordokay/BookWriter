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
HEADER_DIR = IMAGE_DIR / "chapter_headers"
COVER_IMAGE = IMAGE_DIR / "Book_Cover_Light.png"

DEFAULT_TITLE = "The City Beneath the Root"
DEFAULT_AUTHOR = "Claude Code & Pedro Saldanha"

COVER_MAX_WIDTH = 800
COVER_MAX_HEIGHT = 1200
HEADER_MAX_WIDTH = 1200
HEADER_MAX_HEIGHT = 250

CSS = """\
@charset "UTF-8";

body {
    font-family: "Iowan Old Style", Palatino, Georgia, serif;
    line-height: 1.7;
    margin: 1em;
    color: #000;
    background-color: transparent;
}


h1.chapter-title {
    font-size: 1.4em;
    text-align: center;
    margin-top: 1em;
    margin-bottom: 0.3em;
    font-weight: normal;
    letter-spacing: 0.06em;
    color: #2a2a2a;
}

p.chapter-number {
    text-align: center;
    font-size: 0.85em;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #666;
    margin-bottom: 0.2em;
    margin-top: 1.5em;
}

.chapter-separator {
    text-align: center;
    margin-top: 0.5em;
    margin-bottom: 2em;
    color: #999;
    font-size: 0.8em;
    letter-spacing: 0.3em;
}

p {
    text-indent: 1.5em;
    margin-top: 0.3em;
    margin-bottom: 0.3em;
    text-align: justify;
}

/* First paragraph after heading or image has no indent */
h1 + p,
.chapter-separator + p,
.chapter-header + p.chapter-number + h1 + .chapter-separator + p {
    text-indent: 0;
}

em {
    font-style: italic;
}

hr {
    border: none;
    text-align: center;
    margin: 1.5em 0;
}

hr::after {
    content: "\\2022  \\2022  \\2022";
    color: #aaa;
    font-size: 0.7em;
    letter-spacing: 0.5em;
}

.chapter-header {
    text-align: center;
    margin-bottom: 0.5em;
    page-break-after: avoid;
}

.chapter-header img {
    max-width: 100%;
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
        # Convert RGBA to RGB for smaller file size if no transparency needed
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, (12, 18, 22))  # dark bg matching headers
            bg.paste(img, mask=img.split()[3])
            img = bg
        img.save(buf, format="PNG", optimize=True)
        return buf.getvalue()
    except ImportError:
        print(f"  Warning: Pillow not installed, using original image for {image_path.name}")
        return image_path.read_bytes()


def md_to_html(text):
    """Convert markdown text to HTML, handling scene breaks."""
    try:
        import markdown
        # Convert --- scene breaks to <hr> before markdown processing
        text = re.sub(r'^---$', '<hr/>', text, flags=re.MULTILINE)
        return markdown.markdown(text, extensions=["smarty"])
    except ImportError:
        # Fallback
        text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
        text = re.sub(r'^---$', '<hr/>', text, flags=re.MULTILINE)
        paragraphs = re.split(r"\n\n+", text.strip())
        html_parts = []
        for p in paragraphs:
            p = p.strip()
            if p == "<hr/>":
                html_parts.append("<hr/>")
            elif p:
                html_parts.append(f"<p>{p}</p>")
        return "\n".join(html_parts)


def parse_manuscript(text):
    """Split manuscript into chapters."""
    # Split on the --- separator between chapters
    segments = re.split(r'\n\n---\n\n', text)

    chapters = []
    for segment in segments:
        segment = segment.strip()
        match = re.match(r'^#\s+Chapter\s+(\d+):\s*(.+?)$', segment, re.MULTILINE)
        if match:
            number = int(match.group(1))
            title = match.group(2).strip()
            body = segment[match.end():].strip()
            chapters.append({"number": number, "title": title, "body_md": body})

    return chapters


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_epub(title, author, chapters, output_path):
    from ebooklib import epub

    book = epub.EpubBook()
    book.set_identifier("city-beneath-root-001")
    book.set_title(title)
    book.set_language("en")
    book.add_author(author)

    # Add metadata
    book.add_metadata("DC", "description",
        "Five biologists discover a hidden civilization of hyper-advanced frogs "
        "in the Amazon rainforest. An absurd comedy about consciousness, mortality, "
        "and what it means for a civilization to be advanced.")
    book.add_metadata("DC", "subject", "Science Fiction")
    book.add_metadata("DC", "subject", "Absurd Comedy")
    book.add_metadata("DC", "subject", "Philosophical Fiction")

    # CSS
    css_item = epub.EpubItem(
        uid="style", file_name="style/default.css",
        media_type="text/css", content=CSS.encode("utf-8")
    )
    book.add_item(css_item)

    # Cover image
    if COVER_IMAGE.exists():
        cover_bytes = resize_image(COVER_IMAGE, COVER_MAX_WIDTH, COVER_MAX_HEIGHT)
        book.set_cover("images/cover.png", cover_bytes)
        print(f"  Cover image added ({len(cover_bytes) // 1024} KB)")
    else:
        print("  Warning: No cover image found")

    # Build chapters
    epub_chapters = []
    for ch in chapters:
        chapter_filename = f"ch{ch['number']:02d}.xhtml"
        epub_ch = epub.EpubHtml(
            title=f"Chapter {ch['number']}: {ch['title']}",
            file_name=chapter_filename
        )
        epub_ch.add_item(css_item)

        html_parts = []

        # Chapter header banner image
        header_path = HEADER_DIR / f"ch{ch['number']:02d}_header.png"
        if header_path.exists():
            img_bytes = resize_image(header_path, HEADER_MAX_WIDTH, HEADER_MAX_HEIGHT)
            img_item = epub.EpubImage()
            img_filename = f"images/ch{ch['number']:02d}_header.png"
            img_item.file_name = img_filename
            img_item.media_type = "image/png"
            img_item.content = img_bytes
            book.add_item(img_item)
            html_parts.append(
                f'<div class="chapter-header">'
                f'<img src="{img_filename}" alt="Chapter {ch["number"]}"/>'
                f'</div>'
            )

        # Chapter number and title
        html_parts.append(f'<p class="chapter-number">Chapter {ch["number"]}</p>')
        html_parts.append(f'<h1 class="chapter-title">{ch["title"]}</h1>')
        html_parts.append('<p class="chapter-separator">&mdash;</p>')

        # Chapter prose
        html_parts.append(md_to_html(ch["body_md"]))

        epub_ch.content = "\n".join(html_parts).encode("utf-8")
        book.add_item(epub_ch)
        epub_chapters.append(epub_ch)
        print(f"  Ch {ch['number']:2d}: {ch['title']}")

    # TOC and spine
    book.toc = epub_chapters
    book.add_item(epub.EpubNcx())

    # Custom nav page with its own CSS to prevent justify spacing on TOC
    nav_css = epub.EpubItem(
        uid="nav_style",
        file_name="style/nav.css",
        media_type="text/css",
        content=b"""
body { font-family: Georgia, serif; margin: 1em; color: #000; }
h1 { font-size: 1.3em; margin-bottom: 1em; }
ol { list-style-type: none; padding-left: 0; }
li { margin-bottom: 0.5em; text-align: left; }
a { text-decoration: none; color: #333; }
"""
    )
    book.add_item(nav_css)

    nav_page = epub.EpubNav()
    nav_page.add_item(nav_css)
    book.add_item(nav_page)

    book.spine = ["nav"] + epub_chapters

    # Write
    output_path.parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(str(output_path), book)


def main():
    args = parse_args()

    if not MANUSCRIPT.exists():
        print(f"Error: Manuscript not found at {MANUSCRIPT}")
        print("Run 'python3 scripts/compile_manuscript.py' first.")
        sys.exit(1)

    text = MANUSCRIPT.read_text(encoding="utf-8")
    chapters = parse_manuscript(text)

    if not chapters:
        print("Error: No chapters found in manuscript.")
        sys.exit(1)

    print(f"Found {len(chapters)} chapters")

    output_path = (
        Path(args.output) if args.output
        else PROJECT_ROOT / "output" / f"{slugify(args.title)}.epub"
    )

    print(f"Building EPUB: {args.title} by {args.author}")
    build_epub(args.title, args.author, chapters, output_path)

    size_kb = output_path.stat().st_size // 1024
    print(f"\nExported to {output_path} ({size_kb} KB)")


if __name__ == "__main__":
    main()
