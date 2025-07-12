# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "shop",
#         "USER": "postgres",
#         "PASSWORD": "admin",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "neondb",
        "USER": "neondb_owner",
        "PASSWORD": "npg_6SKBtYpgIrE9",
        "HOST": "ep-flat-truth-a5hvoj5r-pooler.us-east-2.aws.neon.tech",
        "PORT": "5432",
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}