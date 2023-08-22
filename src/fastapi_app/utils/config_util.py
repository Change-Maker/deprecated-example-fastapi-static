import os

from loguru import logger
from pydantic import BaseModel, constr, ValidationError


class LoggerSettings(BaseModel):
    enable: bool
    path: str
    level: constr(to_upper=True)
    encoding: str
    rotation: str
    retention: str
    compression: str
    format: str


class UvicornSettings(BaseModel):
    host: str
    port: int
    log_level: str


class Settings(BaseModel):
    logger: LoggerSettings | None
    uvicorn: UvicornSettings


def get_settings(config_path: str) -> Settings | None:
    config_relpath = os.path.relpath(config_path)
    try:
        with open(config_relpath, "r") as f:
            return Settings.model_validate_json(f.read())
    except ValidationError as validation_err:
        logger.error(
            f"The content of '{config_relpath}' is invalid: {validation_err}")
    except Exception as err:
        logger.error(f"Failed to get settings: {err}")
