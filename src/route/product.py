from flask import Blueprint
from flask.ext.restful import Api

from resource import ProductCountResource

PRODUCT_BLUEPRINT = Blueprint('product', __name__)
Api(PRODUCT_BLUEPRINT).add_resource(
    ProductCountResource, '/product/count/<string:supermarket_id>'
)
