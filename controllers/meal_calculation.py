from schemas.meal import MealSchema, MealNutritionSchema, HealthGoalType
from sqlalchemy.orm import Session
from models.meal import Meal


def calcualte_meal_calories(meal_nutrition: MealNutritionSchema):
    return (meal_nutrition.carbohydrates) * 4 + (meal_nutrition.proteins * 4) + (meal_nutrition.fats * 9)

def generate_meal_recommendation(db: Session, goal: HealthGoalType):
    
    offset = 0
    chunk_size = 10

    matching_meals = []

    while True:
        meals = db.query(Meal).offset(offset).limit(chunk_size).all()
        
        if not meals:
            break

        for current_meal in meals:

            current_nutrition = current_meal.nutrition
            print(current_nutrition)

        
        # Move to the next chunk
        offset += chunk_size
