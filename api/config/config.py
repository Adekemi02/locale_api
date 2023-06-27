import os
import redis
from dotenv import load_dotenv, find_dotenv
from datetime import timedelta


load_dotenv(find_dotenv())

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    connection_string = os.environ.get('MONGO_CONNECTION_STRING')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    REDIS_URL = os.environ.get('REDIS_URL')
    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = REDIS_URL
    r = redis.from_url(os.environ['REDIS_URL'])
    r = redis.Redis(host='red-cid1esp5rnuhheud2h10', port=6379, db=0, password=os.environ.get('REDIS_PASSWORD'))
    r.set('key', 'redis-py')
    r.get('key')

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

