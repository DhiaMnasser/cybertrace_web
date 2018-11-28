from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cybertrace_web',
        'USER':'cybertrace',
        'PASSWORD':'cybertrace',
        'HOST':'cybertrace_db',
    }
}

#ALLOWED_HOSTS = ['nginx']

try:
    from .local import *
except ImportError:
    pass
