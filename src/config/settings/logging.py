from config.env import env

handlers = {
    "console": {
        "level": "ERROR",
        "class": "logging.StreamHandler",
        "formatter": "verbose",
    },
    "file": {
        "level": "ERROR",
        "class": "logging.FileHandler",
        "filename": "debug.log",
        "formatter": "verbose",
    },
}

loggers = {
    "": {
        "handlers": ["file", "console"],
        "level": "DEBUG",
        "propagate": True,
    },
    "django.request": {
        "handlers": ["file", "console"],
        "level": "INFO",
        "propagate": False,
    },
}

root = {
    "level": "DEBUG",
    "handlers": ["console"],
}

USE_GRAYLOG = env.bool("USE_GRAYLOG", False)
if USE_GRAYLOG:
    handlers["graypy"] = {
        "level": "DEBUG",
        "class": "graypy.GELFUDPHandler",
        "host": env.str("GELF_UDP_ADDRESS", "graylog"),
        "port": env.int("GELF_UDP_PORT", 12201),
    }
    loggers[""]["handlers"].append("graypy")
    loggers["django.request"]["handlers"].append("graypy")
    root["handlers"].append("graypy")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s|%(asctime)s|%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "root": root,
    "handlers": handlers,
    "loggers": loggers,
}
