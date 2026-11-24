#!/usr/bin/env python3
"""Render entry.png for news-image-20261123: Monday 23 November 2026 in one image.

Six verified stories of that day, drawn with PIL primitives only. Run:
    python3 draw.py            # writes entry.png next to this file
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

NAVY = (20, 33, 61)
PAPER = (247, 243, 234)
AMBER = (242, 160, 7)
INK = (24, 28, 36)
GREY = (84, 90, 100)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)
LINE = (205, 205, 198)

GREEN = (27, 122, 61)
STEEL = (46, 94, 140)
FIRE = (192, 57, 43)
CRIMSON = (142, 31, 47)
TEAL = (14, 124, 123)
PLUM = (91, 75, 138)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
REG = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit in `width` px."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, lines, fnt, color, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


# ---------------------------------------------------------------- icons
def icon_chip(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(232, 245, 233))
    d.rounded_rectangle([cx - 52, cy - 40, cx + 52, cy + 40], 10, fill=GREEN)
    for i in range(3):
        yy = cy - 24 + i * 24
        d.line([cx - 66, yy, cx - 52, yy], fill=GREEN, width=5)
        d.line([cx + 52, yy, cx + 66, yy], fill=GREEN, width=5)
    d.polygon([(cx + 8, cy - 26), (cx - 12, cy + 6), (cx + 2, cy + 6),
               (cx - 8, cy + 28), (cx + 14, cy - 4), (cx, cy - 4)],
              fill=AMBER)


def icon_ship(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(226, 238, 247))
    d.polygon([(cx - 58, cy - 6), (cx + 58, cy - 6), (cx + 44, cy + 22),
               (cx - 44, cy + 22)], fill=STEEL)
    d.rectangle([cx - 26, cy - 30, cx - 8, cy - 6], fill=STEEL)
    d.rectangle([cx - 18, cy - 52, cx - 14, cy - 30], fill=STEEL)
    d.line([cx - 18, cy - 52, cx + 6, cy - 40], fill=STEEL, width=4)
    for yy in (cy + 34, cy + 48):
        d.arc([cx - 62, yy - 10, cx - 20, yy + 10], 0, 180, fill=STEEL, width=4)
        d.arc([cx - 10, yy - 10, cx + 32, yy + 10], 0, 180, fill=STEEL, width=4)
        d.arc([cx + 22, yy - 10, cx + 64, yy + 10], 0, 180, fill=STEEL, width=4)
    d.rectangle([cx + 34, cy - 58, cx + 54, cy - 46], fill=INK)
    d.ellipse([cx + 30, cy - 62, cx + 38, cy - 54], fill=INK)
    d.ellipse([cx + 50, cy - 62, cx + 58, cy - 54], fill=INK)


def icon_factory(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(253, 235, 228))
    d.rectangle([cx - 58, cy - 6, cx + 58, cy + 44], fill=(74, 78, 86))
    d.polygon([(cx - 58, cy - 6), (cx - 38, cy - 26), (cx - 18, cy - 6),
               (cx + 2, cy - 26), (cx + 22, cy - 6), (cx + 42, cy - 26),
               (cx + 58, cy - 6)], fill=(74, 78, 86))
    d.rectangle([cx + 34, cy - 52, cx + 50, cy - 6], fill=(74, 78, 86))
    for xx in (-40, -8, 24):
        d.rectangle([cx + xx, cy + 8, cx + xx + 16, cy + 24], fill=AMBER)
    d.polygon([(cx - 14, cy - 58), (cx - 30, cy - 18), (cx - 8, cy - 26),
               (cx - 2, cy - 48), (cx + 10, cy - 22), (cx + 26, cy - 34),
               (cx + 12, cy - 66)], fill=(230, 126, 34))
    d.polygon([(cx - 2, cy - 52), (cx - 12, cy - 24), (cx + 2, cy - 30),
               (cx + 10, cy - 52)], fill=(247, 220, 111))


def icon_sanction(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 231, 233))
    d.ellipse([cx - 56, cy - 56, cx + 56, cy + 56], outline=CRIMSON, width=10)
    d.line([cx - 40, cy + 40, cx + 40, cy - 40], fill=CRIMSON, width=10)
    d.text((cx, cy - 4), "$", font=BOLD(64), fill=CRIMSON, anchor="mm")


def icon_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(224, 242, 240))
    d.ellipse([cx - 54, cy - 54, cx + 54, cy + 54], fill=(38, 132, 190))
    d.ellipse([cx - 38, cy - 34, cx - 2, cy - 6], fill=(46, 160, 90))
    d.ellipse([cx + 6, cy + 6, cx + 38, cy + 34], fill=(46, 160, 90))
    d.ellipse([cx + 18, cy - 40, cx + 42, cy - 18], fill=(46, 160, 90))
    d.arc([cx - 54, cy - 54, cx + 54, cy + 54], 300, 60, fill=(20, 60, 100), width=4)
    d.line([cx - 56, cy + 56, cx + 56, cy - 56], fill=CRIMSON, width=9)
    d.ellipse([cx - 66, cy - 66, cx + 66, cy + 66], outline=CRIMSON, width=6)


def icon_exam(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(238, 232, 247))
    d.rounded_rectangle([cx - 44, cy - 56, cx + 44, cy + 56], 6,
                        fill=WHITE, outline=PLUM, width=4)
    for i in range(4):
        yy = cy - 32 + i * 18
        d.line([cx - 30, yy, cx + 30, yy], fill=(150, 150, 160), width=4)
    d.line([cx - 38, cy + 36, cx - 14, cy + 52], fill=CRIMSON, width=8)
    d.line([cx - 14, cy + 52, cx + 40, cy + 8], fill=CRIMSON, width=8)


ICONS = [icon_chip, icon_ship, icon_factory, icon_sanction, icon_globe, icon_exam]

STORIES = [
    ("BUSINESS  ·  USA", GREEN,
     "HUANG IS BACK AT NVIDIA",
     "Board reinstates Jensen Huang as CEO; shares soar about 30%."),
    ("WAR  ·  LIBYA", STEEL,
     "UKRAINE SINKS RUSSIAN WARSHIP",
     "Sea drones sink corvette Merkury in Benghazi; cargo ship hit too."),
    ("DISASTER  ·  INDONESIA", FIRE,
     "24 DEAD IN FACTORY FIRE",
     "Cikande candy plant blaze; about 30 workers still missing."),
    ("MIDDLE EAST  ·  IRAN", CRIMSON,
     "US SLAPS IRAN WITH NEW SANCTIONS",
     "Trump warns of fresh strikes after Jan 1 if talks collapse."),
    ("CLIMATE  ·  COP31", TEAL,
     "CLIMATE SUMMIT ENDS WITH NO DEAL",
     "Talks collapse as fossil-fuel wording is blocked; EU walks away."),
    ("ASIA  ·  SOUTH KOREA", PLUM,
     "MINISTER QUITS OVER AI CHEATING",
     "Education chief resigns after exam-cheating scandal."),
]


def render(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=AMBER)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=BOLD(56))
    d.text(((W - tw) / 2, 22), title, font=BOLD(56), fill=WHITE)
    date = "MONDAY  ·  23 NOVEMBER 2026"
    dw = d.textlength(date, font=BOLD(38))
    d.text(((W - dw) / 2, 94), date, font=BOLD(38), fill=AMBER)

    # ---- six story cards, 2 columns x 3 rows
    gx, gy = 10, 166
    cw, ch, gap = 496, 264, 10
    for i, (kicker, accent, head, sub) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (cw + gap)
        y = gy + row * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], 12, fill=CARD, outline=LINE, width=2)
        d.rounded_rectangle([x, y, x + cw, y + 36], 12, fill=accent)
        d.rectangle([x, y + 24, x + cw, y + 36], fill=accent)
        d.text((x + 14, y + 6), kicker, font=BOLD(19), fill=WHITE)

        ix, iy = x + 78, y + 36 + (ch - 36) // 2
        ICONS[i](d, ix, iy, 66)

        tx = x + 164
        twd = cw - 164 - 16
        head_lines = wrap(d, head, BOLD(29), twd)[:3]
        yy = draw_text_block(d, tx, y + 52, head_lines, BOLD(29), INK, 35)
        sub_lines = wrap(d, sub, REG(20), twd)[:3]
        draw_text_block(d, tx, yy + 8, sub_lines, REG(20), GREY, 26)

    # ---- footer
    foot = "All six stories happened or were first reported on Monday 23 November 2026."
    fw = d.textlength(foot, font=REG(17))
    d.text(((W - fw) / 2, 990), foot, font=REG(17), fill=GREY)

    img.save(path, "PNG", optimize=True)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    render(out)
    print("wrote", out, os.path.getsize(out), "bytes")
