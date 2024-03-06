from flask import Blueprint # Blueprints organises related contents of the flask app like routes etc...

api_blueprint = Blueprint("api", __name__) # creates a blueprint instance with the name as 'api'

from . import routes # imports the routes associated with the api blueprint