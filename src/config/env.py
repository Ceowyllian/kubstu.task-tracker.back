import os

import environ

__all__ = [
    "env",
    "BASE_DIR",
]

env = environ.FileAwareEnv()

BASE_DIR = environ.Path(__file__) - 2
env.read_env(os.path.join(BASE_DIR, ".env"))
env.read_env(env.str("ENV_PATH", ".env"))
