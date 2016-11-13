import logging
import logging.handlers
from logging.config import dictConfig

logger = logging.getLogger(__name__)

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}


def configure_logging(logfile_path):
    dictConfig(DEFAULT_LOGGING)

    default_formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s",
            "%d/%m/%Y %H:%M:%S")

    file_handler = logging.handlers.RotatingFileHandler(logfile_path, maxBytes=10485760, backupCount=300,
                                                        encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    file_handler.setFormatter(default_formatter)
    console_handler.setFormatter(default_formatter)

    logging.root.setLevel(logging.DEBUG)
    logging.root.addHandler(file_handler)
    logging.root.addHandler(console_handler)


configure_logging('/tmp/celery.log')
