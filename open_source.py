import streamlit as st
from annotated_text import annotated_text

import whisperx
from configs import config
from whisper_DTW import transcribe
from diarize import diarize


def open_source_inference(audio_path, whisper_model, diarize_model, language=None):
    transcription = transcribe(whisper_model, audio_path, language=language)

    # Now perform Pyannote Open Source Diarization
    # Create Streamlit Slider to indicate the number of speakers that should be present for
    min_num_speakers, max_num_speakers = st.select_slider(
        "Select the minimum and maximum number of expected speakers",
        options=[x+1 for x in range(config["absolute_max_speakers"])],
        value=(2,3)
    )

    diarized_segments = diarize(diarize_model,
                                audio_path=audio_path,
                                min_num_speakers=min_num_speakers,
                                max_num_speakers=max_num_speakers)



    # Assign Speakers to each word
    word_speakers = whisperx.assign_word_speakers(diarized_segments,
                                                  transcription,
                                                  fill_nearest=True)

    # extract all of the 'speaker' and 'text' keys and value pairs from the result['segments'] list of dictionaries

    speaker_text_pairs = []
    speaker_words_pairs = []
    for segment in word_speakers['segments']:
        speaker_text_pairs.append((f"{segment['text']}\n", f"{word['speaker']}"))
        for word in segment['words']:
            speaker_words_pairs.append((f"{word['speaker']}\n", f"{word['text']}"))

    annotated_text(speaker_text_pairs)

    return speaker_text_pairs, speaker_words_pairs