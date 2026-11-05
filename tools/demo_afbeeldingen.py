"""Maakt 10 herkenbare demo-afbeeldingen in Triami-stijl (theme/triami/assets/img/demo/).
Elke afbeelding draagt duidelijk 'DEMO-FOTO' en een onderwerp, zodat ze in de editor
eenvoudig door echte foto's te vervangen zijn (blok selecteren → Vervangen)."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "theme/triami/assets/img/demo"
OUT.mkdir(parents=True, exist_ok=True)
FONTS = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
W, H = 1600, 1000

ROOD, DONKER, ZWART, TINT = (237, 30, 36), (196, 21, 27), (17, 17, 17), (253, 232, 232)

DEMO = [
    ("zwemmen", "Zwemtraining", "Techniek en conditie in het bad", "golven"),
    ("fietsen", "Samen fietsen", "Samen uit, samen thuis", "weg"),
    ("hardlopen", "Looptraining", "Met loopscholing op de baan", "baan"),
    ("groepsfoto", "Groepsfoto", "Triamisten bij elkaar", "groep"),
    ("trainingsweekend", "Trainingsweekend", "Elk jaar in april", "bergen"),
    ("start2tri", "Start2Tri", "Je eerste triathlon", "finish"),
    ("teamcompetitie", "Teamcompetitie", "Samen tegen de rest van Nederland", "groep"),
    ("clubcompetitie", "Clubcompetitie", "Strijden om de wisselbeker", "baan"),
    ("clubkleding", "Clubkleding", "Trisuits in Triami-rood", "shirt"),
    ("kennismaken", "Kom kennismaken", "Train vrijblijvend een keer mee", "golven"),
]


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def achtergrond(soort):
    im = Image.new("RGB", (W, H), ZWART)
    d = ImageDraw.Draw(im)
    for y in range(H):  # zachte verticale gradient zwart → antraciet
        t = y / H
        c = tuple(int(17 + 28 * t) for _ in range(3))
        d.line([(0, y), (W, y)], fill=c)
    lijn = (70, 70, 70)
    if soort == "golven":
        for k in range(9):
            y0 = 420 + k * 60
            pts = [(x, y0 + 18 * __import__("math").sin(x / 90 + k)) for x in range(0, W + 20, 20)]
            d.line(pts, fill=lijn, width=6)
    elif soort == "weg":
        d.polygon([(700, 380), (900, 380), (1500, H), (100, H)], fill=(40, 40, 40))
        for k in range(8):
            y = 420 + k * 75
            w = 6 + k * 3
            d.rectangle([800 - w // 2, y, 800 + w // 2, y + 30 + k * 6], fill=(90, 90, 90))
    elif soort == "baan":
        for k in range(7):
            d.arc([-400 + k * 40, 300 + k * 40, W + 400 - k * 40, H + 900 - k * 40], 180, 360, fill=lijn, width=8)
    elif soort == "bergen":
        d.polygon([(0, H), (350, 450), (650, 700), (1000, 380), (1350, 650), (1600, 500), (1600, H)], fill=(40, 40, 40))
        d.line([(0, H - 120), (350, 450), (650, 700), (1000, 380), (1350, 650), (1600, 500)], fill=lijn, width=6)
    elif soort == "groep":
        for k in range(9):
            x = 160 + k * 160
            r = 70 + (k % 3) * 8
            d.ellipse([x - r // 2, 520 - r, x + r // 2, 520], fill=(55, 55, 55))
            d.rounded_rectangle([x - r // 2 - 20, 540, x + r // 2 + 20, H + 40], 40, fill=(48, 48, 48))
    elif soort == "finish":
        for k in range(12):
            for j in range(3):
                if (k + j) % 2 == 0:
                    d.rectangle([k * 140, 380 + j * 60, k * 140 + 140, 440 + j * 60], fill=(60, 60, 60))
    elif soort == "shirt":
        d.polygon([(560, 360), (700, 330), (800, 380), (900, 330), (1040, 360), (1140, 520), (1040, 560), (1040, 900), (560, 900), (560, 560), (460, 520)], fill=(60, 60, 60))
        d.rectangle([560, 600, 1040, 650], fill=DONKER)
    return im.filter(ImageFilter.GaussianBlur(1.2))


def hartslag(d, y):
    pts = [(0, y), (620, y), (660, y - 50), (700, y + 70), (740, y - 110), (780, y + 90), (820, y), (W, y)]
    d.line(pts, fill=ROOD, width=10, joint="curve")


for slug, titel, sub, soort in DEMO:
    im = achtergrond(soort)
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle([0, 0, W, H], fill=(0, 0, 0, 70))
    hartslag(d, 250)
    # label DEMO-FOTO
    lab = font("mont800.ttf", 44)
    tw = d.textlength("DEMO-FOTO", font=lab)
    d.rounded_rectangle([80, 80, 80 + tw + 64, 80 + 84], 14, fill=DONKER)
    d.text((112, 98), "DEMO-FOTO", font=lab, fill="white")
    # titel en ondertitel
    t = font("mont800.ttf", 120)
    d.text((80, 600), titel.upper(), font=t, fill="white")
    d.text((84, 760), sub, font=font("ss600.ttf", 56), fill=(235, 235, 235))
    d.text((84, 880), "Voorbeeldafbeelding · vervang door een echte foto", font=font("ss400.ttf", 36), fill=(200, 200, 200))
    im.save(OUT / f"{slug}.jpg", "JPEG", quality=78, optimize=True, progressive=True)
    print(slug, (OUT / f"{slug}.jpg").stat().st_size // 1024, "kB")
