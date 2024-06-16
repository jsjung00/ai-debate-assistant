import streamlit as st
<<<<<<< Updated upstream
from streamlit_mic_recorder import mic_recorder
import os
import counter_starter as cs
from openai import OpenAI
import base64
=======
import counter_starter as cs
from streamlit_mic_recorder import mic_recorder
import os
from openai import OpenAI
>>>>>>> Stashed changes
import io

def initialize_api_client(api_key):
    return OpenAI(api_key=api_key)

<<<<<<< Updated upstream
# Replace 'your-api-key' with your actual OpenAI API key
=======
# Setup API client
>>>>>>> Stashed changes
api_key = os.getenv('OPENAI_API_KEY')
api_client = initialize_api_client(api_key)

def whisper_stt(start_prompt="Start recording", stop_prompt="Stop recording", just_once=False,
               use_container_width=False, language=None, callback=None, args=(), kwargs=None, key=None):
    if not 'openai_client' in st.session_state:
        st.session_state.openai_client = OpenAI(api_key=api_key)
    audio = mic_recorder(start_prompt=start_prompt, stop_prompt=stop_prompt, just_once=just_once,
                         use_container_width=use_container_width, format="webm", key=key)
    if audio is None:
        return None
    else:
        audio_bio = io.BytesIO(audio['bytes'])
        audio_bio.name = 'audio.webm'
        try:
            transcript = st.session_state.openai_client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_bio,
                language=language
            )
            return transcript.text
        except Exception as e:
            st.error("Failed to transcribe audio: " + str(e))
            return None

def process_speech(text):
    # Placeholder for actual processing function
    processed_text = cs.generate_counter(text, api_client)
    return processed_text

st.title("AI Debate Coach")

col1, col2, col3 = st.columns([2, 2, 1])  # Adjust column layout

with col1:
<<<<<<< Updated upstream
    st.write("Record your speech or enter text:")
    transcribed_text = whisper_stt(language='en', key="whisper")
    speech_text = st.text_area("Transcribed Speech or Enter Text:", transcribed_text if transcribed_text else "", height=400)
    process_button = st.button("Generate Counter Argument")

with col2:
    if process_button and speech_text:
        processed_speech = process_speech(speech_text)
        st.text_area("Processed Speech:", processed_speech, height=400)
        output_word_count = len(processed_speech.split())
        st.write(f"Output Word Count: {output_word_count}")
    else:
        st.text_area("Processed Speech will appear here once generated", "", height=400)

with col3:
    st.write("Play MP3 from URL")
    mp3_url = "https://fly.storage.tigris.dev/jun-15-hackathon/b58ff711-085a-472e-98db-c174e3dfc5e1.mp3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tid_TFQbzRJSrcbrnH_qnajVVsIBJswyQKSxWcZZhudY_rRRnJTfgG%2F20240616%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20240616T010646Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=c655df9509f8d4d0318c7495be8c568220ac7cd08d3d8bbc29690e3f9ef4b8bd"  # Change this to your actual MP3 URL
    st.audio(mp3_url, format='audio/mp3')
=======
    st.subheader("Record or Input")
    st.write("Record your speech or enter text:")
    transcribed_text = whisper_stt(language='en', key="whisper")
    
    show_input = st.checkbox("Show Input Text Area", value=False, key='show_input')
    if show_input:
        speech_text = st.text_area("Transcribed Speech or Enter Text:", transcribed_text if transcribed_text else "", height=300, key='speech_text')
        process_button = st.button("Generate Counter Argument", key='process_button')
    else:
        speech_text = ""
        process_button = False

with col2:
    st.subheader("Processed Output")
    show_output = st.checkbox("Show Output Text Area", value=False, key='show_output')
    if process_button and speech_text:
        processed_speech = process_speech(speech_text)
    else:
        processed_speech = ""

    if show_output:
        st.text_area("Processed Speech:", processed_speech, height=300, key='processed_speech')
        if processed_speech:
            output_word_count = len(processed_speech.split())
            st.metric(label="Word Count", value=output_word_count)

with col3:
    st.subheader("Playback")
    st.write("Play MP3 from URL")
    mp3_url = "https://yourdomain.com/yourfile.mp3"
    st.audio(mp3_url, format='audio/mp3')
>>>>>>> Stashed changes
