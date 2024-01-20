from fastapi import FastAPI
from config.config import settings
from Routers.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum


def get_application() -> FastAPI:
    tags_metadata = [
        {
            'name' : 'CRUD Python FastAPI with DynamoDB',
            'description': 'Basic CRUD with FastAPI and DynamoDB ',
        }
    ]
    
    application = FastAPI(
        title = settings.PROJECT_NAME,
        version = settings.VERSION,
        description = settings.DESCRIPTION,
        openapi_tags = tags_metadata
    )
    
    application.include_router(api_router)
    
    origins = [
        '*',
    ]
    
    application.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ['*'],
        allow_headers = ['*'],
    )
    
    return application

app = get_application()
handler = Mangum(app)