import re
from typing import Literal

from ..exceptions import (
    InvalidLanguageException,
    ValueTypeException,
    ValueBlankException,
    ValueLetterCaseException,
    ValueContainsNonENGLetters,
    ValueContainsNonRUSLetters,
    ValueContainsOtherCharactersException
)


class Base:

    _SUPPORTED_LANGUAGES = ['en', 'ru']
    _ERRORS_MAP = {
        InvalidLanguageException: 'Язык должен быть один из: ',
        ValueTypeException: 'Значение должно быть строкой',
        ValueBlankException: 'Значение не может быть пустым',
        ValueLetterCaseException: 'Значение должно быть в нижнем регистре',
        ValueContainsNonENGLetters: 'Значение должно состоять только из букв латиницы',
        ValueContainsNonRUSLetters: 'Значение должно состоять только из букв кириллицы',
        ValueContainsOtherCharactersException: 'Значение должно содержать только буквы'
    }

    def _raise_error(self, exception_class, suffix=''):
        base_message = self._ERRORS_MAP.get(exception_class, 'Неизвестная ошибка')
        raise exception_class(f'{base_message}{suffix}')

    def __init__(
            self,
            value: str,
            language: Literal['ru', 'en'] = 'ru'
    ) -> None:

        if language not in self._SUPPORTED_LANGUAGES:
            self._raise_error(
                InvalidLanguageException,
                ', '.join(self._SUPPORTED_LANGUAGES)
            )

        if self._contains_only_letters(value):
            if language == 'ru': self._contains_only_ru_letters(value)
            if language == 'en': self._contains_only_en_letters(value)
            self._value = self._replace_specific_letter(value)
            self._language = language

    @property
    def value(self) -> str:
        return self._value

    @property
    def language(self) -> Literal['ru', 'en']:
        return self._language

    def _contains_only_letters(self, value) -> bool:
        if not isinstance(value, str):
            self._raise_error(ValueTypeException)
        if value is None or len(value) < 1:
            self._raise_error(ValueBlankException)

        pattern = r'[^a-zа-яё]'
        clean_key = re.sub(pattern, '', value, flags=re.IGNORECASE)

        if clean_key != value:
            self._raise_error(ValueContainsOtherCharactersException)
        if clean_key.lower() != value:
            self._raise_error(ValueLetterCaseException)

        return True

    def _contains_only_en_letters(self, value) -> bool:
        pattern = r'[^a-z]'
        clean_key = re.sub(pattern, '', value)

        if clean_key != value:
            self._raise_error(ValueContainsNonENGLetters)

        return True

    def _contains_only_ru_letters(self, value) -> bool:
        pattern = r'[^а-яё]'
        clean_key = re.sub(pattern, '', value)

        if clean_key != value:
            self._raise_error(ValueContainsNonRUSLetters)

        return True

    @staticmethod
    def _replace_specific_letter(value) -> str:
        _from = 'ё'
        _to = 'е'
        return re.sub(_from, _to, value)
