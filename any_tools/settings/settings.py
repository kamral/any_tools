import os
from urllib.parse import urlparse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third - party modules
    'rest_framework',
    'drf_yasg',
    'django_filters',

    # Local apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'any_tools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'any_tools.wsgi.application'


class DSN(object):
    def __init__(self, dsn):
        self._uri = urlparse(dsn)

    def get_django_db_settings(self):
        return dict(
            ENGINE=self._guess_engine(),
            NAME=self.NAME(),
            USER=self.USER(),
            PASSWORD=self.PASSWORD(),
            HOST=self.HOST(),
            PORT=self.PORT(),
        )

    def _guess_engine(self):
        scheme = self._uri.scheme

        if scheme == 'postgres':
            return 'django.db.backends.postgresql'

    def NAME(self):
        return self._uri.path.lstrip('/')

    def USER(self):
        return self._uri.username

    def PASSWORD(self):
        return self._uri.password

    def HOST(self):
        return self._uri.hostname

    def PORT(self):
        return self._uri.port


DATABASES = {
    'default': DSN(os.environ.get('DATABASE_URL', '')).get_django_db_settings(),
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = [
    os.path.abspath(os.path.join(PROJECT_ROOT, 'staticfiles')),
]
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {

   }
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}
