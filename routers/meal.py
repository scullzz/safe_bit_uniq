from fastapi import APIRouter, Depends, HTTPException, Query, Security
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from models.database import get_pg_db
from controllers import db_meal

from schemas.meal import CreateMealRequest

router= APIRouter(prefix="/meal", tags=["meal"])

@router.post("/")
def create_meal(data: CreateMealRequest, db: Session = Depends(get_pg_db)):
    return db_meal.create_meal(db=db, data=data)

