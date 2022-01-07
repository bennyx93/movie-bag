from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
 'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
# app.register_blueprint(movies)
initialize_routes(api)

app.run(debug=True)