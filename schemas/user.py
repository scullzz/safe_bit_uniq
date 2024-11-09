from pydantic import BaseModel

class UserData(BaseModel):
     age: int
     weight: float
     height: float
     gender: str
     active_factor: float