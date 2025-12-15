from fastapi import FastAPI
# from dotenv import load_dotenv # Load environment variables from a .env file
# # Specify the .env file to load # we but load_dotenv at the top to ensure env variables are available throughout the app
# The environment variables is saved inside the system environment so I can access them using os.getenv anywhere in the app
from pydantic import BaseModel
from src.routes import base,data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)
