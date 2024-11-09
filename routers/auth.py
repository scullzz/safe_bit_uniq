from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
import jwt as pyjwt

from schemas.auth import UserRegistrationRequest, UserAuthenticationRequest
from models import User
from models.database import get_pg_db

# Settings
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

router = APIRouter(prefix="/auth", tags=["auth"])

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=False)

# Utility functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return pyjwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Registration endpoint
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(data: UserRegistrationRequest, db: Session = Depends(get_pg_db)):
    # Check if the user already exists
    user = db.query(User).filter(User.firstname == data.firstname).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    # Hash the password and create the user
    hashed_password = hash_password(data.password)
    new_user = User(
        firstname=data.firstname,
        lastname=data.lastname,
        password=hashed_password,
        email=data.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

# Authentication endpoint
@router.post("/authenticate")
def authenticate_user(data: UserAuthenticationRequest, db: Session = Depends(get_pg_db)):
    # Verify user credentials
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Create JWT token
    access_token = create_access_token(data={"sub": user.firstname})
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route example
@router.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_pg_db)):
    try:
        payload = pyjwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except pyjwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    # Query the user in the database
    user = db.query(User).filter(User.firstname == username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user
