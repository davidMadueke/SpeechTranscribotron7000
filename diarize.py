import streamlit as st
import whisperx
import os
from dotenv import load_dotenv
from configs import config

load_dotenv()

@st.cache_resource
def init_diarization_model():
    return whisperx.DiarizationPipeline(use_auth_token=os.getenv("HUGGING_FACE_TOKEN"),
                                                 device=config['device'])
@st.cache_data
def diarize(_model, audio_path, min_num_speakers, max_num_speakers):
    return _model(audio_path, min_speakers=min_num_speakers, max_speakers=max_num_speakers)
