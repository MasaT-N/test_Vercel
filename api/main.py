from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "わたしはカモメです。名前はまだありません。"}