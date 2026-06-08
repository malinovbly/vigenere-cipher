from typing import Literal

from .base import Base
from ..exceptions import (
    ValueTypeException,
    ValueBlankException,
    ValueContainsNonENGLetters,
    ValueContainsNonRUSLetters
)


class Message(Base):

    _ERRORS_MAP = {
        **Base._ERRORS_MAP,
        ValueTypeException: 'Сообщение должно быть строкой',
        ValueBlankException: 'Сообщение не может быть пустым',
        ValueContainsNonENGLetters: 'Сообщение должно состоять только из букв латиницы',
        ValueContainsNonRUSLetters: 'Сообщение должно состоять только из букв кириллицы',
    }

    def __init__(
            self,
            msg: str,
            language: Literal['ru', 'en'] = 'ru'
    ) -> None:
        super().__init__(msg, language)

    def __repr__(self):
        if len(self.value) > 10:
            representation = self.value[:5] + '...' + self.value[-5:]
        else:
            representation = self.value
        return f"Message(value='{representation}')"
