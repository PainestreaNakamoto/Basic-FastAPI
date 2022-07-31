from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from databases import Database


DATABASE_URL = f"postgresql://postgres:root@localhost/articledb"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

Article = Table(
    "article",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("description", String(500))
)

User = Table(
    "user",
    metadata,
    Column("id", Integer , primary_key=True),
    Column("username", String(20)),
    Column("password",String(120))
)

database = Database(DATABASE_URL)