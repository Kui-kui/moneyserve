"""
Define the REST verbs relative to the supermarket
"""
from flask import request
from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from sqlalchemy import desc

from .abc import BaseResource
from model import Address, Supermarket


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
        with_address = request.args.get('with_address') == 'true'
        per_page = int(request.args.get('per_page'))
        page = int(request.args.get('page'))

        order_by = request.args.get('order_by')
        order_condition_mapping = {
            'id_asc': Supermarket.id,
            'id_desc': desc(Supermarket.id),
            'name_asc': Supermarket.name,
            'name_desc': desc(Supermarket.name),
        }

        query = Supermarket.query \
            .with_entities(
                Supermarket.id,
                Supermarket.name,
            ) \

        if order_by:
            query = query.order_by(order_condition_mapping[order_by])

        if with_address:
            query = query.outerjoin(Address, Address.id == Supermarket.address_id) \
                .with_entities(
                    Supermarket.id,
                    Supermarket.name,
                    Address.street,
                    Address.postal_code,
                    Address.city,
                    Address.country,
            ) \

        query = query.paginate(page=page, per_page=per_page)

        return [self.results_to_dict(supermarket) for supermarket in query.items]
