import os
from preprocessing import load_and_preprocess
from embedding import EmbeddingHandler
from utils import load_config

config = load_config()

# Preprocess
df = load_and_preprocess(config["paths"]["data"] + "song_lyrics.csv", config["parameters"]["top_n"])

# Generate embeddings and build index
embedding_handler = EmbeddingHandler(config["model"]["embedding_model"])
embeddings = embedding_handler.extract_embeddings(df["cleaned_lyrics"].tolist())
embedding_handler.build_faiss_index(embeddings)
embedding_handler.save_index(config["paths"]["embeddings"])
