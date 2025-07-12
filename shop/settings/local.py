# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
from .base import *
from dotenv import load_dotenv
import os



load_dotenv()

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


# print(f"DB_NAME: {os.getenv('DB_NAME')}")
# print(f"DB_USER: {os.getenv('DB_USER')}")
# print(f"DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
# print(f"DB_HOST: {os.getenv('DB_HOST')}")
# print(f"DB_PORT: {os.getenv('DB_PORT')}")



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}