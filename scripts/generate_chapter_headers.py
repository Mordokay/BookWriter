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

# Dimensions
W, H = 1400, 250

# Color palette
DEEP_TEAL = (15, 45, 55)
MOSS_GREEN = (40, 70, 45)
WET_STONE = (55, 60, 65)
CHARCOAL = (20, 25, 30)
DARK_BG = (12, 18, 22)

# Accent / glow colors (with alpha for compositing)
CHARTREUSE = (160, 220, 80)
ALGAE_CYAN = (60, 180, 170)
WARM_GOLD = (180, 150, 70)
COPPER_AMBER = (170, 110, 60)
PALE_LIME = (140, 200, 100)
MINERAL_IVORY = (200, 195, 175)
SOFT_BLUE = (70, 140, 160)

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

    base_alpha = 180 if aggressive else 120
    glow_color = (*color, base_alpha)

    for i in range(density):
        x = random.randint(50, w - 50)
        y_start = random.choice([0, h])
        segments = random.randint(4, 8)
        points = [(x, y_start)]
        for s in range(segments):
            dx = random.randint(-60, 60)
            dy = (h // segments) * (1 if y_start == 0 else -1)
            if displaced and i % 3 == 0:
                dx *= 2
            nx = max(20, min(w - 20, points[-1][0] + dx))
            ny = max(20, min(h - 20, points[-1][1] + dy))
            points.append((nx, ny))

        thickness = 3 if aggressive else 2
        for j in range(len(points) - 1):
            draw.line([points[j], points[j + 1]], fill=(*color, 60), width=thickness)
            glow_draw.line([points[j], points[j + 1]], fill=glow_color, width=thickness + 4)

        # Branch points
        if len(points) > 3:
            bp = points[random.randint(1, len(points) - 2)]
            for _ in range(random.randint(1, 3)):
                ex = bp[0] + random.randint(-40, 40)
                ey = bp[1] + random.randint(-30, 30)
                draw.line([bp, (ex, ey)], fill=(*color, 40), width=1)
                glow_draw.line([bp, (ex, ey)], fill=(*color, 80), width=3)


def draw_circles(draw, glow_draw, w, h, color, params):
    """Concentric or scattered circles."""
    cx, cy = w // 2, h // 2

    if params.get("pairs"):
        # Paired circles
        n = params["pairs"]
        for i in range(n):
            x = 200 + i * (w - 400) // (n - 1)
            y = cy + random.randint(-30, 30)
            r = random.randint(20, 35)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 100), width=2)
            glow_draw.ellipse([x - r - 5, y - r - 5, x + r + 5, y + r + 5], outline=(*color, 150), width=6)
            # Connecting line to next
            if i < n - 1:
                x2 = 200 + (i + 1) * (w - 400) // (n - 1)
                draw.line([(x + r, y), (x2 - r - 30, y)], fill=(*color, 40), width=1)

    elif params.get("dissolving"):
        # Circle dissolving into fragments
        for r in range(20, 120, 15):
            alpha = max(20, 140 - r)
            segments = 30
            for s in range(segments):
                angle = 2 * math.pi * s / segments
                if random.random() > 0.3:  # gaps in outer rings
                    a2 = angle + 2 * math.pi / segments * 0.7
                    x1 = cx + r * math.cos(angle)
                    y1 = cy + r * math.sin(angle)
                    x2 = cx + r * math.cos(a2)
                    y2 = cy + r * math.sin(a2)
                    draw.line([(x1, y1), (x2, y2)], fill=(*color, alpha), width=2)
                    glow_draw.line([(x1, y1), (x2, y2)], fill=(*color, alpha + 40), width=5)

    elif params.get("merging"):
        # Multiple circles converging to center
        for i in range(12):
            angle = 2 * math.pi * i / 12
            dist = 80 + random.randint(-20, 20)
            x = cx + dist * math.cos(angle)
            y = cy + dist * math.sin(angle)
            r = random.randint(15, 30)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 80), width=1)
            glow_draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 120), width=4)
        # Central bright point
        glow_draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=(*color, 200))

    elif params.get("dim"):
        # Dim scattered circles (night)
        for _ in range(8):
            x = random.randint(100, w - 100)
            y = random.randint(50, h - 50)
            r = random.randint(15, 45)
            alpha = random.randint(30, 70)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, alpha), width=1)
            glow_draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, alpha + 20), width=3)

    elif params.get("cost"):
        # Circles with one broken
        for i in range(7):
            x = 180 + i * (w - 360) // 6
            y = cy
            r = 25
            if i == 3:  # broken one
                # Draw partial circle
                for angle_deg in range(0, 360, 15):
                    if 90 < angle_deg < 200:
                        continue
                    a = math.radians(angle_deg)
                    a2 = math.radians(angle_deg + 12)
                    x1, y1 = x + r * math.cos(a), y + r * math.sin(a)
                    x2, y2 = x + r * math.cos(a2), y + r * math.sin(a2)
                    draw.line([(x1, y1), (x2, y2)], fill=(*color, 100), width=2)
            else:
                draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 80), width=2)
                glow_draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, 100), width=4)

    elif params.get("five"):
        # Five distinct circles at different heights
        positions = [(250, cy - 40), (450, cy + 20), (650, cy - 10), (850, cy + 30), (1050, cy - 25)]
        sizes = [30, 25, 28, 22, 35]
        alphas = [140, 100, 120, 90, 60]
        for (x, y), r, a in zip(positions, sizes, alphas):
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, a), width=2)
            glow_draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, a + 30), width=5)

    else:
        # Simple concentric
        for r in range(20, 100, 12):
            alpha = max(30, 150 - r)
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(*color, alpha), width=1)
            glow_draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(*color, alpha + 30), width=4)


def draw_waves(draw, glow_draw, w, h, color, params):
    """Horizontal wave patterns."""
    layers = params.get("layers", 5)
    mourning = params.get("mourning", False)
    vibration = params.get("vibration", False)
    displacement = params.get("displacement", False)
    final = params.get("final", False)

    for i in range(layers):
        y_base = 60 + i * (h - 120) // max(layers - 1, 1)
        alpha = max(30, 160 - i * 20)
        freq = 0.008 if not vibration else 0.015 + i * 0.003
        amp = 15 + i * 3 if not displacement else 25 + i * 5

        if mourning:
            amp = max(5, amp - i * 4)  # waves flatten
            alpha = max(20, alpha - i * 15)

        if final:
            freq = 0.006
            amp = 10 + i * 2  # gentle

        points = []
        for x in range(0, w, 3):
            y = y_base + amp * math.sin(freq * x + i * 1.2)
            points.append((x, y))

        if len(points) > 1:
            draw.line(points, fill=(*color, alpha), width=2)
            glow_draw.line(points, fill=(*color, min(255, alpha + 50)), width=5)


def draw_dots(draw, glow_draw, w, h, color, params):
    """Scattered dot patterns (spores, memories, surveillance points)."""
    count = params.get("count", 30)
    fading = params.get("fading", False)
    fungal = params.get("fungal", False)
    sparse = params.get("sparse", False)
    watched = params.get("watched", False)

    for i in range(count):
        x = random.randint(80, w - 80)
        y = random.randint(40, h - 40)
        r = random.randint(2, 6) if not fungal else random.randint(1, 8)

        if sparse:
            r = random.randint(1, 3)

        alpha = 180 - int(i / count * 150) if fading else random.randint(60, 180)

        if watched and i % 5 == 0:
            # Larger "eye" dots
            r = random.randint(5, 9)
            draw.ellipse([x - r, y - r, x + r, y + r], outline=(*color, alpha), width=1)
            draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(*color, alpha))
        else:
            draw.ellipse([x - r, y - r, x + r, y + r], fill=(*color, alpha))

        glow_draw.ellipse([x - r - 3, y - r - 3, x + r + 3, y + r + 3], fill=(*color, min(255, alpha)))


def draw_ring(draw, glow_draw, w, h, color, params):
    """Concentric rings (displacement platform, tightening)."""
    cx, cy = w // 2, h // 2
    rings = params.get("rings", 3)
    tightening = params.get("tightening", False)

    for i in range(rings):
        r = 30 + i * 25 if not tightening else 30 + i * 15
        alpha = max(40, 180 - i * 30)
        width = 2 if not tightening else max(1, 3 - i)
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(*color, alpha), width=width)
        glow_draw.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3],
                         outline=(*color, min(255, alpha + 40)), width=width + 4)

    # Central stones (small dots in a ring)
    stone_r = 20
    for i in range(6):
        angle = 2 * math.pi * i / 6
        sx = cx + stone_r * math.cos(angle)
        sy = cy + stone_r * math.sin(angle)
        draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(*color, 200))
        glow_draw.ellipse([sx - 6, sy - 6, sx + 6, sy + 6], fill=(*color, 150))


def draw_lines(draw, glow_draw, w, h, color, params):
    """Line patterns (power structures, cages, broken systems)."""
    cx, cy = w // 2, h // 2
    radiating = params.get("radiating", False)
    broken = params.get("broken", False)
    cage = params.get("cage", False)

    if radiating:
        for i in range(16):
            angle = 2 * math.pi * i / 16
            length = random.randint(60, 150)
            x2 = cx + length * math.cos(angle)
            y2 = cy + length * math.sin(angle)
            alpha = random.randint(60, 140)
            draw.line([(cx, cy), (x2, y2)], fill=(*color, alpha), width=1)
            glow_draw.line([(cx, cy), (x2, y2)], fill=(*color, min(255, alpha + 50)), width=4)

    elif broken:
        # Parallel lines with breaks
        for i in range(9):
            y = 50 + i * (h - 100) // 8
            alpha = random.randint(60, 140)
            # Draw with random gaps
            x = 100
            while x < w - 100:
                seg_len = random.randint(30, 120)
                gap = random.randint(10, 40)
                draw.line([(x, y), (x + seg_len, y)], fill=(*color, alpha), width=1)
                glow_draw.line([(x, y), (x + seg_len, y)], fill=(*color, min(255, alpha + 40)), width=3)
                x += seg_len + gap

    elif cage:
        # Vertical bars with horizontal connectors
        bar_count = 12
        for i in range(bar_count):
            x = 200 + i * (w - 400) // (bar_count - 1)
            alpha = 80 if i % 2 == 0 else 50
            draw.line([(x, 40), (x, h - 40)], fill=(*color, alpha), width=1)
            glow_draw.line([(x, 40), (x, h - 40)], fill=(*color, alpha + 30), width=3)

        # Two horizontal bars
        for y in [h // 3, 2 * h // 3]:
            draw.line([(200, y), (w - 200, y)], fill=(*color, 60), width=1)
            glow_draw.line([(200, y), (w - 200, y)], fill=(*color, 90), width=3)


def draw_spiral(draw, glow_draw, w, h, color, params):
    """Spiral pattern (mechanism, organic computation)."""
    cx, cy = w // 2, h // 2
    turns = params.get("turns", 3)

    points = []
    for t in range(0, 360 * turns, 3):
        angle = math.radians(t)
        r = 10 + t * 0.12
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        if 20 < x < w - 20 and 20 < y < h - 20:
            points.append((x, y))

    if len(points) > 1:
        alpha = 120
        draw.line(points, fill=(*color, alpha), width=2)
        glow_draw.line(points, fill=(*color, min(255, alpha + 60)), width=6)


def draw_chevrons(draw, glow_draw, w, h, color, params):
    """Opposing chevron patterns (conflict, debate)."""
    cx = w // 2
    # Left-pointing chevrons
    for i in range(5):
        x = cx - 80 - i * 50
        y_top = h // 2 - 60
        y_mid = h // 2
        y_bot = h // 2 + 60
        alpha = max(40, 150 - i * 25)
        draw.line([(x + 30, y_top), (x, y_mid), (x + 30, y_bot)], fill=(*color, alpha), width=2)
        glow_draw.line([(x + 30, y_top), (x, y_mid), (x + 30, y_bot)], fill=(*color, min(255, alpha + 40)), width=5)

    # Right-pointing chevrons (different shade)
    r2, g2, b2 = min(255, color[0] + 40), max(0, color[1] - 30), max(0, color[2] - 20)
    for i in range(5):
        x = cx + 80 + i * 50
        y_top = h // 2 - 60
        y_mid = h // 2
        y_bot = h // 2 + 60
        alpha = max(40, 150 - i * 25)
        draw.line([(x - 30, y_top), (x, y_mid), (x - 30, y_bot)], fill=(r2, g2, b2, alpha), width=2)
        glow_draw.line([(x - 30, y_top), (x, y_mid), (x - 30, y_bot)], fill=(r2, g2, b2, min(255, alpha + 40)), width=5)


def draw_shatter(draw, glow_draw, w, h, color, params):
    """Shattered/cracked pattern (breaking point)."""
    cx, cy = w // 2, h // 2

    # Central impact point
    glow_draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(*color, 200))

    # Radiating cracks
    for i in range(12):
        angle = 2 * math.pi * i / 12 + random.uniform(-0.2, 0.2)
        length = random.randint(60, 180)
        points = [(cx, cy)]
        x, y = cx, cy
        for seg in range(random.randint(3, 6)):
            dx = random.randint(15, 40) * math.cos(angle + random.uniform(-0.3, 0.3))
            dy = random.randint(15, 40) * math.sin(angle + random.uniform(-0.3, 0.3))
            x += dx
            y += dy
            points.append((x, y))

        alpha = random.randint(80, 160)
        if len(points) > 1:
            draw.line(points, fill=(*color, alpha), width=1)
            glow_draw.line(points, fill=(*color, min(255, alpha + 50)), width=4)


SYMBOL_FUNCS = {
    "roots": draw_roots,
    "circles": draw_circles,
    "waves": draw_waves,
    "dots": draw_dots,
    "ring": draw_ring,
    "lines": draw_lines,
    "spiral": draw_spiral,
    "chevrons": draw_chevrons,
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
    """Generate a single chapter header image."""
    # Background gradient
    bg = make_gradient_bg(W, H, DARK_BG, CHARCOAL)
    img = bg.convert("RGBA")

    # Symbol layer
    symbol_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    symbol_draw = ImageDraw.Draw(symbol_layer)

    # Glow layer
    glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    # Draw the abstract symbol
    func = SYMBOL_FUNCS.get(symbol_type)
    if func:
        func(symbol_draw, glow_draw, W, H, accent_color, symbol_params)

    # Blur the glow layer
    glow_blurred = glow_layer.filter(ImageFilter.GaussianBlur(radius=12))

    # Composite: bg + glow + symbols
    img = Image.alpha_composite(img, glow_blurred)
    img = Image.alpha_composite(img, symbol_layer)

    # Add subtle noise texture
    noise = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    noise_draw = ImageDraw.Draw(noise)
    for _ in range(3000):
        x = random.randint(0, W - 1)
        y = random.randint(0, H - 1)
        a = random.randint(3, 12)
        noise_draw.point((x, y), fill=(255, 255, 255, a))
    img = Image.alpha_composite(img, noise)

    # No text — EPUB handles chapter titles in markup

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
    # Three small dots
    for dx in [-20, 0, 20]:
        div_draw.ellipse([cx + dx - 3, cy - 3, cx + dx + 3, cy + 3],
                        fill=(60, 180, 170, 120))
    # Thin lines
    div_draw.line([(40, cy), (cx - 35, cy)], fill=(60, 180, 170, 60), width=1)
    div_draw.line([(cx + 35, cy), (360, cy)], fill=(60, 180, 170, 60), width=1)
    div.save(os.path.join(OUT_DIR, "section_divider.png"), "PNG")
    print("  section_divider.png")

    print(f"\nDone. {len(CHAPTERS)} chapter headers + 1 divider saved to {OUT_DIR}")


if __name__ == "__main__":
    main()
