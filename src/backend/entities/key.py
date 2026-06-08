from typing import Literal

from .base import Base
from ..exceptions import (
    ValueTypeException,
    ValueBlankException,
    ValueLetterCaseException,
    ValueContainsNonENGLetters,
    ValueContainsNonRUSLetters,
    ValueContainsOtherCharactersException
)


class Key(Base):

    _ERRORS_MAP = {
        **Base._ERRORS_MAP,
        ValueTypeException: 'Ключ должен быть строкой',
        ValueBlankException: 'Ключ не может быть пустым',
        ValueLetterCaseException: 'Ключ должен быть в нижнем регистре',
        ValueContainsNonENGLetters: 'Ключ должен состоять только из букв латиницы',
        ValueContainsNonRUSLetters: 'Ключ должен состоять только из букв кириллицы',
        ValueContainsOtherCharactersException: 'Ключ должен содержать только буквы'
    }

    def __init__(
            self,
            key: str,
            language: Literal['ru', 'en'] = 'ru'
    ) -> None:
        super().__init__(key, language)

    def __repr__(self):
        if len(self.value) > 10:
            representation = self.value[:5] + '...' + self.value[-5:]
        else:
            representation = self.value
        return f"Key(value='{representation}')"
