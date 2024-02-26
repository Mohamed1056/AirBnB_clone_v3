#!/usr/bin/python3
'''Script to make index file.'''

from api.v1.views import app_views
import models
from models.base_moodel import BaseModel
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def return_status():
    '''returns the status.'''
    return jsonify(status='OK')
