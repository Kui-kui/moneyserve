from .abc import db, BaseModel


class Supermarket(db.Model, BaseModel):
    """Supermarket model"""
    __tablename__ = 'supermarket'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
