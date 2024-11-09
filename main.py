from fastapi import FastAPI
from routers import user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
