#!/usr/bin/python3
'''Script to create an instance of Flask.'''

from flask import Flask, jsonify
from models import storage
from os import getenv
from api.v1.view import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def downtear(self):
    '''Status of the API.'''
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = 0.0.0.0
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
