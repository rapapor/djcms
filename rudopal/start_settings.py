from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["rudopal.pl","www.rudopal.pl", "rudopal109.usermd.net"] 


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


LOCALE_PATHS = (
        '/usr/home/rudopal109/apps/djcms/locale',
)
