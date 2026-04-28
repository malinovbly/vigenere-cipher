from tkinter import ttk
from typing import Literal

from ..enums import ButtonTexts
from ..utils import switch_page, select_file, open_window


def add_main_menu_button(root, frame, text, page_creator):
    button = ttk.Button(
        frame, text=text, padding=5,
        command=lambda: switch_page(root, page_creator)
    )
    button.pack(fill='x', padx=20, pady=5)


def add_get_result_button(
        root, frame, action: Literal['encrypt', 'decrypt', 'break'],
        result_window_creator, **data):
    button = ttk.Button(
        frame, text=ButtonTexts.Done,
        command=lambda: open_window(root, result_window_creator, True, action=action, **data)
    )
    button.pack(side='right', anchor='s', padx=5, pady=5)


def add_return_button(root, frame, prev_page_creator):
    button = ttk.Button(
        frame, text=ButtonTexts.Return,
        command=lambda: switch_page(root, prev_page_creator)
    )
    button.pack(side='right', anchor='s', padx=5, pady=5)


def create_browse_button(frame, entry, need_pack: bool = True):
    button = ttk.Button(frame, text=ButtonTexts.ChooseFile, command=lambda: select_file(entry))
    if need_pack:
        button.pack(side='right', padx=5, pady=5)
    return button
