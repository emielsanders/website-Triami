#!/usr/bin/env python3
"""Maakt een WordPress Playground-blueprint met het thema en de pagina's inline (geen GitHub nodig).

Output: dist/blueprint-inline.json en dist/playground-link.html (pagina met knop die Playground opent).
"""
import json, base64, urllib.parse
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "theme" / "triami"

def tree(d: Path) -> dict:
    out = {}
    for p in sorted(d.iterdir()):
        if p.name.startswith(".") or p.name == "fonts": continue  # woff2 is binair, kan niet inline
        out[p.name] = tree(p) if p.is_dir() else p.read_text(encoding="utf-8")
    return out

wxr = (ROOT / "dist" / "triami-paginas-import.xml").read_text(encoding="utf-8")
files = tree(THEME)
# Demo zonder binaire fonts: fontFace uit theme.json halen, functions.php valt dan terug op Google Fonts.
tj = json.loads(files["theme.json"])
for ff in tj["settings"]["typography"]["fontFamilies"]:
    ff.pop("fontFace", None)
files["theme.json"] = json.dumps(tj, ensure_ascii=False)

bp = {
  "landingPage": "/", "login": True,
  "preferredVersions": {"php": "8.3", "wp": "latest"},
  "steps": [
    {"step": "installTheme", "themeData": {"resource": "literal:directory", "name": "triami", "files": files}, "options": {"activate": True}},
    {"step": "importWxr", "file": {"resource": "literal", "name": "triami-paginas-import.xml", "contents": wxr}},
    {"step": "setSiteOptions", "options": {"blogname": "Triami Triathlonvereniging", "blogdescription": "Dé triathlonvereniging van Deventer en omstreken", "permalink_structure": "/%postname%/", "timezone_string": "Europe/Amsterdam"}},
    {"step": "runPHP", "code": "<?php require '/wordpress/wp-load.php'; wp_delete_post(1,true); wp_delete_post(2,true); $n=get_page_by_path('nieuws'); if($n){update_option('page_for_posts',$n->ID);} flush_rewrite_rules();"}
  ]
}
js = json.dumps(bp, ensure_ascii=False, separators=(",", ":"))
(ROOT / "dist" / "blueprint-inline.json").write_text(js, encoding="utf-8")
b64 = base64.urlsafe_b64encode(js.encode("utf-8")).decode()
url = "https://playground.wordpress.net/#" + urllib.parse.quote(js, safe="")
print(f"blueprint {len(js)//1024} kB, url {len(url)//1024} kB")
(ROOT / "dist" / "playground-url.txt").write_text(url)
