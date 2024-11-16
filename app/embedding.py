from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class EmbeddingHandler:
    def __init__(self, model_name, index_type="IndexFlatL2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.index_type = index_type

    def extract_embeddings(self, text_list):
        return np.array(self.model.encode(text_list))

    def build_faiss_index(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def save_index(self, path):
        faiss.write_index(self.index, path)

    def load_index(self, path):
        self.index = faiss.read_index(path)

    def search(self, query_embedding, k):
        return self.index.search(query_embedding, k)
