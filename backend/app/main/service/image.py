import os
from werkzeug.utils import secure_filename

from app.main.config import Config
from werkzeug import FileStorage


class ImageManager:
    def __init__(self):
        self.upload_folder = Config.UPLOAD_FOLDER
        self.removal_images = []
        self.upload_images = []

    def _get_image_path(self, image):
        filename = secure_filename(image.filename)
        path = os.path.join(self.upload_folder, filename)
        return path

    def upload(self):
        for image in self.upload_images:
            path = self._get_image_path(image)
            image.save(path)

    def flush(self):
        for image_url in self.removal_images:
            os.remove(image_url)

    def populate_removal(self, image_url):
        self.removal_images.append(image_url)

    def populate_upload(self, image: FileStorage):
        self.upload_images.append(image)
        return self._get_image_path(image)
