import base64
import io
from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from minio import Minio
from models import Restaurant, Category, Dish
from schemas.restaraunts import (
    CreateRestaurantRequest, CreateCategoryRequest, CreateDishRequest,
    RestaurantResponse, CategoryResponse, DishResponse
)
from models.database import get_pg_db
from services.minio_client import get_minio_client

# Define MinIO bucket names
BUCKET_NAME_RESTAURANT = "restaurant-image"
BUCKET_NAME_DISH = "dish-image"

router = APIRouter(prefix="/restaurants", tags=['restaurants'])

# Create Restaurant
@router.post("/create", response_model=RestaurantResponse)
def create_restaurant(data: CreateRestaurantRequest, db: Session = Depends(get_pg_db), minio: Minio = Depends(get_minio_client)):
    object_name = None
    if data.image:
        logo_data = base64.b64decode(data.image)
        if not minio.bucket_exists(BUCKET_NAME_RESTAURANT):
            minio.make_bucket(BUCKET_NAME_RESTAURANT)
        logo_stream = io.BytesIO(logo_data)
        object_name = "restaurant_logo_" + str(uuid.uuid4())
        minio.put_object(
            bucket_name=BUCKET_NAME_RESTAURANT,
            object_name=f"{object_name}.jpg",
            data=logo_stream,
            length=len(logo_data),
            content_type="image/png",
        )
    restaurant = Restaurant(
        name=data.name,
        description=data.description,
        image_bucketname=BUCKET_NAME_RESTAURANT if object_name else None,
        image_filename=object_name if object_name else None
    )
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant

# Get All Restaurants
@router.get("/get-all", response_model=List[RestaurantResponse])
def get_restaurants(db: Session = Depends(get_pg_db)):
    return db.query(Restaurant).all()

# Get One Restaurant by ID
@router.get("/get-one/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_pg_db)):
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    return restaurant

# Create Category
@router.post("/create-categories", response_model=CategoryResponse)
def create_category(data: CreateCategoryRequest, db: Session = Depends(get_pg_db)):
    restaurant = db.query(Restaurant).filter(Restaurant.id == data.restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Restaurant not found")
    category = Category(name=data.name, restaurant_id=data.restaurant_id)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

# Get All Categories
@router.get("/list-categories", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_pg_db)):
    return db.query(Category).all()

# Get One Category by ID
@router.get("/get-one-categories/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_pg_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category

# Create Dish
@router.post("/create-dishes", response_model=DishResponse)
def create_dish(data: CreateDishRequest, db: Session = Depends(get_pg_db), minio: Minio = Depends(get_minio_client)):
    object_name = None
    category = db.query(Category).filter(Category.id == data.category_id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    if data.image:
        image_data = base64.b64decode(data.image)
        if not minio.bucket_exists(BUCKET_NAME_DISH):
            minio.make_bucket(BUCKET_NAME_DISH)
        image_stream = io.BytesIO(image_data)
        object_name = "dish_" + str(uuid.uuid4())
        minio.put_object(
            bucket_name=BUCKET_NAME_DISH,
            object_name=f"{object_name}.jpg",
            data=image_stream,
            length=len(image_data),
            content_type="image/png",
        )
    dish = Dish(
        name=data.name,
        description=data.description,
        price=data.price,
        calories=data.calories,
        category_id=data.category_id,
        image_bucketname=BUCKET_NAME_DISH if object_name else None,
        image_filename=object_name if object_name else None
    )
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish

# Get All Dishes
@router.get("/list-dishes", response_model=List[DishResponse])
def get_dishes(db: Session = Depends(get_pg_db)):
    return db.query(Dish).all()

# Get One Dish by ID
@router.get("/get-one-dishes/{dish_id}", response_model=DishResponse)
def get_dish(dish_id: int, db: Session = Depends(get_pg_db)):
    dish = db.query(Dish).filter(Dish.id == dish_id).first()
    if not dish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dish not found")
    return dish
