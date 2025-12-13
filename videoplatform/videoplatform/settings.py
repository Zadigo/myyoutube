import os
from datetime import timedelta
from pathlib import Path
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR / '.env'

if ENV_PATH.exists():
    dotenv.load_dotenv(ENV_PATH)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',

    'corsheaders',
    'debug_toolbar',
    'import_export',
    'rest_framework',
    'drf_spectacular',
    'django_extensions',
    'rest_framework.authtoken',
    'graphene_django',
    # 'axes',

    'accounts',
    'mediastats',
    'uploads',
    'donations',
    'reports',
    'videos',
    'stories',
    'ratings',
    'comments',
    'notifications',
    'mychannel',
    'history',
    'playlists'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'axes.middleware.AxesMiddleware'
]

ROOT_URLCONF = 'videoplatform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

ASGI_APPLICATION = 'videoplatform.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

USE_S3 = False

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = BASE_DIR / 'media'


def aws_endpoint(path=None):
    base_url = 'https://{bucket}.s3.{region}.amazonaws.com'

    bucket = os.getenv('AWS_S3_REGION_NAME')
    region = os.getenv('AWS_S3_REGION_NAME')
    url = base_url.format(bucket=bucket, region=region)

    if path is not None:
        return url + f'/{path}'

    return url


if USE_S3:
    # S3 Backend Storage
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
    # https://forum.djangoproject.com/t/storage-4-2-how-to-subclass-default/29190/2
    # FIXME: https://github.com/jschneier/django-storages/issues/1361 there seems to
    # be a bug when trying to access the admin with DEBUG

    DEFAULT_S3_SETTINGS = {
        'access_key': os.getenv('AWS_S3_ACCESS_KEY_ID'),
        'secret_key': os.getenv('AWS_S3_SECRET_ACCESS_KEY'),
        'bucket_name': os.getenv('AWS_STORAGE_BUCKET_NAME'),
        'region_name': os.getenv('AWS_S3_REGION_NAME'),
        'object_parameters': {'CacheControl': 'max-age=86400'},
        'endpoint_url': aws_endpoint(),
        # 'cloudfront_key': '',  # AWS_CLOUDFRONT_KEY
        # 'cloudfront_key_id': '',  # AWS_CLOUDFRONT_KEY_ID
        'querystring_auth': False,
        'default_acl': 'public-read'
    }

    STORAGES = {
        'default': {
            'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
            'OPTIONS': {
                **DEFAULT_S3_SETTINGS,
                'location': 'media',
            }
        },
        'staticfiles': {
            'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
            'OPTIONS': {
                **DEFAULT_S3_SETTINGS,
                'file_overwrite': True,
                'location': 'static',
            }
        }
    }

    MEDIA_ROOT = aws_endpoint('media')


MEDIA_URL = 'media/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]


# Sites

SITE_ID = 1


# Debug

INTERNAL_IPS = [
    '127.0.0.1'
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    # 'axes.backends.AxesStandaloneBackend',
    'accounts.backends.EmailAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend'
]


EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# Axes
# https://django-axes.readthedocs.io/en/latest/2_installation.html

AXES_ENABLED = False

AXES_FAILURE_LIMIT = 4

AXES_RESET_ON_SUCCESS = True

AXES_CACHE = 'memcache'

# ATOMIC_REQUESTS = False


# Rest framework:
# https://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

# Cors:
# https://pypi.org/project/django-cors-headers/

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:3000',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173'
    'http://localhost:3000',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ['Token']
}

# Locales

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

LANGUAGE_CODE = 'fr'


# Celery + Redis
# https://docs.celeryq.dev/en/stable/

# Redis default user requires a default
# password to establish the connection:
# https://github.com/redis/redis/issues/13437

REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')

REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:6379'

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')

RABBITMQ_USER = os.getenv('RABBITMQ_DEFAULT_USER', 'guest')

RABBITMQ_PASSWORD = os.getenv('RABBITMQ_DEFAULT_PASS', 'guest')

CELERY_BROKER_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:5672'

CELERY_RESULT_BACKEND = REDIS_URL

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Europe/Oslo'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


# Caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_URL,
        'KEY_PREFIX': 'myyoutube'
    }
}


# HTTPS

if os.getenv('USES_HTTP_SCHEME', 'http') == 'https':
    SESSION_COOKIE_SECURE = True

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    SECURE_PROXY_SSL_HEADERSSL_REDIRECT = True


# N8N

N8N_HOST = os.getenv('N8N_HOST')

N8N_TEST_API_URL = 'http://n8n.gency313.fr/webhook-test/'

N8N_API_URL = 'http://n8n.gency313.fr/webhook/'

N8N_AUTHENTICATION_TOKEN = os.getenv('N8N_AUTHENTICATION_TOKEN')

N8N_REQUEST_USERNAME = os.getenv('N8N_REQUEST_USERNAME')

N8N_REQUEST_PASSWORD = os.getenv('N8N_REQUEST_PASSWORD')


# Fixtures

FIXTURE_DIRS = [
    'fixtures/videos'
]

GOOGLE_CLOUD_PROJECT = 'gency313'


# Firebase

FIREBASE_PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID')


# Schema

GRAPHENE = {
    'SCHEMA': "videoplatform.schema.schema"
}
