"""
Define the REST verbs relative to the product
"""
from flask import request
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument

from .abc import BaseResource
from model import Product, ProductSupermarket, Supermarket


class ProductCountResource(BaseResource):
    """Base functions relative to product count."""

    def get(self, supermarket_id):
        """Get number of products in supermarket."""

        return Product.query \
            .join(ProductSupermarket, ProductSupermarket.product_id == Product.id) \
            .join(Supermarket, ProductSupermarket.supermarket_id == Supermarket.id) \
            .filter(Supermarket.id == supermarket_id) \
            .count()
