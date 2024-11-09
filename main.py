from fastapi import FastAPI
from routers import auth, meal, user, restaraunts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(auth.router)
app.include_router(meal.router)
app.include_router(user.router)
app.include_router(restaraunts.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
