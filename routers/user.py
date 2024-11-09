from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
import jwt as pyjwt
from models.user import HealthGoal, MedicalReference

from schemas.user import Allergies, DietaryPrefence, FoodIntolerance, MedicalCondition, UserData
from models import User
from models.database import get_pg_db

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

router = APIRouter(prefix="/user", tags=["user"])
oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=False)

@router.get('/get_allergies')
def get_allergies():
     allergies = [allergy.value for allergy in Allergies]
     return allergies

@router.get('/get_foodIntolerance')
def get_foodIntolerance():
     intolerances = [intolerance.value for intolerance in FoodIntolerance]
     return intolerances

@router.get('/get_medicalCondition')
def get_medicalCondition():
     conditions = [conditions.value for conditions in MedicalCondition]
     return conditions

@router.get('/get_dietaryPrefence')
def get_dietaryPrefence():
    preference = [preference.value for preference in DietaryPrefence]
    return preference

@router.put("/update-user")
def update_user(data: UserData, token: str = Depends(oauth2_scheme), db: Session = Depends(get_pg_db)):
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
    
    # Update or create HealthGoal entry
    if data.primary_goal or data.target_weight:
        health_goal = db.query(HealthGoal).filter(HealthGoal.user_id == user.id).first()
        if not health_goal:
            health_goal = HealthGoal(user_id=user.id)
            db.add(health_goal)
        health_goal.primary_goal = data.primary_goal
        health_goal.target_weight = data.target_weight

    # Update or create MedicalReference entry based on medical_preferences
    if data.medical_preferences:
        medical_reference = db.query(MedicalReference).filter(MedicalReference.user_id == user.id).first()
        if not medical_reference:
            medical_reference = MedicalReference(user_id=user.id)
            db.add(medical_reference)
        
        # Convert Enum values to strings
        medical_reference.allergies = [allergy.value for allergy in data.medical_preferences.allergies] if data.medical_preferences.allergies else None
        medical_reference.medical_condition = [condition.value for condition in data.medical_preferences.medical_condition] if data.medical_preferences.medical_condition else None
        medical_reference.food_intolerance = [intolerance.value for intolerance in data.medical_preferences.food_intolerance] if data.medical_preferences.food_intolerance else None
        medical_reference.dietary_preference = [preference.value for preference in data.medical_preferences.dietary_preference] if data.medical_preferences.dietary_preference else None

    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully", "user": user}


