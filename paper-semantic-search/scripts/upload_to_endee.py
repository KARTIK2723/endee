import json
import requests

with open("../data/papers_with_embeddings.json") as f:
    papers = json.load(f)

url = "http://localhost:8080/insert"

for i, paper in enumerate(papers):

    payload = {
        "id": i,
        "vector": paper["embedding"],
        "metadata": {
            "title": paper["title"],
            "abstract": paper["abstract"]
        }
    }

    r = requests.post(url, json=payload)

    print(i, r.status_code)

print("Upload completed")