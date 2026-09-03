import faiss

from app.config import FAISS_INDEX_PATH


class FaissService:

    def create_index(self, document_embeddings):

        dimension = document_embeddings.shape[1]

        index = faiss.IndexFlatIP(dimension)

        index.add(document_embeddings)

        return index

    def save_index(self, index):

        faiss.write_index(index, str(FAISS_INDEX_PATH))

        print("FAISS Index saved successfully.")

    def load_index(self):

        return faiss.read_index(str(FAISS_INDEX_PATH))

    def search(self, index, query_embedding, top_k):

        scores, indices = index.search(query_embedding, top_k)

        return scores, indices