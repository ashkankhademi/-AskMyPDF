# embedder.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load once (lightweight)
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(text_list):
    return model.encode(text_list)

def find_most_relevant_chunk(question, chunks, chunk_embeddings, top_k=1):
    question_embedding = model.encode([question])
    similarities = cosine_similarity(question_embedding, chunk_embeddings)[0]
    
    top_indices = similarities.argsort()[::-1][:top_k]
    top_chunks = [chunks[i] for i in top_indices]
    top_scores = [similarities[i] for i in top_indices]
    
    return list(zip(top_chunks, top_scores))
