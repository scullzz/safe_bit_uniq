from enum import Enum
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

from models.base import BaseModel


class Restaurant(BaseModel):
    __tablename__ = "restaurants"

    name = Column(String, nullable=False)
    image_bucketname = Column(String)
    image_filename = Column(String)
    description = Column(String)

    # Relationship to categories
    categories = relationship("Category", back_populates="restaurant")

class Category(BaseModel):
    __tablename__ = "categories"

    name = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id", ondelete="CASCADE"))

    # Relationship to the restaurant and dishes
    restaurant = relationship("Restaurant", back_populates="categories")
    dishes = relationship("Dish", back_populates="category")

class Dish(BaseModel):
    __tablename__ = "dishes"

    name = Column(String, nullable=False)
    description = Column(String)
    image_bucketname = Column(String)
    image_filename = Column(String)
    calories = Column(Float)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))

    # Relationship to category
    category = relationship("Category", back_populates="dishes")