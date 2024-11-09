
from fastapi import APIRouter, Depends, HTTPException, Query, Security
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from schemas.user import UserRegistrationRequest, UserAuthenticationRequest, UserPersonlRequest

router= APIRouter(prefix="/user", tags=["user"])

@router.post("/register")
def register_user(data: UserRegistrationRequest):
    pass

@router.post("/authenticate")
def authenticate_user(data: UserAuthenticationRequest):
    pass


@router.post("/")
def get_user():
    pass


@router.post("/")
def update_user():
    pass


@router.post("/")
def delete_user():
    pass