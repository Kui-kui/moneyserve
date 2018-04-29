"""
Define the REST verbs relative to the supermarket
"""
from flask.ext.restful import Resource

from .abc import BaseResource
from model import Address, Supermarket


class SupermarketResource(BaseResource):
    """Base functions relative to supermarkets."""

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
