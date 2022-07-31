from fastapi import APIRouter, HTTPException , status, Depends
from passlib.hash import pbkdf2_sha256
from api.schemas import AuthLogin
from fastapi.security import OAuth2PasswordRequestForm
from api.db import User , database
from api.token import create_access_token

router = APIRouter(tags=["Auth"])

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    query = User.select().where(User.c.username == request.username)
    myuser = await database.fetch_one(query=query)

    if not myuser:
        print("d")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not pbkdf2_sha256.verify(request.password, myuser.password):
        print('dd')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")
    
    access_token = create_access_token(
        data = {"sub": myuser.username }
    )

    return {"access_token": access_token, "token_type": "bearer"}
