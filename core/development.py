import datetime


SECRET_KEY = "c5b9efe2f3c63c3d1871efeffe6e12df6644d7f2579482a0658882a90e2b1aceebace4ed8ab6954cf25d6833a7c4ae18f2bc"


SIGNING_KEY = SECRET_KEY

ACCESS_TOKEN_EXPIRATION = datetime.datetime.utcnow() + datetime.timedelta(days=7)
REFRESH_TOKEN_EXPIRATION = datetime.datetime.utcnow() + datetime.timedelta(weeks=8)



DATABASE_URL = "postgresql://postgres:123@localhost:5432/ecommerce"
HOST = "localhost"
DATABASE = "ecommerce"
USER = "postgres"
PASSWORD = 123