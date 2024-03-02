from fastapi import FastAPI, HTTPException, UploadFile
from pydantic import BaseModel

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

class RetrainRequest(BaseModel):
    message: str
    attachment: UploadFile

app = FastAPI()

@app.post("/cap_chat")
async def cap_chat(request: RetrainRequest):
    message = request.message
    attachment = request.attachment

    if attachment and attachment.content_length > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File size exceeds maximum limit (10 MB)")

    if attachment and not attachment.filename.endswith(b".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    result = "Received and processed PDF file: " + attachment.filename
    return {"message": result}
