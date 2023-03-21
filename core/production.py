from .development import *

import os

DATABASE_URL = os.environ.get("DATABASE_URL")
HOST = os.environ.get("HOST") 
DATABASE = os.environ.get("DATABASE")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")