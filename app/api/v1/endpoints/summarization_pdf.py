from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.summarization_service import summarize_pdf

router = APIRouter(prefix="/summarize", tags=["Summarization"])

@router.post("/pdf")
async def summarize_uploaded_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    summary = await summarize_pdf(file)
    return {"summary": summary}