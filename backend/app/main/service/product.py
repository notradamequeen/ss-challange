import json

from app.main.exception import NotFoundError
from app.main.model import (
    Image,
    Product,
    ImageInfo,
    ProductInfo,
    db
)

from app.main.service.image import ImageManager
from app.main.service.transaction import Transaction


class ProductManager:
    @classmethod
    def get_products(cls):
        products = Product.query.all()
        return list(
            map(
                lambda product: ProductMapper.map_product_obj_to_json(product),
                products
            )
        )

    @classmethod
    def get_product_by_id(cls, product_id):
        product = Product.query.get(product_id)
        if not product:
            raise NotFoundError(id=product_id, message='Product not found')
        return ProductMapper.map_product_obj_to_json(product)

    @classmethod
    def generate_product(cls, product: ProductInfo):
        with Transaction(db.session) as session:
            product_obj = Product(
                name=product.name,
                description=product.description
            )
            logo = product.logo.img_file
            image_manager = ImageManager()
            if logo:
                logo_url = image_manager.populate_upload(logo)
                product_obj.logo = Image(url=logo_url)

            for image in product.images:
                image_url = image_manager.populate_upload(image.img_file)
                product_obj.images.append(Image(url=image_url))

            session.add(product_obj)
            session.commit()
            image_manager.upload()
            return product_obj

    @classmethod
    def update_product(cls, product_id: int, product: ProductInfo) -> Product:
        with Transaction(db.session) as session:
            image_manager = ImageManager()
            product_obj = Product.query.get(product_id)
            if product_obj is None:
                raise Exception('not found')

            product_obj.name = product.name
            product_obj.description = product.description
            deleted_logo = None

            if product.logo and product.logo.img_file:
                if product_obj.logo:
                    deleted_logo = product_obj.logo
                    image_manager.populate_removal(product_obj.logo.url)

                logo_url = image_manager.populate_upload(product.logo.img_file)
                product_obj.logo = Image(url=logo_url)

            if not product.logo and product_obj.logo:
                deleted_logo = product_obj.logo
                image_manager.populate_removal(product_obj.logo.url)
                product_obj.logo = None

            image_obj_ids = [img.id for img in product_obj.images]
            image_ids = [img.id for img in product.existing_images]
            deleted_image_ids = set(image_obj_ids).difference(set(image_ids))
            deleted_images = Image.query.filter(
                Image.id.in_(tuple(deleted_image_ids))
            )

            for deleted_image in deleted_images:
                product_obj.images.remove(deleted_image)
                image_manager.populate_removal(deleted_image.url)

            for existing_image in product.existing_images:
                existing_image_obj = Image.query.get(existing_image.id)
                existing_image_obj.url = existing_image.url

            for new_image in product.new_images:
                image_url = image_manager.populate_upload(new_image.img_file)
                new_image_obj = Image(url=image_url)
                product_obj.images.append(new_image_obj)

            deleted_images.delete(synchronize_session=False)
            if deleted_logo:
                session.delete(deleted_logo)
            session.commit()
            image_manager.flush()
            image_manager.upload()
            return product_obj


class ProductMapper:
    @classmethod
    def map_json_to_product_info(cls, data: json):
        images = []
        logo = None
        if data.get('images'):
            for image_data in data.get('images'):
                images.append(ImageInfo(img_file=image_data))
        if data.get('logo'):
            logo = ImageInfo(img_file=data.get('logo'))

        return ProductInfo(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            images=images,
            logo=logo
        )

    @classmethod
    def map_object_to_product_info(cls, obj: Product):
        return ProductInfo(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            logo=ImageInfo(id=obj.logo.id, url=obj.logo.url) or None,
            images=list(
                map(
                    lambda image: ImageInfo(id=image.id, url=image.url),
                    obj.images or []
                )
            )
        )

    @classmethod
    def map_product_obj_to_json(cls, product: Product):
        product_data = dict(
            id=product.id,
            name=product.name,
            description=product.description,
            images=[dict(id=img.id, url=img.url) for img in product.images],
            logo=dict(
                id=product.logo.id,
                url=product.logo.url
            ) if product.logo else None,
            created_at=product.created_at.__str__(),
            updated_at=product.updated_at.__str__()
        )
        return product_data


def generate_product_sample(itr: int):
    data = dict(
        name=f'product-{itr}',
        description=f'description product-{itr}',
        logo=dict(url=f'logo-product-{itr}'),
        images=[
            dict(url=f'image1-product-{itr}'),
            dict(url=f'image2-product-{itr}'),
            dict(url=f'image3-product-{itr}')
        ]
    )
    product = ProductMapper.map_json_to_product_info(data)
    return ProductManager.generate_product(product)
