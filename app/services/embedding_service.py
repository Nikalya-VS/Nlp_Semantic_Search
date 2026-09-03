import os
import numpy as np

from sentence_transformers import SentenceTransformer

from app.config import (
    MODEL_NAME,
    EMBEDDINGS_PATH
)


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer(MODEL_NAME)

    def generate_embeddings(self, texts):

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings.astype("float32")

    def save_embeddings(self, embeddings):

        np.save(EMBEDDINGS_PATH, embeddings)

        print("Embeddings saved successfully.")

    def load_embeddings(self):

        return np.load(EMBEDDINGS_PATH)

    def embeddings_exist(self):

        return os.path.exists(EMBEDDINGS_PATH)