from typing import Literal

from .base import Base


class Message(Base):
    def __init__(self,
                 msg: str,
                 lang: Literal['ru', 'en'] = 'ru') -> None:
        super().__init__(msg, lang)

    def __repr__(self):
        if len(self.value) > 10:
            representation = self.value[:5] + '...' + self.value[-5:]
        else:
            representation = self.value
        return f"Message(value='{representation}')"
