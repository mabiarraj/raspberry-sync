import io
import platform

import requests
from PIL import Image

WIDTH = 600
HEIGHT = 400
IMAGE_URL = "https://raspberry-sync-production.up.railway.app/image"


def get_image():
    response = requests.get(IMAGE_URL)
    photo = Image.open(io.BytesIO(response.content)).convert("RGB")
    photo.thumbnail((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    image.paste(photo, ((WIDTH - photo.width) // 2, (HEIGHT - photo.height) // 2))
    return image


image = get_image()

if platform.system() == "Darwin":
    image.show()
else:
    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()
