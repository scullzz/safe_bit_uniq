from fastapi import APIRouter, Depends, HTTPException, Query, Security
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from models.database import get_pg_db
from services.minio_client import get_minio_client
from controllers import db_meal

from minio import Minio

from schemas.meal import CreateMealRequest

router= APIRouter(prefix="/meal", tags=["meal"])

@router.post("/")
def create_meal(
    data: CreateMealRequest, 
    db: Session = Depends(get_pg_db), 
    minio: Minio = Depends(get_minio_client)
):
    return db_meal.create_meal(db=db, data=data)

