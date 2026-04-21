from tkinter import ttk

from ..enums import ButtonTexts
from ..utils import switch_window, select_file


def add_main_menu_button(root, frame, text, window_creator):
    button = ttk.Button(
        frame, text=text, padding=5,
        command=lambda: switch_window(root, window_creator)
    )
    button.pack(fill='x', padx=20, pady=5)


def add_get_result_button(frame, **data):
    button = ttk.Button(frame, text=ButtonTexts.Done, command=lambda: print(data))
    button.pack(side='right', anchor='s', padx=5, pady=5)


def add_return_button(root, frame, main_window_creator):
    button = ttk.Button(
        frame, text=ButtonTexts.Return,
        command=lambda: switch_window(root, main_window_creator)
    )
    button.pack(side='right', anchor='s', padx=5, pady=5)


def create_browse_button(frame, entry, need_pack: bool = True):
    button = ttk.Button(frame, text=ButtonTexts.ChooseFile, command=lambda: select_file(entry))
    if need_pack:
        button.pack(side='right', padx=5, pady=5)
    return button
