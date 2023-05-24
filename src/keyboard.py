from src.item import Item


class LanguageMixin:
    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._name = name
        self._language = 'EN'

    @property
    def language(self):
        return self._language
