from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import torch


class RAGEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Loads the SentenceTransformer model on CPU instead of GPU
        to prevent NotImplementedError in Streamlit Cloud.
        """
        # ✅ Force it to use CPU (Streamlit Cloud has no GPU)
        self.device = "cpu"
        self.model = SentenceTransformer(model_name, device=self.device)
        self.index = None
        self.texts = []

    def create_index(self, docs):
        embeddings = self.model.encode(docs, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.texts = docs

    def retrieve(self, query, k=3):
        if self.index is None:
            return []
        q_embed = self.model.encode([query])
        distances, indices = self.index.search(q_embed, k)
        return [self.texts[i] for i in indices[0]]

        q_embed = self.model.encode([query])
        distances, indices = self.index.search(q_embed, k)
        return [self.texts[i] for i in indices[0]]


