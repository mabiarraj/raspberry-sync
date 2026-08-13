from pathlib import Path

from fastapi import Body, FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
image_path = Path(__file__).parent / "image.jpg"


@app.post("/image")
def upload_image(image: bytes = Body(..., media_type="application/octet-stream")):
    image_path.write_bytes(image)
    return {"ok": True}


@app.get("/image")
def get_image():
    return FileResponse(image_path)
