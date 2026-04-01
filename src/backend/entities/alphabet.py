from typing import Literal


class Alphabet:

    _ALPHABETS = {
        'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
        'en': 'abcdefghijklmnopqrstuvwxyz'
    }

    def __init__(self, language: Literal['ru', 'en']) -> None:
        if language not in self._ALPHABETS:
            raise ValueError(f'unsupported language: {language}')
        self._language = language
        self._alphabet = self._ALPHABETS.get(self._language)

    def __len__(self) -> int:
        return len(self._alphabet)

    def __getitem__(self, index: int) -> str:
        return self._alphabet[index]

    @property
    def language(self) -> Literal['ru', 'en']:
        return self._language

    @property
    def alphabet(self) -> str:
        return self._alphabet

    @property
    def char_to_index_dict(self):
        return {char: i for i, char in enumerate(self._alphabet)}

    @property
    def index_to_char_dict(self):
        return {i: char for i, char in enumerate(self._alphabet)}
