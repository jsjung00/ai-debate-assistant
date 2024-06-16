import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os
<<<<<<< Updated upstream
from openai import OpenAI
import base64
=======
import counter_starter as cs
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
<<<<<<< Updated upstream
               use_container_width=False, language=None, callback=None, args=(), kwargs=None, key = None):
    if not 'openai_client' in st.session_state:
        st.session_state.openai_client = OpenAI(api_key = api_key)
        print(key)
    if not '_last_speech_to_text_transcript_id' in st.session_state:
        st.session_state._last_speech_to_text_transcript_id = 0
    if not '_last_speech_to_text_transcript' in st.session_state:
        st.session_state._last_speech_to_text_transcript = None
    if key and not key + '_output' in st.session_state:
        st.session_state[key + '_output'] = None
    audio = mic_recorder(start_prompt=start_prompt, stop_prompt=stop_prompt, just_once=just_once,
                         use_container_width=use_container_width,format="webm", key=key)
    new_output = False
    if audio is None:
        output = None
    else:
        id = audio['id']
        new_output = (id > st.session_state._last_speech_to_text_transcript_id)
        if new_output:
            output = None
            st.session_state._last_speech_to_text_transcript_id = id
            audio_bio = io.BytesIO(audio['bytes'])
            audio_bio.name = 'audio.webm'
            success = False
            err = 0
            while not success and err < 3:  # Retry up to 3 times in case of OpenAI server error.
                try:
                    transcript = st.session_state.openai_client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_bio,
                        language=language
                    )
                except Exception as e:
                    print(str(e))  # log the exception in the terminal
                    err += 1
                else:
                    success = True
                    output = transcript.text
                    st.session_state._last_speech_to_text_transcript = output
        elif not just_once:
            output = st.session_state._last_speech_to_text_transcript
        else:
            output = None

    if key:
        st.session_state[key + '_output'] = output
    if new_output and callback:
        callback(*args, **(kwargs or {}))
    return output


def process_speech(text):
    # This function calls the counter argument generator from the counter_starter module.
    processed_text = "Processed: " + text  # Placeholder for actual processing function
    return processed_text

st.title("AI Debate Coach")

col1, col2 = st.columns(2)

text = whisper_stt( language = 'en')  
# If you don't pass an API key, the function will attempt to retrieve it as an environment variable : 'OPENAI_API_KEY'.
if text:
    st.write(text)
=======
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

def process_transcript(text):
    # Placeholder for actual processing function
    processed_text = cs.generate_counter(text, api_client)
    mp3_url = "https://fly.storage.tigris.dev/jun-15-hackathon/b58ff711-085a-472e-98db-c174e3dfc5e1.mp3?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=tid_TFQbzRJSrcbrnH_qnajVVsIBJswyQKSxWcZZhudY_rRRnJTfgG%2F20240616%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20240616T010646Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=c655df9509f8d4d0318c7495be8c568220ac7cd08d3d8bbc29690e3f9ef4b8bd"
    return processed_text, mp3_url

st.set_page_config(page_title="AI Audio-to-Audio Interface", layout="wide")
st.title("AI Audio-to-Audio Interface")

col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Record Audio")
    st.write("Click to start recording:")
    transcribed_text = whisper_stt(language='en', key="whisper")

with col2:
    if transcribed_text:
        st.subheader("Transcription")
        st.text_area("Transcribed Speech:", transcribed_text, height=200, key='transcribed_speech')
        
        processed_text, mp3_url = process_transcript(transcribed_text)
        st.subheader("Processed Transcription")
        st.text_area("Processed Speech:", processed_text, height=200, key='processed_speech')
        
        st.subheader("Audio Playback")
        st.write("Listen to the processed audio:")
        st.audio(mp3_url, format='audio/mp3')
    else:
        st.write("Start recording to see the transcription, processed information, and listen to the audio here.")

# Add sleek CSS styles to enhance the UI
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        border: 2px solid rgba(0, 0, 0, 0.1);
    }
    .css-2trqyj {
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .css-1d391kg {
        padding-top: 15px;
        padding-bottom: 15px;
        background-color: #f0f2f6;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)
>>>>>>> Stashed changes
