"""
 settings_test.py
 ----------------
 by Griffon Development Co., Ltd

 Testing settings, specifying test mssql db

"""
from .settings import *  # noqa
from .settings import env

MIGRATION_MODULES = {
    'sqlserver': 'sqlserver.test_migrations',
}

ENV_ROOT_DIR = environ.Path(__file__) - 3
READ_DOT_ENV_FILE = env.bool('READ_DOT_ENV_FILE', default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(f'{BASE_DIR}/.sql')

mssql_host = env('TEST_MSSQL_HOST')
mssql_name = env('TEST_MSSQL_NAME')
mssql_username = env('TEST_MSSQL_USERNAME')
mssql_password = env('TEST_MSSQL_PASSWORD')

DATABASES['mssql_db'] = {
    'ENGINE': 'mssql',
    'HOST': mssql_host,
    'NAME': mssql_name,
    'USER': mssql_username,
    'PASSWORD': mssql_password,
    'PORT': '1433',
    'OPTIONS': {
        'driver': 'ODBC Driver 13 for SQL Server'
      }
}
DATABASES['mssql_db']['ATOMIC_REQUESTS'] = True
