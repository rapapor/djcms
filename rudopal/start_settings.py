from .settings import *

DEBUG = False

ALLOWED_HOSTS = ["rudopal.pl"] #wpisac nazwe domeny



STATIC_URL = '/public/static/'
MEDIA_URL = '/public/media/'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'production.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}