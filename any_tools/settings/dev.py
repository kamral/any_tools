
import os
from urllib.parse import urlparse
from any_tools.settings.settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')


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
