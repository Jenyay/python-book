from basepost import BasePost
from mixins import TextMixin

class TextPost(BasePost, TextMixin):
    """Класс текстового поста для блога"""

    def __init__(self, author, text):
        print("TextPost.__init__()")
        BasePost.__init__(self, author)
        TextMixin.__init__(self, text)
        self._save()

    def _save(self):
        print("Текстовый пост сохранен.")

    def format(self):
        return f"""    Автор: {self._author}
    Дата: {self._date:%d.%m.%Y %H:%M:%S}
    ----
    {self._text}"""
