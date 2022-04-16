from .base import *
import os
import sys

DEBUG = False

SECRET_KEY = os.environ['production_secret']




DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'charleswinters',
            'USER': os.environ['db_username'],
            'PASSWORD': os.environ['db_password'],
            'HOST': 'localhost',
            'PORT': '',
        
        }

    }

try:
    from .local import *
except ImportError:
    pass
