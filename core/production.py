from .development import *

import os
os.environ["PYTHON_ENV"] = "production"
os.environ["DATABASE_URL"] = "postgresql://postgres:azsxdcfvgb@awseb-e-nmpk22gzwr-stack-awsebrdsdatabase-2gwybje6iodk.cbo3ynifpjlw.sa-east-1.rds.amazonaws.com:5432/postgres"
os.environ["HOST"] = "awseb-e-nmpk22gzwr-stack-awsebrdsdatabase-2gwybje6iodk.cbo3ynifpjlw.sa-east-1.rds.amazonaws.com"
os.environ["DATABASE"] = "postgres"
os.environ["USER"] = "postgres"
os.environ["PASSWORD"] = "azsxdcfvgb"

DATABASE_URL = os.environ.get("DATABASE_URL")
HOST = os.environ.get("HOST") 
DATABASE = os.environ.get("DATABASE")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")