from datetime import datetime, timezone

class TextPost:
    """Класс текстового поста для блога"""

    db_name = "posts"

    def __init__(self, author, text):
        self._author = author
        self._text = text
        self._date = datetime.now(timezone.utc)
        self._save()

    def _save(self):
        print(f"Пост сохранен в базу данных {TextPost.db_name}.")

    @property
    def author(self): return self._author

    @property
    def text(self): return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._save()

    @property
    def date(self): return self._date
