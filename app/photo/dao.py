from app.photo.model import Photo
from app.dao.base import BaseDAO


class PhotoDAO(BaseDAO):
    model = Photo