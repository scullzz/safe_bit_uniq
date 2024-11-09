from enum import Enum
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from models.base import BaseModel

    
class User(BaseModel):
    __tablename__ = "user"

    firstname = Column(String)
    lastname = Column(String)

    email = Column(String)
    password = Column(String)
    
    age = Column(Integer)
    weight = Column(Integer)
    height = Column(Integer)

    calorie = Column(String)
    bmr = Column(Float)
    active_factor = Column(Float)

    gender = Column(String)
   
    health_goal = relationship("HealthGoal", uselist=False, back_populates="user")

class HealthGoal(BaseModel):
    __tablename__ = "health_goal"

    primary_goal = Column(String) # weight loss, weight gain, muscle gain, maintenance
    target_weight = Column(Integer) # Desired weight or specific muscle gain targets.
    
    user = relationship("User", back_populates="health_goal")
    user_id = Column(Integer, ForeignKey("user.id"))


