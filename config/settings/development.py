from .base import *

SECRET_KEY = 'django-insecure-%@)0f@4x!j$4m3njii8-)aqkgbgm&87))x=dzp*z@ryczwbvi8'
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
