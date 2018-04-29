from .abc import db, BaseModel


class Product(db.Model, BaseModel):
    """Product model"""
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(
        db.Integer,
        db.ForeignKey('brand.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False
    )
    name = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
