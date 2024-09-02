import streamlit as st
import os
from configs import config
import shutil
from streamlit.runtime.uploaded_file_manager import UploadedFile


def save_file(uploadedfile: UploadedFile):
    # Directory for where audio files will be served
    TEMP_DIR = config["temp_dir"]
    # Create the directory if it doesnt exists
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    with open(os.path.join("tempDir", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return os.path.join("tempDir", uploadedfile.name)

# Optional: Cleanup images directory upon session end
# This can be more complex depending on your app's logic and needs
def cleanup_tmp_dir():
    TEMP_DIR = config["temp_dir"]
    def cleanup():
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
    return cleanup