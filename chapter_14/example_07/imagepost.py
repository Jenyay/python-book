from basepost import BasePost
from mixins import ImageMixin

class ImagePost(BasePost, ImageMixin):
    """Класс поста с картинкой для блога"""

    def __init__(self, author, image):
        print("ImagePost.__init__()")
        BasePost.__init__(self, author)
        ImageMixin.__init__(self, image)
        self._save()

    def _save(self):
        print("Пост с картинкой сохранен.")

    def format(self):
        return f"""    Автор: {self._author}
    Дата: {self._date:%d.%m.%Y %H:%M:%S}
    Картинка: {self._image}"""
