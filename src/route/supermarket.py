from flask import Blueprint
from flask.ext.restful import Api

from resource import SupermarketResource, SupermarketsResource

SUPERMARKET_BLUEPRINT = Blueprint('supermarket', __name__)
Api(SUPERMARKET_BLUEPRINT).add_resource(
    SupermarketResource, '/supermarket/<string:supermarket_id>'
)
Api(SUPERMARKET_BLUEPRINT).add_resource(
    SupermarketsResource, '/supermarkets'
)
