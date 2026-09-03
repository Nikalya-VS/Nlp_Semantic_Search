from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Semantic Search API",
    description="Production Ready Semantic Search System",
    version="1.0.0"
)

app.include_router(router)