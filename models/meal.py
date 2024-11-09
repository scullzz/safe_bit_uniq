from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.sql.schema import ForeignKey

from models.base import BaseModel

from models import BaseModel

class Meal(BaseModel):
    '''
    Meal ID: A unique identifier for each meal entry.
    Meal Name: The name of the dish (e.g., “Grilled Chicken Salad”).
    Meal Type: Categorize the meal as breakfast, lunch, dinner, or snack.
    Estimated Cooking Time: Total time required to prepare the meal, helping users with time constraints choose appropriate options.
    '''

    __tablename__ = "meal"

    name = Column(String)
    type = Column(String) # breakfast, lunch, dinner, or snack.
    estimated_cooking_time = Column(Integer) # minutes

    nutrition = relationship("MealNutrition", back_populates="meal", uselist=False)

 
class MealNutrition(BaseModel):
    '''
    Calories: Total caloric content per serving, essential for users aiming for specific caloric goals (e.g., weight loss or gain).
    Macronutrient Breakdown:
        Carbohydrates: Amount in grams per serving.
        Proteins: Amount in grams per serving, particularly important for muscle gain goals.
        Fats: Amount in grams per serving.
    Micronutrient Content (optional but valuable for certain users):
        Fiber: Helps users who want high-fiber diets.
        Sugar: Relevant for users managing blood sugar (e.g., diabetics).
        Sodium: Important for users needing low-sodium diets.
        Cholesterol: Useful for users managing cholesterol levels.
    '''

    __tablename__ = "meal_nutrition"

    calories = Column(Integer)

    # mesured in grams / gr
    proteins = Column(Integer)
    carbohydrates = Column(Integer)
    fats = Column(Integer)

    # measured in miligrams / mg
    fiber = Column(Integer)
    sugar = Column(Integer)
    sodium =  Column(Integer)
    cholesterol = Column(Integer)

    meal_id = Column(Integer, ForeignKey("meal.id"))

    meal = relationship("Meal", back_populates="nutrition")