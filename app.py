from PIL import Image
import platform

from PIL import Image

photo = Image.open("photo.jpeg").convert("RGB")

# Create an Inky-sized white canvas
image = Image.new("RGB", (600, 400), "white")

# Centre the photo without resizing it
x = (600 - photo.width) // 2
y = (400 - photo.height) // 2

image.paste(photo, (x, y))

if platform.system() == "Darwin":
    image.show()
else:
    from inky.auto import auto
    inky = auto()
    inky.set_image(image)
    inky.show()