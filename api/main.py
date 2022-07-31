from typing import List
from fastapi import FastAPI , status, HTTPException
from api.db import Article, metadata, database, engine 
from api.schemas import ArticleSchemaIn , ArticleSchema
from api.articles import router as articles_router
from api.user import router as user_router
from api.auth import router as auth_router

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(
    articles_router,
    prefix="/article"
)
app.include_router(
    user_router,
    prefix="/user"
)
app.include_router(
    auth_router,
    prefix="/auth"
)