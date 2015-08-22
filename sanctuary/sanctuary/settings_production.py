from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gyeepost',
        'USER': os.environ["OPENSHIFT_POSTGRESQL_DB_USERNAME"],
        'PASSWORD': os.environ["OPENSHIFT_POSTGRESQL_DB_PASSWORD"],
        'HOST': os.environ["OPENSHIFT_POSTGRESQL_DB_HOST"],
        'PORT': os.environ["OPENSHIFT_POSTGRESQL_DB_PORT"],
    }
}
