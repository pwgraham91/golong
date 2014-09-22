__author__ = 'GoldenGate'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'golong', }
}
INTERNAL_IPS = ("127.0.0.1", "10.0.2.2")

STATIC_URL = '/static/'