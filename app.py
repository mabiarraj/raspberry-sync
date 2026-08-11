from PIL import Image
import platform

image = Image.open("photo.jpeg")
image = image.convert("RGB")
image = image.resize((600, 400))

if platform.system() == "Darwin":
    image.show()
else:
    from inky.auto import auto
    inky = auto()
    inky.set_image(image)
    inky.show()