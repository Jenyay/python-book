from abc import ABCMeta, abstractmethod

class TextMixin(metaclass=ABCMeta):
    def __init__(self, text):
        print("TextMixin.__init__()")
        self._text = text

    @abstractmethod
    def _save(self):
        ...

    @property
    def text(self): return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._save()


class ImageMixin(metaclass=ABCMeta):
    def __init__(self, image):
        print("ImageMixin.__init__()")
        self._image = image

    @abstractmethod
    def _save(self):
        ...

    @property
    def image(self): return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self._save()
