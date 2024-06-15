from fastapi import APIRouter, File, Response, UploadFile
from faster_whisper import WhisperModel
from speech.s3_uploader import generate_presigned_url, upload_audiostream_to_s3
from speech.text_to_speech_stream import text_to_speech_stream
import json

model = WhisperModel("tiny")

app_router = APIRouter()

@app_router.post("/")
async def create_user(file: UploadFile = File(...)):
    with open("temp_audio.mp3", "wb") as temp_file:
        temp_file.write(await file.read())
    segments, info = model.transcribe("temp_audio.mp3")
    return [{"start": segment.start, "end": segment.end, "text": segment.text} for segment in segments]


@app_router.post("/text-to-speech/")
async def text_to_speech(text: str):
    audio_stream = text_to_speech_stream(text)
    s3_file_name = upload_audiostream_to_s3(audio_stream)

    signed_url = generate_presigned_url(s3_file_name)

    return Response(content=json.dumps({"signed_url": signed_url}), media_type="application/json")
