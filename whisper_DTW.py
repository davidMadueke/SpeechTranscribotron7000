import streamlit as st
import whisper_timestamped as whisper
from configs import config
import auditok

@st.cache_resource
def init_whisper_model():
    return whisper.load_model(
        config["whisper_model"],
        device=config["device"]
    )

@st.cache_data
def transcribe(_model, audio, language=None):
    audio = whisper.load_audio(audio)
    return whisper.transcribe(
        model=_model,
        audio=audio,
        vad=config["vad"],
        plot_word_alignment=False,
        temperature=0.0,
        language=language,
        compute_word_confidence=True
    )