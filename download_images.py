"""
Downloads free car photos (Unsplash) into main/static/main/images/.
Run once from the project folder:   python download_images.py
"""
import os
import urllib.request

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main", "static", "main", "images")

# file name -> Unsplash image id (direct CDN link, no login needed)
PHOTOS = {
    "hero.jpg": "1658140918789-fb22d2ad7e93",
    "porsche-911-turbo-s.jpg": "1577391140471-f288bb6fe823",
    "porsche-911-gt3.jpg": "1711962842423-28f28b5bbf1d",
    "porsche-911-gt3-rain.jpg": "1711963307913-af439816c855",
    "porsche-gt3-rs.jpg": "1693379807051-905bd51ae97e",
    "porsche-taycan.jpg": "1582804021120-47f6b12635e3",
    "porsche-race.jpg": "1759646848326-446c3e012484",
    "white-sports-car.jpg": "1666846866060-6c958cca482c",
    "road-night.jpg": "1590521793841-3a64745b2783",
    "interior.jpg": "1673176313979-5ceef0158adc",
    "interior-dark.jpg": "1674177786385-1cf286b29320",
    "interior-red.jpg": "1656376220603-36886fb06e05",
    "showroom.jpg": "1704712375640-e7bfe18c7ad0",
}


def download(name, photo_id):
    path = os.path.join(IMAGES_DIR, name)
    if os.path.exists(path) and os.path.getsize(path) > 10_000:
        print(f"  skip   {name} (already exists)")
        return
    url = f"https://images.unsplash.com/photo-{photo_id}?fm=jpg&q=80&w=1600&fit=crop"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp, open(path, "wb") as f:
            f.write(resp.read())
        print(f"  ok     {name}")
    except Exception as e:
        print(f"  FAILED {name}: {e}")


if __name__ == "__main__":
    os.makedirs(IMAGES_DIR, exist_ok=True)
    print(f"Saving images to {IMAGES_DIR}")
    for name, pid in PHOTOS.items():
        download(name, pid)
    print("Done. Photos from Unsplash (free license: https://unsplash.com/license)")
