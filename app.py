import platform

from renderer import render_message

image = render_message("Hello Aryana")

if platform.system() == "Darwin":
    # Mac development
    image.show()

else:
    # Raspberry Pi
    from inky.auto import auto

    inky = auto()
    inky.set_image(image)
    inky.show()