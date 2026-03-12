import streamlit as st
import json
import numpy as np
import os
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="AI Research Paper Semantic Search", layout="wide")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Get absolute path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dataset path
data_path = os.path.join(BASE_DIR, "data", "papers_with_embeddings.json")

# Load papers
with open(data_path) as f:
    papers = json.load(f)

st.title("🔎 AI Research Paper Semantic Search")

st.markdown(
"""
Search academic papers using **semantic similarity** instead of keywords.  
Powered by **vector embeddings** and designed to integrate with the **Endee vector database**.
"""
)

query = st.text_input("Enter your research topic")

st.info("Example searches: deep learning healthcare, transformers NLP, reinforcement learning robotics")

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

if query:

    query_embedding = model.encode(query)

    scores = []

    for paper in papers:
        score = cosine_similarity(query_embedding, paper["embedding"])
        scores.append((score, paper))

    scores.sort(reverse=True)

    st.subheader("Top Matching Papers")

    for score, paper in scores[:5]:
        st.markdown(f"### {paper['title']}")
        st.write(paper["abstract"])
        st.caption(f"Similarity Score: {score:.4f}")
        st.write("---")