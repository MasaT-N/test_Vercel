from fastapi import FastAPI
import os

app = FastAPI()
BLOB_READ_WRITE_TOKEN = os.getenv("BLOB_READ_WRITE_TOKEN")

@app.get("/")
async def root():
    return {"message": f"わたしはカモメです。名前はまだありません。"}