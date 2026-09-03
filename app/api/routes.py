from fastapi import APIRouter

from app.models.schemas import SearchRequest
from app.services.search_service import SearchService

router = APIRouter()

search_service = SearchService()


@router.post("/search")
def semantic_search(request: SearchRequest):

    results = search_service.search(request.query)

    return {
        "results": results
    }