import tkinter
from tkinter import ttk

from .utils import switch_window
from .enums import ButtonTexts, LabelTexts
from .widgets.buttons import add_return_button, add_get_result_button
from .widgets.frames import (create_main_frame,
                             add_main_label_frame,
                             add_enter_key_frame,
                             add_choose_msg_way_frame)


def create_main_window(root):
    frame = ttk.Frame(root)
    frame.grid()
    for r in range(3):
        frame.rowconfigure(index=r, weight=1)
    frame.columnconfigure(index=0, weight=1)

    create_params = {
        'padding': 5
    }
    btn1 = ttk.Button(frame, text=ButtonTexts.EnterEncryptWindow,
                      command=lambda: switch_window(root, WINDOW_CREATORS['encrypt']), **create_params)
    btn2 = ttk.Button(frame, text=ButtonTexts.EnterDecryptWindow,
                      command=lambda: switch_window(root, WINDOW_CREATORS['decrypt']), **create_params)
    btn3 = ttk.Button(frame, text=ButtonTexts.EnterBreakWindow,
                      command=lambda: switch_window(root, WINDOW_CREATORS['break']), **create_params)

    grid_params = {
        'padx': 40,
        'ipady': 10,
        'column': 0,
        'sticky': tkinter.EW
    }
    btn1.grid(row=0, **grid_params)
    btn2.grid(row=1, **grid_params)
    btn3.grid(row=2, **grid_params)

    frame.pack(fill='both', expand=True)


def create_encrypt_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.EncryptWindow)
    add_enter_key_frame(frame)
    add_choose_msg_way_frame(frame)

    add_get_result_button(frame, action='encrypt')

    add_return_button(root, frame, create_main_window)


def create_decrypt_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.DecryptWindow)
    add_enter_key_frame(frame)
    add_choose_msg_way_frame(frame)

    add_get_result_button(frame, action='decrypt')

    add_return_button(root, frame, create_main_window)


def create_breaker_window(root):
    frame = create_main_frame(root)

    add_main_label_frame(frame, LabelTexts.BreakWindow)
    add_choose_msg_way_frame(frame)

    add_get_result_button(frame, action='break')

    add_return_button(root, frame, create_main_window)


WINDOW_CREATORS = {
    'encrypt': create_encrypt_window,
    'decrypt': create_decrypt_window,
    'break': create_breaker_window,
    'main': create_main_window
}
