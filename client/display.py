import io
import platform

from PIL import Image

WIDTH = 600
HEIGHT = 400


def display_image(data):
    photo = Image.open(io.BytesIO(data)).convert("RGB")
    photo.thumbnail((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    image = Image.new("RGB", (WIDTH, HEIGHT), "white")
    image.paste(
        photo,
        (
            (WIDTH - photo.width) // 2,
            (HEIGHT - photo.height) // 2,
        ),
    )

    if platform.system() == "Darwin":
        image.show()
        return

    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()