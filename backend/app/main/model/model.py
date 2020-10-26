from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


product_images = db.Table(
    'product_images',
    db.Column(
        'image_id',
        db.Integer,
        db.ForeignKey('images.id', ondelete="CASCADE")
    ),
    db.Column(
        'product_id',
        db.Integer,
        db.ForeignKey('products.id', ondelete="CASCADE")
    )
)


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(255), unique=True, nullable=False)
    product_logo = db.relationship(
        "Product",
        uselist=False,
        back_populates="logo"
    )
    product = db.relationship(
        "Product",
        secondary=product_images,
        back_populates="images",
        passive_deletes=True
    )


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    logo_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=True)
    logo = db.relationship("Image", back_populates="product_logo")
    images = db.relationship(
        'Image',
        secondary=product_images,
        back_populates="product",
        cascade="all, delete"
    )
    variants = db.relationship(
        "Variant",
        back_populates="product",
        passive_deletes=True
    )
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )


variant_images = db.Table(
    'variant_images',
    db.Column(
        'image_id',
        db.Integer,
        db.ForeignKey('images.id'),
        primary_key=True
    ),
    db.Column(
        'variant_id',
        db.Integer,
        db.ForeignKey('variants.id'),
        primary_key=True
    )
)


class Variant(db.Model):
    __tablename__ = 'variants'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=True)
    color = db.Column(db.String(25), nullable=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False
    )
    product = db.relationship("Product", back_populates="variants")
    images = db.relationship(
        'Image',
        secondary=variant_images,
        lazy='subquery',
        backref=db.backref('variants', lazy=True)
    )
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )
