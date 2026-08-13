import platform

from renderer import render_message

image = render_message("Hello Aryana")

if platform.system() == "Darwin":
    image.show()
else:
    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()
