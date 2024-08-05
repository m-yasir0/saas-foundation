from .development import *
DEBUG = False
ALLOWED_HOSTS = ['.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}
