import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from logger_params.logger_config import LoggerConfig

class Logger:
    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)

    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)

    __file_handler = RotatingFileHandler(
        LoggerConfig.LOGS_FILE_NAME,
        maxBytes=LoggerConfig.MAX_BYTES,
        backupCount=LoggerConfig.BACKUP_COUNT,
        encoding="utf-8"
    )

    __stream_handler = logging.StreamHandler(sys.stdout)

    __formatter = logging.Formatter(
        LoggerConfig.FORMAT,
        LoggerConfig.DATETIME_FORMAT
    )
    __file_handler.setFormatter(__formatter)
    __stream_handler.setFormatter(__formatter)

    __logger.addHandler(__file_handler)
    __logger.addHandler(__stream_handler)

    @staticmethod
    def set_level(level: str | int) -> None:
        Logger.__logger.setLevel(level)

    @staticmethod
    def info(message: str) -> None:
        Logger.__logger.info(message)

    @staticmethod
    def debug(message: str) -> None:
        Logger.__logger.debug(message)

    @staticmethod
    def warning(message: str) -> None:
        Logger.__logger.warning(message)

    @staticmethod
    def error(message: str) -> None:
        Logger.__logger.error(message)

    @staticmethod
    def critical(message: str) -> None:
        Logger.__logger.critical(message)