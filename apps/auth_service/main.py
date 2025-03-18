import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import config

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api.auth import router as auth_router

app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=config.AUTH_PORT, reload=True)
