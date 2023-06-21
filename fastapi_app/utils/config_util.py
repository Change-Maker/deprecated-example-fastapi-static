import os

from loguru import logger
from pydantic import BaseModel, constr, Required, ValidationError


class LoggerSettings(BaseModel):
    enable: bool = Required
    path: str = Required
    level: constr(to_upper=True) = Required
    encoding: str = Required
    rotation: str = Required
    retention: str = Required
    compression: str = Required
    format: str = Required


class UvicornSettings(BaseModel):
    host: str = Required
    port: int = Required
    log_level: str = Required


class Settings(BaseModel):
    logger: LoggerSettings | None
    uvicorn: UvicornSettings = Required


def get_settings(config_path: str) -> Settings | None:
    config_relpath = os.path.relpath(config_path)
    try:
        return Settings.parse_file(config_path)
    except ValidationError as validation_err:
        logger.error(
            f"The content of '{config_relpath}' is invalid: {validation_err}")
    except Exception as err:
        logger.error(f"Failed to get settings: {err}")
