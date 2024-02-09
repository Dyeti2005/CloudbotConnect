import os

class ProductionConfig:
    SECRET_KEY = os.urandom(256)
    DEBUG = True