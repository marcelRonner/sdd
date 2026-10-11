#!/usr/bin/env python3
"""Build a standalone HTML deck (and optionally a PDF) from the slide sources.

The sources in ./source are the files of the Claude Slides artifact
(deck.json + one <section> per slide). This script stitches them into one
HTML page with 1920x1080 slides and can print that page to PDF.

Usage:
    python3 build_deck.py                      # writes sdd-to-idsd.html
    python3 build_deck.py --pdf                # also writes sdd-to-idsd.pdf
    python3 build_deck.py --pdf --font-dir DIR # use local .woff2 files for the PDF
"""
import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "source"

ARROW_SVG = (
    '<svg width="{w}" height="{h}" viewBox="0 0 30 18" style="flex:none;align-self:center" aria-hidden="true">'
    '<path d="M0 6h18V0l12 9-12 9v-6H0z" fill="{c}"/></svg>'
)

BASE_CSS = """
*{box-sizing:border-box;margin:0}
html,body{background:#2b2b2b}
body{display:flex;flex-direction:column;align-items:center;gap:24px;padding:24px 0}
section{position:relative;width:1920px;height:1080px;overflow:hidden;flex:none}
h1,h2,h3,p{margin:0}
ul,ol{padding-left:1.2em}
a{color:#1F5FA8}
table{border-collapse:collapse;width:100%}
th,td{padding:0.35em 0.6em;border-bottom:1px solid #D9D4C7;text-align:left;vertical-align:top}
aside{display:none}
@media print{
  @page{size:1920px 1080px;margin:0}
  html,body{background:none;padding:0;gap:0;display:block}
  section{page-break-after:always;break-after:page}
}
"""


def arrow(match: re.Match) -> str:
    style = match.group(1)
    w = re.search(r"width:(\d+)px", style)
    h = re.search(r"height:(\d+)px", style)
    c = re.search(r"background:(#[0-9A-Fa-f]{3,8})", style)
    return ARROW_SVG.format(w=w.group(1) if w else 30, h=h.group(1) if h else 18, c=c.group(1) if c else "#5C6880")


def build_html(font_css: str) -> str:
    deck = json.loads((SRC / "deck.json").read_text())
    links = "\n".join(
        f'<link rel="stylesheet" href="{f["href"]}">' for f in deck["faces"].values() if "href" in f
    )
    slides = []
    for sid in deck["order"]:
        html = (SRC / "slides" / f"{sid}.html").read_text()
        html = re.sub(r'<x-shape kind="arrow-right" style="([^"]*)"></x-shape>', arrow, html)
        slides.append(html)
    return (
        "<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
        f"<title>{deck['title']}</title>\n{links}\n<style>{font_css}{BASE_CSS}</style></head>\n<body>\n"
        + "\n".join(slides)
        + "\n</body></html>\n"
    )


def local_font_css(font_dir: Path) -> str:
    faces = [
        ("IBM Plex Sans", "ibm-plex-sans-latin-400-normal.woff2", "400"),
        ("IBM Plex Sans", "ibm-plex-sans-latin-500-normal.woff2", "500"),
        ("IBM Plex Sans", "ibm-plex-sans-latin-600-normal.woff2", "600"),
        ("Source Serif 4", "source-serif-4-latin-wght-normal.woff2", "200 900"),
    ]
    css = []
    for family, name, weight in faces:
        path = next(font_dir.rglob(name), None)
        if path:
            css.append(f'@font-face{{font-family:"{family}";src:url("{path.as_uri()}");font-weight:{weight}}}')
    return "".join(css)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--font-dir", type=Path)
    ap.add_argument("--name", default="sdd-to-idsd")
    args = ap.parse_args()

    out_html = HERE / f"{args.name}.html"
    out_html.write_text(build_html(""))
    print("wrote", out_html)

    if args.pdf:
        from playwright.sync_api import sync_playwright

        font_css = local_font_css(args.font_dir) if args.font_dir else ""
        tmp = HERE / f".{args.name}.print.html"
        tmp.write_text(build_html(font_css))
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1920, "height": 1080})
            page.goto(tmp.as_uri(), wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            page.pdf(path=str(HERE / f"{args.name}.pdf"), width="1920px", height="1080px",
                     print_background=True, prefer_css_page_size=True)
            browser.close()
        tmp.unlink()
        print("wrote", HERE / f"{args.name}.pdf")


if __name__ == "__main__":
    main()
