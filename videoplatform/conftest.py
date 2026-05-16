from django.conf import settings


def pytest_configure():
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            SECRET_KEY='aXDfw6xCDKIFRgz2yzpTgAqFBqVLgSeyOVGayj8KqcJAjG3O96dT7cQPMExxAteX',
            PY_UTILITIES_JWT_SECRET='zpDaqupaQR7SxrEcsoFYOkZQIdJPEim4Sz30zC5oBFGOZwY92FYvVeqqO3Z5Pw6P',
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=[
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
                'videos',
                'stories',
                'ratings',
                'mychannel',
                'history',
                'playlists'
            ],
            MIDDLEWARE=[
                'allauth.account.middleware.AccountMiddleware'
            ],
            AUTH_USER_MODEL='auth.User',
            ROOT_URLCONF='commentsplatform.urls',
            DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
            REST_FRAMEWORK={
                'DEFAULT_AUTHENTICATION_CLASSES': [
                    'rest_framework_simplejwt.authentication.JWTAuthentication',
                    'rest_framework.authentication.TokenAuthentication',
                ],
                'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
            },
            SIMPLE_JWT={
                'AUTH_HEADER_TYPES': ['Token']
            },
            STATIC_URL='/static/',
            CELERY_BROKER_URL='',
            CELERY_RESULT_BACKEND=''
        )
