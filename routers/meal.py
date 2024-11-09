from fastapi import APIRouter, Depends, HTTPException, Query, Security
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from schemas.meal import CreateMealRequest

router= APIRouter(prefix="/meal", tags=["meal"])

@router.post("/")
def create_meal(data: CreateMealRequest):
    pass

