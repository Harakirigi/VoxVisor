from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import cv2
import pytesseract
from app.services.recognize_text import recognize_text
from app.services.recognize_objects import recognize_objects
from app.services.transcribe_audio import transcribe_audio
# from app.services.identify_face import identify_face
from app.services.search_image import search_image

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

class Query(BaseModel):
    keyword: str

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("frontend/index.html", "r") as f:
        return HTMLResponse(f.read())

@app.post("/upload/image/text")
async def upload_image_for_text_recognition(file: UploadFile = File(...)):
    content = await file.read()
    text = recognize_text(content)
    return {"recognized_text": text}

@app.post("/upload/image/objects")
async def upload_image_for_object_recognition(file: UploadFile = File(...)):
    content = await file.read()
    objects = recognize_objects(content)
    return {"recognized_objects": objects}

@app.post("/upload/audio/transcribe")
async def upload_audio_for_transcription(file: UploadFile = File(...)):
    content = await file.read()
    transcript = transcribe_audio(content)
    return {"transcription": transcript}

# @app.post("/upload/image/face")
# async def upload_image_for_face_recognition(file: UploadFile = File(...)):
#     content = await file.read()
#     faces = identify_face(content)
#     return {"recognized_faces": faces}

@app.post("/search/image")
async def search_image_based_on_input(file: UploadFile = File(...)):
    content = await file.read()
    search_results = search_image(content)
    return {"search_results": search_results}
