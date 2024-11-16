import streamlit as st
from transcription import transcribe_audio
from retrieval import get_similar_songs
from embedding import EmbeddingHandler
from utils import load_config
import os

config = load_config()

# Initialize
embedding_handler = EmbeddingHandler(config["model"]["embedding_model"])
embedding_handler.load_index(config["paths"]["embeddings"])

# Streamlit app
st.title("Cover Identification System")
youtube_url = st.text_input("Enter YouTube URL:")
k = st.slider("Number of Results:", min_value=1, max_value=10, value=5)

if st.button("Identify"):
    audio_path = config["paths"]["audio"]
    transcription = transcribe_audio(audio_path)
    st.write(f"Transcription: {transcription}")
    results = get_similar_songs(transcription, embedding_handler, k, df)
    st.write("Results:", results)
