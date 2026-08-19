import queue
import time

import requests

from buttons import setup_buttons
from display import display_image

BASE_URL = "https://raspberry-sync-production.up.railway.app"
POLL_SECONDS = 10

version = None
current_image = None
enhanced = False
button_events = queue.Queue()

def button_pressed(button):
    button_events.put(button)

setup_buttons(button_pressed)

while True:
    try:
        while not button_events.empty():
            button = button_events.get()
            if button == "A" and current_image is not None:
                enhanced = not enhanced
                print(
                    "Enhancement:",
                    "ON" if enhanced else "OFF",
                )
                display_image(
                    current_image,
                    enhanced=enhanced,
                )

        response = requests.get(f"{BASE_URL}/metadata")
        response.raise_for_status()
        new_version = response.json()["version"]

        if new_version != version:
            print(f"New image detected: {new_version}")
            response = requests.get(f"{BASE_URL}/image")
            response.raise_for_status()
            current_image = response.content
            enhanced = False
            display_image(current_image)
            version = new_version

    except Exception as error:
        print(f"Error: {error}")

    time.sleep(POLL_SECONDS)