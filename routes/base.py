from fastapi import APIRouter, FastAPI
import os
base_router = APIRouter(
    prefix="/api/v1", # Set a prefix for all routes in this router
    tags=["Base Endpoints"]  # Give a tag for all routes in this router)
    )

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME"),
    app_version = os.getenv("APP_VERSION")
    return {"app_name": app_name,
            "app_version": app_version,
            "message": "Welcome to the Mini RAG Application!"}

