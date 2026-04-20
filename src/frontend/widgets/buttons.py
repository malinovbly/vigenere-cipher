from tkinter import ttk

from ..enums import ButtonTexts
from ..utils import switch_window


def add_return_button(root, frame, main_window_creator):
    button = ttk.Button(frame,
                        command=lambda: switch_window(root, main_window_creator),
                        text=ButtonTexts.Return)
    button.pack(side='right')


def add_get_result_button(frame, **data):
    button = ttk.Button(frame, text=ButtonTexts.Done, command=lambda: print(data))
    button.pack(side='right', padx=5, pady=5)
