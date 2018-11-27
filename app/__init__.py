from flask import Flask, Blueprint
from instance.config import APP_CONFIG


def create_app(app_config):
    """
    Creating an instance of the API.
    """
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[app_config])
    return app
