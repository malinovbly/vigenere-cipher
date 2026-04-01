import re
from typing import Literal


class Base:
    def __init__(self,
                 value: str,
                 language: Literal['ru', 'en'] = 'ru') -> None:
        self._supported_languages = {
            'en': self._contains_only_en_letters,
            'ru': self._contains_only_ru_letters
        }
        if language not in self._supported_languages.keys():
            raise ValueError(f'language must be one of [{', '.join(self._supported_languages.keys())}]')
        if self._contains_only_letters(value) and self._supported_languages[language](value):
            value = self._replace_specific_letter(value)
            self._value = value
            self._language = language

    @property
    def value(self) -> str:
        return self._value

    @property
    def language(self) -> Literal['ru', 'en']:
        return self._language

    @staticmethod
    def _contains_only_letters(value) -> bool:
        if not isinstance(value, str):
            raise TypeError('value must be a string')
        if value is None or len(value) < 1:
            raise ValueError('value must not be empty')
        pattern = r'[^a-zа-яё]'
        clean_key = re.sub(pattern, '', value, flags=re.IGNORECASE)
        if clean_key != value:
            raise ValueError('value must only have letters')
        clean_key = clean_key.lower()
        if clean_key != value:
            raise ValueError('value must be lowercase')
        return True

    @staticmethod
    def _contains_only_en_letters(value) -> bool:
        pattern = r'[^a-z]'
        clean_key = re.sub(pattern, '', value)
        if clean_key != value:
            raise ValueError('value must only have EN letters')
        return True

    @staticmethod
    def _contains_only_ru_letters(value) -> bool:
        pattern = r'[^а-яё]'
        clean_key = re.sub(pattern, '', value)
        if clean_key != value:
            raise ValueError('value must only have RU letters')
        return True

    @staticmethod
    def _replace_specific_letter(value) -> str:
        letter_from = 'ё'
        letter_to = 'е'
        return re.sub(letter_from, letter_to, value)
