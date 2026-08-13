import io
import platform
import time

import requests
from PIL import Image

WIDTH = 600
HEIGHT = 400

BASE_URL = "https://raspberry-sync-production.up.railway.app"
POLL_SECONDS = 10


def get_image():
    response = requests.get(f"{BASE_URL}/image")

    photo = Image.open(io.BytesIO(response.content)).convert("RGB")
    photo.thumbnail((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    image.paste(
        photo,
        (
            (WIDTH - photo.width) // 2,
            (HEIGHT - photo.height) // 2,
        ),
    )

    return image


def display_image(image):
    if platform.system() == "Darwin":
        image.show()
        return

    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()


version = None

while True:
    new_version = requests.get(
        f"{BASE_URL}/metadata"
    ).json()["version"]

    if new_version != version:
        print(f"New image detected: {new_version}")

        image = get_image()
        display_image(image)

        version = new_version

    time.sleep(POLL_SECONDS)