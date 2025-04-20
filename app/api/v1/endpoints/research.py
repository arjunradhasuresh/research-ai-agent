# app/api/v1/endpoints/research.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.agent_executor import run_research_agent

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/research", tags=["Research"])
def research_handler(payload: QueryRequest):
    return run_research_agent(payload.query)
