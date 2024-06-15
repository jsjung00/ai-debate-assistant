from fastapi import APIRouter, UploadFile, File, Response, UploadFile
from faster_whisper import WhisperModel
from pydantic import BaseModel
import requests
from speech.s3_uploader import generate_presigned_url, upload_audiostream_to_s3
from speech.text_to_speech_stream import text_to_speech_stream
import json

from preprompt import process_speech

model = WhisperModel("tiny")

app_router = APIRouter()

@app_router.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    file_location = f"temp_audio/{file.filename}"
    with open(file_location, "wb") as temp_file:
        content = await file.read()
        temp_file.write(content)
    segments, info = model.transcribe(file_location)
    speech =  " ".join([segment.text for segment in segments])
    # print(speech)
    # return speech
    return process_speech( speech )




@app_router.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    with open("temp_audio.mp3", "wb") as temp_file:
        temp_file.write(await file.read())
    segments, info = model.transcribe("temp_audio.mp3")
    return " ".join([segment.text for segment in segments])


@app_router.post("/direct_text")
async def direct_text(text: str):
    return text


@app_router.post("/rag")
async def rag(text: str):
    url = "https://api.conversecart.com/search"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "query": text,
        "indexID": "666e1f0236ae598278a3ee69",
        "sessionID": "string",
        "top_k": 1,
        "loc": 0
    }

    response = requests.post(url, headers=headers, json=data, verify=False)

    print(response.status_code)
    return response.json()

class TextToSpeechRequest(BaseModel):
    text: str


@app_router.post("/text-to-speech/")
async def text_to_speech(request: TextToSpeechRequest):
    audio_stream = text_to_speech_stream(request.text)
    s3_file_name = upload_audiostream_to_s3(audio_stream)

    signed_url = generate_presigned_url(s3_file_name)

    return Response(content=json.dumps({"signed_url": signed_url}), media_type="application/json")
