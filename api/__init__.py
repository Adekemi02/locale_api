from flask import Flask
from .config.config import config_dict
from .model.db import connect_to_db


def create_app(config=config_dict['development']):
    app = Flask(__name__)
    app.config.from_object(config)

    db = connect_to_db()
   

    
    return app
