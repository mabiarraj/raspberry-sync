from PIL import Image, ImageDraw, ImageFont

WIDTH = 600
HEIGHT = 400

WHITE = "white"
BLACK = "black"
RED = "red"


def render_message(message):
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(
        "fonts/Helvetica.ttc",
        44
    )

    # Message
    draw.text(
        (WIDTH // 2, 150),
        message,
        font=font,
        fill=BLACK,
        anchor="mm"
    )

    # Heart
    cx = WIDTH // 2
    cy = 240
    r = 18

    draw.ellipse(
        (cx - 2*r, cy - r, cx, cy + r),
        fill=RED
    )

    draw.ellipse(
        (cx, cy - r, cx + 2*r, cy + r),
        fill=RED
    )

    draw.polygon(
        [
            (cx - 2*r, cy),
            (cx + 2*r, cy),
            (cx, cy + 3*r)
        ],
        fill=RED
    )

    return image