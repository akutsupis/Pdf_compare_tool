from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from requests_func import request
from pdfhandler import load_pdf
import shutil
import os
import uvicorn

app = FastAPI()

# Set up CORS middleware options
origins = [
    "https://pdf-compare-tool.vercel.app/",  # React app runs on localhost:3000
    "https://pdf-compare-tool-r48a.onrender.com",  # FastAPI server runs on 127.0.0.1:3000
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins (websites)
    allow_credentials=True,
    allow_methods=["POST"],  # Allows all methods
    allow_headers=["*"],   # Allows all headers
)

@app.get("/")
def read_root():
    return {"Add": "Wrong place, buddy"}


@app.post("/uploadfiles/")
async def upload_files(rfp: UploadFile = File(...), proposal: UploadFile = File(...), system: str = Form(...), passcode: str = Form(...)):
    # Get the password from the environment
    env_passcode = os.getenv('PASSCODE')

    # Check if the passwords match
    if passcode != env_passcode:
        raise HTTPException(status_code=401, detail="Unauthorized")

    temp_rfp = await save_upload_file_tmp(rfp)
    temp_proposal = await save_upload_file_tmp(proposal)

    # Load PDF for city plan and proposal
    plan_page_count, request_text = load_pdf(temp_rfp)
    proposal_page_count, proposal_text = load_pdf(temp_proposal)

    # Make a request to the OpenAI API
    response = request('gpt-4-turbo',
                       system,
                       request_text,
                       proposal_text)

    # Clean up the temporary files
    os.remove(temp_rfp)
    os.remove(temp_proposal)

    return {"response": response}


async def save_upload_file_tmp(upload_file: UploadFile, tmp_dir="temp"):
    try:
        os.makedirs(tmp_dir)
    except FileExistsError:
        pass

    temp_file = os.path.join(tmp_dir, upload_file.filename)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return temp_file

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
