from fastapi import APIRouter, File, Response, UploadFile
from faster_whisper import WhisperModel
from speech.s3_uploader import generate_presigned_url, upload_audiostream_to_s3
from speech.text_to_speech_stream import text_to_speech_stream
import json

model = WhisperModel("large-v3")

# segments, info = model.transcribe("audio.mp3")

app_router = APIRouter()



@app_router.post("/")
async def create_user(file: UploadFile = File(...)):
    segments, info = model.transcribe(await file.read())
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

@app_router.post("/text-to-speech/")
async def text_to_speech(text: str):
    audio_stream = text_to_speech_stream(text)
    s3_file_name = upload_audiostream_to_s3(audio_stream)

    signed_url = generate_presigned_url(s3_file_name)

    return Response(content=json.dumps({"signed_url": signed_url}), media_type="application/json")

