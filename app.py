import platform
from pathlib import Path

from PIL import Image

from renderer import render_message

WIDTH = 600
HEIGHT = 400


def get_image():
    img_dir = Path(__file__).parent / "img"
    images = [path for path in img_dir.iterdir() if path.is_file()] if img_dir.exists() else []

    if images:
        image = Image.open(images[0]).convert("RGB")
        image.thumbnail((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
        return image

    return render_message("Hello Aryana")


image = get_image()

if platform.system() == "Darwin":
    image.show()
else:
    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()