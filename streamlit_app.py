import streamlit as st
import counter_starter as cs
import os
from openai import OpenAI

def initialize_api_client(api_key):
    return OpenAI(api_key=api_key)

# Replace 'your-api-key' with your actual OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

api_client = initialize_api_client(api_key)


def process_speech(text):
    # This is a placeholder for the processing function.
    # You can implement any specific processing logic here.
    processed_text = cs.generate_counter(text, api_client)
    return processed_text

def save_text(text, filename="processed_speech.txt"):
    with open(filename, "w") as f:
        f.write(text)
    return filename

st.title("AI Debate Coach")

# Create two columns for input and output
col1, col2 = st.columns(2)


# Large text input for speeches in the left column
with col1:
    speech_text = st.text_area("Enter the speech text here:", height=400)
    # Move the button below the text area in the left column
    process_button = st.button("Generate Counter Argument")

# Display output in the right column
with col2:
    if process_button and speech_text:
        # Process the speech
        processed_speech = process_speech(speech_text)

        # Display the processed text in another text area
        st.text_area("Processed Speech:", processed_speech, height=400)
    else:
        # Display an empty text area to align both columns visually
        st.text_area("Processed Speech:", "", height=400)