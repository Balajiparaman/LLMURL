from flask import Flask
from flask_cors import CORS # CORS-Cross Origin Resource Sharing
import os

def create_app():
    '''
    Creates the flask application instance with CORS enabled in the dev environment
    '''
    app = Flask(__name__)
    if os.environ.get("FLASK_ENV") == "development": # checks if environment variable is set to development
        CORS(app) # allows the application to accept requests from other origins during development
    from app.api.routes import api_blueprint # api_blueprint contains the route definitions for API endpoints
    app.register_blueprint(api_blueprint) # makes the routes available in api_blueprint to the flask app

    return app




