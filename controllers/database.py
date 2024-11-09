import os
from typing import Iterator
from sqlalchemy import create_engine
from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

load_dotenv(find_dotenv())

Base = declarative_base()

DATABASE_URL = os.getenv("POSTGRES_URL")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=30,
        pool_timeout=60,
        pool_recycle=1800,
        pool_pre_ping=True,
    ),
)

Base = declarative_base()

def get_pg_db() -> Iterator[Session]:
    """FastAPI dependency that provides a sqlalchemy session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        
