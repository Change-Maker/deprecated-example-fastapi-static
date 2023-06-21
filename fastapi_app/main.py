import asyncio
import os
import sys
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger

from routers import home
from utils import config_util, logger_util

WORKING_DIR = os.path.realpath(os.path.dirname(__file__))
CLIENT_DIR = os.path.realpath(os.path.join(WORKING_DIR, "../client"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before FastAPI app start.
    logger.debug("Before FastAPI app start.")
    yield
    # Before FastAPI app shutdown.
    logger.debug("Before FastAPI app shutdown.")


app = FastAPI(lifespan=lifespan)

app.include_router(home.router)

# Serve static files.
app.mount(
    "/",
    StaticFiles(directory=CLIENT_DIR, html=True),
    name="static",
)


async def main():
    uvicorn_config = uvicorn.Config(
        APP,
        settings.uvicorn.host,
        settings.uvicorn.port,
        log_level=settings.uvicorn.log_level,
    )
    logger_util.override_uvicorn_logger()
    server = uvicorn.Server(uvicorn_config)
    await server.serve()


if __name__ == "__main__":
    APP = "main:app"
    settings = config_util.get_settings(
        os.path.join(WORKING_DIR, "configs/settings.json"),
    )
    if settings is None:
        sys.exit(1)

    if settings.logger is not None:
        logger_util.setup_logger(settings.logger)

    if os.environ.get("MODE", "") == "dev":
        logger.info("In development mode.")
        uvicorn.run(
            APP,
            host=settings.uvicorn.host,
            port=settings.uvicorn.port,
            reload=True,
            log_level=settings.uvicorn.log_level,
        )
    else:
        asyncio.run(main())
