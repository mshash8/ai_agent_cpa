from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends
from typing import Optional
import mimetypes

app = FastAPI()

async def validate_message_or_attachment(message: Optional[str] = Form(None), attachment: Optional[UploadFile] = File(None)):
    if not message and not attachment:
        raise HTTPException(status_code=400, detail="At least one of 'message' or 'attachment' must be provided")
    return message, attachment

@app.post("/cap_chat")
async def cap_chat(message: Optional[str] = Form(None), attachment: Optional[UploadFile] = File(None), validated_data: tuple = Depends(validate_message_or_attachment)):
    message, attachment = validated_data
    processed_message = message.upper() if message else None

    if attachment:
        mime_type, _ = mimetypes.guess_type(attachment.filename)
        if mime_type != 'application/pdf':
            raise HTTPException(status_code=400, detail="Attachment must be a PDF file")
        
        attachment_info = {"filename": attachment.filename, "content_type": attachment.content_type}
        return {"message": processed_message, "attachment": attachment_info}
    else:
        return {"message": processed_message}
