from typing import Literal

from .base import Base


class Message(Base):
    def __init__(self,
                 msg: str,
                 lang: Literal['ru', 'en'] = 'ru') -> None:
        super().__init__(msg, lang)

    def __repr__(self):
        return f"Message(value='{self.value}')"
