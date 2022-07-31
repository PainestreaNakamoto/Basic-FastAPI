from typing import List
from fastapi import Depends, FastAPI, HTTPException, Response, status
from app.database import engine , sessionLocal
from sqlalchemy.orm import Session
from app import models , schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/article" , response_model=List[schemas.ArticleSchema])
async def posts(obj: schemas.ArticleSchema, db:Session = Depends(get_db)):

    new_article = models.Article(title=obj.title, description=obj.description)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article

@app.get("/article/{id}", status_code=status.HTTP_200_OK)
async def get_article(id: int ,db: Session = Depends(get_db)):

    # myarticle = db.query(models.Article).filter(models.Article.id == id).first()
    myarticle = db.query(models.Article).get(id)
    if myarticle:
        return myarticle
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The article id {id} doesn't exits")

@app.get("/get_all", status_code=status.HTTP_201_CREATED , response_model=List[schemas.MyArticleSchema])
async def get(db: Session = Depends(get_db)):

    article = db.query(models.Article).all()
    
    return article
    

@app.put("/article", status_code=status.HTTP_202_ACCEPTED)
async def update_article(id: int,obj: schemas.ArticleSchema, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == id)
    article.first()
    article.update({'title': obj.title, 'description': obj.description},synchronize_session=False)
    if article == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id: {id}")
    db.commit()

    return {"status": "The data is update"}

@app.delete("/article")
async def delete_article(id: int , db: Session = Depends(get_db)): 
    article = db.query(models.Article).filter(models.Article.id == id)
    if article.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exits")

    return Response(status_code=status.HTTP_204_NO_CONTENT) 