import time

import requests

from display import display_image

BASE_URL = "https://raspberry-sync-production.up.railway.app"
POLL_SECONDS = 10

version = None

while True:
    try:
        response = requests.get(f"{BASE_URL}/metadata")
        response.raise_for_status()

        new_version = response.json()["version"]

        if new_version != version:
            print(f"New image detected: {new_version}")

            response = requests.get(f"{BASE_URL}/image")
            response.raise_for_status()

            display_image(response.content)
            version = new_version

    except Exception as error:
        print(f"Polling failed: {error}")

    time.sleep(POLL_SECONDS)