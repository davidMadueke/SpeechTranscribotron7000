import streamlit as st
import assemblyai as aai
from annotated_text import annotated_text
from langchain.document_loaders import AssemblyAIAudioTranscriptLoader
from langchain.document_loaders.assemblyai import TranscriptFormat

@st.cache_data
def assemblyai_inference(audio_path, _config):
    transcript = aai.Transcriber().transcribe(audio_path, _config)
    speaker_text_pairs = []
    for utterance in transcript.utterances:
        speaker_text_pairs.append((f'{utterance.text}\n', f"Speaker {utterance.speaker}"))

    # TODO: Create UI element that allows to select between VTT, Sentences or SRT file format
    annotated_text(speaker_text_pairs)
    file_format_loader = AssemblyAIAudioTranscriptLoader(
        file_path=audio_path, config=_config,
        transcript_format=TranscriptFormat.SUBTITLES_VTT,
    )
    file_format_docs = file_format_loader.load()

    file = file_format_docs[0].page_content
    return speaker_text_pairs, file