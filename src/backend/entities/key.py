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
        ValueTypeException: 'Значение ключа должно быть строкой',
        ValueBlankException: 'Значение ключа не может быть пустым',
        ValueLetterCaseException: 'Значение ключа должно быть в нижнем регистре',
        ValueContainsNonENGLetters: 'Значение ключа должно состоять только из букв латиницы',
        ValueContainsNonRUSLetters: 'Значение ключа должно состоять только из букв кириллицы',
        ValueContainsOtherCharactersException: 'Значение ключа должно содержать только буквы'
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
