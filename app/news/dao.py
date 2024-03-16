from app.news.model import News
from app.dao.base import BaseDAO


class NewsDAO(BaseDAO):
    model = News
