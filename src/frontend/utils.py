from typing import Literal
from tkinter import filedialog

from ..backend.entities.cipher import Cipher
from ..backend.entities.cipher_breaker import CipherBreaker
from ..backend.entities.key import Key
from ..backend.entities.message import Message
from ..backend.file_preprocess.file_preprocess import preprocess_file
from .constants import (ACTIONS,
                        DATA_TO_SAVE,
                        RADIO_MESSAGE_WAY_VALUES,
                        RADIO_LANGUAGE_VALUES)


def select_file(file_entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, 'end')
        file_entry.insert(0, file_path)


def save_data(**data) -> dict:
    saved_data = dict()
    for key, value in data.items():
        if key == 'action':
            saved_data[key] = value
        elif key in DATA_TO_SAVE:
            saved_data[key] = value.get()
    return saved_data


def open_window(root, window_creator, need_save=False, **data):
    saved_data = dict()
    if need_save:
        saved_data = save_data(**data)

    window_creator(root, **saved_data)


def switch_page(root, page_creator, need_save=False, **data):
    saved_data = dict()
    if need_save:
        saved_data = save_data(**data)

    root.winfo_children()[0].destroy()
    page_creator(root, **saved_data)


def split_text_on_one_length_substrings(s: str, length: int = 5) -> str:
    result = [s[i:i + length] for i in range(0, len(s), length)]
    return ' '.join(result)



def get_result(
        action: Literal['encrypt', 'decrypt', 'break'], **data):
    if action not in ACTIONS:
        raise ValueError('Invalid action')

    language = data.get('radio_language')
    key = data.get('key')
    message_way = data.get('radio_message_way')

    if key is None and action != 'break':
        raise ValueError('Invalid key')
    if language is None:
        raise ValueError('Invalid radio_language')
    if message_way is None:
        raise ValueError('Invalid radio_message_way')

    if message_way == 'file':
        file_name = data.get('file_name')
        if file_name is None:
            raise ValueError('Invalid file_name')
        text = preprocess_file(file_name)
        msg = Message(msg=text, language=language)
    elif message_way == 'text':
        message = data.get('message')
        if message is None:
            raise ValueError('Invalid message')
        msg = Message(msg=message, language=language)
    else:
        raise ValueError('Invalid radio_message_way')

    if action in ['encrypt', 'decrypt']:
        k = Key(key=key, language=language)
        cipher = Cipher(message=msg, key=k, action=action)
        return k.value, split_text_on_one_length_substrings(cipher.value.value)
    else:
        breaker = CipherBreaker(ciphertext=msg)
        return breaker.key.value, split_text_on_one_length_substrings(breaker.value.value)
