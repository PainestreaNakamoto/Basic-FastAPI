from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = f"postgresql://postgres:root@localhost/testdb"

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False , autoflush=False, bind=engine)

Base = declarative_base()