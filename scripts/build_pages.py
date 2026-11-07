import argparse
import os
from pathlib import Path
import re
import shutil
import sys
from html import unescape
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parent.parent
PAGE_NAMES = ("home", "cars", "genesis", "elantra", "sonata", "about")
URL_ATTRIBUTES = ("href", "src", "poster", "data-image")


class PageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attributes):
        self.links.extend(value for key, value in attributes if key in URL_ATTRIBUTES and value)


def normalize_base_path(value):
    value = value.strip("/")
    if value and not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", value):
        raise ValueError("Use a repository path such as /LAB-SPORTS-CARS.")
    if any(part in (".", "..") for part in value.split("/")):
        raise ValueError("The base path cannot contain directory traversal.")
    return "/" + value if value else ""


def validate_site(destination, base_path, routes):
    origin = "https://pages.example"
    for route in routes:
        file = destination / route.lstrip("/") / "index.html"
        document = PageLinks()
        document.feed(file.read_text(encoding="utf-8"))
        for link in document.links:
            target = urlsplit(urljoin(origin + base_path + route, unescape(link)))
            if target.netloc != "pages.example":
                continue
            prefix = base_path + "/"
            if not target.path.startswith(prefix):
                raise ValueError(f"Link leaves the hosted project: {link}")
            relative = unquote(target.path[len(prefix):])
            local = destination / relative
            if target.path.endswith("/"):
                local /= "index.html"
            if not local.resolve().is_relative_to(destination.resolve()) or not local.is_file():
                raise ValueError(f"Missing hosted file: {link}")


def build_site(destination, base_path=""):
    from django.test import Client
    from django.urls import reverse

    destination = Path(destination).resolve()
    if destination == ROOT or any(destination == ROOT / name for name in ("static", "templates", "showroom", "sportscars")):
        raise ValueError("Choose a separate output directory.")
    base_path = normalize_base_path(base_path)
    destination.mkdir(parents=True, exist_ok=True)
    client = Client(HTTP_HOST="localhost")
    routes = [reverse(f"showroom:{name}") for name in PAGE_NAMES]

    def prefix_url(match):
        attribute, value = match.groups()
        if value.startswith("/") and not value.startswith("//"):
            value = base_path + value
        return f'{attribute}="{value}"'

    for route in routes:
        response = client.get(route)
        if response.status_code != 200:
            raise ValueError(f"Cannot build {route}: HTTP {response.status_code}")
        html = re.sub(r'\b(href|src|poster|data-image)="([^"]*)"', prefix_url, response.content.decode())
        target = destination / route.lstrip("/") / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")

    shutil.copytree(ROOT / "static", destination / "static", dirs_exist_ok=True)
    (destination / ".nojekyll").write_text("", encoding="utf-8")
    validate_site(destination, base_path, routes)
    return routes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--base-path", default="")
    arguments = parser.parse_args()
    sys.path.insert(0, str(ROOT))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportscars.settings")
    import django
    django.setup()
    routes = build_site(arguments.output, arguments.base_path)
    print(f"Built and checked {len(routes)} pages in {arguments.output.resolve()}")


if __name__ == "__main__":
    main()
