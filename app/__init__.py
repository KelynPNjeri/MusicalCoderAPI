from flask import Flask, Blueprint
from instance.config import APP_CONFIG


def create_app(app_config):
    app = Flask(__name__)
    
    return app
