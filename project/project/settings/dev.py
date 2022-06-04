from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!w7dx--6k)7cq0skrlo43m-0d@l&_v)^1u0fz@k7nvt%d3$u1@"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wagtail_cms',
        'USER': 'wagtail',
        'PASSWORD': '_dev9001_',
        'HOST': 'db',
        'PORT': '5432',
    }

}

try:
    from .local import *
except ImportError:
    pass
