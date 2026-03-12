import pandas as pd
from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Reading dataset...")

df = pd.read_csv("../data/papers.csv")

texts = (df["title"] + " " + df["abstract"]).tolist()

print("Generating embeddings...")

embeddings = model.encode(texts)

df["embedding"] = embeddings.tolist()

df.to_json("../data/papers_with_embeddings.json", orient="records")

print("Embeddings generated successfully")