from fastapi import APIRouter, File, UploadFile
from faster_whisper import WhisperModel

model = WhisperModel("tiny")

app_router = APIRouter()

@app_router.post("/")
async def create_user(file: UploadFile = File(...)):
    with open("temp_audio.mp3", "wb") as temp_file:
        temp_file.write(await file.read())
    segments, info = model.transcribe("temp_audio.mp3")
    return [{"start": segment.start, "end": segment.end, "text": segment.text} for segment in segments]