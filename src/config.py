import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or str(os.uname(24))
