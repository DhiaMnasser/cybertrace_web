from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cybertrace_web',
        'USER':'cybertrace',
        'PASSWORD':'cybertrace',
        'HOST':'db',
        'PORT': 3306,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'cybertrace.log'),
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 10,
        },
        
    },
    'loggers': {
        'django.request': {
            'handlers': ['applogfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'cybertrace': {
            'handlers': ['applogfile',],
            'level': 'DEBUG',
        },
    }
}

with open('.secret_key', 'rb') as myfile:    
    SECRET_KEY = myfile.read()

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
