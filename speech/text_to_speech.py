from .text_to_speech_stream import text_to_speech_stream
from .s3_uploader import upload_audiostream_to_s3, generate_presigned_url



def text_to_speech(text):
    audio_stream = text_to_speech_stream(text)
    s3_file_name = upload_audiostream_to_s3(audio_stream)

    signed_url = generate_presigned_url(s3_file_name)
    return signed_url
