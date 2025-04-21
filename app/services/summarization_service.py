from fastapi import UploadFile
from app.services.tools import extract_text_from_pdf, summarize_text

async def summarize_pdf(file: UploadFile) -> str:
    pdf_bytes = await file.read()
    text = extract_text_from_pdf(pdf_bytes)
    summary = summarize_text(text)
    return summary
