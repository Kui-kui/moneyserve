from .abc import db, BaseModel


class ProductSupermarket(db.Model, BaseModel):
    """ProductSupermarket model"""
    __tablename__ = 'product_supermarket'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False
    )
    supermarket_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'supermarket.id',
            onupdate='CASCADE',
            ondelete='CASCADE'
        ),
        nullable=False
    )
