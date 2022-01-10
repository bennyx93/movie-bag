from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)

# imports requiring app and mail
from resources.routes import initialize_routes

api = Api(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# app.config['MONGODB_SETTINGS'] = {
#  'host': 'mongodb://localhost/movie-bag'
# }

initialize_db(app)
# https://flask.palletsprojects.com/en/2.0.x/blueprints/
# Can use blueprint instead of Api. It is used to better organize the code.
# app.register_blueprint(movies)
initialize_routes(api)