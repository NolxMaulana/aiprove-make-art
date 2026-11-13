#!/usr/bin/env python3
"""Original AIProve poster: broadsheet-meets-terminal. No external assets."""
from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = os.path.expanduser("~/workspace/aiprove/make-art-aiprove")
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_R = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
MONO_R = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

PAPER = (246, 241, 227)
INK = (17, 17, 17)
RED = (212, 43, 30)
GREEN = (51, 209, 122)
DARK = (16, 20, 24)
DARK2 = (28, 34, 40)
CREAM = (250, 246, 232)
AMBER = (255, 176, 32)
CYAN = (55, 200, 232)

def F(path, size):
    return ImageFont.truetype(path, size)

def center(d, y, text, font, fill, x0=0, x1=2400):
    b = d.textbbox((0, 0), text, font=font)
    w = b[2] - b[0]
    d.text(((x0 + x1 - w) / 2 - b[0], y), text, font=font, fill=fill)
    return y + (b[3] - b[1])

def wrap_center(d, cx, y, text, font, fill, max_w):
    # simple word wrap, centred lines
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textbbox((0, 0), t, font=font)[2] <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    for ln in lines:
        b = d.textbbox((0, 0), ln, font=font)
        d.text((cx - (b[2]-b[0])/2 - b[0], y), ln, font=font, fill=fill)
        y += int((b[3]-b[1]) * 1.35)
    return y

def draw_mascot(d, cx, cy, s=1.0):
    """Pru, the proof-bot: round cream head, dark screen face, check eye, antenna."""
    # antenna
    d.line([(cx, cy-210*s), (cx, cy-285*s)], fill=INK, width=int(14*s))
    d.ellipse([cx-28*s, cy-318*s, cx+28*s, cy-262*s], fill=RED, outline=INK, width=int(6*s))
    d.ellipse([cx-12*s, cy-302*s, cx+12*s, cy-278*s], fill=(255,255,255))
    # ears / side bolts
    d.ellipse([cx-235*s, cy-40*s, cx-185*s, cy+10*s], fill=AMBER, outline=INK, width=int(6*s))
    d.ellipse([cx+185*s, cy-40*s, cx+235*s, cy+10*s], fill=AMBER, outline=INK, width=int(6*s))
    # head
    d.rounded_rectangle([cx-210*s, cy-190*s, cx+210*s, cy+190*s], radius=int(90*s), fill=CREAM, outline=INK, width=int(10*s))
    # screen face
    d.rounded_rectangle([cx-165*s, cy-140*s, cx+165*s, cy+90*s], radius=int(36*s), fill=DARK, outline=INK, width=int(6*s))
    # check mark (the eye / verdict)
    d.line([(cx-105*s, cy-45*s), (cx-35*s, cy+25*s), (cx+115*s, cy-95*s)], fill=GREEN, width=int(28*s), joint="curve")
    # cursor block under check
    d.rectangle([cx-115*s, cy+28*s, cx-55*s, cy+58*s], fill=CYAN)
    d.rectangle([cx-35*s, cy+28*s, cx+115*s, cy+58*s], fill=(120, 130, 140))
    # mouth grille / body hint below face
    d.rounded_rectangle([cx-110*s, cy+118*s, cx+110*s, cy+168*s], radius=int(18*s), fill=(255,255,255), outline=INK, width=int(5*s))
    for i in range(3):
        x = cx - 70*s + i*70*s
        d.line([(x, cy+132*s), (x, cy+154*s)], fill=INK, width=int(8*s))
    # small name tag
    d.rounded_rectangle([cx-95*s, cy+205*s, cx+95*s, cy+258*s], radius=int(20*s), fill=RED, outline=INK, width=int(5*s))
    f = F(MONO, int(38*s))
    b = d.textbbox((0,0), "PRU", font=f)
    d.text((cx-(b[2]-b[0])/2-b[0], cy+210*s), "PRU", font=f, fill=(255,255,255))

def make_poster(w=2400, h=3000, path="poster.png"):
    img = Image.new("RGB", (w, h), PAPER)
    d = ImageDraw.Draw(img)
    # subtle paper texture: faint dots grid
    for x in range(0, w, 48):
        for y in range(0, h, 48):
            d.point((x, y), fill=(238, 232, 214))
    # outer frame
    d.rectangle([36, 36, w-37, h-37], outline=INK, width=10)
    d.rectangle([58, 58, w-59, h-59], outline=INK, width=3)

    y = 105
    y = center(d, y, "T H E   A G E N T   G A Z E T T E", F(MONO, 46), INK) + 28
    d.line([(150, y), (w-150, y)], fill=INK, width=4); y += 22
    # masthead
    y = center(d, y, "AIPROVE", F(SERIF, 380), INK) + 150
    # red rule under masthead
    d.rectangle([150, y, w-150, y+14], fill=RED); y += 42
    y = center(d, y, "The proof is the product.", F(SERIF_I, 78), INK) + 40
    # double rule
    d.line([(150, y), (w-150, y)], fill=INK, width=6); y += 12
    d.line([(150, y), (w-150, y)], fill=INK, width=3); y += 48
    # headline
    y = center(d, y, "DON'T TAKE THEIR WORD FOR IT.", F(SANS, 96), INK) + 18
    y = center(d, y, "MAKE THEM PROVE IT.", F(SANS, 96), RED) + 60

    # terminal window
    tx0, ty0, tx1, ty1 = 170, y, w-170, y+920
    d.rounded_rectangle([tx0, ty0, tx1, ty1], radius=36, fill=DARK, outline=INK, width=6)
    d.rounded_rectangle([tx0, ty0, tx1, ty0+92], radius=36, fill=DARK2, outline=INK, width=4)
    d.rectangle([tx0, ty0+46, tx1, ty0+92], fill=DARK2)
    for i, c in enumerate([(212,43,30), (255,176,32), (51,209,122)]):
        d.ellipse([tx0+42+i*62, ty0+30, tx0+78+i*62, ty0+66], fill=c, outline=INK, width=3)
    f = F(MONO, 40)
    d.text((tx0+300, ty0+24), "aiprove — verify", font=f, fill=(200,205,210))
    # mascot inside terminal, left
    draw_mascot(d, tx0+330, ty0+470, s=0.82)
    # terminal text, right of mascot
    lx = tx0+640
    ly = ty0+190
    lines = [
        ("$ ", (255,255,255), "aiprove verify --agent", (255,255,255)),
        ("> ", GREEN, "claim ........ CHECKED", (230,235,240)),
        ("> ", GREEN, "proof ........ VALID", (230,235,240)),
        ("> ", GREEN, "verdict ...... PROVEN", (230,235,240)),
    ]
    mf = F(MONO, 54); mf2 = F(MONO, 54)
    for prompt, pc, text, tc in lines:
        d.text((lx, ly), prompt, font=mf, fill=pc)
        pw = d.textbbox((0,0), prompt, font=mf)[2]
        d.text((lx+pw, ly), text, font=mf2, fill=tc)
        ly += 92
    # big check badge in terminal bottom right
    d.ellipse([tx1-330, ty1-260, tx1-110, ty1-40], fill=GREEN, outline=INK, width=6)
    d.line([(tx1-285, ty1-150), (tx1-235, ty1-100), (tx1-155, ty1-190)], fill=DARK, width=22, joint="curve")
    d.text((lx, ly+18), "$ prove it.  _", font=F(MONO, 50), fill=CYAN)
    y = ty1 + 70


    # three columns
    cols = [
        ("VERIFY", "Every claim gets\nchecked in the open."),
        ("BUILD", "Agents ship real work.\nThe sandbox decides."),
        ("EARN", "Proof that holds up\nis proof that pays."),
    ]
    col_w = (w-300)//3
    cy0 = y
    for i, (t, body) in enumerate(cols):
        cx = 150 + i*col_w + col_w//2
        if i: d.line([(150+i*col_w, cy0+10), (150+i*col_w, cy0+270)], fill=INK, width=3)
        center(d, cy0, t, F(SANS, 62), INK, x0=150+i*col_w, x1=150+(i+1)*col_w)
        wrap_center(d, cx, cy0+105, body, F(SERIF_R, 52), INK, col_w-70)
    y = cy0 + 320
    d.line([(150, y), (w-150, y)], fill=INK, width=4); y += 36
    y = center(d, y, "AIPROVE.FUN  •  PROOF OVER PROMISE", F(MONO, 48), INK) + 30
    y = center(d, y, "NO HYPE, JUST PROOF.", F(MONO, 40), RED) + 70
    d.line([(150, y), (w-150, y)], fill=INK, width=6); y += 12
    d.line([(150, y), (w-150, y)], fill=INK, width=3); y += 45
    y = center(d, y, "IN THIS ISSUE", F(SANS, 58), INK) + 45
    issues = [
        ("01", "Claims, checked line by line."),
        ("02", "Work that runs, not work that promises."),
        ("03", "A verdict you can read, and re-run."),
    ]
    for num, txt in issues:
        d.text((170, y), num, font=F(MONO, 48), fill=RED)
        d.text((300, y), txt, font=F(SERIF_R, 54), fill=INK)
        y += 80
    img.save(os.path.join(OUT, path), "PNG", optimize=True)
    print(path, img.size, os.path.getsize(os.path.join(OUT, path)))

def make_square():
    # Square variant: reuse poster art by rendering a 2400x2400 crop-style version
    # Simpler: open poster, centre-crop top portion is not ideal, so build a compact square
    # using the same elements via a fresh canvas.
    w = h = 2400
    img = Image.new("RGB", (w, h), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([36, 36, w-37, h-37], outline=INK, width=10)
    d.rectangle([58, 58, w-59, h-59], outline=INK, width=3)
    y = 100
    y = center(d, y, "T H E   A G E N T   G A Z E T T E", F(MONO, 42), INK, x1=w) + 24
    d.line([(150, y), (w-150, y)], fill=INK, width=4); y += 20
    y = center(d, y, "AIPROVE", F(SERIF, 340), INK, x1=w) + 135
    d.rectangle([150, y, w-150, y+14], fill=RED); y += 40
    y = center(d, y, "MAKE THEM PROVE IT.", F(SANS, 88), RED, x1=w) + 55
    tx0, ty0, tx1, ty1 = 170, y, w-170, y+820
    d.rounded_rectangle([tx0, ty0, tx1, ty1], radius=36, fill=DARK, outline=INK, width=6)
    d.rounded_rectangle([tx0, ty0, tx1, ty0+88], radius=36, fill=DARK2, outline=INK, width=4)
    d.rectangle([tx0, ty0+44, tx1, ty0+88], fill=DARK2)
    for i, c in enumerate([(212,43,30), (255,176,32), (51,209,122)]):
        d.ellipse([tx0+42+i*62, ty0+28, tx0+78+i*62, ty0+64], fill=c, outline=INK, width=3)
    d.text((tx0+300, ty0+22), "aiprove — verify", font=F(MONO, 38), fill=(200,205,210))
    draw_mascot(d, tx0+330, ty0+440, s=0.80)
    lx = tx0+640; ly = ty0+180
    for prompt, text in [("$ ", "aiprove verify"), ("> ", "proof ... VALID"), ("> ", "verdict ... PROVEN")]:
        d.text((lx, ly), prompt, font=F(MONO, 52), fill=GREEN if prompt=="> " else (255,255,255))
        pw = d.textbbox((0,0), prompt, font=F(MONO, 52))[2]
        d.text((lx+pw, ly), text, font=F(MONO, 52), fill=(230,235,240))
        ly += 88
    d.ellipse([tx1-320, ty1-250, tx1-110, ty1-40], fill=GREEN, outline=INK, width=6)
    d.line([(tx1-275, ty1-145), (tx1-228, ty1-98), (tx1-152, ty1-182)], fill=DARK, width=20, joint="curve")
    y = ty1 + 70
    y = center(d, y, "The proof is the product.", F(SERIF_I, 72), INK, x1=w) + 55
    cols = [("VERIFY", "Every claim gets\nchecked in the open."), ("BUILD", "Agents ship real work.\nThe sandbox decides."), ("EARN", "Proof that holds up\nis proof that pays.")]
    col_w = (w-300)//3
    cy0 = y
    for i, (tt, body) in enumerate(cols):
        cx = 150 + i*col_w + col_w//2
        if i: d.line([(150+i*col_w, cy0+10), (150+i*col_w, cy0+260)], fill=INK, width=3)
        center(d, cy0, tt, F(SANS, 56), INK, x0=150+i*col_w, x1=150+(i+1)*col_w)
        wrap_center(d, cx, cy0+95, body, F(SERIF_R, 46), INK, col_w-60)
    y = cy0 + 310
    d.line([(150, y), (w-150, y)], fill=INK, width=4); y += 34
    center(d, y, "AIPROVE.FUN  •  NO HYPE, JUST PROOF.", F(MONO, 44), INK, x1=w)
    img.save(os.path.join(OUT, "poster-square.png"), "PNG", optimize=True)
    print("poster-square.png", img.size, os.path.getsize(os.path.join(OUT, "poster-square.png")))

if __name__ == "__main__":
    make_poster()
    make_square()
