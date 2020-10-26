from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restplus import Api

from .config import config_by_name
from .api.product import ProductListAPI, ProductDetailAPI
from .api.variant import VariantListAPI, VariantDetailAPI
from .model import db


flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    api = Api(
        app,
        title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
        version='1.0',
        description='a boilerplate for flask restplus web service'
    )
    api.add_resource(ProductListAPI, '/products/')
    api.add_resource(ProductDetailAPI, '/products/<int:product_id>/')
    api.add_resource(VariantListAPI, '/product/<int:product_id>/variants/')
    api.add_resource(VariantDetailAPI, '/variant/<int:variant_id>/')
    print(api.urls)
    flask_bcrypt.init_app(app)

    return app
