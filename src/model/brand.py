from .abc import db, BaseModel


class Brand(db.Model, BaseModel):
    """Brand model"""
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
