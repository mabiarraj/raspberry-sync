import io
import platform
import time
from pathlib import Path

import requests
from PIL import Image

WIDTH = 600
HEIGHT = 400
BASE_URL = "https://raspberry-sync-production.up.railway.app"
VERSION_PATH = Path(__file__).parent / "version.txt"
POLL_SECONDS = 10


def get_image():
    response = requests.get(f"{BASE_URL}/image")
    photo = Image.open(io.BytesIO(response.content)).convert("RGB")
    photo.thumbnail((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    image.paste(photo, ((WIDTH - photo.width) // 2, (HEIGHT - photo.height) // 2))
    return image


def display_image(image):
    if platform.system() == "Darwin":
        image.show()
        return

    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()


def get_local_version():
    return VERSION_PATH.read_text() if VERSION_PATH.exists() else None


while True:
    version = requests.get(f"{BASE_URL}/metadata").json()["version"]

    if version != get_local_version():
        print(f"New image detected: {version}")
        display_image(get_image())
        VERSION_PATH.write_text(version)

    time.sleep(POLL_SECONDS)
