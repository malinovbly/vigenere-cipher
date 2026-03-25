from typing import Literal

from .base import Base


class Key(Base):
    def __init__(self,
                 key: str,
                 lang: Literal['ru', 'en'] = 'ru') -> None:
        super().__init__(key, lang)

    def __repr__(self):
        return f"Key(value='{self.value}')"
