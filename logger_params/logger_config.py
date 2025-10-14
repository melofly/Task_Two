import logging
import os

class LoggerConfig:
    LOGS_DIR_NAME = "logs"
    LOGGER_NAME = "TestLogger"
    LOGS_FILE_NAME = os.path.join(LOGS_DIR_NAME, "tests.log")
    LOGS_LEVEL = logging.INFO

    MAX_BYTES = 100000
    BACKUP_COUNT = 5

    FORMAT = "[%(asctime)s] [%(levelname)s] - %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"