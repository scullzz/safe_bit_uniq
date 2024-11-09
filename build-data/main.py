import base64
import requests

CREATE_MEAL_REQUEST_URL = "http://0.0.0.0:7575/meal/"

def create_meal_request(
    name: str, type: str, estimated_cooking_time: int, 
    nutritions: dict, ingredients: list[str], image_path: str
):
    base64_string = None
    
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")

    data = {
        "meal": {
            "name": name,
            "type": type,
            "estimated_cooking_time": estimated_cooking_time
        },
        "nutrition": {
            "proteins": nutritions["proteins"],
            "carbohydrates": nutritions["carbohydrates"],
            "fats": nutritions["fats"],
            "fiber": nutritions["fiber"],
            "sugar": nutritions["sugar"],
            "sodium": nutritions["sodium"],
            "cholesterol": nutritions["cholesterol"]
        },
        "ingredients": ingredients,
        "image": base64_string
    }

    response = requests.post(CREATE_MEAL_REQUEST_URL, json=data)

    print(response)


create_meal_request(
    name="Grilled Chicken Caesar Salad",
    type="lunch",
    estimated_cooking_time=15,

    nutritions = {
        "proteins": 30,
        "carbohydrates": 20,
        "fats": 15,
        "fiber": 4,
        "sugar": 5,
        "sodium": 350,
        "cholesterol": 60
    },

    ingredients = [
        "200g grilled chicken breast",
        "2 cups romaine lettuce, chopped",
        "1/4 cup parmesan cheese, grated",
        "1/2 cup cherry tomatoes, halved",
        "1/4 cup Caesar dressing",
        "1/2 cup croutons",
        "1 tbsp olive oil",
        "Salt and pepper to taste"
    ],
    image_path="images/food_01.png"
)

