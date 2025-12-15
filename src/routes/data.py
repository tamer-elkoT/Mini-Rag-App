from fastapi import FastAPI, APIRouter, Depends, UploadFile
from src.helper.config import get_settings, Settings
import os
# from controllers.DataController import DataController # Import the DataController Class to handle data-related logic
# another way to import the DataController after add it to __init__.py in controllers folder
from src.controllers import DataController


data_router = APIRouter(
    prefix="/api/data",
    tags=["Data Endpoints"],
)
# Define a POST route at the path "/api/data/upload/"
# We will recieve data upload requests here 
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    # Validate the file properties (logic not implemented here) will be inside controllers
    data_controller = DataController()
    is_valid, message = data_controller.validate_uploaded_file(file)

    return {"is_valid": is_valid, "message": message}