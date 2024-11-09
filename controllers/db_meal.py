from schemas.meal import MealSchema, MealNutritionSchema, HealthGoalType, CreateMealRequest
from sqlalchemy.orm import Session
from models.meal import Meal, MealNutrition
from minio import Minio
import uuid
import base64
import io

BUCKET_NAME = "meal-image"

def calcualte_meal_calories(meal_nutrition: MealNutritionSchema):
    return (meal_nutrition.carbohydrates) * 4 + (meal_nutrition.proteins * 4) + (meal_nutrition.fats * 9)

def create_meal(db: Session, data: CreateMealRequest, minio_client: Minio ):
    calculated_calories = calcualte_meal_calories(meal_nutrition=data.nutrition)

    object_name = None

    if data.image:
        image_data = base64.b64decode(data.image)

        if not minio_client.bucket_exists(BUCKET_NAME):
            minio_client.make_bucket(BUCKET_NAME)

        image_stream = io.BytesIO(image_data)
        object_name = "food_" + str(uuid.uuid4())

        minio_client.put_object(
            bucket_name=BUCKET_NAME,
            object_name=f"{object_name}.jpg",
            data=image_stream,
            length=len(image_data),
            content_type="image/png",
        )

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

    meal = Meal(
        name=data.meal.name, type=data.meal.type, 
        estimated_cooking_time=data.meal.estimated_cooking_time, 
        image_bucketname=BUCKET_NAME,
        image_filename=object_name
    )
    
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
    


