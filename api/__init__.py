from flask import Flask
from .config.config import config_dict
from .model.db import connect_to_db
from flask_restx import Api
from .routes.views import state_ns, cache
from .routes.auth import auth_ns
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis
from http import HTTPStatus

# rediss://red-cid1esp5rnuhheud2h10:zs5u1nfxArvi4CPlcsBDLftct6WSpL62@oregon-redis.render.com:6379

def create_app(config=config_dict['development']):
    app = Flask(__name__)
    app.config.from_object(config)
    
    CORS(app)

    jwt = JWTManager(app)
    
    db = connect_to_db()

    redis_client = FlaskRedis(app)

    cache.init_app(app, config={
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": app.config['REDIS_URL']
        })
   
    api = Api(app, 
              title='Locale API',  
              description='''
                A simple API for getting states and local governments in Nigeria
              '''
            )
    
    api.add_namespace(state_ns, path='/api/v1')
    api.add_namespace(auth_ns, path='/api/v1')

    @app.errorhandler(429)
    def handle_rate_limit_exception(e):
        return {'message': 'Rate limit exceeded. Too many requests'}, HTTPStatus.TOO_MANY_REQUESTS

    return app
