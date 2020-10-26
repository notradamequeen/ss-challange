import json
from app.main.model import (
    Image,
    ImageInfo,
    Variant,
    VariantInfo,
    db
)
from app.main.service.image import ImageManager
from app.main.service.transaction import Transaction


class VariantManager:
    @classmethod
    def get_variants_by_product(cls, product_id: int):
        variants = Variant.query.filter_by(product_id=product_id)
        return list(
            map(
                lambda variant: VariantMapper.map_variant_obj_to_json(variant),
                variants
            )
        )

    @classmethod
    def get_variant_by_id(cls, variant_id: int):
        variant_obj = Variant.query.get(variant_id)
        return VariantMapper.map_variant_obj_to_json(variant_obj)

    @classmethod
    def generate_variant_for_product(cls, variant: VariantInfo) -> Variant:
        with Transaction(db.session) as session:
            image_manager = ImageManager()
            variant_obj = Variant(
                name=variant.name,
                size=variant.size,
                color=variant.color,
                product_id=variant.product_id
            )
            for image in variant.images:
                img_url = image_manager.populate_upload(image.img_file)
                variant_obj.images.append(Image(url=img_url))

            session.add(variant_obj)
            session.commit()
            image_manager.upload()
            return variant_obj

    @classmethod
    def update_variant(cls, variant_id: int, variant: VariantInfo) -> Variant:
        with Transaction(db.session) as session:
            image_manager = ImageManager()
            variant_obj = Variant.query.get(variant_id)

            variant_obj.name = variant.name
            variant_obj.color = variant.color
            variant_obj.size = variant.size

            image_obj_ids = [img.id for img in variant_obj.images]
            image_ids = [img.id for img in variant.existing_images]
            deleted_image_ids = set(image_obj_ids).difference(set(image_ids))
            deleted_images = Image.query.filter(
                Image.id.in_(tuple(deleted_image_ids))
            )

            for deleted_image in deleted_images:
                variant_obj.images.remove(deleted_image)
                image_manager.populate_removal(deleted_image.url)

            for existing_image in variant.existing_images:
                existing_image_obj = Image.query.get(existing_image.id)
                existing_image_obj.url = existing_image.url

            for new_image in variant.new_images:
                image_url = image_manager.populate_upload(new_image.img_file)
                new_image_obj = Image(url=image_url)
                variant_obj.images.append(new_image_obj)

            deleted_images.delete(synchronize_session=False)
            session.commit()
            image_manager.flush()
            image_manager.upload()
            return variant_obj

    @classmethod
    def remove_variant(cls, variant_id: int):
        with Transaction(db.session) as session:
            variant_obj = Variant.query.get(variant_id)
            image_manager = ImageManager()
            for image in variant_obj.images:
                session.delete(image)
                image_manager.populate_removal(image.url)
            session.delete(variant_obj)
            session.commit()
            image_manager.flush()
            return True


class VariantMapper:
    @classmethod
    def map_json_to_variant_info(cls, data: json) -> VariantInfo:
        images = []
        if data.get('images'):
            for image_data in data.get('images'):
                images.append(ImageInfo(img_file=image_data))

        return VariantInfo(
            id=data.get('id'),
            name=data.get('name'),
            color=data.get('color'),
            size=data.get('size'),
            product_id=data.get('product_id'),
            images=images,
        )

    @classmethod
    def map_obj_to_variant_info(cls, variant: Variant) -> VariantInfo:
        return VariantInfo(
            id=variant.id,
            name=variant.name,
            size=variant.size,
            color=variant.color,
            product_id=variant.product_id,
            images=[Image(id=img.id, url=img.url) for img in variant.images],
            created_at=variant.created_at,
            updated_at=variant.updated_at
        )

    @classmethod
    def map_variant_obj_to_json(cls, variant: Variant):
        return dict(
            id=variant.id,
            name=variant.name,
            size=variant.size,
            color=variant.color,
            product_id=variant.product_id,
            images=[dict(id=img.id, url=img.url) for img in variant.images],
            created_at=variant.created_at.__str__(),
            updated_at=variant.updated_at.__str__()
        )
