import pandas as pd

from sentence_transformers import SentenceTransformer

import numpy as np

import os

import faiss

df = pd.read_csv("semantic_search_preprocessed.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")

df["Search_Text"] = (
    df["Clean Query"].fillna("") + " " +
    df["Clean Title"].fillna("") + " " +
    df["Clean Content"].fillna("") + " " +
    df["Keywords"].fillna("")
)

if os.path.exists("faiss_index.bin"):

    print("Loading FAISS Index...")

    index = faiss.read_index("faiss_index.bin")

else:

    print("Generating document embeddings...")

    document_embeddings = model.encode(
        df["Search_Text"].tolist(),
        show_progress_bar=True
    ).astype("float32")

    faiss.normalize_L2(document_embeddings)

    dimension = document_embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(document_embeddings)

    faiss.write_index(index, "faiss_index.bin")

    print("FAISS Index saved successfully!")

query = input("\n🔍 Enter your search query: ")

query_embedding = model.encode([query]).astype("float32")

faiss.normalize_L2(query_embedding)

scores, indices = index.search(query_embedding, 5)

print("\nTop 5 Semantic Search Results\n")

for score, idx in zip(scores[0], indices[0]):

    print("=" * 80)

    print("Document ID :", df.iloc[idx]["Document ID"])

    print("Category    :", df.iloc[idx]["Category"])

    print("Title       :", df.iloc[idx]["Title"])

    print("Similarity  :", round(float(score), 4))

    print("Content     :")

    print(df.iloc[idx]["Content"][:500])

    print()