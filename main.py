import streamlit as st
import assemblyai as aai
from annotated_text import annotated_text
import io
from dotenv import load_dotenv
import os
import time
import whisper_timestamped as whisper
import whisperx
from configs import config, assemblyAI_config
from whisper_DTW import transcribe, init_whisper_model
from diarize import diarize, init_diarization_model
from helper import save_file, cleanup_tmp_dir
from open_source import open_source_inference
from assemblyAI_API import assemblyai_inference

load_dotenv()

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

aai.settings.api_key = os.getenv("ASSEMBLY_API_KEY")

"""
# Multi-speaker Speech Transcription Tool

"""
# Provide user with access to Open Source or Closed Source Models

model_options = st.selectbox(
    "Select whether the engine should use Open Source Models or a Closed Source Service (Note: Closed source requires an API Key)",
    options=("Open Source", "Assembly AI"),
    index=None,
    placeholder="Select Model type..."
)
if model_options == "Open Source":
    # Initialise Model
    with st.sidebar.status("Initialising Whisper model...") as status:
        whisper_model = init_whisper_model()
        status.update(label="Whisper Model Loaded", state="complete", expanded=False)

    with st.sidebar.status("Initialising Diarization model...") as status:
        diarize_model = init_diarization_model()
        status.update(label="Diarization Model Loaded", state="complete", expanded=False)

# TODO: Implement UI option to input AssemblyAI API key

# Upload and save Input Audio File
cleanup_tmp_dir() #Remove any traces of temporary directory on load
input_audio = st.file_uploader(
    "Upload your Audio File here",
    type=['mp3', 'wav'],
    accept_multiple_files=False,
    help="Note: Later editions will allow for larger file sizes"
)

#Once a file has been loaded, perform the Whisper DTW transcription
if input_audio is not None:
    audio_path = save_file(input_audio)
    st.audio(input_audio, format="audio/wav")
    input_audio_bytes = input_audio.read()
    print(input_audio.name, audio_path)

    # TODO: Add choice of language to Configs.py and add a UI element
    if model_options == "Open Source":
        speaker_text_pairs, speaker_words_pairs = open_source_inference(
            audio_path=audio_path,
            whisper_model=whisper_model,
            diarize_model=diarize_model,
            language=None
        )
    elif model_options == "Assembly AI":
        speaker_text_pairs, file = assemblyai_inference(
            audio_path=audio_path,
            _config=assemblyAI_config
        )

        with open(f"{input_audio.name.split('.')[0]}_transcription.vtt", "w") as transcription_file:
            transcription_file.write(file)  # Write the content of the `file` variable

        with open(f"{input_audio.name.split('.')[0]}_transcription.vtt", "r") as file:
            download_button = st.download_button(
                label="Download Transcription File here",
                data=file,
                file_name=f"{input_audio.name.split('.')[0]}_transcription.vtt",
                mime="text/vtt"
            )
    else:
        st.error('Model Choice has not been selected. Please select a choice')


