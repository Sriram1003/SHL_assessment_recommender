import os
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

catalog_df = None
index = None
model = SentenceTransformer("all-MiniLM-L6-v2")

csv_path = "backend/data/shl_catalog.csv"

def create_dataset_if_not_exists():
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found at {csv_path}")

def load_faiss_index():
    global catalog_df, index

    create_dataset_if_not_exists()
    catalog_df = pd.read_csv(csv_path)

    texts = (
        catalog_df["Assessment Name"].fillna("") + " " +
        catalog_df["Description"].fillna("") + " " +
        catalog_df["Test Type"].fillna("")
    ).tolist()

    embeddings = model.encode(texts, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    print("✅ FAISS index created and embeddings loaded")

def search_catalog(query):
    global catalog_df, index

    if catalog_df is None or index is None:
        return {"error": "Index not initialized"}

    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, 5)

    results = catalog_df.iloc[indices[0]].to_dict(orient="records")
    return results
