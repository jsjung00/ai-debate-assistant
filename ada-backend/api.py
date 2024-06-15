from fastapi import APIRouter, File, UploadFile
from faster_whisper import WhisperModel

model = WhisperModel("large-v3")

segments, info = model.transcribe("audio.mp3")

app_router = APIRouter()



@app_router.post("/")
async def create_user(file: UploadFile = File(...)):
    segments, info = model.transcribe(await file.read())
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))