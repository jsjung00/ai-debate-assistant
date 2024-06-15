from fastapi import APIRouter, UploadFile, File, Response, UploadFile
from faster_whisper import WhisperModel
from fastapi.middleware.cors import CORSMiddleware
from speech.text_to_speech_stream import text_to_speech_stream
from speech.s3_uploader import upload_audiostream_to_s3, generate_presigned_url
import json

model = WhisperModel("tiny")

app_router = APIRouter()

@app_router.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    file_location = f"temp_audio/{file.filename}"
    with open(file_location, "wb") as temp_file:
        content = await file.read()
        temp_file.write(content)
    segments, info = model.transcribe(file_location)
    return [{"start": segment.start, "end": segment.end, "text": segment.text} for segment in segments]


from pydantic import BaseModel

class TextToSpeechRequest(BaseModel):
    text: str

@app_router.post("/text-to-speech/")
async def text_to_speech(request: TextToSpeechRequest):
    audio_stream = text_to_speech_stream(request.text)
    s3_file_name = upload_audiostream_to_s3(audio_stream)

    signed_url = generate_presigned_url(s3_file_name)

    return Response(content=json.dumps({"signed_url": signed_url}), media_type="application/json")
