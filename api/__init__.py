from flask import Flask
from .config.config import config_dict
from .model.db import connect_to_db
from flask_restx import Api
from .routes.views import state_ns


def create_app(config=config_dict['development']):
    app = Flask(__name__)
    app.config.from_object(config)

    db = connect_to_db()
   
    api = Api(app, 
              title='Locale API',  
              description='''
                A simple API for getting states and local governments in Nigeria
              '''
            )
    
    api.add_namespace(state_ns, path='/api/v1')

    
    return app
