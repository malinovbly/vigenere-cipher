from typing import Literal, Optional

from pydantic import BaseModel


class SaveDataModel(BaseModel):
    action: Literal['encrypt', 'decrypt', 'break'] = 'encrypt'
    language: Literal['ru', 'en'] = 'ru'
    message: str = ''
    key: Optional[str] = ''
