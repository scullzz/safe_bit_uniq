from schemas.meal import MealSchema, MealNutritionSchema, HealthGoalType, CreateMealRequest
from sqlalchemy.orm import Session
from models.meal import Meal, MealNutrition

def calcualte_meal_calories(meal_nutrition: MealNutritionSchema):
    return (meal_nutrition.carbohydrates) * 4 + (meal_nutrition.proteins * 4) + (meal_nutrition.fats * 9)

def create_meal(db: Session, data: CreateMealRequest):
    calculated_calories = calcualte_meal_calories(meal_nutrition=data.nutrition)

    nutrition = MealNutrition(
        proteins=data.nutrition.proteins, 
        carbohydrates=data.nutrition.carbohydrates,
        fats=data.nutrition.fats,

        calories=calculated_calories,
        cholesterol=data.nutrition.cholesterol,
        fiber=data.nutrition.fiber,
        sugar=data.nutrition.sugar,
        sodium=data.nutrition.sodium
    )

    meal = Meal(name=data.meal.name, type=data.meal.type, estimated_cooking_time=data.meal.estimated_cooking_time)
    meal.nutrition = nutrition

    db.add(meal)
    db.flush()
    db.refresh(meal)

    nutrition.meal_id = meal.id
    
    db.add(nutrition)
    db.commit()

    db.refresh(nutrition)
    db.refresh(meal)

    return meal
    


