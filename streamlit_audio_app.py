import streamlit as st
from streamlit_mic_recorder import mic_recorder
import os
import counter_starter as cs
from speech.text_to_speech import text_to_speech
from openai import OpenAI
import io

def initialize_api_client(api_key):
    return OpenAI(api_key=api_key)

# Replace 'your-api-key' with your actual OpenAI API key
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
    processed_text = cs.generate_counter(text, api_client)
    return processed_text

st.title("AI Debate Coach")

col1, col2, col3 = st.columns([2, 2, 1])  # Adjust column layout

with col1:
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

        # Generate the MP3 URL from processed speech
        mp3_url = text_to_speech(processed_speech)
        st.session_state['mp3_url'] = mp3_url  # Store the MP3 URL in session state for access in another part of the app
    else:
        st.text_area("Processed Speech will appear here once generated", "", height=400)

with col3:
    st.write("Play MP3 from URL")
    if 'mp3_url' in st.session_state and st.session_state['mp3_url']:
        st.audio(st.session_state['mp3_url'], format='audio/mp3')
    else:
        st.write("No audio to play yet. Process some text to generate audio.")
