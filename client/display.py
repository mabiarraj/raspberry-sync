import io
import platform

from PIL import Image, ImageEnhance

WIDTH = 600
HEIGHT = 400


def enhance_photo(photo):
    photo = ImageEnhance.Contrast(photo).enhance(1.15)
    photo = ImageEnhance.Color(photo).enhance(1.25)
    photo = ImageEnhance.Sharpness(photo).enhance(1.10)
    photo = ImageEnhance.Brightness(photo).enhance(1.05)

    return photo


def display_image(data, enhanced=False):
    photo = Image.open(io.BytesIO(data)).convert("RGB")

    if enhanced:
        photo = enhance_photo(photo)

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