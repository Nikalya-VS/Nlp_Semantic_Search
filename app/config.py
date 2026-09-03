from pathlib import Path
import os

from dotenv import load_dotenv


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


# ============================================================
# PROJECT PATHS
# ============================================================

DATA_DIR = BASE_DIR / "data"

DATASET_PATH = DATA_DIR / "semantic_search_preprocessed.csv"

EMBEDDINGS_PATH = DATA_DIR / "document_embeddings.npy"

FAISS_INDEX_PATH = DATA_DIR / "faiss_index.bin"


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "all-MiniLM-L6-v2"
)

TOP_K = int(
    os.getenv(
        "TOP_K",
        "5"
    )
)

EMBEDDING_DIMENSION = int(
    os.getenv(
        "EMBEDDING_DIMENSION",
        "384"
    )
)


# ============================================================
# API CONFIGURATION
# ============================================================

API_HOST = os.getenv(
    "API_HOST",
    "127.0.0.1"
)

API_PORT = int(
    os.getenv(
        "API_PORT",
        "8000"
    )
)


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

APP_NAME = os.getenv(
    "APP_NAME",
    "Semantic Search AI"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
).lower() == "true"