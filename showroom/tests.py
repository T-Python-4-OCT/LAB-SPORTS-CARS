from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse
from PIL import Image

from .data import VEHICLES, SOCIAL_LINKS
from scripts.build_pages import build_site


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.assets, self.symbols, self.ids, self.tabs = [], [], [], set(), []
        self.cards = 0

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if "data-car-card" in attrs:
            self.cards += 1
        if attrs.get("role") == "tab":
            self.tabs.append(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        for key in ("src", "href", "poster"):
            value = attrs.get(key, "")
            if value.startswith("/static/"):
                self.assets.append(urlsplit(value).path)
                if tag == "use":
                    self.symbols.append(urlsplit(value).fragment)


class ShowroomTests(SimpleTestCase):
    page_names = ("home", "cars", "genesis", "elantra", "sonata", "about")

    def test_pages_export_works_under_repository_path(self):
        with TemporaryDirectory() as directory:
            output = Path(directory)
            routes = build_site(output, "/LAB-SPORTS-CARS")
            self.assertEqual(len(routes), 6)
            home = (output / "index.html").read_text(encoding="utf-8")
            detail = (output / "cars/hyundai-genesis-coupe/index.html").read_text(encoding="utf-8")
            self.assertIn('href="/LAB-SPORTS-CARS/cars/"', home)
            self.assertIn('poster="/LAB-SPORTS-CARS/static/', home)
            self.assertIn('src="/LAB-SPORTS-CARS/static/videos/elantra-n-hero.mp4"', home)
            self.assertIn('data-image="/LAB-SPORTS-CARS/static/', detail)
            self.assertTrue((output / "static/videos/elantra-n-hero.mp4").is_file())
            self.assertTrue((output / ".nojekyll").is_file())

    def test_six_pages_and_all_internal_links_and_static_assets(self):
        documents = {}
        sprite = ET.parse(settings.BASE_DIR / "static/images/ui-icons.svg")
        symbols = {node.attrib["id"] for node in sprite.iter() if "id" in node.attrib}
        for name in self.page_names:
            url = reverse(f"showroom:{name}")
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, url)
            self.assertTemplateUsed(response, "base.html")
            self.assertContains(response, '<html lang="en">')
            self.assertContains(response, 'id="mobile-nav"')
            self.assertContains(response, 'js/theme.js')
            document = Document()
            document.feed(response.content.decode())
            documents[url] = document
            for asset in document.assets:
                self.assertIsNotNone(finders.find(asset.removeprefix("/static/")), asset)
            for symbol in document.symbols:
                self.assertIn(symbol, symbols)
        for url, document in documents.items():
            for href in document.links:
                target = urlsplit(href)
                if target.scheme or target.netloc:
                    continue
                path = target.path or url
                self.assertIn(path, documents, href)
                if target.fragment:
                    self.assertIn(target.fragment, documents[path].ids, href)

    def test_collection_has_three_hyundai_models_and_correct_prices(self):
        response = self.client.get(reverse("showroom:cars"))
        document = Document()
        document.feed(response.content.decode())
        self.assertEqual(document.cards, 3)
        self.assertEqual(len({car["slug"] for car in VEHICLES}), 3)
        for car in VEHICLES:
            self.assertContains(response, car["name"])
            self.assertContains(response, f'SAR {car["demo_price_sar"]:,}')
        self.assertContains(response, "3 Cars Found")
        for control in ("brand-filter", "model-filter", "price-filter", "year-filter", "car-search", "saved-filter"):
            self.assertContains(response, f'id="{control}"')

    def test_home_matches_reference_sections_and_featured_order(self):
        response = self.client.get(reverse("showroom:home"))
        html = response.content.decode()
        for title in ("Performance", "Without Limits", "Featured Cars", "More Than a Car", "Why Choose Us", "Ready to Drive"):
            self.assertIn(title, html)
        document = Document()
        document.feed(html)
        self.assertEqual(document.cards, 3)
        self.assertLess(html.index('data-slug="hyundai-genesis-coupe"'), html.index('data-slug="hyundai-elantra-n-2025"'))
        self.assertLess(html.index('data-slug="hyundai-elantra-n-2025"'), html.index('data-slug="hyundai-sonata-n-line"'))

    def test_three_detail_pages_have_correct_data_and_accessible_tabs(self):
        self.assertEqual(len(VEHICLES), 3)
        for car in VEHICLES:
            response = self.client.get(reverse(f'showroom:{car["url_name"]}'))
            for value in (car["name"], car["engine"], car["power"], car["transmission"], car["drive"]):
                self.assertContains(response, value)
            self.assertContains(response, 'data-inquire="' + car["name"] + '"')
            self.assertContains(response, 'data-wishlist="' + car["slug"] + '"')
            document = Document()
            document.feed(response.content.decode())
            self.assertEqual(len(document.tabs), 4)
            self.assertEqual(sum(tab["aria-selected"] == "true" for tab in document.tabs), 1)
            for tab in document.tabs:
                self.assertIn(tab["aria-controls"], document.ids)
            self.assertGreaterEqual(len(car["gallery"]), 2)
            for photo in car["gallery"]:
                self.assertTrue(Path(settings.BASE_DIR, "static", photo["path"]).is_file())

    def test_about_matches_reference_sections(self):
        response = self.client.get(reverse("showroom:about"))
        for title in ("Driven by", "Passion", "Our Story", "What Drives Us", "Drivers First", "Straight Answers", "Everyday Excitement", "More Than a Dealer"):
            self.assertContains(response, title)

    def test_elantra_is_2025_n_manual_and_old_url_redirects(self):
        canonical = reverse("showroom:elantra")
        self.assertEqual(canonical, "/cars/hyundai-elantra-n-2025/")
        response = self.client.get(canonical)
        for specification in ("Hyundai Elantra N 2025", "2.0L Turbo GDI", "276 hp", "6-speed manual", "Performance Blue"):
            self.assertContains(response, specification)
        self.assertNotContains(response, "Elantra N Line")
        self.assertRedirects(
            self.client.get(reverse("showroom:elantra-legacy") + "?photo=2"),
            canonical + "?photo=2",
            status_code=301,
        )

    def test_shared_footer_and_google_typography(self):
        for name in self.page_names:
            response = self.client.get(reverse(f"showroom:{name}"))
            for text in ("Stay in the Loop", "Privacy Policy", "Terms of Service", "newsletter-form", "fonts.googleapis.com", "Phudu", "Material+Symbols+Outlined"):
                self.assertContains(response, text)

    def test_demo_pages_reject_posts(self):
        for name in self.page_names:
            response = self.client.post(reverse(f"showroom:{name}"), {"email": "demo@example.com"})
            self.assertEqual(response.status_code, 405)
            self.assertEqual(response.headers["Allow"], "GET")

    def test_unknown_model(self):
        self.assertEqual(self.client.get("/cars/unknown-model/").status_code, 404)

    def test_active_photos_are_high_resolution_real_hyundai_assets(self):
        expected = {"Hyundai Genesis Coupe", "Hyundai Elantra N 2025", "Hyundai Sonata N Line"}
        self.assertEqual({car["name"] for car in VEHICLES}, expected)
        for car in VEHICLES:
            for photo in car["gallery"]:
                with Image.open(settings.BASE_DIR / "static" / photo["path"]) as source:
                    self.assertGreaterEqual(source.width, 500)
                    self.assertGreaterEqual(source.height, 220)
                self.assertNotIn("outdoor", photo["path"])
                self.assertNotIn("reference/", photo["path"])
                self.assertIn("editorial/", photo["path"])
            with Image.open(settings.BASE_DIR / "static" / car["image"]["path"]) as main_photo:
                self.assertGreaterEqual(main_photo.width, 950)
            for feature in car["features"]:
                self.assertTrue((settings.BASE_DIR / "static" / feature["image"]["path"]).is_file())
        for name in self.page_names:
            response = self.client.get(reverse(f"showroom:{name}"))
            for previous in ("Porsche", "Ferrari", "Lamborghini", "McLaren", "Aston Martin", "Mercedes-AMG", "/images/reference/", "outdoor.webp"):
                self.assertNotContains(response, previous)

    def test_social_links_use_hyundai_wallan(self):
        response = self.client.get(reverse("showroom:home"))
        self.assertEqual({social["name"] for social in SOCIAL_LINKS}, {"Instagram", "YouTube", "Facebook", "X"})
        for social in SOCIAL_LINKS:
            self.assertContains(response, social["url"])
            self.assertContains(response, f'aria-label="Hyundai Wallan on {social["name"]}"')

