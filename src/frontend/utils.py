import re
import tkinter
from tkinter import filedialog
from typing import Literal

from ..backend.entities.cipher import Cipher
from ..backend.entities.cipher_breaker import CipherBreaker
from ..backend.entities.key import Key
from ..backend.entities.message import Message


def split_text_same_length_substrings(s: str, length: int = 5) -> str:
    result = [s[i:i + length] for i in range(0, len(s), length)]
    return ' '.join(result)


def clear_string(string: str) -> str:
    pattern = r'[^a-zа-яё]'
    cleared_string = re.sub(pattern, '', string, flags=re.IGNORECASE)
    return cleared_string


def select_file(text_widget):
    filetypes = (
        ('text files', '*.txt'),
    )
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    with open(file_path, 'r', encoding='utf-8') as f:
        text_widget.delete('1.0', tkinter.END)
        text_widget.insert(tkinter.INSERT, ''.join(f.readlines()))


def get_result(action: Literal['encrypt', 'decrypt', 'break'], **data):
    language = data.get('language')
    key = data.get('key')
    message = data.get('message').lower()

    msg = Message(msg=message, language=language)

    if action in ['encrypt', 'decrypt']:
        k = Key(key=key.lower(), language=language)
        cipher = Cipher(message=msg, key=k, action=action)
        return (
            k.value,
            split_text_same_length_substrings(msg.value),
            split_text_same_length_substrings(cipher.value.value)
        )
    else:
        breaker = CipherBreaker(ciphertext=msg)
        return (
            breaker.key.value,
            split_text_same_length_substrings(msg.value),
            split_text_same_length_substrings(breaker.value.value)
        )
