import logging.config

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format':"[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s",
            # 'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }

    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'filters': None,
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': '/tmp/celery.log'
        },

    },
    'loggers': {
        'rpi': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOG_CONFIG)

logger = logging.getLogger("rpi")
