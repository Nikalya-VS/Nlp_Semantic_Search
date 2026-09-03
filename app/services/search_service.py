import pandas as pd
import faiss
from fastapi import HTTPException
from app.utils.logger import logger
from app.services.preprocessing_service import PreprocessingService

from app.config import (
    DATASET_PATH,
    TOP_K
)

from app.services.embedding_service import EmbeddingService
from app.services.faiss_service import FaissService


class SearchService:

    def __init__(self):

        try:

            self.embedding_service = EmbeddingService()

            self.faiss_service = FaissService()

            self.df = pd.read_csv(DATASET_PATH)

            self.preprocessing_service = PreprocessingService()

            self.df = self.preprocessing_service.create_search_text(self.df)

            self.index = self.faiss_service.load_index()

            logger.info("SearchService initialized successfully.")

        except Exception as e:

            logger.error(str(e))

            raise HTTPException(
                status_code=500,
                detail="Failed to initialize Search Service."
            )

    def search(self, query):

        try:

            if not query.strip():

                raise HTTPException(
                    status_code=400,
                    detail="Query cannot be empty."
                )

            logger.info(f"Received Query: {query}")

            query_embedding = self.embedding_service.generate_embeddings([query])

            faiss.normalize_L2(query_embedding)

            scores, indices = self.faiss_service.search(
                self.index,
                query_embedding,
                TOP_K
            )

            results = []

            for score, idx in zip(scores[0], indices[0]):

                row = self.df.iloc[idx]

                results.append({

                    "document_id": int(row["Document ID"]),

                    "category": row["Category"],

                    "title": row["Title"],

                    "content": row["Content"],

                    "keywords": row["Keywords"],

                    "similarity": round(float(score), 4)

                })

            logger.info(f"Returned {len(results)} results.")

            return results

        except HTTPException:

            raise

        except Exception as e:

            logger.exception(e)

            raise HTTPException(
                status_code=500,
                detail="Internal Server Error"
            )