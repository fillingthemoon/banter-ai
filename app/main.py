import logging

from fastapi import FastAPI
from app.routers.main import router as main_router

LOGGING_FORMAT = (
    "%(asctime)s - %(name)s - %(funcName)s:%(lineno)d - %(levelname)s - %(message)s"
)

logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)


def get_application() -> FastAPI:
    application = FastAPI()

    application.include_router(main_router)

    return application


app = get_application()
