from flask import request
from flask_restplus import Resource
from app.main.exception import NotFoundError
from app.main.service.product import ProductMapper, ProductManager


class ProductListAPI(Resource):
    def get(self):
        return ProductManager.get_products()

    def post(self):
        """Creates a new Product """
        data = request.form.to_dict()
        data['logo'] = request.files.get('logo')
        data['images'] = request.files.getlist('images[]')
        product_info = ProductMapper.map_json_to_product_info(data)
        product = ProductManager.generate_product(product_info)
        return ProductMapper.map_product_obj_to_json(product)


class ProductDetailAPI(Resource):
    def get(self, product_id):
        try:
            return ProductManager.get_product_by_id(product_id)
        except NotFoundError as e:
            return f'{e.message}: {e.payload}', e.status_code

    def put(self, product_id):
        data = request.form.to_dict()
        data['logo'] = request.files.get('logo')
        data['images'] = request.files.getlist('images[]')
        product_info = ProductMapper.map_json_to_product_info(data)
        product = ProductManager.update_product(product_id, product_info)
        return ProductMapper.map_product_obj_to_json(product)
