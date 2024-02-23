from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LuckyHead$default',
        'USER': 'LuckyHead',
        'PASSWORD': 'qwerty10051983',
        'HOST': 'LuckyHead.mysql.pythonanywhere-services.com',
    }
}
