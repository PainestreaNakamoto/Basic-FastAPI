from fastapi import APIRouter, Depends, status , HTTPException
from typing import List
from api.db import Article, metadata, database, engine 
from api.schemas import ArticleSchemaIn , ArticleSchema, UserSchema
from api.token import get_current_user

router = APIRouter(tags=["Article"])


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model = ArticleSchema)
async def insert_article(article: ArticleSchemaIn):
    query = Article.insert().values(title = article.title, description=article.description)
    last_record_id = await database.execute(query)

    return {**article.dict(),"id": last_record_id}


@router.get("/all", response_model=List[ArticleSchema])
async def get_articel(current_user: UserSchema = Depends(get_current_user)):
    query = Article.select()
    data = await database.fetch_all(query=query)
    return data

@router.get("/detail/{id}", response_model = ArticleSchema)
async def get_details(id: int):
    query = Article.select().where(id== Article.c.id)
    myarticle = await database.fetch_one(query=query)
    if not myarticle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,  detail="Aritcle not found")
    
    return {**myarticle}    

@router.put("/update/{id}",response_model= ArticleSchema)
async def update_article(id: int,  article: ArticleSchemaIn):
    query = Article.update().where(Article.c.id == id).values(**article.dict())
    await database.execute(query)

    return {**article.dict(),"id":id}


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(id: int):
    query = Article.delete().where(Article.c.id == id)
    await database.execute(query=query)

    return {"message": "Article deleted"}