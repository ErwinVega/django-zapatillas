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

# FIXME: CACHES SETTINS
print("REDIS_PUBLIC_URL:", os.environ.get('REDIS_PUBLIC_URL'))
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_PUBLIC_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 100,
                "retry_on_timeout": True,  
            },
            "SERIALIZER_CLASS": "django_redis.serializers.msgpack.MSGPackSerializer",
            "COMPRESSOR_CLASS": "django_redis.compressors.zlib.ZlibCompressor",

            
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

            