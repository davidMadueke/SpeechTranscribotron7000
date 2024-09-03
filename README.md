# Speech Transcribotron7000

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Features](#features)
- [Contributing](#contributing)

## Introduction
AI based Speech Transcription involves an AI taking an audio file and returning a transcript of the speech detected in that audio file, along with the ability to detect the exact time in which said speech occurred and identifying who is speaking at that time instant (which is called Speaker Diarization). 

Current state of the art speech transcription tools include algorithms such as Avid’s Phrase Finder, Adobe’s AI Transcriber and Trint. However, many of these options are either difficult to integrate between multiple production studios and labels, are not performant in terms of transcription accuracy, reliy on uploading data to an external server, or cannot perform effective Speaker Diarization.

Our solution utilises state of the art research and AI models to perform AI based speech transcription with Speaker Diarization. It has been shown to provably achieve as good if not better results than the current flagship transcription tools, with the added flexibility and privacy that a potential in-house developed solution can offer.

## Installation

To get started with this project, you'll need to clone the repository and install the required dependencies. Make sure you have [Python 3.9+](https://www.python.org/downloads/) installed.

```bash
# Clone the repository
git clone https://github.com/davidMadueke/SpeechTranscribotron7000.git

# Navigate to the project directory
cd SpeechTranscribotron7000

# Install the dependencies
pip install -r requirements.txt

```

## Setup
This project requires you to have an [Assembly AI API key](https://www.assemblyai.com/) and a [Hugging Face Token](https://huggingface.co/). These keys are necessary for accessing the services provided by Assembly AI and Hugging Face, respectively.

## Environment Variables
Create a .env file in the root directory of your project and add your keys as shown below:

```bash
# .env file
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
HUGGINGFACE_TOKEN=your_huggingface_token
```

## Usage
To start the streamlit application, run the following command:

```
streamlit run main.py
```

This will launch the application in your default web browser. You can now interact with the machine learning models via the Streamlit interface.

![Web UI](https://github.com/davidMadueke/SpeechTranscribotron7000/blob/main/assets/WebUI.png?raw=true)

