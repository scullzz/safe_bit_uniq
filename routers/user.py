from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
import jwt as pyjwt

from schemas.user import UserData
from models import User
from models.database import get_pg_db

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

router = APIRouter(prefix="/user", tags=["user"])
oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=False)

@router.put("/update-user")
def update_user(data: UserData, token: str = Depends(oauth2_scheme), db: Session = Depends(get_pg_db)):
    print(data)
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    try:
        # Remove "Bearer" prefix if present
        token = token.replace("Bearer ", "")
        # Decode the JWT token
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

    # Update user data based on fields in `data`, excluding password
    if data.age:
        user.age = data.age
    if data.weight:
        user.weight = data.weight
    if data.height:
        user.height = data.height
    if data.gender:
        user.gender = data.gender
    if data.active_factor:
        user.active_factor = data.active_factor
     
    if data.gender.lower() == "male":
        user.bmr = round(88.36 + (13.4 * data.weight) + (4.8 * data.height) - (5.7 * data.age))
    elif data.gender.lower() == "female":
        user.bmr = round(447.6 + (9.2 * data.weight) + (3.1 * data.height) - (4.3 * data.age))
    else:
        raise ValueError("Gender should be either 'Male' or 'Female'")

    user.calorie = round(user.bmr * data.active_factor)   

    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": user}
