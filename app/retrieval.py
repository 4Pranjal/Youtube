from embedding import EmbeddingHandler

def get_similar_songs(query, embedding_handler, k, df):
    query_embedding = embedding_handler.extract_embeddings([query])
    D, I = embedding_handler.search(query_embedding, k)
    results = []
    for i in range(k):
        song_index = I[0][i]
        results.append({
            "title": df.iloc[song_index]["title"],
            "artist": df.iloc[song_index]["artist"],
            "score": D[0][i]
        })
    return results
