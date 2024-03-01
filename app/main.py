from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_news():
    return {"new": "съемка в ДС"}
