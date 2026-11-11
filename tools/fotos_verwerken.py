"""Verwerkt clubfoto's (uit de Mailchimp-bibliotheek) voor de website: rechtop zetten, 16:10 uitsnijden,
maximaal 1600 px breed, licht verbeteren (contrast, kleur, verscherping) en alle metadata (EXIF/GPS) weglaten.
Gebruik: python3 tools/fotos_verwerken.py <bronmap>"""
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

BRON = Path(sys.argv[1])
DOEL = Path(__file__).resolve().parents[1] / "theme/triami/assets/img/foto"
DOEL.mkdir(parents=True, exist_ok=True)

# bron-id -> (bestandsnaam, verticale focus 0..1)
FOTOS = {
    "17": ("zwemmen-onder-water", .5), "242": ("fietsen-langs-het-water", .5), "0": ("looptraining-baan", .5),
    "130": ("zwembad-van-boven", .5), "62": ("zwemtraining-buitenbad", .55), "169": ("fietsen-herfst", .6),
    "1": ("groep-atletiekbaan", .55), "48": ("open-water-groep", .55), "342": ("open-water-avond", .5),
    "25": ("open-water-zonsondergang", .6), "319": ("open-water-meer", .55), "50": ("trainingsweekend-heuvelland", .6),
    "35": ("trainingsweekend-groep", .5), "156": ("trainingsweekend-tunnel", .6), "76": ("trainingsweekend-mountainbike", .55),
    "6": ("hardlopen-heide", .62), "14": ("groep-crosstriathlon", .6), "63": ("groepsfoto-fietsen", .55),
    "286": ("crossloop-heide", .6), "114": ("teamcompetitie-finish", .5),
}

for n, (naam, fy) in FOTOS.items():
    p = next(BRON.glob(n + ".*"))
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    w, h = im.size
    tw = min(1600, w if w / h <= 1.6 else int(h * 1.6))
    im = ImageOps.fit(im, (tw, round(tw / 1.6)), Image.LANCZOS, centering=(.5, fy))
    # lichte verbetering: half-om-half automatisch contrast, iets meer kleur, milde verscherping
    im = Image.blend(im, ImageOps.autocontrast(im, cutoff=.5), .5)
    im = ImageEnhance.Color(im).enhance(1.06)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=55, threshold=3))
    out = DOEL / f"{naam}.jpg"
    im.save(out, "JPEG", quality=76, optimize=True, progressive=True)  # zonder exif = geen GPS of camera-info
    print(f"{naam:34s} {im.size[0]}x{im.size[1]} {out.stat().st_size // 1024} kB")
