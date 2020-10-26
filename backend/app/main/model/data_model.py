from typing import List
from datetime import datetime
from werkzeug import FileStorage


class ImageInfo:
    id: int
    url: str
    img_file: FileStorage

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.url = kwargs.get('url', None)
        self.img_file = kwargs.get('img_file', None)
        super().__init__()


class ProductInfo:
    id: int
    name: str
    description: str
    logo: ImageInfo
    images: List[ImageInfo]
    created_at: datetime
    updated_at: datetime

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.logo = kwargs.get('logo')
        self.images = kwargs.get('images')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        super().__init__()

    @property
    def new_images(self) -> List[ImageInfo]:
        return list(filter(
            lambda image: image.id is None,
            self.images
        ))

    @property
    def existing_images(self) -> List[ImageInfo]:
        return list(filter(
            lambda image: image.id is not None,
            self.images
        ))


class VariantInfo:
    id: int
    name: str
    size: str
    color: str
    product_id: int
    images: List[ImageInfo]
    created_at: datetime
    updated_at: datetime

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name')
        self.size = kwargs.get('size')
        self.color = kwargs.get('color')
        self.product_id = kwargs.get('product_id')
        self.images = kwargs.get('images')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        super().__init__()

    @property
    def new_images(self) -> List[ImageInfo]:
        return list(filter(
            lambda image: image.id is None,
            self.images
        ))

    @property
    def existing_images(self) -> List[ImageInfo]:
        return list(filter(
            lambda image: image.id is not None,
            self.images
        ))
