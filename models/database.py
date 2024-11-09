import os
from typing import Iterator

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import NullPool, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

load_dotenv(find_dotenv(), override=True)

DATABASE_URL = os.getenv("POSTGRES_URL")  # or other relevant config var
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

Base = declarative_base()


engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_pg_db() -> Iterator[Session]:
    """FastAPI dependency that provides a sqlalchemy session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()