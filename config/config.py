from pydantic import BaseSettings

class config(BaseSettings):
    CONTAINER_NAME: str = 'CRUD Python FastAPI with DynamoDB'
    VERSION:  str = '0.0.1'
    PROJECT_NAME: str = 'BackEnd Module 1'
    DESCRIPTION: str = 'Resful API -  FastAPI_DynamoDB'
    
settings = config()