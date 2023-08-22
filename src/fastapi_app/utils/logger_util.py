import logging

from loguru import logger

from utils.config_util import LoggerSettings


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(
            depth=depth,
            exception=record.exc_info,
        ).log(level, record.getMessage())


def setup_logger(
        logger_settings: LoggerSettings,
        disable_console_log: bool = False,
        ):
    if disable_console_log:
        logger.remove()

    if logger_settings.enable:
        logger.add(
            sink=logger_settings.path,
            level=logger_settings.level,
            encoding=logger_settings.encoding,
            enqueue=True,
            rotation=logger_settings.rotation,
            retention=logger_settings.retention,
            compression=logger_settings.compression,
            format=logger_settings.format,
        )


def override_uvicorn_logger():
    for name in ("uvicorn", "uvicorn.access"):
        logging.getLogger(name).handlers = [InterceptHandler()]
