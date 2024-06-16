import streamlit as st
import counter_starter as cs
import os
from openai import OpenAI

def initialize_api_client(api_key):
    return OpenAI(api_key=api_key)

# Replace 'your-api-key' with your actual OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
api_client = initialize_api_client(api_key)

def process_speech(text):
    # This function calls the counter argument generator from the counter_starter module.
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
    process_button = st.button("Generate Counter Argument")
    if speech_text:  # Display the word count for the input speech
        input_word_count = len(speech_text.split())
        st.write(f"Input Word Count: {input_word_count}")

# Display output in the right column
with col2:
    if process_button and speech_text:
        # Process the speech
        processed_speech = process_speech(speech_text)

        # Display the processed text in another text area
        st.text_area("Processed Speech:", processed_speech, height=400)
        
        # Display the word count for the processed speech
        output_word_count = len(processed_speech.split())
        st.write(f"Output Word Count: {output_word_count}")
    else:
        # Display an empty text area to align both columns visually
        st.text_area("Processed Speech:", "", height=400)
        st.write("Output Word Count: 0")
