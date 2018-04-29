"""
Define the REST verbs relative to the supermarket
"""
from flask import request
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument

from .abc import BaseResource
from model import Address, Supermarket
from util import parse_params


class SupermarketResource(BaseResource):
    """Base functions relative to supermarket."""

    def get(self, supermarket_id):
        """Get supermarket by id."""
        supermarket = Supermarket.query \
            .filter(Supermarket.id == supermarket_id) \
            .outerjoin(Address, Address.id == Supermarket.address_id) \
            .with_entities(
                Supermarket.id,
                Supermarket.name,
                Address.street,
                Address.postal_code,
                Address.city,
                Address.country,
            ) \
            .one()

        if supermarket:
            return self.results_to_dict(supermarket)

        return None


class SupermarketsResource(BaseResource):
    """Base functions relative to supermarkets."""

    def get(self):
        """Get all supermarkets."""
        query = Supermarket.query \
            .outerjoin(Address, Address.id == Supermarket.address_id) \
            .with_entities(
                Supermarket.id,
                Supermarket.name,
                Address.street,
                Address.postal_code,
                Address.city,
                Address.country,
            ) \
            .all()

        return self.result_to_dict_list(query)
