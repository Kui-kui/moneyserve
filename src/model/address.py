from .abc import db, BaseModel


class Address(db.Model, BaseModel):
    """Address model."""
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120))
    postal_code = db.Column(db.String(120))
    city = db.Column(db.String(120))
    country = db.Column(db.String(120))
