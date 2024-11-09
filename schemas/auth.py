from pydantic import BaseModel

class UserRegistrationRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str

class UserAuthenticationRequest(BaseModel):
    email: str
    password: str


