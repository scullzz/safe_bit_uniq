from fastapi import FastAPI
from routers import auth, meal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(auth.router)
app.include_router(meal.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
