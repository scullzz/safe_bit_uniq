from pydantic import BaseModel, Field
from typing import Literal

HealthGoalType = Literal["Weight Loss", "Weight Gain", "Muscle Gain", "Maintenance"]

class MealSchema(BaseModel):
    name: str = Field(..., description="The name of the meal (e.g., 'Grilled Chicken Salad')")
    type: Literal["breakfast", "lunch", "dinner", "snack"] = Field(
        ..., 
        description="The type of meal, chosen from 'breakfast', 'lunch', 'dinner', or 'snack'"
    )
    estimated_cooking_time: int = Field(
        ..., 
        description="Estimated cooking time in minutes, representing the time needed to prepare the meal"
    )

    class Config:
        orm_mode = True

class MealNutritionSchema(BaseModel):
    # Measured in grams (g)
    proteins: int = Field(..., description="Amount of protein in grams (g)")
    carbohydrates: int = Field(..., description="Amount of carbohydrates in grams (g)")
    fats: int = Field(..., description="Amount of fats in grams (g)")

    # Measured in milligrams (mg)
    fiber: int = Field(..., description="Amount of fiber in milligrams (mg)")
    sugar: int = Field(..., description="Amount of sugar in milligrams (mg)")
    sodium: int = Field(..., description="Amount of sodium in milligrams (mg)")
    cholesterol: int = Field(..., description="Amount of cholesterol in milligrams (mg)")


    class Config:
        orm_mode = True


class CreateMealRequest(BaseModel):
    meal: MealSchema
    nutrition: MealNutritionSchema

