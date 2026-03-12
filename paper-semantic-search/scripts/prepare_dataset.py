import json
import pandas as pd

papers = []

with open("../data/arxiv-metadata-oai-snapshot.json", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        paper = json.loads(line)

        title = paper.get("title", "")
        abstract = paper.get("abstract", "")

        papers.append({
            "title": title,
            "abstract": abstract
        })

        # limit dataset to 2000 papers
        if i >= 2000:
            break

df = pd.DataFrame(papers)

df.to_csv("../data/papers.csv", index=False)

print("Dataset prepared successfully")