import re
from typing import Literal


class Base:
    def __init__(self,
                 value: str,
                 lang: Literal['ru', 'en'] = 'ru') -> None:
        self._langs = {
            'en': self.__contains_only_en_letters,
            'ru': self.__contains_only_ru_letters
        }
        if lang not in self._langs.keys():
            raise ValueError(f'Language must be one of [{', '.join(self._langs.keys())}]')
        value = value.lower()
        if self.__contains_only_letters(value) and self._langs[lang](value):
            value = self.__replace_specific_letter(value)
            self._value = value
            self._lang = lang

    @property
    def value(self) -> str:
        return self._value

    @property
    def language(self) -> str:
        return self._lang

    @staticmethod
    def __contains_only_letters(value) -> bool:
        if not isinstance(value, str):
            raise TypeError('Value must be a string')
        if value is None or len(value) < 1:
            raise ValueError('Value must not be empty')
        pattern = r'[^a-zа-яё]'
        clean_key = re.sub(pattern, '', value)
        if clean_key != value:
            raise ValueError('Value must only have letters')
        return True

    @staticmethod
    def __contains_only_en_letters(value) -> bool:
        pattern = r'[^a-z]'
        clean_key = re.sub(pattern, '', value)
        if clean_key != value:
            raise ValueError('Value must only have EN letters')
        return True

    @staticmethod
    def __contains_only_ru_letters(value) -> bool:
        pattern = r'[^а-яё]'
        clean_key = re.sub(pattern, '', value)
        if clean_key != value:
            raise ValueError('Value must only have RU letters')
        return True

    @staticmethod
    def __replace_specific_letter(value) -> str:
        letter_from = 'ё'
        letter_to = 'е'
        return re.sub(letter_from, letter_to, value)
