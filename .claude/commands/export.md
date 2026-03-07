Export the manuscript to EPUB format.

First, ensure the compiled manuscript exists and is up to date at output/manuscript.md. If it does not exist, run:

    .venv/bin/python3 scripts/compile_manuscript.py

Then ensure the required Python packages are installed in the virtual environment:

    .venv/bin/pip install ebooklib markdown Pillow

Then run the EPUB export script:

    .venv/bin/python3 scripts/export_epub.py

The script will:
1. Read the compiled manuscript from output/manuscript.md
2. Split it into chapters
3. Include the cover image from ImageAssets/Book_cover.png (if it exists)
4. Include chapter images from ImageAssets/ (resized for e-readers, if they exist)
5. Generate the EPUB in output/

If the user specifies a custom title or author, pass them as arguments:

    .venv/bin/python3 scripts/export_epub.py --title "Custom Title" --author "Custom Author"

After the script completes, report the output file path and file size.