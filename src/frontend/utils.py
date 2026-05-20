import os
import sys
from typing import Literal
from tkinter import filedialog

from ..backend.entities.cipher import Cipher
from ..backend.entities.cipher_breaker import CipherBreaker
from ..backend.entities.key import Key
from ..backend.entities.message import Message
from ..backend.data_preprocess.data_preprocess import preprocess_file, clear_string
from .constants import ACTIONS, DATA_TO_SAVE, DATA_TO_CLEAR


def setup_hotkeys(window):
    def keypress(e):
        if e.keycode == 86 and e.keysym != 'v':
            _handle_clipboard(window, "<<Paste>>")
        elif e.keycode == 67 and e.keysym != 'c':
            _handle_clipboard(window, "<<Copy>>")
        elif e.keycode == 88 and e.keysym != 'x':
            _handle_clipboard(window, "<<Cut>>")

    window.bind("<Control-KeyPress>", keypress)


def _handle_clipboard(window, event_name):
    widget = window.focus_get()
    if hasattr(widget, 'event_generate'):
        widget.event_generate(event_name)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


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
        elif key in DATA_TO_CLEAR:
            if key == 'message':
                saved_data[key] = clear_string(value.get("1.0", "end-1c"))
            elif key == 'key':
                saved_data[key] = value.get()
            else:
                saved_data[key] = clear_string(value.get())
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


def split_text_same_length_substrings(s: str, length: int = 5) -> str:
    result = [s[i:i + length] for i in range(0, len(s), length)]
    return ' '.join(result)


def get_result(
        action: Literal['encrypt', 'decrypt', 'break'], **data):
    if action not in ACTIONS:
        raise ValueError('Невалидное действие!')

    language = data.get('radio_language')
    key = data.get('key')
    message_way = data.get('radio_message_way')

    if (key is None or len(key) == 0) and action != 'break':
        raise ValueError('Ключ не может быть пустым!')
    if language is None or len(language) == 0:
        raise ValueError('Не был выбран язык!')
    if message_way is None or len(message_way) == 0:
        raise ValueError('Не был выбран способ ввода сообщения!')

    if message_way == 'file':
        file_name = data.get('file_name')
        if file_name is None or len(file_name) == 0:
            raise ValueError('Несуществующее или невалидное имя файла!')
        text = preprocess_file(file_name)
        msg = Message(msg=text, language=language)
    elif message_way == 'text':
        message = data.get('message').lower()
        if message is None or len(message) == 0:
            raise ValueError('Сообщение не может быть пустым!')
        msg = Message(msg=message, language=language)
    else:
        raise ValueError('Не был выбран способ ввода сообщения!')

    if action in ['encrypt', 'decrypt']:
        k = Key(key=key.lower(), language=language)
        cipher = Cipher(message=msg, key=k, action=action)
        return k.value, split_text_same_length_substrings(cipher.value.value)
    else:
        breaker = CipherBreaker(ciphertext=msg)
        return breaker.key.value, split_text_same_length_substrings(breaker.value.value)
