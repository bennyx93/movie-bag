from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
# https://flask.palletsprojects.com/en/2.0.x/blueprints/
# Can use blueprint instead of Api. It is used to better organize the code.
# app.register_blueprint(movies)
initialize_routes(api)

app.run(debug=True)