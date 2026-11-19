#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news infographic, 1024x1024 PNG.
Written from scratch for make.fun news-image-20261119.
All five stories verified as happening / first reported on 19 Nov 2026."""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BG = (13, 22, 38)          # deep ink navy
PANEL = (22, 34, 56)       # panel navy
PANEL2 = (27, 42, 68)
WHITE = (245, 244, 238)
MUTED = (176, 188, 205)
GOLD = (232, 184, 74)
RED = (214, 48, 49)
INK = (10, 16, 28)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_O = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img, "RGBA")

# ---- subtle diagonal texture ----
for i in range(-H, W, 46):
    d.line([(i, 0), (i + H, H)], fill=(255, 255, 255, 5), width=1)

# ---- masthead ----
d.rectangle([0, 0, W, 8], fill=RED)
d.text((48, 34), "THE WORLD IN ONE DAY", font=F(SANS_B, 26), fill=GOLD)
d.text((48, 64), "THURSDAY 19 NOVEMBER 2026", font=F(SERIF_B, 42), fill=WHITE)
d.text((48, 128), "Five stories that defined the day  —  from Shenzhen to deep space",
       font=F(SANS_O, 22), fill=MUTED)
# date badge, top right
d.rounded_rectangle([852, 34, 976, 94], radius=10, fill=GOLD)
d.text((914, 42), "19", font=F(SERIF_B, 34), fill=INK, anchor="mt")
d.text((914, 74), "NOV", font=F(SANS_B, 15), fill=INK, anchor="mt")
d.line([(48, 168), (976, 168)], fill=GOLD, width=3)

def wrap(text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def panel(x, y, w, h, accent, kicker, headline, body, icon):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=PANEL)
    d.rounded_rectangle([x, y, x + w, y + 6], radius=3, fill=accent)
    d.rounded_rectangle([x, y + 3, x + w, y + 6], radius=0, fill=accent)
    d.text((x + 22, y + 20), kicker, font=F(SANS_B, 17), fill=accent)
    hf = F(SANS_B, 30)
    lines = wrap(headline, hf, w - 44)
    yy = y + 48
    for ln in lines:
        d.text((x + 22, yy), ln, font=hf, fill=WHITE)
        yy += 36
    bf = F(SANS, 19)
    blines = wrap(body, bf, w - 44)
    yy += 8
    for ln in blines:
        d.text((x + 22, yy), ln, font=bf, fill=MUTED)
        yy += 26
    icon(x, y, w, h, accent)

def icon_pos(x, y, w, h):
    """Top-right corner, beside the short kicker — never over text."""
    return x + w - 116, y + 12

# ---------- HERO: three presidents ----------
hx, hy, hw, hh = 48, 186, 928, 252
d.rounded_rectangle([hx, hy, hx + hw, hy + hh], radius=16, fill=(58, 24, 30))
d.rounded_rectangle([hx, hy, hx + hw, hy + 6], radius=3, fill=RED)
# three flag discs
cx, cy, r = 890, 322, 42
for i, (col, lab) in enumerate([((178, 34, 52), "US"), ((212, 160, 40), "CN"), ((40, 90, 170), "RU")]):
    x0 = cx - 190 + i * 95
    d.ellipse([x0 - r, cy - r, x0 + r, cy + r], fill=col, outline=WHITE, width=3)
    d.text((x0, cy), lab, font=F(SANS_B, 24), fill=WHITE, anchor="mm")
d.text((hx + 26, hy + 20), "SHENZHEN  ·  APEC SUMMIT", font=F(SANS_B, 17), fill=(255, 150, 140))
d.text((hx + 26, hy + 48), "THREE PRESIDENTS,", font=F(SERIF_B, 42), fill=WHITE)
d.text((hx + 26, hy + 96), "ONE ROOM", font=F(SERIF_B, 42), fill=GOLD)
body = ("Trump, Xi and Putin hold the first trilateral summit of the "
        "three leaders — nuclear arms, Ukraine, Iran and trade on the table.")
bf = F(SANS, 20)
yy = hy + 164
for ln in wrap(body, bf, 620):
    d.text((hx + 26, yy), ln, font=bf, fill=(228, 222, 210))
    yy += 27

# ---------- icons ----------
def icon_controller(x, y, w, h, accent):
    ox, oy = icon_pos(x, y, w, h)
    d.rounded_rectangle([ox, oy, ox + 84, oy + 46], radius=14, fill=accent)
    d.ellipse([ox + 16, oy + 16, ox + 30, oy + 30], fill=BG)
    d.ellipse([ox + 54, oy + 16, ox + 68, oy + 30], fill=BG)
    d.line([(ox + 23, oy + 12), (ox + 23, oy + 34)], fill=BG, width=4)
    d.line([(ox + 12, oy + 23), (ox + 34, oy + 23)], fill=BG, width=4)

def icon_chart(x, y, w, h, accent):
    ox, oy = icon_pos(x, y, w, h)
    pts = [(ox, oy + 40), (ox + 22, oy + 26), (ox + 44, oy + 32), (ox + 66, oy + 12), (ox + 88, oy + 2)]
    d.line(pts, fill=accent, width=5, joint="curve")
    d.ellipse([pts[-1][0] - 7, pts[-1][1] - 7, pts[-1][0] + 7, pts[-1][1] + 7], fill=accent)
    d.line([(ox, oy + 46), (ox + 92, oy + 46)], fill=MUTED, width=2)

def icon_handshake(x, y, w, h, accent):
    ox, oy = icon_pos(x, y, w, h)
    d.ellipse([ox, oy + 2, ox + 52, oy + 54], outline=accent, width=5)
    d.ellipse([ox + 40, oy + 2, ox + 92, oy + 54], outline=(255, 255, 255), width=5)

def icon_satellite(x, y, w, h, accent):
    ox, oy = icon_pos(x, y, w, h)
    for sx, sy in [(ox + 8, oy + 4), (ox + 60, oy + 0), (ox + 92, oy + 22), (ox + 20, oy + 30)]:
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=WHITE)
    d.line([(ox + 20, oy + 50), (ox + 52, oy + 24)], fill=accent, width=4)
    d.ellipse([ox + 44, oy + 16, ox + 68, oy + 40], fill=accent)
    d.polygon([(ox + 52, oy + 24), (ox + 78, oy + 4), (ox + 86, oy + 16), (ox + 60, oy + 36)], fill=(140, 170, 220))

# ---------- 2x2 grid ----------
gx, gy = 48, 458
gw, gh, gap = 456, 240, 16
panel(gx, gy, gw, gh, (168, 92, 214), "CULTURE  ·  GAMING",
      "VICE CITY OPENS",
      "Grand Theft Auto VI goes live worldwide, unlocking at midnight in "
      "each market after a 13-year wait. Pre-orders topped $1.5bn; critics score it 99.",
      icon_controller)
panel(gx + gw + gap, gy, gw, gh, (232, 120, 40), "TECH  ·  MARKETS",
      "AI GOES PUBLIC",
      "Anthropic debuts on Nasdaq as ANT, priced at $83 a share in an "
      "~$81bn IPO — the biggest AI listing yet, valuing the Claude maker above $1trn.",
      icon_chart)
panel(gx, gy + gh + gap, gw, gh, (232, 184, 74), "ASIA  ·  DEFENCE",
      "TOKYO'S 2+2",
      "India and Japan hold their fourth foreign-and-defence ministers' "
      "dialogue in Tokyo, deepening Indo-Pacific security and technology ties.",
      icon_handshake)
panel(gx + gw + gap, gy + gh + gap, gw, gh, (90, 160, 230), "SPACE  ·  SCIENCE",
      "ONE LIGHT-DAY AWAY",
      "NASA confirms Voyager 1 is one light-day from Earth — 25.9 billion "
      "km — the farthest any human-made object has ever flown.",
      icon_satellite)

# ---------- footer ----------
fy = 976
d.line([(48, fy - 8), (976, fy - 8)], fill=(60, 72, 96), width=1)
d.text((48, fy + 4), "SOURCES: REUTERS · BBC · THE HINDU · NASA · 19 NOV 2026",
       font=F(SANS_B, 15), fill=MUTED)
d.text((976, fy + 4), "make.fun  ·  news-image-20261119",
       font=F(SANS, 15), fill=MUTED, anchor="ra")

img.save("/home/hatch/workspace/makefun/news-image-20261119/entry.png",
         optimize=True)
import os
print("saved", os.path.getsize("/home/hatch/workspace/makefun/news-image-20261119/entry.png"), "bytes")
print(img.size)
