from typing import Literal
from tkinter import filedialog
from tkinter import ttk

from .enums import ButtonTexts


def select_file(file_entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, 'end')
        file_entry.insert(0, file_path)


def switch_window(root, new_window_creator):
    root.winfo_children()[0].destroy()
    new_window_creator(root)


def destroy_child_by_name(parent, name: str):
    try:
        parent.nametowidget(name).destroy()
    except KeyError:
        pass


def get_result(
        action: Literal['encrypt', 'decrypt', 'break'],
        message: str = None, key: str = None, file_name: str = None):
    pass
