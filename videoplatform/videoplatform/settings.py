import os
from datetime import timedelta
from pathlib import Path

import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV_PATH = BASE_DIR / '.env'

if ENV_PATH.exists():
    dotenv.load_dotenv(ENV_PATH)


def get_debug():
    debug = os.getenv('DEBUG', '0')
    return True if debug == '1' else False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_debug()

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'corsheaders',
    'debug_toolbar',
    'import_export',
    'rest_framework',
    'drf_spectacular',
    'django_extensions',
    'rest_framework.authtoken',
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
    'school',
    'playlists',
    'hero',
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
    'allauth.account.middleware.AccountMiddleware'
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
            ],
        },
    },
]

WSGI_APPLICATION = 'videoplatform.wsgi.application'


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

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Sites

SITE_ID = 1


# Uploads

DEFAULT_FILE_STORAGE = 'uploads.storage.CustomFileSystemStorage'


# Debug

INTERNAL_IPS = [
    '127.0.0.1'
]


# Models

NOTIFICATION_MODEL = 'notifications.Notification'

MEDIA_MODEL = 'videos.Video'


# CACHE

# https://pypi.org/project/pymemcache/
# https://pypi.org/project/pylibmc/

if DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': BASE_DIR / 'cache'
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient'
            },
            'KEY_PREFIX': 'myyoutube'
        },
        'memcache': {
            'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
            'LOCATION': [
                '127.0.0.1:11211'
            ]
        }
    }

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = [
    # 'axes.backends.AxesStandaloneBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
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


# Django All Auth for more information
# on the settings for django-allauth
# https://docs.allauth.org/en/latest/socialaccount/provider_configuration.html

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APPS': [
            {
                'client_id': '123',
                'secret': '456',
                'key': ''
            }
        ],
        # These are provider-specific settings that can only be
        # listed here:
        'SCOPE': [
            "profile",
            "email",
        ],
        'AUTH_PARAMS': {
            "access_type": "online",
        }
    }
}


# Locales

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

LANGUAGE_CODE = 'fr'


# Celery
# https://docs.celeryq.dev/en/stable/#

if not DEBUG:
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

    REDIS_URL = f'redis://:{REDIS_PASSWORD}@redis:6379'

    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')

    RABBITMQ_USER = os.getenv('RABBITMQ_DEFAULT_USER')

    RABBITMQ_PASSWORD = os.getenv('RABBITMQ_DEFAULT_PASS')

    CELERY_BROKER_URL = 'amqp://{user}:{password}@rabbitmq:5672'.format(
        user=RABBITMQ_USER,
        password=RABBITMQ_PASSWORD
    )

    CELERY_RESULT_BACKEND = f'redis://:{REDIS_PASSWORD}@redis:6379'
else:
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672'

    CELERY_RESULT_BACKEND = 'rpc://'


CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Europe/Oslo'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


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
