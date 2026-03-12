# AI Research Paper Semantic Search

🔎 A semantic search engine for academic research papers using vector embeddings and similarity search.

This project allows users to search research papers using **meaning and context** instead of simple keyword matching.

Example query:

```
deep learning healthcare
```

The system returns the **most semantically relevant research papers**.

---

# Live Demo

https://2qqpzkkvutc4dappw2ewaqy.streamlit.app/

---

# Problem Statement

Traditional search engines rely on **keyword matching**, which often fails to capture the semantic meaning of queries.

Example:

Search query:

```
deep learning healthcare
```

Keyword search may fail to return relevant papers if the words differ slightly.

To solve this, we use **vector embeddings** that represent text in a high-dimensional semantic space and perform **vector similarity search**.

---

# Solution

This system converts research papers into **vector embeddings** using a transformer model and performs **semantic similarity search** to retrieve the most relevant papers.

The system architecture includes:

1. Research paper dataset
2. Text embeddings using SentenceTransformers
3. Vector similarity search
4. Streamlit web interface for user interaction

---

# Dataset

Source:

* arXiv research paper metadata

Dataset contains:

* Paper title
* Paper abstract
* Vector embeddings

Files:

```
data/
 ├── papers.csv
 └── papers_with_embeddings.json
```

---

## Tech Stack

1. Python
2. Streamlit
3. Sentence Transformers
4. NumPy
5. Vector Similarity Search

---

## System Architecture

1. User enters a research query
2. Query is converted into an embedding using **SentenceTransformers**
3. Vector similarity search is performed
4. Most relevant research papers are retrieved
5. Results are displayed in the **Streamlit UI**

---

# Project Structure

```
paper-semantic-search
│
├── app.py
├── requirements.txt
├── scripts
│   ├── prepare_dataset.py
│   ├── generate_embeddings.py
│   └── upload_to_endee.py
│
└── data
    ├── papers.csv
    └── papers_with_embeddings.json
```

---

# How Endee Vector Database Is Used

Endee is used as the **vector database infrastructure** for storing and retrieving embeddings.

The project demonstrates how vector embeddings can be generated and uploaded to a vector database for semantic search applications.

This architecture is designed to scale to **millions or billions of vectors**, enabling large-scale AI search systems.

---

# Setup Instructions

Clone the repository

```
git clone https://github.com/KARTIK2723/endee.git
```

Navigate to project folder

```
cd paper-semantic-search
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run app.py
```

---

# Example Queries

```
deep learning healthcare
transformers in NLP
reinforcement learning robotics
graph neural networks
```

---

# Future Improvements

Integration with Endee vector database for large-scale vector retrieval
Support for millions of research papers
Paper filtering by domain
Advanced ranking models
Citation-based recommendations

---

## Author

**Kartik Sharma**
B.Tech CSE
Galgotias University
