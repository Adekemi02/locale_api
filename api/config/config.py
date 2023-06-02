import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient


load_dotenv(find_dotenv())

class Config:
    secret_key = os.environ.get('SECRET_KEY')
    connection_string = os.environ.get('MONGO_CONNECTION_STRING')

class DevConfig(Config):
    DEBUG = os.environ.get('FLASK_DEBUG')

class TestConfig(Config):
    pass
    
class ProdConfig(Config):
    pass

config_dict = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}

