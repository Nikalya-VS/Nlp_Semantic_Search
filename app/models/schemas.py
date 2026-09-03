from pydantic import BaseModel


class SearchRequest(BaseModel):

    query: str


class SearchResult(BaseModel):

    document_id: int

    category: str

    title: str

    content: str

    similarity: float


class SearchResponse(BaseModel):

    results: list[SearchResult]