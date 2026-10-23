#!/usr/bin/env python3
"""Prepare the public Shivam Clinic files for Cloudflare Pages Direct Upload."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
from urllib.parse import unquote, urlsplit
from check_site import validate_site

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "shivamclinic.com"
PUBLIC_TYPES = {".html", ".css", ".js", ".json", ".svg", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".ico", ".woff", ".woff2", ".ttf"}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links.extend(value for name, value in attrs if name in {"src", "href", "poster"} and value)


def main():
    files = [p for p in ROOT.iterdir() if p.is_file() and (p.suffix in PUBLIC_TYPES or p.name in {"robots.txt", "sitemap.xml", "_headers", "_redirects"})]
    for directory in (ROOT / "assets", ROOT / "blog"):
        files.extend(p for p in directory.rglob("*") if p.is_file() and p.suffix in PUBLIC_TYPES)
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    for source in files:
        if source.is_symlink() or not source.resolve().is_relative_to(ROOT):
            raise ValueError(f"Public asset must be inside the site directory: {source}")
        if source.stat().st_size > 25 * 1024 * 1024:
            raise ValueError(f"Asset exceeds the Pages 25 MiB limit: {source}")
        destination = OUTPUT / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    errors = []
    for page in OUTPUT.rglob("*.html"):
        parser = Links()
        parser.feed(page.read_text())
        for link in parser.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path = unquote(parsed.path)
            target = OUTPUT / path.lstrip("/") if path.startswith("/") else page.parent / path
            if not target.exists():
                errors.append(f"{page.relative_to(OUTPUT)}: {link}")
    if errors:
        raise ValueError("Missing public files:\n" + "\n".join(errors))
    validate_site(OUTPUT)
    print(f"Prepared {len(files)} public files in {OUTPUT}")
    print("Local page and asset links passed.")


if __name__ == "__main__":
    main()
