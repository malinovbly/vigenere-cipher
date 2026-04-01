from typing import Literal

from .base import Base


class Key(Base):
    def __init__(self,
                 key: str,
                 language: Literal['ru', 'en'] = 'ru') -> None:
        super().__init__(key, language)

    def __repr__(self):
        if len(self.value) > 10:
            representation = self.value[:5] + '...' + self.value[-5:]
        else:
            representation = self.value
        return f"Key(value='{representation}')"
