# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
from .base import *
from dotenv import load_dotenv
import dj_database_url
import os



load_dotenv()

# print(f"DB_NAME: {os.getenv('DB_NAME')}")
# print(f"DB_USER: {os.getenv('DB_USER')}")
# print(f"DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
# print(f"DB_HOST: {os.getenv('DB_HOST')}")
# print(f"DB_PORT: {os.getenv('DB_PORT')}")

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "neondb",
#         "USER": "neondb_owner",
#         "PASSWORD": "npg_6SKBtYpgIrE9",
#         "HOST": "ep-flat-truth-a5hvoj5r-pooler.us-east-2.aws.neon.tech",
#         "PORT": "5432",
#         'OPTIONS': {
#             'sslmode': 'require',
#         },
#     }
# }
print("DATABASE_URL:", os.environ.get('DATABASE_URL'))


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}