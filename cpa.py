from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Depends
from typing import Optional
import mimetypes
import requests
import json

app = FastAPI()

async def validate_message_or_attachment(message: Optional[str] = Form(None), attachment: Optional[UploadFile] = File(None)):
    if not message and not attachment:
        raise HTTPException(status_code=400, detail="At least one of 'message' or 'attachment' must be provided")
    return message, attachment

@app.post("/cap_chat")
async def cap_chat(message: Optional[str] = Form(None), attachment: Optional[UploadFile] = File(None), validated_data: tuple = Depends(validate_message_or_attachment)):
    message, attachment = validated_data
    processed_message = message.upper() if message else None


    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
    "model": "gpt-4-0125-preview",
    "messages": [
        {
        "role": "user",
        "content": message
        }
    ],
    "temperature": 0.7
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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',
    'Cookie': '__cf_bm=c6zqRVLH6tKL37ONCjCjkS4bqUwnReIx5CIdhKg7Hc8-1709420057-1.0.1.1-NjnrF9y9TMXyFxihiMAU.jONQw.HNsMMxVzmWJkxfHq9XMIgtvjuh_dasorHVpqTtpj61HlBUSxjSM7er_ONXA; _cfuvid=1WbNdpOnR7mNFv33uScpGok6bqVcXVWu7HObBcOaZQE-1709420057007-0.0.1.1-604800000'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


    if attachment:
        mime_type, _ = mimetypes.guess_type(attachment.filename)
        if mime_type != 'application/pdf':
            raise HTTPException(status_code=400, detail="Attachment must be a PDF file")
        
        attachment_info = {"filename": attachment.filename, "content_type": attachment.content_type}
        return {"message": processed_message, "attachment": attachment_info}
    else:
        response_data = json.loads(response.text)
        # print(type(response.text))
        # print("response_data: ", response_data)
        # message_content = response_data['message']
        # parsed_message = json.loads(message_content)
        content = response_data['choices'][0]['message']['content']
        # print("content: ", content)
        return {"message": content}
