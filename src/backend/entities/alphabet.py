from typing import Literal


class Alphabet:

    _ALPHABETS = {
        'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
        'en': 'abcdefghijklmnopqrstuvwxyz'
    }

    _RU_LETTERS_FREQUENCIES = {
        'а': 0.062, 'б': 0.014, 'в': 0.038, 'г': 0.013, 'д': 0.025, 'е': 0.072, 'ж': 0.007, 'з': 0.016,
        'и': 0.062, 'й': 0.010, 'к': 0.028, 'л': 0.035, 'м': 0.026, 'н': 0.053, 'о': 0.090, 'п': 0.023,
        'р': 0.040, 'с': 0.045, 'т': 0.053, 'у': 0.021, 'ф': 0.002, 'х': 0.009, 'ц': 0.003, 'ч': 0.012,
        'ш': 0.006, 'щ': 0.003, 'ъ': 0.014, 'ы': 0.016, 'ь': 0.014, 'э': 0.003, 'ю': 0.006, 'я': 0.018
    }

    _EN_LETTERS_FREQUENCIES = {
        'a': 0.0796, 'b': 0.0160, 'c': 0.0284, 'd': 0.0401, 'e': 0.1286, 'f': 0.0262, 'g': 0.0199,
        'h': 0.0539, 'i': 0.0777, 'j': 0.0016, 'k': 0.0041, 'l': 0.0351, 'm': 0.0243, 'n': 0.0751,
        'o': 0.0662, 'p': 0.0181, 'q': 0.0017, 'r': 0.0683, 's': 0.0662, 't': 0.0972, 'u': 0.0248,
        'v': 0.0115, 'w': 0.0180, 'x': 0.0017, 'y': 0.0152, 'z': 0.0005
    }

    def __init__(self, language: Literal['ru', 'en']) -> None:
        if language not in self._ALPHABETS:
            raise ValueError(f'unsupported language: {language}')
        self._language = language
        self._alphabet = self._ALPHABETS.get(self._language)
        self._frequencies = self._RU_LETTERS_FREQUENCIES if self._language == 'ru' else self._EN_LETTERS_FREQUENCIES

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
    def frequencies(self) -> dict:
        return self._frequencies

    @property
    def char_to_index_dict(self):
        return {char: i for i, char in enumerate(self._alphabet)}

    @property
    def index_to_char_dict(self):
        return {i: char for i, char in enumerate(self._alphabet)}
