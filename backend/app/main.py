import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import api_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="ActionAgent",
    description="AI agent backend for student planning, research, and study support.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "service": "ActionAgent",
        "status": "ok",
        "message": "Student task planning and research assistant.",
    }
