from .base import *
import os
import sys
import dj_database_url

DEBUG = os.getenv("DEBUG", "False") == "True"


DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

if os.getenv("DATABASE_URL", None) is None:
    raise Exception("DATABASE_URL environment variable not defined")
DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
}


try:
    from .local import *
except ImportError:
    pass
