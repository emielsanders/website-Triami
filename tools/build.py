#!/usr/bin/env python3
"""Bouwt de uitleverbare bestanden van de Triami-website.

- dist/triami.zip                 : het thema, klaar voor 'Thema uploaden' in WordPress
- dist/triami-paginas-import.xml  : WXR-import met alle pagina's uit content/pages/

Gebruik:  python3 tools/build.py
"""
from __future__ import annotations

import datetime as dt
import html
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "theme" / "triami"
PAGES = ROOT / "content" / "pages"
DIST = ROOT / "dist"
SITE = "https://www.triami.nl"


def read_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit(f"Geen front matter in {path.name}")
    meta = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    meta.setdefault("slug", path.stem)
    meta.setdefault("order", "0")
    meta["content"] = m.group(2).strip()
    return meta


def build_wxr(pages: list[dict]) -> str:
    now = dt.datetime.now(dt.timezone.utc)
    pub = now.strftime("%a, %d %b %Y %H:%M:%S +0000")
    stamp = now.strftime("%Y-%m-%d %H:%M:%S")
    ids = {p["slug"]: 100 + i for i, p in enumerate(pages)}
    items = []
    for p in pages:
        parent = ids.get(p.get("parent", ""), 0)
        items.append(
            f"""
    <item>
        <title><![CDATA[{p['title']}]]></title>
        <link>{SITE}/{p['slug']}/</link>
        <pubDate>{pub}</pubDate>
        <dc:creator><![CDATA[admin]]></dc:creator>
        <guid isPermaLink="false">{SITE}/?page_id={ids[p['slug']]}</guid>
        <description></description>
        <content:encoded><![CDATA[{p['content']}]]></content:encoded>
        <excerpt:encoded><![CDATA[]]></excerpt:encoded>
        <wp:post_id>{ids[p['slug']]}</wp:post_id>
        <wp:post_date><![CDATA[{stamp}]]></wp:post_date>
        <wp:post_date_gmt><![CDATA[{stamp}]]></wp:post_date_gmt>
        <wp:comment_status><![CDATA[closed]]></wp:comment_status>
        <wp:ping_status><![CDATA[closed]]></wp:ping_status>
        <wp:post_name><![CDATA[{p['slug']}]]></wp:post_name>
        <wp:status><![CDATA[publish]]></wp:status>
        <wp:post_parent>{parent}</wp:post_parent>
        <wp:menu_order>{p['order']}</wp:menu_order>
        <wp:post_type><![CDATA[page]]></wp:post_type>
        <wp:post_password><![CDATA[]]></wp:post_password>
        <wp:is_sticky>0</wp:is_sticky>
    </item>"""
        )
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
    xmlns:content="http://purl.org/rss/1.0/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:wp="http://wordpress.org/export/1.2/">
<channel>
    <title>Triami Triathlonvereniging</title>
    <link>{SITE}</link>
    <description>Dé triathlonvereniging van Deventer en omstreken</description>
    <pubDate>{pub}</pubDate>
    <language>nl-NL</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:base_site_url>{SITE}</wp:base_site_url>
    <wp:base_blog_url>{SITE}</wp:base_blog_url>
    <wp:author><wp:author_id>1</wp:author_id><wp:author_login><![CDATA[admin]]></wp:author_login><wp:author_email><![CDATA[secretaris@triami.nl]]></wp:author_email><wp:author_display_name><![CDATA[Triami]]></wp:author_display_name><wp:author_first_name><![CDATA[]]></wp:author_first_name><wp:author_last_name><![CDATA[]]></wp:author_last_name></wp:author>
    <generator>triami-website/tools/build.py</generator>
{''.join(items)}
</channel>
</rss>
"""


def build_zip() -> Path:
    DIST.mkdir(exist_ok=True)
    out = DIST / "triami.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(THEME.rglob("*")):
            if f.is_file() and ".DS_Store" not in f.name:
                z.write(f, "triami/" + str(f.relative_to(THEME)))
    return out


def main() -> None:
    pages = sorted((read_page(p) for p in PAGES.glob("*.html")), key=lambda p: int(p["order"]))
    DIST.mkdir(exist_ok=True)
    xml = DIST / "triami-paginas-import.xml"
    xml.write_text(build_wxr(pages), encoding="utf-8")
    z = build_zip()
    print(f"{xml.relative_to(ROOT)}: {len(pages)} pagina's")
    print(f"{z.relative_to(ROOT)}: {z.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
