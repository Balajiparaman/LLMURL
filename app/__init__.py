import logging
from flask import Flask
from flask_cors import CORS  # CORS-Cross Origin Resource Sharing
import os


def create_app():
    '''
    Creates the flask application instance with CORS enabled in the dev environment
    '''
    logging.basicConfig(level=logging.DEBUG)

    app = Flask(__name__)
    # checks if environment variable is set to development
    if os.environ.get("FLASK_ENV") == "development":

        # allows the application to accept requests from other origins during development
        CORS(app)
    # api_blueprint contains the route definitions for API endpoints
    from app.api.routes import api_blueprint
    # makes the routes available in api_blueprint to the flask app
    app.register_blueprint(api_blueprint)

    logging.debug("Blueprint registered")

    return app
