from flask import Blueprint, jsonify, current_app
from flask.ext.restful import Api

from resource import CommonResource

COMMON_BLUEPRINT = Blueprint('common', __name__)
Api(COMMON_BLUEPRINT).add_resource(CommonResource, '/routes')
