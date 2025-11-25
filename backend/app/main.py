from fastapi import FastAPI
from app.api.posts import router as posts_router
from app.db import connect, disconnect

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect()

@app.on_event("shutdown")
async def shutdown():
    await disconnect()

app.include_router(posts_router, prefix="/posts", tags=["posts"])