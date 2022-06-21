import os
from dotenv import dotenv_values, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = {
    **dotenv_values('.env')
}

engine = create_engine('sqlite:///sqlitedb.file')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
