import assemblyai as aai

config = {
    "device": "cpu",
    "whisper_model": "small",
    "vad": "auditok",
    "absolute_max_speakers": 6,
    "temp_dir": "tempDir",

}

assemblyAI_config = aai.TranscriptionConfig(
    speaker_labels=True, auto_chapters=True, entity_detection=True,
    language_detection=False, summarization=False, punctuate=True,
    speech_model="best"
)