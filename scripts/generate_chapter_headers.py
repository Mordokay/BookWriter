#!/usr/bin/env python3
"""
Generate abstract chapter header images for The City Beneath the Root.
Style: Painterly Bioluminescent Literary Sci-Fi

Each header is a wide banner (1400x250) with:
- Dark organic background with gradient
- Abstract geometric shapes symbolic of the chapter
- Bioluminescent glow effects
- No text (chapter titles handled by EPUB markup)
"""

import os
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Seed for reproducibility
random.seed(42)

# Output directory
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ImageAssets", "chapter_headers")
os.makedirs(OUT_DIR, exist_ok=True)

# Dimensions — high resolution, no downscaling
# E-reader scales smoothly to fit screen
W, H = 5600, 1000
S = 4  # scale factor for line widths, radii, positions vs original 1400x250 design

# Color palette — LIGHT MODE for e-ink Kindle
# Light background, dark lines
DEEP_TEAL = (220, 235, 240)
MOSS_GREEN = (225, 238, 225)
WET_STONE = (230, 230, 232)
CHARCOAL = (240, 242, 244)
DARK_BG = (245, 245, 243)

# Accent / line colors — DARK for visibility on e-ink
CHARTREUSE = (50, 80, 35)
ALGAE_CYAN = (30, 80, 75)
WARM_GOLD = (80, 65, 30)
COPPER_AMBER = (90, 55, 25)
PALE_LIME = (55, 85, 40)
MINERAL_IVORY = (70, 70, 60)
SOFT_BLUE = (35, 70, 85)

# Chapter data: (number, title, primary_accent, symbol_type, symbol_params)
# symbol_type: "roots", "circles", "waves", "dots", "ring", "lines", "grid", "spiral", "chevrons", "shatter"
CHAPTERS = [
    (1,  "Root Density",                    CHARTREUSE,   "roots",    {"density": 12}),
    (2,  "The Monitored",                   ALGAE_CYAN,   "dots",     {"count": 40, "watched": True}),
    (3,  "First Contact",                   WARM_GOLD,    "ring",     {"rings": 3}),
    (4,  "Temporary Coordinators\nof Distributed Harmonies", ALGAE_CYAN, "grid", {"cols": 5}),
    (5,  "The Pairings",                    WARM_GOLD,    "circles",  {"pairs": 5}),
    (6,  "The Machine for\nDistributing Power", COPPER_AMBER, "lines", {"radiating": True}),
    (7,  "Breakfast, Childcare,\nSex, Boredom", PALE_LIME, "waves",  {"layers": 5}),
    (8,  "Competitive Vibrations",          ALGAE_CYAN,   "waves",    {"layers": 7, "vibration": True}),
    (9,  "Show Me the Mechanism",           CHARTREUSE,   "spiral",   {"turns": 3}),
    (10, "The Fungal Audit",                PALE_LIME,    "dots",     {"count": 60, "fungal": True}),
    (11, "The Temporary\nSwamp Event",      WARM_GOLD,    "circles",  {"dissolving": True}),
    (12, "Wet In, Wet Out",                 ALGAE_CYAN,   "waves",    {"layers": 3, "mourning": True}),
    (13, "Every Elegant\nSystem Leaks",     COPPER_AMBER, "lines",    {"broken": True}),
    (14, "The Other Root",                  CHARTREUSE,   "roots",    {"density": 8, "displaced": True}),
    (15, "The Archive\nRemembers Selectively", WARM_GOLD, "dots",     {"count": 30, "fading": True}),
    (16, "The Siberian Argument",           SOFT_BLUE,    "chevrons", {"opposing": True}),
    (17, "After Hours",                     ALGAE_CYAN,   "circles",  {"dim": True}),
    (18, "Voluntary Participation",         COPPER_AMBER, "ring",     {"rings": 5, "tightening": True}),
    (19, "The Growth",                      CHARTREUSE,   "roots",    {"density": 20, "aggressive": True}),
    (20, "The Merging",                     WARM_GOLD,    "circles",  {"merging": True}),
    (21, "The Archivist's Silence",         MINERAL_IVORY,"dots",     {"count": 20, "sparse": True}),
    (22, "Talla's Wager",                   COPPER_AMBER, "shatter",  {}),
    (23, "The Displacement",                ALGAE_CYAN,   "waves",    {"layers": 9, "displacement": True}),
    (24, "The Cost",                        WARM_GOLD,    "circles",  {"cost": True}),
    (25, "The Administrative\nCourtesy",    MINERAL_IVORY,"lines",    {"cage": True}),
    (26, "Five Answers",                    WARM_GOLD,    "circles",  {"five": True}),
    (27, "The Wet Continuity",              ALGAE_CYAN,   "waves",    {"layers": 4, "final": True}),
]


def make_gradient_bg(w, h, color_top, color_bot):
    """Create a vertical gradient background."""
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / h
        r = int(color_top[0] * (1 - t) + color_bot[0] * t)
        g = int(color_top[1] * (1 - t) + color_bot[1] * t)
        b = int(color_top[2] * (1 - t) + color_bot[2] * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def add_glow(img, glow_layer, intensity=0.6):
    """Composite a blurred glow layer onto the image."""
    blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=20))
    from PIL import ImageChops
    enhanced = Image.blend(Image.new("RGB", img.size, (0, 0, 0)), blurred, intensity)
    from PIL import ImageChops
    return ImageChops.add(img, enhanced)


def draw_roots(draw, glow_draw, w, h, color, params):
    """Organic root-like branching lines."""
    density = params.get("density", 10)
    aggressive = params.get("aggressive", False)
    displaced = params.get("displaced", False)

    for i in range(density):
        x = random.randint(50*S, w - 50*S)
        y_start = random.choice([0, h])
        segments = random.randint(4, 8)
        points = [(x, y_start)]
        for s in range(segments):
            dx = random.randint(-60*S, 60*S)
            dy = (h // segments) * (1 if y_start == 0 else -1)
            if displaced and i % 3 == 0:
                dx *= 2
            nx = max(20*S, min(w - 20*S, points[-1][0] + dx))
            ny = max(20*S, min(h - 20*S, points[-1][1] + dy))
            points.append((nx, ny))

        thickness = S * (5 if aggressive else 4)
        alpha = 220 if aggressive else 180
        for j in range(len(points) - 1):
            draw.line([points[j], points[j + 1]], fill=(*color, alpha), width=thickness)

        if len(points) > 3:
            bp = points[random.randint(1, len(points) - 2)]
            for _ in range(random.randint(1, 3)):
                ex = bp[0] + random.randint(-40*S, 40*S)
                ey = bp[1] + random.randint(-30*S, 30*S)
                draw.line([bp, (ex, ey)], fill=(*color, 140), width=S*2)


def draw_circles(draw, glow_draw, w, h, color, params):
    """Concentric or scattered circles."""
    cx, cy = w // 2, h // 2
    lw = S * 3  # base line width

    if params.get("pairs"):
        n = params["pairs"]
        for i in range(n):
            x = 200*S + i * (w - 400*S) // (n - 1)
            y = cy + random.randint(-30*S, 30*S)
            r = random.randint(20*S, 35*S)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 180), width=lw)
            if i < n - 1:
                x2 = 200*S + (i + 1) * (w - 400*S) // (n - 1)
                draw.line([(x + r, y), (x2 - r - 30*S, y)], fill=(*color, 100), width=S*2)

    elif params.get("dissolving"):
        for r in range(20*S, 120*S, 15*S):
            alpha = max(60, 200 - r // S)
            segments = 30
            for s in range(segments):
                angle = 2 * math.pi * s / segments
                if random.random() > 0.3:
                    a2 = angle + 2 * math.pi / segments * 0.7
                    x1 = cx + r * math.cos(angle)
                    y1 = cy + r * math.sin(angle)
                    x2 = cx + r * math.cos(a2)
                    y2 = cy + r * math.sin(a2)
                    draw.line([(x1, y1), (x2, y2)], fill=(*color, alpha), width=lw)

    elif params.get("merging"):
        for i in range(12):
            angle = 2 * math.pi * i / 12
            dist = 80*S + random.randint(-20*S, 20*S)
            x = cx + dist * math.cos(angle)
            y = cy + dist * math.sin(angle)
            r = random.randint(15*S, 30*S)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 160), width=lw)
        draw.ellipse([cx - 8*S, cy - 8*S, cx + 8*S, cy + 8*S], fill=(*color, 220))

    elif params.get("dim"):
        for _ in range(8):
            x = random.randint(100*S, w - 100*S)
            y = random.randint(50*S, h - 50*S)
            r = random.randint(15*S, 45*S)
            alpha = random.randint(80, 150)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, alpha), width=lw)

    elif params.get("cost"):
        for i in range(7):
            x = 180*S + i * (w - 360*S) // 6
            y = cy
            r = 25*S
            if i == 3:
                for angle_deg in range(0, 360, 15):
                    if 90 < angle_deg < 200:
                        continue
                    a = math.radians(angle_deg)
                    a2 = math.radians(angle_deg + 12)
                    x1, y1 = x + r * math.cos(a), y + r * math.sin(a)
                    x2, y2 = x + r * math.cos(a2), y + r * math.sin(a2)
                    draw.line([(x1, y1), (x2, y2)], fill=(*color, 180), width=lw)
            else:
                draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 160), width=lw)

    elif params.get("five"):
        positions = [(250*S, cy - 40*S), (450*S, cy + 20*S), (650*S, cy - 10*S), (850*S, cy + 30*S), (1050*S, cy - 25*S)]
        sizes = [30*S, 25*S, 28*S, 22*S, 35*S]
        alphas = [200, 160, 180, 140, 120]
        for (x, y), r, a in zip(positions, sizes, alphas):
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, a), width=lw)

    else:
        for r in range(20*S, 100*S, 12*S):
            alpha = max(60, 200 - r // S)
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(*color, alpha), width=lw)


def draw_waves(draw, glow_draw, w, h, color, params):
    """Horizontal wave patterns."""
    layers = params.get("layers", 5)
    mourning = params.get("mourning", False)
    vibration = params.get("vibration", False)
    displacement = params.get("displacement", False)
    final = params.get("final", False)
    lw = S * 3

    for i in range(layers):
        y_base = 60*S + i * (h - 120*S) // max(layers - 1, 1)
        alpha = max(80, 220 - i * 20)
        freq = 0.008 / S if not vibration else (0.015 + i * 0.003) / S
        amp = (15 + i * 3) * S if not displacement else (25 + i * 5) * S

        if mourning:
            amp = max(5*S, amp - i * 4*S)
            alpha = max(60, alpha - i * 15)

        if final:
            freq = 0.006 / S
            amp = (10 + i * 2) * S

        points = []
        for x in range(0, w, 3):
            y = y_base + amp * math.sin(freq * x + i * 1.2)
            points.append((x, y))

        if len(points) > 1:
            draw.line(points, fill=(*color, alpha), width=lw)


def draw_dots(draw, glow_draw, w, h, color, params):
    """Scattered dot patterns."""
    count = params.get("count", 30)
    fading = params.get("fading", False)
    fungal = params.get("fungal", False)
    sparse = params.get("sparse", False)
    watched = params.get("watched", False)

    for i in range(count):
        x = random.randint(80*S, w - 80*S)
        y = random.randint(40*S, h - 40*S)
        r = random.randint(2*S, 6*S) if not fungal else random.randint(1*S, 8*S)
        if sparse:
            r = random.randint(1*S, 3*S)

        alpha = 220 - int(i / count * 150) if fading else random.randint(100, 220)

        if watched and i % 5 == 0:
            r = random.randint(5*S, 9*S)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, alpha), width=S*2)
            draw.ellipse([x - 2*S, y - 2*S, x + 2*S, y + 2*S], fill=(*color, alpha))
        else:
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(*color, alpha))


def draw_ring(draw, glow_draw, w, h, color, params):
    """Concentric rings."""
    cx, cy = w // 2, h // 2
    rings = params.get("rings", 3)
    tightening = params.get("tightening", False)
    lw = S * 3

    for i in range(rings):
        r = (30 + i * 25) * S if not tightening else (30 + i * 15) * S
        alpha = max(80, 220 - i * 30)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(*color, alpha), width=lw)

    stone_r = 20 * S
    for i in range(6):
        angle = 2 * math.pi * i / 6
        sx = cx + stone_r * math.cos(angle)
        sy = cy + stone_r * math.sin(angle)
        draw.ellipse([sx - 3*S, sy - 3*S, sx + 3*S, sy + 3*S], fill=(*color, 220))


def draw_lines(draw, glow_draw, w, h, color, params):
    """Line patterns."""
    cx, cy = w // 2, h // 2
    radiating = params.get("radiating", False)
    broken = params.get("broken", False)
    cage = params.get("cage", False)
    lw = S * 3

    if radiating:
        for i in range(16):
            angle = 2 * math.pi * i / 16
            length = random.randint(60*S, 150*S)
            x2 = cx + length * math.cos(angle)
            y2 = cy + length * math.sin(angle)
            alpha = random.randint(120, 200)
            draw.line([(cx, cy), (x2, y2)], fill=(*color, alpha), width=lw)

    elif broken:
        for i in range(9):
            y = 50*S + i * (h - 100*S) // 8
            alpha = random.randint(120, 200)
            x = 100*S
            while x < w - 100*S:
                seg_len = random.randint(30*S, 120*S)
                gap = random.randint(10*S, 40*S)
                draw.line([(x, y), (x + seg_len, y)], fill=(*color, alpha), width=lw)
                x += seg_len + gap

    elif cage:
        bar_count = 12
        for i in range(bar_count):
            x = 200*S + i * (w - 400*S) // (bar_count - 1)
            alpha = 160 if i % 2 == 0 else 100
            draw.line([(x, 40*S), (x, h - 40*S)], fill=(*color, alpha), width=lw)
        for y in [h // 3, 2 * h // 3]:
            draw.line([(200*S, y), (w - 200*S, y)], fill=(*color, 120), width=lw)


def draw_spiral(draw, glow_draw, w, h, color, params):
    """Spiral pattern."""
    cx, cy = w // 2, h // 2
    turns = params.get("turns", 3)
    lw = S * 3

    points = []
    for t in range(0, 360 * turns, 2):
        angle = math.radians(t)
        r = 10*S + t * 0.12 * S
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        if 20*S < x < w - 20*S and 20*S < y < h - 20*S:
            points.append((x, y))

    if len(points) > 1:
        draw.line(points, fill=(*color, 180), width=lw)


def draw_chevrons(draw, glow_draw, w, h, color, params):
    """Opposing chevron patterns."""
    cx = w // 2
    lw = S * 3
    for i in range(5):
        x = cx - 80*S - i * 50*S
        y_top = h // 2 - 60*S
        y_mid = h // 2
        y_bot = h // 2 + 60*S
        alpha = max(80, 200 - i * 25)
        draw.line([(x + 30*S, y_top), (x, y_mid), (x + 30*S, y_bot)], fill=(*color, alpha), width=lw)

    r2, g2, b2 = min(255, color[0] + 40), max(0, color[1] - 30), max(0, color[2] - 20)
    for i in range(5):
        x = cx + 80*S + i * 50*S
        y_top = h // 2 - 60*S
        y_mid = h // 2
        y_bot = h // 2 + 60*S
        alpha = max(80, 200 - i * 25)
        draw.line([(x - 30*S, y_top), (x, y_mid), (x - 30*S, y_bot)], fill=(r2, g2, b2, alpha), width=lw)


def draw_grid(draw, glow_draw, w, h, color, params):
    """Grid pattern — distributed coordination nodes connected by faint lines."""
    cols = params.get("cols", 5)
    rows = 3
    lw = S * 3
    margin_x = 200 * S
    margin_y = 80 * S

    # Node positions
    nodes = []
    for row in range(rows):
        for col in range(cols):
            x = margin_x + col * (w - 2 * margin_x) // max(cols - 1, 1)
            y = margin_y + row * (h - 2 * margin_y) // max(rows - 1, 1)
            # Slight organic offset
            x += random.randint(-15 * S, 15 * S)
            y += random.randint(-10 * S, 10 * S)
            nodes.append((x, y))

    # Connection lines — horizontal and vertical neighbors
    for row in range(rows):
        for col in range(cols):
            idx = row * cols + col
            # Right neighbor
            if col < cols - 1:
                n_idx = row * cols + col + 1
                alpha = random.randint(80, 130)
                draw.line([nodes[idx], nodes[n_idx]], fill=(*color, alpha), width=S * 2)
            # Below neighbor
            if row < rows - 1:
                n_idx = (row + 1) * cols + col
                alpha = random.randint(80, 130)
                draw.line([nodes[idx], nodes[n_idx]], fill=(*color, alpha), width=S * 2)

    # Nodes themselves — small filled circles with outer ring
    for x, y in nodes:
        r_outer = random.randint(8 * S, 12 * S)
        alpha = random.randint(140, 200)
        draw.ellipse([x - r_outer, y - r_outer, x + r_outer, y + r_outer],
                     outline=(*color, alpha), width=lw)
        r_inner = 3 * S
        draw.ellipse([x - r_inner, y - r_inner, x + r_inner, y + r_inner],
                     fill=(*color, alpha))


def draw_shatter(draw, glow_draw, w, h, color, params):
    """Shattered/cracked pattern."""
    cx, cy = w // 2, h // 2
    lw = S * 3

    draw.ellipse([cx - 5*S, cy - 5*S, cx + 5*S, cy + 5*S], fill=(*color, 230))

    for i in range(12):
        angle = 2 * math.pi * i / 12 + random.uniform(-0.2, 0.2)
        points = [(cx, cy)]
        x, y = float(cx), float(cy)
        for seg in range(random.randint(3, 6)):
            dx = random.randint(15*S, 40*S) * math.cos(angle + random.uniform(-0.3, 0.3))
            dy = random.randint(15*S, 40*S) * math.sin(angle + random.uniform(-0.3, 0.3))
            x += dx
            y += dy
            points.append((x, y))

        alpha = random.randint(140, 220)
        if len(points) > 1:
            draw.line(points, fill=(*color, alpha), width=lw)


SYMBOL_FUNCS = {
    "roots": draw_roots,
    "circles": draw_circles,
    "waves": draw_waves,
    "dots": draw_dots,
    "ring": draw_ring,
    "lines": draw_lines,
    "spiral": draw_spiral,
    "chevrons": draw_chevrons,
    "grid": draw_grid,
    "shatter": draw_shatter,
}


def render_text(img, chapter_num, title, color):
    """Render chapter number and title onto the image."""
    draw = ImageDraw.Draw(img)

    # Try to use a nice font, fall back to default
    title_size = 32
    num_size = 18
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir Next.ttc", title_size, index=4)  # Demi Bold
        num_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir Next.ttc", num_size, index=1)  # Italic
    except (OSError, IOError):
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", title_size)
            num_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", num_size)
        except (OSError, IOError):
            title_font = ImageFont.load_default()
            num_font = ImageFont.load_default()

    # Chapter number
    num_text = f"CHAPTER {chapter_num}"
    num_bbox = draw.textbbox((0, 0), num_text, font=num_font)
    num_w = num_bbox[2] - num_bbox[0]
    num_x = (W - num_w) // 2
    num_y = 60

    # Draw number with subtle glow
    for offset in [(0, 0)]:
        draw.text((num_x + offset[0], num_y + offset[1]), num_text,
                  fill=(200, 195, 175, 160), font=num_font)

    # Chapter title
    lines = title.split("\n")
    line_height = title_size + 8
    total_text_height = len(lines) * line_height
    title_y_start = num_y + 40

    for i, line in enumerate(lines):
        t_bbox = draw.textbbox((0, 0), line, font=title_font)
        t_w = t_bbox[2] - t_bbox[0]
        t_x = (W - t_w) // 2
        t_y = title_y_start + i * line_height

        # Text shadow/glow
        shadow_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow_img)
        shadow_draw.text((t_x, t_y), line, fill=(*color, 100), font=title_font)
        shadow_blurred = shadow_img.filter(ImageFilter.GaussianBlur(radius=8))
        img = Image.alpha_composite(img, shadow_blurred)

        # Main text
        draw = ImageDraw.Draw(img)
        draw.text((t_x, t_y), line, fill=(230, 225, 210, 240), font=title_font)

    # Thin decorative line below title
    line_y = title_y_start + total_text_height + 15
    line_half = 80
    cx = W // 2
    draw.line([(cx - line_half, line_y), (cx + line_half, line_y)],
              fill=(*color, 80), width=1)

    return img


def generate_chapter_header(chapter_num, title, accent_color, symbol_type, symbol_params):
    """Generate a single chapter header image at high resolution."""
    # Background gradient
    bg = make_gradient_bg(W, H, DARK_BG, CHARCOAL)
    img = bg.convert("RGBA")

    # Symbol layer — draw directly, no glow blur (clean lines for e-ink)
    symbol_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    symbol_draw = ImageDraw.Draw(symbol_layer)

    # Pass symbol_draw as both draw and glow_draw — the "glow" lines
    # become thicker accent lines at high res instead of blurred halos
    func = SYMBOL_FUNCS.get(symbol_type)
    if func:
        func(symbol_draw, symbol_draw, W, H, accent_color, symbol_params)

    # Composite
    img = Image.alpha_composite(img, symbol_layer)

    return img


def main():
    print("Generating chapter headers...")
    for ch_num, title, accent, sym_type, sym_params in CHAPTERS:
        img = generate_chapter_header(ch_num, title, accent, sym_type, sym_params)

        # Save as PNG
        filename = f"ch{ch_num:02d}_header.png"
        filepath = os.path.join(OUT_DIR, filename)
        img.save(filepath, "PNG", optimize=True)
        print(f"  {filename} ({title.split(chr(10))[0]})")

    # Also generate a simple section divider (ornamental break)
    div = Image.new("RGBA", (400, 40), (0, 0, 0, 0))
    div_draw = ImageDraw.Draw(div)
    cx, cy = 200, 20
    # Three small dots (dark for e-ink)
    for dx in [-20, 0, 20]:
        div_draw.ellipse([cx + dx - 3, cy - 3, cx + dx + 3, cy + 3],
                        fill=(80, 80, 80, 180))
    # Thin lines
    div_draw.line([(40, cy), (cx - 35, cy)], fill=(80, 80, 80, 100), width=1)
    div_draw.line([(cx + 35, cy), (360, cy)], fill=(80, 80, 80, 100), width=1)
    div.save(os.path.join(OUT_DIR, "section_divider.png"), "PNG")
    print("  section_divider.png")

    print(f"\nDone. {len(CHAPTERS)} chapter headers + 1 divider saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
