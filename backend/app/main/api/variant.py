from flask import request
from flask_restplus import Resource
from app.main.service.variant import VariantManager, VariantMapper


class VariantListAPI(Resource):
    def get(self, product_id):
        return VariantManager.get_variants_by_product(product_id)

    def post(self, product_id):
        data = request.form.to_dict()
        data['images'] = request.files.getlist('images[]')
        data['product_id'] = product_id
        variant_info = VariantMapper.map_json_to_variant_info(data)
        variant = VariantManager.generate_variant_for_product(variant_info)
        return VariantMapper.map_variant_obj_to_json(variant)


class VariantDetailAPI(Resource):
    def get(self, variant_id):
        return VariantManager.get_variant_by_id(variant_id)

    def put(self, variant_id):
        data = request.form.to_dict()
        data['images'] = request.files.getlist('images[]')
        variant_info = VariantMapper.map_json_to_variant_info(data)
        variant = VariantManager.update_variant(variant_id, variant_info)
        return VariantMapper.map_variant_obj_to_json(variant)

    def delete(self, variant_id):
        VariantManager.remove_variant(variant_id)
        return 'success delete variant'
