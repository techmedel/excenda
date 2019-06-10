from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas
import os
import routes

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__) 
CORS(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.register_blueprint(routes.get_blueprint())

if __name__ == '__main__': 
    if not pandas.isnull(os.environ.get('PORT')):
        app.run(port = os.environ.get('PORT'))
    else:
        app.run(port = '5400') 