import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("../data/papers_with_embeddings.json") as f:
    papers = json.load(f)

query = input("Search research papers: ")

query_vector = model.encode(query)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = []

for paper in papers:
    score = cosine_similarity(query_vector, paper["embedding"])
    scores.append((score, paper))

scores.sort(reverse=True)

for score, paper in scores[:5]:
    print("\nTitle:", paper["title"])
    print("Abstract:", paper["abstract"])