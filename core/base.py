from . import development
from . import production
import os

environment = os.environ.get("PYTHON_ENV") or "development"

settings = None


if environment == "production":
    settings = production
if environment == "development":
    settings = development


    
