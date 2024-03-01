from fastapi import FastAPI

app = FastAPI()


@app.get("/bookings")
async def get_bookings():
    return {"booking": "заезд на неделю"}
