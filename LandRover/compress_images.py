from pathlib import Path
from PIL import Image

IMAGES_DIR = Path("main/static/main/images")
MAX_WIDTH = 1920

for path in IMAGES_DIR.rglob("*"):
    if path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    size_before = path.stat().st_size // 1024
    img = Image.open(path)

    if img.width > MAX_WIDTH:
        new_height = int(img.height * MAX_WIDTH / img.width)
        img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)

    if path.suffix.lower() == ".png":
        img.save(path, optimize=True)
    else:
        img = img.convert("RGB")
        img.save(path, quality=75, optimize=True)

    size_after = path.stat().st_size // 1024
    print(f"{path.name}: {size_before} KB -> {size_after} KB")