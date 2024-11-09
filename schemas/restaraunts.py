# schemas.py

from pydantic import BaseModel
from typing import Optional

class CreateRestaurantRequest(BaseModel):
    name: str
    description: Optional[str] = None
    image: Optional[str] = None  # Base64 encoded logo image

class CreateCategoryRequest(BaseModel):
    name: str
    restaurant_id: int

class CreateDishRequest(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int
    calories: Optional[float] = None
    image: Optional[str] = None  # Base64 encoded dish image


class RestaurantResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    image_bucketname: Optional[str] = None
    image_filename: Optional[str] = None

    class Config:
        orm_mode = True

class CategoryResponse(BaseModel):
    id: int
    name: str
    restaurant_id: int

    class Config:
        orm_mode = True

class DishResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    calories: Optional[float] = None
    category_id: int
    image_bucketname: Optional[str] = None
    image_filename: Optional[str] = None

    class Config:
        orm_mode = True
