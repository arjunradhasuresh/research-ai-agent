from fastapi import FastAPI
from app.api.v1.endpoints import health_check,research

app = FastAPI(
    title="AI AGENT",
    version="1.0"
)


app.include_router(health_check.router)
app.include_router(research.router)

