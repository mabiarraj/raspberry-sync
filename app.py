from pathlib import Path

import gpiod
import gpiodevice
from gpiod.line import Bias, Direction, Edge
from PIL import Image, ImageOps

from inky.auto import auto


WIDTH = 600
HEIGHT = 400

BUTTONS = [5, 6, 16, 24]

PHOTOS = [
    "photo1.jpeg",
    "photo2.jpeg",
    "photo3.jpeg",
    "photo4.jpeg",
]


inky = auto()

base_dir = Path(__file__).parent


def display_photo(filename):
    photo = Image.open(base_dir / filename).convert("RGB")

    # Fit inside the display without stretching.
    photo.thumbnail((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    # White 600x400 canvas.
    image = Image.new("RGB", (WIDTH, HEIGHT), "white")

    x = (WIDTH - photo.width) // 2
    y = (HEIGHT - photo.height) // 2

    image.paste(photo, (x, y))

    inky.set_image(image)
    inky.show()


input_settings = gpiod.LineSettings(
    direction=Direction.INPUT,
    bias=Bias.PULL_UP,
    edge_detection=Edge.FALLING,
)

chip = gpiodevice.find_chip_by_platform()

offsets = [
    chip.line_offset_from_id(button)
    for button in BUTTONS
]

line_config = dict.fromkeys(offsets, input_settings)

request = chip.request_lines(
    consumer="raspberry-sync",
    config=line_config,
)


print("Waiting for button presses...")


while True:
    for event in request.read_edge_events():
        index = offsets.index(event.line_offset)

        filename = PHOTOS[index]

        print(f"Button {index + 1}: {filename}")

        display_photo(filename)