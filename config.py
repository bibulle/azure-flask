import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sql-server-1234.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'db1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'bob'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Bib1Bib1Bib1'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'mystorageaccountaaa'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '3xhagmvSMl62gioMdwnMikHbAlYAudnpQMk67t8xdKShcQougisCzzqwBzsXgjBW3qKmg5yp0Bz3+ASttU8q4g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
