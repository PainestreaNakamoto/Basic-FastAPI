from fastapi import APIRouter , status
from api.schemas import UserSchema, UserSchemaIn 
from api.db import User , database
from typing import List
from passlib.hash import pbkdf2_sha256

router = APIRouter(tags=["User"])

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model = UserSchema)
async def insert_article(user: UserSchemaIn):
    hashed_password = pbkdf2_sha256.hash(user.password)
    print(hashed_password)
    query = User.insert().values(username = user.username, password=hashed_password)
    last_record_id = await database.execute(query)

    return {**user.dict(),"id": last_record_id}
