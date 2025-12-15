from fastapi import APIRouter, FastAPI, Depends
# Import the Settings class and the get_settings function from your config module
# Settings: Pydantic model for environment/config variables
# get_settings: function that returns a Settings instance for dependency injection
from src.helper.config import get_settings, Settings
import os
# Create a new APIRouter instance
# APIRouter allows us to organize routes in a modular way instead of putting all routes directly in FastAPI app
base_router = APIRouter(
    prefix="/api", # Set a prefix for all routes in this router
    tags=["Base Endpoints"]  # Give a tag for all routes in this router)
    )
# Define a GET route at the path "/api/" (because of the prefix)
@base_router.get("/")
# The `async def` makes this an asynchronous endpoint
async def welcome(
    # FastAPI Dependency Injection: automatically provide a Settings instance
    # get_settings() is called internally and returns Settings with environment variables loaded
    app_settings: Settings = Depends(get_settings)
    ):
    # app_settings = get_settings()
    # app_name = os.getenv("APP_NAME"),
    app_name = app_settings.APP_NAME
    # app_version = os.getenv("APP_VERSION")
    app_version = app_settings.APP_VERSION

    return {"app_name": app_name,
            "app_version": app_version,
            "message": "Welcome to the Application!"}

