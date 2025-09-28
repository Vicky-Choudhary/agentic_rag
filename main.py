from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FilePathRequest:
    file_path : str

    
@app.get('/upload')
def upload(request : FilePathRequest):
    file_path = request.file_path